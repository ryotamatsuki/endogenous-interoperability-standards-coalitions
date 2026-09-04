# Project State

Last updated: 2026-09-04

## Canonical status

- Project: Endogenous Interoperability and Standards Coalitions
- Last completed stage: **Stage 9 — Repository / Reproducibility Setup**
- Stage-9 report: `reviews/STAGE_09_REPRODUCIBILITY_SETUP_2026-09-04.md`
- Stage-9 decisions: `decisions/STAGE9_CESD_DECISIONS.md`
- Freeze specification: `theory/THEORY_FREEZE_CESD_2026-09-04.md`
- Proposition register: `theory/PROPOSITION_REGISTER_CESD_2026-09-04.md`
- Freeze ID: `CESD-THEORY-FREEZE-2026-09-04-v1`
- C-ESD canonical verdict: **REPRODUCIBILITY BASELINE READY**
- Current canonical stage: **Stage 10 — Section-by-Section Paper Construction**
- Current route: C1 TERMINATED / C2 TERMINATED / C-RP TERMINATED / C-ESD THEORY FROZEN + REPRODUCIBILITY READY
- Production manuscript authorized: **YES**
- Theory frozen: **YES**
- Recommended journal level: **IJIO / field-journal full paper**
- Target journal: not permanently locked

## Canonical workflow

- Repository: `ryotamatsuki/research-paper-workflow`
- Version: `v1.1`
- Release SHA: `488e5ab06c207909296a7564eaf9066f7f94319c`
- Stage-9 template: `templates/STAGE_09_REPRODUCIBILITY_SETUP.md`
- Stage-9 starting main SHA: `95755cb82bceb136626279c5ff65fe1f1149afaa`
- Stage-9 verdict: `REPRODUCIBILITY BASELINE READY`
- Next canonical stage: Stage 10 — Section-by-Section Paper Construction

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
- `paper/` modular LaTeX scaffold;
- `references/references.bib`;
- `requirements.txt` + `.python-version`;
- root `Makefile`;
- `.github/workflows/reproducibility.yml`;
- `docs/REPRODUCIBILITY.md`;
- `docs/STAGE10_WRITING_CONTRACT.md`.

Build gates:

- `make verify`;
- `make outputs`;
- `make paper`;
- `make all`.

The initial clean GitHub Actions run passed frozen verification, deterministic output generation, and LaTeX scaffold compilation.

## Explicit post-freeze exclusions

No silent addition of relative-profit objectives, private interoperability investment, endogenous network intensity, policy costs, transfers/side payments, lobbying, dynamics, topology choice, additional countries, heterogeneous national CS incidence, alternative spatial geometries, or empirical estimation.

Any such change requires a formal theory-change record and rerunning affected gates.

## Stage-9 verdict

**REPRODUCIBILITY BASELINE READY.**

## Next action

Execute **Stage 10 — Section-by-Section Paper Construction** in the dependency order fixed in `docs/STAGE10_WRITING_CONTRACT.md`.

Stage 10 may write against the frozen theory; it may not change the model, upgrade proof-status claims, or hand-edit generated numerical results.
