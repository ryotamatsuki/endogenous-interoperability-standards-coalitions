# Project State

Last updated: 2026-09-05

## Canonical status

- Project: Endogenous Interoperability and Standards Coalitions
- Working title: **Standards Coalitions and Strategic Product Repositioning**
- Canonical workflow: `ryotamatsuki/research-paper-workflow` v1.1
- Workflow release SHA: `488e5ab06c207909296a7564eaf9066f7f94319c`
- Previous theory freeze: `CESD-THEORY-FREEZE-2026-09-04-v2`
- Theory status: **MAJOR-REOPEN — PRICE CONTINUATION EQUILIBRIUM NOT YET VALIDATED**
- Stage 11R2: **REOPENED AS DOWNSTREAM OF THE PRICE-CONTINUATION FAILURE**
- Stage 12 journal positioning: **administratively complete, but submission authorization suspended**
- Stage 13: **CLOSURE REVOKED pending repaired continuation game**
- Stage 14 submission QA authorized: **NO**
- Primary intended target after successful repair: **International Journal of Industrial Organization (IJIO)**

## Reopen trigger

A hostile audit of main commit `461b7486807ebb22e8ce26227f7f9a9ddbae8adf` identified a valid off-path price deviation under the standard all-product Salop interpretation.

At canonical IS policy `s_I=0.25` and locations

`x=(0.4, 0.5, 5/6)`,

the manuscript's local-adjacent price system returns

`p=(0.25, 0.215, 0.285)` and `q=(1/3, 43/150, 19/50)`.

If firm 2 instead chooses `p_2=0.174`, direct all-product consumer choice gives

`q_2=81/125=0.648`,

so operating profit rises from approximately `0.0616333` to `0.112752`.

Therefore the reported local price candidate is not a price Nash equilibrium at that off-path location profile under the standard Salop choice set.

Regression authority: `verification/stage04rr_price_continuation_counterexample.py`.

## Code-level failure

`verification/stage04_cesd_minimal.py::profits_general` returns `None` when the adjacent-arc interior conditions fail. `verification/stage04r_cesd_continuation_repair.py::best_deviation_continuous` and `max_policy_continuation_gain` then omit such deviations from the profitability comparison. The former "whole-circle" audit therefore verified only deviations whose downstream price candidate stayed on the local interior branch; it did not establish the correct price continuation for every location deviation.

## What remains valid conditionally

The following objects were independently reproduced on the maintained interior branch and are not presently alleged to contain arithmetic errors:

- `Delta_M^(B-T)≈-0.010167`;
- `Delta_M^(FULL)≈+0.001571`;
- the reported member welfare decomposition;
- the reported world-welfare ordering at the canonical branch;
- the 9/9 sign robustness conditional on the same continuation branch.

These are no longer sufficient to support an SPNE or coalition-stability claim until the price continuation is repaired.

## Repair contract

Before any new freeze or submission authorization:

1. Define consumer choice and generalized travel/adaptation cost for **all products** at every location profile, including non-neighbor choice, coincident locations, and order changes; or explicitly adopt and economically defend a different choice-set model.
2. Characterize or globally solve the price subgame for every location profile required by unilateral location deviations. A failed local interior branch may not be treated as an unprofitable deviation.
3. Recompute location best responses using the repaired price continuation.
4. Recompute policy choices, B-T/FULL/B-EQ/B-X0 rankings, welfare decomposition, and coalition blocking.
5. Only if the reversal survives, rerun local robustness and the hostile referee gate.
6. Distinguish `FULL SU vs IS consumer loss` from the causal effect of repositioning (`FULL vs B-T` within a regime).
7. Treat the domestic-profit-incidence sensitivity as a scope limitation; do not claim ownership robustness without re-solving the game under alternative ownership structures.

## Current verdict

**MAJOR-REOPEN — DO NOT SUBMIT.**

The next active research stage is **Stage 4RR — Global Price-Continuation Repair**. Stage 13 and Stage 14 are blocked until Stage 4RR and all affected downstream stages are revalidated.
