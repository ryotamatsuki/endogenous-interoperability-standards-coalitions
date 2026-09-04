# Stage 9 — Repository / Reproducibility Setup: C-ESD

Date: 2026-09-04
Canonical workflow: `ryotamatsuki/research-paper-workflow` v1.1
Workflow SHA: `488e5ab06c207909296a7564eaf9066f7f94319c`
Theory freeze: `CESD-THEORY-FREEZE-2026-09-04-v1`

## 1. Executive verdict

**REPRODUCIBILITY BASELINE READY.**

The repository now has a production scaffold in which the frozen Stage-4/7 computational objects are the sole numerical source, manuscript-facing tables are generated deterministically, the LaTeX manuscript is modular, dependencies are recorded, and CI verifies both the mathematics and build.

No theory change was introduced.

## 2. Starting remote state

Stage-9 work started only after re-inspecting the remote repository.

- starting `main` SHA: `95755cb82bceb136626279c5ff65fe1f1149afaa`;
- open PRs at start: none;
- historical stage branches: inspected; no historical reset performed;
- Stage-9 branch: `stage9/reproducibility-setup` created from the latest `main`.

## 3. Production repository structure

```text
.github/workflows/reproducibility.yml
.python-version
.gitignore
Makefile
requirements.txt
README.md
PROVENANCE.md
paper/
  main.tex
  preamble.tex
  sections/
    01_introduction.tex
    02_model.tex
    03_equilibrium.tex
    04_main_results.tex
    05_welfare.tex
    06_related_literature.tex
    07_conclusion.tex
references/
  references.bib
scripts/
  generate_outputs.py
tests/
  test_freeze_consistency.py
docs/
  REPRODUCIBILITY.md
  STAGE10_WRITING_CONTRACT.md
verification/
  stage04_cesd_minimal.py
  stage07_cesd_welfare_generality.py
theory/
  THEORY_FREEZE_CESD_2026-09-04.md
  PROPOSITION_REGISTER_CESD_2026-09-04.md
  PARAMETER_WELFARE_VERIFICATION_REGISTER_CESD_2026-09-04.md
```

Existing research records under `model/`, `literature/`, `reviews/`, `decisions/`, `notes/`, and `prompts/` remain preserved.

## 4. Build system

The root `Makefile` defines:

- `make verify` — Stage-4 verification + Stage-7 verification + freeze-consistency gate;
- `make outputs` — deterministic regeneration of manuscript-facing CSV and TeX;
- `make paper` — regeneration of outputs followed by `latexmk` PDF compilation;
- `make all` — complete verification and build;
- `make clean` — clean LaTeX/generated outputs.

The manuscript itself contains no duplicated model implementation.

## 5. Verification and tests

Canonical computational sources are unchanged:

1. `verification/stage04_cesd_minimal.py`
   - exact homogeneous symbolic checks;
   - heterogeneous weighted-Salop equilibrium machinery;
   - B-T / B-X / FULL witness;
   - whole-circle unilateral location-deviation audit;
   - local parameter-box check.

2. `verification/stage07_cesd_welfare_generality.py`
   - exact transfer cancellation;
   - national member welfare decomposition;
   - witness global-welfare ranking;
   - constrained social-location benchmark;
   - upper welfare threshold `gamma_W`.

3. `tests/test_freeze_consistency.py`
   - verifies Stage-8 freeze ID and frozen sign pattern remain present;
   - verifies the production scaffold and canonical verification sources exist;
   - verifies the output generator imports rather than reimplements the Stage-4/7 sources.

## 6. Environment / dependencies

Production Python is recorded as 3.12.

Pinned packages:

- `numpy==2.1.3`;
- `scipy==1.14.1`;
- `sympy==1.13.3`.

The LaTeX build uses `latexmk` and TeX Live packages installed in CI.

## 7. Table / figure pipeline

`scripts/generate_outputs.py` imports the frozen Stage-4 and Stage-7 verification modules and writes:

- `tables/generated_results.csv`;
- `tables/generated_results.tex`.

These generated outputs are intentionally ignored by Git and must not be hand edited.

No frozen theoretical figure is currently required. Therefore Stage 9 does not manufacture a decorative figure pipeline merely to satisfy a directory convention. If Stage 10 introduces a figure that visualizes already-frozen results, it must be generated deterministically from frozen verification objects and may not change theory.

## 8. Bibliography

`references/references.bib` provides a production BibTeX source seeded with verified closest-paper records from the Stage-6 literature matrix. Stage 10 may add verified references but may not change the frozen closest-paper positioning without literature change control.

## 9. CI / validation

GitHub Actions workflow: `.github/workflows/reproducibility.yml`.

Clean-environment sequence:

1. checkout;
2. Python 3.12 setup;
3. pinned dependency installation;
4. `make verify`;
5. `make outputs`;
6. TeX Live / `latexmk` installation;
7. `make paper`.

The first Stage-9 CI run completed successfully through all seven production steps, including the full frozen verification gates and LaTeX scaffold build.

A local-equivalent LaTeX smoke test was also performed in the working environment. `pdflatex` produced the scaffold PDF; the local container lacked the standalone `bibtex` executable, while the CI TeX installation provided the complete build and passed. This local environment difference is not a repository blocker.

## 10. Provenance

`PROVENANCE.md` now records:

- project relationship to the prior frozen standards-coalition paper;
- workflow version/SHA;
- Stage-8 freeze ID;
- Stage-9 starting main SHA;
- canonical computational source files;
- closest-paper positioning authority;
- post-freeze theory change-control rule.

`docs/REPRODUCIBILITY.md` documents collaborator-facing setup and build commands.

## 11. Remaining blockers

No Stage-9 blocker remains.

The main theoretical limitations identified at Stage 8 remain frozen limitations rather than reproducibility failures, especially the computational lower global-BR boundary and the Ruiz + Gandal-Shy synthesis attack.

## 12. Exact Stage-10 writing contract

Stage 10 may construct sections only against the Stage-8 freeze.

Required dependency order:

1. Model;
2. Equilibrium characterization;
3. Main results and B-T/B-X/FULL interaction;
4. Welfare;
5. approved robustness/generality discussion only;
6. institutional bridge;
7. related literature;
8. introduction;
9. discussion;
10. conclusion.

Reported numerical values must come from generated outputs or be directly traceable to the canonical verification modules. The FULL-only reversal must retain its frozen constructive regular-region proof status and must not be rewritten as a global closed-form theorem.

Any theory change requires Stage-8 change control and rerunning affected research gates.

## 13. Final verdict

**REPRODUCIBILITY BASELINE READY.**

Route: **Stage 10 — Section-by-Section Paper Construction**.
