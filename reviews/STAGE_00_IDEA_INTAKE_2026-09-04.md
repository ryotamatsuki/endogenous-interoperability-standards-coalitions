# Stage 0 — Idea / Motivation Intake

Date: 2026-09-04
Repository: `ryotamatsuki/endogenous-interoperability-standards-coalitions`
Canonical workflow: `ryotamatsuki/research-paper-workflow` v1.1
Workflow release SHA: `488e5ab06c207909296a7564eaf9066f7f94319c`
Template: `templates/STAGE_00_IDEA_INTAKE.md`

## 1. Executive verdict

**Canonical verdict: `GO TO AUDIT`**

The project merits Stage 1, but **not under the original broad contribution claim**.

The preliminary external check already shows that the following package is heavily occupied by prior work:

- a continuous/endogenous degree of compatibility;
- horizontal differentiation / Hotelling competition;
- network externalities;
- compatibility chosen before product-market competition;
- price competition after compatibility choice;
- an interior partial-compatibility equilibrium;
- comparison of private compatibility with welfare;
- coordinated/common standardization or a network alliance.

Most importantly, Stadler, Tobler Trexler and Unsorg (2022) explicitly study firms choosing the degree of compatibility before price competition in a horizontally differentiated network-good model and derive partial compatibility as an SPNE. Foros and Hansen (2001) study the level of compatibility followed by Hotelling competition and compare private compatibility investment with welfare. Toshimitsu (2018) studies compatibility choice, product differentiation, network externalities, welfare, and the stability of a network alliance. These are not peripheral overlaps; they strike directly at the originally proposed mechanism.

Accordingly, Stage 0 **rejects** the idea that the paper's contribution can be "Salop + network effects + endogenous partial interoperability + price competition." Interiority `0 < a_o* < 1` remains a model-viability test, but is no longer a meaningful novelty signal by itself.

A potentially defensible research question survives only if the project is reframed around a different whole-game object:

> a formal standards coalition is formed by countries/governments, but firms retain a post-coalition choice over the *implementation intensity* of interoperability; the privately chosen implementation level may then change national participation/deviation incentives and thereby stabilize or destabilize the formal coalition.

That post-coalition private-implementation / national-coalition-stability feedback is conceptually distinct enough to justify a formal Stage 1 audit. Whether it is actually novel remains completely unresolved.

## 2. Phenomenon vs. proposed explanation

### 2.1 Phenomenon

Formal adoption of a common standard need not imply complete technical or economic interoperability. A standard may leave firms discretion over implementation, interfaces, adapters, APIs, feature availability, portability, or other design choices that determine how interoperable products or ecosystems are in practice.

The economically relevant observable is therefore potentially not just a binary standards-membership state, but a degree of effective interoperability within or across formally standardized systems.

This is the phenomenon only. It does not establish why firms choose a particular degree or that the degree is endogenous in the relevant institution.

### 2.2 Proposed explanation

The current hypothesis is that firms retain discretion over an interoperability instrument `a_i` after the standards/cooperation environment is determined. Raising `a_i` may create some combination of:

- greater network value;
- lower switching, adaptation, or mismatch frictions;
- larger accessible complement/network scope;
- stronger substitutability and price competition;
- weaker lock-in or ecosystem rents;
- real implementation/compliance/coordination cost.

A firm's profit-maximizing interoperability choice may therefore differ from the interoperability level that makes national participation in a standards coalition attractive.

The proposed explanation is not yet established. Several of its components are already standard in the compatibility literature.

## 3. Actors / decisions / frictions / outcomes

### Actors

1. **Firms** — choose prices/quantities and, in the surviving candidate route, retain control over implementation-level interoperability.
2. **Consumers/users** — choose among differentiated products/ecosystems and may benefit from interoperability through lower frictions, larger effective networks, portability, or complement access.
3. **National governments / standards-coalition members** — decide whether participation in a formal standards arrangement is nationally beneficial, taking account of domestic consumer and producer surplus and cross-border effects.
4. **Standards organization / coalition mechanism** — an institution that may determine participation or a formal common standard without necessarily controlling all implementation choices.

### Candidate decisions

- coalition membership / deviation by governments or countries;
- firm interoperability implementation `a_i`;
- price competition conditional on interoperability;
- consumer product choice.

### Frictions

- horizontal or vertical product differentiation;
- network benefits or complement access;
- switching/adaptation/mismatch costs;
- private ecosystem rents / lock-in;
- technical or organizational implementation cost;
- cross-border welfare externalities and rent shifting.

### Welfare-relevant outcomes

- consumer surplus;
- domestic producer surplus;
- total/national welfare;
- interoperability implementation;
- prices and market shares;
- coalition participation/deviation payoffs;
- coalition stability.

## 4. Candidate mechanisms

Stage 0 does not select a canonical model. The following are genuinely different candidates to audit.

### M1 — Post-coalition implementation moral hazard / strategic insulation

A formal standards agreement is chosen first, but firms subsequently control interoperability implementation. Firms may implement less (or more) interoperability than governments anticipated because they value product-market rents differently from national welfare. Anticipated post-coalition implementation can then affect whether countries join or deviate.

This is the strongest surviving mechanism candidate because it changes the timing and identity of the decision makers relative to a one-stage compatibility alliance.

### M2 — Competition–network-value trade-off

Higher interoperability increases network value but also changes product substitutability and price competition. This can generate a private interior choice.

**Assessment:** economically coherent but already heavily occupied by the prior literature. It can be a building block, not the contribution.

### M3 — International national-welfare / rent-shifting wedge

Governments maximize national welfare rather than firm profit or world welfare. Interoperability may transfer surplus across countries through prices, market shares, foreign ownership, consumer benefits, or network spillovers. A government can therefore prefer an interoperability regime different from both the private firm optimum and the global social optimum.

This mechanism does not require Salop specifically.

### M4 — Pairwise interoperability network / multi-member free riding

With at least three firms/countries, effective interoperability may be pairwise (`A_ij`) rather than summarized by one industry-wide scalar. A member's implementation can confer benefits on other members while intensifying competition against itself, generating free riding, complementarity, or topology-dependent coalition incentives.

This candidate does **not** require Salop. It may instead use a network/graph or symmetric demand system.

### M5 — Switching / portability mechanism without network externalities

Interoperability reduces future switching or data-portability frictions. Firms may strategically preserve incompatibility to protect installed customers or future rents, while governments value mobility and competition.

This candidate deliberately does **not** rely on network externalities. Jeon, Menicucci and Nasr (2023) makes this family a serious prior-art risk and must be audited before use.

### M6 — Modular / complement-access interoperability without spatial transport cost

Interoperability determines which complementary components, services, or applications can be combined across systems. The economic margin is the scope of feasible combinations or supporting services rather than consumer distance on a Salop/Hotelling space.

This is an alternative to treating interoperability as a transport-cost shifter and therefore avoids the most direct reparameterization risk. It is also close to classic mix-and-match / supporting-services compatibility work and must be audited.

## 5. Main prior-art and reparameterization risks

### 5.1 Strongest whole-game absorption route

The strongest obvious absorption argument is:

1. take the existing literature in which firms choose a degree of compatibility before market competition;
2. interpret compatibility as the project's `a_i`;
3. map network externalities to the effective interoperable installed base;
4. use horizontal differentiation for product competition;
5. solve the price or quantity subgame;
6. compare independent compatibility with common/coordinated compatibility or welfare.

That mapping already captures most of the originally proposed chain.

The preliminary search identifies at least the following high-risk sources:

- Stadler, Manfred; Céline Tobler Trexler; Maximiliane Unsorg (2022), "The Perpetual Trouble with Network Products: Why IT Firms Choose Partial Compatibility," *Networks and Spatial Economics* 22, 903–913. DOI: `10.1007/s11067-022-09572-x`. Continuous compatibility, horizontal differentiation, network effects, compatibility first and prices second, explicit partial-compatibility equilibrium, and common standardization decisions.
- Foros, Øystein; Bjørn Hansen (2001), "Competition and compatibility among Internet Service Providers," *Information Economics and Policy* 13(4), 411–425. DOI: `10.1016/S0167-6245(01)00044-0`. Firms choose a level of compatibility/interconnection before Hotelling competition; compatibility investment is compared with the welfare-maximizing level.
- Toshimitsu, Tsuyoshi (2018), "Strategic Compatibility Choice, Network Alliance, and Welfare," *Journal of Industry, Competition and Trade* 18(2), 245–252. DOI: `10.1007/s10842-017-0264-1`. Differentiated duopoly, network externalities, compatibility choice, network alliance, stability, and welfare.
- Garcia, Filomena (2016), "Revealing Incentives for Compatibility Provision in Vertically Differentiated Network Industries," *Journal of Economics & Management Strategy*. DOI: `10.1111/jems.12146`. Compatibility is chosen before Bertrand pricing in a differentiated network industry.
- "Partial compatibility with network externalities and double purchase" (1999), *Information Economics and Policy* 11(2), 209–227. DOI: `10.1016/S0167-6245(99)00006-2`. Degree of compatibility is a product-design choice under network externalities.
- Jeon, Doh-Shin; Domenico Menicucci; Nikrooz Nasr (2023), "Compatibility Choices, Switching Costs, and Data Portability," *American Economic Journal: Microeconomics* 15(1), 30–73. DOI: `10.1257/mic.20200309`. Dynamic compatibility choice, switching costs, and portability.
- "Partial compatibility in two-sided markets: Equilibrium and welfare analysis" (2022), *Economic Modelling* 116, 105989. DOI: `10.1016/j.econmod.2022.105989`. Compatibility configurations, network effects, coalition-proof outcomes, and welfare.
- Nicholas Economides and Fredrick Flyer (1997/1998), "Compatibility and Market Structure for Network Goods." Network externalities, product differentiation, technical standards, compatibility, and coalition structures.
- Huang, Jinglei; Guofu Tan; Tat-How Teh; Junjie Zhou (2026), "A Network Approach to Interoperability," working paper / SSRN, posted March 2026. Models interoperability as a weighted network among competing platforms with user externalities and studies equilibrium prices and welfare.
- Martin Peitz (2026), "Asymmetric Platform Oligopoly," *RAND Journal of Economics*. Includes a continuous degree of partial compatibility as the share of functionalities whose network effects become industry-wide and studies effects on prices, shares, and user surplus.

These are Stage 0 preliminary hits only. Stage 1/2 must inspect the full papers and cannot rely on abstracts alone.

### 5.2 Salop / transport-cost reparameterization risk

If consumer utility can be written so that interoperability only changes

`t -> t(a)`

and every equilibrium object depends on `a` only through the effective transport coefficient `t(a)`, then `a` is not an economically distinct strategic primitive. It is a change of variable.

Interoperability becomes economically distinct only if it changes at least one additional object or strategic linkage that cannot be absorbed into `t`, for example:

- accessible network size;
- pairwise connection structure;
- complement availability;
- switching state dependence;
- coalition participation/deviation payoffs;
- asymmetric cross-border surplus flows;
- implementation costs with an independently justified technology.

Accordingly, "a common standard reduces Salop transport cost" is insufficient as the core mechanism.

### 5.3 Artificial interiority risk

Stadler et al. (2022) already derives intermediate compatibility using coordination-cost structure. Therefore, even successful derivation of `0 < a_o* < 1` would not by itself distinguish this project.

Any convex implementation cost still requires independent economic interpretation. The project must not choose curvature because it mechanically produces a first-order condition with an interior root.

## 6. Theory vs. empirical route

**Recommended route: theory.**

The central unresolved question is a strategic timing / institutional-design problem: formal coalition formation and private post-coalition implementation interact through national welfare and deviation incentives. This is naturally a theory question.

An empirical route could later motivate or discipline the implementation margin, but at Stage 0 there is no identified dataset, quasi-experiment, or measurable causal estimand. A mixed route would therefore be premature.

The theory route should remain minimal. It should not simultaneously endogenize firm locations, dynamic installed bases, coalition membership, interoperability topology, standards design, and pricing.

## 7. One-sentence research question

> **When a formal standards coalition fixes participation but member firms retain control over implementation-level interoperability, under what conditions does the profit-maximizing interoperability choice differ from the national-welfare threshold required for coalition stability enough to change whether the coalition persists or unravels?**

This replaces the broader provisional question for purposes of Stage 1 audit.

## 8. Initial literature map

Stage 1/2 must organize the literature by whole-game role rather than keyword overlap.

### Family A — endogenous degree of compatibility + price/quantity competition

Priority sources:

- Stadler, Tobler Trexler & Unsorg (2022).
- Foros & Hansen (2001).
- Garcia (2016).
- the 1999 partial-compatibility paper with network externalities and double purchase.

Question: Is private continuous interoperability plus downstream competition already fully characterized, including the private/welfare wedge?

### Family B — compatibility + alliance / coalition stability

Priority sources:

- Toshimitsu (2018).
- Economic Modelling (2022), "Partial compatibility in two-sided markets: Equilibrium and welfare analysis."
- Economides & Flyer (1997/1998).

Question: Does an existing network alliance/compatibility coalition already reproduce government participation, firm compatibility, and stability after suitable relabeling?

### Family C — standards / common compatibility decisions

Priority source:

- Stadler et al. (2022), especially the common standardization decision and SDO-cost comparison.

Question: Is the proposed formal-coalition stage merely their common compatibility decision with countries renamed as standards members?

### Family D — switching costs / portability / lock-in

Priority source:

- Jeon, Menicucci & Nasr (2023).

Question: Can a non-network switching/portability mechanism create the post-coalition wedge, or is it already absorbed by dynamic compatibility-choice models?

### Family E — network topology / modern interoperability

Priority sources:

- Huang, Tan, Teh & Zhou (2026), "A Network Approach to Interoperability."
- Peitz (2026), "Asymmetric Platform Oligopoly."

Question: Does continuous/pairwise interoperability in an oligopoly network already generate the pricing/welfare objects needed for this project?

### Family F — modular / systems compatibility

Priority sources to recover and audit through citations in the close papers:

- Matutes & Regibeau (1988), mix-and-match compatibility;
- Economides (1989) and related compatibility-system models;
- partial compatibility / supporting-services literature;
- optimal compatibility in systems markets.

Question: Is the proposed complement-access mechanism merely a classic systems-market compatibility result?

### Family G — international standards and national welfare

This is the most important potentially surviving family. Stage 1 must search explicitly for models with:

- countries/governments as coalition members;
- firms as separate strategic actors;
- endogenous post-agreement compatibility/implementation;
- national rather than world welfare;
- membership/deviation stability affected by firms' implementation choices.

The related repository `private-compatibility-standards-coalitions` is a benchmark/provenance source only, not evidence that this combination is novel.

## 9. Required Stage 1 inputs

Stage 1 must obtain and verify, at minimum:

1. Full text of Stadler et al. (2022), with exact utility, compatibility technology, timing, cost structure, equilibrium compatibility, common-decision case, and welfare content.
2. Full text of Foros & Hansen (2001), with exact interpretation of the compatibility level, Hotelling subgame, and private-versus-welfare investment result.
3. Full text of Toshimitsu (2018), especially the definition and stability concept of the network alliance and whether alliance membership is chosen by firms or another actor.
4. Full text of Garcia (2016) and the 1999 partial-compatibility paper to determine whether continuous compatibility plus Bertrand/quantity competition is already generic.
5. Full text / working paper of Huang et al. (2026) because it is a current direct interoperability paper and may dominate a network-topology extension.
6. The relevant section of Peitz (2026) on partial compatibility and its treatment of network effects, pricing, and user surplus.
7. Jeon et al. (2023) for the non-network switching/portability route.
8. The original prior standards-coalition model from `private-compatibility-standards-coalitions`, read only as an explicit benchmark, to identify exactly what changes when implementation `a` is inserted after coalition formation.
9. A Stage 1 player/timing/objective comparison table for every close paper: players, decision makers, timing, compatibility variable, product competition, government role, welfare object, coalition concept, and equilibrium/stability result.
10. A precise institutional interpretation for "formal standard fixed but implementation interoperability remains privately discretionary." Without such an interpretation, the surviving timing distinction risks becoming formal rather than economic.

## 10. Minimum economic primitives for a later interiority test

An eventual minimal model should require no more than the following primitives until the mechanism survives:

1. A formal coalition state `C` or membership profile chosen by governments/countries.
2. A firm-controlled interoperability implementation variable `a_i` available after `C`.
3. A downstream market competition stage.
4. One consumer benefit channel from interoperability.
5. One private cost/rent-loss channel from interoperability with an independent economic interpretation.
6. National welfare that differs structurally from firm profit.
7. A coalition-deviation payoff calculated after anticipating the firm's equilibrium `a_i`.

Salop is not a necessary primitive. Network externalities are not a necessary primitive. Neither should enter unless Stage 1/3 shows they are indispensable to the surviving mechanism.

## 11. Conceptual assessment of `a_o*` vs. `â`

The distinction is **conceptually meaningful**, but only under a careful definition.

Define `a_o*` as the equilibrium interoperability implementation chosen by profit-maximizing firms in the relevant coalition state.

Do **not** define `â` as merely the government's welfare-maximizing `a`. Instead, the more useful object is a **coalition-stability threshold**: the interoperability level at which a government's membership payoff equals its deviation payoff, for example conceptually

`W_i(member | a) - W_i(deviate | equilibrium continuation) = 0`.

Then:

- `a_o*` comes from a firm's private optimization problem;
- `â` comes from a government's participation/deviation condition;
- they can differ even if the government never directly chooses `a`;
- the ordering `a_o* < â` can mean private implementation is too weak to sustain participation;
- `a_o* > â` can mean firms privately implement enough interoperability to sustain the coalition, or potentially overprovide it from a national perspective depending on the rest of the model.

This is a genuine conceptual separation because the objectives, decision makers, and equilibrium conditions are different.

However, if the government directly chooses `a`, if government welfare is proportional to firm profit, or if the deviation payoff changes with `a` in exactly the same way as the firm's profit, the distinction can collapse. Stage 1/4 must test this rather than assume it.

## 12. Evidence/modeling results that would make interoperability economically important rather than cosmetic

The project becomes economically meaningful only if at least one of the following survives:

- holding formal coalition membership fixed, endogenous firm implementation changes a government's incentive to remain in or leave the coalition;
- the firm's compatibility FOC and the government's participation condition respond differently to a primitive parameter, causing a genuine stability regime change;
- a multi-member interoperability externality creates free riding or strategic complementarity not present in the binary benchmark;
- an interoperability change affects both product-market competition and a distinct network/complement/portability object, so it cannot be absorbed into `t(a)`;
- the endogenous-implementation model generates a coalition/welfare proposition unavailable in both the prior binary coalition model and the standard continuous-compatibility model separately.

Interiority alone is not sufficient.

## 13. Stage 0 decisions

### Accepted

- Continue as a theory candidate to Stage 1 audit.
- Reframe the contribution target around **formal coalition formation followed by privately controlled interoperability implementation and feedback into national coalition stability**.
- Treat `0 < a_o* < 1` as a viability condition, not a novelty claim.
- Define `â`, if retained, as a coalition participation/deviation threshold rather than automatically as the government's welfare optimum.
- Keep Salop and network effects optional.

### Rejected

- "Continuous compatibility" as a novelty claim.
- "Salop + network effects + endogenous interoperability" as a contribution claim.
- Interiority by itself as evidence that the model is worth a paper.
- Treating common standardization by firms as equivalent to a government standards coalition without proving the distinction.

## 14. Final verdict

# `GO TO AUDIT`

The broad original mechanism is substantially preempted by prior literature, but a narrower whole-game question survives: whether a government standards coalition can be destabilized or stabilized by firms' endogenous post-agreement interoperability implementation.

This is sufficiently precise and economically nontrivial to justify Stage 1, but novelty is **not** established.

## 15. Next-stage contract

Stage 1 may audit only the following research object:

> formal standards coalition / government membership -> privately controlled interoperability implementation -> downstream market competition -> national welfare -> coalition participation/deviation stability.

Stage 1 must determine whether this timing, actor separation, and stability feedback is already present in prior work and whether a minimal economic interpretation exists for post-standard private interoperability discretion.

Stage 1 must **not**:

- treat Salop as canonical;
- assume network effects are necessary;
- claim novelty from combining known ingredients;
- build a full model;
- import the frozen theory of `private-compatibility-standards-coalitions` as if it were established here;
- add a convex cost solely to force interiority.

If Stage 1 finds a paper whose whole game already contains government/formal-coalition membership, privately chosen post-agreement interoperability, downstream competition, national welfare, and coalition stability with no substantive missing strategic result, the project should be routed toward `NO-GO` at the earliest affected gate rather than repaired by adding complexity.
