#!/usr/bin/env python3
"""Create a non-destructive Obsidian topic workspace."""

from __future__ import annotations

import argparse
import csv
import hashlib
import re
import unicodedata
from datetime import date
from pathlib import Path


LEDGER_COLUMNS = [
    "source_id",
    "title",
    "authors",
    "year",
    "source_type",
    "venue",
    "doi_or_url",
    "peer_reviewed",
    "relevance",
    "method_fit",
    "credibility_notes",
    "bias_notes",
    "role",
    "decision",
    "exclusion_reason",
    "rights",
    "external_upload",
    "local_path",
    "drive_path",
    "drive_file_url",
    "notebooklm_status",
    "checked_on",
]


def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    ascii_value = normalized.encode("ascii", "ignore").decode("ascii").lower()
    slug = re.sub(r"[^a-z0-9]+", "-", ascii_value).strip("-")
    if slug:
        return slug[:80].rstrip("-")
    digest = hashlib.sha256(value.encode("utf-8")).hexdigest()[:8]
    return f"topic-{digest}"


def note_templates(topic: str, slug: str, today: str) -> dict[str, str]:
    return {
        "00 Topic Map.md": f"""---
note_type: topic-map
topic: {slug}
created: {today}
last_verified:
---

# {topic}

## Scope

## Learning target

## Prerequisites

## Central concepts

## Open questions

## Contradictions

- [[04 Contradictions]]

## Misconceptions

- [[05 Misconceptions]]

## Due review

- [[06 Recall Queue]]
""",
        "01 Research Questions.md": f"""---
note_type: research-questions
topic: {slug}
created: {today}
---

# Research questions: {topic}

## Primary question

## Subquestions

## Explicit exclusions

## Evidence needed
""",
        "02 Concept Map.md": f"""---
note_type: concept-map
topic: {slug}
created: {today}
---

# Concept map: {topic}

Record meaningful directed relations in prose. Treat AI-generated maps as candidates until their source links are verified.

## Prerequisite relations

## Causal or mechanistic relations

## Contrasts and boundary cases

## Unverified candidate edges
""",
        "04 Contradictions.md": f"""---
note_type: contradictions
topic: {slug}
created: {today}
---

# Contradictions: {topic}

For each contradiction, record both claims, source IDs and locators, conditions that may reconcile them, and current resolution status.
""",
        "05 Misconceptions.md": f"""---
note_type: misconceptions
topic: {slug}
created: {today}
---

# Misconceptions: {topic}

Record the incorrect model, why it was tempting, corrective evidence, and a transfer question that distinguishes the models.
""",
        "06 Recall Queue.md": f"""---
note_type: recall-queue
topic: {slug}
created: {today}
---

# Recall queue: {topic}

| Prompt | Concept | Difficulty | Last attempt | Result or error | Next review | Evidence to revisit |
| --- | --- | --- | --- | --- | --- | --- |
""",
        "Concepts/_Concept Note Template.md": f"""---
note_type: concept
topic: {slug}
status: seed
confidence: low
source_ids: []
last_verified:
next_review:
---

# Concept

## Proposition

## Explanation

## Evidence and locators

## Boundaries or failure cases

## Links

## Recall prompts
""",
        "Sources/_Source Note Template.md": f"""---
note_type: source
topic: {slug}
source_id:
decision:
source_type:
checked_on:
doi_or_url:
drive_file_url:
notebooklm_status: not_added
---

# Source

## Identity and role

## Drive file

## Claims and locators

## Method and limitations

## What this source cannot support
""",
        "Sessions/_Session Note Template.md": f"""---
note_type: study-session
topic: {slug}
date:
---

# Study session

## Outcome

## Notes changed

## Belief updates

## Unresolved questions

## Next action
""",
        "Exports/NotebookLM/00 Curated Source Guide.md": f"""# Curated source guide: {topic}

Generated from `03 Evidence Ledger.csv`. Rebuild after source decisions change.
""",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("vault", type=Path, help="Obsidian vault root")
    parser.add_argument("topic", help="Human-readable topic title")
    parser.add_argument("--slug", help="Optional folder slug")
    parser.add_argument("--dry-run", action="store_true", help="Show the target without writing")
    args = parser.parse_args()

    vault = args.vault.expanduser().resolve()
    slug = args.slug or slugify(args.topic)
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]{0,79}", slug):
        parser.error("slug must contain lowercase letters, digits, and hyphens only")

    topic_dir = vault / "Topics" / slug
    if args.dry_run:
        print(topic_dir)
        return 0

    for relative in ("Concepts", "Sources", "Sessions", "Exports/NotebookLM"):
        (topic_dir / relative).mkdir(parents=True, exist_ok=True)

    created: list[Path] = []
    skipped: list[Path] = []
    for relative, content in note_templates(args.topic, slug, date.today().isoformat()).items():
        target = topic_dir / relative
        if target.exists():
            skipped.append(target)
            continue
        target.write_text(content, encoding="utf-8")
        created.append(target)

    ledger = topic_dir / "03 Evidence Ledger.csv"
    if ledger.exists():
        skipped.append(ledger)
    else:
        with ledger.open("w", encoding="utf-8", newline="") as handle:
            csv.writer(handle).writerow(LEDGER_COLUMNS)
        created.append(ledger)

    print(f"Topic workspace: {topic_dir}")
    print(f"Created: {len(created)}; preserved existing: {len(skipped)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
