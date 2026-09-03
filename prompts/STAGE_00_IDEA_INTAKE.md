# Stage 0 — Idea / Motivation Intake

> Canonical authority: `ryotamatsuki/research-paper-workflow` v1.1 at `488e5ab06c207909296a7564eaf9066f7f94319c` → `GOVERNANCE.md` → `THEORY_PAPER_RESEARCH_PIPELINE.md` → `templates/STAGE_00_IDEA_INTAKE.md`.

## 0. Role

Act as a research director in industrial organization, economics of standards, network economics, and spatial competition. Treat the idea as unproven. Determine whether endogenous partial interoperability can be converted into a precise research question worth formal audit. Do not sell the idea.

## 1. Project context

- Working title: `Endogenous Interoperability and Standards Coalitions`
- Research topic: endogenous partial interoperability, standards coalitions, network effects, product differentiation, price competition, and national welfare
- Core phenomenon: standards and ecosystems may differ continuously in interoperability rather than being simply compatible/incompatible
- Initial question: When firms can choose the degree of interoperability rather than only whether to adopt a common standard, how do network effects and product differentiation shape private interoperability choices, price competition, national welfare, and standards-coalition stability?
- Source files / notes: `README.md`, `PROJECT_STATE.md`, `PROVENANCE.md`, `notes/IDEA_SEED.md`, `model/MINIMAL_MODEL_HYPOTHESES.md`, `literature/PRIOR_ART_LEDGER.md`, `decisions/DECISION_LOG.md`
- Related prior project: `ryotamatsuki/private-compatibility-standards-coalitions` — benchmark only; do not alter or silently import its frozen theory
- Target journal: `UNRESOLVED`
- Current date: `2026-09-04`

If a field is unknown, mark it `UNRESOLVED`; do not invent it.

## 2. Stage objective

Extract the economic question from the motivating idea and decide whether the project merits a formal source/mathematical audit.

## 3. Canonical inputs

Read all repository source files listed above. Preserve what they actually support. Treat candidate mechanisms and model structure as hypotheses, not established facts.

## 4. Allowed changes

You may reframe the question, generate competing mechanisms, recommend theory/empirical/mixed routes, or recommend abandoning Salop/network effects/endogenous `a_i` if they are not the right primitive.

## 5. Prohibited changes

Do not build a full model, write a paper, claim novelty from unfamiliarity or ingredient combination, or add complexity merely to generate interiority.

Do not treat `0 < a_o* < 1` as a result. It is an early proposed kill condition to be audited later.

## 6. Mandatory tasks

1. State the phenomenon without explaining it.
2. State the proposed explanation separately.
3. Identify agents, choices, constraints, strategic interactions, and welfare-relevant outcomes.
4. Distinguish theoretical contribution from application/institutional motivation.
5. Generate 3–8 genuinely different candidate mechanisms. At least one candidate must not rely on Salop; at least one must not rely on network externalities.
6. Identify descriptive-only, known-result, parameterization, old-model-with-new-label, and continuous-reparameterization risks.
7. Test whether “interoperability reduces transport/switching cost” is economically distinct from simply redefining the Salop transport-cost parameter.
8. Explain what evidence or modeling result would make endogenous interoperability economically important rather than cosmetic.
9. Recommend theory, empirical, or mixed route and explain why.
10. Produce one falsifiable one-sentence research question.
11. Specify the literature families and exact source material that Stage 1/2 must audit.
12. Identify the minimum economic primitives needed for a later interiority test. Do not assume a convex cost is legitimate merely because it helps algebraically.
13. Assess whether the proposed distinction between private interoperability `a_o*` and a government/coalition threshold `â` is conceptually meaningful before mathematics is done.
14. State the strongest obvious way existing endogenous-compatibility literature could absorb the whole game.

## 7. Evidence requirements

Use repository materials as the primary basis. External literature research may be recommended for Stage 1/2, but do not infer novelty from the absence of citations in the repository.

## 8. Verification protocol

Cross-check that every factual claim is supported by supplied material, externally verified, or labeled as a hypothesis. No mathematics beyond simple consistency checks is required at Stage 0.

## 9. Project-specific kill tests

Kill or radically reframe the branch if it is only:

- binary compatibility with a continuous label;
- a rescaling of spatial transport cost;
- a standard network-effects comparative static in a new application;
- an old compatibility-investment model with standards-coalition vocabulary;
- a construction where interior `a_i` requires an arbitrary convex term with no independent interpretation;
- a model in which the government/coalition threshold is definitionally the same object as the private optimum;
- a project whose only novelty claim is combining Salop, network effects, and standards coalitions.

## 10. Success criteria

Proceed only if there is:

- a precise economic question;
- at least one defensible strategic mechanism candidate;
- a credible reason endogenous interoperability could generate a new full-game result;
- a clear Stage 1/2 audit plan;
- a plausible conceptual distinction between private interoperability choice and coalition/welfare incentives.

## 11. Failure criteria

Return `NO-GO` if the phenomenon is too vague, the contribution is already obviously cosmetic, or no researchable strategic/welfare margin can be identified.

## 12. Required final output

1. Executive verdict
2. Phenomenon vs explanation
3. Actors / decisions / frictions / outcomes
4. Candidate mechanisms
5. Main prior-art and reparameterization risks
6. Theory vs empirical route
7. One-sentence research question
8. Initial literature map
9. Required Stage 1 inputs
10. Conceptual assessment of `a_o*` vs `â`
11. Verdict and next-stage contract

## 13. Final verdict

Choose exactly one:

- `GO TO AUDIT`
- `CONDITIONAL GO` — specify one blocker
- `NO-GO`

## 14. Next-stage contract

State exactly what Stage 1 may audit and what must remain unchanged. A `CONDITIONAL GO` permits work only on the identified blocker.

## 15. Repository output

Save the completed Stage 0 report to:

`reviews/STAGE_00_IDEA_INTAKE_2026-09-04.md`

Then update `PROJECT_STATE.md` and append any accepted/rejected decisions to `decisions/DECISION_LOG.md`.
