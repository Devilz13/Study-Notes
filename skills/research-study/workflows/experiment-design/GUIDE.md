# Experiment Design

Design the smallest study that can genuinely discriminate among the important explanations while meeting the standards of the field and paper type.

## Calibrate the Study

Identify the study family before prescribing methods: controlled experiment, machine-learning benchmark, observational or causal study, survey/user study, simulation, qualitative study, replication, or mixed methods. Do not apply ML-specific baselines and ablations to every discipline.

Read [paper-types-and-venues.md](../../references/paper-types-and-venues.md) when the plan supports a submission.

## Design Workflow

1. **Claim and decision.** State the primary question, falsifiable hypothesis or estimand, competing explanations, and what decision the result should inform.
2. **Units and variables.** Define population/sample, unit of analysis, independent/exposure variables, outcomes, controls, confounders, and measurement validity.
3. **Comparators.** Select simple, established, current, and task-relevant baselines or control conditions. Ensure equal data, tuning effort, preprocessing, and evaluation rules where fairness requires it.
4. **Metrics.** Name one or more primary outcomes before secondary and diagnostic metrics. Define direction, units, aggregation, clinically/practically meaningful effect, and failure criteria.
5. **Analysis.** Plan sample size or power reasoning, randomization/blinding where applicable, uncertainty intervals, statistical tests or models, multiple-comparison handling, missing data, and robustness checks.
6. **Mechanism tests.** Add ablations, sensitivity analysis, negative controls, subgroup/error analysis, cross-setting transfer, or qualitative inspection only when they test a specific claim.
7. **Integrity threats.** Check leakage, contamination, p-hacking, cherry-picking, benchmark overfitting, selection bias, measurement drift, and post-treatment variables.
8. **Execution.** Estimate data, compute, people, cost, time, dependencies, stopping rules, risks, and fallback plans.
9. **Reproducibility.** Record versions, seeds, environment, preprocessing, splits, code, artifacts, and deviations from the plan.

Use [experiment-plan.md](templates/experiment-plan.md) for a full protocol.

## Output Contract

Provide a claim-to-experiment map, primary and secondary analyses, comparators, expected interpretation for positive/negative/ambiguous outcomes, resource budget, risks, and reproducibility checklist. Label exploratory analyses as exploratory. Do not invent expected effect sizes or power inputs; show sensitivity ranges when inputs are uncertain.
