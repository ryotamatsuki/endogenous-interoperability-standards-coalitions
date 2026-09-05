# Stage 4RR — Global Price-Continuation Repair Specification

Date: 2026-09-05

Status: **OPEN RESEARCH SPECIFICATION — NOT A THEORY FREEZE**

## Objective

Replace the maintained adjacent-interior continuation with a price game that is defined after every admissible location profile and every unilateral price deviation required by SPNE.

## Primary consumer-choice specification

Consumers remain uniformly distributed on the physical unit circle and may choose **any** of the three products.

For a fixed location profile, order the firms around the circle. Each physical arc whose endpoints are adjacent firms `i,j` carries local friction density `tau_ij(rho,s)`. For a consumer at point `y`, define the adaptation/transport cost to product `i` as the cheaper clockwise/counterclockwise line integral of these local friction densities from `y` to `x_i`.

Denote this weighted geodesic by `d_Tau(y,x_i;x,rho,s)`. The repaired utility candidate is

`u_i(y)=A-p_i-d_Tau(y,x_i;x,rho,s)+v n_i`,

with `n=G_rho q`.

Consumer demand is the measure of consumers for whom product `i` attains the maximum utility, with measure-zero ties split by a fixed neutral rule.

This definition:

- permits non-neighbor purchases;
- remains defined when a price deviation causes a firm to leapfrog a neighbor in market coverage;
- nests the homogeneous canonical IS metric, where `d_Tau=(tbar-s_I)d_c`;
- preserves the original policy-induced pairwise friction map on physical arcs.

Coincident product locations require a separate deterministic tie convention and must be included in the strategy space unless formally excluded for an independent economic reason.

## Price-subgame requirements

A candidate price continuation is admissible only if every firm's price is a **global** best response over its full feasible price set, using the all-product demand system above and resolving the network fixed point consistently.

The repair must explicitly handle:

1. active-set changes in which one product captures consumers beyond an immediate neighbor;
2. zero-demand products;
3. boundary market shares;
4. discontinuities/kinks at active-set changes;
5. possible nonexistence of pure price equilibrium at some location profiles.

A local FOC plus negative local second derivative is not sufficient.

## Pure-equilibrium existence gate

Before recomputing the location game, determine whether the repaired linear-spatial price subgame admits a pure equilibrium at every location profile needed to evaluate unilateral location deviations from candidate equilibria.

If pure continuation fails on economically relevant deviations, the project must choose explicitly among:

- mixed-price continuations;
- a different globally well-behaved demand/transport specification;
- a justified restriction of the location strategy space;
- an explicit local-choice/segmented-market model.

No option may be selected solely because it reproduces the old canonical numbers.

## Alternative local-choice model

The original equations can be completed as a segmented local-choice model in which consumers on an arc may purchase only from the two products bounding that arc. If adopted, arc demand must be clipped at 0 and the full arc length when the indifferent point leaves the interval, and the price subgame must be solved with these corners.

This route is mathematically smaller but economically more restrictive than standard Salop. It therefore requires renewed institutional interpretation and novelty review and is **not** the default repair.

## Downstream success criteria

Stage 4RR closes only if:

- consumer demand is globally defined;
- the relevant price continuations are genuine equilibria;
- no location deviation is discarded because a local formula returns `None`;
- location equilibrium is re-established;
- policy equilibrium is re-established;
- headline welfare and blocking claims are recomputed from the repaired game.

The old values are comparison diagnostics, not targets.
