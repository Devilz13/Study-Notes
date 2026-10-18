# Paper Writing

Turn verified research content into a clear, defensible argument for the intended paper type and audience. Do not create evidence merely to complete a section.

## Context

Determine the paper type, venue, contribution, audience, available evidence, source format, target section, and desired editing depth. Read [paper-types-and-venues.md](../../references/paper-types-and-venues.md) when venue or submission type matters.

Supported modes include outline, new draft, structural edit, section rewrite, line edit, LaTeX conversion, camera-ready preparation, and reviewer-driven revision. Preserve the user's voice and terminology unless they request a different style.

## Workflow

1. **Build the argument map.** Connect problem → gap → insight → method → evidence → contribution → limitation. Flag any link that lacks evidence.
2. **Assign section jobs.** Every section and paragraph should advance one identifiable part of the argument. Remove duplication and move detail to the correct location.
3. **Draft from evidence.** Use supplied results, verified sources, and explicit placeholders such as `[RESULT NEEDED]` or `[CITATION TO VERIFY]`. Never fabricate a citation, number, experiment, or claim of novelty.
4. **Check traceability.** Make claims match figures, tables, equations, appendices, and cited sources. Keep terminology and notation stable.
5. **Simulate the reader.** Test whether a domain reviewer can identify the problem, difference from prior work, mechanism, evidence, and limitations quickly.
6. **Revise and record.** Provide the requested text plus a concise change log and unresolved evidence needs when edits are substantial.

## Section Logic

- **Abstract:** problem, gap/context, approach, strongest supported result, and contribution—without promises the paper does not deliver.
- **Introduction:** motivation, precise gap, core insight, contribution list, and roadmap. Contributions must match later evidence.
- **Related work:** synthesize competing approaches and position the contribution fairly; do not use citation lists as argument substitutes.
- **Method:** define assumptions, notation, algorithm/system, design choices, and complexity or implementation details needed to understand and reproduce the work.
- **Experiments/study:** map each experiment or analysis to a claim; report comparators, metrics, uncertainty, resources, and limitations.
- **Results/discussion:** distinguish observation from interpretation, and discuss negative or ambiguous findings honestly.
- **Conclusion:** answer the research question and state limitations/future work without introducing new results.

## Editing Rules

- Prefer precise subjects, verbs, and measurable claims over inflated language.
- Keep one main message per paragraph and lead with why a technical detail matters.
- Define acronyms and symbols on first use; avoid renaming concepts without reason.
- Make captions understandable with minimal dependence on the body.
- Preserve citation commands, labels, and cross-references in LaTeX unless intentionally changing them.
- Do not weaken caveats or uncertainty to make the paper sound stronger.

## Output Contract

Deliver the requested prose or source first. For substantial work, add assumptions, a change log, unresolved placeholders, and the next highest-value revision. If the user supplied files, preserve their structure and unrelated content.
