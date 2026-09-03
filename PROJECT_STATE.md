# Project State

Last updated: 2026-09-04

## Canonical status

- Project: Endogenous Interoperability and Standards Coalitions
- Current canonical stage: Stage 0 — Idea / Motivation Intake
- Stage 0 execution status: NOT YET RUN
- Canonical verdict: UNRESOLVED
- Current route: theory candidate
- Production manuscript authorized: NO
- Theory frozen: NO
- Target journal: UNRESOLVED

## Canonical workflow reference

- Repository: `ryotamatsuki/research-paper-workflow`
- Version: `v1.1`
- Release SHA: `488e5ab06c207909296a7564eaf9066f7f94319c`
- Stage 0 template: `templates/STAGE_00_IDEA_INTAKE.md`

## Frozen project boundary

This project is independent from `private-compatibility-standards-coalitions`. The earlier paper may later serve as a benchmark, but its frozen theory is not the canonical model of this repository and must not be modified through this project.

## Current research question — provisional

When firms can choose the degree of interoperability rather than only whether to adopt a common standard, how do network effects and product differentiation shape the private interoperability choice, price competition, national welfare, and the stability of standards coalitions?

This wording is provisional until Stage 0.

## Early economic kill tests

Before investing in a full model, the project must determine whether a disciplined minimal structure can deliver all of the following:

1. A nonempty parameter region with an interior private interoperability choice: `0 < a_o* < 1`.
2. An economically distinct government/coalition threshold `â` rather than a relabeling of the firm's private FOC.
3. Parameter regions with `a_o* < â` and/or `a_o* > â` that change coalition stability, welfare, or another full-game strategic result.
4. A mechanism that cannot be reduced to a standard compatibility/network-effects model plus a cosmetic continuous parameter.
5. A credible economic reason for any curvature/cost needed to generate interiority; no ad hoc convex term may be introduced solely to force `a_o*` into `(0,1)`.

Failure of tests 1–3 is a strong reason to kill or radically simplify the endogenous-interoperability branch.

## Candidate architecture — not frozen

- Salop circular differentiation is a candidate representation, not yet canonical.
- Firm-level interoperability intensity `a_i ∈ [0,1]` is the preferred first candidate.
- Pairwise effective compatibility derived from `(a_i,a_j)` remains UNRESOLVED.
- Network externalities are allowed as a candidate mechanism but should enter only if they generate a distinct strategic margin.
- Price competition should be solved after interoperability choices in the candidate timing.
- Government/national-welfare objectives and coalition formation are downstream objects and must not be hard-coded before the private interoperability mechanism survives.

## Next action

Execute `prompts/STAGE_00_IDEA_INTAKE.md` and save the report as:

`reviews/STAGE_00_IDEA_INTAKE_2026-09-04.md`

If and only if the Stage 0 verdict is `GO TO AUDIT`, proceed to Stage 1 Source & Mathematical Audit using the canonical v1.1 template. A `CONDITIONAL GO` may work only on its specified blocker.
