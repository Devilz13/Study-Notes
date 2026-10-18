# Research Paper Review

Produce a rigorous, fair, specific review whose priorities change with the user's selected mode and the paper type.

## Intake and Mode

If the user says only “review this paper” or equivalent, ask for:

1. mode: peer reviewer, author coach, comparison/literature analyst, or all;
2. paper type;
3. target venue/track and reviewing guidelines, if any.

If the user declines to specify, state the assumptions and review without pretending venue-specific certainty. Read [paper-types-and-venues.md](../../references/paper-types-and-venues.md) and [research-integrity.md](../../references/research-integrity.md).

Mode priorities:

| Mode | Primary priority | Typical decision output |
| --- | --- | --- |
| Peer reviewer | Soundness, novelty, significance, venue fit, decision-critical questions | Formal review and venue score/recommendation when requested or required |
| Author coach | Highest-value fixes, claim/evidence repair, clarity, submission readiness | Prioritized revision plan; verdict only if useful |
| Comparison/literature | Exact differences, evidence quality, positioning, gaps | Comparative synthesis rather than accept/reject |
| All | Reviewer simulation plus actionable author plan and positioning | Layered output without repeating the same critique three times |

## Preflight

- Ensure the complete paper, appendices, supplement, and relevant artifacts are available or list what is missing.
- For scanned or unreliable documents, use [document-ingestion](../document-ingestion/GUIDE.md).
- Verify current venue rules from official guidance when a venue is named.
- Calibrate validation expectations to the submission type. Do not apply full-paper standards to demos, vision papers, posters, or short papers unless the venue does.
- Treat novelty assessment as a literature task; search or qualify it rather than relying on memory.

## Review Passes

1. **Orientation:** title, abstract, introduction, conclusion, figures, tables, and contribution claims.
2. **Claim-evidence map:** connect each central claim to its method, assumptions, experiment/proof, and result.
3. **Technical audit:** examine methodology, derivations, experimental design, baselines, controls, statistics, artifacts, and reproducibility.
4. **Positioning and significance:** compare with verified closest work and assess whether the difference matters.
5. **Decision and revision:** rank strengths, major concerns, minor concerns, questions, and repairs according to mode.

## Structured Understanding

Before criticizing, establish:

- problem and importance;
- claimed contributions;
- approach or methodology;
- key findings and metrics;
- acknowledged and unacknowledged limitations.

Consequential observations should point to pages, sections, figures, tables, equations, appendices, or source labels.

### Numerical & Consistency Checks — most info from LinkedIn

Retain the heading annotation above as requested; it is not an instruction to treat LinkedIn as authoritative paper evidence.

Run the detailed checklist in [consistency-checks.md](references/consistency-checks.md). At minimum, compare numbers across text, tables, figures, abstract, and conclusion; recompute reported improvements; check sample sizes, statistical relationships, units, references, acronyms, terminology, and citation existence/style. Verify decision-critical values against the rendered source rather than OCR alone.

## Critical Dimensions

Weight dimensions by paper and venue type. Mark a dimension not applicable rather than penalizing it.

- **Novelty and contribution:** What is new relative to verified closest work, and is the difference substantive?
- **Soundness:** Are assumptions, methods, proofs, and causal/empirical claims justified?
- **Significance:** Would the result change understanding, capability, practice, evidence, or future work?
- **Clarity:** Can the intended audience follow the argument, notation, figures, and scope?
- **Evaluation completeness:** Do the experiments or analyses test the central claims with appropriate controls and alternatives?
- **Reproducibility:** Are data, code, parameters, procedures, and artifacts sufficient for the paper type?
- **Related work:** Is positioning accurate, complete enough, and fair?
- **Ethics and limitations:** Are relevant risks, data practices, impacts, and boundary conditions addressed?
- **Venue alignment:** Does the work meet current scope, format, and contribution expectations?

## Findings and Questions

Classify a **major concern** only when it can materially change a central claim or decision. Pair each weakness with why it matters, supporting location/evidence, and a feasible repair or verification path. Questions for authors must be genuine: explain what answer would change the assessment.

Use [constructive-feedback.md](references/constructive-feedback.md) for tone and [scoring-and-decisions.md](references/scoring-and-decisions.md) when a score or verdict is requested. Never force a universal 1–10 score onto a venue with a different form.

## Output by Mode

- **Peer reviewer:** use [review-form.md](templates/review-form.md), adapted to the official venue form.
- **Author coach:** lead with up to ten actions ranked by expected benefit relative to implementation cost, then explain strengths, major issues, minor issues, and exact revision suggestions.
- **Comparison/literature:** route evidence gathering and synthesis through [literature-review](../literature-review/GUIDE.md); use an exact comparison table and qualify novelty coverage.
- **Meta-review:** use [meta-review-form.md](templates/meta-review-form.md); synthesize consensus, disagreement, rebuttal, review quality, and decision rationale without merely averaging scores.
- **All:** give one shared summary and evidence audit, then separate “Reviewer View” and “Author Action Plan.”

End with confidence based on corpus completeness, document quality, venue information, and subfield familiarity—not rhetorical certainty.

## Ethics

Respect review confidentiality and venue policy. Do not upload a submission to an external OCR, search, or analysis service without authorization. Critique the paper, not the authors. If a possible flaw is uncertain, request clarification rather than using it as a decisive rejection reason.
