# Stage 7.5 — Full-Theory Freeze Decision: C-ESD

Date: 2026-09-04
Canonical workflow: `ryotamatsuki/research-paper-workflow` v1.1
Release SHA: `488e5ab06c207909296a7564eaf9066f7f94319c`

## 1. Executive freeze-decision verdict

**GO TO FULL PAPER.**

C-ESD now contains more than a model-specific algebraic curiosity. The surviving result can be stated without notation, survives the canonical nested-benchmark test, has a nonempty regular region rather than a knife-edge witness, generates an exact national/global welfare wedge, and admits a broader convex-adjustment-cost interpretation.

The project should therefore receive full-paper investment, subject to a Stage-8 theory freeze. No new strategic extension is required before manuscript construction.

The contribution must remain narrow. The paper is not about the novelty of interoperability policy, Salop competition, network effects, endogenous product differentiation, or partial standards unions individually. Its contribution is the interaction-induced reversal of government coalition preferences when standard depth and product positioning are both endogenous.

## 2. Working title and core question

Working title:

> **Standards Coalitions, Endogenous Standard Depth, and Strategic Product Repositioning**

Core question:

> Can firms' endogenous product repositioning overturn the international standards-coalition outcome selected when governments choose the depth of interoperability?

## 3. Mechanism card

### Phenomenon

Regional standards unions may become politically stable even when international standardization is selected in benchmarks that endogenize only government policy or only firm product differentiation.

### Friction

A standards bloc can deepen internal interoperability, reducing within-bloc standard friction while increasing relative separation from outsiders. Firms retain a distinct horizontal product-characteristic margin that can be redesigned only at real adjustment cost.

### Strategic response

After a regional standards union compresses standard-based differentiation between its members, member firms strategically move apart on the remaining product-characteristic dimension. This re-differentiation softens competition and reallocates rents toward member firms.

### Equilibrium effect

At the canonical regular witness and an open audited neighborhood:

- `B-T` (endogenous policy, fixed locations): IS is stable;
- `B-X` (exogenous zero depth, endogenous locations): IS is stable;
- `FULL` (endogenous policy and endogenous locations): SU members re-differentiate, the three SUs are stable, and IS is pair-blockable.

Formally:

`Delta_M^(B-T)<0`,

`Delta_M^(B-X)<0`,

but

`Delta_M^(FULL)>0`.

### Welfare effect

The SU member gain is not a consumer-surplus gain. Exactly,

`Delta_M = Delta Pi_M + Delta CS/3`.

At the canonical witness:

- `Delta CS/3=-0.0325785`;
- `Delta Pi_M=+0.0341498`;
- `Delta_M=+0.0015713`.

Domestic producer-rent gains narrowly outweigh member consumer losses.

World welfare satisfies

`GW=A+v q'Gq-TC-sum_i C_i^D`,

so prices cancel as transfers. At the witness, `GW_IS>GW_SU>GW_SW`. The politically stable regional union is globally inefficient relative to IS.

Private firms also over-re-differentiate relative to the constrained social location benchmark.

### Empirical implication

Deeper regional/interface standardization should be associated with convergence on the regulated interface dimension but greater differentiation on unregulated/non-interface product characteristics among member firms, especially when redesign costs are intermediate rather than prohibitive.

## 4. Essential assumptions versus tractability assumptions

### Essential economic assumptions

1. **Policy-controlled compatibility depth.** Governments/blocs can choose a meaningful interoperability/standard-depth margin after the formal coalition partition is known.
2. **Bloc asymmetry.** Under SU, deeper integration lowers within-bloc standard friction while raising relative bloc-boundary separation. The exact `1/2` coefficient is not essential, but the within-versus-cross-bloc asymmetry is.
3. **A separate product-differentiation margin.** Firms can reposition on a product characteristic distinct from the standardized interface.
4. **Positive but costly repositioning.** Repositioning is feasible but not free; the mechanism requires an intermediate effective adjustment-cost curvature.
5. **Network externality.** The compatibility regime changes network reach/value and thereby the product-location incentive. In the selected mechanism, eliminating the network force kills the diagnostic SU re-differentiation channel.
6. **National objectives include domestic producer rents but not foreign producer rents.** This creates the government/global welfare wedge.
7. **Sequential commitment.** Governments choose standards depth before firms choose product positions and prices.

### Tractability / normalization assumptions

1. Three symmetric countries/firms.
2. Unit Salop circle and equally spaced inherited anchors.
3. Quadratic baseline redesign cost `gamma d_c(x_i,h_i)^2/2`.
4. Uniform consumers and symmetric `CS/3` national incidence.
5. Full market coverage.
6. Zero marginal production cost.
7. Fixed network coefficient `v` conditional on the formal compatibility graph.
8. No direct policy cost.
9. The cross-bloc coefficient `1/2` in the policy map, chosen as a symmetric mean-preserving normalization for SU pairwise frictions.

The Stage-7 convex-cost audit shows that quadratic curvature is not the conceptual source of the mechanism: for a regular convex cost with `C(0)=C'(0)=0`, finite local curvature and the same SU marginal-profit force generate positive re-differentiation. The headline reversal requires intermediate effective curvature.

## 5. Core propositions and proof / verification status

### P1 — Exact downstream price system

**Verified analytically.**

For heterogeneous pairwise frictions, demand is a weighted-Laplacian affine system. The price equilibrium is uniquely characterized on the regular domain by the exact matrix solution documented in Stage 4.

### P2 — SU strategic re-differentiation

**Verified on the selected regular branch and generalized locally to convex adjustment costs.**

The SU asymmetry generates a nonzero outward location force for members, while symmetric IS/SW inherited configurations have zero corresponding force. Stage 4 and Stage 7 establish positive re-differentiation in the regular region.

Not claimed: a global theorem that every parameterization or every local stationary point yields a valid location Nash equilibrium. Low-adjustment-cost counterexamples with profitable circle jumps are documented and excluded.

### P3 — FULL-only coalition-stability reversal

**Verified as a constructive nonempty-region result.**

At `(t_bar,v,gamma,s_bar)=(1,0.04,0.11,0.25)`:

`Delta_M^(B-T)=-0.010167`,

`Delta_M^(B-X)=-0.000434`,

`Delta_M^(FULL)=+0.001571`.

All continuation regularity and whole-circle unilateral location-deviation checks pass. Strict inequalities plus continuity imply a nonempty open region. Numerical neighborhood audits pass 23/27 nearby points and 108/125 on the wider grid.

Not claimed: a closed-form global characterization of the entire parameter space.

### P4 — National member threshold

**Exact identity.**

A prospective SU member prefers SU iff

`Delta Pi_M > -Delta CS/3`.

This identifies the reversal as domestic producer-rent capture rather than consumer gain.

### P5 — Global welfare wedge

**Exact identity plus verified witness ranking.**

`GW=A+v q'Gq-TC-sum_i C_i^D`.

At the witness, `GW_IS>GW_SU>GW_SW`, while decentralized coalition stability selects SU.

### P6 — Private over-re-differentiation

**Verified at the canonical SU policy/witness as a second-best location comparison.**

Inherited distance `0.333333`, constrained social distance `0.431427`, private equilibrium distance `0.497533`.

Not claimed as a global theorem for all parameters.

### P7 — Intermediate adjustment-cost condition

**Verified as an economic-region characterization, not a global closed-form theorem.**

The selected regular reversal requires

`gamma_GBR(v,s_bar) < gamma < gamma_W(v,s_bar)`

plus the benchmark inequalities. For `v=0.04,s_bar=0.25`, `gamma_W=0.132983` and the audited global-BR transition is approximately `gamma≈0.10`.

## 6. Closest-paper distinction

The strongest synthesis attack combines Ruiz (2004) with Gandal–Shy (2001). Ruiz already has government standard-recognition policy followed by firms' endogenous product characteristics and price competition, so the policy-to-product-position timing is not new. Gandal–Shy already has three countries, standardization unions, network effects, national welfare, and coalition incentives, so partial standards-union stability is not new. However, neither paper contains the full strategic-feedback network tested here: regime-specific endogenous standard depth induces endogenous horizontal product repositioning, and the resulting product response reverses the national coalition ranking relative to both the policy-only and location-only benchmarks. Ruiz's endogenous-characteristics extension does not generate this coalition-stability reversal, while Gandal–Shy has no post-policy endogenous product-location margin. The contribution is therefore the verified interaction result, not a claim that the ingredients themselves are new.

This distinction is precise enough for a field-paper introduction, although the synthesis attack remains the strongest referee risk.

## 7. Welfare and generality case

The project passes the substantive-welfare test for three reasons.

First, the national coalition gain and world welfare move in opposite directions. This is a genuine organizational misallocation, not a price-transfer accounting artifact.

Second, the private product-location response is distorted relative to a constrained social planner: firms re-differentiate too much once the regional standard is deepened.

Third, the mechanism generalizes conceptually beyond the quadratic cost and beyond one industry label. It requires a policy-controlled interface dimension, network value, a separate horizontal product margin, and national objectives with domestic-rent incidence. Stage 7 identified physical EV-charging standards and digital messaging interoperability as genuinely different institutional analogues for the policy primitive, while correctly leaving strategic re-differentiation as an empirical prediction rather than an established fact.

## 8. Would a skeptical field referee see more than a parameter exercise?

**Yes, with disciplined presentation.**

Reasons:

1. The headline result is explicitly benchmarked against B-T and B-X and disappears when either strategic margin is removed.
2. The canonical witness is globally checked, not merely a local FOC solution.
3. Strict witness inequalities plus continuity produce an open parameter region.
4. The welfare decomposition is exact and economically interpretable.
5. The same qualitative mechanism extends to regular convex adjustment costs.
6. Counterexamples are documented rather than repaired with ad hoc primitives.

The project would become a parameter exercise only if the paper over-emphasized the numerical threshold table or claimed a universal ranking. The manuscript must instead center the interaction mechanism and the rent-capture/global-welfare wedge.

## 9. Major referee risks

### Risk 1 — Ruiz + Gandal–Shy synthesis

**Major, not fatal.**

Defense: result-level interaction and benchmark sign reversal, not ingredient novelty.

### Risk 2 — No closed-form global `gamma_GBR`

**Major technical limitation, not a freeze blocker.**

The global circle ordering creates nonsmooth jumps. The paper should state the result as a constructive open-region theorem/verified proposition and avoid pretending to have a complete global classification.

### Risk 3 — Symmetric national CS incidence

**Major interpretation limitation, not fatal.**

`CS/3` is a clean symmetric baseline. The paper must not claim heterogeneous national incidence results absent from the model.

### Risk 4 — Policy-map specificity

**Major modeling risk.**

The exact `1/2` cross-bloc coefficient is a normalization; the paper must explain the deeper economic restriction as mean-preserving redistribution of standard differentiation from within-bloc to bloc-boundary pairs. Novelty cannot rely on this exact coefficient.

### Risk 5 — Institutional evidence does not establish re-differentiation

**Not fatal.**

Institutional examples validate the policy-controlled interoperability margin only. Re-differentiation remains a falsifiable model prediction.

No unresolved risk currently qualifies as a single fatal blocker requiring a return to Stage 3–7.

## 10. Full-paper value assessment

**Full-paper value: YES.**

The branch now has:

- a concise general mechanism;
- a result unavailable in both nested benchmarks;
- a globally checked constructive equilibrium witness and nonempty open region;
- exact national and global welfare identities;
- a private/social product-positioning wedge;
- a general convex-cost interpretation;
- a disciplined novelty distinction against the two closest literatures;
- multiple institutional analogues for the policy primitive.

This package is materially stronger than a research note.

## 11. Recommended journal level

Recommended level: **field-journal full paper**.

Primary fit recommendation: **International Journal of Industrial Organization (IJIO)** level, given the core industrial-organization mechanism, product differentiation, compatibility/network effects, government policy, and coalition/welfare results.

A stronger general-theory outlet would require a substantially more global analytic characterization than is currently frozen. A short-note outlet would understate the existing welfare and mechanism package.

Journal target is recommended rather than permanently locked at Stage 7.5; Stage 8 may record the target while freezing theory, but may not alter the model to fit a journal.

## 12. Exact Stage-8 freeze scope

Stage 8 should freeze exactly the following theory package.

### Frozen timing

`rho -> bloc depths s_C -> pairwise Tau(rho,s) -> product locations x_i -> prices -> W_i -> coalition stability`.

### Frozen policy map

- same bloc: `tau_ij=t_bar-s_C`;
- different blocs: `tau_ij=t_bar+(s_C+s_D)/2`;
- bloc objective: `sum_{i in C} W_i`;
- simultaneous bloc-depth choices.

### Frozen product-market block

- unit Salop circle;
- weighted-friction consumer utility with fixed network coefficient `v` conditional on formal compatibility graph;
- inherited symmetric anchors;
- costly product repositioning;
- downstream price competition;
- full coverage regular domain.

### Frozen welfare block

- national welfare `W_i=CS/3+Pi_i`;
- global welfare identity with price-transfer cancellation;
- strict-blocking IS/SU/SW coalition stability.

### Frozen main contribution

Only:

> **Interaction-induced coalition-stability reversal:** policy endogeneity alone and product-position endogeneity alone leave IS stable, while their interaction can induce SU-member re-differentiation that raises domestic producer rents enough to reverse member national welfare and make regional standards unions stable; the resulting decentralized SU can be globally welfare-inferior to IS.

### Frozen supporting results

1. Exact weighted-Laplacian demand/price characterization.
2. SU strategic re-differentiation on the regular branch.
3. Exact member threshold `Delta Pi_M > -Delta CS/3`.
4. Exact global welfare identity.
5. Private over-re-differentiation at the canonical witness/second-best comparison.
6. Intermediate adjustment-cost regularity/welfare region.
7. B-T and B-X as mandatory nested benchmarks.

### Explicitly excluded from Stage-8 freeze

Do not add before manuscript construction:

- relative-profit objectives;
- private interoperability investment;
- endogenous network intensity;
- policy costs;
- transfers or side payments;
- lobbying;
- dynamics;
- endogenous topology choice;
- additional countries;
- heterogeneous national CS incidence;
- alternative spatial geometries solely to strengthen the theorem;
- empirical estimation.

Any such item is future-work/robustness material and requires a separate post-freeze decision.

## 13. Final verdict

**GO TO FULL PAPER.**

Route:

`Stage 7.5 GO -> Stage 8 Theory Freeze -> full-paper construction`.
