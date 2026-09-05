# Project State

Last updated: 2026-09-05

## Canonical status

- Project: Endogenous Interoperability and Standards Coalitions
- Working title: **Standards Coalitions and Strategic Product Repositioning**
- Canonical workflow: `ryotamatsuki/research-paper-workflow` **v1.2**
- Workflow release tag: `v1.2`
- Previous theory freeze: `CESD-THEORY-FREEZE-2026-09-04-v2`
- Theory status: **REOPENED — CURRENT CONTINUATION ARCHITECTURE FAILED**
- Stage 4RR: **CONDITIONAL GO completed; localized repair sent to Stage 5RR**
- Stage 5RR: **NO-GO — localized consideration does not restore pure price continuation**
- Stage 11R2: **STALE / REOPENED downstream of continuation failure**
- Stage 12 journal positioning: **administratively complete, submission authorization suspended**
- Stage 13: **CLOSURE REVOKED**
- Stage 14 submission QA authorized: **NO**
- Primary intended target only if a new architecture survives: **International Journal of Industrial Organization (IJIO)**

## Stage 5RR result

Stage 5RR tested exactly one authorized repair: explicit localized competition, where consumers on each positive-length arc compare only the two firms bounding that arc.

This repair fails at the same feasible hostile IS location history:

- `s_I=1/4`;
- `x=(2/5,1/2,5/6)`;
- old price candidate `p=(1/4,43/200,57/200)`.

Even under localized choice, firm 1 (index 0) can raise price from `1/4` to `71/200`, abandon the short `1/10` arc, retain demand `71/300` on its long arc, and raise operating profit from

`1/12 = 0.083333...`

to

`5041/60000 = 0.0840166...`.

More importantly, the localized IS price subgame at this history has no pure Nash equilibrium.

Because each firm's localized demand is the sum of two clipped affine arc shares, each own-price profit is continuous and piecewise quadratic. Any pure best response must therefore lie at an interior FOC, `p_i=0`, or one of four incident arc-share kinks. The exact Stage 5RR verifier enumerates all 27 global arc states and all six necessary optimality equations per firm, solves **2440 nonsingular candidate systems** exactly, and checks every candidate against the exact global best-response correspondence.

Pure price Nash equilibria found: **0**.

Authority:

- `verification/stage05rr_localized_price_nonexistence.py`
- `reviews/STAGE_05RR_LOCALIZED_COMPETITION_HARDENING_2026-09-05.md`
- `decisions/STAGE05RR_CESD_DECISIONS.md`

## Interpretation

The Stage 4RR localized repair removed the originally identified large price-cut deviation by firm 2, but that was not enough. Stage 5RR finds a different exact profitable deviation and then establishes pure-equilibrium nonexistence at the hostile off-path history.

This is a continuation-existence failure, not a small robustness issue. Since the original location game allows this history, the paper cannot claim a pure-strategy SPNE under the localized repair.

Mixed price equilibria are not ruled out. However, moving to mixed continuation, changing transport-cost curvature, restricting the location strategy domain, or replacing the competition microfoundation would be a distinct model architecture. Under canonical workflow v1.2, a second unrelated repair may not be stacked inside Stage 5.

## Literature status of the repair primitive

Localized/limited-information circular competition is a recognized theoretical device. de Frutos, Hamoudi and Jarque (2002, *Regional Science and Urban Economics*, 32(4), 531–540, DOI `10.1016/S0166-0462(01)00094-1`) analyze an oligopoly extension under limited consumer information in which consumers compare only the two closest firms.

Their oligopoly section fixes firms at equidistant locations. It therefore does not provide the missing endogenous-location continuation result needed here.

## What remains valid only conditionally

The following old-branch objects remain historical diagnostics, not theorem/SPNE evidence:

- `Delta_M^(B-T)≈-0.010167`;
- `Delta_M^(FULL)≈+0.001571`;
- reported member welfare decomposition;
- reported world-welfare ordering;
- 9/9 local sign robustness conditional on the old branch.

They cannot be used for submission unless a new continuation architecture is solved and all downstream equilibrium/welfare objects are recomputed.

## Current verdict

**STAGE 5RR NO-GO — DO NOT SUBMIT.**

Stage 6 is not authorized. The current localized-consideration branch terminates here.

Next permissible research action: **return to Stage 3 and compare genuinely distinct continuation architectures, or terminate the paper.**
