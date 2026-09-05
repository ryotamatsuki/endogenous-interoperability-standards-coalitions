# Stage 4RR — Global Price-Continuation Repair

Date: 2026-09-05

Canonical workflow: `ryotamatsuki/research-paper-workflow` **v1.2**

Workflow release tag: `v1.2`

Reopened theory: `CESD-THEORY-FREEZE-2026-09-04-v2`

## 1. Executive verdict

**CONDITIONAL GO — ONE BLOCKER: COMPLETE AND CERTIFY THE EXPLICIT LOCALIZED-COMPETITION PRICE CONTINUATION.**

The old unrestricted-SPNE claim remains invalid. The preferred all-product weighted-geodesic repair is not yet certified because the linear circular price game can leave the regular local branch after feasible location deviations, and pure-strategy continuation existence is not guaranteed merely by the old FOC/SOC system.

However, Stage 4RR identifies one bounded and economically recognizable repair: make the localized-competition structure explicit. Consumers located on the arc bounded by two adjacent product positions compare only those two bounding products. This is not treated as an implicit consequence of Salop distance; it is an explicit consideration/market-segmentation primitive.

The exact hostile counterexample then no longer works: at `x=(0.4,0.5,5/6)` and the old price candidate `p=(0.25,0.215,0.285)`, lowering firm 2's price to `0.174` raises its all-product demand to `0.648`, but under the explicit localized choice set its demand is only `0.340666...` and operating profit is `0.059276`, below the old candidate profit `0.0616333...`.

This does **not** yet prove global price equilibrium under localized competition. Corners and active-set switches must now be solved rather than discarded.

## 2. Why the all-product repair is not closed

The current pairwise friction primitive `tau_ij` was originally used on the arc bounded by products `i` and `j`. A weighted-geodesic extension can make this into a globally defined delivered-cost metric, so it is a coherent all-product extension.

But the old price formula is only the interior adjacent-market branch. The hostile example proves that a finite price cut can cross that branch and poach consumers from another segment. Therefore the old formula cannot be used as the continuation at arbitrary off-path locations.

The broader spatial-competition literature confirms that this is a real equilibrium-existence issue rather than a numerical nuisance. de Frutos, Hamoudi and Jarque (1999), *Regional Science and Urban Economics*, show for a circular location-then-price model that, outside special transport-cost specifications, feasible locations can exist for which no pure price equilibrium exists. DOI: `10.1016/S0166-0462(99)00014-9`.

This result is not imported mechanically as a theorem for the present three-firm heterogeneous-friction/network model. It is used as a kill warning: the workflow may not presume pure continuation existence after arbitrary location deviations.

## 3. Repair candidates

### A. All-product weighted-geodesic choice

Status: **UNRESOLVED / NOT CERTIFIED**.

Pros:
- closest to a literal global spatial-choice interpretation;
- allows a consumer to compare all products;
- preserves the idea that compatibility changes effective separation.

Blocker:
- requires a global price-subgame solution, potentially including mixed continuation if pure equilibrium fails at relevant histories;
- the old linear branch is insufficient;
- this is not a bounded repair relative to the current manuscript.

### B. Explicit localized competition / bounding-product consideration

Status: **SELECTED BOUNDED REPAIR CANDIDATE**.

Primitive:
- sort product locations on the circle;
- each consumer belongs to one arc between two adjacent product positions;
- that consumer's consideration set is exactly the two products bounding that arc;
- on arc `(i,j)` the delivered utility comparison uses the existing pairwise `tau_ij` symmetrically for distance to either endpoint;
- if a price deviation causes one endpoint to capture the whole arc, demand is clipped at the arc boundary rather than returning `None`;
- order changes trigger a new adjacency graph and a new set of arc-level contests;
- zero-length/coincident-location cases must receive an explicit tie/segment rule before certification.

This is a substantive model interpretation and must be stated in the model section. It cannot be hidden behind the phrase 'interior Salop equilibrium'.

This route has precedent as localized spatial competition. Modern treatments explicitly describe Salop-style circular competition as localized competition with immediate neighbors, while other papers impose parameter regions in which consumers purchase from one of the two firms between which they are located. This supports economic recognizability, but it does not remove the need to defend the restriction for standards/interoperability applications.

Relevant examples:
- localized competition discussion: `https://www.monash.edu/__data/assets/pdf_file/0003/925527/competition_and_access_regulation_in_the_telecommunications-industry_with_multiple_networks.pdf`;
- explicit two-bounding-firm parameter-region formulation: `https://www.degruyter.com/document/doi/10.1515/bejeap-2015-0064/html`;
- general circular-market choice discussion: `https://doi.org/10.1007/s10058-022-00290-x`.

### C. Change transport-cost curvature

Status: **REJECTED AT THIS REPAIR STEP**.

Quadratic or other curvature can improve equilibrium-existence properties, but it changes demand, price equations, location incentives, welfare, and likely the headline mechanism. It is a larger theory change than necessary before localized competition is tested.

### D. Restrict firm location strategy sets/minimum separation

Status: **REJECTED**.

This would remove the hostile histories by assumption and is not economically acceptable without an independent institutional constraint.

## 4. Independent counterexample reconstruction

Canonical hostile history:

- regime: IS;
- `s_I=0.25`;
- `x=(0.4,0.5,5/6)`;
- old interior candidate `p=(0.25,0.215,0.285)`.

Old candidate shares:

`q=(1/3,43/150,19/50)`.

Firm 2 old operating profit:

`0.215*(43/150)=0.061633333...`.

All-product deviation to `p_2'=0.174`:

`q_2'=81/125=0.648`,

`pi_2'=0.174*(81/125)=0.112752`.

Therefore the old candidate is not a Nash equilibrium under all-product choice.

Under explicit localized competition, the same deviation gives arc-clipped demand

`q_2'=0.340666666...`

and

`pi_2'=0.174*0.340666666...=0.059276`,

which is below `0.061633333...`.

Thus the exact hostile deviation is neutralized by the localized primitive. This is only a regression test, not a global equilibrium proof.

## 5. Required active-set solver

The next computation must not reuse `profits_general`.

For every fixed `(x, regime, s, v)` and price vector:

1. sort locations and construct the three arcs;
2. for each arc compute the unconstrained indifferent point;
3. classify the arc as left-endpoint capture / interior split / right-endpoint capture;
4. solve the network-share fixed point conditional on that active-set pattern;
5. verify the inequalities defining the active set;
6. compute exact/validated demand and profit;
7. globally maximize each firm's price over all active-set regions;
8. report `SOLVED_EQUILIBRIUM`, `MULTIPLE_EQUILIBRIA`, `SOLVED_NO_EQUILIBRIUM`, `UNRESOLVED`, or `NUMERICAL_FAILURE`;
9. never discard a failed region as an unprofitable deviation.

With three arcs there are at most `3^3=27` arc-status patterns before tie/coincident-location refinements, so exact active-set enumeration is feasible.

## 6. Off-path continuation completeness status

- all-product weighted-geodesic continuation: **UNRESOLVED**;
- explicit localized competition at the single hostile history: **counterexample defeated, but global continuation not yet certified**;
- coincident locations: **UNRESOLVED**;
- order changes: **defined conceptually, solver not yet certified**;
- boundary market shares: **must be included by active-set enumeration**;
- pure-price multiplicity/nonexistence: **must be reported, not filtered**.

Continuation verdict under the v1.2 checklist: **UNRESOLVED**.

## 7. Consequences for the headline result

No old welfare or coalition-stability number is promoted back to theorem status at this stage.

The old branch calculations remain diagnostics only:

- `Delta_M^(B-T)≈-0.010167`;
- `Delta_M^(FULL)≈+0.001571`;
- 9/9 local sign exercise conditional on the old branch.

If the localized active-set solver validates the old on-path regular branch and all relevant location deviations, the headline reversal may survive with little numerical change. If it changes the location equilibrium or policy continuation, all welfare and stability objects must be recomputed.

## 8. Novelty/institutional implication

Selecting localized competition changes the interpretation of the demand primitive. Therefore, if it survives mathematical repair, Stage 6 novelty re-kill and Stage 7 institutional validation must explicitly assess whether a two-bounding-product consideration set is defensible for standards/interoperability competition.

The paper must not describe the model as unrestricted all-product Salop choice.

## 9. Canonical Stage 4 verdict

**CONDITIONAL GO**.

Exactly one blocker is authorized:

> Complete the explicit localized-competition active-set price-continuation solver and certify all off-path continuations needed for unilateral location deviations, including boundary and coincident-location cases.

No other primitive may be changed during this repair.

## 10. Routing

Route to **Stage 5RR — Localized-Competition Continuation Hardening** under workflow v1.2.

Stage 5RR may change only the consumer consideration-set specification from implicit/unrestricted ambiguity to the explicit two-bounding-product localized competition primitive and implement the associated complete active-set continuation solver.

If Stage 5RR cannot certify the continuation without an additional substantive change, return `NO-GO` for this architecture rather than stacking further assumptions.
