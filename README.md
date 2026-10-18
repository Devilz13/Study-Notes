# Samuel Research and Study

One workflow for research, course-file organization, NotebookLM study, and Obsidian memory. It supports ChatGPT and Claude.

Start with [the shared AI operating guide](README_AI.md). The unified [research-study skill](skills/research-study/SKILL.md) includes the ten research workflows and the study-memory workflow.

## Structure

| Directory | Purpose |
| --- | --- |
| `Samuel/Samuel Work/` | Private-work template; no workplace records in this public repository |
| `Samuel/Samuel Study/ICT111/` | ICT111 source files, assignments, and lesson slides |
| `Samuel/Samuel Study/ICT201/` | ICT201 source files, assignments, and lesson slides |
| `Samuel/Samuel Study/Shared References/` | Four retained textbook libraries |
| `Obsidian Vault/` | Linked memory, module maps, concepts, and recall |

Both modules have `Assignments/Assignment 1/`, `Assignments/Assignment 2/`, and `Slides/Lesson1/` through `Slides/Lesson7/`. The module folders are ready for later files. Course titles and lesson content are not inferred.

## Use it

1. Open `Obsidian Vault/` in Obsidian.
2. Start at [Samuel Home](Obsidian%20Vault/00%20Samuel%20Home.md).
3. Add bulk study files to `Samuel/Samuel Study/00 Inbox/`, or use the matching private Drive folder.
4. Ask ChatGPT or Claude: "Use research-study. Read README_AI.md. Organize the new files by module, assignment, and lesson. Preserve originals. Update the source registry and linked memory."
5. Use [NotebookLM workflow](docs/NOTEBOOKLM_WORKFLOW.md) for notebook creation and source processing.
6. Use [Syncthing setup](docs/SYNCTHING_SETUP.md) for free PC–Android vault replication.

## Checks

```bash
python scripts/bootstrap_workspace.py
python scripts/rebuild_notebooklm_manifests.py
python scripts/validate_study_structure.py
python -m unittest discover -s tests -v
```

See [integration status](docs/INTEGRATION_STATUS.md) for what is connected and what still requires setup. Creating a folder or prompt does not run NotebookLM or configure the user's devices.

The four existing textbook files are retained. Their existing publication does not establish external-upload rights. Their evidence ledgers retain the previous authorization state. New raw files and assignments are private by default.
