# Integration acceptance checklist

Use the private setup record for account-specific connection results. This reusable public file deliberately contains no live account metadata, notebook IDs, source counts, device IDs, or private resource links.

| Component | Required evidence before claiming it works |
| --- | --- |
| Unified skill | Valid skill metadata and a saved installation |
| Google Drive | Authorized folder/file write followed by metadata or listing readback |
| Personal NotebookLM / Gemini Notebook | Actual notebook creation, source import, and processing checked separately |
| Obsidian | Valid linked notes and a vault opened on the user's actual device |
| Syncthing | PC-to-Android and Android-to-PC edits, conflicts, and restore checked on actual devices |
| ChatGPT/Claude direct device bridge | Authenticated scope-limited read/write test on the trusted host |
| Baidu Unlimited-OCR | Configured compatible model endpoint and page-level extraction verification |

The cloud repository checkout does not mount a local Windows folder. Repository edits do not prove that a Windows or Android installation has been configured. Follow `WINDOWS_SETUP.md` and `SYNCTHING_SETUP.md` for that device handoff.

Do not infer content ingestion from empty notebooks or folder creation. Later source files require screening and authorization appropriate to their destinations.
