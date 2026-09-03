# Endogenous Interoperability and Standards Coalitions

Private research-development repository for a theory project on endogenous partial interoperability, network effects, product differentiation, price competition, national welfare, and standards-coalition stability.

## Research status

- Working title: *Endogenous Interoperability and Standards Coalitions*
- Field: Industrial Organization / Economics of Standards / Network Economics / Spatial Competition
- Current stage: Stage 0 — Idea / Motivation Intake
- Canonical workflow: `ryotamatsuki/research-paper-workflow`
- Workflow version: `v1.1`
- Workflow release SHA: `488e5ab06c207909296a7564eaf9066f7f94319c`
- Target journal: `UNRESOLVED`
- Repository role: research-development repository; not yet a production manuscript repository
- Initialized: 2026-09-04

## Core research program

The project studies the sequence

`formal standards coalition → endogenous interoperability a → network effects + product differentiation → price competition → national welfare → coalition stability`.

The central economic margin is that interoperability is not merely binary. Firms may choose an interoperability intensity `a`, potentially trading off access to network benefits and lower switching/mismatch frictions against product differentiation or strategic insulation.

## Early kill conditions

The project should not be expanded unless a minimal model can generate a nonempty parameter region with an interior private interoperability choice,

`0 < a_o* < 1`,

and a distinct government/coalition-relevant interoperability threshold `â` such that the ordering

`a_o* ≷ â`

changes coalition stability, welfare, or another strategically meaningful equilibrium outcome.

If endogenous partial interoperability is generically corner-valued, or if the private optimum and coalition/welfare threshold collapse to the same object, the added model complexity requires re-justification.

## Repository structure

- `PROJECT_STATE.md` — canonical current status and next-stage contract
- `PROVENANCE.md` — origin, workflow, and boundary with prior projects
- `notes/IDEA_SEED.md` — motivating idea and research question
- `model/MINIMAL_MODEL_HYPOTHESES.md` — non-canonical candidate architecture and kill tests
- `literature/PRIOR_ART_LEDGER.md` — Stage 1/2 literature-audit ledger
- `prompts/STAGE_00_IDEA_INTAKE.md` — instantiated executable Stage 0 prompt
- `reviews/` — Stage reports once executed
- `decisions/DECISION_LOG.md` — accepted/rejected research decisions

## Boundary with prior standards-coalition paper

This repository is separate from `private-compatibility-standards-coalitions`. The prior paper's frozen theory must not be silently altered or treated as the canonical model here. Results may be used only as an explicitly documented benchmark or nested comparison after provenance and novelty checks.

## Governance

Follow the hierarchy in the canonical workflow:

`GOVERNANCE.md → THEORY_PAPER_RESEARCH_PIPELINE.md → stage template → checklist`.

Weak branches should be killed early. Unknown items are recorded as `UNRESOLVED`; novelty is not inferred from ingredient combination alone; and rejected mechanisms remain part of the research record.
