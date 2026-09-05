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

This is an authorized downstream diagnostic, but after the closest-paper re-kill it is **not by itself a publication-level novelty result**.

## Decision 7 — binding novelty re-kill

The binding addendum is

`reviews/STAGE_04R4A_NOVELTY_REKILL_WOECKENER_2026-09-05.md`.

Woeckener (1999), *Network effects, compatibility decisions, and horizontal product differentiation*, materially absorbs the generic mechanism

`compatibility commitment first -> later product-location differentiation -> softened downstream competition`.

Gabszewicz, Marini and Tarola additionally absorb the generic timing claim that an upstream coalition structure can change later endogenous differentiation and prices.

Therefore the following are prohibited as headline novelty claims:

- standards/compatibility chosen first induces later differentiation;
- compatibility becomes more attractive because firms can subsequently differentiate;
- coalition formation changes later differentiation and prices.

Current classification remains **DISTINCT BUT NARROW**, but only conditionally. The surviving candidate contribution is narrower:

`technical standards coalition -> post-standard costly repositioning -> endogenous substitutability network -> changed national welfare/blocking incentives -> different stable standards coalition or stability threshold`.

The closest-paper set now explicitly includes Woeckener (1999) and Gabszewicz–Marini–Tarola in addition to Ushchev–Zenou, Economides–Skrzypacz, Baake–Boom, Barrett–Yang, and earlier compatibility/endogenous-differentiation work.

## Decision 8 — revised Stage 4R4A verdict

Stage 4R4A verdict is revised to:

**CONDITIONAL GO — CONTINUATION AND REPOSITIONING PASS; PUBLICATION-LEVEL NOVELTY DEPENDS ENTIRELY ON THE STANDARDS-COALITION STABILITY RESULT AT STAGE 5R4.**

This supersedes any earlier Stage 4R4A text that labels the novelty gate an unconditional PASS.

## Decision 9 — Stage 5R4 fatal novelty contract

Next formal stage: **Stage 5R4 — Endogenous Standards-Depth, Welfare & Coalition Reconstruction**.

Using only the new affine-demand architecture, Stage 5R4 must:

1. solve standards-depth choices globally for `IS`, each `SU_ij`, and `SW`;
2. re-solve the location game after every material standards-depth deviation;
3. compute national and world welfare from representative-consumer surplus plus operating profits net of repositioning costs;
4. rebuild strict-blocking coalition stability from scratch;
5. compare the endogenous-position model with an otherwise identical fixed-position benchmark;
6. establish on a nondegenerate parameter region at least one coalition-level result that disappears under fixed positions: a different stable partition, a strict stability-threshold shift, a blocking reversal, or a private-versus-social stability wedge caused specifically by post-standard repositioning.

If Stage 5R4 produces only the Woeckener-type result that compatibility induces more differentiation and can become more attractive, the required verdict is:

**NO-GO — TERMINATE THIS PAPER.**

No further continuation refoundation or automatic Stage 3 repair is authorized after such a failure.

All old Salop policy optima, welfare tables, reversal magnitudes, coalition thresholds, theory freeze, referee gates, and submission artifacts remain stale.