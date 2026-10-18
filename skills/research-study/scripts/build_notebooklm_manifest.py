#!/usr/bin/env python3
"""Build a curated NotebookLM manifest and source guide from a source ledger."""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path


REQUIRED_COLUMNS = {
    "source_id",
    "title",
    "authors",
    "year",
    "source_type",
    "venue",
    "doi_or_url",
    "role",
    "decision",
    "rights",
    "external_upload",
    "local_path",
    "drive_path",
    "drive_file_url",
    "notebooklm_status",
}
OUTPUT_COLUMNS = [
    "source_id",
    "title",
    "authors",
    "year",
    "source_type",
    "venue",
    "doi_or_url",
    "role",
    "decision",
    "rights",
    "external_upload",
    "upload_state",
    "local_path",
    "drive_path",
    "drive_file_url",
    "notebooklm_status",
]


def csv_safe(value: str) -> str:
    cleaned = value.replace("\r", " ").replace("\n", " ").strip()
    if cleaned.startswith(("=", "+", "-", "@")):
        return "'" + cleaned
    return cleaned


def markdown_safe(value: str) -> str:
    return value.replace("|", "\\|").replace("\r", " ").replace("\n", " ").strip()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ledger", type=Path, help="Path to 03 Evidence Ledger.csv")
    parser.add_argument("--out-dir", type=Path, help="Output directory; defaults to Exports/NotebookLM")
    args = parser.parse_args()

    ledger = args.ledger.expanduser().resolve()
    out_dir = (args.out_dir or ledger.parent / "Exports" / "NotebookLM").expanduser().resolve()

    with ledger.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        missing = REQUIRED_COLUMNS - set(reader.fieldnames or [])
        if missing:
            parser.error("ledger is missing columns: " + ", ".join(sorted(missing)))
        rows = [{key: (value or "").strip() for key, value in row.items()} for row in reader]

    seen: set[str] = set()
    curated: list[dict[str, str]] = []
    for row in rows:
        source_id = row["source_id"]
        if not re.fullmatch(r"SRC-(?:[0-9]{4,}|[A-F0-9]{12})", source_id):
            parser.error(f"invalid source_id: {source_id or '<blank>'}")
        if source_id in seen:
            parser.error(f"duplicate source_id: {source_id}")
        seen.add(source_id)
        if row["decision"] not in {"accepted", "context", "rejected"}:
            parser.error(f"invalid decision for {source_id}: {row['decision']}")
        if row["decision"] == "rejected":
            continue
        if row["external_upload"] != "allowed":
            upload_state = "authorization_required"
        elif not row["drive_file_url"]:
            upload_state = "drive_upload_required"
        else:
            upload_state = "ready"
        curated.append({**row, "upload_state": upload_state})

    out_dir.mkdir(parents=True, exist_ok=True)
    manifest = out_dir / "source-manifest.csv"
    with manifest.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=OUTPUT_COLUMNS, extrasaction="ignore")
        writer.writeheader()
        for row in curated:
            writer.writerow({key: csv_safe(row.get(key, "")) for key in OUTPUT_COLUMNS})

    guide = out_dir / "00 Curated Source Guide.md"
    lines = [
        "# Curated source guide",
        "",
        "Generated from the topic evidence ledger. This file is an index, not authorization to upload source contents.",
        "",
        "| ID | Title | Role | Decision | Rights | Upload state | Drive file |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for row in curated:
        values = [
            row["source_id"],
            row["title"],
            row["role"],
            row["decision"],
            row["rights"],
            row["upload_state"],
            row["drive_file_url"] or row["drive_path"] or row["local_path"],
        ]
        lines.append("| " + " | ".join(markdown_safe(value) for value in values) + " |")
    guide.write_text("\n".join(lines) + "\n", encoding="utf-8")

    ready = sum(row["upload_state"] == "ready" for row in curated)
    print(f"Curated sources: {len(curated)}; ready for NotebookLM: {ready}; pending: {len(curated) - ready}")
    print(manifest)
    print(guide)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
