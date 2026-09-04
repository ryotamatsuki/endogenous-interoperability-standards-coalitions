# Audited Stage-1 Representation

Date: 2026-09-04
Status: **FROZEN FOR STAGE 2 COMPARISON ONLY — NOT A CANONICAL PAPER MODEL**

This document records the residual game that survives the Stage-1 source and mathematical audit. It intentionally does **not** select Salop, Cournot, Bertrand, a network-effect function, an interoperability aggregator, or an implementation-cost function. Those choices remain unauthorized until novelty and mechanism gates justify them.

## 1. What is already occupied

The following are benchmark ingredients, not contribution claims:

- continuous / partial compatibility;
- compatibility chosen before downstream product-market competition;
- differentiated products plus network externalities;
- private compatibility versus welfare wedges;
- intermediate private compatibility;
- firm/network alliances and common standardization;
- government policies that mandate or incentivize a continuous degree of technical compatibility;
- international agreements over compatibility policy.

The project also has an especially important **own nested benchmark**: `ryotamatsuki/private-compatibility-standards-coalitions`. Its frozen timing is already

`formal government partition -> private standard adoption -> Cournot competition -> national welfare -> coalition stability`.

Therefore actor separation and this timing sequence are not new by themselves.

## 2. Audited residual game skeleton

Let countries be `i in N`, each with a domestic firm. Let `rho` denote a formal standards partition / coalition state chosen or inherited at the government level.

### Stage G — formal standards state

Governments/countries select or face a formal state

`rho in R`.

A deviation by country `i` changes the formal state from `rho` to some admissible `rho' in D_i(rho)`.

### Stage A — private implementation

Conditional on `rho`, firms choose implementation-level interoperability

`a_i in A_i(rho)`.

The equilibrium implementation vector is regime-specific:

`a*(rho; theta)`.

It must be derived from firm objectives after correctly anticipating the downstream market equilibrium. For an interior component, a first-order condition is only a candidate. SOC, global best response, feasibility, and corners are mandatory.

### Stage M — downstream market competition

Given `(rho,a)`, firms choose prices, quantities, or another market action `y` according to one justified competition model. Denote the equilibrium

`y*(rho,a;theta)`.

### Stage W — national welfare

For each country,

`W_i(rho,a,y;theta)`

must use a fixed market definition and consistent utility system. At minimum it must specify domestic consumer surplus, worldwide or market-specific profit ownership, implementation/compliance costs, transfers/taxes if any, and whether foreign surplus is excluded.

Define the continuation value

`V_i(rho;theta) = W_i(rho, a*(rho;theta), y*(rho,a*(rho;theta);theta); theta)`.

### Stage S — coalition stability

The primitive stability condition is **not** `a_o* >= â`.

For every admissible unilateral government deviation `rho' in D_i(rho)`, stability requires

`Delta_i(rho,rho';theta) = V_i(rho;theta) - V_i(rho';theta) >= 0`.

Both terms use their own regime-specific private implementation and market continuation equilibria.

## 3. Status of the proposed threshold `â`

A scalar coalition-stability threshold may be introduced only as a **derived representation**.

For example, if a member-state payoff difference can be written, after substituting the deviation continuation, as

`Delta_i(a^M;theta)`

and if Stage 4/5 proves that this function is continuous, monotone in the relevant scalar implementation measure, and has a unique root, then define

`â_i(theta)` by `Delta_i(â_i;theta)=0`.

Without those properties, `â` may not exist, may be non-unique, or may be misleading because a government deviation changes both the formal state and the private continuation equilibrium. Later work must therefore start from `Delta_i`, not from a presumed threshold.

## 4. Status of `a_o*`

The notation `a_o*` is also provisional. In the general game the relevant object is the vector `a*(rho;theta)`. A scalar `a_o*` is legitimate only under a proved symmetric or one-dimensional reduction.

Interiority `0<a_o*<1` is a viability property, not a novelty result.

## 5. Reparameterization discipline

If interoperability enters consumer demand only through an effective differentiation coefficient such as

`t_eff = t(a)`

and all downstream equilibrium objects depend on `a` only through `t_eff`, then the product-market block is a change of variable. Foros-type models illustrate this risk directly.

A project may still use such a block as a benchmark, but it cannot claim a new interoperability mechanism from it. For the new branch to justify complexity, formal state `rho` and private implementation `a` must interact through at least one independently interpretable primitive such as:

- feasible implementation set;
- implementation/compliance technology;
- pairwise accessible network/complement set;
- asymmetric cross-border surplus incidence;
- deviation-specific implementation incentives;
- another channel that cannot be eliminated by redefining a single substitutability parameter.

## 6. Curvature and interiority discipline

No cost function is canonical at Stage 1. A quadratic or convex implementation cost may be introduced later only if it has an independent engineering, organizational, licensing, certification, or coordination interpretation.

A symmetric FOC cannot establish a private implementation equilibrium. Later derivations must verify:

1. downstream equilibrium existence and uniqueness on the claimed region;
2. reduced-profit differentiability or KKT conditions;
3. own SOC / concavity where used;
4. global best response over `[0,1]` or the actual feasible set;
5. asymmetric deviations from a symmetric candidate;
6. boundary choices `a_i=0,1`;
7. parameter restrictions needed for all of the above.

## 7. Nested benchmarks Stage 2 must use

### B0 — binary private-adoption standards-coalition benchmark

`private-compatibility-standards-coalitions` already supplies formal government partitions, private post-partition adoption, competition, national welfare, and stability. The continuous model must recover or clearly contrast this benchmark.

### B1 — continuous private-compatibility benchmark

Stadler et al. (2022), Foros & Hansen (2001), de Palma et al. (1999), Garcia (2016), Toshimitsu (2018), and related papers cover major versions of continuous compatibility followed by product-market competition.

### B2 — government continuous-compatibility policy benchmark

Klimenko (2009) studies partially incompatible products, government compatibility standards/policies, compatibility-enhancing effort, international competition, national policy incentives, and international coordination.

### B3 — government standards-union benchmark

Gandal & Shy (2001) supplies governments/countries forming standardization unions under network effects/conversion costs, but compatibility recognition is binary.

## 8. Residual research question frozen for Stage 2

> Does endogenizing a continuous post-agreement private interoperability implementation margin inside a government standards-coalition game generate a coalition-stability result that is unavailable in both (i) binary private-adoption coalition models and (ii) continuous compatibility / government-policy models considered separately?

This is a **generalization/unification candidate**, not a novelty claim.

## 9. Minimum surviving contribution standard

Stage 2 must reject the branch unless there is a credible path to at least one full-game result that cannot be obtained by relabeling or mechanically combining B0–B3. Examples of the required *type* of result include a genuinely new stability boundary, regime reversal, or strategic feedback caused by endogenous implementation. These are examples of result classes, not predicted findings.

If the continuous model merely smooths the binary adoption threshold or replaces a fixed cost with a continuous cost while preserving the same stability logic, the branch should be killed or returned for radical reframing.
