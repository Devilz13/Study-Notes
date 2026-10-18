# Windows setup

The cloud session cannot write directly to the Windows folder supplied in chat. Use these steps on the PC.

1. Keep the existing `academic-research-skill` folder as a backup.
2. Open or clone the Study-Notes repository. Use the `study-memory-structure` branch while PR #1 is open.
3. Open a terminal in that checkout.
4. Run `python scripts/install_skill.py --agent both` to install the single merged skill for Claude Code and Codex.
5. If an earlier `research-study` installation exists, review it. Run the same command with `--replace` only when you want to replace it. The installer makes a sibling backup.
6. Remove or disable older standalone research/study skill installations after checking that the merged skill works. Do not remove your source files.
7. Read `docs/SYNCTHING_SETUP.md`. Keep the live vault outside OneDrive.
8. Open the live vault in Obsidian. Start with `00 Samuel Home.md`.
9. Add new study files to the Drive Samuel Study inbox, or the checkout's private local inbox. Ask either assistant to read README_AI.md before organization.

ChatGPT Work uses the installed personal skill in this account. A local installation does not automatically grant an ordinary Claude or ChatGPT chat access to the PC's files or external services.
