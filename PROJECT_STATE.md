# Project State

Last updated: 2026-09-04

## Canonical status

- Project: Endogenous Interoperability and Standards Coalitions
- Last completed stage: **Stage 8 — Canonical Theory Freeze**
- Freeze specification: `theory/THEORY_FREEZE_CESD_2026-09-04.md`
- Proposition register: `theory/PROPOSITION_REGISTER_CESD_2026-09-04.md`
- Parameter/welfare/verification register: `theory/PARAMETER_WELFARE_VERIFICATION_REGISTER_CESD_2026-09-04.md`
- Stage-8 decisions: `decisions/STAGE8_CESD_DECISIONS.md`
- Freeze ID: `CESD-THEORY-FREEZE-2026-09-04-v1`
- C-ESD canonical verdict: **THEORY FROZEN — GO TO REPRODUCIBILITY SETUP**
- Current canonical stage: **Stage 9 — Repository / Reproducibility Setup**
- Current route: C1 TERMINATED / C2 TERMINATED / C-RP TERMINATED / C-ESD THEORY FROZEN
- Production manuscript authorized: **YES after Stage-9 reproducibility setup; Stage 10 construction follows**
- Theory frozen: **YES**
- Recommended journal level: **IJIO / field-journal full paper**
- Target journal: not permanently locked

## Canonical workflow

- Repository: `ryotamatsuki/research-paper-workflow`
- Version: `v1.1`
- Release SHA: `488e5ab06c207909296a7564eaf9066f7f94319c`
- Stage-8 template: `templates/STAGE_08_THEORY_FREEZE.md`
- Stage-8 verdict: `THEORY FROZEN — GO TO REPRODUCIBILITY SETUP`
- Next canonical stage: Stage 9 — Repository / Reproducibility Setup

## Frozen project boundary

`ryotamatsuki/private-compatibility-standards-coalitions` remains the frozen institutional IS/SU/SW benchmark B0 and must not be modified.

C-ESD does not algebraically nest B0. B0 is an institutional/coalition benchmark only.

## Frozen C-ESD game

Timing:

`rho -> bloc depths s_C -> pairwise Tau(rho,s) -> product locations x_i -> prices -> W_i -> coalition stability`.

Policy map:

- same bloc `C`: `tau_ij=t_bar-s_C`;
- different blocs `C,D`: `tau_ij=t_bar+(s_C+s_D)/2`;
- bloc `C` maximizes `sum_{i in C} W_i`;
- standards blocs choose depths simultaneously.

Formal partition determines the compatibility graph and fixed network coefficient `v`. Firms choose costly horizontal product repositioning on a unit Salop circle after observing policy depth. Baseline redesign cost is quadratic around inherited anchors `h=(1/6,1/2,5/6)`.

National welfare is `W_i=CS/3+Pi_i`. Coalition stability uses strict-blocking exclusive-membership logic.

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
- `Delta_M^(FULL)=+0.001571`;
- `S_B-T=S_B-X={IS}`;
- `S_FULL={SU_12,SU_13,SU_23}`.

Proof-status rule: this reversal is frozen as a **CONDITIONAL constructive regular-region result**, not as a global closed-form theorem. The lower whole-circle global-BR boundary is computationally verified rather than analytically characterized.

## Frozen exact analytic results

The following are `PROVED` on their stated regular domains:

1. weighted-Laplacian affine demand system;
2. regular interior price-equilibrium characterization;
3. fixed-cyclic-order location FOC/SOC system;
4. exact member welfare decomposition `Delta_M=Delta Pi_M+Delta CS/3`;
5. exact world-welfare identity `GW=A+v q'Gq-TC-sum_i C_i^D`.

## Frozen welfare package

At the witness:

- `Delta CS/3=-0.0325785`;
- `Delta Pi_M=+0.0341498`;
- `Delta_M=+0.0015713`.

Thus the coalition reversal is driven by domestic producer-rent gains that narrowly exceed member consumer losses.

World welfare at the witness:

- `GW_IS=-0.0225000`;
- `GW_SU=-0.0586685`;
- `GW_SW=-0.0700000`.

This ranking is witness-specific / computational, not a global welfare theorem.

At fixed canonical SU policy:

- inherited member distance `0.333333`;
- constrained social distance `0.431427`;
- private equilibrium distance `0.497533`.

This private/social positioning comparison is also witness-specific.

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
- fixed `v` conditional on the compatibility graph;
- no direct policy cost;
- cross-bloc coefficient `1/2` as a symmetric mean-preserving normalization.

## Main remaining referee risks

1. Ruiz (2004) + Gandal–Shy (2001) synthesis attack.
2. No closed-form global lower `gamma_GBR` threshold because circle-order changes create nonsmooth deviations.
3. Symmetric national consumer-surplus incidence.
4. Policy-map normalization must not be sold as a primitive fact.
5. Institutional sources validate policy-controlled interoperability, not observed strategic re-differentiation.

These are frozen limitations, not unresolved Stage-8 blockers.

## Permanently killed novelty claims

Do not claim novelty from:

- government standards policy affecting product characteristics;
- continuous government compatibility policy;
- Salop + network effects + compatibility;
- partial compatibility / SU stability itself;
- broad strategic response to interoperability;
- coalitional interoperability price/welfare effects.

## Explicit post-freeze exclusions

No silent addition of:

- relative-profit objectives;
- private interoperability investment;
- endogenous network intensity;
- policy costs;
- transfers/side payments;
- lobbying;
- dynamics;
- topology choice;
- additional countries;
- heterogeneous national CS incidence;
- alternative spatial geometries;
- empirical estimation.

Any such change requires a formal theory-change record and rerunning affected gates.

## Stage-8 verdict

**THEORY FROZEN — GO TO REPRODUCIBILITY SETUP.**

## Next action

Execute **Stage 9 — Repository / Reproducibility Setup** without changing the frozen theory.

Stage 9 should organize modular LaTeX, bibliography, symbolic/numerical verification, deterministic tables/figures, dependency/environment specification, build orchestration, tests/CI where feasible, and provenance/decision records. Stage 10 manuscript construction must use the Stage-8 freeze as the sole theory authority.
