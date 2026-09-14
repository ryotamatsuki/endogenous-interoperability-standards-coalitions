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
- Stage 7R: **GO — ALTERNATIVE-REALIZATION ROBUSTNESS PASS**
- Selected mechanism: **C1 — Realized Interoperability Depth**
- Next canonical action: **REPEAT STAGE 7.5 — Full-Theory Freeze Decision**
- Submission authorization: **NO**
- Theory freeze: **NONE**
- Stage 7.5A: **BLOCKED pending repeat Stage 7.5**
- Formal verification: **APPLICABLE; NOT YET IMPLEMENTED/PASSED**

## Relationship to historical branches

`main` remains the canonical terminated history of the prior architecture. PR #65 remains the historical affine-demand conditional-go source and fixed-depth welfare-reversal witness. The revival branch does not rewrite either authority and inherits no old theory freeze, journal selection, referee pass, or submission authorization.

## Canonical C1 baseline

For `i!=j`,

`K_ij=c0+lambda*phi(x_i-x_j)/Tau_ij(rho,s)-v*M_ij(rho,s)`,

where within a multi-country bloc `M_ij=s_C/s_bar` and across blocs `M_ij=0`.

No nonlinear realization map, policy cost, home bias, asymmetry, bargaining, extra market, no-crossing restriction, dynamic selection rule, or second policy dimension has been added to the canonical baseline. The nonlinear realization map used at Stage 7R is a robustness exercise only.

## Permanent first Stage-4A counterexample

At low repositioning cost `gamma=.03`, the FULL-SU full-depth location game has at least two distinct global-BR pure-strategy Nash equilibria. At `(v,gamma)=(.12,.03)` they give opposite signs for SU-member welfare relative to IS. Therefore the old low-gamma FULL stable-set reversal and `v_FULL≈.133687` threshold are not selection-free model implications.

Permanent regression:

`verification/stage04a_independent_multiplicity_red_team.py`.

No implicit selection rule may suppress this equilibrium.

## Stage 4R / repeat Stage 4A certified scope

Stage 4R kept the model unchanged and narrowed theorem scope to higher repositioning-cost curvature `gamma`.

The repaired baseline headline point is `(v,gamma)=(.11,.10)`.

At the repaired point:

- FULL-SU location `x_SU≈(.14246245,.52420422,.83333333)`;
- IS welfare ≈ `.1432822599`;
- FULL SU member welfare ≈ `.1433644618`;
- FULL SU outsider welfare ≈ `.1419734070`;
- FULL SW welfare ≈ `.1425185185`.

Repeat Stage 4A independently certified the repaired higher-`gamma` continuation class against multiplicity/global-deviation attacks on the declared stress domain. It did **not** certify global uniqueness for all `gamma` or all primitives.

Baseline thresholds at `gamma=.10`:

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

## Stage 7 welfare / institutional authority

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

The institutional interpretation `depth -> realized interoperability` is defensible in environments with multi-function standards, implementation profiles, and conformance/interoperability testing. The literal linear baseline map `chi(s)=s/s_bar` is a reduced-form normalization.

## Stage 7.5 authority

- review: `reviews/STAGE_075_REVIVAL_FULL_THEORY_FREEZE_DECISION_2026-09-15.md`
- decision record: `decisions/STAGE075_REVIVAL_DECISIONS_2026-09-15.md`

Stage 7.5 verdict: **CONDITIONAL GO**.

Exact blocker:

> **The surviving coalition-threshold mechanism had not yet survived any credible alternative functional formulation outside the current baseline architecture.**

Exactly one repair was authorized: replace only the linear realization map in a robustness exercise by

`chi_alt(s)=2(s/s_bar)-(s/s_bar)^2`.

## Stage 7R authority

- verifier: `verification/stage07r_alternative_realization_robustness.py`
- review: `reviews/STAGE_07R_REVIVAL_ALTERNATIVE_REALIZATION_2026-09-15.md`
- decision record: `decisions/STAGE07R_REVIVAL_DECISIONS_2026-09-15.md`

Stage 7R verdict:

**GO — ALTERNATIVE-REALIZATION ROBUSTNESS PASS.**

The Stage-7.5 blocker is resolved without changing the canonical baseline model.

Alternative robustness map:

`chi_alt(s)=2(s/s_bar)-(s/s_bar)^2`.

Because `chi_alt'(s_bar)=0`, policy was re-optimized from zero rather than inherited from the baseline.

At `gamma=.10`, the alternative-realization SU-vs-IS member-welfare thresholds are approximately:

- `v_FIX_alt≈.05133198`;
- `v_FULL_alt≈.10666955`.

Hence

`v_FULL_alt > v_FIX_alt`.

At the transparent same-primitive witness `(v,gamma)=(.08,.10)`:

### B-FIX

- optimized IS depth ≈ `.17777483`;
- optimized SU member depth ≈ `.19091946`;
- optimized SU outsider depth = `.25`;
- `W_M(SU)-W(IS)≈-.000205416`.

### FULL

- optimized IS depth ≈ `.17777483`;
- optimized SU member depth = `.25`;
- optimized SU outsider depth = `.25`;
- `W_M(SU)-W(IS)≈+.000195579`.

Thus product repositioning continues to shift the government coalition-blocking threshold and changes the SU-vs-IS coalition comparison under a credible nonlinear realization map.

Selection-safety attack under the alternative formulation:

- `v in {.06,.08,.10,.11}`;
- `s_12 in {0,.0625,.125,.1875,.25}`;
- `s_3=.25`;
- `gamma=.10`;
- 20 material SU histories total.

A dispersed full-system multi-start plus whole-circle unilateral-deviation audit retained exactly one global-BR pure SU location Nash at every attacked history.

This is finite robustness evidence. It does not establish a theorem for arbitrary monotone `chi`, arbitrary demand, arbitrary product geometry, country asymmetry, or all redesign-cost values.

## Formal-verification applicability

Status: **FORMALIZATION APPLICABLE**.

Future Stage-7.5A targets include:

- exact baseline B-FIX factorization `v_FIX=1/15`;
- exact baseline IS welfare derivative and sufficient condition `v>1/18`;
- strict-welfare inequalities -> blocking/stability logic;
- exact threshold-ordering components separable from numerical location continuation;
- the statement-fidelity boundary between baseline certified theorems and Stage-7R robustness evidence.

There is no Formal Verification PASS yet.

## Current routing

**NEXT: REPEAT STAGE 7.5 — FULL-THEORY FREEZE DECISION.**

If the repeat Stage 7.5 issues `GO`, the next stage is Stage 7.5A Generality / Quantifier Red-Team plus the embedded Formal Verification Gate. Stage 8 theory freeze, journal positioning, manuscript rehabilitation, and submission authorization remain blocked.