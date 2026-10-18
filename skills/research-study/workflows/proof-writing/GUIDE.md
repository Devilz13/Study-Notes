# Proof Writing

Produce a proof whose assumptions, dependencies, and logical transitions can be checked. A polished argument is not a substitute for a valid one.

## Select the Mode

- **Develop:** build a proof from a claim.
- **Verify:** check an existing proof line by line.
- **Repair:** locate the first invalid step and find the weakest sufficient correction.
- **Explain:** translate a valid proof to the user's level without losing conditions.
- **Typeset:** improve notation and LaTeX while preserving mathematical content.

## Workflow

1. **Normalize the claim.** State domains, quantifiers, regularity conditions, edge cases, probability space, asymptotic regime, and exactly what must be shown.
2. **Inventory dependencies.** List definitions, lemmas, cited theorems, and assumptions. Verify that theorem conditions match before invoking them.
3. **Stress-test.** Try small cases, boundary values, dimensional checks, and counterexamples. If the claim is false or underspecified, stop and show why.
4. **Choose a strategy.** Consider direct proof, contradiction, induction, construction, reduction, invariants, extremal arguments, convexity, probabilistic methods, or information-theoretic methods as appropriate.
5. **Derive.** Make each consequential implication explicit. Track equality/inequality direction, conditioning, limits, interchange operations, measurability, convergence, and hidden positivity assumptions.
6. **Verify independently.** Check for circular reasoning, stronger conclusions than premises allow, dropped cases, overloaded notation, and dependence on an unproved lemma.
7. **Present.** Give a clean theorem statement, proof outline, full proof, and verification notes. Use stable LaTeX labels and consistent notation.

## Repair Rules

Identify the earliest invalid or unsupported transition rather than merely rewriting the ending. Prefer the weakest additional assumption or narrowest corrected conclusion. Distinguish a repaired theorem from the original claim.

## Output Contract

Include the normalized statement, assumptions, dependency list, strategy, proof, edge-case checks, and remaining gaps. When certainty is incomplete, label the argument as a proof sketch or partial result. Never invent a theorem name, citation, or condition.
