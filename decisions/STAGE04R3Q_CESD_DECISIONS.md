# Stage 4R3Q C-ESD Decision Record

Date: 2026-09-05
Workflow: `research-paper-workflow` v1.2
Stage: Stage 4R3Q — Pure-Quadratic Global Continuation Minimal Model Gate

## Decision

**NO-GO.**

The pure-quadratic localized continuation architecture selected at Stage 3R3 is rejected.

## Binding reason

At feasible IS history

- `s_I=1/4`,
- `x=(2/5,1/2,5/6)`,
- `tau=3/4`,

the localized pure-quadratic price subgame has no pure Nash equilibrium.

Exact finite enumeration:

- 27 global arc active states;
- six necessary best-response modes per firm;
- 2440 nonsingular candidate systems solved exactly;
- 0 pure price Nash equilibria.

Authority:

- `verification/stage04r3q_quadratic_price_nonexistence.py`
- `reviews/STAGE_04R3Q_PURE_QUADRATIC_GLOBAL_CONTINUATION_2026-09-05.md`

## Consequences

- Q1 continuation completeness fails.
- Do not proceed to Stage 5 on this architecture.
- Do not solve location, policy, welfare, reversal, or coalition stability under this architecture.
- No new theory freeze is authorized.
- Stage 13/14 remain blocked.
- IJIO submission remains prohibited.

## Next permissible route

Return to **Stage 3R4 — Continuation Architecture Re-Selection II** if research continues.

Priority reserve families:

1. mixed-price continuation under the original linear competition architecture;
2. a broader competition-stage redesign with globally defined pure continuation.

No architecture may be selected solely because it excludes the known hostile history from the strategy set.
