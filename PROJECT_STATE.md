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
- Stage 7: **GO — GO TO STAGE 7.5**
- Stage 7.5: **CONDITIONAL GO — ONE GENERALITY ROBUSTNESS BLOCKER**
- Selected mechanism: **C1 — Realized Interoperability Depth**
- Next canonical action: **Stage 7R — bounded alternative-realization robustness test, then repeat Stage 7.5**
- Submission authorization: **NO**
- Theory freeze: **NONE**
- Stage 7.5A: **BLOCKED pending Stage 7R / repeat Stage 7.5**
- Formal verification: **APPLICABLE; NOT YET IMPLEMENTED/PASSED**

## Relationship to historical branches

`main` remains the canonical terminated history of the prior architecture. PR #65 remains the historical affine-demand conditional-go source and fixed-depth welfare-reversal witness. The revival branch does not rewrite either authority and inherits no old theory freeze, journal selection, referee pass, or submission authorization.

## C1 model retained unchanged

For `i!=j`,

`K_ij=c0+lambda*phi(x_i-x_j)/Tau_ij(rho,s)-v*M_ij(rho,s)`,

where within a multi-country bloc `M_ij=s_C/s_bar` and across blocs `M_ij=0`.

No nonlinear realization map, policy cost, home bias, asymmetry, bargaining, extra market, no-crossing restriction, dynamic selection rule, or second policy dimension has been added to the canonical baseline.

## Permanent first Stage-4A counterexample

At low repositioning cost `gamma=.03`, the FULL-SU full-depth location game has at least two distinct global-BR pure-strategy Nash equilibria. At `(v,gamma)=(.12,.03)` they give opposite signs for SU-member welfare relative to IS. Therefore the old low-gamma FULL stable-set reversal and `v_FULL≈.133687` threshold are not selection-free model implications.

Permanent regression:

`verification/stage04a_independent_multiplicity_red_team.py`.

No implicit selection rule may suppress this equilibrium.

## Stage 4R / repeat Stage 4A certified scope

Stage 4R kept the model unchanged and narrowed theorem scope to higher repositioning-cost curvature `gamma`.

The repaired headline point is `(v,gamma)=(.11,.10)`.

At the repaired point:

- FULL-SU location `x_SU≈(.14246245,.52420422,.83333333)`;
- IS welfare ≈ `.1432822599`;
- FULL SU member welfare ≈ `.1433644618`;
- FULL SU outsider welfare ≈ `.1419734070`;
- FULL SW welfare ≈ `.1425185185`.

Repeat Stage 4A independently certified the repaired higher-`gamma` continuation class against multiplicity/global-deviation attacks on the declared stress domain. It did **not** certify global uniqueness for all `gamma` or all primitives.

Thresholds at `gamma=.10`:

- `v_FIX=1/15=.0666666667` exactly;
- `v_EXO-HIST≈.0993400329`;
- `v_FULL≈.1196400688`.

## Stage 6 novelty authority

- `docs/REVIVAL_STAGE6_NOVELTY_REKILL_MATRIX_2026-09-15.md`
- `reviews/STAGE_06_REVIVAL_NOVELTY_REKILL_2026-09-15.md`
- `decisions/STAGE06_REVIVAL_DECISIONS_2026-09-15.md`

Stage 6 verdict: **GO**.

Only surviving core contribution:

> **In a government standards-coalition game with endogenous realized-interoperability depth, post-policy costly product repositioning can remain consequential after policy adjustment: in a selection-safe higher-redesign-cost region, allowing repositioning shifts the bilateral-union versus international-standardization national-welfare blocking threshold relative to the otherwise identical fixed-position policy game, and can therefore change the stable standards partition.**

Generic compatibility-induced differentiation, continuous standards policy, coalition-induced downstream strategy, standards breadth/depth, regional-versus-multilateral standards stability, and generic policy-to-strategy-to-policy-reversal claims remain killed.

Strongest current novelty threat: the 2026 Menegaki–Serfes complementary-oligopoly standards/coalition program. If a later public version contains the same product-repositioning threshold mechanism, Stage 6 must be reopened.

## Stage 7 welfare / generality / institutional authority

- `verification/stage07_welfare_generality.py`
- `docs/REVIVAL_STAGE7_WELFARE_GENERALITY_INSTITUTIONAL_2026-09-15.md`
- `reviews/STAGE_07_REVIVAL_WELFARE_GENERALITY_INSTITUTIONAL_2026-09-15.md`
- `decisions/STAGE07_REVIVAL_DECISIONS_2026-09-15.md`

Stage 7 verdict: **GO — GO TO STAGE 7.5**.

At `(v,gamma)=(.11,.10)` the FULL-SU versus IS member-welfare gain is approximately:

- domestic profit `+.00007085`;
- domestic consumer-surplus share `+.00001136`;
- national welfare `+.00008220`.

By contrast, B-FIX SU is about `-.00037303` below IS in member national welfare. The economic object is therefore a repositioning-driven coalition-threshold shift, mainly through restored domestic producer rents with a smaller positive consumer-surplus contribution.

The institutional interpretation `depth -> realized interoperability` is defensible in environments with multi-function standards, implementation profiles, and conformance/interoperability testing. The literal linear map `chi(s)=s/s_bar` is only a reduced-form normalization.

Essential economic ingredients identified at Stage 7:

1. intensive interoperability/harmonization margin;
2. compatibility gain from depth;
3. competitive compression from harmonization;
4. separate costly post-policy design margin;
5. national objectives combining domestic consumer surplus and producer profit;
6. selection-safe continuation.

No general theorem is established for arbitrary demand, arbitrary realization maps, asymmetric countries, or arbitrary redesign costs.

## Stage 7.5 authority

- review: `reviews/STAGE_075_REVIVAL_FULL_THEORY_FREEZE_DECISION_2026-09-15.md`
- decision record: `decisions/STAGE075_REVIVAL_DECISIONS_2026-09-15.md`

Stage 7.5 verdict:

**CONDITIONAL GO.**

The project passes the following full-paper tests:

- the core result can be stated without model-specific notation;
- the minimal strategic chain is economically coherent;
- the welfare/organizational implication is substantive despite small local level effects;
- the surviving novelty is a full-game threshold result, not setup novelty;
- institutional motivation exists for an intensive realized-interoperability margin.

Exact blocker:

> **The surviving coalition-threshold mechanism has not yet survived any credible alternative functional formulation outside the current baseline architecture.**

This is the only authorized Stage-7.5 blocker.

## Stage 7R authorized robustness test

Stage 7R may alter **only** the realization map for a robustness exercise, while keeping the baseline model unchanged as canonical.

Pre-specified alternative:

`chi_alt(s)=2(s/s_bar)-(s/s_bar)^2`, `s in [0,s_bar]`.

Properties:

- smooth;
- monotone;
- concave;
- `chi_alt(0)=0`;
- `chi_alt(s_bar)=1`.

Passing requirement:

- re-solve B-FIX and FULL on a declared selection-safe higher-`gamma` test domain;
- preserve well-defined continuation/policy equilibria under the alternative map;
- obtain a strict B-FIX/FULL blocking-threshold difference or equivalent coalition-stability difference;
- do not retune parameters after observing the result merely to recover the headline ranking.

No asymmetry, policy cost, extra market, bargaining, new strategic variable, no-crossing restriction, selection rule, or second robustness modification is authorized in this cycle.

If the alternative-realization test passes, repeat Stage 7.5. If it fails materially, do not grant full-theory-freeze authorization on the baseline alone without reassessing scope.

## Formal-verification applicability

Status: **FORMALIZATION APPLICABLE**.

Future Stage-7.5A targets include:

- exact B-FIX factorization `v_FIX=1/15`;
- exact IS welfare derivative and sufficient condition `v>1/18`;
- strict-welfare inequalities -> blocking/stability logic;
- exact threshold-ordering components separable from numerical location continuation;
- any analytic high-`gamma` uniqueness condition later added to theorem scope.

There is no Formal Verification PASS yet. Lean does not substitute for the Stage-7R economic robustness test.

## Current routing

**NEXT: STAGE 7R — ONE BOUNDED ALTERNATIVE-REALIZATION ROBUSTNESS TEST.**

Then repeat Stage 7.5. Stage 7.5A, Stage 8 theory freeze, journal positioning, manuscript rehabilitation, and submission authorization remain blocked.