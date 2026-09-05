# Project State

Last updated: 2026-09-05

## Canonical status

- Project: Endogenous Interoperability and Standards Coalitions
- Working title: **Standards Coalitions and Strategic Product Repositioning**
- Canonical workflow: `ryotamatsuki/research-paper-workflow` **v1.2**
- Workflow release tag: `v1.2`
- Previous theory freeze: `CESD-THEORY-FREEZE-2026-09-04-v2`
- Theory status: **REOPENED — PURE-QUADRATIC LOCALIZED ARCHITECTURE FAILED**
- Stage 5RR: **NO-GO — linear localized continuation terminated**
- Stage 3R3: **GO — pure-quadratic localized transport selected for kill test**
- Stage 4R3Q: **NO-GO — Q1 continuation existence fails at first hostile feasible history**
- Stage 11R2: **STALE / REOPENED downstream of continuation failure**
- Stage 12 journal positioning: **administratively complete, submission authorization suspended**
- Stage 13: **CLOSURE REVOKED**
- Stage 14 submission QA authorized: **NO**
- Primary intended target only if a rebuilt theory survives: **International Journal of Industrial Organization (IJIO)**

## Stage 4R3Q result

Stage 4R3Q tested exactly the architecture selected at Stage 3R3: pure-quadratic localized circular competition with the existing policy-dependent pair friction map.

At the feasible IS history

- `s_I=1/4`;
- `x=(2/5,1/2,5/6)`;
- common `tau=3/4`;
- arc lengths `(1/10,1/3,17/30)`;

a consumer on an arc of length `ell` between adjacent firms `i,j` uses

`u_i=A-p_i-tau*y^2+v*n_i`,

`u_j=A-p_j-tau*(ell-y)^2+v*n_j`.

Under IS the network term is common and cancels pairwise. The raw localized share is

`ell/2 + (p_j-p_i)/(2*tau*ell)`,

clipped to `[0,ell]`.

The unique all-interior stationary price candidate is

`p=(816/17975,1167/28760,7939/86280)`.

It is not Nash. Firm 0 can move from

`p_0=816/17975 ≈ 0.0453964`

to its exact global best response

`p_0'=95727/575200 ≈ 0.166424`,

raising operating profit from

`208896/12924025 ≈ 0.0161634`

to

`539038737/16542752000 ≈ 0.0325846`.

More importantly, the exact Stage 4R3Q verifier enumerates the full finite candidate set for pure Nash equilibrium:

- 27 global arc active states;
- six necessary best-response modes per firm: interior FOC, zero price, four incident arc-share kinks;
- 2440 nonsingular candidate systems solved exactly with SymPy rationals;
- every surviving candidate checked against the exact global best-response correspondence;
- pure price Nash equilibria found: **0**.

Authority:

- `verification/stage04r3q_quadratic_price_nonexistence.py`
- `reviews/STAGE_04R3Q_PURE_QUADRATIC_GLOBAL_CONTINUATION_2026-09-05.md`
- `decisions/STAGE04R3Q_CESD_DECISIONS.md`

## Interpretation

The classical quadratic-distance existence rationale was a legitimate reason to test this architecture, but it is not a theorem for this three-firm localized circular game with unequal off-path arc lengths and policy-dependent pair frictions.

Q1 from Stage 3R3 is false: not every feasible location history admits the pure price continuation required for the intended pure-strategy SPNE.

The failure occurs at the first hostile history, so Stage 4R3Q stops immediately. No further location, policy, welfare, reversal, or coalition-stability calculations are authorized under this architecture.

## What remains historical only

The following old-branch objects are not theorem/SPNE evidence:

- `Delta_M^(B-T)≈-0.010167`;
- `Delta_M^(FULL)≈+0.001571`;
- reported member welfare decomposition;
- reported world-welfare ordering;
- 9/9 local sign robustness conditional on the old linear branch.

## Current verdict

**STAGE 4R3Q NO-GO — DO NOT SUBMIT.**

Do not proceed to Stage 5 on this architecture.

If the project continues, the next formal research action is **Stage 3R4 — Continuation Architecture Re-Selection II**.

Priority reserve families:

1. mixed-price continuation under the original linear architecture;
2. broader redesign of the competition stage with globally defined pure continuation.
