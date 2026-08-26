# NotebookLM workflow

Create four personal NotebookLM notebooks, not one mixed notebook:

1. Networking Fundamentals
2. Computing Research Methods
3. Systems Analysis and Design
4. C++ Programming

For each notebook:

1. Upload or import only the files listed in that subject's `source-manifest.csv` after confirming authorization.
2. Add `00 Curated Source Guide.md` as a source so NotebookLM sees the source role and upload state.
3. Paste the subject's `01 NotebookLM Processing Prompt.md`.
4. Ask follow-up questions within that subject notebook.
5. Copy only the final `CHATGPT HANDOFF` section back into ChatGPT.
6. Verify cited passages before promoting candidate concepts from `seed` to `developing` in Obsidian.

NotebookLM output is source-grounded synthesis, not canonical memory. Obsidian becomes canonical only after source checking, preserved locators, and an explicit note update.

## Drive layout

Mirror `Academic Source Library/` into a private Drive folder with the same structure. When Drive links exist, add them to each topic's `03 Evidence Ledger.csv`, rebuild the manifests, and update the corresponding source note.

Do not put the live Obsidian vault inside this Drive source folder.
