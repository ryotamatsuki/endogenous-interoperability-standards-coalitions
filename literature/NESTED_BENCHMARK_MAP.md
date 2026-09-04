# Nested Benchmark Map — Stage 2

Date: 2026-09-04
Status: canonical Stage-2 literature map

## Candidate full architecture

The candidate full game is not yet a functional-form model. Its economically relevant structure is:

`government formal regime rho -> firms choose continuous implementation a(rho) -> downstream competition -> national continuation values V_i(rho) -> government participation/deviation stability`.

The key endogenous feedback to test is that a government deviation changes `rho`, which changes the firms' continuation implementation equilibrium, which changes product-market outcomes and therefore changes the deviation payoff itself.

## B0 — Binary private adoption inside government standards coalitions

Source: `ryotamatsuki/private-compatibility-standards-coalitions`.

Already contains:

- governments/countries as formal-coalition players;
- formal partition `rho`;
- later private adoption decisions;
- downstream Cournot competition;
- national welfare `CS_i + Pi_i`;
- coalition stability from government continuation payoffs.

Restriction/recovery from candidate full architecture:

- restrict private interoperability choice to a finite/binary adoption set;
- retain the same government-regime and continuation-value logic.

What the candidate must add beyond B0:

- not merely a continuous version of the same adoption threshold;
- a new intensive-margin response `a*(rho)` whose regime dependence changes stability qualitatively.

## B1 — Continuous private compatibility without government coalition formation

Representative sources: Stadler, Tobler Trexler & Unsorg (2022); Foros & Hansen (2001); de Palma, Leruth & Regibeau (1999); Garcia (2016); Toshimitsu (2018); Jeon, Menicucci & Nasr (2023).

Already contains:

- endogenous compatibility/interoperability;
- network benefits and competition softening/intensification trade-offs;
- differentiated downstream competition;
- interior or discrete compatibility equilibria;
- private-versus-social compatibility wedges;
- in some papers firm alliances or coalition-proof compatibility configurations.

Restriction/recovery from candidate full architecture:

- fix the government formal regime `rho`;
- suppress government participation/deviation stage and national-welfare coalition stability.

What the candidate must add beyond B1:

- regime-dependent private implementation must feed back into an upstream government coalition decision; an ordinary compatibility FOC is not new.

## B2 — Government continuous compatibility policy / international coordination

Primary source: Klimenko (2009), *Journal of International Economics*, DOI `10.1016/j.jinteco.2008.08.005`; related 2009 IREF paper.

Already contains:

- partial technical compatibility;
- consumers valuing network externalities and variety;
- firms able to affect compatibility and incur compatibility-related costs;
- government minimum compatibility standards and compatibility-linked taxes/subsidies;
- strategic government policy under international competition;
- national policy incentives and international agreements/coordinated policy.

Restriction/recovery from candidate full architecture:

- fix treaty/coordination participation;
- give governments direct continuous policy instruments over compatibility rather than endogenous coalition-membership choices with a separate private post-agreement implementation game.

What the candidate must add beyond B2:

- self-enforcing participation/deviation in a standards coalition when governments anticipate firms' separate continuation implementation choices.

## B3 — Government standardization unions

Source: Gandal & Shy (2001), *Journal of International Economics*, DOI `10.1016/S0022-1996(00)00067-2`.

Already contains:

- governments choosing recognition policy;
- three-country standardization unions;
- network effects and conversion costs;
- national welfare incentives for forming/excluding from unions.

Restriction/recovery from candidate full architecture:

- make compatibility/recognition binary;
- suppress a privately chosen continuous post-agreement implementation intensity.

What the candidate must add beyond B3:

- a private intensive margin after formal union formation that changes regime-specific continuation values and stability.

## B4 — Firm standards-coalition formation

Source: Economides & Skrzypacz (2003), *Standards Coalitions Formation and Market Structure in Network Industries*.

Already contains:

- endogenous technical-standards coalitions;
- firms deciding affiliation before oligopoly competition;
- network-effect benefits from coalition size;
- intensified competition within a common platform;
- endogenous coalition structure and stationary/no-delay coalition equilibria.

Important clarification:

The paper's abstract describes firms as free to choose their 'degree of technical compatibility', but the implemented coalition game is a partition game: firms in the same coalition adopt the same standard and firms in different coalitions are incompatible. Compatibility is therefore coalition/configuration based rather than an independent continuous post-coalition intensity choice.

Restriction/recovery relative to candidate full architecture:

- collapse government and firm actors into a single profit-maximizing coalition player;
- make affiliation itself determine compatibility;
- remove national consumer-surplus objectives and government deviation incentives.

What the candidate must add beyond B4:

- a two-level game in which coalition membership and implementation are controlled by different actors with different objectives.

## B5 — Coalition-proof and network-structured interoperability frontier

Representative sources:

- Ding, Ko & Shen (2022), *Economic Modelling*, partial compatibility in two-sided markets;
- Huang, Tan, Teh & Zhou (2026), *A Network Approach to Interoperability*;
- Bourreau, Raizonville & Thébaudin (2026), *Journal of Industrial Economics*;
- Ekmekci, White & Wu (2025), *Management Science*;
- Kim (2026), *Journal of Economics & Management Strategy*.

Already contains:

- partial/coalitional interoperability configurations;
- coalition-proof private outcomes in platform models;
- weighted interoperability networks and interoperability strength;
- current regulation/welfare analysis of interoperability;
- platform asymmetry and installed-base effects.

Restriction/recovery from candidate full architecture:

- replace countries/governments by platforms or regulator-exogenous policy;
- suppress endogenous international standards-coalition membership with national welfare.

What the candidate must add beyond B5:

- national participation/deviation incentives that endogenously depend on private implementation equilibria under each formal regime.

## Whole-game absorption conclusion

No single benchmark B0–B5 reproduces all of the following simultaneously:

1. countries/governments choose or evaluate formal standards-coalition membership;
2. private firms are distinct downstream actors;
3. after the formal regime is fixed, firms choose a continuous interoperability implementation intensity;
4. downstream market competition follows;
5. government payoffs are national welfare rather than firm profits or global surplus;
6. a government deviation changes the formal regime and therefore changes the private implementation continuation equilibrium;
7. coalition stability is evaluated using those regime-specific continuation values.

This is not proof of novelty. The architecture survives only as a generalization/unification candidate.

## Unique strategic feedback required for survival

Define the continuation mapping

`rho -> a*(rho;theta) -> x*(rho,a*) -> V_i(rho;theta)`.

The potentially new interaction is the **regime-dependent implementation feedback**:

`rho` affects private interoperability incentives, and the induced change in `a*` feeds back into the government's incentive to remain in or deviate from `rho`.

B0 has this feedback only through a binary adoption margin; B1/B5 lack government coalition membership; B2 has government compatibility policy but not self-enforcing coalition membership with a separate private continuation implementation choice; B4 has coalition formation but the same firms control both coalition membership and compatibility and maximize profits.

## Stage-3 theorem target

Stage 3 must test for at least one result of the following class:

### Implementation-induced stability reversal

There exists a nonempty parameter region in which a formal coalition would be stable under an exogenous/full or binary implementation benchmark but becomes unstable when firms optimally choose continuous post-agreement interoperability, or vice versa, because

`a*(rho;theta) != a*(rho';theta)`

changes the sign of

`Delta_i(rho,rho';theta) = V_i(rho;theta) - V_i(rho';theta)`.

A stronger result would establish a non-monotone or disconnected stability region in a primitive parameter (network intensity, implementation cost, differentiation, market asymmetry) that cannot occur in the nested binary benchmark.

If Stage 3 cannot produce such a result without adding unrelated primitives, the generalization should be killed.
