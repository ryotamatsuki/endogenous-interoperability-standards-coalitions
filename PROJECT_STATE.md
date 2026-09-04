# Project State

Last updated: 2026-09-04

## Canonical status

- Project: Endogenous Interoperability and Standards Coalitions
- Last completed stage: **Stage 7R — Welfare / Generality Refresh**
- Stage-7R report: `reviews/STAGE_07R_WELFARE_GENERALITY_REFRESH_CESD_2026-09-04.md`
- Stage-7R decisions: `decisions/STAGE7R_CESD_DECISIONS.md`
- Stage-7R verification: `verification/stage07r_cesd_welfare_refresh.py`
- Stage-7R institutional refresh: `literature/STAGE7R_CESD_INSTITUTIONAL_REFRESH.md`
- Stage-4R report: `reviews/STAGE_04R_CONTINUATION_POLICY_REPAIR_2026-09-04.md`
- Stage-4R verification: `verification/stage04r_cesd_continuation_repair.py`
- Stage-11 trigger report: `reviews/STAGE_11_REFEREE_GATE_CESD_2026-09-04.md`
- Historical freeze ID: `CESD-THEORY-FREEZE-2026-09-04-v1` — **SUSPENDED pending Stage 8R re-freeze**
- Stage-7R verdict: **GO TO STAGE 8R — THEORY RE-FREEZE**
- Current canonical stage: **Stage 8R — Theory Re-Freeze**
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

The policy variable `s_C` is **additional within-coalition harmonization depth conditional on the formal regime**.

Feasible action set:

- `s_C in [0,s_bar]` if `|C|>=2`;
- `s_C=0` if `|C|=1`.

Pairwise friction map:

- same bloc `C`: `tau_ij=t_bar-s_C`;
- different blocs `C,D`: `tau_ij=t_bar+(s_C+s_D)/2`.

Therefore:

- IS: the grand coalition chooses `s_I in [0,s_bar]`;
- `SU_12`: coalition `{1,2}` chooses `s_12 in [0,s_bar]`, outsider singleton has `s_3=0`;
- SW: all blocs are singletons, so all depth variables equal zero.

Under `SU_12`:

`tau_12=t_bar-s_12`,

`tau_13=tau_23=t_bar+s_12/2`.

The within-bloc convergence / cross-bloc divergence mechanism is unchanged. Formal regime membership determines the binary compatibility/network graph. `s=0` means zero **additional harmonization depth**, not zero compatibility.

## Stage-4R continuation repair

Stage 11 found that the historical action set incorrectly gave singleton blocs positive harmonization-depth instruments and thereby created off-path policy values without verified downstream pure location equilibria.

Stage 4R repaired this by removing singleton depth instruments and requiring actual whole-circle location Nash continuations inside policy evaluation.

At `(t_bar,v,gamma,s_bar)=(1,0.04,0.11,0.25)`, Stage-4R verification establishes:

1. continuous whole-circle location best responses over every feasible repaired IS/SU policy depth;
2. all cyclic orders and circular-anchor branches on a dense policy grid;
3. one regular whole-circle location equilibrium at every audited IS/SU depth and in SW;
4. global scalar policy optimization on repaired action sets;
5. the B-T/B-X/FULL interaction signs and coalition-stability inequalities.

The canonical equilibrium path remains unchanged:

- `s_I*=0.25`;
- `s_12*=0.25`, outsider depth `0`;
- `s_SW=0`;
- `x_SU≈(0.084567,0.582100,0.833333)`.

## Main contribution after repair

The interaction-induced coalition-stability reversal survives:

`Delta_M^(B-T)<0`,

`Delta_M^(B-X)<0`,

`Delta_M^(FULL)>0`.

At the repaired canonical witness:

- `Delta_M^(B-T)≈-0.010167`;
- `Delta_M^(B-X)≈-0.000434`;
- `Delta_M^(FULL)≈+0.001571`.

FULL ranking:

`W_M^SU > W^IS > W_O^SU`, and `W_M^SU > W^SW`.

Hence B-T and B-X select IS, while FULL makes the three two-country SUs stable and IS pair-blockable.

The surviving contribution remains only the **FULL-only interaction result**. No ingredient-level novelty claim is revived.

## Stage-7R welfare / generality refresh

The Stage-4R repair does not alter the Stage-7 welfare package.

Exact identities retained:

- `Delta_M = Delta Pi_M + Delta CS/3`;
- `GW = A + v q'Gq - TC - sum_i C_i^D`.

At the repaired canonical witness:

- `Delta CS/3≈-0.0325785`;
- `Delta Pi_M≈+0.0341498`;
- `Delta_M≈+0.0015713`.

Thus SU becomes nationally attractive through domestic producer-rent capture rather than consumer gains.

Global welfare, reported net of the common baseline utility `A`:

- `GW_IS≈-0.0225000`;
- `GW_SU≈-0.0586685`;
- `GW_SW≈-0.0700000`.

Hence `GW_IS>GW_SU>GW_SW` at the witness.

Private/social member-product distances under repaired canonical SU policy:

- inherited: `D0=1/3`;
- constrained social: `D_social≈0.431427`;
- private: `D_private≈0.497533`.

Thus `D_private>D_social>D0`: some re-differentiation is socially useful, but firms over-re-differentiate.

The repaired upper welfare threshold remains `gamma_W≈0.132983` at `v=0.04`, `s_bar=0.25`. The historical approximate lower `gamma_GBR` language is no longer treated as a structural closed-form threshold; Stage-4R direct continuation verification is authoritative for regularity at the canonical witness.

## Institutional interpretation after repair

The Stage-7 primary-source classifications remain unchanged. Stage 4R improves semantic discipline:

- `s_C` is coalition-level additional harmonization depth;
- singleton blocs have no internal harmonization margin;
- the exact cross-bloc `1/2` coefficient remains a stylized normalization;
- strategic product re-differentiation remains a model prediction, not an established empirical fact.

Institutional records:

- `literature/STAGE7_CESD_INSTITUTIONAL_VALIDATION.md`;
- `literature/STAGE7R_CESD_INSTITUTIONAL_REFRESH.md`.

## Remaining Stage-11 attacks retained

The fatal continuation/SPNE attack is repaired. Remaining items for re-freeze / manuscript refresh / repeated Stage 11:

- Ruiz (2004) + Gandal–Shy (2001) synthesis risk;
- claim discipline / bounded sensitivity around the `1/2` cross-bloc normalization;
- binary formal compatibility graph versus continuous additional harmonization depth must be explicit;
- symmetric `CS/3` incidence is a limitation;
- institutional examples do not verify the exact cross-bloc derivative or observed strategic re-differentiation;
- welfare levels should be labeled net of common baseline utility `A`;
- IJIO-level fit remains unresolved.

## Required downstream refresh

Execute in order:

1. **Stage 8R — Theory Re-Freeze**;
2. **Stage 9R — Repository / Reproducibility Refresh**;
3. **Stage 10R — Manuscript Refresh**;
4. **Stage 11R — Repeated Robustness / Referee Attack Gate**.

Stage 6 novelty re-kill does not need repetition unless a later stage changes the mechanism or surviving contribution.

Stage 12 remains blocked until repeated Stage 11 returns `GO TO JOURNAL POSITIONING`.

## Current verdict

**STAGE 7R GO — WELFARE / GENERALITY PACKAGE PRESERVED.**

Proceed to Stage 8R theory re-freeze. No extensions are authorized during re-freeze.
