# Stage 4R4A Canonical Decisions

Date: 2026-09-05
Workflow: `ryotamatsuki/research-paper-workflow` v1.2

## Decision 1 — competition architecture

Adopt the Stage 3R4 quadratic representative-consumer / affine-demand Bertrand architecture for the rebuilt theory path.

The discrete Salop consumer-allocation architecture remains terminated and may not be revived inside Stage 4R4A.

## Decision 2 — pairwise curvature map

For the Stage 4R4A minimal model, retain the old `Tau(reg,s)` and `G(reg)` policy maps and define

`K_ii=b`,

`K_ij=c0 + lambda*phi(x_i-x_j)/Tau_ij(reg,s) - v G_ij(reg)` for `i!=j`,

with

`phi(z)=[1+cos(2 pi z)]/2`.

Canonical Stage 4R4A witness parameters:

- `a=2`;
- `b=10`;
- `c0=0.30`;
- `lambda=0.50`;
- `v=0.08`;
- `gamma=0.03`;
- `tbar=1`;
- `sbar=0.25`;
- `h=(1/6,1/2,5/6)`.

These values are an architecture witness, not a continuation of the old Salop calibration.

## Decision 3 — global demand semantics

Demand is the unique solution to

`max_{q>=0} a1'q - (1/2)q'Kq - p'q`.

Negative affine quantities are never admissible. Zero-demand active sets are part of the model and are solved from KKT conditions.

No `None`, NaN, failed optimizer, or invalid active set can be interpreted as an unprofitable deviation.

## Decision 4 — global primitive restrictions

The Stage 4R4A admissible policy box implies

`Tau_ij in [3/4,5/4]` and `K_ij in [0.22,0.966666...]`.

The primitive restrictions

`b>2c_max`,

`b c_min > c_max^2`,

`b-2c_max+c_min>0`

are retained because they deliver uniform strict concavity, positive zero-price demand, and the substitute sign structure of `D=K^{-1}` over the whole upstream strategy domain.

These are global ex-ante architecture restrictions, not location exclusions.

## Decision 5 — Bertrand continuation

Use the globally nonnegative representative-consumer affine-demand continuation. The paper may cite Farahat and Perakis (2010) for the standard existence/uniqueness architecture, while retaining an independent KKT demand evaluator and direct global price-deviation regression.

The affine-demand continuation itself is not a contribution claim.

## Decision 6 — Stage 4R4A result-level witness

At `sbar=0.25`, the Stage 4R4A model delivers:

- `IS`: anchor locations remain the equilibrium;
- `SW` at zero depth: anchor locations remain the equilibrium;
- `SU_12`: the two member firms move away from one another, approximately to `(0.1404,0.5263)`, while the outsider remains at `5/6`.

For member 1,

`W_1(SU_12)-W_1(IS)<0` at fixed anchors,

but

`W_1(SU_12)-W_1(IS)>0` at endogenous location equilibria.

The strict reversal survives all 9 points in the pre-specified local box

`v in {0.07,0.08,0.09}` and `gamma in {0.025,0.030,0.035}`.

This is the only Stage 4R4A economic result authorized for downstream development.

## Decision 7 — novelty classification

Current classification: **DISTINCT BUT NARROW**.

Do not claim novelty from any of the following separately:

- affine demand / quadratic representative consumer;
- unique differentiated-product Bertrand equilibrium;
- compatibility and network effects;
- product-variety networks;
- standards-coalition formation;
- endogenous product differentiation or redesign costs.

The candidate contribution is only the full timing/result loop:

`standards architecture -> costly post-standard repositioning -> endogenous substitutability network -> Bertrand competition -> regime/member-welfare reversal -> coalition-stability implication`.

The strongest identified threats remain Ushchev–Zenou (2018), Economides–Skrzypacz (2003 working paper), Baake–Boom (2001), Barrett–Yang (2001), and earlier compatibility/endogenous-differentiation work.

## Decision 8 — downstream authority

Stage 4R4A verdict: **GO — GO TO FULL POLICY / COALITION REBUILD**.

Next formal stage: **Stage 5R4 — Endogenous Standards-Depth, Welfare & Coalition Reconstruction**.

All old Salop policy optima, welfare tables, reversal magnitudes, coalition thresholds, theory freeze, referee gates, and submission artifacts remain stale.

If Stage 5R4 fails to produce a nondegenerate coalition/stability result under the new architecture, the default route is termination rather than another continuation refoundation.
