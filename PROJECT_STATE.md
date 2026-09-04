# Project State

Last updated: 2026-09-04

## Canonical status

- Project: Endogenous Interoperability and Standards Coalitions
- Last completed stage: **Stage 6 — C-ESD Novelty Re-Kill**
- Stage-6 report: `reviews/STAGE_06_NOVELTY_REKILL_CESD_2026-09-04.md`
- Stage-6 closest-paper matrix: `literature/STAGE6_CESD_CLOSEST_PAPER_MATRIX.md`
- Stage-6 decisions: `decisions/STAGE6_CESD_DECISIONS.md`
- C-ESD canonical verdict: **GO**
- Current canonical stage: **Stage 7 — Welfare / Generality**
- Current route: C1 TERMINATED / C2 TERMINATED / C-RP TERMINATED / C-ESD SURVIVED STAGE 6
- Production manuscript authorized: NO
- Theory frozen: NO
- Target journal: UNRESOLVED

## Canonical workflow

- Repository: `ryotamatsuki/research-paper-workflow`
- Version: `v1.1`
- Release SHA: `488e5ab06c207909296a7564eaf9066f7f94319c`
- Stage-6 template: `templates/STAGE_06_NOVELTY_REKILL.md`
- Stage-6 route on GO: Stage 7 — Welfare / Generality

## Frozen project boundary

`ryotamatsuki/private-compatibility-standards-coalitions` remains the frozen Stage-8 mandatory institutional/coalition benchmark B0 and must not be modified.

C-ESD does not algebraically nest B0. B0 uses different demand, conversion-cost and private-adoption primitives.

## Frozen C-ESD game

C-ESD — **Endogenous Standard Differentiation × Strategic Product Repositioning**.

Timing:

`rho -> bloc depths s_C -> pairwise Tau(rho,s) -> product locations x_i -> prices -> W_i -> coalition stability`.

Policy map:

- same bloc `C`: `tau_ij=t_bar-s_C`;
- different blocs `C,D`: `tau_ij=t_bar+(s_C+s_D)/2`;
- bloc `C` maximizes `sum_{i in C} W_i` and blocs choose simultaneously.

Formal partition determines the compatibility network; network coefficient `v` is fixed with respect to depth. No direct policy cost exists.

Consumers are uniformly distributed on a unit Salop circle and each country owns one third of consumer mass. Firm repositioning cost is substantive:

`gamma d_c(x_i,h_i)^2/2`,

with anchors `h=(1/6,1/2,5/6)`.

## Stage-4 headline result retained through Stage 6

At the regular witness `t_bar=1`, `v=0.04`, `gamma=0.11`, `s_bar=0.25`:

### B-T — endogenous policy, fixed locations

Stable set: `{IS}`.

`Delta_M^(B-T)=-0.010167`.

### B-X — zero policy depth, endogenous locations

Stable set: `{IS}`.

`Delta_M^(B-X)=-0.000434`.

### FULL

SU members strategically re-differentiate. Stable set:

`{SU_12,SU_13,SU_23}`.

`Delta_M^(FULL)=+0.001571`.

A local 3x3x3 audit passes 23/27 points and a wider 5x5x5 audit passes 108/125 points, subject to whole-circle unilateral location-deviation checks. Low-gamma local stationary points with profitable jumps are rejected.

## Stage-6 killed novelty claims

The following are permanently unavailable as main contribution claims:

1. government standards policy affects endogenous product differentiation — Ruiz (2004) already contains this timing;
2. compatibility/network effects interact with product differentiation — broad prior literature;
3. partial compatibility / standards unions can be stable — Gandal–Shy, Matutes–Padilla, Economides–Skrzypacz, Ding–Ko–Shen and others;
4. continuous government compatibility policy — Klimenko (2009);
5. coalition-based interoperability has distinct price/welfare effects — current weighted-network interoperability literature;
6. interoperability regulation can induce strategic firm responses or unintended effects in a broad sense — current mandated-interoperability literature;
7. Salop/circle + compatibility + network effects is novel.

## Stage-6 surviving contribution

Only one main contribution candidate survives:

> **Interaction-induced coalition-stability reversal.** Endogenous government standard depth and endogenous firm product positioning each separately leave international standardization stable, but together induce regional-standardization members to re-differentiate enough to reverse their national-welfare ranking and destabilize international standardization in favor of regional standards unions.

Formal sign pattern:

`Delta_M^(B-T)<0`,

`Delta_M^(B-X)<0`,

`Delta_M^(FULL)>0`.

This is classified as a **NEW INTERACTION RESULT / MECHANISM**, not setup novelty.

## Strongest novelty threats

1. **Ruiz (2004) + Gandal & Shy (2001) synthesis attack**: Ruiz has policy -> endogenous product characteristics -> price competition; Gandal–Shy has three-country government standardization unions and coalition incentives. No audited theorem directly contains the FULL-only interaction reversal, but a referee may regard the architecture as a natural synthesis.
2. **Huang, Tan, Teh & Zhou (2026)**: current weighted-interoperability-network frontier includes coalitional configurations, prices and welfare, but not endogenous product positioning driving national government coalition stability.
3. **Kretschmer et al. (2025)**: mandated interoperability can trigger strategic firm responses that offset regulation, so the broad strategic-response narrative is old.

## Stage-6 verdict

**GO**.

The surviving FULL-only sign reversal is not directly absorbed by the audited literature or by either nested benchmark.

## Next action

Execute **Stage 7 — Welfare / Generality** on the surviving interaction result only.

Stage 7 must:

1. characterize the economic condition/region for the reversal beyond the numerical witness;
2. test dependence on the quadratic redesign cost and anchored Salop regularization without changing the core timing;
3. decompose consumer-surplus versus domestic-profit channels;
4. establish how general the `B-T=IS`, `B-X=IS`, `FULL=SU` ranking is;
5. keep every Stage-6 killed novelty claim dead.