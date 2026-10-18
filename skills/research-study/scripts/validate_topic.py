#!/usr/bin/env python3
"""Validate a Study Memory Research topic workspace."""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path


REQUIRED_FILES = [
    "00 Topic Map.md",
    "01 Research Questions.md",
    "02 Concept Map.md",
    "03 Evidence Ledger.csv",
    "04 Contradictions.md",
    "05 Misconceptions.md",
    "06 Recall Queue.md",
]
REQUIRED_DIRS = ["Concepts", "Sources", "Sessions", "Exports/NotebookLM"]
ALLOWED_DECISIONS = {"accepted", "context", "rejected", "unreviewed"}
ALLOWED_UPLOAD = {"allowed", "not_allowed", "ask"}
ALLOWED_NOTEBOOKLM = {"not_added", "added", "synced", "excluded"}


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), [
            {key: (value or "").strip() for key, value in row.items()} for row in reader
        ]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("topic_dir", type=Path)
    args = parser.parse_args()
    topic_dir = args.topic_dir.expanduser().resolve()
    errors: list[str] = []
    warnings: list[str] = []

    for relative in REQUIRED_FILES:
        if not (topic_dir / relative).is_file():
            errors.append(f"missing file: {relative}")
    for relative in REQUIRED_DIRS:
        if not (topic_dir / relative).is_dir():
            errors.append(f"missing directory: {relative}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    fields, rows = read_csv(topic_dir / "03 Evidence Ledger.csv")
    needed = {
        "source_id",
        "decision",
        "exclusion_reason",
        "external_upload",
        "drive_file_url",
        "notebooklm_status",
    }
    for name in sorted(needed - set(fields)):
        errors.append(f"ledger missing column: {name}")

    seen: set[str] = set()
    curated_ids: set[str] = set()
    for index, row in enumerate(rows, start=2):
        source_id = row.get("source_id", "")
        if not re.fullmatch(r"SRC-(?:[0-9]{4,}|[A-F0-9]{12})", source_id):
            errors.append(f"ledger row {index}: invalid source_id {source_id or '<blank>'}")
        elif source_id in seen:
            errors.append(f"ledger row {index}: duplicate source_id {source_id}")
        seen.add(source_id)

        decision = row.get("decision", "")
        if decision not in ALLOWED_DECISIONS:
            errors.append(f"ledger row {index}: invalid decision {decision or '<blank>'}")
        elif decision == "rejected" and not row.get("exclusion_reason", ""):
            errors.append(f"ledger row {index}: rejected source lacks exclusion_reason")
        else:
            if decision in {"accepted", "context"}:
                curated_ids.add(source_id)

        upload = row.get("external_upload", "")
        if upload not in ALLOWED_UPLOAD:
            errors.append(f"ledger row {index}: invalid external_upload {upload or '<blank>'}")
        elif decision in {"accepted", "context"} and upload == "allowed" and not row.get("drive_file_url", ""):
            warnings.append(f"ledger row {index}: authorized curated source lacks drive_file_url")

        notebooklm_status = row.get("notebooklm_status", "")
        if notebooklm_status not in ALLOWED_NOTEBOOKLM:
            errors.append(
                f"ledger row {index}: invalid notebooklm_status {notebooklm_status or '<blank>'}"
            )

    manifest_path = topic_dir / "Exports" / "NotebookLM" / "source-manifest.csv"
    if manifest_path.is_file():
        _, manifest_rows = read_csv(manifest_path)
        manifest_ids = {row.get("source_id", "").lstrip("'") for row in manifest_rows}
        extra = manifest_ids - curated_ids
        missing = curated_ids - manifest_ids
        if extra:
            errors.append("manifest contains non-curated IDs: " + ", ".join(sorted(extra)))
        if missing:
            warnings.append("manifest is stale; missing IDs: " + ", ".join(sorted(missing)))
    elif curated_ids:
        warnings.append("curated sources exist but source-manifest.csv has not been built")

    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")
    if errors:
        return 1
    print(f"OK: {topic_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
