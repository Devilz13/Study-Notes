# Obsidian memory model

## Topic structure

Keep each study topic under `Topics/<topic-slug>/`:

```text
00 Topic Map.md
01 Research Questions.md
02 Concept Map.md
03 Evidence Ledger.csv
04 Contradictions.md
05 Misconceptions.md
06 Recall Queue.md
Concepts/
Sources/
Sessions/
Exports/NotebookLM/
```

The topic map is the durable entry point for machines and manual inspection, but ChatGPT remains the learner's normal entry point. ChatGPT should read or update the topic map through an authorized bridge when available. It links to prerequisites, central concepts, open questions, contradictions, and due recall work.

## Note types

### Concept note

Represent one proposition, mechanism, definition, distinction, or procedure. Include:

```yaml
---
note_type: concept
topic: <topic-slug>
status: seed
confidence: low
source_ids: []
last_verified:
next_review:
---
```

Use `status: seed | developing | stable | superseded` and `confidence: low | medium | high`. Confidence reflects evidence fit and agreement, not writing polish.

Recommended sections:

- Proposition
- Explanation
- Evidence and locators
- Boundaries or failure cases
- Links
- Recall prompts

### Source note

Record bibliographic identity, source role, decision, the stable Google Drive file link, NotebookLM status, structured extracts with locators, methodological limitations, and claims the source can or cannot support. Keep source binaries in Drive, not in the vault.

### Session note

Record the learning objective, notes changed, belief updates, unresolved questions, and next action. Do not make session notes the only home of a durable concept.

## Link rules

- Link concepts because a meaningful relation exists, not because terms co-occur.
- State the relation in prose near the link: prerequisite, causes, contrasts with, measured by, example of, or exception to.
- Every central topic-map node must link to at least one concept note or a clearly labeled open question.
- Every canonical factual claim must cite one or more source IDs, unless clearly labeled as the learner's inference or question.
- Every source ID that represents a stored file should resolve through its source note to the access-controlled Drive file.
- Keep contradictions in their own note and link both claims and their supporting sources.

## Memory promotion

Promote a concept from `seed` to `developing` after source verification and from `developing` to `stable` after the learner can retrieve or apply it and material contradictions are represented. Mark it `superseded` when later evidence displaces it; retain the history and link to the replacement.

## Recall queue

Prefer prompts that require explanation, comparison, derivation, diagnosis, or transfer. Each row or task should contain:

- prompt;
- linked concept;
- difficulty;
- last attempt;
- result or error pattern;
- next review;
- evidence to revisit when the answer is disputed.

Use the learner's actual mistakes to update `05 Misconceptions.md` and generate later prompts.

## ChatGPT access

Conversation history is working context, not the canonical study memory. At the start of a continued topic, retrieve the topic map, due recall items, and relevant concept/source notes through an authorized Obsidian bridge when available. Persist verified changes after the interaction. If direct vault access is unavailable, generate the complete Markdown update and clearly leave it in `prepared` state until imported.
