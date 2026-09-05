# Stage 4R4B — Affine-Demand Policy, Welfare, Reversal & Coalition Reconstruction

Date: 2026-09-06
Canonical workflow: `ryotamatsuki/research-paper-workflow` v1.2
Parent subgate: Stage 4R4A — `GO`

## 1. Executive verdict

**NO-GO — TERMINATE THIS PAPER.**

The affine-demand re-foundation successfully repairs the downstream Bertrand-continuation defect, and endogenous product repositioning is genuinely nonzero in the standards-union history. But the economic contribution required by Stage 4 does not survive reconstruction.

At the pre-registered transparent normalization

`t_bar=1, s_bar=1/4, beta=1/5, v=1/50, a=1, gamma=1/5`,

the standards-union member bloc chooses the boundary depth

` s_12*=0 `,

while the outsider chooses

` s_3*=s_bar=1/4 `.

The member firms do reposition outward in FULL, but this changes welfare levels only. It does not reverse the member bloc's policy incentive and does not change the coalition-stability ranking relative to either nested benchmark.

International standardization (IS) is strictly preferred by every country to the corresponding SU and SW continuation in `B-T`, `B-X`, and `FULL`. Therefore the full-model coalition result is already available without the interaction of endogenous standard depth and endogenous repositioning.

This violates the Stage-4 success criterion requiring at least one welfare or coalition-stability result that is unavailable from each nested benchmark separately.

Under the binding Stage 3R4 / Stage 4R4A contract, failure here routes to termination, not to a fifth competition-architecture repair.

## 2. Welfare accounting under the affine model

For fixed `(rho,s,y)`, the Stage 4R4A effective curvature matrix is

`K=B-vG_rho`,

with unique Bertrand continuation `(p,q)`.

At the representative-consumer optimum,

`CS = U(q)-p'q = (1/2) q'Kq`.

The inherited model contains three symmetric countries and no home-bias primitive. Therefore the minimal national allocation is

`CS_i = CS/3`.

Firm `i`'s national profit is worldwide operating profit net of its own repositioning cost,

`Pi_i = p_i q_i - gamma y_i^2/2`.

Hence

`W_i = CS/3 + Pi_i`.

No transfer, policy cost, home-market weight, or additional demand shifter is introduced.

## 3. B-T: exact policy result with fixed product positions

Fix inherited anchors `y=0` and consider `SU_12` with outsider depth fixed at `s_3=s_bar=1/4`.

At the anchors all pairwise chordal distances equal `3/2`, so the entire continuation is rational in `s_12` under the frozen parameter normalization.

Let

`Omega_12^BT(s_12)=W_1+W_2`.

Exact symbolic differentiation produces a rational function whose numerator is a degree-16 polynomial on `s_12 in [0,1/4]`.

After the affine change `s_12=t/4`, `t in [0,1]`, all 17 Bernstein coefficients of that numerator are strictly negative. The denominator is positive throughout the maintained regular region.

Therefore

`d Omega_12^BT / d s_12 < 0`

for the entire policy interval, and

` s_12^{BT}=0 `.

At the endpoints, the exact derivative is also strictly negative. This is not a numerical optimizer result.

Authority: `verification/stage04r4b_policy_welfare_coalition.py`.

## 4. FULL: endogenous repositioning does not rescue union depth

For each `s_12` on the Stage-4R4B policy audit grid, with `s_3=s_bar`, the SU location subgame is re-solved.

The symmetric candidate

`y=(-d,d,0)`

is not accepted from FOCs alone. For every audited policy value, each firm's unrestricted unilateral displacement problem on `[-1/2,1/2]` is solved and the candidate must coincide with the global best response.

The member-bloc welfare sequence is strictly decreasing as `s_12` increases from `0` to `1/4`.

Conversely, holding `s_12=0`, outsider welfare rises monotonically with `s_3` on the full audit grid. Hence the canonical FULL policy outcome is

`(s_12*,s_3*)=(0,1/4)`.

At that outcome the location equilibrium is approximately

`y=(-0.002833, +0.002833, 0)`.

Thus repositioning is economically active, but it does not change the union bloc's policy sign.

The reconstructed FULL SU national welfare is approximately

`W_SU^FULL=(0.353837, 0.353837, 0.349450)`.

For comparison, at the same policy vector with fixed positions,

`W_SU^BT=(0.353776, 0.353776, 0.349560)`.

Repositioning raises member welfare slightly and lowers outsider welfare slightly. This is a level effect, not a policy reversal or coalition-stability reversal.

## 5. B-X: zero-depth benchmark

Set all continuous depths to zero but retain the formal standards/network partition and allow repositioning.

For `SU_12`, the location equilibrium is approximately

`y=(-0.000603,+0.000603,0)`,

with

`W_SU^BX=(0.353389,0.353389,0.348681)`.

For IS, symmetry pins `y=0` and

`W_IS=(0.357552,0.357552,0.357552)`.

For symmetric SW at zero depth,

`W_SW^BX=(0.348993,0.348993,0.348993)`.

The key coalition ordering is therefore already present when the continuous depth channel is shut down.

## 6. IS and SW policy reconstruction

### IS

Symmetry pins locations at the inherited anchors. Global IS welfare falls when common depth moves from zero to `s_bar` at the frozen normalization. The IS bloc therefore selects

` s_I*=0 `.

The resulting per-country welfare is approximately `0.357552`.

### SW

At symmetric maximum singleton depths, symmetry gives `y=0`.

A supplemental FULL audit holds the other two singleton depths at `s_bar`, varies one country's depth over the full policy grid, and re-solves the three-firm location game at every deviation. Candidate location equilibria are subjected to unrestricted global best-response checks.

Own national welfare rises monotonically with own singleton depth, so the symmetric policy equilibrium is

` s_1*=s_2*=s_3*=s_bar `.

The resulting per-country welfare is approximately `0.350582`.

Authority: `verification/stage04r4b_sw_full_policy_check.py`.

## 7. Coalition-stability reconstruction

Use the same strict-blocking interpretation as the inherited project: a coalition deviation matters only if every member of the deviating coalition is strictly better off under the continuation of the alternative standards partition.

At the frozen affine witness:

- under `B-X`, every country strictly prefers IS to SU and SW;
- under `B-T`, every country strictly prefers IS to the policy-equilibrium SU and SW continuations;
- under `FULL`, every country again strictly prefers IS to SU and SW.

Thus the grand IS coalition is stable and both SU and SW are blocked by the grand coalition in all three architectures.

The FULL stability conclusion is therefore an immediate qualitative repetition of the benchmark result. Endogenous repositioning changes SU welfare levels but not the coalition ordering.

## 8. Full-model-only result test

The Stage-4 requirement was stronger than merely finding a nonzero derivative or nonzero location move. The project needed at least one substantive result requiring both strategic components.

| Object | B-T | B-X | FULL | Full-model-only? |
|---|---|---|---|---|
| SU member depth | `s_12*=0` | depth disabled | `s_12*=0` | **No** |
| SU outward repositioning | disabled | small/nonzero | larger/nonzero | Mechanism interaction only |
| IS policy | `s_I*=0` | depth disabled | `s_I*=0` | **No** |
| SW policy | maximal singleton depth | depth disabled | maximal singleton depth | **No material reversal** |
| IS vs SU welfare ranking | IS higher | IS higher | IS higher | **No** |
| IS vs SW welfare ranking | IS higher | IS higher | IS higher | **No** |
| coalition stability | IS stable | IS stable | IS stable | **No** |

The only interaction result is quantitative: positive outsider specificity induces more SU-member repositioning and changes welfare magnitudes. That falls below the workflow's contribution threshold and is already close to prior literature on compatibility-induced differentiation.

## 9. Wider hostile parameter audit

A pre-termination sensitivity audit varied `beta`, `v`, and `gamma` across regular cells satisfying the Stage 4R4A global demand inequalities. For the audited cells, SU member welfare remained monotonically decreasing over the union-depth grid when the outsider chooses maximal specificity. No positive member-bloc depth region emerged in the audit.

This grid is not treated as a theorem for the entire parameter space. Its purpose is model-search discipline: after the exact B-T monotonicity result and the canonical FULL failure, there is no evidence justifying another parameter search aimed at manufacturing a reversal.

## 10. Why this is a kill rather than a hardening problem

The failure is not a missing robustness check or one isolated parameter restriction. The rebuilt model already has:

- globally defined demand;
- unique Bertrand continuation;
- genuine endogenous repositioning;
- an endogenous standards-depth game;
- reconstructed consumer surplus and national welfare.

What is missing is the paper's remaining publishable contribution: a welfare or coalition-stability theorem created by the interaction of standard-depth choice and repositioning.

Adding home bias, policy costs, bargaining weights, nonlinear standards benefits, another network-depth channel, asymmetric country weights, or a different welfare allocation now would be feature accumulation targeted at obtaining a desired sign. That is prohibited by Stage 4.

## 11. Candidate-proposition kill table

| Candidate | Result |
|---|---|
| R4B-1: affine model has a well-defined welfare object | **PASS** |
| R4B-2: standards depth changes repositioning | **PASS** |
| R4B-3: endogenous repositioning changes the SU member bloc's optimal depth | **KILL** at the frozen witness; both B-T and FULL choose zero |
| R4B-4: FULL creates a welfare reversal relative to B-T/B-X | **KILL** |
| R4B-5: FULL changes coalition stability | **KILL** |
| R4B-6: at least one headline result is unavailable from both benchmarks | **KILL** |
| R4B-7: remaining result is IJIO-sufficient | **KILL** |

## 12. Artefact and solver ledger

New authority files:

- `verification/stage04r4b_policy_welfare_coalition.py`
- `verification/stage04r4b_sw_full_policy_check.py`
- `reviews/STAGE_04R4B_AFFINE_POLICY_WELFARE_COALITION_RECONSTRUCTION_2026-09-06.md`
- `decisions/STAGE04R4B_CESD_DECISIONS.md`

The exact B-T sign proof uses SymPy rationals and Bernstein coefficients.

The FULL location calculations use root finding only to generate candidates; every accepted location candidate is independently checked against each firm's unrestricted one-dimensional global best-response problem. Failure/nonconvergence is never interpreted as an unprofitable deviation.

## 13. Canonical Stage 4 verdict

This completes the reopened canonical Stage 4 investigation.

**NO-GO.**

The affine-demand architecture fixes the equilibrium-continuation flaw but does not produce a strategically new welfare/stability result.

## 14. Routing

**TERMINATE THIS PAPER.**

Do not proceed to Stage 5, Stage 6, theory freeze, journal positioning refresh, or submission QA.

Do not return automatically to Stage 3 for another pricing/demand architecture. Stage 3R4 explicitly made termination the default if the affine reconstruction failed its full-game welfare/stability test.

Any future use of pieces of this project should begin as a distinct Stage 0 research question or a clearly separate paper, not as another repair cycle of `Standards Coalitions and Strategic Product Repositioning`.
