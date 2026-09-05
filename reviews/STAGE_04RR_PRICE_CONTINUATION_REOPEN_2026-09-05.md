# Stage 4RR — Price-Continuation Reopen

Date: 2026-09-05

Audited main commit: `461b7486807ebb22e8ce26227f7f9a9ddbae8adf`

Previous freeze: `CESD-THEORY-FREEZE-2026-09-04-v2`

## Executive verdict

**MAJOR-REOPEN. DO NOT SUBMIT.**

The prior continuation verification does not establish a price Nash equilibrium after every unilateral location deviation. The failure is substantive because location best responses, policy values, and coalition stability require correct off-path price continuations.

## Confirmed counterexample

Under the canonical IS parameters with `s_I=0.25`, let

`x=(0.4, 0.5, 5/6)`.

The manuscript's local adjacent-arc system returns

`p=(0.25, 0.215, 0.285)` and `q=(1/3, 43/150, 19/50)`.

Because all firms are in the same network under IS, `v n_i` is common across products and cancels from consumer comparisons. Under the standard Salop interpretation in which every consumer may choose every product, firm 2 can choose

`p_2'=0.174=87/500`.

Direct circular delivered-cost comparison gives

`q_2'=81/125=0.648`.

Hence

- local-branch operating profit: `(43/200)(43/150)=1849/30000≈0.0616333`;
- deviating operating profit: `(87/500)(81/125)=7047/62500=0.112752`.

The price candidate is therefore not a Nash equilibrium of the unrestricted all-product price game at this location profile.

Regression file: `verification/stage04rr_price_continuation_counterexample.py`.

## Why the previous whole-circle test missed it

`verification/stage04_cesd_minimal.py::profits_general` computes the affine adjacent-arc price candidate and returns `None` whenever a quantity, price, or adjacent indifferent point exits the maintained interior branch.

`verification/stage04r_cesd_continuation_repair.py::best_deviation_continuous` then maps such an outcome to `None`, while its scalar optimizer assigns a large penalty rather than evaluating the true continuation profit. `max_policy_continuation_gain` similarly penalizes `dev is None`.

Thus the previous procedure searched the whole **location circle** but not the whole **price-continuation game**. Deviations that leave the maintained local interior price branch were silently excluded from the profitability comparison.

## Mathematical consequence

The current Proposition `Regular price equilibrium` proves at most a stationary/interior solution on a maintained adjacent-market branch. Positivity, negative own-price second derivative on that branch, and interior adjacent indifferent points do not rule out a large price deviation that changes the set of products competing for a consumer.

Accordingly, the following claims are suspended:

1. unrestricted price Nash equilibrium after arbitrary location deviations;
2. whole-circle location Nash equilibrium;
3. policy-stage SPNE values;
4. coalition-stability conclusions based on those values.

## What the counterexample does not prove

It does **not** prove that the headline reversal is false. The published branch arithmetic, canonical welfare decomposition, world-welfare ordering, and 9/9 local sign checks remain reproducible conditional on the maintained interior continuation. They simply no longer certify an SPNE.

## Repair choice

The repair will not silently impose an adjacent-only purchase restriction merely to preserve the existing formulas. The primary repair target is the standard all-product consumer choice interpretation.

Because heterogeneous `tau_ij` was originally defined only through adjacent arc comparisons, the repaired model must first define a global delivered-cost object for non-neighbor products. The preferred candidate is a weighted geodesic on the circle: each arc between adjacent product locations carries the policy-induced friction density for its endpoint pair, and a consumer may reach any product along the cheaper clockwise/counterclockwise weighted path. This nests the canonical homogeneous IS case and makes non-neighbor choice well-defined.

An adjacent-only segmented-market model remains a possible alternative only if the all-product formulation proves analytically or economically unsuitable; adopting it would require an explicit model change and renewed novelty/institutional review.

## Required revalidation sequence

1. Global consumer-choice definition.
2. Price subgame active-set / corner characterization and global best-response test.
3. Repaired location equilibrium.
4. Repaired policy equilibrium.
5. Recompute B-T, FULL, B-EQ, B-X0 and welfare decomposition.
6. Recompute coalition blocking.
7. Re-run robustness and hostile referee gate.
8. Only then issue a new theory freeze and re-integrate the manuscript.

## Additional wording correction

The manuscript must distinguish two comparisons:

- `FULL SU vs IS`: member consumers lose in the reported canonical regime comparison;
- `FULL SU vs B-T SU`: the effect of allowing repositioning within SU, which need not have the same sign for consumer surplus.

No sentence may equate `consumer loss under SU relative to IS` with `consumer harm caused by repositioning` without a direct within-regime comparison.

## Final verdict

**MAJOR-REOPEN — Stage 4RR Global Price-Continuation Repair required.**
