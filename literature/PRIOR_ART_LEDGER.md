# Prior-Art Ledger

Status: **Stage 1 source/math audit completed; Stage 2 whole-game novelty audit not yet run**  
Date: 2026-09-04

This ledger distinguishes what Stage 1 has already verified from what Stage 2 still must establish. No entry below is a final novelty verdict unless explicitly marked as a rejected contribution claim.

| Benchmark family | Close source / project | Stage-1 verified overlap | Stage-1 status | Stage-2 absorption question |
|---|---|---|---|---|
| **B0 — binary private adoption inside government standards coalitions** | `ryotamatsuki/private-compatibility-standards-coalitions` | Formal government partition → private adoption → Cournot → national welfare → coalition stability | **MANDATORY NESTED BENCHMARK** | Does continuous implementation do more than smooth/relabel B0 thresholds? |
| Continuous private compatibility + price competition | Stadler, Tobler Trexler & Unsorg (2022), DOI `10.1007/s11067-022-09572-x` | `k_i∈[0,1]`, network effects, Hotelling-type differentiation, compatibility first, prices second, partial compatibility, common firm standardization | **HIGH-RISK / FULL MODEL INSPECTED** | Does the new model add a full-game coalition-stability result rather than another compatibility FOC? |
| Compatibility level + Hotelling + welfare | Foros & Hansen (2001), DOI `10.1016/S0167-6245(01)00044-0` | Compatibility/interconnection before Hotelling pricing; private vs welfare investment; `t` and `k` enter an effective substitutability composite in accessible precursor | **HIGH-RISK / REPARAMETERIZATION BENCHMARK** | Is any `t(a)` model merely this logic under new notation? |
| Compatibility + alliance stability + welfare | Toshimitsu (2018), DOI `10.1007/s10842-017-0264-1` | Differentiated Cournot, network effects, strategic compatibility, stable/socially optimal network alliance; providers control compatibility absent intervention | **HIGH-RISK / FULL EQUATIONS STILL REQUIRED FOR STAGE 2** | Is government coalition stability substantively different from a firm network alliance? |
| Partial compatibility + network externalities | de Palma, Leruth & Regibeau (1999), DOI `10.1016/S0167-6245(99)00006-2` | Degree of compatibility is endogenous product design under network externalities | **CLOSE** | Does continuous implementation add anything beyond classic partial-compatibility design? |
| Compatibility before Bertrand pricing | Garcia (2016), DOI `10.1111/jems.12146` | Differentiated network products; compatibility choice before Bertrand pricing; private/social incentives | **CLOSE** | Is downstream pricing a contribution-relevant channel or standard background? |
| Switching costs / portability | Jeon, Menicucci & Nasr (2023), DOI `10.1257/mic.20200309` | Dynamic compatibility choice, switching costs, data portability | **HIGH-RISK FOR NON-NETWORK ROUTE** | Is a switching/portability extension already absorbed? |
| Pairwise/network interoperability | Huang, Tan, Teh & Zhou (2026), *A Network Approach to Interoperability* | Weighted interoperability network among competing platforms; prices and welfare | **CURRENT HIGH-RISK** | Would pairwise `A_ij` add anything after this paper? |
| Platform partial compatibility | Peitz (2026), *Asymmetric Platform Oligopoly* | Continuous share of compatible functionalities with network effects; prices/shares/user surplus | **CURRENT CLOSE** | Is functionality-share interoperability already standard? |
| **B3 — government standardization unions** | Gandal & Shy (2001), DOI `10.1016/S0022-1996(00)00067-2` | Governments recognize foreign standards and form standardization unions; horizontal differentiation; conversion costs/network effects | **MANDATORY GOVERNMENT-COALITION BENCHMARK** | Does a continuous private continuation choice create a new stability result beyond binary recognition/adoption? |
| **B2 — government continuous-compatibility policy / international coordination** | Klimenko (2009 JIE), DOI `10.1016/j.jinteco.2008.08.005` | Partial technical compatibility, government minimum compatibility standard, compatibility-enhancing effort, strategic policy, international coordination/agreement | **VERY HIGH-RISK / MANDATORY BENCHMARK** | Does endogenous coalition membership/stability add a non-nested strategic feedback? |
| Government interoperability standard + trade taxes | Klimenko (2009 IREF), DOI `10.1016/j.iref.2008.09.015` | Government minimum interoperability standard; foreign compatibility policy/investment; international duopoly | **HIGH-RISK** | Can the proposed government–firm wedge be reconstructed as a policy game rather than coalition game? |
| Interconnection agreement + policy intervention | Ji & Daitoh (2008), DOI `10.1111/j.1468-5876.2007.00408.x` | ISP interconnection agreement under network externalities; optimal government intervention; international extension | **CLOSE** | Does policy intervention plus private interconnection absorb the wedge? |
| Systems / mix-and-match compatibility | Matutes & Regibeau and related systems literature | Compatibility expands feasible combinations/complement access | **FAMILY BENCHMARK** | Is any complement-access route classic systems compatibility? |

## Stage-1 mathematical audit finding — Stadler et al. (2022)

The project has a reproducible SymPy audit at:

`verification/stage01_stadler_sympy.py`.

Verified:

- published price equilibrium: exact;
- published symmetric compatibility FOC: exact;
- reported interior root: exact stationary point.

But the stated condition `gamma > beta(5+4b)/12` does not by itself guarantee the own SOC/global best response for all reported `b>=0`. An exact admissible counterexample is recorded in the script and Stage-1 report.

Implication for this project: no symmetric FOC may be promoted to an interoperability equilibrium without SOC/KKT/global/corner checks.

## Stage-1 reparameterization finding

A Foros-type Hotelling representation uses the composite

`t - beta(1-k)`.

If the new interoperability variable only replaces a transport/substitutability coefficient, the product-market block is a change of variable. Such a representation can be used as a benchmark but not as the core contribution mechanism.

## Stage-1 correction to the coalition-threshold idea

The primitive government stability object is

`Delta_i(rho,rho';theta) = V_i(rho;theta) - V_i(rho';theta)`,

where each `V_i` uses its own regime-specific private implementation and product-market continuation equilibrium.

Do **not** assume a scalar `â` exists. It is a permissible derived object only if continuity, monotonicity, and a unique root are proved after continuation equilibria are substituted.

## Stage-2 frozen comparison question

> Does endogenizing a continuous post-agreement private interoperability implementation margin inside a government standards-coalition game generate a coalition-stability result that is unavailable in both B0 (binary private-adoption coalition models) and B1/B2 (continuous compatibility/private or government-policy models) considered separately?

## Stage-2 kill standard

Return `NO-GO` if the candidate whole game can be generated by:

1. taking B0's government-coalition / private-adoption / stability architecture;
2. replacing binary adoption with a standard continuous compatibility-investment block from B1/B2;
3. obtaining the same qualitative stability logic after a smooth change of thresholds.

A surviving generalization/unification route requires at least one full-model strategic or welfare result unavailable in the nested benchmarks alone.
