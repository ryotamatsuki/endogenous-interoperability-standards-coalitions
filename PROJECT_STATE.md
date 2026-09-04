# Project State

Last updated: 2026-09-04

## Canonical status

- Project: Endogenous Interoperability and Standards Coalitions
- Last completed stage: **Stage 4R — Continuation-Existence / Policy-Stage Repair**
- Stage-4R report: `reviews/STAGE_04R_CONTINUATION_POLICY_REPAIR_2026-09-04.md`
- Stage-4R decisions: `decisions/STAGE4R_CESD_DECISIONS.md`
- Stage-4R model note: `model/STAGE4R_CESD_CONTINUATION_POLICY_REPAIR.md`
- Stage-4R verification: `verification/stage04r_cesd_continuation_repair.py`
- Stage-11 trigger report: `reviews/STAGE_11_REFEREE_GATE_CESD_2026-09-04.md`
- Historical freeze ID: `CESD-THEORY-FREEZE-2026-09-04-v1` — **SUSPENDED pending re-freeze**
- Stage-4R verdict: **REPAIR PASSES — CORE MECHANISM PRESERVED**
- Current canonical stage: **Stage 7R — Welfare / Generality Refresh**
- Production manuscript submission-ready: **NO until downstream refresh and repeated Stage 11**
- Stage 12 journal positioning authorized: **NO**
- Target journal: **UNRESOLVED pending repeated Stage 11**

## Canonical workflow

- Repository: `ryotamatsuki/research-paper-workflow`
- Version: `v1.1`
- Release SHA: `488e5ab06c207909296a7564eaf9066f7f94319c`

## Project boundary

`ryotamatsuki/private-compatibility-standards-coalitions` remains the frozen institutional IS/SU/SW benchmark B0 and must not be modified.

C-ESD does not algebraically nest B0. B0 is an institutional/coalition benchmark only.

## Repaired C-ESD game

Timing:

`rho -> harmonization depths of non-singleton blocs -> pairwise Tau(rho,s) -> product locations x_i -> prices -> W_i -> coalition stability`.

The continuous policy variable `s_C` is now defined strictly as **within-coalition harmonization depth**.

Feasible action set:

- `s_C in [0,s_bar]` if `|C|>=2`;
- `s_C=0` if `|C|=1`.

Pairwise friction map remains unchanged:

- same bloc `C`: `tau_ij=t_bar-s_C`;
- different blocs `C,D`: `tau_ij=t_bar+(s_C+s_D)/2`.

Therefore:

- IS: the grand coalition chooses `s_I in [0,s_bar]`;
- `SU_12`: coalition `{1,2}` chooses `s_12 in [0,s_bar]`, outsider singleton has `s_3=0` by definition;
- SW: every bloc is a singleton, so all depth variables equal zero.

Under `SU_12`:

`tau_12=t_bar-s_12`,

`tau_13=tau_23=t_bar+s_12/2`.

Thus the within-bloc convergence / cross-bloc divergence mechanism is unchanged.

Formal regime membership determines the binary compatibility/network graph. `s=0` means zero **additional harmonization depth conditional on the regime**, not zero compatibility.

## Why Stage 4R fixes the Stage-11 failure

Stage 11 found that the historical action set gave an SU outsider a positive depth instrument even though a singleton has no within-coalition harmonization relation. Off-path choices such as `(s_12,s_3)=(0.25,0.20)` could then leave the whole-circle pure location-equilibrium domain.

The repair removes that economically misclassified singleton instrument rather than reducing `s_bar` or adding a policy cost.

The historical cap remains `s_bar=0.25` at the canonical witness.

The repaired policy stage never assigns welfare to a fixed-order location candidate unless it passes continuous whole-circle unilateral best-response checks.

## Stage-4R continuation verification

Canonical verification: `verification/stage04r_cesd_continuation_repair.py`.

At `(t_bar,v,gamma,s_bar)=(1,0.04,0.11,0.25)` it verifies:

1. continuous whole-circle location best responses for the repaired continuation;
2. joint global search over feasible policy depth and unilateral deviation location for IS and SU, with maximum gains zero up to numerical precision;
3. all cyclic orders and circular-anchor branches on a dense 51-point feasible-depth grid, with exactly one regular interior whole-circle location equilibrium at every audited IS/SU depth;
4. one regular whole-circle location equilibrium in SW;
5. global scalar policy optimization on the repaired action sets;
6. B-T/B-X/FULL interaction signs and coalition-stability inequalities.

The Stage-4R verification is now included in the root `make verify` gate.

## Repaired canonical witness

The canonical parameter vector remains

`(t_bar,v,gamma,s_bar)=(1,0.04,0.11,0.25)`.

Repaired FULL policy choices remain:

- `s_I*=0.25`;
- `s_12*=0.25`, outsider depth fixed at `0`;
- `s_SW=0`.

FULL `SU_12` product locations remain approximately

`(0.084567, 0.582100, 0.833333)`.

The repair therefore leaves the historical equilibrium path unchanged.

## Main contribution after repair

The interaction-induced coalition-stability reversal survives unchanged:

`Delta_M^(B-T)<0`,

`Delta_M^(B-X)<0`,

`Delta_M^(FULL)>0`.

At the repaired canonical witness:

- `Delta_M^(B-T)≈-0.010167`;
- `Delta_M^(B-X)≈-0.000434`;
- `Delta_M^(FULL)≈+0.001571`.

The repaired FULL ranking remains

`W_M^SU > W^IS > W_O^SU`, and `W_M^SU > W^SW`.

Hence B-T and B-X continue to select IS, while FULL makes the three two-country SUs stable and IS pair-blockable.

The surviving contribution is still only the **FULL-only interaction result**. No ingredient-level novelty claim is revived.

## Theory-change classification

Stage 4R is a bounded **action-set clarification**:

Changed:

- singleton blocs no longer have a positive harmonization-depth action;
- downstream continuation validity is imposed inside policy evaluation rather than checked only after selecting the policy path.

Unchanged:

- IS/SU/SW partitions;
- pairwise friction formula and `1/2` normalization;
- compatibility/network graphs;
- Salop product-positioning game;
- redesign cost;
- price competition;
- national welfare `CS/3 + Pi_i`;
- coalition-stability rule;
- canonical parameter vector and equilibrium path;
- Stage-6 novelty result.

Because the historical freeze explicitly allowed every bloc to choose depth, the historical Stage-8 freeze is suspended and must be refreshed.

## Remaining Stage-11 attacks retained

The mathematical continuation/SPNE attack that triggered Stage 4R is repaired at the canonical constructive witness. The following remain for downstream refresh / repeated Stage 11:

- Ruiz (2004) + Gandal–Shy (2001) synthesis risk;
- claim discipline / sensitivity around the `1/2` cross-bloc normalization;
- explicit interpretation of binary formal compatibility graph versus continuous additional harmonization depth;
- symmetric `CS/3` incidence as an external-validity limitation;
- institutional examples do not verify the exact cross-bloc derivative or observed strategic re-differentiation;
- reported welfare levels should be labeled net of common baseline utility `A`;
- IJIO-level fit remains unresolved.

## Required downstream refresh

Because the action set changed, execute in order:

1. **Stage 7R — Welfare / Generality Refresh**;
2. **Stage 8R — Theory Re-Freeze**;
3. **Stage 9R — Repository / Reproducibility Refresh**;
4. **Stage 10R — Manuscript Refresh**;
5. **Stage 11R — Repeated Robustness / Referee Attack Gate**.

Stage 6 novelty re-kill does not need repetition unless a later stage changes the economic mechanism or surviving contribution.

Stage 12 remains blocked until repeated Stage 11 returns `GO TO JOURNAL POSITIONING`.

## Current verdict

**STAGE 4R REPAIR PASSES — CORE MECHANISM PRESERVED.**

The fatal Stage-11 off-path continuation failure is repaired without changing the canonical witness or tuning the policy cap. The project now advances to Stage 7R welfare/generality refresh under the repaired action set.
