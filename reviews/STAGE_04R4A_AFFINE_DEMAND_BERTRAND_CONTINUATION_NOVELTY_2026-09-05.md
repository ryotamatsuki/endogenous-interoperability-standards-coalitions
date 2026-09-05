# Stage 4R4A — Affine-Demand Bertrand Continuation & Novelty Gate

Date: 2026-09-05
Canonical workflow: `ryotamatsuki/research-paper-workflow` v1.2
Prior stage: Stage 3R4 — `GO — GO TO MINIMAL MODEL`
Target journal if rebuilt theory survives: *International Journal of Industrial Organization*

## 1. Executive verdict

**GO — THE AFFINE-DEMAND BERTRAND RE-FOUNDATION PASSES THE MINIMAL CONTINUATION / REPOSITIONING / NOVELTY GATE.**

This is the first post-reopen architecture that clears the continuation gate without restricting the location strategy set around the observed equilibrium or changing the equilibrium concept. It replaces discrete Salop market allocation with a representative-consumer quadratic utility, but retains:

- Bertrand price competition;
- the old standards-depth map `Tau(reg,s)`;
- the old standards/network matrix `G(reg)`;
- endogenous product repositioning on the circle;
- repositioning costs around inherited anchors;
- national welfare and coalition-formation logic as downstream objects.

The continuation architecture itself is not novel and must not be sold as a contribution. Its value is that it is globally well-defined and conventional enough to support the actual contribution test.

The minimal solved result is substantive: at the pre-registered witness, a bilateral standards union is worse for a member than integrated standards when positions are fixed, but the member ranking reverses once firms can strategically reposition. The bilateral members move away from one another in characteristic space, while the outsider remains essentially at its inherited anchor. The reversal survives all 9 points in a small ex-ante `(v,gamma)` box.

This result survives the Stage 4 novelty kill only narrowly. Closest prior art contains each component separately or in pairs, but the searched papers do not contain the same full loop: endogenous standards-coalition architecture -> costly product repositioning -> endogenous substitutability network -> Bertrand continuation -> coalition-member welfare reversal/stability implications.

Stage 5 is therefore authorized. No manuscript rehabilitation or submission authorization follows yet.

## 2. Frozen minimal architecture

### 2.1 Representative consumer

For fixed standards regime `rho`, standards depth `s`, and product positions `x`, quantities solve

`max_{q >= 0}  a 1' q - (1/2) q' K(rho,s,x) q - p' q`.

The Stage 4R4A witness fixes

- `a = 2`;
- diagonal curvature `b = 10`;
- baseline pair substitution `c0 = 0.30`;
- spatial-substitution loading `lambda = 0.50`;
- network strength `v = 0.08`;
- repositioning cost `gamma = 0.03`;
- `tbar = 1`;
- `sbar = 0.25`;
- inherited anchors `h=(1/6,1/2,5/6)`.

The circular proximity kernel is

`phi_ij(x) = [1 + cos(2 pi (x_i-x_j))]/2 in [0,1]`.

For every pair `i != j`, the effective inverse-demand cross-curvature is

`K_ij = c0 + lambda * phi_ij(x) / Tau_ij(rho,s) - v G_ij(rho)`,

and `K_ii=b`.

This keeps the old policy objects intact:

- lower `Tau_ij` increases competitive substitutability;
- `G_ij=1` gives the pair a network-compatibility benefit that partially offsets competitive substitutability;
- repositioning changes `phi_ij`, hence the product-substitution network faced by the later Bertrand game.

The old discrete consumer arc partition is the only major architecture object removed.

### 2.2 Standards maps retained from the old model

`G(IS)=11'`, `G(SU_12)` has the `1-2` block compatible and country 3 singleton, and `G(SW)=I`.

The old `Tau` map is also retained:

- under `IS`, all pair frictions are `tbar-s_I`;
- under `SU_12`, the member pair has `tbar-s_12` and the two cross-bloc frictions rise with the two bloc depths;
- under `SW`, bilateral frictions rise with the relevant singleton depths.

Thus Stage 4R4A does not re-optimize the standards map around the desired reversal.

## 3. Gate A — global demand well-posedness

### 3.1 Primitive bounds

On the admissible Stage 4 strategy box,

`Tau_ij in [3/4,5/4]`, `phi_ij in [0,1]`, and `G_ij in {0,1}`.

Hence every off-diagonal element satisfies

`c_min = c0-v = 0.22`,

`c_max = c0 + lambda/(tbar-sbar) = 0.966666...`.

The pre-registered diagonal `b=10` satisfies all three global inequalities

`b > 2 c_max`,

`b c_min > c_max^2`,

`b - 2 c_max + c_min > 0`.

These inequalities are not fitted to an equilibrium location. They hold uniformly over the entire circle and policy box.

### 3.2 Consequences

For any feasible history:

1. `K` is symmetric strictly diagonally dominant with positive diagonal, hence positive definite.
2. The consumer problem has a unique solution for every nonnegative price vector.
3. Writing `D=K^{-1}`, the 3x3 cofactor formula gives, for example,

   `D_12 proportional to c_13 c_23 - b c_12 < c_max^2 - b c_min < 0`,

   and symmetrically for the other cross terms.

   Therefore direct interior demand has negative own-price and positive cross-price responses.
4. The row sums of `D` are positive. For row 1 the numerator factors as

   `(b-c_23)(b-c_12-c_13+c_23)`,

   whose second factor is bounded below by `b-2c_max+c_min > 0`.

The executable verifier additionally checks the matrix properties at policy endpoints, coincident-product histories, the former hostile Salop location, and deterministic pseudo-random histories.

**Gate A verdict: PASS.**

## 4. Gate B — global Bertrand continuation

### 4.1 Interior closed form

At an interior demand point,

`q = D(a1-p)`.

With one product per firm and zero marginal cost, firm `i` has FOC

`q_i - D_ii p_i = 0`.

Therefore the simultaneous stationary price vector is

`p* = [D + diag(D)]^{-1} D (a1)`.

The global primitive bounds above imply positive zero-price demand; the executable gate verifies strictly positive `p*` and `q*` across the adversarial history set.

### 4.2 Nonnegative demand and off-path price deviations

Negative affine quantities are not permitted. Demand for every `p>=0` is defined by the KKT system of the representative-consumer quadratic program. The verifier solves all `2^3` quantity active sets directly and treats failure to find a valid KKT set as an error.

For representative difficult histories, including the former hostile location and coincident products, each firm's `p*` is checked against a direct global one-price deviation search using the KKT demand evaluator. No old Salop continuation formula is reused.

### 4.3 Literature theorem used

Farahat and Perakis (2010), *Operations Research Letters* 38(4), derive a globally nonnegative extension of affine substitute demand from quadratic representative-consumer utility and prove existence and uniqueness of Bertrand equilibrium; their equilibrium coincides with the affine closed-form equilibrium. This is the relevant continuation architecture, not a new theorem claimed by this paper.

The Stage 4R4A primitive is deliberately restricted to the single-product-per-firm substitute case and independently checks the sign structure and global deviations used here.

**Gate B verdict: PASS for the frozen Stage 4R4A primitive domain.**

## 5. Gate C — endogenous repositioning

The location-stage payoff is

`pi_i = p_i^*(rho,s,x) q_i^*(rho,s,x) - gamma d_c(x_i,h_i)^2/2`.

Each unilateral location best response is searched over the full circle; failed price continuation is impossible under Gates A-B and is not filtered.

At the canonical policy histories:

- `IS, s_I=sbar`: the symmetric anchor profile remains the location equilibrium;
- `SW, s=0`: the symmetric anchor profile remains the location equilibrium;
- `SU_12, s_12=sbar, s_3=0`: firms 1 and 2 move outward from their inherited anchors while firm 3 stays at its anchor.

The canonical SU profile is approximately

`x_SU = (0.1404, 0.5263, 0.8333)`,

versus

`h = (0.1667,0.5000,0.8333)`.

Thus repositioning is neither pinned at anchors nor driven to maximal differentiation. It responds specifically to the bilateral standards architecture.

The verifier performs whole-circle unilateral best-response audits at the computed profiles.

**Gate C verdict: PASS.**

## 6. Gate D — result-level novelty kill

### 6.1 The minimal new result

Define member-1 national welfare as

`W_1 = CS/3 + pi_1`.

At fixed anchors,

`Delta_fixed = W_1(SU_12) - W_1(IS) < 0`.

At endogenous location equilibria,

`Delta_full = W_1(SU_12) - W_1(IS) > 0`.

At the canonical witness the margins are of order

- fixed positions: about `-2.1e-4`;
- endogenous repositioning: about `+2.7e-4`.

The outsider is worse off under the bilateral standard in the endogenous equilibrium.

This is exactly the type of result required by Stage 3R4: remove repositioning and the sign reversal disappears; remove the standards architecture and there is no bilateral-versus-integrated comparison generating the repositioning incentive.

The local `(v,gamma)` box

`v in {0.07,0.08,0.09}`,

`gamma in {0.025,0.030,0.035}`

passes the strict fixed-negative/full-positive reversal at all 9 points.

### 6.2 Closest-paper reconstruction

#### Ushchev and Zenou (2018)

They develop price competition on an exogenous product-variety network and obtain a unique Bertrand equilibrium with prices determined by network structure. This directly absorbs any claim that "product substitutability network affects Bertrand prices" is novel.

What is absent from their model is the present upstream game in which a standards architecture changes pairwise compatibility and firms then incur costs to reposition products, thereby endogenizing the substitutability network before price competition. The Stage 4R4A reversal is not available in an exogenous product network.

#### Economides and Skrzypacz (2003 working paper)

They study standards-coalition formation in network industries. Joining a standards coalition gives network benefits but increases product-market competition, and equilibrium coalition size depends on network effects. This is a direct threat to any generic coalition-stability contribution.

Their searched model does not add a costly post-coalition product-repositioning stage that endogenously changes the later product-substitution structure. Accordingly, the present contribution cannot be "coalitions trade off compatibility and competition"; it must be the endogenous strategic adaptation of product differentiation and its effect on coalition rankings.

#### Baake and Boom (2001)

They combine network externalities, compatibility decisions, endogenous product quality/differentiation, and later price competition. This is the strongest component-overlap threat. Their timing has firms choose inherent qualities, then decide whether to provide compatibility, then compete in prices.

The present loop reverses that ordering for the key strategic object: standards-coalition architecture is set first, after which firms reposition products in response to it. The result is therefore a policy/coalition-induced strategic differentiation response rather than differentiation determining the later compatibility decision.

#### Barrett and Yang (2001)

They connect international standards, redesign costs, network effects, and multi-attribute competition and show rational noncompliance with an international standard. This absorbs broad claims about international standards plus redesign/network frictions.

Their redesign decision concerns compliance/adoption relative to an international standard. The Stage 4R4A mechanism instead has firms remain within a chosen standards architecture and strategically reposition a separate product characteristic, changing the intensity of subsequent Bertrand substitution and potentially reversing member welfare rankings.

#### Earlier compatible differentiated-products work

The older literature also studies compatibility with endogenous differentiation/quality, including quantity-competition variants. Hence neither "compatibility changes differentiation" nor "differentiation with network externalities" can be claimed as new in isolation.

### 6.3 Novelty verdict

The closest literature does **not**, on the evidence found in this gate, reconstruct the complete result-level loop:

`standards coalition / architecture -> costly post-standard repositioning -> endogenous substitutability network -> Bertrand equilibrium -> reversal of member regime ranking -> coalition-stability implications`.

The distance is real but narrow. The paper remains vulnerable if the downstream coalition result is weak or if a closer paper with this timing/result is found.

**Gate D verdict: PASS — DISTINCT BUT NARROW.**

## 7. What Stage 4R4A does not authorize

This gate does not restore any old theorem or production manuscript result. In particular it does not authorize use of:

- the old Salop price equations;
- old location equilibria;
- old `Delta_M^(B-T)` or `Delta_M^(FULL)` values;
- old world-welfare ordering;
- old policy-depth optimum;
- old coalition-stability thresholds;
- old Stage 8 freeze or downstream stages.

All such objects are stale and must be recomputed under the affine-demand architecture.

## 8. Canonical Stage 4R4A verdict

**GO — GO TO FULL POLICY / COALITION REBUILD.**

The re-founded minimal model has:

- globally well-posed consumer demand;
- a conventional globally nonnegative affine-demand Bertrand continuation;
- nondegenerate endogenous repositioning;
- a strict and locally robust fixed-position/endogenous-position member-welfare reversal;
- a surviving but narrow result-level novelty claim.

Default termination is therefore not triggered at Stage 4R4A.

## 9. Next-stage contract

Next formal stage:

**Stage 5R4 — Endogenous Standards-Depth, Welfare & Coalition Reconstruction.**

Stage 5R4 must, using only the new affine-demand architecture:

1. solve standards-depth choices globally for `IS`, each `SU_ij`, and `SW`;
2. solve the nested location game after every material standards-depth deviation;
3. compute national and world welfare from the representative-consumer surplus plus profits/repositioning costs;
4. rebuild strict-blocking coalition stability from scratch;
5. determine whether a nondegenerate reversal/stability threshold survives;
6. return `NO-GO / TERMINATE` if the coalition result collapses even though the continuation architecture is valid.

No parameter search may use the sign of an old Salop result as its objective.
