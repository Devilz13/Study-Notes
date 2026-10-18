# Research-to-memory pipeline

## Topic intake

Capture only decisions that change the work:

- topic and explicit exclusions;
- purpose: understand, pass an assessment, design a project, or conduct research;
- target depth and deadline;
- expected outputs and assessment format;
- prerequisite topics;
- supplied sources and whether external upload is permitted;
- existing Obsidian topic folder or NotebookLM notebook.

Split a topic when it requires substantially different research questions, source communities, or assessment outcomes. Link related topics from their maps rather than merging them into a catch-all folder.

## Evidence gates

### Gate 1: Discovery

Invoke the smallest applicable the research workflows in `research-study` path. Common paths are:

- document ingestion → paper reading;
- literature review → idea generation;
- paper reading → research-paper review;
- proof writing → paper writing.

Record every plausible candidate before judging it. Search failure does not prove that no evidence exists.

### Gate 2: Sieve

Deduplicate by DOI, stable URL, report number, or normalized title and year. Classify each source as:

- `accepted`: supports a question and is credible enough for direct use;
- `context`: useful orientation, terminology, history, or a competing position, but not strong enough for a central claim;
- `rejected`: duplicate, irrelevant, inaccessible, methodologically unsuitable, retracted, superseded, or otherwise excluded.

Do not reduce quality to one universal numeric score. Explain the decision using relevance, evidence type, method fit, authority, recency where relevant, conflicts of interest, and known corrections or retractions.

### Gate 3: Drive and NotebookLM

Store authorized accepted and contextual source files in the topic's Google Drive library, then record their stable Drive links and build the source manifest. Review confidentiality and rights before any upload. Import the curated Drive files into NotebookLM. Use NotebookLM to produce study and teaching analysis and locate patterns and tensions, not to replace source reading.

### Gate 4: Canonical memory

Promote a statement into an Obsidian concept note only when it has:

1. a clear proposition;
2. one or more traceable source IDs or an explicit `inference` label;
3. an appropriate confidence label;
4. links to the topic map and relevant neighboring concepts;
5. unresolved objections or boundary conditions where applicable.

## Session loop

At the start of a study session:

1. Receive the learner's request in ChatGPT.
2. Retrieve the topic map, due recall prompts, and unresolved questions through the authorized Obsidian bridge when available.
3. Select or confirm one outcome, such as resolving a contradiction or learning one mechanism.

At the end:

1. Return the requested study or teaching interaction through ChatGPT.
2. Write or update atomic notes through the authorized Obsidian bridge, or prepare the exact Markdown update when direct access is unavailable.
3. Add source IDs and locators.
4. Record changed beliefs and remaining uncertainty.
5. Add recall prompts that require retrieval or application, not mere recognition.
6. Set the next review date based on difficulty and assessment timing.

## Refresh and drift

Refresh a topic when the user adds sources, evidence is time-sensitive, a contradiction remains unresolved, or an assessment scope changes. During refresh:

- compare new claims with existing notes;
- flag superseded notes instead of silently rewriting history;
- update `last_verified` and `confidence` only after evidence review;
- rebuild the NotebookLM manifest if source decisions changed;
- preserve rejected-source reasons to avoid rediscovering the same dead ends.
