#!/usr/bin/env python3
"""Rebuild NotebookLM manifests from every subject evidence ledger."""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SUBJECTS = (
    "networking-fundamentals",
    "computing-research-methods",
    "systems-analysis-and-design",
    "cpp-programming",
)
OUTPUT_COLUMNS = (
    "source_id", "title", "authors", "year", "source_type", "venue",
    "doi_or_url", "role", "decision", "rights", "external_upload",
    "upload_state", "local_path", "drive_path", "drive_file_url",
    "notebooklm_status",
)


def upload_state(row: dict[str, str]) -> str:
    if row["external_upload"] != "allowed":
        return "authorization_required"
    if not row["drive_file_url"]:
        return "drive_upload_required"
    return "ready"


def write_outputs(slug: str, rows: list[dict[str, str]]) -> None:
    curated = [row | {"upload_state": upload_state(row)} for row in rows if row["decision"] in {"accepted", "context"}]
    destinations = (
        ROOT / "Academic Source Library" / slug,
        ROOT / "Obsidian Vault" / "Topics" / slug / "Exports" / "NotebookLM",
    )
    for destination in destinations:
        destination.mkdir(parents=True, exist_ok=True)
        with (destination / "source-manifest.csv").open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(
                handle,
                fieldnames=OUTPUT_COLUMNS,
                extrasaction="ignore",
                lineterminator="\n",
            )
            writer.writeheader()
            writer.writerows(curated)
        guide = [
            "# Curated source guide", "",
            "Generated from the topic evidence ledger. This index is not authorization to upload source contents.", "",
            "| ID | Title | Role | Decision | Rights | Upload state | Drive file |",
            "| --- | --- | --- | --- | --- | --- | --- |",
        ]
        for row in curated:
            values = (
                row["source_id"], row["title"], row["role"], row["decision"],
                row["rights"], row["upload_state"],
                row["drive_file_url"] or row["drive_path"] or row["local_path"],
            )
            guide.append("| " + " | ".join(value.replace("|", "\\|") for value in values) + " |")
        (destination / "00 Curated Source Guide.md").write_text("\n".join(guide) + "\n", encoding="utf-8")
    print(f"{slug}: {len(curated)} curated source(s)")


def main() -> int:
    for slug in SUBJECTS:
        ledger = ROOT / "Obsidian Vault" / "Topics" / slug / "03 Evidence Ledger.csv"
        with ledger.open(encoding="utf-8-sig", newline="") as handle:
            rows = [{key: (value or "").strip() for key, value in row.items()} for row in csv.DictReader(handle)]
        write_outputs(slug, rows)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
