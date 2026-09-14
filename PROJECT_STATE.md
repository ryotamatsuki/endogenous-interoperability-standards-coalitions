# Project State

Last updated: 2026-09-15

## Canonical status for this branch

- Project: Endogenous Interoperability and Standards Coalitions — **revival track**
- Revival working title: **Standards Coalitions, Policy Adjustment, and Strategic Product Repositioning**
- Branch: `revival/stage00-coalition-repositioning`
- Source branch / PR: `stage04r4a-affine-demand-bertrand-novelty` / PR #65
- Source head: `9f19a82e28415b571a086693323a3377f286fd73`
- Canonical workflow: `ryotamatsuki/research-paper-workflow` **v2.1**
- Workflow authority commit: `f48984013898696f010f0437a8cfed6b5b54bdc2`
- Stage 0: **GO TO AUDIT**
- Stage 1: **GO TO NOVELTY GATE**
- Stage 2: **GO TO MECHANISM SEARCH**
- Stage 3: **GO TO MINIMAL MODEL**
- Stage 4 initial construction: **GO, later reopened by Stage 4A**
- Stage 4A first pass: **NO-GO / REOPEN STAGE 4**
- Stage 4R multiplicity repair: **GO — REPEAT STAGE 4A**
- Stage 4A repeat: **GO — MATHEMATICAL ADVERSARIAL CERTIFICATION PASS**
- Stage 6: **GO — GO TO STAGE 7**
- Selected mechanism: **C1 — Realized Interoperability Depth**
- Next canonical stage: **Stage 7 — Welfare / Generality / Institutional Validation**
- Submission authorization: **NO**
- Theory freeze: **NONE**
- Formal verification: **APPLICABLE; NOT YET IMPLEMENTED/PASSED**

## Relationship to historical branches

`main` remains the canonical terminated history of the prior architecture. PR #65 remains the historical affine-demand conditional-go source and fixed-depth welfare-reversal witness. The revival branch does not rewrite either authority and inherits no old theory freeze, journal selection, referee pass, or submission authorization.

## Stage 0–3 authority

- Stage 0: `reviews/STAGE_00_REVIVAL_IDEA_INTAKE_2026-09-10.md`
- Stage 1: `reviews/STAGE_01_REVIVAL_SOURCE_MATHEMATICAL_AUDIT_2026-09-10.md`
- Stage 2: `reviews/STAGE_02_REVIVAL_NOVELTY_GATE_2026-09-10.md`
- Stage 3: `reviews/STAGE_03_REVIVAL_MECHANISM_SEARCH_2026-09-10.md`
- Stage-3 model: `model/REVIVAL_STAGE3_SELECTED_MECHANISM_2026-09-10.md`

Generic compatibility-induced differentiation, continuous standards policy, coalition-induced downstream strategy, standards breadth/depth, and generic policy-to-strategy-to-policy-reversal claims remain killed.

## C1 model retained unchanged

For `i!=j`,

`K_ij=c0+lambda*phi(x_i-x_j)/Tau_ij(rho,s)-v*M_ij(rho,s)`,

where within a multi-country bloc `M_ij=s_C/s_bar` and across blocs `M_ij=0`.

No nonlinear realization map, policy cost, home bias, asymmetry, bargaining, extra market, no-crossing restriction, dynamic selection rule, or second policy dimension has been added.

## Permanent first Stage-4A counterexample

At low repositioning cost `gamma=.03`, the FULL-SU full-depth location game has at least two distinct global-BR pure-strategy Nash equilibria. At `(v,gamma)=(.12,.03)` they give opposite signs for SU-member welfare relative to IS. Therefore the old low-gamma FULL stable-set reversal and `v_FULL≈.133687` threshold are not selection-free model implications.

Permanent regression:

`verification/stage04a_independent_multiplicity_red_team.py`.

No implicit selection rule may suppress this equilibrium.

## Stage 4R repair authority

- model repair scope: `model/REVIVAL_STAGE4R_C1_MULTIPLICITY_REPAIR_2026-09-10.md`
- construction verifier: `verification/stage04r_multiplicity_safe_region.py`
- review: `reviews/STAGE_04R_REVIVAL_C1_MULTIPLICITY_REPAIR_2026-09-10.md`
- decision record: `decisions/STAGE04R_REVIVAL_DECISIONS.md`

Stage 4R kept the model unchanged and narrowed theorem scope to higher repositioning-cost curvature `gamma`.

The repaired headline point is `(v,gamma)=(.11,.10)`.

Construction welfare:

- IS: `.1432822599`;
- FULL SU member: `.1433644618`;
- FULL SU outsider: `.1419734070`;
- FULL SW: `.1425185185`.

At `gamma=.10`, construction thresholds are

- `v_FIX=1/15=.0666666667`;
- `v_EXO-HIST≈.0993400328`;
- `v_FULL≈.1196400688`.

## Repeat Stage 4A authority

- independent red-team: `verification/stage04a_repeat_high_gamma_red_team.py`
- review: `reviews/STAGE_04A_REPEAT_REVIVAL_C1_MATH_RED_TEAM_2026-09-15.md`
- theorem certificates: `theorem_certificates/STAGE04A_REPEAT_REVIVAL_C1_CERTIFICATES_2026-09-15.md`
- decision record: `decisions/STAGE04A_REPEAT_REVIVAL_DECISIONS_2026-09-15.md`

Repeat Stage 4A verdict:

**GO — MATHEMATICAL ADVERSARIAL CERTIFICATION PASS.**

Certified repaired scope:

1. low-`gamma` crossing multiplicity remains a permanent failure of global uniqueness;
2. the higher-`gamma` stress box and 81 additional SU policy histories reveal no second global-BR pure Nash under the independent attack;
3. at `(v,gamma)=(.11,.10)`, IS, SU, and SW each have one attacked location Nash under the independent alternative-equilibrium search;
4. downstream-re-solved SU depth attacks preserve `(s_12,s_3)=(.25,.25)`;
5. FULL bilateral SUs are stable under the frozen strict-blocking correspondence at the repaired witness, while B-FIX retains IS against the SU pair block;
6. independent threshold reconstruction reproduces `v_EXO-HIST≈.0993400329`, `v_FULL≈.1196400688`, and exact `v_FIX=1/15`.

The project does **not** claim analytic/global uniqueness for all `gamma` or all parameter values.

## Stage 6 authority

- updated prior-art/result matrix: `docs/REVIVAL_STAGE6_NOVELTY_REKILL_MATRIX_2026-09-15.md`
- review: `reviews/STAGE_06_REVIVAL_NOVELTY_REKILL_2026-09-15.md`
- decision record: `decisions/STAGE06_REVIVAL_DECISIONS_2026-09-15.md`

Stage 6 verdict:

**GO — GO TO STAGE 7 WELFARE / GENERALITY / INSTITUTIONAL VALIDATION.**

### Stage-6 binding novelty boundary

The following are not available as headline novelty:

- compatibility-induced product differentiation;
- interoperability/network benefit versus competition trade-offs;
- continuous government compatibility/standards policy;
- coalition/interoperability membership followed by an endogenous action;
- standards breadth/depth as a coalition-stability margin;
- regional versus multilateral standards stability;
- costly product repositioning itself;
- continuous standardization changing downstream strategy;
- private versus social preferred standards depth/participation.

This boundary is strengthened by the 2026 Menegaki–Serfes work on complementary-goods coalition stability, breadth/depth coordination, and voluntary interoperability-standard participation.

### Only surviving core contribution

> **In a government standards-coalition game with endogenous realized-interoperability depth, post-policy costly product repositioning can remain consequential after policy adjustment: in a selection-safe higher-redesign-cost region, allowing repositioning shifts the bilateral-union versus international-standardization national-welfare blocking threshold relative to the otherwise identical fixed-position policy game, and can therefore change the stable standards partition.**

This is a narrow full-game/result-level contribution. It is not setup novelty.

### Strongest current novelty threat

Mandatory comparison at later manuscript/submission stages:

- Menegaki & Serfes (2026), *Coalition Stability with Complementary Goods*;
- Menegaki & Serfes (2026), *Breadth, Depth, and Coalition Stability in Complementary Oligopoly*;
- Menegaki & Serfes, current working-paper listing *The Architecture of Voluntary Standards in Complementary Oligopoly*.

If a public later version contains an endogenous product-design/repositioning margin that shifts an interoperability-coalition blocking threshold, Stage 6 must be reopened.

Own prior art also remains binding:

- `standardization-scope-direction-innovation` kills generic continuous-standardization -> downstream-strategy -> policy-reversal novelty;
- `private-compatibility-standards-coalitions` kills generic formal-partition -> private response -> welfare -> stability novelty.

## Formal-verification applicability

Status: **FORMALIZATION APPLICABLE**.

Future Stage-7.5A targets include:

- exact B-FIX factorization `v_FIX=1/15`;
- exact IS welfare derivative and sufficient condition `v>1/18`;
- strict-welfare inequalities -> blocking/stability logic;
- exact threshold-ordering components separable from numerical location continuation;
- any analytic high-`gamma` uniqueness condition later added to theorem scope.

There is no formal-verification PASS yet.

## Current routing

**NEXT: STAGE 7 — WELFARE / GENERALITY / INSTITUTIONAL VALIDATION.**

Stage 7 may interpret only the surviving threshold/stability result. Theory freeze, Stage 7.5A formal/quantifier certification, journal positioning, manuscript rehabilitation, and submission remain blocked.