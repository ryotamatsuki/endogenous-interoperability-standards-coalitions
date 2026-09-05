# Project State

Last updated: 2026-09-06

## Canonical status

- Project: Endogenous Interoperability and Standards Coalitions
- Working title: **Standards Coalitions and Strategic Product Repositioning**
- Canonical workflow: `ryotamatsuki/research-paper-workflow` **v1.2**
- Workflow release SHA: `944e6bace951e13645b02200a63bf25363dc7242`
- Previous theory freeze: `CESD-THEORY-FREEZE-2026-09-04-v2` — **REOPENED / NON-AUTHORITATIVE**
- Theory status: **REOPENED — AFFINE-DEMAND BERTRAND RE-FOUNDATION SURVIVES CONTINUATION SUBGATE**
- Stage 5RR: **NO-GO — linear localized continuation terminated**
- Stage 4R3Q: **NO-GO — pure-quadratic localized continuation terminated**
- Stage 3R4: **GO — affine-demand Bertrand re-foundation selected**
- Stage 4R4A: **GO — continuation/demand/repositioning subgate passes; novelty survives narrowly**
- Stage 11R2: **STALE / REOPENED**
- Stage 12 journal positioning: **administratively complete, submission authorization suspended**
- Stage 13: **CLOSURE REVOKED**
- Stage 14 submission QA authorized: **NO**
- Primary intended target only if rebuilt theory survives: **International Journal of Industrial Organization (IJIO)**

## Terminated spatial architectures

The project has permanently terminated three pure-strategy spatial price-continuation implementations:

1. unrestricted all-product linear Salop;
2. explicit localized linear competition;
3. explicit localized pure-quadratic competition.

No additional transport-curvature or consideration-set patch is authorized.

## Current Stage 4R4A architecture

Consumers are no longer allocated to Salop arcs. The circle is retained as a smooth product-characteristic space.

For positions `x`, define

`delta_ij(x)=1-cos(2*pi*(x_i-x_j))`.

Retain the frozen standards-depth map `tau_ij(rho,s)` and formal compatibility network `G_rho` from `model/STAGE3R_CESD_POLICY_MAP.md`.

Representative-consumer utility is

`U(q)=a*1'q-(1/2)q'Bq+(v/2)q'G_rho q`, `q>=0`,

where

`B_ii=1`,

`B_ij=beta/[1+tau_ij+delta_ij]`, `i != j`,

and

`K=B-vG_rho`.

The globally nonnegative affine-demand object is used; negative quantities are never treated as economic demand.

## Global regularity result

Let

`m_min=1/(3+t_bar+s_bar)`,

`m_max=1/(1+t_bar-s_bar)`,

`k_min=beta*m_min-v`,

`k_max=beta*m_max`.

In the sufficient region

- `0<v<beta*m_min`;
- `2*k_max<1`;
- `k_min>k_max^2`,

`K` is uniformly positive definite for every admissible regime, policy-depth vector and location profile. `H=K^{-1}` has positive diagonal and strictly negative off-diagonal entries, so demand is globally gross-substitute.

For the transparent normalization

`t_bar=1`, `s_bar=1/4`, `beta=1/5`, `v=1/50`,

`m_min=4/17`, `m_max=4/7`, `k_min=23/850`, `k_max=4/35`, and the inequalities hold exactly.

## Bertrand continuation

For positive quantities,

`q=H(a*1-p)`, `H=K^{-1}`.

Let `D=diag(H_ii)`. The one-product-per-firm zero-cost Bertrand solution is

`p*=(D+H)^(-1)H(a*1)`,

with

`q*=Dp*`.

The maintained global substitute structure permits use of the Farahat–Perakis (2010) nonnegative affine-demand result: the Bertrand equilibrium exists and is unique and coincides with the affine-demand equilibrium.

Continuation status throughout the maintained region:

**`SOLVED_EQUILIBRIUM`**.

## Repositioning result

Write `y_i in [-1/2,1/2]`, `x_i=(h_i+y_i) mod 1`, with repositioning cost `gamma*y_i^2/2`.

Operating profit after the unique Bertrand continuation is smooth on the compact displacement cube. If

`M=max_i sup_y |d^2 pi_i^B/dy_i^2|`,

then `M<infinity`, and for `gamma>M` each firm payoff is strictly concave in its own displacement. Hence a pure repositioning Nash equilibrium exists for every standards history in this sufficient region.

Exact SU_12 anchor differentiation at the transparent normalization shows:

- member 1 has a strictly negative displacement gradient;
- member 2 has the symmetric positive gradient;
- the outsider gradient is zero;
- increasing `s_12` from zero to `1/4` makes the member outward gradient strictly stronger.

Thus repositioning is nondegenerate and standards depth changes the repositioning incentive.

Authorities:

- `model/STAGE4R4A_AFFINE_DEMAND_BERTRAND.md`
- `verification/stage04r4a_affine_bertrand_gate.py`
- `reviews/STAGE_04R4A_AFFINE_DEMAND_BERTRAND_CONTINUATION_NOVELTY_2026-09-06.md`
- `decisions/STAGE04R4A_CESD_DECISIONS.md`

## Novelty status

Broad claims are killed by prior art:

- Farahat–Perakis (2010): nonnegative affine demand / unique Bertrand;
- Ushchev–Zenou (2018): product-variety networks / Bertrand;
- Baake–Boom (2001): compatibility, network externalities, endogenous differentiation and price competition;
- Barrett–Yang (2001): international standards, redesign costs and network effects;
- Cheng–Huang (2025): compatibility interacting with quality competition and expanded differentiation;
- Rodrigues (2026): endogenous product design under linear demand with product characteristics shaping competitive interactions.

Therefore the only surviving contribution route is narrow:

`government standards-bloc depth -> post-policy costly horizontal repositioning -> changed Bertrand competition/welfare -> coalition stability`.

Current novelty classification: **DISTINCT BUT NARROW — NOT YET IJIO-SUFFICIENT**.

## Historical outputs remain invalid

All old spatial-model policy optima, locations, welfare decompositions, reversal values and coalition-stability results remain historical diagnostics only. They may not be transplanted into the affine model.

## Current verdict and routing

**STAGE 4R4A GO — CONTINUE WITHIN STAGE 4 — DO NOT SUBMIT.**

Stage 4R4A is a project-specific subgate, not completed canonical Stage 4.

Next formal project substage:

**Stage 4R4B — Affine-Demand Policy, Welfare, Reversal & Coalition Reconstruction.**

Stage 4R4B must solve the bloc-depth/repositioning continuation under the new demand system, derive consumer surplus and national welfare, compare `B-T`, `B-X`, and `FULL`, and produce at least one welfare or coalition-stability result requiring both endogenous standards depth and endogenous repositioning. If it cannot, terminate the paper rather than launching another architecture repair.
