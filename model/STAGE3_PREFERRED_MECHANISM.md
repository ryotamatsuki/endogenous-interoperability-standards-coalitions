# Stage 3 Preferred Mechanism — Coalition-Scope Implementation Crowd-Out

Date: 2026-09-04  
Status: **SELECTED FOR STAGE 4 MINIMAL-MODEL TEST ONLY**

## Mechanism

A formal standards coalition changes the scope of partners reached by one firm's interoperability implementation. A broader coalition can raise the demand/network return to implementation while simultaneously increasing the product-market rent loss from making more rivals effectively interoperable. Firms choose implementation to maximize profit; governments evaluate national consumer surplus plus home-firm profit.

The mechanism therefore permits:

`formal regime rho -> partner scope -> private implementation a*(rho) -> downstream competition -> national welfare -> government stability`.

The headline target is an **implementation-induced stability reversal**.

## Minimal regime comparison

Three countries and one domestic firm per country.

- `rho^IS={{1,2,3}}`.
- `rho_12^SU={{1,2},{3}}`, interpreted as the continuation after country 3 leaves IS.

No additional formal regime is needed unless Stage 4 requires it as a benchmark.

## Timing

1. Formal regime is fixed for a continuation subgame.
2. Firms choose `a_i in [0,1]` simultaneously.
3. Firms compete in quantities.
4. Consumers purchase.
5. National welfare is calculated.
6. Government deviation/stability is evaluated across regime-specific continuation equilibria.

## Implementation primitive

`a_i` is the completeness/intensity with which firm `i` implements the common interface available to its formal coalition.

The same implementation technology and cost function must be used under IS and SU. Regime dependence must arise because the formal coalition changes the number/scope of eligible interoperability partners, not because the model assigns different cost coefficients by regime.

For the first Stage-4 pass, isolate this mechanism using a one-sided implementation exposure specification. Do not introduce bilateral `Phi(a_i,a_j)`, weakest-link effects, topology, or free-riding.

## First downstream candidate

In national market `k`, test a stripped B0-style linear Cournot network-good system:

`p_i^k = 1 - Q^k + v a_i sum_{j in C_i(rho),j!=i} q_j^k`.

This is a candidate primitive to be audited, not a result.

If it does not produce an economically meaningful reach-versus-competition trade-off, Stage 4 must report that failure rather than alter the model by adding another mechanism.

## Implementation cost

First test:

`C(a_i)=kappa a_i^2/2`.

Interpretation: engineering, conformance testing, maintenance, documentation, certification/profile support, and ongoing interoperability support.

The cost is not a contribution. Stage 4 must reject any stationary point that fails SOC/KKT/global/corner checks and must not change curvature solely to manufacture interiority.

## Firm objective

`Pi_i = sum_k p_i^k q_i^k - C(a_i)`.

## Government objective

`W_i = CS_i + Pi_i`.

Foreign-firm profits are excluded from national welfare.

## Stability

For country 3:

`Delta_3^endo = W_3(rho^IS; a*(rho^IS)) - W_3(rho_12^SU; a*(rho_12^SU))`.

Benchmark at minimum:

`Delta_3^full = W_3(rho^IS; full/fixed implementation) - W_3(rho_12^SU; benchmark implementation)`.

The required Stage-4 headline test is a nonempty region with

`sign Delta_3^endo != sign Delta_3^full`.

## Coalition-scope crowd-out sub-result

A useful intermediate target is

`a_IS* < a_SU*`.

This must be derived from the same product-market primitives. It may not be assumed via regime-specific implementation costs.

A reduced-form diagnostic used at Stage 3 was

`pi(a;s)=b s a - 0.5[kappa+chi s^2]a^2`,

which gives

`a*(s)=b s/[kappa+chi s^2]`.

Then implementation falls when scope increases from one to two partners iff

`kappa < 2 chi`.

This diagnostic is not the Stage-4 model. The coefficient `chi s^2` must emerge from actual downstream competition if the mechanism is to survive.

## Mandatory nested comparisons

- B0: binary/fixed private compatibility inside government standards coalitions.
- B1: fix `rho` and recover ordinary continuous compatibility/implementation competition.
- B3: fix implementation exogenously and recover a government standards-regime comparison.
- B4 contrast: collapse government and firm actors; the national-welfare continuation feedback disappears.

## Prohibited Stage-4 rescue moves

Do not add:

- bilateral implementation free-riding;
- government minimum compatibility policy or firm top-up;
- trade taxes/subsidies;
- private outsider bypass;
- directional link matrices;
- switching costs/dynamics;
- installed bases;
- pairwise network topology;
- additional countries;
- arbitrary curvature.

If the selected mechanism fails, report `NO-GO` for C1 and return to Stage 3 before considering C2.
