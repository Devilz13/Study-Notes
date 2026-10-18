# Paper Reading

Help the user build an accurate mental model of the paper. Adapt technical depth, terminology, and use of analogy to the user's background.

## Inputs and Modes

Use the paper, supplement, code, or source files the user provides. If the document is scanned or extraction is unreliable, route through [document-ingestion](../document-ingestion/GUIDE.md).

Infer the mode when clear; otherwise ask whether the user wants:

- a quick orientation;
- a teaching explanation;
- a deep technical reading;
- a replication-oriented reading;
- answers to specific questions.

## Reading Passes

1. **Map the paper.** Read the title, abstract, introduction, conclusion, headings, figures, and tables. Identify the claimed problem, contributions, and result.
2. **Trace the argument.** For each major claim, locate the method, assumption, evidence, and stated limitation that supports it.
3. **Resolve the technical core.** Explain the mechanism, equations, algorithm, study design, datasets, baselines, and evaluation at the depth required.
4. **Interpret.** Explain what the results do and do not establish, where the work fits, and which questions remain.

Do not let the abstract or conclusion substitute for the body. Distinguish the authors' claims from your interpretation and independent verification.

## Equations and Figures

For a key equation, define symbols, domains, assumptions, dimensions/units, and the role of each term before manipulating it. Show intermediate reasoning when the derivation matters. If a step cannot be verified, identify the gap.

For a key figure or table, explain the axes, units, comparison, uncertainty, sample size, and the conclusion the authors draw. Do not infer precise values from an unreadable plot.

## Output Shape

Choose the smallest structure that serves the request. A deep reading normally covers:

- one-paragraph orientation;
- problem and why it matters;
- claimed contributions;
- method or argument, step by step;
- key evidence and results;
- essential equations, figures, or tables;
- assumptions and limitations;
- field positioning and related concepts;
- what to read or verify next.

Use analogies only when they clarify the mechanism, and state where the analogy stops matching the real method. Cite page, section, figure, table, or equation locations for consequential explanations.
