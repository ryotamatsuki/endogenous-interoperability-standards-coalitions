# Project State

Last updated: 2026-09-04

## Canonical status

- Project: Endogenous Interoperability and Standards Coalitions
- Last completed stage: **Stage 7.5 — Full-Theory Freeze Decision**
- Stage-7.5 report: `reviews/STAGE_075_FREEZE_DECISION_CESD_2026-09-04.md`
- Stage-7.5 decisions: `decisions/STAGE75_CESD_DECISIONS.md`
- C-ESD canonical verdict: **GO TO FULL PAPER**
- Current canonical stage: **Stage 8 — Theory Freeze**
- Current route: C1 TERMINATED / C2 TERMINATED / C-RP TERMINATED / C-ESD APPROVED FOR FULL PAPER
- Production manuscript authorized: **YES, subject to Stage-8 theory freeze**
- Theory frozen: NO
- Recommended journal level: **IJIO / field-journal full paper**
- Target journal: not yet permanently locked

## Canonical workflow

- Repository: `ryotamatsuki/research-paper-workflow`
- Version: `v1.1`
- Release SHA: `488e5ab06c207909296a7564eaf9066f7f94319c`
- Stage-7.5 template: `templates/STAGE_075_FREEZE_DECISION.md`
- Stage-7.5 GO route: Stage 8 — Theory Freeze

## Frozen project boundary

`ryotamatsuki/private-compatibility-standards-coalitions` remains the frozen Stage-8 institutional/coalition benchmark B0 and must not be modified.

C-ESD does not algebraically nest B0. B0 remains an institutional IS/SU/SW benchmark only.

## C-ESD game approved for freeze

Timing:

`rho -> bloc depths s_C -> pairwise Tau(rho,s) -> product locations x_i -> prices -> W_i -> coalition stability`.

Policy map:

- same bloc `C`: `tau_ij=t_bar-s_C`;
- different blocs `C,D`: `tau_ij=t_bar+(s_C+s_D)/2`;
- bloc `C` maximizes `sum_{i in C} W_i`;
- standards blocs choose depths simultaneously.

Formal partition determines the compatibility network and fixed network coefficient `v`. Firms choose costly horizontal product repositioning on a unit Salop circle after observing policy depth.

## Frozen main contribution

Only the following main contribution is authorized:

> **Interaction-induced coalition-stability reversal.** Endogenous government standard depth and endogenous firm product positioning each separately leave international standardization stable, but together can induce SU members to re-differentiate sufficiently to reverse their national-welfare ranking and make regional standards unions stable while IS becomes pair-blockable.

Canonical sign pattern:

`Delta_M^(B-T)<0`,

`Delta_M^(B-X)<0`,

`Delta_M^(FULL)>0`.

At the canonical witness `(t_bar,v,gamma,s_bar)=(1,0.04,0.11,0.25)`:

- `Delta_M^(B-T)=-0.010167`;
- `Delta_M^(B-X)=-0.000434`;
- `Delta_M^(FULL)=+0.001571`.

The result is a constructive nonempty-region result, not a claimed global parameter classification.

## Frozen welfare package

Exact member identity:

`Delta_M = Delta Pi_M + Delta CS/3`.

At the witness:

- `Delta CS/3=-0.0325785`;
- `Delta Pi_M=+0.0341498`;
- `Delta_M=+0.0015713`.

Thus the coalition reversal is driven by domestic producer-rent gains that narrowly exceed member consumer losses.

Exact world-welfare identity:

`GW=A+v q'Gq-TC-sum_i C_i^D`.

At the witness:

- `GW_IS=-0.0225000`;
- `GW_SU=-0.0586685`;
- `GW_SW=-0.0700000`.

Hence decentralized SU stability can be globally inefficient relative to IS.

At fixed canonical SU policy:

- inherited member distance `0.333333`;
- constrained social distance `0.431427`;
- private equilibrium distance `0.497533`.

Firms over-re-differentiate relative to the constrained social benchmark.

## Essential assumptions

1. Policy-controlled standards depth.
2. SU within-bloc versus cross-bloc friction asymmetry.
3. A distinct horizontal product-characteristic margin.
4. Positive but costly repositioning with intermediate effective curvature.
5. Network effects.
6. National welfare includes domestic producer rents but excludes foreign producer rents.
7. Government standards decisions precede firm product-position and price choices.

## Tractability / normalization assumptions

- three symmetric countries/firms;
- Salop circle and symmetric inherited anchors;
- quadratic baseline repositioning cost;
- symmetric national `CS/3` allocation;
- full coverage;
- zero marginal production cost;
- fixed `v` conditional on the formal compatibility graph;
- no direct policy cost;
- `1/2` cross-bloc coefficient as a symmetric mean-preserving normalization.

## Main remaining referee risks

1. Ruiz (2004) + Gandal–Shy (2001) synthesis attack.
2. No closed-form global lower `gamma_GBR` threshold because circle-order changes create nonsmooth deviations.
3. Symmetric national consumer-surplus incidence.
4. Policy-map normalization must not be sold as a primitive fact.
5. Institutional sources validate policy-controlled interoperability, not observed strategic re-differentiation.

These are major limitations but not Stage-7.5 blockers.

## Permanently killed novelty claims

Do not claim novelty from:

- government standards policy affecting product characteristics;
- continuous government compatibility policy;
- Salop + network effects + compatibility;
- partial compatibility / SU stability itself;
- broad strategic response to interoperability;
- coalitional interoperability price/welfare effects.

## Stage-7.5 verdict

**GO TO FULL PAPER.**

## Next action

Execute **Stage 8 — Theory Freeze** exactly on the Stage-7.5 package.

Stage 8 may clarify notation and theorem packaging but may not add relative profit, private interoperability investment, endogenous network intensity, policy costs, transfers, lobbying, dynamics, topology choice, additional countries, heterogeneous national CS incidence, or alternative spatial geometries.
