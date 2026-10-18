# Free PC–Android Obsidian sync

Use Syncthing on Windows and a maintained Syncthing-Fork Android client. Use one sync engine for the live vault.

1. Make an independent backup of existing notes.
2. Create a live vault folder outside OneDrive and Google Drive. On Windows, `%USERPROFILE%\Obsidian\Samuel` is a suitable example.
3. Copy the contents of this repository's `Obsidian Vault/` into that live vault. Do not copy the entire repository or the source-file tree.
4. Open the live folder as a vault in Obsidian.
5. Install Syncthing from its official source on Windows. Install a currently maintained Android client from its verified project or F-Droid listing.
6. Pair the devices. Share only the live vault as Send & Receive.
7. Select an Android-local folder that Obsidian can open. Open it as the Android vault.
8. Apply the repository's `.stignore` rules on each device. Syncthing does not distribute `.stignore` automatically.
9. Enable versioning for received changes on the Windows copy. Keep an independent backup for local edits; synchronization and remote-change versioning do not replace one.
10. Create a disposable note on Windows. Verify it on Android. Edit it on Android. Verify that change on Windows.
11. Test a conflict and restoration using disposable notes. Preserve sync-conflict copies until reconciled.
12. Mark sync operational only after these checks pass on the actual devices.

Keep the user's existing `OneDrive\Documents\academic-research-skill` folder as a skill/source package if desired. Keep the live Syncthing vault outside OneDrive to avoid two synchronization engines writing it.

Keep PDFs and PowerPoint source files in the separate Google Drive hierarchy. The vault contains notes and stable source links.

Official references:

- <https://syncthing.net/downloads/>
- <https://docs.syncthing.net/users/ignoring.html>
- <https://docs.syncthing.net/users/versioning.html>
- <https://github.com/researchxxl/syncthing-android>
