# Samuel - ICT111: NotebookLM processing prompt

Use this prompt after sources have been added. This file does not create or run a notebook.

```text
Process only the selected sources for ICT111. Do not infer missing module titles, lesson content, or assignment requirements. If no source is available, report "awaiting files" and stop.
Identify each source by title and source ID. Cite substantive claims with page, slide, section, or timestamp when available. Distinguish explicit evidence, derived inference, and uncertainty.
Produce source coverage; prerequisites; atomic concepts and relationships; concise revision notes; worked examples supported by sources; contradictions and misconceptions; recall questions with a separate cited answer key.
For assignments, extract the exact brief and rubric before suggesting work. Separate the student's draft, official requirements, feedback, and source evidence.
Finish with CHATGPT / CLAUDE HANDOFF in Markdown: source IDs and locators; candidate claims; proposed concept notes and links; unresolved questions; recall items; and passages that the assistant must verify. Label the whole handoff unverified_synthesis. Generated statements do not become verified merely because a heading says "verified".
```
