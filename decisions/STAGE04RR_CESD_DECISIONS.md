# Stage 4RR — Global Price-Continuation Repair Decisions

Date: 2026-09-05

Canonical workflow: `ryotamatsuki/research-paper-workflow` v1.2

- D-04RR-01: Main commit `461b7486807ebb22e8ce26227f7f9a9ddbae8adf` is not submission-authoritative because the off-path price continuation was not globally validated.
- D-04RR-02: Previous freeze `CESD-THEORY-FREEZE-2026-09-04-v2` remains reopened for the limited purpose of repairing consumer choice, price continuation, and all downstream equilibrium objects affected by that repair.
- D-04RR-03: Stage 13 closure remains revoked and Stage 14 remains blocked.
- D-04RR-04: `verification/stage04rr_price_continuation_counterexample.py` is a permanent regression test for unrestricted all-product choice.
- D-04RR-05: `None`, invalid interior branch, NaN, nonconvergence, or other solver failure may never be treated as evidence that a price/location deviation is unprofitable.
- D-04RR-06: The all-product weighted-geodesic repair remains mathematically coherent but is **UNRESOLVED**, not certified. The old interior price system is insufficient for its off-path price subgames.
- D-04RR-07: The broader circular spatial-competition literature is treated as an equilibrium-existence warning: feasible locations can generate nonconcave/discontinuous price incentives, so pure continuation existence may not be presumed.
- D-04RR-08: The bounded repair candidate selected for hardening is **explicit localized competition**: consumers on an arc consider exactly the two products bounding that arc.
- D-04RR-09: This localized consideration set is a substantive primitive and must be stated and defended; it is not an implicit theorem of unrestricted Salop choice.
- D-04RR-10: Under localized competition the exact hostile deviation `p_2: 0.215 -> 0.174` at `x=(0.4,0.5,5/6)` yields demand `511/1500≈0.340667` and profit `14819/250000=0.059276`, below the old candidate profit `0.0616333...`. Regression authority: `verification/stage04rr_localized_choice_regression.py`.
- D-04RR-11: Defeating that one counterexample is not a global equilibrium proof. The remaining blocker is a complete 27-pattern arc active-set price solver plus explicit coincident-location/tie handling.
- D-04RR-12: Changing transport-cost curvature or imposing minimum location separation is not authorized in the next step. If localized competition cannot close the continuation with no further primitive change, this architecture returns to `NO-GO` rather than accumulating assumptions.
- D-04RR-13: Old canonical welfare numbers remain conditional diagnostics only; reproducing them is not a success criterion.
- D-04RR-14: A new theory freeze is prohibited until price, location, policy, welfare, and coalition stability have all been recomputed and revalidated under the repaired continuation.
- D-04RR-15: The manuscript must distinguish `FULL SU vs IS` consumer incidence from the within-regime causal effect of repositioning `FULL vs B-T`.
- D-04RR-16: The domestic-profit-incidence sensitivity remains a scope warning, not an ownership-robustness result.

## Canonical Stage 4 verdict

**CONDITIONAL GO**

Exactly one blocker:

> Complete and certify the explicit localized-competition active-set price continuation for every off-path history needed to evaluate unilateral location deviations, including boundary and coincident-location cases.

## Routing

**GO TO Stage 5RR — Localized-Competition Continuation Hardening.**

Stage 5RR may change only the consideration-set primitive from ambiguity/unrestricted interpretation to the explicit two-bounding-product localized competition specification and implement its complete continuation solver. No additional theory feature is authorized.
