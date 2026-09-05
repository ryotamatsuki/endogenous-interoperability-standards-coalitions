# Stage 4R4A — Affine-Demand Bertrand Minimal Model

Date: 2026-09-06
Canonical workflow: `ryotamatsuki/research-paper-workflow` v1.2
Parent architecture: Stage 3R4

## 1. Purpose

This subgate replaces the failed spatial consumer-allocation continuation with one globally defined differentiated-product demand system while preserving the project’s standards policy map, network partition, endogenous product repositioning, Bertrand pricing, and coalition logic.

No old Salop demand formula is reused.

## 2. Product characteristics and standards

There are three firms/countries. Product positions remain on the unit circle. Write inherited anchors

`h=(1/6,1/2,5/6)`

and represent firm `i`'s strategic displacement by

`y_i in [-1/2,1/2]`, `x_i=(h_i+y_i) mod 1`.

The repositioning cost remains

`gamma*y_i^2/2`.

The formal standards partitions and the depth-to-friction map are unchanged from `model/STAGE3R_CESD_POLICY_MAP.md`:

- IS: `tau_ij=t_bar-s_I`, all pairs in the common network;
- SU_12: `tau_12=t_bar-s_12`, `tau_13=tau_23=t_bar+(s_12+s_3)/2`, with `G_12=G_21=1` and the outsider separated;
- SW: singleton blocs with cross-bloc friction from the same frozen map and no cross-firm network links.

## 3. Smooth characteristic distance

To avoid the ordering/capture discontinuities that killed the spatial continuations, the characteristic-distance input to demand is the smooth chordal distance

`delta_ij(x)=1-cos(2*pi*(x_i-x_j)) in [0,2]`.

This is a product-characteristic distance, not consumer travel cost.

## 4. Representative-consumer utility

Let `q>=0` be the quantity vector. Gross utility is

`U(q)=a*1'q - (1/2) q' B(rho,s,x) q + (v/2) q' G_rho q`.

Normalize own curvature to one and define, for `i != j`,

`B_ii=1`,

`B_ij=beta/[1+tau_ij(rho,s)+delta_ij(x)]`.

The effective curvature matrix is

`K(rho,s,x)=B(rho,s,x)-v G_rho`.

Consumer demand solves

`max_{q>=0} U(q)-p'q`.

When all quantities are positive,

`q=H(a*1-p)`, where `H=K^{-1}`.

For zero-demand products, demand is the globally nonnegative quadratic-utility extension; no negative-demand branch is treated as economic demand.

## 5. Global regularity region

Because

`delta_ij in [0,2]`

and

`tau_ij in [t_bar-s_bar,t_bar+s_bar]`, define

`m_min = 1/(3+t_bar+s_bar)`,

`m_max = 1/(1+t_bar-s_bar)`.

Assume

`0 < v < beta*m_min`,

and define

`k_min=beta*m_min-v`,

`k_max=beta*m_max`.

The Stage 4R4A sufficient regularity region is

`2*k_max < 1`,

`k_min > k_max^2`.

These restrictions are chosen from global matrix bounds before any search for a welfare reversal.

### Positive definiteness

Every off-diagonal element of `K` lies in `[k_min,k_max]`, while every diagonal element equals one. Hence `2*k_max<1` gives strict row diagonal dominance with positive diagonal. Symmetry then implies `K` is positive definite uniformly over every admissible `(rho,s,x)`.

### Gross substitutes

For a 3x3 symmetric matrix with unit diagonal and off-diagonal entries `k_12,k_13,k_23`,

`(K^{-1})_ij = (k_ik*k_jk-k_ij)/det(K)` for distinct `i,j,k`.

The bound `k_min>k_max^2` therefore implies every off-diagonal element of `H=K^{-1}` is strictly negative. Its diagonal elements are positive. Thus

`dq_i/dp_i=-H_ii<0`,

`dq_i/dp_j=-H_ij>0` for `i != j`.

The products are gross substitutes over the full upstream strategy domain.

## 6. Bertrand continuation

There is one product per firm, marginal production cost normalized to zero, and `p_i>=0`.

On the positive-demand branch, firm `i`'s FOC is

`q_i-p_i H_ii=0`.

Let `D=diag(H_11,H_22,H_33)`. The unique stationary price vector is

`p*=(D+H)^(-1) H (a*1)`.

At this vector,

`q*=D p*`.

Under the regularity conditions above, `H` has positive diagonal and nonpositive off-diagonal entries, while its row sums are positive. Therefore `D+H` is positive definite with nonpositive off-diagonal entries and has a nonnegative inverse; `p*>0` and `q*>0` for `a>0`.

For the globally nonnegative affine-demand extension derived from quadratic utility, Farahat and Perakis (2010) establish existence and uniqueness of Bertrand equilibrium for differentiated substitute products and show that the equilibrium coincides with the affine-demand equilibrium that permits negative quantities. The maintained region above verifies the required substitute structure at every history. Hence the continuation outcome is classified

`SOLVED_EQUILIBRIUM`

for every admissible `(rho,s,x)` in this Stage 4R4A parameter region.

## 7. Repositioning stage

Operating profit after the unique price continuation is

`pi_i^B(y;rho,s)=p_i*(y;rho,s) q_i*(y;rho,s)`.

Total firm payoff is

`Pi_i(y;rho,s)=pi_i^B(y;rho,s)-gamma*y_i^2/2`.

The chordal map is smooth and the global regularity inequalities keep all relevant matrix inverses uniformly nonsingular. Therefore `pi_i^B` is `C^2` on the compact displacement cube. Define

`M=max_i sup_y |d^2 pi_i^B/d y_i^2| < infinity`.

For the nonempty parameter region `gamma>M`, every firm's payoff is strictly concave in its own displacement on the convex compact strategy interval. Standard concave-game existence therefore gives a pure repositioning Nash equilibrium for every `(rho,s)`.

The condition is a sufficient theoretical region, not a fitted numerical restriction. Stage 4R4B must determine whether policy/welfare conclusions survive in a quantitatively and institutionally meaningful part of this region.

## 8. Exact nondegeneracy witness

For the pre-registered transparent normalization

`t_bar=1`, `s_bar=1/4`, `beta=1/5`, `v=1/50`, `a=1`,

the global regularity inequalities hold exactly.

At `SU_12`, inherited anchors, and zero depth, the exact operating-profit derivative of member 1 with respect to its displacement is strictly negative. At full test depth `s_12=1/4, s_3=0`, the same derivative is also strictly negative and has a strictly larger absolute value. By mirror symmetry member 2 has the opposite derivative and the outsider's derivative is zero.

Thus the affine architecture does not mechanically pin all firms at the inherited anchors. Deeper SU integration locally strengthens members' incentive to move outward from one another in this witness.

Exact expressions and assertions are in `verification/stage04r4a_affine_bertrand_gate.py`.

This witness is used only to establish nondegeneracy and a full-model interaction exists; it is not a proof of any welfare ranking or coalition-stability result.

## 9. Nested-benchmark interpretation

- `B-T`: fixed `y=0`; no strategic repositioning response is possible.
- `B-X`: zero continuous standard depth; formal network architecture remains but the depth-induced redistribution of pairwise friction is absent.
- `FULL`: both depth and repositioning operate.

The exact SU derivative comparison shows an interaction that cannot be generated by `B-T`, and the change from the zero-depth derivative to the positive-depth derivative is absent from `B-X` by construction.

This is only a mechanism-level distinction. It does not yet establish a welfare or coalition-stability reversal.

## 10. Scope of this subgate

Stage 4R4A establishes:

1. a single pre-registered map from standards and product positions to quadratic demand curvature;
2. a nonempty global regularity region;
3. globally complete and unique Bertrand continuation;
4. a sufficient region for pure repositioning-equilibrium existence;
5. exact evidence that repositioning is nondegenerate under an SU history.

It does **not** yet authorize reuse of any historical welfare, policy-depth, reversal, or coalition-stability result from the failed spatial architecture.
