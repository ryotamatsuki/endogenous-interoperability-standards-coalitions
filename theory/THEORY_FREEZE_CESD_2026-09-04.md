# Canonical Theory Freeze — C-ESD

Freeze date: 2026-09-04
Workflow: `ryotamatsuki/research-paper-workflow` v1.1
Workflow SHA: `488e5ab06c207909296a7564eaf9066f7f94319c`
Stage-7.5 authority: `reviews/STAGE_075_FREEZE_DECISION_CESD_2026-09-04.md`
Freeze ID: `CESD-THEORY-FREEZE-2026-09-04-v1`
Status: **THEORY FROZEN**

## 1. Working title

**Standards Coalitions, Endogenous Standard Depth, and Strategic Product Repositioning**

## 2. Approved research question

Can firms' endogenous product repositioning overturn the international standards-coalition outcome selected when governments choose the depth of interoperability?

## 3. Approved contribution statement

Only the following main contribution is authorized:

> **Interaction-induced coalition-stability reversal.** Endogenous government standard depth and endogenous firm product positioning each separately leave international standardization stable, but together can induce regional-standardization-union members to re-differentiate sufficiently to reverse their national-welfare ranking and make regional standards unions stable while international standardization becomes pair-blockable.

Canonical sign pattern:

`Delta_M^(B-T)<0`,

`Delta_M^(B-X)<0`,

`Delta_M^(FULL)>0`

on a verified regular nonempty region.

This is a result-level interaction claim. It is not a setup-novelty claim and it is not a global parameter-space theorem.

## 4. Players and objectives

There are three symmetric countries and three domestic firms, one firm per country.

Consumers have unit mass and are uniformly distributed on a unit Salop circle. Country of origin is independent of product taste; each country owns one third of the consumer population.

Formal standards regimes are

`rho in {IS, SU_12, SU_13, SU_23, SW}`.

Each formal standards bloc `C in rho` chooses one depth `s_C` and maximizes

`Omega_C = sum_{i in C} W_i`.

Firm `i` chooses product location `x_i` and then price `p_i` to maximize net profit

`Pi_i = p_i q_i - C_i^D`.

National welfare is

`W_i = CS/3 + Pi_i`.

Foreign firm profits are excluded from country `i`'s welfare.

## 5. Timing and information

The frozen sequential game is

`rho -> bloc depths s_C -> pairwise Tau(rho,s) -> product locations x_i -> prices p_i -> national welfare -> strict-blocking coalition stability`.

All players observe previous-stage choices. Standards blocs choose depth simultaneously conditional on the formal partition. Firms choose locations after observing the policy-induced pairwise friction matrix. Price competition follows location choice.

No stage may be reordered in the baseline paper.

## 6. Policy map

Primitive baseline standard friction is `t_bar>0`. Each depth satisfies

`0 <= s_C <= s_bar < t_bar`.

Pairwise standard-induced friction is

- same bloc `C`: `tau_ij = t_bar - s_C`;
- different blocs `C,D`: `tau_ij = t_bar + (s_C+s_D)/2`.

For `SU_12`:

`tau_12=t_bar-s_12`,

`tau_13=tau_23=t_bar+(s_12+s_3)/2`.

The coefficient `1/2` is a symmetric mean-preserving normalization, not an empirical claim or novelty claim. The essential restriction is the SU within-bloc/cross-bloc asymmetry: deeper bloc integration lowers internal standard friction and raises relative bloc-boundary separation.

No direct policy cost is present.

## 7. Product-market utility and network structure

Firm anchors are

`h=(1/6,1/2,5/6)`.

Firm `i` chooses `x_i` on the unit circle and pays baseline redesign/repositioning cost

`C_i^D = gamma d_c(x_i,h_i)^2/2`,

with `gamma>0` and circular distance `d_c`.

On the arc between adjacent products `i,j`, a consumer at distance `y` from `i` obtains

`u_i = A - p_i - tau_ij y + v n_i`,

and from `j`

`u_j = A - p_j - tau_ij(ell_ij-y) + v n_j`.

`A` is sufficiently large for full coverage.

Network size is

`n = G_rho q`,

with

- `G_IS = 11'`;
- under `SU_12`, `G_SU=[[1,1,0],[1,1,0],[0,0,1]]`;
- `G_SW=I`.

The network coefficient `v>0` is fixed conditional on the formal compatibility graph and does not itself depend on policy depth.

The indifferent consumer on arc `ij` is

`y_ij = ell_ij/2 + [p_j-p_i+v(n_i-n_j)]/(2 tau_ij)`.

## 8. Exact demand and price block

Let `L(Tau)` be the weighted graph Laplacian with edge weights `w_ij=1/tau_ij` and let `b(x)` denote the zero-price/no-network Voronoi share vector.

Demand is exactly

`q = b - (1/2)L p + (v/2)L G_rho q`.

Define

`A_rho = I - (v/2)L G_rho`,

`D = -(1/2) A_rho^{-1} L`.

Then

`q = A_rho^{-1}b + Dp`.

With zero marginal production cost, the price FOC is

`q_i + D_ii p_i = 0`.

On the regular domain where `D_ii<0`, define

`M=diag(-1/D_ii)`.

Then

`p=Mq`,

`q=K b`,

`K=(I-DM)^{-1}A_rho^{-1}`.

This price Nash equilibrium is unique on the regular domain specified below.

## 9. Location block

For cyclic order `1 -> 2 -> 3 -> 1`,

`b(x)=b0+Bx`,

`b0=(1/2,0,1/2)'`,

`B=[[0,1/2,-1/2],[-1/2,0,1/2],[1/2,-1/2,0]]`.

Because `q=Kb`, write

`q=c+Rx`, `c=Kb0`, `R=KB`.

Operating profit is

`pi_i^o=M_ii q_i^2`.

Net profit is

`Pi_i=M_ii(c_i+R_i x)^2-gamma(x_i-h_i)^2/2`.

Conditional location FOC:

`2M_ii R_ii(c_i+R_i x)-gamma(x_i-h_i)=0`.

Conditional own-location SOC:

`2M_ii R_ii^2-gamma<0`.

A conditional cyclic-order solution is not sufficient for equilibrium. Every canonical FULL witness must also pass a whole-circle unilateral location-deviation check that permits a change in cyclic order.

## 10. Equilibrium concept

The paper uses subgame-perfect Nash equilibrium of the sequential policy-location-price game, with:

1. unique interior price Nash equilibrium on the regular domain;
2. location Nash equilibrium requiring both the conditional FOC/SOC solution and no profitable whole-circle unilateral location deviation;
3. Nash equilibrium among standards blocs at the depth stage;
4. strict-blocking exclusive-membership stability across `IS/SU/SW` regimes.

For a symmetric SU, let `W_I` denote common IS welfare, `W_M` SU-member welfare, `W_O` SU-outsider welfare and `W_W` common SW welfare.

- IS is blocked by an SU-forming pair when `W_M>W_I`.
- A symmetric SU is blocked by IS only when all three countries strictly gain.
- A member can break SU to SW only when `W_W>W_M`.
- SW is blocked by IS if `W_I>W_W` for all countries or by an SU-forming pair when `W_M>W_W`.

## 11. Parameter and regularity restrictions

Primitive restrictions:

- `t_bar>0`;
- `v>0`;
- `gamma>0`;
- `0<=s_C<=s_bar<t_bar`;
- `A` sufficiently large for full coverage.

Regular continuation restrictions:

- every `tau_ij>0`;
- `A_rho` nonsingular;
- `I-DM` nonsingular;
- `D_ii<0` for every firm;
- equilibrium quantities and prices strictly positive;
- every indifferent consumer lies strictly inside the corresponding arc;
- location SOCs hold on the selected cyclic-order branch;
- no firm has a profitable unilateral location deviation anywhere on the circle.

For the symmetric SW closed form, positive price requires `2t-3v>0`.

Canonical witness:

`t_bar=1`, `v=0.04`, `gamma=0.11`, `s_bar=0.25`.

## 12. Mandatory nested benchmarks

### B-T — endogenous standard depth, fixed product locations

Depth choices are endogenous; product positions are fixed at inherited anchors.

At the canonical witness:

`S_B-T={IS}`,

`Delta_M^(B-T)=-0.010167`.

### B-X — zero policy depth, endogenous product locations

All `s_C=0`; product locations are endogenous.

At the canonical witness:

`S_B-X={IS}`,

`Delta_M^(B-X)=-0.000434`.

### FULL

Both depth and product positions are endogenous.

At the canonical witness:

- IS: `s_I=s_bar`;
- `SU_12`: `(s_12,s_3)=(s_bar,0)`;
- SW: `(s_1,s_2,s_3)=(0,0,0)`;
- `x^SU=(0.084567,0.582100,0.833333)`;
- `Delta_M^(FULL)=+0.001571`;
- `S_FULL={SU_12,SU_13,SU_23}`.

The interaction result is defined relative to both B-T and B-X. Neither benchmark may be omitted from the main theoretical presentation.

## 13. Welfare block

Exact aggregate consumer surplus is obtained by integrating utility arc by arc. It satisfies

`CS = A + v q'G_rho q - sum_i p_i q_i - TC`,

where `TC` is total standard-induced transportation/adaptation cost.

National welfare is

`W_i=CS/3+Pi_i`.

For a prospective SU member,

`Delta_M = Delta Pi_M + Delta CS/3`.

Hence an SU member prefers SU to IS iff

`Delta Pi_M > -Delta CS/3`.

At the canonical witness:

- `Delta CS/3=-0.0325785`;
- `Delta Pi_M=+0.0341498`;
- `Delta_M=+0.0015713`.

The member gain is therefore a domestic-producer-rent effect that narrowly exceeds the member consumer loss.

World welfare is exactly

`GW=CS+sum_i Pi_i`

`  = A + v q'G_rho q - TC - sum_i C_i^D`.

Price payments cancel globally as transfers.

At the witness:

- `GW_IS=-0.0225000`;
- `GW_SU=-0.0586685`;
- `GW_SW=-0.0700000`.

Thus decentralized SU stability can be globally inefficient relative to IS.

At fixed canonical SU policy `(s_12,s_3)=(0.25,0)`:

- inherited member distance: `0.333333`;
- constrained social location distance: `0.431427`;
- private equilibrium member distance: `0.497533`.

Private firms over-re-differentiate relative to this constrained second-best social location benchmark.

## 14. Adjustment-cost interpretation

The quadratic cost is frozen as the baseline specification because it produces the verified closed-form conditional location system. It is not the conceptual source of the mechanism.

For interpretation only, Stage 7 established that a regular differentiable strictly convex repositioning cost `C(d)` with `C(0)=C'(0)=0` and finite local curvature inherits positive SU re-differentiation when the same SU marginal operating-profit force is present.

The reversal requires intermediate effective adjustment-cost curvature:

- too high: repositioning is too weak and `Delta_M<0`;
- intermediate: domestic rent gain can exceed the per-country CS loss and `Delta_M>0`;
- too low: global circle jumps may invalidate the selected local branch.

For `v=0.04, s_bar=0.25`, the audited upper welfare threshold is

`gamma_W=0.132983`,

while the global-BR transition is numerically around `gamma≈0.10`.

This is not a global closed-form parameter classification.

## 15. Empirical and institutional interpretation

The paper may use the following only as institutional analogues for the policy primitive:

- EU AFIR EV-charging interoperability rules;
- EU DMA Article 7 messaging interoperability;
- EU common-charger / USB-C rules.

These establish that governments can regulate a technical interoperability/interface margin. They do not establish the predicted strategic product re-differentiation response.

Authorized empirical predictions include:

1. within-bloc interface convergence accompanied by greater differentiation on non-interface product characteristics;
2. stronger repositioning under partial/regional interoperability than under symmetric industry-wide interoperability;
3. stronger responses for firms with lower but non-negligible redesign costs;
4. member producer-rent gains can coexist with consumer losses;
5. outsider welfare can fall;
6. regional interoperability can be politically stable while global welfare favors industry-wide interoperability.

## 16. Closest-paper distinction

The strongest synthesis attack combines Ruiz (2004) and Gandal–Shy (2001).

Ruiz already contains government standard-recognition policy followed by endogenous product characteristics and price competition. Gandal–Shy already contains three countries, standardization unions, network effects, national welfare and coalition incentives. Therefore neither timing nor partial standards-union stability is new.

The frozen distinction is result-level: neither paper contains the verified full feedback in which regime-specific endogenous standard depth induces endogenous horizontal product repositioning and that response reverses the national coalition ranking relative to both a policy-only and a location-only benchmark. Ruiz's endogenous-characteristics extension does not generate this coalition-stability reversal, while Gandal–Shy has no post-policy endogenous product-location margin.

The manuscript must present this as a narrow interaction contribution, not as a claim that its ingredients are new.

## 17. Explicitly excluded and claims not made

The frozen baseline does not contain and the manuscript may not silently add:

- relative-profit objectives;
- private interoperability investment;
- endogenous network intensity;
- direct policy costs;
- transfers or side payments;
- lobbying;
- dynamics;
- endogenous topology choice;
- additional countries;
- heterogeneous national consumer-surplus incidence;
- alternative spatial geometries;
- empirical estimation.

Permanently killed novelty claims include:

- government standards policy affects product characteristics;
- continuous government compatibility policy;
- Salop + network effects + compatibility;
- partial compatibility / SU stability itself;
- strategic response to interoperability in a broad sense;
- coalitional interoperability price/welfare effects.

The paper does not claim:

- a closed-form global classification of all parameter values;
- that every local location stationary point is a global Nash equilibrium;
- that SU always reduces global welfare;
- that firms always over-re-differentiate for all parameters;
- that observed firms have empirically re-differentiated after the cited EU interoperability policies;
- that B0 is algebraically nested by C-ESD.

## 18. Verification artifacts frozen by reference

Canonical mathematical and computational records:

- `model/STAGE4_MINIMAL_MODEL_CESD.md`;
- `verification/stage04_cesd_minimal.py`;
- `reviews/STAGE_06_NOVELTY_REKILL_CESD_2026-09-04.md`;
- `reviews/STAGE_07_WELFARE_GENERALITY_CESD_2026-09-04.md`;
- `verification/stage07_cesd_welfare_generality.py`;
- `reviews/STAGE_075_FREEZE_DECISION_CESD_2026-09-04.md`.

These records define the approved result and its limitations. Manuscript statements must remain consistent with them.

## 19. Approved robustness scope

Already approved for interpretation/support:

- B-T and B-X nested benchmarks;
- exact national and global welfare accounting;
- neighborhood parameter audits of the regular reversal region;
- whole-circle unilateral location-deviation checks;
- constrained social location comparison;
- local general-convex-adjustment-cost interpretation.

Not approved as silent baseline changes:

- any new strategic variable or player;
- any new government instrument;
- any alternative network specification;
- any heterogeneity extension;
- any alternative spatial model.

## 20. Theory change control

Any theoretical change after this freeze requires a new change record containing:

1. exact proposed change;
2. economic reason;
3. affected equations/assumptions;
4. affected propositions and welfare claims;
5. affected verification scripts/tests;
6. affected prior-art/novelty claims;
7. stages that must be re-run.

Minimum routing rules:

- notation-only clarification with no mathematical change: no earlier gate rerun, but record the edit;
- primitive/timing/objective/policy-map change: reopen Stage 3 or Stage 4 as appropriate, then rerun Stages 6–8;
- new proposition from the same unchanged model: rerun mathematical verification and Stage 6 if claimed as a contribution, then Stages 7–8 if welfare/generality changes;
- new welfare incidence or government objective: reopen Stage 4/7 and rerun Stage 7.5/8;
- new extension intended only for robustness: must be explicitly authorized after the baseline manuscript is reproducible and may not alter the frozen baseline.

No silent theory drift is permitted.

## 21. Stage-8 verdict

**THEORY FROZEN — GO TO REPRODUCIBILITY SETUP.**

Next stage: **Stage 9 — Repository / Reproducibility Setup**.
