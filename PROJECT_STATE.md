# Project State

Last updated: 2026-09-05

## Canonical status

- Project: Endogenous Interoperability and Standards Coalitions
- Working title: **Standards Coalitions and Strategic Product Repositioning**
- Canonical workflow: `ryotamatsuki/research-paper-workflow` **v1.2**
- Workflow release tag: `v1.2`
- Previous theory freeze: `CESD-THEORY-FREEZE-2026-09-04-v2`
- Theory status: **REOPENED — SPATIAL CONTINUATION FAMILY TERMINATED; AFFINE-DEMAND BERTRAND RE-FOUNDATION SELECTED**
- Stage 5RR: **NO-GO — linear localized continuation terminated**
- Stage 3R3: **GO — pure-quadratic localized transport selected for kill test**
- Stage 4R3Q: **NO-GO — Q1 continuation existence fails at first hostile feasible history**
- Stage 3R4: **GO — quadratic representative-consumer / affine-demand Bertrand selected**
- Stage 11R2: **STALE / REOPENED downstream of continuation failure**
- Stage 12 journal positioning: **administratively complete, submission authorization suspended**
- Stage 13: **CLOSURE REVOKED**
- Stage 14 submission QA authorized: **NO**
- Primary intended target only if the rebuilt theory survives: **International Journal of Industrial Organization (IJIO)**

## Binding continuation failures

Three versions of the spatial location-then-price family have failed the globally complete pure-continuation requirement:

1. unrestricted all-product linear Salop continuation;
2. explicit localized linear continuation;
3. explicit localized pure-quadratic continuation.

At the feasible IS history `s_I=1/4`, `x=(2/5,1/2,5/6)`, both localized variants have no pure price Nash equilibrium under exact finite candidate enumeration.

Stage 4R3Q authority:

- `verification/stage04r3q_quadratic_price_nonexistence.py`
- `reviews/STAGE_04R3Q_PURE_QUADRATIC_GLOBAL_CONTINUATION_2026-09-05.md`
- `decisions/STAGE04R3Q_CESD_DECISIONS.md`

The repeated failure is now treated as architecture-level evidence. No additional transport-curvature or localized-consideration patch is authorized.

## Stage 3R4 architecture re-selection II

Stage 3R4 compared the two remaining serious continuation families:

1. mixed-price continuation under the original linear spatial model;
2. a broader competition-stage redesign with conventional pure Bertrand continuation.

### Mixed-price route

Mixed pricing remains theoretically legitimate and is retained only as a reserve. Classical Hotelling work establishes mixed price equilibria when pure equilibria fail, including location-price SPNE constructions in simpler two-firm environments.

It is not selected because the present upstream game requires a well-defined expected continuation payoff for every relevant three-firm off-path location history with policy-dependent compatibility and network effects. Existence of some mixed equilibrium is insufficient if equilibrium payoffs or supports are non-unique. Characterizing that correspondence would become the main technical contribution of a different paper.

### Selected route

Stage 3R4 selects:

> **quadratic representative-consumer / globally nonnegative affine-demand Bertrand competition with endogenous product repositioning and standards-dependent pairwise substitutability/network structure.**

The circle remains a product-characteristic space used to define pairwise proximity and repositioning cost, but consumers are no longer partitioned into local arcs. A strictly concave quadratic utility produces globally defined differentiated-product demand.

A provisional Stage 4 object is

`U(q;rho,s,x) = a' q - (1/2) q' B(rho,s,x) q + (v/2) q' G_rho q`,

with `q>=0`, and effective curvature

`K(rho,s,x)=B(rho,s,x)-v G_rho`.

Stage 4 must choose one minimal pre-registered map from standards regime/depth and circular product positions into `B`, then prove `K` positive definite over the complete upstream strategy domain. Nonnegative demand and all zero-demand active sets must be handled globally.

Firms then compete in prices. Repositioning cost remains `gamma d_c(x_i,h_i)^2/2` unless Stage 4 independently kills that primitive.

## Prior-art risk created by the redesign

The selected architecture is conventional enough to avoid inventing a bespoke continuation device, but it creates a new novelty threat.

Closest families include:

- product-variety networks with linear-quadratic preferences and unique Bertrand equilibrium;
- compatibility decisions with network externalities and endogenous differentiation;
- international standards with redesign costs and network effects;
- differentiated price/quantity competition with network compatibility effects.

Therefore the paper cannot claim novelty from affine demand, product networks, compatibility, network effects, or differentiation separately.

The project survives only if the solved full game delivers a distinct joint loop:

`standards coalition -> compatibility/substitutability structure -> costly strategic repositioning -> changed Bertrand competition -> welfare/profit feedback -> coalition stability`,

and at least one substantive theorem/result disappears when either standards coalition choice or endogenous repositioning is removed.

## Stage 4R4A contract

Next formal stage: **Stage 4R4A — Affine-Demand Bertrand Continuation & Novelty Gate**.

Lexicographic gates:

1. **Demand well-posedness:** pre-register one minimal `(rho,s,x)->B` map and prove global strict concavity / positive definiteness; define nonnegative demand for all histories.
2. **Price continuation:** prove or exactly certify globally complete, payoff-unique Bertrand equilibrium including zero-demand active sets.
3. **Repositioning:** only after 1–2 pass, solve the location/repositioning game globally and require nondegenerate strategic repositioning.
4. **Novelty kill:** attack the actual solved full game against the closest product-variety-network and compatibility/differentiation literature.
5. **Economic continuation:** only after 1–4 pass may policy depth, welfare, reversal, and coalition stability be recomputed.

If any of Gates 1–4 fails, the default canonical recommendation is **TERMINATE THIS PAPER**, not another automatic Stage 3 repair cycle.

## What remains historical only

The following old-branch objects are not theorem/SPNE evidence:

- `Delta_M^(B-T)≈-0.010167`;
- `Delta_M^(FULL)≈+0.001571`;
- reported member welfare decomposition;
- reported world-welfare ordering;
- 9/9 local sign robustness conditional on the old linear branch.

## Current verdict

**STAGE 3R4 GO — DO NOT SUBMIT.**

Proceed to **Stage 4R4A — Affine-Demand Bertrand Continuation & Novelty Gate**.
