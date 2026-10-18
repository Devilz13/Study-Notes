# PC–Android synchronization

## Default free architecture

Use **Syncthing for the plain Markdown vault**, not Obsidian Sync or Google Drive. Keep source files in Google Drive as a separate store:

```text
ChatGPT MCP bridge ↔ always-on vault ↔ Syncthing ↔ PC vault
                               |
                               └─ Syncthing-Fork ↔ Android vault

Google Drive source library → NotebookLM processing
              └─ stable links → Obsidian source notes
```

Google Drive owns PDFs, PPT/PPTX, DOCX, datasets, images, and other sources. NotebookLM reads curated Drive sources and produces study and teaching analysis. Obsidian owns linked Markdown notes, verified summaries, concept maps, and recall memory. Syncthing replicates only the vault.

Run the ChatGPT-facing MCP bridge on the always-on PC, NAS, or server and allow it to access only the vault folder. This preserves ordinary files for direct, auditable reads and writes. It replaces the role previously assigned to Obsidian Headless; the official Headless client is for Obsidian services and requires Obsidian Sync for vault synchronization.

### Setup checklist

1. Create the canonical vault on an always-on trusted PC, NAS, or server. A desktop PC can fill this role if it is usually online.
2. Install Syncthing on that host and on the PC. Install the maintained community Syncthing-Fork on Android from F-Droid or its current verified release source.
3. Share one vault folder as `Send & Receive` to both devices. Open each local copy as a vault in Obsidian.
4. Give the MCP service a narrowly allowlisted path to the canonical host copy. Test create, read, patch, and sync-status operations with a disposable note.
5. Create `Academic Source Library/<topic-slug>/` in Google Drive outside the vault. Store authorized accepted/context source files there and link them from source notes.
6. Import the curated Drive files into NotebookLM and record their status in the evidence ledger.
7. Enable Syncthing file versioning on the always-on host and also keep an independent backup. Synchronization and conflict copies are not backups.
8. Verify PC→Android, Android→PC, MCP→both devices, deletion, conflict-copy, and restore behavior before migrating valuable notes.

Current references:

- <https://obsidian.md/help/sync-notes>
- <https://obsidian.md/help/headless>
- <https://github.com/researchxxl/syncthing-android>
- <https://docs.syncthing.net/users/syncing.html>
- <https://docs.syncthing.net/users/versioning.html>
- <https://docs.syncthing.net/users/ignoring.html>

## Free alternatives

| Method | PC–Android fit | Trade-off |
| --- | --- | --- |
| Syncthing plus Syncthing-Fork | Preferred | Free, peer-to-peer, and preserves normal Markdown files for MCP access; Android uses a community-maintained client and needs battery/background configuration |
| Self-hosted LiveSync | Strong Obsidian experience | Free and near-real-time with CouchDB, object storage, or WebRTC, but adds server/plugin complexity and is less direct for a filesystem-based MCP bridge |
| Remotely Save with WebDAV, S3, or Dropbox | Viable | Free backends exist and mobile is supported, but syncing is driven by the Obsidian plugin; Google Drive support is a paid feature and free conflict handling is basic |
| FolderSync plus Google Drive | Viable fallback | Mirrors Drive to an Android local folder, but Obsidian does not officially support Drive as a vault-sync service and simultaneous edits need care |
| Git | Backup/history supplement | Excellent history but mobile commits, pulls, and conflict resolution are not seamless enough for primary sync |

Use Self-hosted LiveSync when the user values in-app near-real-time synchronization more than direct plain-folder access by the MCP host. Use Remotely Save when the user already has reliable WebDAV or S3-compatible storage and accepts plugin-driven synchronization. Do not run any of these beside Syncthing on the same live vault.

If switching methods, make a complete backup, stop every writer using the old method, migrate a disposable copy first, then enable only the chosen method.

## Conflict policy

- Let synchronization finish before opening the same note on another device.
- Avoid editing the same file concurrently on PC and Android.
- Preserve conflict copies until changes are compared.
- Use `.stignore` for device-specific workspace state such as `.obsidian/workspace*.json`, cache data, and disposable temporary files. Decide deliberately whether to sync themes, snippets, plugins, and hotkeys.
- Use consistent filename casing across Windows, Android, and Linux hosts.
- Exempt Syncthing-Fork from Android battery optimization only to the extent needed for reliable background sync, and set network restrictions to the user's preference.
- Test the chosen method with a disposable vault before migrating valuable notes.
