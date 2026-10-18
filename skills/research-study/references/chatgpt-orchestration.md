# ChatGPT orchestration

## Ownership

| Layer | Role |
| --- | --- |
| ChatGPT | Primary input, user interface, orchestration, clarification, and final response |
| Academic Research | Evidence discovery, ingestion, reading, comparison, review, and source sieve |
| Google Drive | Canonical source files and stable links |
| NotebookLM | Source-grounded processing for study and teaching |
| Obsidian | Durable verified notes, maps, misconceptions, recall state, and session continuity |

The user should normally be able to say `start`, `add these files`, `teach me`, `make a lesson`, `quiz me`, `correct this`, or `continue` in ChatGPT. Translate that request into backend work without asking the user to operate every layer.

## Orchestration loop

1. Read the active topic state from the conversation and, when available, the topic's Obsidian map and evidence ledger.
2. Determine whether the request needs new research, existing-source processing, memory retrieval, memory update, or a combination.
3. Invoke only the needed Academic Research sub-skill and backend adapters.
4. Verify every external mutation by readback or observable state.
5. Return the requested answer, study interaction, or teaching artifact in ChatGPT.
6. Persist verified changes to Obsidian and source metadata to the evidence ledger when access exists.
7. State only material pending actions or evidence gaps.

## Backend adapters

### Google Drive

Use the connected Drive capability for source search, upload, organization, stable links, and readback when exposed. Preserve access controls. If write access is unavailable, prepare the accepted file list, canonical filenames, folder destinations, and ledger updates, then request one upload handoff.

### NotebookLM

Use an available NotebookLM integration or a user-requested authenticated browser action. Send only authorized curated sources or source selections. Retrieve the cited result back into ChatGPT. If no callable path exists, provide one ready-to-paste processing prompt and the precise source selection; resume in ChatGPT when the user returns the output.

### Obsidian

Use an authorized local, plugin, or service bridge to read and write Markdown notes when available. Preserve note identity and links. If no bridge exists, generate a deterministic Markdown patch or complete note file instead of pretending it was stored. Ask for one import/save handoff and continue from ChatGPT afterward.

## Confirmation and failure rules

- Distinguish `prepared`, `submitted`, `stored`, `processed`, `verified`, and `persisted` states.
- Do not collapse a prepared manifest into a claimed Drive upload, or a NotebookLM prompt into a claimed NotebookLM result.
- Do not call a generated Markdown note an Obsidian memory until it is written into the vault or the user confirms import.
- Preserve partial progress when one backend is unavailable; do not restart the research pipeline.
- Keep authentication and manual takeover requests narrow and provider-specific.

## Chat interaction modes

- **Research:** report the sieve, strongest evidence, disagreements, and gaps.
- **Study:** teach interactively, adapt to errors, and update misconceptions and recall prompts.
- **Teaching:** produce objectives, lesson sequence, examples, checks, and assessment material grounded in selected sources.
- **Maintenance:** add sources, refresh stale claims, repair links, or reconcile NotebookLM output with Obsidian memory.

In every mode, the user's working surface remains ChatGPT even though durable state lives elsewhere.
