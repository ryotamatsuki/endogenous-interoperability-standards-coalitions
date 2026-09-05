# Project State

Last updated: 2026-09-05

## Canonical status

- Project: Endogenous Interoperability and Standards Coalitions
- Working title: **Standards Coalitions and Strategic Product Repositioning**
- Canonical workflow: `ryotamatsuki/research-paper-workflow` **v1.2**
- Workflow release tag: `v1.2`
- Previous theory freeze: `CESD-THEORY-FREEZE-2026-09-04-v2` — **STALE**
- Theory status: **REOPENED — AFFINE-DEMAND BERTRAND RE-FOUNDATION PASSED MINIMAL MODEL GATE**
- Stage 5RR: **NO-GO — linear localized continuation terminated**
- Stage 4R3Q: **NO-GO — pure-quadratic localized continuation terminated**
- Stage 3R4: **GO — affine-demand Bertrand re-foundation selected**
- Stage 4R4A: **GO — continuation, repositioning, and result-level novelty gate passed**
- Stage 11R2: **STALE / REOPENED**
- Stage 12 journal positioning: **administratively complete, submission authorization suspended**
- Stage 13: **CLOSURE REVOKED**
- Stage 14 submission QA authorized: **NO**
- Primary intended target only if the rebuilt theory survives: **International Journal of Industrial Organization (IJIO)**

## Terminated continuation architectures

The following pure-strategy spatial continuation architectures are permanently non-authoritative for this paper:

1. unrestricted all-product linear Salop;
2. localized linear Salop;
3. localized pure-quadratic Salop.

The repeated continuation failures are treated as architecture-level evidence. No further transport-curvature or consideration-set patch is authorized.

## Current architecture

Stage 4R4A replaces discrete spatial consumer allocation with a quadratic representative-consumer demand system while keeping the circle as product-characteristic space.

For fixed regime `rho`, standards depth `s`, locations `x`, prices `p`, and quantities `q>=0`, demand solves

`max a1'q - (1/2)q'K(rho,s,x)q - p'q`.

The old policy maps `Tau(reg,s)` and `G(reg)` are retained. The new effective curvature matrix is

`K_ii=b`,

`K_ij=c0 + lambda*phi(x_i-x_j)/Tau_ij(reg,s) - v G_ij(reg)`,

with

`phi(z)=[1+cos(2 pi z)]/2`.

Stage 4R4A witness parameters are

- `a=2`;
- `b=10`;
- `c0=0.30`;
- `lambda=0.50`;
- `v=0.08`;
- `gamma=0.03`;
- `tbar=1`;
- `sbar=0.25`;
- anchors `h=(1/6,1/2,5/6)`.

These replace the old Salop calibration for the rebuilt branch.

## Stage 4R4A Gate A — demand well-posedness

Across the complete Stage 4 policy/location domain,

`Tau_ij in [3/4,5/4]`,

and every off-diagonal curvature lies in

`[c_min,c_max]=[0.22,0.966666...]`.

The global inequalities

`b>2c_max`,

`b*c_min>c_max^2`,

`b-2c_max+c_min>0`

imply strict positive definiteness of `K`, negative off-diagonal elements of `D=K^{-1}`, and positive row sums of `D`. Hence the interior affine system has ordinary substitute signs and the consumer quadratic program has a unique solution for every nonnegative price vector.

Nonnegative demand is defined globally from KKT active sets. Negative-demand truncation and solver filtering are prohibited.

Gate A: **PASS**.

## Stage 4R4A Gate B — Bertrand continuation

For an interior history,

`q=D(a1-p)`

and the one-product-per-firm Bertrand FOCs imply

`p*=[D+diag(D)]^{-1}D(a1)`.

The current primitive domain produces positive equilibrium prices and quantities. The project uses the globally nonnegative representative-consumer affine-demand continuation, with Farahat–Perakis (2010) as the standard existence/uniqueness reference and an independent finite KKT demand evaluator plus direct global price-deviation regression.

The affine-demand continuation is an infrastructure primitive, not a novelty claim.

Gate B: **PASS**.

## Stage 4R4A Gate C — strategic repositioning

Whole-circle best-response verification gives the qualitative Stage 4R4A location pattern:

- `IS, s_I=sbar`: anchors remain the equilibrium;
- `SW, s=0`: anchors remain the equilibrium;
- `SU_12, s_12=sbar`: firms 1 and 2 move outward from their inherited anchors while firm 3 remains essentially fixed.

Canonical bilateral-standard profile is approximately

`x_SU=(0.1404,0.5263,0.8333)`

versus

`h=(0.1667,0.5000,0.8333)`.

Repositioning is therefore nondegenerate and standards-contingent.

Gate C: **PASS**.

## Stage 4R4A Gate D — minimal reversal and novelty

At fixed anchors, member-1 national welfare satisfies

`W_1(SU_12)-W_1(IS)<0`.

At endogenous location equilibria,

`W_1(SU_12)-W_1(IS)>0`.

At the Stage 4R4A witness the approximate margins are

- fixed positions: `-2.1e-4`;
- endogenous repositioning: `+2.7e-4`.

The outsider loses under the bilateral standard. The strict fixed-negative/full-positive reversal survives all 9 points in

`v in {0.07,0.08,0.09}` × `gamma in {0.025,0.030,0.035}`.

Closest prior-art threats include:

- Ushchev–Zenou (2018): Bertrand competition on an exogenous product-variety network;
- Economides–Skrzypacz (2003 working paper): standards-coalition formation and network competition;
- Baake–Boom (2001): compatibility, network effects, endogenous quality/differentiation, and later prices;
- Barrett–Yang (2001): international standards, redesign costs, network effects, and multi-attribute competition;
- earlier compatible differentiated-product models with endogenous differentiation.

None of these may be described as absent. Current novelty classification remains:

**DISTINCT BUT NARROW**.

The only candidate contribution is the full timing/result loop

`standards architecture -> costly post-standard repositioning -> endogenous substitutability network -> Bertrand competition -> member regime-ranking reversal -> coalition-stability implication`.

Gate D: **PASS, narrow**.

## Authoritative Stage 4R4A artifacts

- `verification/stage04r4a_affine_bertrand_gate.py`
- `reviews/STAGE_04R4A_AFFINE_DEMAND_BERTRAND_CONTINUATION_NOVELTY_2026-09-05.md`
- `decisions/STAGE04R4A_CESD_DECISIONS.md`

## What remains stale

All old Salop-branch equilibrium, welfare, policy, coalition-stability, theory-freeze, referee-gate, and submission objects are historical only, including:

- `Delta_M^(B-T)≈-0.010167`;
- `Delta_M^(FULL)≈+0.001571`;
- old member welfare decomposition;
- old world-welfare ordering;
- old standards-depth optima;
- old coalition thresholds;
- old 9/9 Salop robustness result.

## Current verdict

**STAGE 4R4A GO — DO NOT SUBMIT.**

Next formal stage:

**Stage 5R4 — Endogenous Standards-Depth, Welfare & Coalition Reconstruction.**

Stage 5R4 must rebuild policy depth, location continuation after policy deviations, national/world welfare, and strict-blocking coalition stability from the new affine-demand model only. If the coalition result collapses, default routing is termination rather than another continuation refoundation.
