# Minimal Model Hypotheses

Status: NON-CANONICAL CANDIDATE ARCHITECTURE
Date: 2026-09-04

This file records candidate modeling choices to test. Nothing here is frozen before the relevant workflow stage.

## 1. Baseline environment candidate

Use `n ≥ 3` firms located symmetrically on a Salop circle as the first tractable differentiation benchmark. Consumers are distributed uniformly and buy at most one unit.

The Salop structure is useful only if interoperability changes an economically distinct margin. If interoperability merely rescales the transport-cost coefficient, the model risks being a reparameterization and should be killed or redesigned.

## 2. Endogenous interoperability variable

Preferred first candidate:

`a_i ∈ [0,1]`

where higher `a_i` means that firm `i` makes its product/ecosystem more interoperable with the relevant standard or other firms.

A pairwise effective interoperability map is required:

`A_ij = Φ(a_i, a_j)`.

Candidate forms such as `min{a_i,a_j}`, `a_i a_j`, or another technology-based aggregator must not be selected for algebraic convenience alone. Stage 1/3 must identify an economic interpretation and test sensitivity to the aggregator.

## 3. Consumer-side channels

Candidate utility channels are deliberately separated:

### A. Friction channel

Interoperability may reduce effective switching, adaptation, mismatch, or transport-like cost between interoperable products/ecosystems.

### B. Network channel

Interoperability may increase the effective installed base/network accessible to a consumer.

These channels should initially be modeled separately. Combining them is justified only if the minimal model shows that both are needed for the key result.

## 4. Firm-side trade-off

A private interior choice requires opposing marginal effects. Candidate sources are:

- greater network value/demand from higher interoperability;
- stronger price competition from lower effective differentiation;
- loss of ecosystem-specific rents or lock-in;
- an economically interpretable engineering/compliance cost of interoperability.

A convex cost may be used only if it corresponds to a plausible technology or organizational constraint. It must not be inserted solely to manufacture an interior optimum.

## 5. Candidate timing

Initial timing to test:

1. coalition/standard environment;
2. firms choose `a_i`;
3. firms set prices;
4. consumers choose;
5. welfare and coalition-deviation incentives are evaluated.

Alternative timing — especially government/coalition choice before or after firms choose `a_i` — remains open.

## 6. Objects to derive before model expansion

For the smallest viable symmetric version, derive:

- price subgame equilibrium `p*(a)`;
- profit `π(a_i,a_-i)`;
- symmetric interoperability best response;
- conditions for `0 < a_o* < 1`;
- comparative statics of `a_o*` with respect to differentiation, network strength, and any interoperability cost;
- national welfare `W(a)` under the candidate institutional structure;
- a distinct threshold `â` relevant to coalition membership/stability;
- parameter regions in which the ordering `a_o* ≷ â` changes.

## 7. Hard kill conditions

Kill or radically redesign the baseline if any of the following holds robustly:

1. `a_o*` is generically `0` or `1` and interiority requires arbitrary functional-form engineering.
2. `a` is mathematically equivalent to redefining Salop transport cost with no new strategic interaction.
3. Network effects do not alter any full-game result beyond a level shift.
4. `â` is not economically distinct from `a_o*` or from a trivial welfare optimum.
5. Endogenous interoperability never changes coalition stability.
6. The whole game is nested in existing endogenous-compatibility literature without a new strategic or welfare result.

## 8. Complexity discipline

Do not simultaneously endogenize firm locations, compatibility, coalition membership, standard design, prices, installed bases, and dynamic adoption in the first model. Add one margin only after the preceding minimal mechanism survives its kill test.
