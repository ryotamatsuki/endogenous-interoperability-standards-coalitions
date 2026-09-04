# Stage 6 — Novelty Re-Kill: C-ESD

Date: 2026-09-04
Canonical workflow: `ryotamatsuki/research-paper-workflow` v1.1
Release SHA: `488e5ab06c207909296a7564eaf9066f7f94319c`

## 1. Executive re-kill verdict

**GO -> GO TO WELFARE / GENERALITY.**

Stage 6 kills nearly every setup-level and ingredient-level claim, but one proposition survives the whole-game absorption test:

> There exists a regular parameter region in which endogenous government standard-depth choice alone and endogenous firm product positioning alone each select international standardization, while their interaction induces strategic re-differentiation by regional-standardization members and reverses government coalition preferences, making the three two-country standardization unions stable and international standardization pair-blockable.

At the Stage-4 witness:

`Delta_M^(B-T)<0`,

`Delta_M^(B-X)<0`,

but

`Delta_M^(FULL)>0`.

No audited prior model or theorem directly reproduces this interaction result.

This is a novelty-survival decision, not a priority proof. The strongest remaining threat is the combination of Ruiz (2004) and Gandal–Shy (2001).

## 2. Frozen Stage-4 proposition set

The model is unchanged at Stage 6.

Timing:

`rho -> bloc depths s_C -> pairwise Tau(rho,s) -> product locations x_i -> prices -> national welfare -> coalition stability`.

Nested benchmarks:

- `B-T`: endogenous government depth, fixed locations;
- `B-X`: zero depth, endogenous locations;
- `FULL`: endogenous depth and endogenous locations.

Stage-4 witness:

- B-T stable set: `{IS}`;
- B-X stable set: `{IS}`;
- FULL stable set: `{SU_12,SU_13,SU_23}`.

## 3. Proposition-by-proposition re-kill

### P1 — Government standards policy affects endogenous product differentiation

**KILLED AS NOVELTY.**

Ruiz (2004) directly studies governments choosing recognition policy before firms choose product characteristics and then compete in prices. Therefore the timing `government standard policy -> endogenous product characteristics -> price competition` is old.

Ruiz is particularly damaging to any broad C-ESD claim because he explicitly asks whether endogenous product characteristics change the policy result.

### P2 — Compatibility/network effects and product differentiation interact strategically

**KILLED AS NOVELTY.**

This is deeply established in Economides–Flyer, Matutes–Padilla, Baake–Boom, Jonard–Schenk, Wang–Lyu, and related network-compatibility work.

Do not claim novelty from `Salop + compatibility + network effects + endogenous differentiation`.

### P3 — Partial compatibility / a two-member standards coalition can be stable

**KILLED AS NOVELTY.**

Gandal–Shy obtain two-country standardization unions in a three-country government model. Matutes–Padilla obtain strict-subset ATM sharing in a three-bank spatial/network model. Economides–Skrzypacz derive standards coalitions of various sizes. Ding–Ko–Shen show partial compatibility can be a unique coalition-proof market outcome.

Therefore the fact that `SU` can be stable is not a contribution.

### P4 — Governments choose a continuous compatibility/interoperability policy under network effects

**KILLED AS NOVELTY.**

Klimenko (2009) directly analyzes continuous government policies toward technical compatibility in network industries, including non-cooperative policy and international agreements.

### P5 — Interoperability regulation can induce a strategic firm response that offsets its intended effect

**KILLED AS A BROAD CLAIM.**

Recent work by Kretschmer, Rasch, Shekhar & Wenzel studies a mandated-interoperability-induced strategic response by the incumbent that can offset regulatory objectives and even harm users. The response variable differs, but the generic unintended-response claim is not new.

### P6 — Coalition-based interoperability has different competition/welfare effects from industry-wide interoperability

**KILLED AS NOVELTY.**

The current Huang–Tan–Teh–Zhou working paper studies weighted interoperability networks and explicitly distinguishes industry-wide and coalitional interoperability configurations, deriving price and welfare effects.

### P7 — FULL-only standards-coalition stability reversal

**SURVIVES AS MAIN CONTRIBUTION CANDIDATE.**

The exact result is:

`Delta_M^(B-T)<0`,

`Delta_M^(B-X)<0`,

`Delta_M^(FULL)>0`.

Equivalently, policy endogeneity alone selects IS, product-position endogeneity alone selects IS, but the interaction selects SU.

No re-opened paper directly establishes this result or makes it an immediate corollary.

The closest threat, Ruiz, has the relevant policy-to-location timing but reports that endogenous product characteristics do not reverse the qualitative government-policy equilibrium. The closest coalition paper, Gandal–Shy, has the three-country standards-union architecture and coalition incentives but no endogenous product-location response. Current weighted-interoperability work has coalition configurations, prices and welfare but no government coalition-stability reversal induced by endogenous product repositioning.

## 4. Whole-game absorption test

### Ruiz (2004)

Players: two governments, two firms, consumers.

Strategies/timing: government recognition -> endogenous product characteristics -> price competition.

Objective: national welfare including domestic profit.

Overlap: extremely strong on sequential policy/product-differentiation architecture.

Missing from Ruiz: three-country IS/SU/SW coalition partition, continuous bloc depth, network coalition graph, coalition-stability comparison.

Most importantly, Ruiz's endogenous-location extension preserves his government-policy qualitative conclusion rather than generating the C-ESD interaction reversal.

Classification: **STRUCTURALLY VERY CLOSE**, not exact prior art.

### Gandal & Shy (2001)

Players: three governments/countries/firms.

Architecture: recognition policy; standardization unions; network effects/conversion costs; national welfare and participation incentives.

Overlap: extremely strong on institutional coalition structure.

Missing: endogenous product positioning after policy and continuous standard depth.

Classification: **STRUCTURALLY VERY CLOSE**, not exact prior art.

### Klimenko (2009)

Overlap: continuous government compatibility policy, international competition, network effects, international coordination.

Missing: standards-union coalition formation/stability and endogenous product positioning.

Classification: **STRUCTURALLY VERY CLOSE**.

### Matutes–Padilla / Economides–Skrzypacz / Ding–Ko–Shen

Overlap: partial compatibility coalitions can arise or be stable.

Missing: government-depth -> product-location -> national coalition preference feedback.

Classification: **STRUCTURALLY VERY CLOSE / COMPONENT OVERLAP**, depending on paper.

### Huang–Tan–Teh–Zhou (2026)

Overlap: current frontier on weighted interoperability networks, coalitional configurations, pricing and welfare.

Missing: endogenous horizontal product positioning and government standards-coalition stability.

Classification: **STRUCTURALLY VERY CLOSE / CURRENT FRONTIER**.

### Whole-game conclusion

No single prior game reproduces the economically relevant player set, strategy sets, timing, endogenous controls, welfare incidence and stability comparison after direct relabeling or parameter restriction.

Reconstruction requires stitching together multiple prior literatures with different players and feedback networks. Under the canonical checklist, that is not sufficient for absorption because the FULL architecture generates a result absent from both nested benchmarks.

## 5. Nested-benchmark result comparison

| Result | B-T | B-X | FULL | Prior-art status |
|---|---:|---:|---:|---|
| Government depth endogenous | yes | no | yes | old — Klimenko-type policy margin |
| Product location endogenous | no | yes | yes | old — Ruiz / spatial-differentiation literature |
| SU-specific strategic re-differentiation | no | limited/exogenous-depth only | yes | ingredients old; exact government-depth interaction not directly located |
| IS stable | yes | yes | no | IS stability itself old |
| SU stable | no | no | yes | SU stability itself old |
| `Delta_M` sign reversal created only by interaction | no | no | **yes** | **survives** |

## 6. Updated closest-paper ordering

1. **Ruiz (2004)** — strongest strategic-timing threat.
2. **Gandal & Shy (2001)** — strongest institutional/coalition threat.
3. **Klimenko (2009)** — strongest continuous-government-compatibility threat.
4. **Huang, Tan, Teh & Zhou (2026)** — strongest current interoperability-network/welfare threat.
5. **Ding, Ko & Shen (2022)** — strongest coalition-proof partial-compatibility threat.
6. **Matutes & Padilla (1994)** — strongest three-player Salop/network partial-compatibility threat.
7. **Economides & Skrzypacz (2003/04)** — strongest firm-standards-coalition threat.
8. **Wang & Lyu (2020)** — strongest endogenous-positioning/network-compatibility threat.
9. **Kretschmer et al. (2025)** — strongest recent strategic-response-to-mandate threat.
10. **Agur & Copestake (2025)** — relevant policy × coalition interaction analogy, but different game.

Detailed matrix: `literature/STAGE6_CESD_CLOSEST_PAPER_MATRIX.md`.

## 7. Killed claim set

The following must not be used as contribution claims after Stage 6:

- government standards policy can affect firm product characteristics;
- interoperability reduces differentiation / changes price competition;
- network effects create compatibility incentives;
- firms may strategically re-differentiate in compatibility/network markets in a broad sense;
- continuous government compatibility policy;
- international compatibility agreements;
- partial compatibility or standardization unions can be stable;
- coalition interoperability can outperform full interoperability on some welfare dimension;
- mandated interoperability can have unintended strategic responses;
- circular spatial competition with compatibility/network effects.

## 8. Surviving claim set

Only the following claim is authorized as the main contribution candidate:

> **Interaction-induced coalition-stability reversal.** Endogenous government standard depth and endogenous firm product positioning are strategic complements at the game-architecture level: each margin alone leaves international standardization stable, but together they induce regional-standardization members to re-differentiate enough to reverse their national-welfare ranking and destabilize international standardization in favor of regional standards unions.

Secondary mechanism description, not a separate novelty claim:

`SU depth -> lower internal standard friction / higher boundary friction -> member product re-differentiation -> member profit and national welfare rise relative to IS -> coalition preference reversal`.

## 9. Revised contribution statement

Do not write: "We introduce endogenous interoperability, network effects and product differentiation into a standards-coalition model."

Use instead:

> Existing work separately shows that governments choose compatibility policy, firms adapt product characteristics to standards policy, and partial standards coalitions can be stable. The contribution here is an interaction result: when government standard depth and firm product positioning are both endogenous, the strategic product response can reverse the government coalition ranking even though either endogenous margin in isolation selects international standardization.

## 10. Strongest remaining novelty threat

**Ruiz (2004) + Gandal–Shy (2001) synthesis attack.**

A hostile referee can argue that C-ESD simply grafts Ruiz's endogenous product characteristics onto Gandal–Shy's standardization unions. Stage 6 does not find a direct prior theorem establishing the FULL-only reversal, so this is not absorption. But this attack is credible.

Stage 7 must therefore show that the reversal has a clean economic region/condition and is not merely a numerical consequence of one Salop/redesign specification. Generality is now essential to publication value.

A second current threat is Huang–Tan–Teh–Zhou (2026), because it moves interoperability research toward weighted coalition networks and welfare. The distinction must remain explicit: their strategic object is interoperability-network configuration/strength and price competition, while C-ESD's surviving result comes from government standard depth inducing endogenous horizontal repositioning and changing national coalition stability.

## 11. Evidence limits

- Ruiz is a working-paper version located through a publicly available full-text copy; no later journal publication was identified in this audit.
- Economides–Skrzypacz is a working-paper/SSRN contribution.
- Huang–Tan–Teh–Zhou is a current 2026 working paper and may evolve.
- Recent working papers were searched through 2026-09-04; the search cannot prove nonexistence of unpublished work.

Accordingly the correct claim is "survives the audited novelty re-kill," not "first in the literature."

## 12. Canonical verdict

**GO**.

Route:

**GO TO STAGE 7 — WELFARE / GENERALITY.**

Stage 7 may interpret and generalize only the surviving FULL-only interaction result. All killed setup-level claims remain dead.

Stage 7 must specifically attack whether the sign reversal survives beyond the witness/redesign-cost specification and characterize the economic condition under which strategic re-differentiation overturns the standards-coalition ranking.