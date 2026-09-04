# Stage 3 Re-entry — C-RP Relative-Profit-Induced Interoperability Restraint

Date: 2026-09-04
Workflow: `ryotamatsuki/research-paper-workflow` v1.1
Release SHA: `488e5ab06c207909296a7564eaf9066f7f94319c`
Template: `templates/STAGE_03_MECHANISM_SEARCH.md`

## Research question

Can a fixed global relative-profit objective make firms restrain post-agreement interoperability more strongly under a broad government standards coalition, thereby generating a government coalition-stability reversal unavailable in the profit-maximizing C2 benchmark?

## Binding background

- C1/CSIC failed Stage 4 and is terminated.
- C2 bilateral implementation/free-riding failed Stage 3 re-entry and is terminated as a mechanism.
- The integrable bilateral technology from C2 may be reused only as a neutral technology:
  `A_ij=a_i+a_j-a_i a_j`.
- Stage-2 killed ingredient-level novelty claims remain binding.

## Primary C-RP architecture

Three countries/firms, regimes `IS={{1,2,3}}` and `SU_12={{1,2},{3}}`.

Consumer side / inverse demand in each national market:

`p_i=1-Q+v sum_{j in C_i(rho),j!=i} A_ij q_j`,

where `A_ij=A_ji=a_i+a_j-a_i a_j`.

Firm net profit:

`Pi_i = sum_k p_i^k q_i^k - kappa a_i^2/2`.

Firm objective, with reference group fixed globally and independent of the formal coalition:

`U_i=Pi_i-(alpha/2) sum_{j!=i} Pi_j`, `0<=alpha<1`.

Government objective remains actual national welfare:

`W_i=CS_i+Pi_i`.

Timing: formal regime -> implementation -> quantity competition -> national welfare -> government stability comparison.

## Mandatory Stage-3R tests

1. Targeted prior-art kill on relative profit/RPE plus R&D/investment spillovers, product differentiation, network effects, and strategic competition.
2. Derive enough of the full-RP Cournot continuation and implementation marginal returns to compare IS and SU.
3. Test the candidate ordering `a_IS*(alpha)<a_SU*(alpha)` rather than assume it.
4. Artifact benchmark: hold product-market competition at ordinary-profit Cournot and apply RP only to the implementation objective; determine whether the purported rival-profit-spillover channel is genuinely regime differential.
5. Verify consumer-side integrability from symmetric bilateral `A_ij`.
6. Numerically audit `a_IS<a_SU`, `Delta_3^endo<0`, reversal relative to alpha=0, and reversal relative to costless/full interoperability on a documented grid.
7. Return `NO-GO` if no positive diagnostic survives. Do not add coalition-dependent reference groups, capacity constraints, scope costs, policy instruments, topology, dynamics, or endogenous alpha to force the result.

## GO condition

Proceed to Stage 4 only if the fixed-global-reference C-RP architecture produces a nonempty, non-mechanical region with a regime-specific implementation effect and a plausible stability reversal that cannot be reduced to generic tougher Cournot competition or known relative-profit investment-spillover results.