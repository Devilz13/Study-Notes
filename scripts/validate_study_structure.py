#!/usr/bin/env python3
"""Validate source, NotebookLM, and Obsidian links in this repository."""

from __future__ import annotations

import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SUBJECTS = {
    "networking-fundamentals": "SRC-0001 - Network Fundamentals - CCNA Exploration Companion Guide.pdf",
    "computing-research-methods": "SRC-0001 - Researching Information Systems and Computing.pdf",
    "systems-analysis-and-design": "SRC-0001 - Systems Analysis and Design in a Changing World.pdf",
    "cpp-programming": "SRC-0001 - Starting Out with C++ - Ninth Global Edition.pdf",
}
REQUIRED_FILES = (
    "00 Topic Map.md", "01 Research Questions.md", "02 Concept Map.md",
    "03 Evidence Ledger.csv", "04 Contradictions.md", "05 Misconceptions.md",
    "06 Recall Queue.md",
)
WIKILINK = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")


def resolve_wikilink(source: Path, target: str, vault: Path) -> bool:
    target = target.strip()
    if target.startswith("../") or target.startswith("./"):
        return False
    if "/" in target:
        candidates = [vault / f"{target}.md"]
        topic_dir = next((parent for parent in source.parents if parent.parent.name == "Topics"), None)
        if topic_dir is not None:
            candidates.append(topic_dir / f"{target}.md")
        return any(candidate.is_file() for candidate in candidates)
    local = source.parent / f"{target}.md"
    if local.is_file():
        return True
    topic_dir = next((parent for parent in source.parents if parent.parent.name == "Topics"), None)
    if topic_dir is not None and (topic_dir / f"{target}.md").is_file():
        return True
    matches = list(vault.rglob(f"{target}.md"))
    return len(matches) == 1


def main() -> int:
    errors: list[str] = []
    vault = ROOT / "Obsidian Vault"
    for slug, pdf_name in SUBJECTS.items():
        topic = ROOT / "Obsidian Vault" / "Topics" / slug
        library = ROOT / "Academic Source Library" / slug
        for name in REQUIRED_FILES:
            if not (topic / name).is_file():
                errors.append(f"{slug}: missing {name}")
        pdf = library / "Sources" / "Accepted" / pdf_name
        if not pdf.is_file():
            errors.append(f"{slug}: missing canonical PDF {pdf_name}")
        ledger_path = topic / "03 Evidence Ledger.csv"
        if ledger_path.is_file():
            with ledger_path.open(encoding="utf-8-sig", newline="") as handle:
                rows = list(csv.DictReader(handle))
            if len(rows) != 1:
                errors.append(f"{slug}: expected one ledger source, found {len(rows)}")
            elif not re.fullmatch(r"SRC-[0-9]{4,}", rows[0].get("source_id", "")):
                errors.append(f"{slug}: invalid source_id")
            elif rows[0].get("local_path") != str(pdf.relative_to(ROOT)):
                errors.append(f"{slug}: ledger local_path does not match canonical PDF")
        manifest = library / "source-manifest.csv"
        if not manifest.is_file():
            errors.append(f"{slug}: missing source-manifest.csv")
        prompt = library / "01 NotebookLM Processing Prompt.md"
        if not prompt.is_file():
            errors.append(f"{slug}: missing NotebookLM prompt")
        source_notes = list((topic / "Sources").glob("SRC-*.md"))
        if len(source_notes) != 1:
            errors.append(f"{slug}: expected one concrete source note")
    cross_map = ROOT / "Obsidian Vault" / "Topics" / "cross-topic-index" / "00 Topic Map.md"
    if cross_map.is_file():
        text = cross_map.read_text(encoding="utf-8")
        for slug in SUBJECTS:
            if slug not in text:
                errors.append(f"cross-topic-index: missing link to {slug}")
    else:
        errors.append("cross-topic-index: missing topic map")
    root_pdfs = list(ROOT.glob("*.pdf"))
    if root_pdfs:
        errors.append("repository root still contains unclassified PDFs")
    for note in vault.rglob("*.md"):
        text = note.read_text(encoding="utf-8")
        for target in WIKILINK.findall(text):
            if not resolve_wikilink(note, target, vault):
                errors.append(f"{note.relative_to(ROOT)}: unresolved wikilink [[{target}]]")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("OK: four subject libraries, four NotebookLM packages, and five Obsidian topic maps")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
