# Integration requirements

## Core distinction

A skill tells ChatGPT how to perform a workflow. A connector or MCP server gives ChatGPT authenticated tools that can read or change an external system. Do not call this system fully connected until the tools below exist and pass read/write tests.

## Required connections

| Backend | Required for full automation | Without it |
| --- | --- | --- |
| Google Drive | Connected Drive capability or Google Drive API exposed through authenticated MCP tools | Prepare filenames, folders, and manifests for manual upload |
| Personal Gemini Notebook / NotebookLM | No assumed API; use an explicitly requested authenticated browser action or manual handoff | Produce exact source selection and ready-to-paste prompt |
| Gemini Notebook Enterprise | Google Cloud project, license, IAM, and its notebook/source REST APIs exposed through MCP tools | Do not claim programmatic notebook creation or source processing |
| Obsidian | MCP tools that read/write the vault's Markdown files on a trusted host | Produce complete Markdown updates for manual import |
| ChatGPT | Installed plugin or developer-mode connection to the remote MCP server | The skill remains instructions only |

Official OpenAI guidance permits remote MCP servers to connect ChatGPT to external data and actions. The server must be reachable through public HTTPS or a supported secure tunnel and should use authentication for private data.

Official references:

- <https://developers.openai.com/api/docs/mcp>
- <https://developers.openai.com/plugins/deploy/connect-chatgpt>

## NotebookLM modes

Do not assume that consumer NotebookLM exposes the same programmable surface as Gemini Notebook Enterprise. Google documents notebook creation, source management, file upload, retrieval, and deletion APIs for Gemini Notebook Enterprise; some source API features are Preview or Pre-GA and require a Google Cloud project, IAM, and licensing. Verify current availability before implementation.

Official references:

- <https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/api-notebooks>
- <https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/api-notebooks-sources>

For the personal product, treat browser or manual handoff as the supported path unless a current official API is verified.

## Obsidian connection options

### Recommended free agent path: plain vault plus Syncthing

1. Keep the canonical plain-file vault on a trusted, usually-on PC, NAS, or server.
2. Run a narrow authenticated MCP service against only that vault folder.
3. Expose topic-scoped read, write, guarded patch, conflict, and sync-status tools.
4. Let Syncthing replicate the vault to PC and Syncthing-Fork replicate it to an Android-local folder that Obsidian can open.
5. Keep Google Drive source binaries outside the vault.

Do not use the official Obsidian Headless client for this free path. It is a command-line client for Obsidian services and its vault synchronization uses Obsidian Sync. The MCP service here is a custom headless vault bridge over ordinary Markdown files, not Obsidian Headless.

Official and project references:

- <https://obsidian.md/help/headless>
- <https://obsidian.md/help/sync-notes>
- <https://github.com/researchxxl/syncthing-android>
- <https://docs.syncthing.net/users/syncing.html>

### Alternative plugin paths

Self-hosted LiveSync supports CouchDB, object storage, and WebRTC across Obsidian-compatible platforms. Remotely Save supports mobile and several free-capable backends, including WebDAV and S3-compatible storage. Prefer these only when their in-app sync behavior is more important than having the MCP host operate directly on a normal synchronized vault directory. Never combine them with Syncthing or Obsidian Sync on the same live vault.

Project references:

- <https://github.com/vrtmrz/obsidian-livesync>
- <https://github.com/remotely-save/remotely-save>

### Google Drive vault path

Google Drive can be the vault's single sync engine, but Obsidian does not officially support it as a native vault sync service. On PC, Drive for desktop keeps the vault folder locally available. On Android, a third-party folder-sync app or Obsidian plugin must mirror the Drive folder into a local directory that Obsidian can open. The Google Drive Android app alone is not the agent/vault bridge.

If this path is chosen:

1. Store the vault in a dedicated Drive folder separate from source binaries.
2. Keep the entire vault locally available on PC.
3. Configure one bidirectional Android folder pair from Drive to a local Obsidian vault folder.
4. Let the MCP server use the Google Drive API or a trusted local Drive mirror to read and write Markdown.
5. Prevent concurrent edits and keep independent backups.
6. Do not also enable Obsidian Sync for the same vault.

Official reference: <https://obsidian.md/help/sync-notes>

## Minimum MCP tool surface

Expose narrow, auditable tools rather than arbitrary filesystem or account access:

- `drive_store_source`
- `drive_get_source_link`
- `notebook_create_or_get`
- `notebook_add_sources`
- `notebook_run_study_task`
- `obsidian_read_topic`
- `obsidian_write_note`
- `obsidian_apply_patch`
- `obsidian_sync_status`
- `obsidian_list_conflicts`

Mark reads and writes correctly, require confirmation for consequential writes, validate topic-local paths, and return stable identifiers so ChatGPT can verify every mutation.
