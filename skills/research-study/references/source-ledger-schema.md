# Source ledger schema

Use `03 Evidence Ledger.csv` as the topic's source registry. Keep one row per distinct source.

## Required columns

| Column | Meaning |
| --- | --- |
| `source_id` | Stable topic-local ID such as `SRC-0001`; never renumber after use |
| `title` | Source title |
| `authors` | Author or responsible organization |
| `year` | Publication year when known |
| `source_type` | Paper, review, standard, textbook, lecture, dataset, webpage, video, or other |
| `venue` | Journal, publisher, institution, course, or site |
| `doi_or_url` | DOI, canonical URL, report number, or other stable locator |
| `peer_reviewed` | `yes`, `no`, or `unknown` |
| `relevance` | Short explanation of which topic question it serves |
| `method_fit` | Why its design can or cannot support the intended use |
| `credibility_notes` | Authority, limitations, corrections, retractions, or verification notes |
| `bias_notes` | Funding, conflicts, advocacy role, selection bias, or `none_identified` |
| `role` | `anchor`, `method`, `counterpoint`, `background`, `example`, or `assessment` |
| `decision` | `accepted`, `context`, or `rejected` |
| `exclusion_reason` | Required for rejected rows; otherwise blank |
| `rights` | `public`, `open_license`, `licensed`, `personal`, `confidential`, or `unknown` |
| `external_upload` | `allowed`, `not_allowed`, or `ask` |
| `local_path` | Optional path to a local source file; never fabricate it |
| `drive_path` | Topic-relative path in the Google Drive source library |
| `drive_file_url` | Stable access-controlled Drive link used by Obsidian and NotebookLM |
| `notebooklm_status` | `not_added`, `added`, `synced`, or `excluded` |
| `checked_on` | ISO date of the latest source-level check |

## Decision rules

- Accept a source because it serves a defined question and is fit for that claim, not because it looks academic.
- Use `context` for orientation and competing viewpoints that should remain visible but should not anchor a central claim.
- Reject duplicates while pointing `exclusion_reason` to the retained source ID.
- Treat preprints, vendor material, course notes, and tertiary summaries according to their actual evidentiary role rather than banning them categorically.
- Check retraction or correction status for sources that materially support high-stakes or central claims.
- Never infer permission to upload from the existence of a local copy. `external_upload` remains `ask` until authorization is known.

## Source note naming

Name source notes `Sources/SRC-0001 - Short Title.md`. Start each with properties for `source_id`, `decision`, `source_type`, `checked_on`, `doi_or_url`, `drive_file_url`, and `notebooklm_status`. Record page, section, figure, table, equation, or timestamp locators next to extracted claims. Keep Drive links access-controlled; linking never implies public sharing.


## Unified ecosystem additions

Scope legacy `SRC-0001` identifiers by topic. New bulk-file plans may use `SRC-` plus twelve uppercase hexadecimal hash characters. Use `unreviewed` for registered sources that have not passed screening; exclude these from NotebookLM manifests. The full SHA-256 remains the duplicate authority.
