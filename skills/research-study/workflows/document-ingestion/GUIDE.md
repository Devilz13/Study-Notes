# Document Ingestion

Produce a canonical Markdown representation and provenance record suitable for reading, review, literature synthesis, and numerical checks.

## Decide the Extraction Path

1. Inspect the file type, page count, text layer, layout, language, tables, equations, and image-only pages.
2. Use native extraction for born-digital PDF text, HTML, Markdown, Word, and LaTeX.
3. Use Baidu Unlimited-OCR for scanned or image-only content and pages whose native extraction is unusable.
4. For mixed documents, preserve native text and OCR only the affected pages or regions.

Do not route a normal born-digital PDF through OCR merely because OCR is available. Native text is normally more accurate for citations, symbols, ligatures, and copyable values.

## Confidentiality Gate

Treat unpublished papers, peer-review submissions, and proprietary documents as potentially confidential. Prefer a local Unlimited-OCR deployment. Do not send material to Baidu Cloud or another remote endpoint without explicit authorization and a policy check. Read [research-integrity.md](../../references/research-integrity.md).

## Unlimited-OCR

Read [baidu-unlimited-ocr.md](references/baidu-unlimited-ocr.md) before first setup or when changing backends. The bundled [unlimited_ocr_client.py](scripts/unlimited_ocr_client.py) sends pages to a configured Baidu Unlimited-OCR-compatible local endpoint and creates page files, a merged Markdown document, and a manifest.

If no compatible runtime or endpoint is configured, explain the requirement and ask the user whether to configure local processing or explicitly authorize the managed API. Do not silently substitute another OCR engine.

## Quality Assurance

Verify at least:

- source page count versus extracted page count;
- title, authors, abstract, section order, references, and appendix boundaries;
- a sample of equations, tables, superscripts, subscripts, minus signs, decimal points, and citation markers;
- reading order in multi-column pages;
- page markers and figure/table association;
- failed or suspicious pages in the OCR manifest.

Compare critical numerical evidence against the rendered page. Mark uncertain text instead of guessing. Preserve the original file and do not overwrite it.

## Output Contract

Return or create:

- canonical Markdown with source-page markers;
- individual page transcripts when OCR was used;
- a manifest naming the source, model, extraction route, page status, and file hash;
- an uncertainty log for unreadable or structurally ambiguous content.

Hand the canonical representation, original file, and uncertainty log to the next sub-skill. Downstream work must cite original page locations, not only transcript line numbers.
