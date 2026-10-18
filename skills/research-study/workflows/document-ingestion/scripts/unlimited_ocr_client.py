#!/usr/bin/env python3
"""Page-traceable client for a Baidu Unlimited-OCR SGLang endpoint.

This script does not install or launch the model. It converts PDF pages to
images when needed, submits each page or image to an OpenAI-compatible local
endpoint, and writes page Markdown, a merged document, and a JSON manifest.
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import json
import mimetypes
import os
import sys
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen


DEFAULT_URL = os.environ.get("UNLIMITED_OCR_URL", "http://127.0.0.1:10000")
DEFAULT_MODEL = os.environ.get("UNLIMITED_OCR_MODEL", "Unlimited-OCR")


@dataclass(frozen=True)
class Job:
    index: int
    label: str
    image_path: Path


@dataclass
class PageResult:
    index: int
    label: str
    status: str
    output_file: str | None
    attempts: int
    error: str | None = None


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def is_loopback_url(url: str) -> bool:
    host = (urlparse(url).hostname or "").lower()
    return host in {"127.0.0.1", "localhost", "::1"}


def encode_image(path: Path) -> dict:
    mime = mimetypes.guess_type(path.name)[0] or "image/png"
    payload = base64.b64encode(path.read_bytes()).decode("ascii")
    return {
        "type": "image_url",
        "image_url": {"url": f"data:{mime};base64,{payload}"},
    }


def parse_sse(response) -> str:
    chunks: list[str] = []
    for raw_line in response:
        if not raw_line:
            continue
        line = raw_line.decode("utf-8") if isinstance(raw_line, bytes) else raw_line
        if not line.startswith("data:"):
            continue
        data = line[len("data:") :].strip()
        if data == "[DONE]":
            break
        event = json.loads(data)
        delta = event.get("choices", [{}])[0].get("delta", {}).get("content", "")
        if delta:
            chunks.append(delta)
    return "".join(chunks)


def request_page(job: Job, args: argparse.Namespace, output_dir: Path) -> PageResult:
    payload = {
        "model": args.model,
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": args.prompt},
                    encode_image(job.image_path),
                ],
            }
        ],
        "temperature": 0,
        "skip_special_tokens": False,
        "images_config": {"image_mode": args.image_mode},
        "stream": True,
    }

    error: str | None = None
    for attempt in range(1, args.retries + 1):
        try:
            request = Request(
                f"{args.server_url.rstrip('/')}/v1/chat/completions",
                data=json.dumps(payload).encode("utf-8"),
                headers={"Content-Type": "application/json"},
                method="POST",
            )
            with urlopen(request, timeout=args.timeout) as response:
                text = parse_sse(response).strip()
            if not text:
                raise RuntimeError("OCR endpoint returned no text")
            output_name = f"page_{job.index:04d}.md"
            (output_dir / output_name).write_text(text + "\n", encoding="utf-8")
            return PageResult(job.index, job.label, "ok", output_name, attempt)
        except (HTTPError, URLError, TimeoutError, OSError, RuntimeError, ValueError, json.JSONDecodeError) as exc:
            error = f"{type(exc).__name__}: {exc}"
            if attempt < args.retries:
                time.sleep(min(2 ** (attempt - 1), 8))

    return PageResult(job.index, job.label, "failed", None, args.retries, error)


def collect_images(image_dir: Path) -> list[Job]:
    extensions = {".png", ".jpg", ".jpeg", ".webp", ".bmp", ".tif", ".tiff"}
    paths = sorted(
        path for path in image_dir.rglob("*") if path.is_file() and path.suffix.lower() in extensions
    )
    return [Job(index, str(path.relative_to(image_dir)), path) for index, path in enumerate(paths, 1)]


def render_pdf(pdf_path: Path, dpi: int, temp_dir: Path) -> list[Job]:
    try:
        import fitz
    except ImportError as exc:  # pragma: no cover - dependency error path
        raise RuntimeError("Install PyMuPDF to OCR PDF files.") from exc

    document = fitz.open(pdf_path)
    try:
        matrix = fitz.Matrix(dpi / 72, dpi / 72)
        jobs: list[Job] = []
        for index, page in enumerate(document, 1):
            image_path = temp_dir / f"source_page_{index:04d}.png"
            page.get_pixmap(matrix=matrix, alpha=False).save(image_path)
            jobs.append(Job(index, f"source page {index}", image_path))
        return jobs
    finally:
        document.close()


def merge_pages(results: Iterable[PageResult], output_dir: Path, merge_name: str) -> None:
    sections: list[str] = []
    for result in sorted(results, key=lambda item: item.index):
        sections.append(f"<!-- source-page: {result.index}; label: {result.label} -->")
        if result.status == "ok" and result.output_file:
            sections.append((output_dir / result.output_file).read_text(encoding="utf-8").rstrip())
        else:
            sections.append(f"[OCR FAILED: {result.error or 'unknown error'}]")
    (output_dir / merge_name).write_text("\n\n".join(sections) + "\n", encoding="utf-8")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run page-traceable OCR against a Baidu Unlimited-OCR endpoint."
    )
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--pdf", type=Path, help="PDF to render and OCR page by page")
    source.add_argument("--image-dir", type=Path, help="Directory of page images")
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--server-url", default=DEFAULT_URL)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--prompt", default="document parsing.")
    parser.add_argument("--image-mode", choices=("gundam", "base"), default="gundam")
    parser.add_argument("--dpi", type=int, default=300)
    parser.add_argument("--concurrency", type=int, default=2)
    parser.add_argument("--timeout", type=int, default=1200)
    parser.add_argument("--retries", type=int, default=3)
    parser.add_argument("--merge-name", default="document.md")
    parser.add_argument(
        "--allow-remote",
        action="store_true",
        help="Acknowledge that the endpoint is not loopback and may receive document data",
    )
    return parser


def validate_args(args: argparse.Namespace, parser: argparse.ArgumentParser) -> Path:
    source = args.pdf or args.image_dir
    assert source is not None
    source = source.resolve()
    if not source.exists():
        parser.error(f"Source does not exist: {source}")
    if args.pdf and not source.is_file():
        parser.error("--pdf must reference a file")
    if args.image_dir and not source.is_dir():
        parser.error("--image-dir must reference a directory")
    if args.dpi < 72 or args.dpi > 600:
        parser.error("--dpi must be between 72 and 600")
    if args.concurrency < 1 or args.retries < 1:
        parser.error("--concurrency and --retries must be positive")
    if not is_loopback_url(args.server_url) and not args.allow_remote:
        parser.error("Remote endpoint blocked; review confidentiality and pass --allow-remote explicitly")
    return source


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    source = validate_args(args, parser)
    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="unlimited_ocr_") as temp_name:
        jobs = (
            render_pdf(source, args.dpi, Path(temp_name))
            if args.pdf
            else collect_images(source)
        )
        if not jobs:
            parser.error("No pages or supported images found")

        results: list[PageResult] = []
        with ThreadPoolExecutor(max_workers=args.concurrency) as executor:
            futures = {
                executor.submit(request_page, job, args, output_dir): job for job in jobs
            }
            for future in as_completed(futures):
                result = future.result()
                results.append(result)
                print(f"[{result.status}] {result.label}", file=sys.stderr)

    merge_pages(results, output_dir, args.merge_name)
    manifest = {
        "engine": "baidu/Unlimited-OCR",
        "served_model": args.model,
        "source": str(source),
        "source_sha256": sha256_file(source) if source.is_file() else None,
        "page_count": len(results),
        "successful_pages": sum(item.status == "ok" for item in results),
        "settings": {
            "dpi": args.dpi if args.pdf else None,
            "image_mode": args.image_mode,
            "prompt": args.prompt,
        },
        "pages": [asdict(item) for item in sorted(results, key=lambda item: item.index)],
    }
    (output_dir / "ocr_manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    failures = [item for item in results if item.status != "ok"]
    print(
        f"OCR complete: {len(results) - len(failures)}/{len(results)} pages succeeded; "
        f"merged output: {output_dir / args.merge_name}",
        file=sys.stderr,
    )
    return 2 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
