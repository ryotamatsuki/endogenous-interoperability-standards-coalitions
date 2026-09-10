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
- Selected Stage-3 mechanism: **C1 — Realized Interoperability Depth**
- Next canonical stage: **Stage 4 — Minimal Model**
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

### Stage 1 binding findings

- The historical fixed-depth #65 welfare reversal is reproducible.
- Under the source architecture, IS lower-bound depth is structurally implied along the symmetric-anchor continuation: `dW_IS/ds<0`, hence `s_I*=0`.
- The source reason is that coalition membership activates the full compatibility/network term while continuous depth changes competitive substitutability through `Tau` without increasing realized interoperability.
- This source depth interpretation is mathematically coherent but economically restrictive.
- The endogenous-depth source diagnostic leaves IS preferred to SU, so no coalition reversal exists at the canonical #65 witness.
- National-welfare aggregation and the full blocking correspondence require explicit treatment before a future stability theorem.

## Stage 2 authority

- `docs/REVIVAL_STAGE2_PRIOR_ART_MATRIX_2026-09-10.md`
- `reviews/STAGE_02_REVIVAL_NOVELTY_GATE_2026-09-10.md`
- `decisions/STAGE02_REVIVAL_DECISIONS.md`

Stage 2 verdict: **GO — GO TO MECHANISM SEARCH**.

### Stage 2 binding novelty boundary

Generic claims about compatibility-induced differentiation, continuous standards policy, standards-coalition stability, coalition-induced downstream choices, and continuous standardization changing a later firm strategy are occupied by prior literature and/or own SSDI.

The only surviving contribution family is:

> **Absorption versus non-absorption of strategic product repositioning in a standards-coalition game with endogenous bloc depth, with a coalition-stability consequence that disappears when product positions are fixed.**

No exact prior model was identified for that whole-game/result class, but the gap is narrow and result-dependent.

## Stage 3 authority

- `docs/REVIVAL_STAGE3_CANDIDATE_MECHANISM_MATRIX_2026-09-10.md`
- `model/REVIVAL_STAGE3_SELECTED_MECHANISM_2026-09-10.md`
- `reviews/STAGE_03_REVIVAL_MECHANISM_SEARCH_2026-09-10.md`
- `decisions/STAGE03_REVIVAL_DECISIONS.md`

Stage 3 verdict: **GO — GO TO MINIMAL MODEL**.

### Stage 3 candidate search

Ten distinct candidates were compared under ex-ante weights for whole-game novelty, mechanism clarity, minimality/tractability, welfare/coalition leverage, institutional plausibility, empirical bridge, and referee defensibility.

TOP 3:

1. **C1 — Realized interoperability depth** — 92/100;
2. C2 — Multi-market common standard — 82/100;
3. C3 — Home-market incidence / asymmetric national surplus — 77/100.

Only C1 is authorized for Stage 4.

### Selected mechanism — C1 Realized Interoperability Depth

The existing bloc depth variable receives one coherent technical interpretation:

- formal coalition membership determines which firms are potential interoperability partners;
- standards depth determines how completely interoperability is realized within the bloc;
- the same depth also compresses standard-related differentiation through the retained `Tau` map.

The Stage-4 baseline realization map is pre-fixed as

`chi(s)=s/s_bar`.

For `i != j`, the candidate affine-demand map is

`K_ij = c0 + lambda*phi(x_i-x_j)/Tau_ij(rho,s) - v*M_ij(rho,s)`,

where `M_ij=chi(s_C)` for two firms in the same multi-country bloc and `M_ij=0` across blocs.

No nonlinear `chi`, home bias, heterogeneous repositioning costs, policy cost, bargaining rule, extra market, implementation effort, standard-direction choice, or second policy dimension is authorized in the first Stage-4 attempt.

### Reduced-form mechanism logic

Under symmetric IS with fixed positions,

`c_FIX(s)=c0 + lambda*phi_bar/(t_bar-s) - v*chi(s)`.

Stage 1 established `dW_IS/dc<0`, while now

`dc_FIX/ds=lambda*phi_bar/(t_bar-s)^2-v*chi'(s)`.

Thus standards depth has a genuine interoperability-benefit / competition-cost trade-off instead of the mechanically negative policy effect in PR #65.

In FULL, product positions depend on depth. If members reposition apart, the induced fall in product proximity can attenuate the marginal competitive cost of deeper interoperability. This induced term is absent in `B-FIX`. Whether it is large enough to change policy or coalition stability is an open Stage-4 question, not an assumed result.

## Stage 4 mandatory benchmarks

Stage 4 must solve:

- `B-FIX`: endogenous coalition/depth with product positions fixed;
- `B-EXO`: endogenous product positions with exogenous depth;
- `FULL`: endogenous depth and product positions;
- historical #65 as a predecessor/comparison object only.

## Stage 4 fatal contribution gate

The C1 minimal model must establish on a nondegenerate regular region at least one of:

- a different stable partition in `B-FIX` and `FULL`;
- a strict coalition-stability threshold shift caused by repositioning;
- a coalition-blocking reversal caused by repositioning;
- a private/social coalition-stability wedge caused specifically by repositioning.

Removing endogenous product positioning must remove the headline result.

A positive optimal depth, nonzero repositioning, fixed-depth welfare reversal, or small welfare-level difference is insufficient.

If no repositioning-essential coalition-level result survives, the mandatory verdict is **NO-GO — TERMINATE THE REVIVAL**.

Stage 4 failure may not be repaired in the same cycle by adding C2/C3, asymmetry, nonlinear network effects, extra markets, bargaining, or another primitive. Any such future pivot requires a fresh workflow rollback / Stage-0 authorization.

## Next canonical stage

**Stage 4 — Minimal Model: test C1 Realized Interoperability Depth only.**