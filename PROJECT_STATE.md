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
- Selected mechanism: **C1 — Realized Interoperability Depth**
- Next canonical stage: **Stage 6 — Novelty Re-Kill**
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

The only surviving novelty family remains a coalition-stability / blocking-threshold result that depends indispensably on strategic product repositioning after endogenous bloc depth choice. Generic compatibility-induced differentiation, continuous standardization policy, coalition-induced downstream strategy, and generic policy-to-strategy-to-policy-reversal claims remain killed.

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

Stage 4R kept the model unchanged and narrowed the theorem domain to higher repositioning-cost curvature `gamma`.

The repaired headline point is

`(v,gamma)=(.11,.10)`.

Stage-4R construction gives FULL-SU location

`x_SU≈(.14246245,.52420422,.83333333)`

with approximate welfare

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

### Certified repaired scope

1. The low-`gamma` crossing equilibrium is independently reproduced and remains a permanent failure of global uniqueness.
2. In the higher-`gamma` full-depth stress box `v in {.09,.10,.11,.12,.13}`, `gamma in {.08,.10,.12}`, independent full-system multi-start + whole-circle deviation search retains one pure Nash per attacked SU history.
3. An additional 81 material SU policy histories spanning zero/intermediate/full depths around the repaired region reveal no second global-BR pure Nash under the independent attack.
4. At `(v,gamma)=(.11,.10)`, independent alternative-equilibrium searches find one attacked location Nash each for IS, SU, and SW.
5. Downstream-re-solved SU unilateral depth attacks preserve the policy candidate `(s_12,s_3)=(.25,.25)`.
6. At the repaired witness, FULL has the bilateral SUs stable under the frozen strict-blocking correspondence, while B-FIX retains IS against SU pair blocking.
7. Independent threshold reconstruction gives `v_EXO-HIST≈.0993400329` and `v_FULL≈.1196400688`, with exact `v_FIX=1/15`.

### Scope limitation

The project does **not** claim analytic/global uniqueness for all `gamma` or all parameter values. The maximum certified statement is a repaired higher-redesign-cost continuation class supported by independent adversarial equilibrium-set and global-BR attacks. Any stronger generality must pass later quantifier/generality and formal-verification gates.

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

**NEXT: STAGE 6 — NOVELTY RE-KILL.**

Stage 6 must assess the repaired high-`gamma` theorem, not the superseded low-`gamma` claim. Theory freeze, journal positioning, manuscript rehabilitation, and submission remain blocked until later workflow gates pass.
