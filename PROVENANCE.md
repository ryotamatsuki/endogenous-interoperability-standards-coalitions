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

Current submission-authoritative freeze:

`CESD-THEORY-FREEZE-2026-09-04-v2`

The earlier freeze is retained only for historical provenance and is superseded where it conflicts with the repaired action set.

## Why v2 exists

Stage 11 identified an off-path SPNE problem: the historical policy action set gave singleton blocs a positive harmonization-depth instrument even though a singleton has no within-coalition harmonization relation. Stage 4R repaired the action set so that only non-singleton blocs choose depth and required whole-circle location Nash continuations inside policy evaluation. Stage 7R confirmed that the welfare/generality package is unchanged, and Stage 8R re-froze the repaired theory as v2.

## Theory authority

The sole theory authority for submission-oriented production is:

`theory/THEORY_FREEZE_CESD_2026-09-04_v2.md`.

Proof-status authority is:

`theory/PROPOSITION_REGISTER_CESD_2026-09-04_v2.md`.

Parameter/welfare authority is:

`theory/PARAMETER_WELFARE_VERIFICATION_REGISTER_CESD_2026-09-04_v2.md`.

The main reversal remains a conditional constructive regular-region result, not a global closed-form theorem.

## Verification provenance

Canonical computational chain:

- `verification/stage04_cesd_minimal.py` — baseline algebra and historical benchmark implementation;
- `verification/stage04r_cesd_continuation_repair.py` — repaired action sets, policy-stage optimization, and whole-circle continuation verification over feasible depth choices;
- `verification/stage07_cesd_welfare_generality.py` — exact welfare accounting utilities;
- `verification/stage07r_cesd_welfare_refresh.py` — repaired welfare decomposition, global-welfare ranking at the witness, constrained social-location comparison, and `gamma_W`.

Production-facing generated objects are created by `scripts/generate_outputs.py`, which imports Stage 7R rather than reimplementing model logic. Stage 7R itself uses the repaired Stage 4R continuation.

## Literature provenance

Closest-paper positioning is governed by the Stage-6 closest-paper matrix and the v2 freeze. The paper must not revive setup-level novelty claims killed earlier. Institutional examples validate the policy-controlled interoperability primitive, not observed strategic re-differentiation.

## Change control

Post-v2 theory changes require an explicit record of what changed, why, affected equations/propositions, verification and literature claims, and the workflow stages to rerun. No silent theory drift is allowed during Stage 10R manuscript refresh or later production.
