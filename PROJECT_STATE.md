# Project State

Last updated: 2026-09-04

## Canonical status

- Project: Endogenous Interoperability and Standards Coalitions
- Last completed stage: Stage 1 — Source & Mathematical Audit
- Stage 1 execution status: COMPLETED
- Stage 1 report: `reviews/STAGE_01_SOURCE_MATHEMATICAL_AUDIT_2026-09-04.md`
- Stage 1 canonical verdict: `GO TO NOVELTY GATE`
- Current canonical stage: Stage 2 — Literature Frontier / Novelty Kill Gate
- Stage 2 status: AUTHORIZED / NOT YET RUN
- Current route: theory candidate — GENERALIZATION / UNIFICATION CANDIDATE
- Production manuscript authorized: NO
- Theory frozen: NO
- Target journal: UNRESOLVED

## Canonical workflow reference

- Repository: `ryotamatsuki/research-paper-workflow`
- Version: `v1.1`
- Release SHA: `488e5ab06c207909296a7564eaf9066f7f94319c`
- Stage 1 template: `templates/STAGE_01_AUDIT.md`
- Next template: `templates/STAGE_02_NOVELTY_GATE.md`

## Frozen project boundary

This project remains independent from `private-compatibility-standards-coalitions`. The earlier paper is now a **mandatory nested benchmark** for novelty analysis, but its Stage-8 frozen theory must not be altered through this repository.

## Stage 1 audited residual research question

> Does endogenizing a continuous post-agreement private interoperability implementation margin inside a government standards-coalition game generate a coalition-stability result that is unavailable in both (i) binary private-adoption coalition models and (ii) continuous compatibility / government-policy models considered separately?

This replaces the Stage-0 wording for Stage 2 purposes.

## Stage 1 findings binding on later work

### 1. Actor/timing separation is not a novelty claim

The frozen benchmark `private-compatibility-standards-coalitions` already has the timing

`formal government partition -> private standard adoption -> Cournot competition -> national welfare -> coalition stability`.

Therefore the new project cannot claim novelty merely because governments choose a formal coalition and firms move later.

### 2. Continuous compatibility plus government policy is also occupied

Klimenko (2009) studies partial technical compatibility, government compatibility standards/policies, compatibility-enhancing effort, international competition, national policy incentives, and international coordination. The residual contribution, if any, must involve endogenous **coalition membership/stability** combined with private continuous implementation.

### 3. The scalar threshold `â` is not primitive

Coalition stability must first be evaluated using regime-specific continuation equilibria:

`Delta_i(rho,rho';theta) = V_i(rho;theta) - V_i(rho';theta)`.

A scalar `â` may be defined only if a later model proves continuity, monotonicity, and a unique root in an economically meaningful scalar implementation statistic.

### 4. `a_o*` is not primitive either

The general object is a regime-specific implementation vector `a*(rho;theta)`. A scalar `a_o*` requires a proved symmetric or one-dimensional reduction.

### 5. Symmetric FOC is insufficient for interoperability equilibrium

The Stage-1 SymPy audit of Stadler, Tobler Trexler & Unsorg (2022) exactly reproduces their price equilibrium and symmetric compatibility FOC, but finds that the stated interiority condition alone does not guarantee the own SOC/global best response for all admissible installed bases. Later project work must verify SOC, global best responses, asymmetric deviations, and corners.

Verification artifact: `verification/stage01_stadler_sympy.py`.

### 6. Transport-cost-only interoperability remains a kill route

If `a` enters the product market only through an effective coefficient such as `t_eff=t(a)`, the downstream block is a change of variable. Foros-type compatibility models make this risk explicit. A paper contribution requires an independently interpretable interaction between formal state `rho` and private implementation `a`.

## Stage 1 audited representation

See:

`model/AUDITED_STAGE1_REPRESENTATION.md`.

No specific Salop/Cournot/Bertrand/network-effect/cost functional form is canonical at this stage.

## Stage 2 mandatory nested benchmarks

- **B0:** `private-compatibility-standards-coalitions` — binary private adoption within government standards coalitions.
- **B1:** continuous private compatibility — Stadler et al.; Foros & Hansen; de Palma et al.; Garcia; Toshimitsu; Jeon et al.
- **B2:** government continuous compatibility / international coordination — especially Klimenko (2009), plus related policy-intervention work.
- **B3:** government standardization unions — especially Gandal & Shy (2001).

## Stage 2 primary kill test

Kill the branch if the proposed continuous model can be obtained by taking B0, inserting a standard continuous-compatibility block from B1/B2, and merely smoothing/relabeling the existing binary stability thresholds without producing a new full-game strategic or welfare result.

## Next action

Instantiate and execute Stage 2 — Literature Frontier / Novelty Kill Gate using the canonical v1.1 template.

Stage 2 may compare literature and determine whole-game absorption. It may not add complexity merely to evade prior art.
