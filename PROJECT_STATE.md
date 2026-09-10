# Project State

Last updated: 2026-09-10

## Canonical status for this branch

- Project: Endogenous Interoperability and Standards Coalitions — **revival track**
- Historical working title: **Standards Coalitions and Strategic Product Repositioning**
- Revival working title: **Standards Coalitions, Policy Adjustment, and Strategic Product Repositioning**
- Branch: `revival/stage00-coalition-repositioning`
- Source branch / PR: `stage04r4a-affine-demand-bertrand-novelty` / PR #65
- Source head: `9f19a82e28415b571a086693323a3377f286fd73`
- Canonical workflow: `ryotamatsuki/research-paper-workflow` **v2.1**
- Workflow authority commit: `f48984013898696f010f0437a8cfed6b5b54bdc2`
- Revival Stage 0: **GO TO AUDIT**
- Revival Stage 1: **GO TO NOVELTY GATE**
- Revival Stage 2: **GO — GO TO MECHANISM SEARCH**
- Revival Stage 3: **GO — GO TO MINIMAL MODEL**
- Revival Stage 4: **GO AT CONSTRUCTION LEVEL — NOW REOPENED**
- Revival Stage 4A: **NO-GO / REOPEN STAGE 4**
- Exact Stage-4A blocker: **SU product-location equilibrium multiplicity with welfare/stability selection dependence**
- Selected mechanism: **C1 — Realized Interoperability Depth**
- Next canonical stage: **REOPENED STAGE 4 — multiplicity / selection characterization**
- Submission authorization: **NO**
- Theory freeze: **NONE FOR REVIVAL TRACK**
- Stage 6 novelty re-kill: **BLOCKED**
- Formal verification: **APPLICABLE; IMPLEMENTATION NOT YET AUTHORIZED / PASSED**
- Historical IJIO target: **context only; not binding**

## Relationship to main and PR #65

This branch does not replace or rewrite historical authority:

1. `main` preserves the canonical terminated history of the prior paper architecture.
2. PR #65 preserves the historical affine-demand conditional-go branch and its fixed-depth welfare-reversal witness.

The revival branch starts from PR #65 for provenance only and inherits no old theory freeze, referee gate, journal selection, manuscript integration, or submission authorization.

## Stage 0–3 authority

- Stage 0: `reviews/STAGE_00_REVIVAL_IDEA_INTAKE_2026-09-10.md`
- Revival provenance: `decisions/REVIVAL_2026-09-10_DECISION_RECORD.md`
- Stage 1: `reviews/STAGE_01_REVIVAL_SOURCE_MATHEMATICAL_AUDIT_2026-09-10.md`
- Stage 2: `reviews/STAGE_02_REVIVAL_NOVELTY_GATE_2026-09-10.md`
- Stage 3: `reviews/STAGE_03_REVIVAL_MECHANISM_SEARCH_2026-09-10.md`
- Stage-3 selected model: `model/REVIVAL_STAGE3_SELECTED_MECHANISM_2026-09-10.md`

The surviving research object remains an absorption/non-absorption or coalition-stability result that depends indispensably on product repositioning after endogenous bloc depth choice. Generic compatibility-induced differentiation, continuous standardization policy, coalition-induced downstream strategy, and continuous-policy-to-strategy-to-policy-reversal claims remain killed by Stage 2 and own SSDI prior art.

## Stage 4 construction authority

- `model/REVIVAL_STAGE4_C1_MINIMAL_MODEL_2026-09-10.md`
- `verification/stage04_revival_c1_minimal_model.py`
- `verification/stage04_revival_policy_completion.py`
- `theorem_certificates/STAGE04_REVIVAL_C1_PRELIMINARY_CERTIFICATES.md`
- `reviews/STAGE_04_REVIVAL_C1_MINIMAL_MODEL_2026-09-10.md`
- `decisions/STAGE04_REVIVAL_DECISIONS.md`

Stage 4 selected only **C1 — Realized Interoperability Depth**. For `i!=j`,

`K_ij=c0+lambda*phi(x_i-x_j)/Tau_ij(rho,s)-v*M_ij(rho,s)`,

where within a multi-country bloc `M_ij=s_C/s_bar` and across blocs `M_ij=0`.

No nonlinear realization map, policy cost, home bias, asymmetry, bargaining, extra market, or second policy dimension was added.

### Stage-4 construction findings retained provisionally

- affine-demand regularity survives on the stated threshold domain;
- the preferred outward SU location equilibrium exists;
- exact IS policy trade-off survives, with sufficient upper-depth condition `v>1/18`;
- exact fixed-position member-indifference threshold `v_FIX=1/15` survives;
- Stage-4 production solver obtained a preferred-branch stable-set reversal and ordered threshold result.

The last two preferred-branch FULL results are **not certified model-level conclusions after Stage 4A**.

## Stage 4A authority

- independent regression: `verification/stage04a_independent_multiplicity_red_team.py`
- adversarial review: `reviews/STAGE_04A_REVIVAL_C1_MATH_RED_TEAM_2026-09-10.md`
- theorem certificates: `theorem_certificates/STAGE04A_REVIVAL_C1_ADVERSARIAL_CERTIFICATES.md`
- decision record: `decisions/STAGE04A_REVIVAL_DECISIONS.md`

Stage 4A verdict:

**NO-GO / REOPEN STAGE 4.**

## Binding Stage-4A counterexample

At FULL-SU policy history `(s_12,s_3)=(.25,.25)` and `(v,gamma)=(.08,.03)`, independent multi-start solution of the full three-firm location FOC system plus whole-circle unilateral best-response attacks finds at least two distinct pure-strategy Nash equilibria.

### E1 — preferred outward equilibrium

`x≈(.13544022,.53122644,.83333333)`.

- SU member welfare ≈ `.14320705`;
- IS welfare ≈ `.14275239`;
- therefore `W_M(SU)>W(IS)`.

### E2 — omitted crossing equilibrium

`x≈(.47774332,.18892335,.83333333)`.

- SU member welfare ≈ `.14061475`;
- SU outsider welfare ≈ `.14296880`;
- therefore `W_M(SU)<W(IS)`.

Both E1 and E2 survive dense whole-circle unilateral best-response audits. E2 is not a failed stationary point or a local-only optimum.

The same qualitative multiplicity occurs at the Stage-4 interaction point `(v,gamma)=(.12,.03)`:

- preferred SU branch gives member welfare ≈ `.143577` > IS ≈ `.143460`;
- crossing SU branch gives member welfare ≈ `.140983` < IS.

Hence the Stage-4 stable-set conclusion is equilibrium-selection dependent.

## Consequences for Stage-4 claims

### Still retained

- P1 affine-demand regularity / attacked Bertrand continuation: **survives Stage-4A attack**;
- P2 outward repositioning: **survives as an existence claim only**;
- P3 exact IS marginal policy condition: **survives**;
- exact B-FIX threshold `1/15`: **survives**.

### Reopened / revoked as selection-free claims

- `FULL stable set={SU_12,SU_13,SU_23}`;
- nine-point stable-set reversal as a unique equilibrium implication;
- `v_FULL≈.13368738` as a unique model-implied threshold;
- `v_FIX<v_EXO-HIST<v_FULL` as a selection-free theorem;
- FULL-only stable-partition identification relative to B-FIX and B-EXO-HIST;
- FULL SU upper-depth policy equilibrium as a selection-free continuation result.

The Stage-4 preferred branch may remain a valid conditional equilibrium path, but the current model has no equilibrium-selection rule that makes it the unique continuation.

## No silent refinement

The following are not part of the model and may not be used to delete the crossing equilibrium without explicit workflow authorization:

- closest-anchor equilibrium selection;
- no-crossing/order-preservation restriction;
- selection by best-response dynamics initialized at anchors;
- welfare/Pareto selection;
- risk dominance;
- arbitrary preferred-branch selection.

## Reopened Stage-4 contract

Before Stage 4A can be repeated, Stage 4 must:

1. characterize the relevant SU location-equilibrium correspondence over the policy/threshold domain;
2. determine whether policy and coalition conclusions are invariant across all relevant equilibria;
3. if not invariant, determine whether an economically defensible and symmetric equilibrium refinement/selection is part of the intended model;
4. re-solve every material bloc-depth deviation using the correct continuation object;
5. restate blocking/stability and threshold claims with exact equilibrium-selection quantifiers;
6. preserve `stage04a_independent_multiplicity_red_team.py` as a permanent regression test;
7. return `NO-GO` if no non-ad-hoc resolution preserves a substantive FULL-only coalition result.

## Formal-verification applicability

Stage 4A records **FORMALIZATION APPLICABLE**. Preliminary future Lean targets, after theorem scope stabilizes, are:

- exact B-FIX factorization and threshold `v_FIX=1/15`;
- exact IS derivative and sufficient condition `v>1/18`;
- welfare-to-strict-blocking logical implications;
- any analytic equilibrium-branch conditions and threshold ordering that survive Stage-4 repair.

Formal implementation is deferred until the theorem scope is stable; there is no formal-verification PASS yet.

## Current routing

**REOPEN STAGE 4 — EQUILIBRIUM MULTIPLICITY / SELECTION CHARACTERIZATION.**

Stage 6, Stage 7.5A, theory freeze, journal positioning, manuscript rehabilitation, and submission remain blocked.
