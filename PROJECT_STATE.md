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
- Revival Stage 4: **GO — GO TO STAGE 4A**
- Selected mechanism: **C1 — Realized Interoperability Depth**
- Next canonical stage: **Stage 4A — Independent Mathematical Adversarial Certification Gate**
- Submission authorization: **NO**
- Theory freeze: **NONE FOR REVIVAL TRACK**
- Historical IJIO target: **context only; not binding**

## Relationship to main and PR #65

This branch does not replace or rewrite either historical authority:

1. `main` preserves the canonical terminated history of the prior paper architecture.
2. PR #65 preserves the historical affine-demand conditional-go branch and its fixed-depth welfare-reversal witness.

The revival track starts from PR #65 solely to preserve useful source mathematics and provenance. It does not inherit old Stage 4, theory-freeze, hostile-referee, journal-selection, manuscript-integration, or submission passing status.

## Stage 0 authority

- `reviews/STAGE_00_REVIVAL_IDEA_INTAKE_2026-09-10.md`
- `decisions/REVIVAL_2026-09-10_DECISION_RECORD.md`

Stage 0 verdict: **GO TO AUDIT**.

Live research question:

> **When standards blocs choose standards depth optimally before firms reposition products, under what economically defensible conditions does post-policy product repositioning change the stable standards-coalition set rather than being absorbed by the blocs' policy adjustment?**

## Stage 1 authority

- `model/REVIVAL_STAGE1_AUDITED_REPRESENTATION_2026-09-10.md`
- `verification/stage01_revival_source_audit.py`
- `reviews/STAGE_01_REVIVAL_SOURCE_MATHEMATICAL_AUDIT_2026-09-10.md`
- `decisions/STAGE01_REVIVAL_DECISIONS.md`

Stage 1 verdict: **GO TO NOVELTY GATE**.

Binding findings:

- the historical #65 fixed-depth welfare reversal is reproducible;
- in the source architecture, IS `s_I*=0` is structural because depth changes competitive substitutability but not realized interoperability;
- this source depth interpretation is mathematically coherent but economically restrictive;
- restoring endogenous depth in the source architecture absorbs the fixed-depth reversal;
- national welfare and the complete blocking correspondence required explicit rebuilding.

## Stage 2 authority

- `docs/REVIVAL_STAGE2_PRIOR_ART_MATRIX_2026-09-10.md`
- `reviews/STAGE_02_REVIVAL_NOVELTY_GATE_2026-09-10.md`
- `decisions/STAGE02_REVIVAL_DECISIONS.md`

Stage 2 verdict: **GO — GO TO MECHANISM SEARCH**.

Binding novelty boundary:

- generic compatibility-induced differentiation is occupied;
- continuous compatibility/standardization policy is occupied;
- standards-coalition stability is occupied;
- coalition-induced downstream strategic choice is occupied;
- own SSDI already occupies the generic `continuous standardization -> endogenous downstream response -> policy reversal` architecture.

The only surviving contribution family is an **absorption/non-absorption or coalition-stability result that depends indispensably on product repositioning after endogenous bloc depth choice**.

## Stage 3 authority

- `docs/REVIVAL_STAGE3_CANDIDATE_MECHANISM_MATRIX_2026-09-10.md`
- `model/REVIVAL_STAGE3_SELECTED_MECHANISM_2026-09-10.md`
- `reviews/STAGE_03_REVIVAL_MECHANISM_SEARCH_2026-09-10.md`
- `decisions/STAGE03_REVIVAL_DECISIONS.md`

Stage 3 verdict: **GO — GO TO MINIMAL MODEL**.

Ten candidates were compared. The selected and only Stage-4-authorized mechanism was **C1 — Realized Interoperability Depth**.

C1 keeps one depth variable and gives it one literal technical interpretation:

- membership determines potential interoperability partners;
- depth determines how fully interoperability is realized within the bloc;
- the same depth compresses standard-related differentiation through the retained `Tau` map.

The realization map is fixed as

`chi(s)=s/s_bar`.

For `i!=j`,

`K_ij=c0+lambda*phi(x_i-x_j)/Tau_ij(rho,s)-v*M_ij(rho,s)`,

where within a multi-country bloc `M_ij=chi(s_C)` and across blocs `M_ij=0`.

No nonlinear `chi`, policy cost, home bias, asymmetry, bargaining, second policy dimension, or extra market is authorized.

## Stage 4 authority

- `model/REVIVAL_STAGE4_C1_MINIMAL_MODEL_2026-09-10.md`
- `verification/stage04_revival_c1_minimal_model.py`
- `verification/stage04_revival_policy_completion.py`
- `theorem_certificates/STAGE04_REVIVAL_C1_PRELIMINARY_CERTIFICATES.md`
- `reviews/STAGE_04_REVIVAL_C1_MINIMAL_MODEL_2026-09-10.md`
- `decisions/STAGE04_REVIVAL_DECISIONS.md`

Stage 4 verdict: **GO — GO TO STAGE 4A INDEPENDENT MATHEMATICAL ADVERSARIAL CERTIFICATION**.

### S4-1 — global continuation construction survives

On the threshold audit domain `v in [.06,.16]`, off-diagonal curvature is uniformly bounded by

`c_min=.14`, `c_max=.966666...`,

and the inherited sufficient inequalities for positive definiteness / substitute-demand structure continue to hold over the full policy box and product circle. KKT nonnegative demand and direct global one-price deviation regressions pass at hostile histories.

This is construction evidence, not Stage-4A certification.

### S4-2 — C1 removes the mechanical `s_I*=0` result

At symmetric IS anchors,

`c_IS(s)=c0+lambda*(1/4)/(t_bar-s)-v*s/s_bar`.

The exact Stage-1 derivative `dW_IS/dc<0` still holds, but now the depth effect is

`dc_IS/ds=lambda*(1/4)/(t_bar-s)^2-v/s_bar`.

Thus depth has a genuine realized-interoperability benefit versus competitive-compression trade-off. A sufficient threshold for the upper-depth policy is

`v>1/18`.

### S4-3 — canonical stable-set reversal

At `(v,gamma)=(.08,.03)`:

- `B-FIX stable set = {IS}`;
- `FULL stable set = {SU_12,SU_13,SU_23}`.

Canonical FULL SU policy is `(s_12,s_3)=(.25,.25)` and the member firms reposition to approximately

`(.135440,.531226,.833333)`.

Approximate welfare:

- IS: `.14275239` each;
- B-FIX SU member: `.14263839`;
- FULL SU member: `.14320705`;
- FULL SU outsider: `.14182976`;
- FULL SW: `.14251852` each.

The same B-FIX/FULL stable-set reversal is reproduced at all nine points of the pre-existing box

`v in {.07,.08,.09}` x `gamma in {.025,.03,.035}`.

### S4-4 — ordered blocking thresholds

At `gamma=.03`, the SU-member indifference/blocking thresholds against IS are

- `v_FIX=1/15 approximately .06666667` for B-FIX;
- `v_EXO-HIST approximately .11154504` for the pre-existing #65 positive exogenous-depth benchmark;
- `v_FULL approximately .13368738` for FULL.

Hence

`v_FIX < v_EXO-HIST < v_FULL`.

The B-EXO/FULL ordering persists at the pre-existing redesign-cost values:

- `gamma=.025`: `.11264515 < .13493252`;
- `gamma=.030`: `.11154504 < .13368738`;
- `gamma=.035`: `.11048100 < .13247968`.

### S4-5 — FULL-only interaction region

At the transparent point `v=.12,gamma=.03`, which lies strictly between the derived B-EXO-HIST and FULL thresholds:

- B-FIX -> `{IS}`;
- B-EXO-HIST -> `{IS}`;
- FULL -> `{SU_12,SU_13,SU_23}`.

Thus the FULL stable-partition result is not reproduced by either binding nested benchmark at the same primitives. Removing endogenous positioning or removing endogenous policy under the pre-existing exogenous-depth benchmark destroys the headline outcome.

### S4-6 — stability rule now explicit

Stage 4 freezes a strict residual-membership blocking correspondence: a deviating coalition forms an exclusive bloc, nondeviators retain residual links where feasible, and all deviators must strictly gain at the alternative partition's own complete continuation equilibrium.

This rule is a mandatory Stage-4A attack target.

## Stage 4A contract

Stage 4A must independently certify or defeat:

1. global Bertrand continuation on the full stated history domain;
2. SU location equilibrium globality/multiplicity throughout threshold brackets;
3. SU and SW global policy best responses beyond finite-grid construction evidence;
4. uniqueness and ordering of `v_EXO-HIST` and `v_FULL` roots;
5. local-open-set / quantifier claims;
6. the complete blocking correspondence and stable-set calculations;
7. robustness to alternative equilibrium selections if multiplicity is found.

Stage 4A may not silently repair the model. A failed headline certificate reopens or kills the theory.

## Current routing

**NEXT: STAGE 4A — INDEPENDENT MATHEMATICAL ADVERSARIAL CERTIFICATION GATE.**

No Stage 6, theory freeze, journal positioning, manuscript rehabilitation, or submission authorization is active.
