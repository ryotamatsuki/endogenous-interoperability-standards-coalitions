# Project State

Last updated: 2026-09-05

## Canonical status

- Project: Endogenous Interoperability and Standards Coalitions
- Working title: **Standards Coalitions and Strategic Product Repositioning**
- Canonical workflow: `ryotamatsuki/research-paper-workflow` **v1.2**
- Workflow release tag: `v1.2`
- Previous theory freeze: `CESD-THEORY-FREEZE-2026-09-04-v2`
- Theory status: **REOPENED — LOCALIZED-COMPETITION CONTINUATION HARDENING REQUIRED**
- Stage 4RR: **CONDITIONAL GO — one blocker identified**
- Stage 11R2: **STALE / REOPENED downstream of continuation failure**
- Stage 12 journal positioning: **administratively complete, submission authorization suspended**
- Stage 13: **CLOSURE REVOKED**
- Stage 14 submission QA authorized: **NO**
- Primary intended target after successful repair: **International Journal of Industrial Organization (IJIO)**

## Stage 4RR result

The hostile all-product counterexample remains valid and permanently rejects the old claim that the local interior price system supplies a valid continuation after every feasible location deviation.

The preferred all-product weighted-geodesic extension is coherent as a global choice model but is **not certified**: Stage 4RR could not establish the pure price continuation required for every off-path location history, and the old FOC/SOC/interiority system cannot substitute for that proof.

Stage 4RR therefore selected one bounded repair candidate for hardening:

> **Explicit localized competition.** A consumer on an arc between adjacent product positions considers exactly the two products bounding that arc. If one product captures the whole arc after a price deviation, demand is clipped at the boundary rather than returning `None`. Location-order changes rebuild the adjacency graph.

This is a substantive consideration-set primitive and must be stated and defended. It is not to be described as unrestricted all-product Salop choice.

## Regression evidence

Canonical hostile history:

- IS, `s_I=0.25`;
- `x=(0.4,0.5,5/6)`;
- old candidate `p=(0.25,0.215,0.285)`;
- old firm-2 operating profit `0.0616333...`.

All-product deviation `p_2'=0.174`:

- `q_2'=81/125=0.648`;
- `pi_2'=0.112752`;
- therefore the old price candidate is not Nash under all-product choice.

Explicit localized competition, same deviation:

- `q_2'=511/1500≈0.3406667`;
- `pi_2'=14819/250000=0.059276`;
- therefore this exact hostile deviation is not profitable under the localized primitive.

Authorities:

- `verification/stage04rr_price_continuation_counterexample.py`
- `verification/stage04rr_localized_choice_regression.py`
- `reviews/STAGE_04RR_GLOBAL_PRICE_CONTINUATION_REPAIR_2026-09-05.md`
- `decisions/STAGE04RR_CESD_DECISIONS.md`

## Remaining single blocker

Before any new freeze or downstream welfare/stability work, Stage 5RR must complete a fail-closed active-set continuation solver for the explicit localized game:

1. sort locations and construct arcs;
2. enumerate left-capture / interior / right-capture statuses for all arcs (`3^3=27` before tie refinements);
3. solve the network-share fixed point conditional on each active set;
4. verify active-set inequalities;
5. globally solve each firm's price best response across all active sets;
6. classify each continuation as `SOLVED_EQUILIBRIUM`, `MULTIPLE_EQUILIBRIA`, `SOLVED_NO_EQUILIBRIUM`, `UNRESOLVED`, or `NUMERICAL_FAILURE`;
7. define and test coincident-location/tie cases;
8. use the repaired price continuation to re-run the full unilateral location-deviation problem.

No additional model primitive is authorized in Stage 5RR.

## What remains valid only conditionally

The following old-branch objects remain diagnostics, not theorem/SPNE evidence:

- `Delta_M^(B-T)≈-0.010167`;
- `Delta_M^(FULL)≈+0.001571`;
- reported member welfare decomposition;
- reported world-welfare ordering;
- 9/9 local sign robustness conditional on the old branch.

They must all be recomputed if the repaired continuation changes location or policy equilibrium.

## Current verdict

**STAGE 4RR CONDITIONAL GO — DO NOT SUBMIT.**

Next formal stage: **Stage 5RR — Localized-Competition Continuation Hardening**.
