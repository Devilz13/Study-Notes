# NotebookLM workflow

## Role in the system

Use NotebookLM as the source-grounded processing engine for studying and teaching one topic. Keep ChatGPT as the user-facing input and output surface: ChatGPT selects the processing task, supplies or prepares the prompt, retrieves the relevant result, verifies it, and presents it to the learner. Google Drive holds the canonical source files. Obsidian holds the durable memory because its notes are locally accessible, linkable, and independently syncable.

Before processing, determine the NotebookLM mode. Use verified Gemini Notebook Enterprise APIs for programmatic automation. For the personal product, use an explicitly requested authenticated browser action or manual prompt/source handoff unless a current official API is available. Never describe a generated prompt as a completed NotebookLM run.

## Source preparation

1. Rebuild the manifest from `03 Evidence Ledger.csv`.
2. Include only `accepted` and `context` sources.
3. Store authorized files in Google Drive with stable filenames beginning with their source IDs.
4. Record `drive_path` and `drive_file_url` in the evidence ledger.
5. Keep a `00 Curated Source Guide.md` in the Drive topic folder so source roles and exclusions remain visible.
6. Preview files marked `licensed`, `personal`, `confidential`, or `unknown`; obtain explicit authorization before external upload.

NotebookLM accepts Markdown, PDF, DOCX, TXT, CSV, Google Docs, Slides, Sheets, images, audio, web URLs, ePub, and other supported inputs. Verify current support in Google's official help before relying on a format. Google Drive imports can auto-update, while ordinary uploaded files may behave as point-in-time copies.

Official reference: <https://support.google.com/gemininotebook/answer/16215270>

## Recommended Drive library

Use a dedicated Google Drive folder outside the Obsidian vault:

```text
Academic Source Library/
└── <topic-slug>/
    ├── 00 Curated Source Guide.md
    ├── source-manifest.csv
    ├── Sources/
    │   ├── Accepted/
    │   └── Context/
    └── NotebookLM Outputs/
        ├── Study/
        └── Teaching/
```

Store PDFs, slide decks, documents, datasets, images, and other authorized files under `Sources/`. Use `NotebookLM Outputs/` only for outputs deliberately exported from NotebookLM. Do not let NotebookLM or Drive write directly into the live Obsidian vault.

## Analysis sequence

From ChatGPT, direct NotebookLM to work only from selected topic sources and to cite its evidence. Useful prompts include:

1. `Map the central concepts and directed relationships. For every relationship, cite the source and state whether it is explicit or inferred.`
2. `Build a claim matrix: claim, supporting sources, contradicting sources, conditions, evidence type, and unresolved uncertainty.`
3. `Find terminology collisions where different sources use the same term differently or different terms for the same construct.`
4. `Identify the smallest prerequisite chain needed to explain this topic to a learner at <level>. Cite each step.`
5. `Generate difficult retrieval and application questions. Do not reveal the answer until after the question set.`
6. `List claims that appear in only one source, claims based on weak evidence, and questions the current source set cannot answer.`

Treat mind maps and generated notes as candidate structures. Verify edges, claims, and quotations against the cited passages before moving them into Obsidian.

## Personal NotebookLM master processing prompt

Use the following prompt in a personal NotebookLM notebook **after** its accepted and contextual Drive sources have been added. Replace only the bracketed fields. This is a manual handoff artifact, not evidence that ChatGPT has run or retrieved NotebookLM.

```text
You are the source-grounded study and teaching processor for this notebook.

Topic: [TOPIC]
Learner and current level: [LEARNER / LEVEL]
Goal: [EXAM, SKILL, OR TEACHING OUTCOME]
Time available: [TIME]
Desired teaching style: [e.g. concise, worked examples first, beginner-friendly]

Use only the sources in this notebook. Do not add outside facts, examples, citations, or assumed background knowledge. If the source set cannot answer something, say "not established by the notebook sources" and identify the missing source or evidence needed.

Evidence rules
- Cite every substantive claim with the source title. Include page, slide, section, figure, table, or timestamp when NotebookLM makes it available.
- Label each relationship or conclusion as Direct (explicitly stated), Derived (a careful inference from cited material), or Uncertain (insufficient, conflicting, or ambiguous evidence).
- Preserve disagreement: show conflicting claims side by side with their sources and conditions. Never force a single answer merely to make a clean summary.
- Separate source claims from your explanation for the learner. Do not invent quotations, locations, calculations, definitions, or references.
- Prefer the sources marked as accepted in "00 Curated Source Guide" where that guide is present. Treat contextual sources as background and identify when you use one.

Produce the following in order.

1. SOURCE COVERAGE
   - List the sources used, their role, and the important questions they cannot answer.
   - State any apparent source-quality, date, scope, terminology, or evidence limitations.

2. TEACHABLE KNOWLEDGE MAP
   - Give 8–20 atomic concepts, each with: concept, one-sentence meaning, prerequisites, and cited source(s).
   - Give directed links in this form: [A] --relationship--> [B] | Direct/Derived/Uncertain | citations.
   - Identify terminology collisions, prerequisites, dependencies, and common look-alikes.

3. EXAM-READY EXPLANATION
   - Explain the topic from first principles at the stated learner level.
   - Use a layered format: 60-second overview; core explanation; worked example(s) grounded in the sources; limits and exceptions.
   - Use analogies only when useful. Label their limit so the analogy is not mistaken for evidence.

4. MISCONCEPTIONS, CONTRADICTIONS, AND GAPS
   - List likely misconceptions or confusing distinctions, how to correct each, and citations.
   - List conflicts or unresolved questions: claim A, claim B, source(s), applicable conditions, and what would resolve them.

5. ACTIVE RECALL AND TEACHING
   - Create 10 retrieval questions ordered from foundational to application. Do not reveal answers until a separate answer key.
   - Then create the answer key with citations and brief explanations.
   - Create one 10-minute teaching outline and one 60-second short-form explanation, both tied to the sources.

6. CHATGPT HANDOFF — output this final section as compact Markdown, ready to copy into ChatGPT
   # NotebookLM Handoff: [TOPIC]
   ## Source coverage and confidence
   ## Verified core claims
   - Claim | Direct/Derived/Uncertain | sources and locators | caveat
   ## Atomic concepts and links
   - Concept: ...
   - Link: A --relationship--> B | label | citations
   ## Misconceptions / contradictions / open questions
   ## Recall queue
   - Question | answer | citations | difficulty
   ## Proposed Obsidian notes
   - Filename | purpose | outgoing [[links]] | source titles / Drive source IDs
   ## What ChatGPT should verify next

Keep the CHATGPT HANDOFF factual, compact, and traceable. Do not include uncited material in it.
```

Paste the `CHATGPT HANDOFF` back into ChatGPT for source checking, conversion into atomic Obsidian notes, and scheduling of recall. Keep its source labels and locators intact; ChatGPT must not treat the handoff as canonical until the relevant cited passages are verified.

## Study and teaching outputs

For studying, ask NotebookLM for layered explanations, prerequisite checks, cited summaries, flashcards, application questions, misconception diagnostics, audio/video overviews, and a weak-area list. For teaching, ask for learning objectives, a lesson sequence, worked examples, analogies with stated limits, checks for understanding, assessment questions, and both short-form and full-lesson outlines. Keep generated teaching material tied to the selected sources and the intended learner level.

NotebookLM remains the processor rather than the main user interface: bring its relevant generated summaries and teaching aids back through ChatGPT. They do not automatically become canonical notes. Export only useful outputs, verify material claims, and then distill them into Obsidian.

## Return to Obsidian

For each retained NotebookLM insight:

- label its origin `NotebookLM synthesis`;
- attach the cited `source_id` values and locators;
- link the Obsidian source note back to `drive_file_url`;
- verify the cited passages;
- convert broad summaries into atomic concept notes;
- record contradictory evidence instead of forcing consensus;
- add unanswered questions to the topic map;
- add retrieval prompts to the recall queue.

Do not copy NotebookLM prose wholesale when a shorter, proposition-based note preserves the evidence more clearly.
