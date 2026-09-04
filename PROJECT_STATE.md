# Project State

Last updated: 2026-09-04

## Canonical status

- Project: Endogenous Interoperability and Standards Coalitions
- Last completed stage: **Stage 4 — C-ESD Minimal Model**
- Stage-4 report: `reviews/STAGE_04_MINIMAL_MODEL_CESD_2026-09-04.md`
- Stage-4 model source: `model/STAGE4_MINIMAL_MODEL_CESD.md`
- Stage-4 verification: `verification/stage04_cesd_minimal.py`
- Stage-4 decisions: `decisions/STAGE4_CESD_DECISIONS.md`
- C-ESD canonical verdict: **GO**
- Current canonical stage: **Stage 6 — Novelty Re-Kill**
- Current route: C1 TERMINATED / C2 TERMINATED / C-RP TERMINATED / C-ESD SURVIVED STAGE 4
- Production manuscript authorized: NO
- Theory frozen: NO
- Target journal: UNRESOLVED

## Canonical workflow

- Repository: `ryotamatsuki/research-paper-workflow`
- Version: `v1.1`
- Release SHA: `488e5ab06c207909296a7564eaf9066f7f94319c`
- Stage-4 template: `templates/STAGE_04_MINIMAL_MODEL.md`
- Stage-4 route on GO: Stage 6 — Novelty Re-Kill

## Frozen project boundary

`ryotamatsuki/private-compatibility-standards-coalitions` remains the frozen Stage-8 mandatory institutional/coalition benchmark B0 and must not be modified.

C-ESD does not algebraically nest B0. B0 uses different demand, conversion-cost and private-adoption primitives.

## C-ESD frozen mechanism

C-ESD — **Endogenous Standard Differentiation × Strategic Product Repositioning**.

Timing:

`rho -> bloc depths s_C -> pairwise Tau(rho,s) -> product locations x_i -> prices -> W_i -> coalition stability`.

### Policy map

For each formal standards bloc `C`, `s_C in [0,s_bar]`, `s_bar<t_bar`.

Same bloc:

`tau_ij=t_bar-s_C`.

Different blocs `C,D`:

`tau_ij=t_bar+(s_C+s_D)/2`.

Bloc `C` maximizes `sum_{i in C} W_i`; blocs choose simultaneously.

The formal partition determines the compatibility-network graph and network coefficient `v` is fixed with respect to policy depth.

No direct policy cost is present.

## Stage-4 Salop microfoundation

Consumers are uniformly distributed on a unit product-characteristic circle. Country of origin is independent of product taste; each country owns one third of consumer mass.

On arc `ij`:

`u_i=A-p_i-tau_ij y+v n_i`.

The exact weighted-Laplacian demand is

`q=b-(1/2)L(Tau)p+(v/2)L(Tau)G_rho q`.

Price and location continuations are solved by backward induction. Firm redesign/repositioning cost remains

`gamma d_c(x_i,h_i)^2/2`,

with inherited anchors

`h=(1/6,1/2,5/6)`.

Every certified location witness must pass whole-circle unilateral-deviation checks, not only local FOCs/SOCs.

## Stage-4 exact benchmark results

At equal spacing and common friction `t`:

IS:

`q_i=1/3`, `p_i=t/3`, `W_i=v/3-t/36`.

Thus `s_I*=s_bar`.

Symmetric SW:

`q_i=1/3`, `p_i=(2t-3v)/6`, `W_i=v/9-t/36`.

In the Stage-4 result region, the SW singleton-policy equilibrium is `s_i=0`.

## Stage-4 witness

Normalize

`t_bar=1`, `v=0.04`, `gamma=0.11`, `s_bar=0.25`.

### B-T — endogenous policy, fixed product positions

- IS: `W=-0.007500`
- SU member: `W=-0.017667`
- SU outsider: `W=-0.025410`
- SW: `W=-0.023333`

Stable set:

`{IS}`.

### B-X — zero policy depth, endogenous product positions

- IS: `W=-0.014444`
- SU member: `W=-0.014878`
- SU outsider: `W=-0.033413`
- SW: `W=-0.023333`

Stable set:

`{IS}`.

### FULL

Policy equilibrium:

- IS: `s_I=0.25`
- SU_12: `(s_12,s_3)=(0.25,0)`
- SW: `(0,0,0)`

SU location equilibrium:

`x=(0.084567,0.582100,0.833333)`.

Welfare:

- IS: `W=-0.007500`
- SU member: `W=-0.005929`
- SU outsider: `W=-0.046811`
- SW: `W=-0.023333`

Therefore

`W_M^FULL > W_I^FULL > W_O^FULL`,

and `W_M^FULL>W_W^FULL`.

Stable set:

`{SU_12,SU_13,SU_23}`.

## Headline interaction

Define

`Delta_M=W_SU_member-W_IS`.

At the Stage-4 witness:

`Delta_M^(B-T)=-0.010167`,

`Delta_M^(B-X)=-0.000434`,

`Delta_M^(FULL)=+0.001571`.

Thus neither government policy choice alone nor product repositioning alone generates the coalition reversal. The interaction does.

## Robustness / regularity audit

A local 3x3x3 grid around the witness passes the strict FULL-only reversal plus whole-circle SU location best-response checks at 23/27 points. A wider 5x5x5 audit passes at 108/125 points.

Low-`gamma` counterexamples exist where an SU local stationary point fails because the outsider has a profitable jump around the circle. Those points are rejected; no new primitive is added to rescue them.

## Stage-4 verdict

**GO**.

The FULL architecture generates a coalition-stability result unavailable from both nested benchmarks.

## Next action

Execute **Stage 6 — Novelty Re-Kill** on the actual surviving proposition:

> Endogenous government standard depth and endogenous firm product repositioning interact to reverse standards-coalition stability: B-T and B-X select international standardization, while the FULL game makes regional standardization unions stable and IS pair-blockable.

Do not add relative profit, private interoperability investment, endogenous network intensity, policy costs, transfers, dynamics, lobbying, topology choice or additional countries before the novelty re-kill is completed.
