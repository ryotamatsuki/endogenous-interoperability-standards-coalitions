# Stage 4 — Minimal Model: CSIC

Date: 2026-09-04
Repository: `ryotamatsuki/endogenous-interoperability-standards-coalitions`
Canonical workflow: `ryotamatsuki/research-paper-workflow` v1.1
Workflow release SHA: `488e5ab06c207909296a7564eaf9066f7f94319c`
Template: `templates/STAGE_04_MINIMAL_MODEL.md`

## Role

Act as a skeptical theorist and symbolic-verification engineer. Solve the Stage-3 C1 mechanism exactly; do not engineer the desired result.

## Frozen mechanism

**Coalition-Scope Implementation Crowd-Out (CSIC).**

Formal regime `rho` changes the scope of eligible interoperability partners. Firms then choose implementation intensity, compete in Cournot quantities, and governments evaluate national welfare and deviation incentives.

## Frozen minimal model

- Countries/firms: `i=1,2,3`, one domestic firm per country.
- Three identical national markets; every firm serves every market.
- Regimes: `rho^IS={{1,2,3}}` and `rho_12^SU={{1,2},{3}}`.
- Timing: `rho -> a -> q -> W -> stability`.
- Implementation: `a_i in [0,1]`.
- Inverse demand in each national market `k`:
  `p_i^k = 1-Q^k + v a_i sum_{j in C_i(rho),j!=i} q_j^k`.
- Implementation cost, paid once by firm i:
  `C_i(a_i)=kappa a_i^2/2`.
- Firm objective:
  `Pi_i=sum_k p_i^k q_i^k-kappa a_i^2/2`.
- Government objective, only if consumer surplus is coherently derivable:
  `W_i=CS_i+Pi_i`.

Use `0<v<=1/4` as the first regularity domain because it nests the weak-network domain used in benchmark B0 and permits exact monotonicity/feasibility checks. Report separately any statement that relies on this restriction.

## Mandatory tests

1. Solve the Cournot subgame for arbitrary implementation profiles under IS and SU.
2. Derive reduced implementation profits and global best-response conditions.
3. Characterize symmetric implementation equilibria, including full-implementation corners and interior roots.
4. Test, rather than assume, `a_IS* < a_SU*`.
5. Verify SOC/KKT/global-best-response logic and feasibility.
6. Audit inverse-demand integrability for asymmetric unilateral implementation deviations. If no coherent utility/CS object exists, state the welfare consequence explicitly.
7. Where equilibrium-consistent symmetric welfare can be constructed as a diagnostic, derive it but do not silently treat it as a full microfoundation.
8. Compare endogenous stability with two full-implementation benchmarks:
   - cost-bearing mandated `a=1`;
   - costless/exogenous full interoperability technology.
9. Search analytically and numerically for implementation-induced stability reversal.
10. Distinguish a genuine CSIC reversal from a mechanical implementation-cost comparison.
11. Recover the required nested benchmarks conceptually.
12. Return exactly one verdict: `GO`, `CONDITIONAL GO` with one blocker, or `NO-GO`.

## Hard no-rescue rule

Do not introduce bilateral `Phi(a_i,a_j)`, free riding, regime-specific costs, policy instruments, bypass, trade costs/taxes, switching costs, topology, dynamics, installed bases, extra countries, or new curvature.

If the one-sided CSIC primitive does not generate the selected reach-versus-competition mechanism, return `NO-GO` and route back to Stage 3.

## Required artifacts

- `reviews/STAGE_04_MINIMAL_MODEL_CSIC_2026-09-04.md`
- `model/STAGE4_MINIMAL_MODEL_CSIC.md`
- `verification/stage04_csic_sympy.py`
- updated `PROJECT_STATE.md`
- updated `decisions/DECISION_LOG.md`
