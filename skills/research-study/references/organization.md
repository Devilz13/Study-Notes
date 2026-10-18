# Bulk organization rules

Read `ecosystem.json` and `README_AI.md` in the target repository. Use its paths as the layout authority.

1. Inventory the requested inbox. Record original path, SHA-256, file type, explicit module/assignment/lesson hints, and proposed destination.
2. Route by visible module code. Use a user-specified module unless the file contradicts it. Hold conflicting or absent module codes.
3. Use `Assignments/Assignment 1`, `Assignments/Assignment 2`, and `Slides/Lesson1` through `Slides/Lesson7` as initial folders. Add later numbers when supported. Do not invent lesson titles.
4. Route books used by several modules to `Shared References`. Do not guess module mappings from a book title.
5. Produce a plan before mutation. Apply authorized high-confidence entries by copy. Verify destination hashes. Keep originals until a separate deduplication or move request authorizes deletion.
6. Record exact duplicates and their intended module references. Keep changed editions and near-duplicates. Do not silently overwrite a collision.
7. Put uncertain cases in the review list. Inspect document headings if extraction is available. For unreadable scans use Baidu Unlimited-OCR, or leave `ocr_required` when unavailable.
8. Update source registries, NotebookLM packages, and Obsidian source notes after verified file writes. A copied file is unreviewed evidence until screened.
9. Keep intake reports and source binaries out of public commits by default. Commit public scaffolding and explicitly authorized sources only. Check staged paths before pushing.
10. Append a session record with counts for organized, duplicate, review, OCR, external handoff, and failed files.

## Copy-only helper

From a repository checkout:

```bash
python skills/research-study/scripts/organize_files.py plan --root . --inbox "Samuel/Samuel Study/00 Inbox" --output .local/intake-plan.json
python skills/research-study/scripts/organize_files.py apply --root . --plan .local/intake-plan.json
```

The first command performs no source-file writes. The second copies only entries marked `copy`. It rejects changed inputs, traversal, symlinks, and collisions. It does not authenticate, upload, extract text, infer page content, update evidence ledgers, or delete originals. Complete those steps through the appropriate workflow.
