# Project State

Last updated: 2026-09-10

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
- Selected mechanism: **C1 — Realized Interoperability Depth**
- Next canonical stage: **Stage 4A repeat independent mathematical adversarial certification**
- Submission authorization: **NO**
- Theory freeze: **NONE**
- Stage 6 novelty re-kill: **BLOCKED pending Stage 4A repeat**
- Formal verification: **APPLICABLE; NOT YET IMPLEMENTED/PASSED**

## Relationship to historical branches

`main` remains the canonical terminated history of the prior architecture. PR #65 remains the historical affine-demand conditional-go source and fixed-depth welfare-reversal witness. The revival branch does not rewrite either authority and inherits no old theory freeze, journal selection, referee pass, or submission authorization.

## Stage 0–3 authority

- Stage 0: `reviews/STAGE_00_REVIVAL_IDEA_INTAKE_2026-09-10.md`
- Stage 1: `reviews/STAGE_01_REVIVAL_SOURCE_MATHEMATICAL_AUDIT_2026-09-10.md`
- Stage 2: `reviews/STAGE_02_REVIVAL_NOVELTY_GATE_2026-09-10.md`
- Stage 3: `reviews/STAGE_03_REVIVAL_MECHANISM_SEARCH_2026-09-10.md`
- Stage-3 model: `model/REVIVAL_STAGE3_SELECTED_MECHANISM_2026-09-10.md`

The only surviving novelty family remains an absorption/non-absorption or coalition-stability result that depends indispensably on strategic product repositioning after endogenous bloc depth choice. Generic compatibility-induced differentiation, continuous standardization policy, coalition-induced downstream strategy, and generic policy-to-strategy-to-policy-reversal claims remain killed.

## C1 model retained unchanged

For `i!=j`,

`K_ij=c0+lambda*phi(x_i-x_j)/Tau_ij(rho,s)-v*M_ij(rho,s)`,

where within a multi-country bloc `M_ij=s_C/s_bar` and across blocs `M_ij=0`.

No nonlinear realization map, policy cost, home bias, asymmetry, bargaining, extra market, no-crossing restriction, dynamic selection rule, or second policy dimension has been added.

## First Stage-4A blocker retained permanently

At low repositioning cost `gamma=.03`, the FULL-SU full-depth location game has at least two distinct global-BR pure-strategy Nash equilibria. At `(v,gamma)=(.12,.03)` these equilibria give opposite signs for SU-member welfare relative to IS. Therefore the old low-gamma FULL stable-set reversal and `v_FULL≈.133687` threshold are not selection-free model implications.

Permanent regression:

`verification/stage04a_independent_multiplicity_red_team.py`.

No closest-anchor, no-crossing, dynamics, Pareto/welfare, or risk-dominance selection rule is authorized to suppress this equilibrium.

## Stage 4R authority

- model repair scope: `model/REVIVAL_STAGE4R_C1_MULTIPLICITY_REPAIR_2026-09-10.md`
- construction verifier: `verification/stage04r_multiplicity_safe_region.py`
- review: `reviews/STAGE_04R_REVIVAL_C1_MULTIPLICITY_REPAIR_2026-09-10.md`
- decision record: `decisions/STAGE04R_REVIVAL_DECISIONS.md`

Stage 4R verdict:

**GO — REPEAT STAGE 4A.**

## Stage 4R repair logic

The model is not changed. Stage 4R treats `gamma`, the existing quadratic repositioning-cost curvature, as part of the theorem domain and asks whether the crossing-equilibrium problem disappears in a higher-adjustment-cost region.

At `gamma=.05`, a declared construction multi-start audit covers 18 SU policy/parameter histories spanning `v in {.07,.11,.13}` and policy depths from zero through full depth. No alternative global-BR SU equilibrium is found on this finite audit set. This is construction evidence only; `.05` is not claimed to be an analytic uniqueness threshold.

The conservative repaired headline point is

`(v,gamma)=(.11,.10)`.

At FULL SU policy `(s_12,s_3)=(.25,.25)`, the construction search finds one global-BR SU location equilibrium:

`x_SU≈(.14246245,.52420422,.83333333)`.

Approximate national welfare:

- IS: `.1432822599`;
- FULL SU member: `.1433644618`;
- FULL SU outsider: `.1419734070`;
- FULL SW: `.1425185185`.

Thus SU members strictly prefer SU to both IS and SW at the repaired construction point.

## Repaired policy / threshold construction

At `v=.11`, exact IS calculus gives `s_I=.25` because `v>1/18`.

Stage-4R downstream-re-solved full-domain scans give the construction SU policy candidate `(s_12,s_3)=(.25,.25)` and SW candidate `(.25,.25,.25)` at the repaired point.

At `gamma=.10`, the blocking thresholds are:

- `v_FIX=1/15=.0666666667` exactly;
- `v_EXO-HIST≈.0993400328`;
- `v_FULL≈.1196400688`.

Hence

`v_FIX < v_EXO-HIST < v_FULL`,

and the repaired illustration `v=.11` lies strictly between `v_EXO-HIST` and `v_FULL`.

The conceptual headline is narrowed to the **B-FIX versus FULL repositioning-induced blocking/stability-threshold shift after endogenous policy optimization**. B-EXO-HIST remains an auxiliary pre-existing benchmark; it does not establish that endogenous policy is generically necessary.

## What remains uncertified

Stage 4R does **not** yet certify:

- continuous-domain uniqueness of the SU location equilibrium in a higher-`gamma` region;
- absence of non-symmetric alternative equilibria near the repaired point;
- analytic location-equilibrium uniqueness;
- global SU/SW policy best responses beyond construction evidence;
- the repaired `v_FULL` root as a model-level theorem;
- the open-neighborhood / selection-free quantifier.

These are the mandatory targets of the repeat Stage 4A.

## Repeat Stage-4A kill contract

The repeat independent audit must:

1. actively search for crossing and non-symmetric SU equilibria at and around `(v,gamma)=(.11,.10)`;
2. attack a nondegenerate higher-`gamma` neighborhood, not only the single witness;
3. re-solve policy deviations under every additional continuation equilibrium discovered;
4. independently recompute the B-FIX/FULL blocking thresholds;
5. audit the complete strict-blocking stable-set logic;
6. return to Stage 4 or terminate C1 if welfare/stability again depends on equilibrium selection.

No selection rule is available as an automatic fallback.

## Formal-verification applicability

Status remains **FORMALIZATION APPLICABLE**. Future Lean targets, after theorem scope stabilizes, include the exact B-FIX factorization `v_FIX=1/15`, the IS policy inequality `v>1/18`, welfare-to-strict-blocking implications, and any analytic uniqueness/high-`gamma` condition that survives the repeat Stage 4A.

## Current routing

**NEXT: REPEAT STAGE 4A — INDEPENDENT MATHEMATICAL ADVERSARIAL CERTIFICATION.**

Stage 6, Stage 7.5A, theory freeze, journal positioning, manuscript rehabilitation, and submission remain blocked.