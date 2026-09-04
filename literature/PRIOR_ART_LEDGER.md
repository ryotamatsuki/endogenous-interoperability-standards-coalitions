# Prior-Art Ledger

Status: **Stage 2 whole-game novelty audit completed**  
Date: 2026-09-04

The canonical novelty conclusion is narrow: no single audited prior model reproduces the complete candidate game, but every ingredient-level claim is already known. The project survives only as a generalization/unification candidate whose Stage-3 burden is to produce a new coalition-stability result.

| Benchmark family | Close source / project | Verified overlap | Stage-2 classification | Binding implication |
|---|---|---|---|---|
| **B0 — binary private adoption inside government standards coalitions** | `ryotamatsuki/private-compatibility-standards-coalitions` | Government partition → private adoption → Cournot → national welfare → stability | **STRUCTURALLY VERY CLOSE / MANDATORY NESTED BENCHMARK** | Continuous implementation must do more than smooth B0 thresholds. |
| **B1 — continuous private compatibility** | Stadler, Tobler Trexler & Unsorg (2022), DOI `10.1007/s11067-022-09572-x` | Continuous `k_i`, network effects, differentiation, compatibility then prices, partial compatibility | **COMPONENT OVERLAP / VERY CLOSE** | Interiority and continuous FOCs are not novelty. |
| B1 | Foros & Hansen (2001), DOI `10.1016/S0167-6245(01)00044-0` | Compatibility before Hotelling competition; private vs welfare; transport/compatibility composite | **STRUCTURALLY VERY CLOSE / REPARAMETERIZATION THREAT** | A pure `t(a)` representation is not contribution-worthy. |
| B1 | de Palma, Leruth & Regibeau (1999), DOI `10.1016/S0167-6245(99)00006-2` | Partial compatibility under network externalities | **COMPONENT OVERLAP** | Degree-of-compatibility as product design is old. |
| B1 | Garcia (2016), DOI `10.1111/jems.12146` | Compatibility before Bertrand pricing; private/social incentives | **COMPONENT OVERLAP** | Downstream pricing after compatibility is old. |
| B1 | Toshimitsu (2018), DOI `10.1007/s10842-017-0264-1` | Strategic compatibility, network effects, differentiated Cournot, stable/socially optimal network alliance | **STRUCTURALLY VERY CLOSE** | Alliance stability plus compatibility is old; government/national objective must matter. |
| B1 | Jeon, Menicucci & Nasr (2023), DOI `10.1257/mic.20200309` | Dynamic compatibility choice, switching costs, data portability | **COMPONENT OVERLAP / HIGH-RISK FOR SWITCHING ROUTE** | Switching/portability is not a novelty escape hatch. |
| **B2 — government continuous compatibility / international coordination** | Klimenko (2009 JIE), DOI `10.1016/j.jinteco.2008.08.005` | Partial compatibility; firm compatibility-enhancing activity; government minimum standard and compatibility policy; national incentives; international agreement | **STRUCTURALLY VERY CLOSE / MANDATORY** | Continuous compatibility + government policy + international coordination is already occupied. |
| B2 | Klimenko (2009 IREF), DOI `10.1016/j.iref.2008.09.015` | Government interoperability standard, trade-tax interaction, international duopoly | **STRUCTURALLY VERY CLOSE** | Government–firm compatibility wedge can be a policy-game result rather than coalition result. |
| **B3 — government standardization unions** | Gandal & Shy (2001), DOI `10.1016/S0022-1996(00)00067-2` | Three-country government recognition policy; standardization unions; network effects/conversion costs | **STRUCTURALLY VERY CLOSE / MANDATORY** | Government union formation is old; only post-union private intensive implementation can differ. |
| **B4 — firm standards-coalition formation** | Economides & Skrzypacz (2003), SSRN `378340` | Endogenous standards-platform coalitions; network benefits vs within-platform competition; oligopoly continuation; stationary coalition equilibrium | **STRUCTURALLY VERY CLOSE / MANDATORY** | Coalition formation driven by compatibility/competition is old. Distinct government objectives and post-coalition private intensity are required. |
| **B5 — coalition-proof/platform partial compatibility** | Ding, Ko & Shen (2022), DOI `10.1016/j.econmod.2022.105989` | Partial compatibility, three platforms, coalition-proof market outcome, welfare | **STRUCTURALLY VERY CLOSE** | Coalition-proof partial compatibility is already an explicit result class. |
| B5 | Huang, Tan, Teh & Zhou (2026), SSRN `6244719` | Weighted interoperability network; coalitional configurations; equilibrium prices; welfare | **CURRENT STRUCTURALLY CLOSE FRONTIER** | Pairwise/weighted topology is not an easy pivot. |
| B5 | Ekmekci, White & Wu (2025), DOI `10.1287/mnsc.2023.02810` | Platform competition and interoperability regulation | **COMPONENT OVERLAP** | Regulation/interoperability welfare is current literature. |
| B5 | Bourreau, Raizonville & Thébaudin (2026), DOI `10.1111/joie.70018` | Endogenous platform interoperability, installed-base asymmetry, welfare | **COMPONENT OVERLAP / CURRENT** | Endogenous interoperability and asymmetry are current frontier topics. |
| B5 | Kim (2026), DOI `10.1111/jems.12643` | Data portability/interoperability regulation, switching costs, network effects | **COMPONENT OVERLAP / CURRENT** | Portability/regulatory interoperability is occupied. |
| SSO membership/governance | Fiedler, Larrain & Prüfer (2023), DOI `10.1016/j.respol.2023.104761` | Endogenous SSO participation, implementation motives, governance | **MERELY RELATED / INSTITUTIONAL BENCHMARK** | Endogenous membership itself is not new. |
| Product-standards agreements | Geng (2019), DOI `10.1111/ecin.12785` | International standards agreements, national welfare, NT vs MR; vertical standards | **MERELY RELATED** | Useful agreement benchmark, not direct horizontal compatibility absorption. |

## Stage-2 whole-game finding

No single source above contains all of the following simultaneously:

1. countries/governments as formal standards-coalition members;
2. distinct private firms as downstream actors;
3. a continuous private interoperability implementation choice made after the formal regime is determined;
4. downstream market competition;
5. national welfare rather than firm-profit or world-welfare coalition payoffs;
6. a government deviation that changes the regime and therefore changes the private implementation continuation equilibrium;
7. coalition stability evaluated using those regime-specific continuation values.

Therefore there is **no Stage-2 EXACT PRIOR ART finding for the whole game**.

This does not establish novelty. The closest absorption argument combines B0 + B2 + B4 and asks whether the proposed paper merely inserts a standard continuous compatibility block into the existing binary coalition skeleton.

## Permanently killed contribution claims

Do not later claim novelty from:

- continuous or partial interoperability;
- interior interoperability;
- network effects plus compatibility;
- price/quantity competition after compatibility;
- private/social compatibility wedges;
- standards coalition formation;
- government standardization unions;
- coalition-proof partial compatibility;
- government continuous-compatibility policy;
- international compatibility agreements;
- pairwise/weighted/coalitional interoperability networks.

## Surviving Stage-3 question

> Can a government coalition regime change firms' post-agreement continuous implementation incentives enough that the regime-specific continuation equilibria reverse a government's participation/deviation incentive relative to binary or exogenous-implementation benchmarks?

Primitive stability object:

`Delta_i(rho,rho';theta) = V_i(rho;theta) - V_i(rho';theta)`.

The preferred Stage-3 target is a nonempty parameter region with

`sign Delta_i^endo != sign Delta_i^benchmark`.

## Stage-3 kill standard

Return `NO-GO` if continuous implementation only produces a smooth threshold in place of B0's binary threshold or reproduces a known comparative static from B1–B5.

See `literature/NESTED_BENCHMARK_MAP.md` and `reviews/STAGE_02_NOVELTY_KILL_GATE_2026-09-04.md`.
