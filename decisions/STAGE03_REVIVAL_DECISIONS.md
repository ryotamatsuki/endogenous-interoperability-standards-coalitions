# Stage 3 Revival Decisions

Date: 2026-09-10

Workflow: `ryotamatsuki/research-paper-workflow` v2.1.

Branch: `revival/stage00-coalition-repositioning`.

## Decision 1 — Stage-2 novelty boundary remains binding

No killed Stage-2 claim may be restored. In particular, novelty cannot rest on compatibility-induced differentiation, continuous standards policy, coalition-induced downstream action, or generic policy-ranking reversal.

## Decision 2 — Candidate search method

Ten genuinely distinct candidate mechanisms/generalizations were compared under ex-ante weights for whole-game novelty, mechanism clarity, tractability, welfare/coalition leverage, institutional plausibility, empirical bridge, and referee defensibility.

Authority: `docs/REVIVAL_STAGE3_CANDIDATE_MECHANISM_MATRIX_2026-09-10.md`.

## Decision 3 — TOP 3

1. C1 — Realized interoperability depth;
2. C2 — Multi-market common standard;
3. C3 — Home-market incidence / asymmetric national surplus.

Only C1 is authorized for the next stage.

## Decision 4 — Selected mechanism

**SELECT C1 — REALIZED INTEROPERABILITY DEPTH.**

Formal standards membership defines the potential compatibility set. The existing bloc depth variable determines the degree of realized interoperability inside that set while also changing standard-related competitive differentiation through the retained `Tau` map.

The baseline Stage-4 realization map is fixed before result search as

`chi(s)=s/s_bar`.

No nonlinear `chi`, separate benefit policy, policy cost, new player, home-bias parameter, heterogeneous repositioning cost, bargaining rule, extra market, or additional policy dimension is authorized in the first Stage-4 attempt.

## Decision 5 — Selected affine-demand map

For `i != j`, Stage 4 will test

`K_ij = c0 + lambda*phi(x_i-x_j)/Tau_ij(rho,s) - v*M_ij(rho,s)`,

where `M_ij=chi(s_C)` for pairs inside the same multi-country standards bloc and `M_ij=0` across blocs. The existing quadratic demand/KKT and Bertrand continuation architecture is retained subject to fresh Stage-4 global verification.

## Decision 6 — Source economics being tested

PR #65 mechanically generated `s_I*=0` because depth increased competitive substitutability while the full compatibility term was already activated by membership. C1 asks whether a technically meaningful depth variable that simultaneously realizes interoperability and changes competition creates a genuine marginal trade-off.

The desired conclusion is not assumed. C1 passes only if product repositioning changes a coalition-level result after depth optimization.

## Decision 7 — Required benchmarks

Stage 4 must solve:

- `B-FIX`: endogenous coalition/depth, fixed positions;
- `B-EXO`: endogenous positions with exogenous depth;
- `FULL`: endogenous depth and positions;
- historical #65 as a documented predecessor, not as a passing result.

## Decision 8 — Fatal Stage-4 contribution test

Stage 4 must establish on a nondegenerate regular region at least one of:

- different stable partition in B-FIX vs FULL;
- strict stability-threshold shift;
- coalition-blocking reversal;
- private/social coalition-stability wedge caused specifically by repositioning.

Removing product repositioning must remove the headline result.

If none survives, the mandatory verdict is **NO-GO — TERMINATE THE REVIVAL**.

## Decision 9 — No rescue inside Stage 4

Failure of C1 may not be repaired in the same cycle by adding C2/C3 or any rejected candidate. A later reuse of those ideas would require a fresh workflow rollback/new Stage-0 authorization.

## Decision 10 — Stage verdict

**GO — GO TO MINIMAL MODEL.**

Next canonical stage: **Stage 4 — Minimal Model**.