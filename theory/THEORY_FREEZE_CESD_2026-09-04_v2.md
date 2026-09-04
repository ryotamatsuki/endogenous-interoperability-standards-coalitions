# Canonical Theory Re-Freeze — C-ESD

Freeze date: 2026-09-04
Workflow: `ryotamatsuki/research-paper-workflow` v1.1
Workflow SHA: `488e5ab06c207909296a7564eaf9066f7f94319c`
Stage-4R authority: `reviews/STAGE_04R_CONTINUATION_POLICY_REPAIR_2026-09-04.md`
Stage-7R authority: `reviews/STAGE_07R_WELFARE_GENERALITY_REFRESH_CESD_2026-09-04.md`
Freeze ID: `CESD-THEORY-FREEZE-2026-09-04-v2`
Status: **THEORY RE-FROZEN**
Supersedes for submission purposes: `CESD-THEORY-FREEZE-2026-09-04-v1`.

## 1. Working title

**Standards Coalitions, Endogenous Standard Depth, and Strategic Product Repositioning**

## 2. Approved research question

Can firms' endogenous product repositioning overturn the international standards-coalition outcome selected when governments choose the depth of harmonization inside a standards coalition?

## 3. Approved contribution statement

Only the following main contribution is authorized:

> **Interaction-induced coalition-stability reversal.** Endogenous government harmonization depth and endogenous firm product positioning each separately leave international standardization stable, but together can induce members of a regional standards union to re-differentiate sufficiently to reverse their national-welfare ranking and make regional standards unions stable while international standardization becomes pair-blockable.

Canonical sign pattern:

`Delta_M^(B-T)<0`,

`Delta_M^(B-X)<0`,

`Delta_M^(FULL)>0`.

This is a result-level interaction claim. It is not a setup-novelty claim and not a global parameter-space theorem.

## 4. Players and objectives

There are three symmetric countries and three domestic firms, one firm per country. Consumers have unit mass and are uniformly distributed on a unit Salop circle. Country of residence is independent of product taste; each country contains one third of consumers.

Formal standards regimes are

`rho in {IS, SU_12, SU_13, SU_23, SW}`.

For each non-singleton standards bloc `C`, the coalition chooses an additional within-coalition harmonization depth `s_C` and maximizes

`Omega_C = sum_{i in C} W_i`.

Singleton blocs have no internal harmonization margin and therefore have the degenerate policy action `s_C=0`.

Firm `i` chooses product location `x_i` and then price `p_i` to maximize

`Pi_i = p_i q_i - C_i^D`.

National welfare is

`W_i = CS/3 + Pi_i`.

Foreign firm profits are excluded from country `i`'s welfare.

## 5. Timing and information

The sequential game is

`rho -> harmonization depths of non-singleton blocs -> Tau(rho,s) -> product locations x -> prices p -> national welfare -> coalition stability`.

All players observe previous-stage choices. Firms choose locations after observing the policy-induced pairwise friction matrix. Prices are chosen after locations.

No stage may be reordered in the baseline paper.

## 6. Repaired policy action set and friction map

Primitive baseline standard friction is `t_bar>0` and `0<=s_bar<t_bar`.

The feasible policy action is

- `s_C in [0,s_bar]` if `|C|>=2`;
- `s_C=0` if `|C|=1`.

Pairwise standard-induced friction is

- same bloc `C`: `tau_ij=t_bar-s_C`;
- different blocs `C,D`: `tau_ij=t_bar+(s_C+s_D)/2`.

Hence:

- IS: one grand coalition chooses `s_I in [0,s_bar]`;
- `SU_12`: coalition `{1,2}` chooses `s_12 in [0,s_bar]`, while outsider singleton has `s_3=0`;
- SW: all blocs are singletons, hence all depth variables equal zero.

For `SU_12`:

`tau_12=t_bar-s_12`,

`tau_13=tau_23=t_bar+s_12/2`.

Thus deeper SU harmonization lowers member-member standard friction while increasing bloc-boundary friction relative to the baseline. The coefficient `1/2` is a symmetric normalization, not an empirical claim or novelty claim.

Formal regime membership determines the binary compatibility/network graph. `s=0` means zero **additional harmonization depth conditional on the regime**, not zero compatibility.

No direct policy cost is present.

## 7. Product-market utility, network structure, and redesign cost

Firm anchors are

`h=(1/6,1/2,5/6)`.

Firm `i` chooses `x_i` on the unit circle and pays

`C_i^D = gamma d_c(x_i,h_i)^2/2`,

with `gamma>0` and circular distance `d_c`.

On an arc between adjacent products `i,j`, a consumer at distance `y` from `i` obtains

`u_i=A-p_i-tau_ij y+v n_i`,

and from `j`

`u_j=A-p_j-tau_ij(ell_ij-y)+v n_j`.

`A` is sufficiently large for full coverage.

Network size is

`n=G_rho q`,

with

- `G_IS=11'`;
- under `SU_12`, `G_SU=[[1,1,0],[1,1,0],[0,0,1]]`;
- `G_SW=I`.

The network coefficient `v>0` is fixed conditional on the formal compatibility graph and does not depend on depth.

## 8. Demand and price block

Let `L(Tau)` be the weighted graph Laplacian with edge weights `1/tau_ij` and `b(x)` the zero-price/no-network Voronoi share vector. Demand is exactly

`q=b-(1/2)Lp+(v/2)LG_rho q`.

Define

`A_rho=I-(v/2)LG_rho`,

`D=-(1/2)A_rho^{-1}L`.

Then

`q=A_rho^{-1}b+Dp`.

With zero marginal production cost, the price FOC is

`q_i+D_ii p_i=0`.

On the regular domain with `D_ii<0`, define `M=diag(-1/D_ii)`. Then

`p=Mq`,

`q=(I-DM)^{-1}A_rho^{-1}b`.

The interior price Nash equilibrium is unique on the stated regular domain.

## 9. Location block

For a fixed cyclic order, `b(x)=b0+Bx`, so `q=c+Rx`. Net profit is quadratic in own location on that branch and the conditional FOC is

`2M_ii R_ii(c_i+R_i x)-gamma(x_i-h_i)=0`.

The conditional own-location SOC is

`2M_ii R_ii^2-gamma<0`.

A conditional fixed-order solution is not sufficient for equilibrium. A valid continuation must pass a whole-circle unilateral location-deviation check permitting changes in cyclic order.

## 10. Equilibrium concept and repaired continuation requirement

The solution concept is subgame-perfect Nash equilibrium of the sequential policy-location-price game, followed by strict-blocking exclusive-membership coalition stability.

A valid policy payoff may be assigned only when the downstream location-price continuation is an actual Nash equilibrium. At the canonical witness, Stage 4R verifies the repaired continuation on the entire feasible IS and SU depth domains by:

1. continuous whole-circle unilateral location best-response searches;
2. joint global search over policy depth and unilateral deviation location;
3. enumeration of cyclic orders and circular-anchor branches on a dense feasible-depth grid;
4. global scalar policy optimization.

The historical v1 off-path failure arose only because singleton blocs were incorrectly given positive harmonization-depth instruments. That instrument is absent in v2.

## 11. Primitive and regularity restrictions

Primitive restrictions:

- `t_bar>0`;
- `v>0`;
- `gamma>0`;
- `0<=s_bar<t_bar`;
- `s_C in [0,s_bar]` only for non-singleton blocs;
- `s_C=0` for singleton blocs;
- `A` sufficiently large for full coverage.

Regular continuation restrictions:

- every `tau_ij>0`;
- `A_rho` nonsingular;
- `I-DM` nonsingular;
- `D_ii<0` for every firm;
- equilibrium quantities and prices strictly positive;
- every indifferent consumer lies inside the corresponding arc;
- conditional location SOCs hold on the selected branch;
- no firm has a profitable unilateral location deviation anywhere on the circle.

For symmetric SW, positive price requires `2t-3v>0`.

Canonical witness:

`t_bar=1`, `v=0.04`, `gamma=0.11`, `s_bar=0.25`.

## 12. Mandatory nested benchmarks

### B-T — endogenous harmonization depth, fixed product locations

Non-singleton coalition depths are endogenous; product positions are fixed at inherited anchors. Singleton depths are zero by definition.

At the canonical witness:

`S_B-T={IS}`,

`Delta_M^(B-T)≈-0.010167`.

### B-X — zero additional harmonization depth, endogenous product locations

All non-singleton depths are fixed at zero; product locations are endogenous. Formal compatibility/network graphs remain regime-specific.

At the canonical witness:

`S_B-X={IS}`,

`Delta_M^(B-X)≈-0.000434`.

### FULL

Both non-singleton coalition depth and product positions are endogenous.

At the canonical witness:

- IS: `s_I*=0.25`;
- `SU_12`: `s_12*=0.25`, outsider depth `0`;
- SW: all depths `0`;
- `x^SU≈(0.084567,0.582100,0.833333)`;
- `Delta_M^(FULL)≈+0.001571`;
- `S_FULL={SU_12,SU_13,SU_23}`.

Neither B-T nor B-X may be omitted from the main theoretical presentation.

## 13. Welfare block

Exact aggregate consumer surplus satisfies

`CS=A+v q'G_rho q-sum_i p_i q_i-TC`.

National welfare is

`W_i=CS/3+Pi_i`.

For a prospective SU member,

`Delta_M=Delta Pi_M+Delta CS/3`.

Hence SU is preferred to IS iff

`Delta Pi_M>-Delta CS/3`.

At the canonical witness:

- `Delta CS/3≈-0.0325785`;
- `Delta Pi_M≈+0.0341498`;
- `Delta_M≈+0.0015713`.

The member gain is a domestic-producer-rent effect that narrowly exceeds the member consumer loss.

World welfare is exactly

`GW=A+v q'G_rho q-TC-sum_i C_i^D`.

Price payments cancel globally as transfers.

Reported witness welfare levels are **net of the common baseline utility `A`**:

- `GW_IS≈-0.0225000`;
- `GW_SU≈-0.0586685`;
- `GW_SW≈-0.0700000`.

Thus `GW_IS>GW_SU>GW_SW` at the witness.

At fixed canonical SU policy:

- inherited member distance `1/3`;
- constrained social distance `≈0.431427`;
- private equilibrium distance `≈0.497533`.

This is a constrained second-best location comparison, not a global first-best theorem.

## 14. Adjustment-cost interpretation

The quadratic redesign cost is the frozen baseline specification. For interpretation only, Stage 7/7R establish that the re-differentiation mechanism does not conceptually require quadratic cost: a regular differentiable strictly convex adjustment cost with `C(0)=C'(0)=0` and finite local curvature can preserve the same positive SU repositioning force.

The canonical upper welfare threshold remains

`gamma_W≈0.132983`

at `v=0.04`, `s_bar=0.25`.

No structural closed-form lower `gamma_GBR` threshold is frozen in v2. Regularity at the canonical witness is established directly by the Stage-4R continuation audit.

## 15. Empirical and institutional interpretation

The paper may use EU EV-charging interoperability, DMA messaging interoperability, and common-charger/USB-C rules only as institutional analogues showing that policy can regulate technical interoperability margins.

They do not establish the model's exact cross-bloc derivative or observed strategic product re-differentiation.

Authorized predictions include within-bloc interface convergence with greater differentiation on other characteristics, stronger repositioning under partial interoperability, adjustment-cost heterogeneity, producer-rent/consumer divergence, outsider loss, and possible national/global welfare conflict.

## 16. Closest-paper distinction

The strongest synthesis attack combines Ruiz (2004) and Gandal–Shy (2001), with Klimenko (2009) also close on continuous compatibility policy and international coordination.

The contribution is not government standards policy, endogenous product characteristics, network effects, continuous compatibility, or SU stability separately. The authorized distinction is the verified interaction result: regime-specific harmonization depth induces endogenous horizontal product repositioning, and that strategic response reverses coalition ranking relative to both a policy-only and a location-only benchmark.

## 17. Proof-status boundary

The weighted demand system, regular price equilibrium, fixed-order location characterization, national-welfare identity, and world-welfare identity are analytic results on their stated domains.

The FULL-only coalition-stability reversal remains a **CONDITIONAL constructive regular-domain result**. At the canonical witness the entire repaired feasible policy domain has been computationally audited for valid downstream continuations, but no closed-form global theorem over all primitive parameter values is claimed.

The witness world-welfare ranking and private/social distance comparison remain numerical witness results.

## 18. Explicit exclusions and claims not made

The baseline does not contain relative-profit objectives, private interoperability investment, endogenous network intensity, direct policy costs, transfers, lobbying, dynamics, endogenous topology choice, more countries, heterogeneous national CS incidence, alternative spatial geometries, or empirical estimation.

The paper does not claim that every local location stationary point is a Nash equilibrium, that SU always lowers global welfare, that firms always over-re-differentiate, that the cited EU cases empirically exhibit the predicted repositioning, that the `1/2` coefficient is structural, or that B0 is algebraically nested.

## 19. Canonical verification artifacts

Submission-authoritative theory is tied to:

- `model/STAGE4_MINIMAL_MODEL_CESD.md`;
- `reviews/STAGE_04R_CONTINUATION_POLICY_REPAIR_2026-09-04.md`;
- `model/STAGE4R_CESD_CONTINUATION_POLICY_REPAIR.md`;
- `verification/stage04r_cesd_continuation_repair.py`;
- `reviews/STAGE_06_NOVELTY_REKILL_CESD_2026-09-04.md`;
- `reviews/STAGE_07R_WELFARE_GENERALITY_REFRESH_CESD_2026-09-04.md`;
- `verification/stage07r_cesd_welfare_refresh.py`;
- `literature/STAGE7R_CESD_INSTITUTIONAL_REFRESH.md`.

The historical v1 freeze and historical Stage-4/7 files remain provenance records but do not override v2 where they conflict on the policy action set.

## 20. Approved robustness scope

Approved support includes B-T and B-X, exact welfare accounting, repaired whole-circle continuation auditing across feasible policy depths at the canonical witness, local parameter sensitivity already recorded historically, constrained social-location comparison, and local regular-convex-cost interpretation.

No additional robustness or new strategic mechanism may be added during Stage 9R/10R without theory-change control.

## 21. Theory change control

Any post-freeze theoretical change must record what changed, why, affected equations/propositions, affected verification, affected literature claims, and stages to rerun. Any change to the repaired action set, friction map, network graph, timing, welfare objective, coalition-stability rule, or strategic margins requires reopening the relevant earlier stages.

No silent theory drift is permitted.

## 22. Freeze verdict

**THEORY FROZEN — GO TO REPRODUCIBILITY REFRESH (STAGE 9R).**
