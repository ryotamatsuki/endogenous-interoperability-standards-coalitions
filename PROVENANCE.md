# Provenance

## Project origin

This repository was initialized on 2026-09-04 as an independent theory project extending international standards-coalition analysis to a setting with endogenous standards depth and firms' strategic product repositioning.

## Relationship to prior work

Related repository: `ryotamatsuki/private-compatibility-standards-coalitions`.

That project is a frozen institutional IS/SU/SW benchmark only. C-ESD does not algebraically nest it, and its theory must not be modified from this repository.

## Workflow provenance

Canonical workflow:

- repository: `ryotamatsuki/research-paper-workflow`
- version: `v1.1`
- release SHA: `488e5ab06c207909296a7564eaf9066f7f94319c`

Stage-8 freeze ID:

`CESD-THEORY-FREEZE-2026-09-04-v1`

Stage-9 starting `main` SHA:

`95755cb82bceb136626279c5ff65fe1f1149afaa`

At Stage-9 start, no open pull requests were found. Historical stage branches were inspected and the production branch was created from the latest `main`; no historical reset was performed.

## Theory authority

The sole theory authority for manuscript production is:

`theory/THEORY_FREEZE_CESD_2026-09-04.md`.

Proof-status authority is:

`theory/PROPOSITION_REGISTER_CESD_2026-09-04.md`.

The main reversal remains a conditional constructive regular-region result, not a global closed-form theorem.

## Verification provenance

Canonical computational sources:

- `verification/stage04_cesd_minimal.py` — demand/price system, B-T/B-X/FULL witness, location FOC/SOC, whole-circle unilateral-deviation checks, local parameter box;
- `verification/stage07_cesd_welfare_generality.py` — exact transfer cancellation, national welfare decomposition, witness global-welfare ranking, constrained social-location comparison, `gamma_W` threshold.

Production-facing generated objects must be created by `scripts/generate_outputs.py`, which imports those verification modules rather than reimplementing the model.

## Literature provenance

Closest-paper positioning is governed by the Stage-6 closest-paper matrix and Stage-8 freeze. The paper must not revive setup-level novelty claims killed earlier. Institutional examples validate the policy-controlled interoperability primitive, not observed strategic re-differentiation.

## Change control

Post-freeze theory changes require an explicit record of what changed, why, affected equations/propositions, verification and literature claims, and the workflow stages to rerun. No silent theory drift is allowed during Stage 10 manuscript construction.
