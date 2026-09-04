# Project State

Last updated: 2026-09-04

## Canonical status

- Project: Endogenous Interoperability and Standards Coalitions
- Last completed stage: **Stage 10 — Section-by-Section Paper Construction**
- Stage-10 report: `reviews/STAGE_10_PAPER_CONSTRUCTION_CESD_2026-09-04.md`
- Stage-10 decisions: `decisions/STAGE10_CESD_DECISIONS.md`
- Freeze specification: `theory/THEORY_FREEZE_CESD_2026-09-04.md`
- Proposition register: `theory/PROPOSITION_REGISTER_CESD_2026-09-04.md`
- Freeze ID: `CESD-THEORY-FREEZE-2026-09-04-v1`
- C-ESD canonical verdict: **FULL DRAFT READY FOR REFEREE GATE**
- Current canonical stage: **Stage 11 — Robustness / Referee Attack Gate**
- Current route: C1 TERMINATED / C2 TERMINATED / C-RP TERMINATED / C-ESD THEORY FROZEN + REPRODUCIBILITY READY + FULL DRAFT READY
- Production manuscript authorized: **YES**
- Theory frozen: **YES**
- Recommended journal level: **IJIO / field-journal full paper**
- Target journal: not permanently locked

## Canonical workflow

- Repository: `ryotamatsuki/research-paper-workflow`
- Version: `v1.1`
- Release SHA: `488e5ab06c207909296a7564eaf9066f7f94319c`
- Stage-8 theory freeze remains the sole theory authority.
- Stage-9 reproducibility baseline remains the sole production/verification authority.
- Next canonical stage: Stage 11 — Robustness / Referee Attack Gate.

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

Formal partition determines the compatibility graph and fixed network coefficient `v`. Firms choose costly horizontal product repositioning on a unit Salop circle after observing policy depth. National welfare is `W_i=CS/3+Pi_i`. Coalition stability uses strict-blocking exclusive-membership logic.

## Frozen main contribution

Only the following main contribution is authorized and is now written in the manuscript:

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

Proof-status rule: the reversal is a **CONDITIONAL constructive regular-region result**, not a global closed-form theorem.

## Frozen exact analytic results

`PROVED` on stated regular domains:

1. weighted-Laplacian affine demand system;
2. regular interior price-equilibrium characterization;
3. fixed-cyclic-order location FOC/SOC system;
4. exact member welfare decomposition `Delta_M=Delta Pi_M+Delta CS/3`;
5. exact world-welfare identity `GW=A+v q'Gq-TC-sum_i C_i^D`.

Witness-specific global-welfare rankings and private/social distance comparisons remain computational illustrations, not global theorems.

## Stage-9 reproducibility baseline

Production sources:

- `verification/stage04_cesd_minimal.py`;
- `verification/stage07_cesd_welfare_generality.py`;
- `scripts/generate_outputs.py`;
- `tests/test_freeze_consistency.py`;
- `references/references.bib`;
- root `Makefile`;
- `.github/workflows/reproducibility.yml`.

Build gates remain `make verify`, `make outputs`, `make paper`, and `make all`.

## Stage-10 manuscript

Current production manuscript:

- `paper/main.tex`;
- `paper/sections/01_introduction.tex`;
- `paper/sections/02_model.tex`;
- `paper/sections/03_equilibrium.tex`;
- `paper/sections/04_main_results.tex`;
- `paper/sections/05_welfare.tex`;
- `paper/sections/06_related_literature.tex`;
- `paper/sections/07_conclusion.tex`;
- `paper/sections/08_appendix.tex`.

The paper was constructed in dependency order and preserves the Stage-8 proof-status boundary. The main benchmarks B-T and B-X remain in the main text. The welfare section makes the domestic-rent / consumer-loss incidence explicit. The appendix separates analytic proofs from the computational whole-circle verification supporting the constructive regular-region result.

GitHub Actions passed the frozen verification gates, deterministic output generation, and full LaTeX manuscript compilation on the Stage-10 manuscript head.

## Explicit post-freeze exclusions

No silent addition of relative-profit objectives, private interoperability investment, endogenous network intensity, policy costs, transfers/side payments, lobbying, dynamics, topology choice, additional countries, heterogeneous national CS incidence, alternative spatial geometries, or empirical estimation.

Any such change requires a formal theory-change record and rerunning affected gates.

## Stage-10 verdict

**FULL DRAFT READY FOR REFEREE GATE.**

## Next action

Execute **Stage 11 — Robustness / Referee Attack Gate** on the manuscript as written.

Stage 11 must attack mathematical correctness, whole-circle location equilibrium, policy-stage equilibrium, coalition stability, welfare accounting, proof-status wording, robustness of the regular region, Ruiz + Gandal–Shy synthesis risk, exposition and IJIO-level contribution strength. It may recommend revisions consistent with the freeze; substantive theory changes require formal change control.
