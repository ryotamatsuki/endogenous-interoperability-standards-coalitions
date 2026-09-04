# Stage 10 — Section-by-Section Paper Construction: C-ESD

Date: 2026-09-04
Theory authority: `CESD-THEORY-FREEZE-2026-09-04-v1`
Stage-9 authority: `reviews/STAGE_09_REPRODUCIBILITY_SETUP_2026-09-04.md`

## 1. Executive verdict

**FULL DRAFT READY FOR REFEREE GATE.**

The Stage-8-frozen theory has been converted into a coherent modular manuscript without changing the game, policy map, welfare definitions, benchmark definitions, coalition-stability logic, or proof-status boundaries. The manuscript compiles cleanly under the Stage-9 reproducibility pipeline and all frozen mathematical verification gates pass.

Route: **Stage 11 — Robustness / Referee Attack Gate**.

## 2. Construction order completed

The manuscript was built in the dependency order mandated by `docs/STAGE10_WRITING_CONTRACT.md`:

1. Model;
2. Equilibrium characterization;
3. Main results and B-T/B-X/FULL interaction;
4. Welfare, incidence and generality;
5. Related literature;
6. Introduction;
7. Conclusion;
8. proof / verification appendix;
9. abstract finalized only after the body was fixed.

## 3. Manuscript structure

- `paper/main.tex` — title, abstract, section assembly, bibliography;
- `paper/sections/01_introduction.tex` — question, mechanism, contribution, limitations and roadmap;
- `paper/sections/02_model.tex` — regimes, bloc-depth policy map, Salop/network demand, product repositioning, welfare and timing;
- `paper/sections/03_equilibrium.tex` — weighted-Laplacian demand, price equilibrium, conditional location system, global-BR qualification, policy-stage continuation values;
- `paper/sections/04_main_results.tex` — mandatory B-T/B-X benchmarks, strategic re-differentiation, constructive FULL-only coalition reversal;
- `paper/sections/05_welfare.tex` — exact member decomposition, national/global wedge, private/social positioning comparison, convex-cost interpretation and institutional bridge;
- `paper/sections/06_related_literature.tex` — narrow result-level distinction against Gandal–Shy, Ruiz, Klimenko and compatibility/differentiation literatures;
- `paper/sections/07_conclusion.tex` — disciplined summary and limitations;
- `paper/sections/08_appendix.tex` — analytic derivations and explicit computational verification boundary.

## 4. Main contribution as written

The manuscript states only the Stage-8-authorized contribution:

> Endogenous standard depth alone and endogenous product positioning alone each leave international standardization stable, but their joint endogeneity can induce SU-member strategic re-differentiation that reverses member national welfare and makes regional standardization unions stable while IS becomes pair-blockable.

The canonical sign pattern remains

`Delta_M^(B-T)<0`,

`Delta_M^(B-X)<0`,

`Delta_M^(FULL)>0`.

No ingredient-level novelty claim was revived.

## 5. Proof-status discipline

The manuscript distinguishes three classes exactly as frozen.

### Analytic / proved on stated regular domains

- weighted-Laplacian affine demand;
- regular interior price-equilibrium characterization;
- fixed-cyclic-order location FOC/SOC system;
- exact member welfare decomposition;
- exact global-welfare transfer-cancellation identity.

### Constructive regular-region result

The FULL-only coalition reversal is explicitly presented as a constructive nonempty-region proposition. The text records the canonical witness, strict inequalities, continuity argument, whole-circle deviation requirement and neighborhood audits. It explicitly states that no global closed-form classification is claimed.

### Witness-specific comparisons

The world-welfare ordering and private/social product-distance comparison are explicitly described as canonical-witness results rather than global theorems.

## 6. Numerical provenance

All manuscript-facing numerical objects remain traceable to the Stage-4/7 verification modules. The main-results section imports `tables/generated_results.tex` when available; the file is regenerated from `scripts/generate_outputs.py` and is not hand edited.

No manual numerical override was introduced in Stage 10.

## 7. Literature positioning

The manuscript adopts the frozen narrow positioning.

- Gandal & Shy (2001) already provide three-country standardization-union and coalition incentives.
- Ruiz (2004) already provides government standards policy followed by endogenous product characteristics and price competition.
- Klimenko (2009) already provides continuous government compatibility policy with network effects.
- Baake & Boom, Matutes & Padilla, and Ding–Ko–Shen establish important compatibility/network/differentiation components.

The paper therefore claims novelty only for the verified interaction-induced coalition-ranking reversal relative to B-T and B-X.

## 8. Build and verification gate

On PR #32, GitHub Actions completed successfully on the manuscript head through:

1. Python dependency installation;
2. Stage-4 frozen verification;
3. Stage-7 welfare/generality verification;
4. freeze-consistency tests;
5. deterministic table regeneration;
6. TeX Live / latexmk setup;
7. full manuscript + appendix compilation.

No theory or verification code was modified to make the manuscript build.

## 9. Remaining limitations intentionally preserved

The full draft does not resolve or hide the following Stage-8 limitations:

1. no closed-form global lower whole-circle `gamma_GBR` boundary;
2. symmetric national `CS/3` incidence;
3. exact cross-bloc `1/2` coefficient is a normalization;
4. institutional examples validate the policy-controlled interoperability primitive but not observed re-differentiation;
5. Ruiz + Gandal–Shy synthesis remains the strongest novelty/referee attack;
6. headline reversal is not a universal parameter-space theorem.

These items are inputs to Stage 11 rather than reasons to alter the frozen theory during Stage 10.

## 10. Stage-11 contract

Stage 11 must attack the manuscript as written. It should re-audit:

- mathematical correctness and notation consistency;
- whole-circle location equilibrium logic;
- policy-stage equilibrium and coalition stability;
- proof-status wording;
- welfare accounting and incidence;
- robustness of the constructive regular region;
- closest-paper synthesis / incremental-contribution risk;
- exposition, referee readability and IJIO-level contribution strength.

Stage 11 may recommend revisions consistent with the freeze. Any substantive theory change requires formal Stage-8 change control and rerunning affected gates.

## 11. Final verdict

**FULL DRAFT READY FOR REFEREE GATE.**

Next canonical stage: **Stage 11 — Robustness / Referee Attack Gate**.
