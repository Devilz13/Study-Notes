# Integration status

Checked on: 2026-08-26

| Backend | Current state | What is prepared | Remaining handoff |
| --- | --- | --- | --- |
| GitHub repository | Read/write repository branch | PDFs, topic workspaces, manifests, notes, and validation scripts | Merge the prepared branch after review |
| Google Drive | Manual handoff | Canonical Drive folder layout, filenames, and upload manifests | Authorize and upload the four source folders to a private Drive location; record stable links |
| Personal NotebookLM | Manual handoff | Four source selections and four ready-to-paste processing prompts | Create one notebook per subject, add its curated source, and return the `CHATGPT HANDOFF` section |
| Obsidian | Prepared plain-file vault | Linked topic maps, concept seeds, source notes, recall queues, and cross-topic index | Open `Obsidian Vault/` locally and let Syncthing replicate it |
| Syncthing | Configuration prepared | `.stignore`, topology, validation checklist, and conflict policy | Install/configure Syncthing on the host/PC and Syncthing-Fork on Android |
| ChatGPT-to-vault bridge | Disconnected | Narrow recommended tool surface documented below | Deploy an authenticated MCP service on the trusted host when direct ChatGPT writes are desired |

## Automation level

The repository is NotebookLM-ready but the external backends are not yet connected. No Drive upload, NotebookLM import, or Obsidian sync is claimed as completed.

For a later ChatGPT-first bridge, expose only topic-scoped operations such as reading a topic map, writing one note, applying a guarded patch, listing conflicts, and checking sync status. Do not expose arbitrary host filesystem access.
