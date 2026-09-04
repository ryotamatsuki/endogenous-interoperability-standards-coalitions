# Project State

Last updated: 2026-09-04

## Canonical status

- Project: Endogenous Interoperability and Standards Coalitions
- Last completed stage: **Stage 10R — Manuscript Refresh**
- Stage-10R report: `reviews/STAGE_10R_MANUSCRIPT_REFRESH_CESD_2026-09-04.md`
- Stage-10R decisions: `decisions/STAGE10R_CESD_DECISIONS.md`
- Canonical theory freeze: `theory/THEORY_FREEZE_CESD_2026-09-04_v2.md`
- Canonical proposition register: `theory/PROPOSITION_REGISTER_CESD_2026-09-04_v2.md`
- Canonical parameter/welfare register: `theory/PARAMETER_WELFARE_VERIFICATION_REGISTER_CESD_2026-09-04_v2.md`
- Current freeze ID: **`CESD-THEORY-FREEZE-2026-09-04-v2`**
- Historical freeze ID: `CESD-THEORY-FREEZE-2026-09-04-v1` — **SUPERSEDED / PROVENANCE ONLY**
- Stage-10R verdict: **FULL DRAFT REFRESHED UNDER v2 — GO TO STAGE 11R REPEATED ROBUSTNESS / REFEREE ATTACK GATE**
- Current canonical stage: **Stage 11R — Repeated Robustness / Referee Attack Gate**
- Production manuscript submission-ready: **NO until Stage 11R passes**
- Stage 12 journal positioning authorized: **NO**
- Target journal: **UNRESOLVED pending Stage 11R**

## Canonical workflow

- Repository: `ryotamatsuki/research-paper-workflow`
- Version: `v1.1`
- Release SHA: `488e5ab06c207909296a7564eaf9066f7f94319c`

## Project boundary

`ryotamatsuki/private-compatibility-standards-coalitions` remains the frozen institutional IS/SU/SW benchmark B0 and must not be modified.

C-ESD does not algebraically nest B0. B0 is an institutional/coalition benchmark only.

## v2 frozen game

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
- `SU_12`: coalition `{1,2}` chooses `s_12 in [0,s_bar]`, outsider singleton has `s_3=0` by definition;
- SW: all blocs are singletons, so there is no continuous depth decision and all depths equal zero by definition.

Under `SU_12`:

`tau_12=t_bar-s_12`,

`tau_13=tau_23=t_bar+s_12/2`.

Formal regime membership determines the binary compatibility/network graph. `s=0` means zero **additional harmonization depth**, not zero compatibility.

## Stage-4R continuation repair incorporated into v2

Stage 11 found that v1 incorrectly gave singleton blocs positive harmonization-depth instruments, creating off-path policy values without verified downstream pure location equilibria.

Stage 4R repaired this by removing singleton depth instruments and requiring actual whole-circle location Nash continuations inside policy evaluation.

At `(t_bar,v,gamma,s_bar)=(1,0.04,0.11,0.25)`, canonical Stage-4R verification establishes:

1. continuous whole-circle location best responses over every feasible repaired IS/SU policy depth;
2. joint global search over policy depth and unilateral deviation location with no profitable deviations above numerical tolerance;
3. all cyclic orders and circular-anchor branches on a dense 51-point policy grid;
4. exactly one regular whole-circle location equilibrium at every audited IS/SU depth and one in SW;
5. global scalar policy optimization on repaired action sets;
6. B-T/B-X/FULL interaction signs and coalition-stability inequalities.

Canonical continuation verification: `verification/stage04r_cesd_continuation_repair.py`.

## Canonical witness

The parameter vector remains

`(t_bar,v,gamma,s_bar)=(1,0.04,0.11,0.25)`.

FULL policy choices:

- `s_I*=0.25`;
- `s_12*=0.25`, outsider singleton depth `0` by definition;
- SW has no continuous depth choice.

FULL `SU_12` product locations:

`x_SU≈(0.084567,0.582100,0.833333)`.

## Main contribution

The interaction-induced coalition-stability reversal remains:

`Delta_M^(B-T)<0`,

`Delta_M^(B-X)<0`,

`Delta_M^(FULL)>0`.

At the witness:

- `Delta_M^(B-T)≈-0.010167`;
- `Delta_M^(B-X)≈-0.000434`;
- `Delta_M^(FULL)≈+0.001571`.

FULL ranking:

`W_M^SU > W^IS > W_O^SU`, and `W_M^SU > W^SW`.

Hence B-T and B-X select IS, while FULL makes the three two-country SUs stable and IS pair-blockable.

The contribution remains only the **FULL-only interaction result**. No ingredient-level novelty claim is authorized.

## Proof-status boundary under v2

`PROVED` on stated domains:

- weighted-Laplacian demand system;
- unique regular interior price equilibrium;
- fixed-order location characterization;
- `Delta_M=Delta Pi_M+Delta CS/3`;
- `GW=A+v q'Gq-TC-sum_i C_i^D`.

`CONDITIONAL`:

- SU strategic re-differentiation on the regular branch;
- FULL-only coalition-stability reversal;
- general convex-adjustment-cost interpretation.

`NUMERICALLY SUPPORTED ONLY`:

- repaired full-policy-domain continuation validity at canonical primitives;
- witness world-welfare ranking;
- witness private/social location wedge.

No closed-form global parameter-space theorem is claimed.

## Welfare package

At the witness:

- `Delta CS/3≈-0.0325785`;
- `Delta Pi_M≈+0.0341498`;
- `Delta_M≈+0.0015713`.

Thus SU becomes nationally attractive through domestic producer-rent capture rather than consumer gains.

Global welfare levels, reported net of common baseline utility `A`:

- `GW_IS-A≈-0.0225000`;
- `GW_SU-A≈-0.0586685`;
- `GW_SW-A≈-0.0700000`.

Hence `GW_IS>GW_SU>GW_SW` at the witness.

Private/social member-product distances:

- inherited: `1/3`;
- constrained social: `≈0.431427`;
- private: `≈0.497533`.

The upper welfare threshold remains `gamma_W≈0.132983` at `v=0.04`, `s_bar=0.25`. No structural closed-form lower `gamma_GBR` threshold is part of v2.

## Stage-9R reproducibility authority

The active production chain is:

1. v2 theory/proposition/parameter registers;
2. `verification/stage04r_cesd_continuation_repair.py` for repaired continuations;
3. `verification/stage07r_cesd_welfare_refresh.py` for repaired welfare outputs;
4. `scripts/generate_outputs.py` for manuscript-facing serialization;
5. `tests/test_freeze_consistency.py` for v2 production consistency;
6. `docs/REPRODUCIBILITY.md` for environment/build instructions;
7. `docs/STAGE10R_WRITING_CONTRACT.md` for manuscript refresh constraints.

Historical v1 records remain provenance only and may not drive production tests or generated manuscript outputs.

## Stage-10R manuscript authority

The full production manuscript has been refreshed to v2. Submission-facing text now enforces:

- only non-singleton blocs choose additional harmonization depth;
- singleton blocs have depth zero by definition and no positive instrument;
- SU outsider depth is not a strategic policy choice;
- SW has no continuous depth stage;
- policy-stage values are based on verified whole-circle location-Nash continuations;
- the FULL-only reversal is constructive/conditional rather than a global analytic theorem;
- canonical full-policy-domain continuation validity is computationally supported at the witness;
- world-welfare numerical levels are reported net of `A`;
- manuscript-facing computation points to the Stage-4R / Stage-7R repaired chain;
- old v1 neighborhood-count language and the old numerical-looking lower `gamma_GBR≈0.10` threshold are not used as submission-authoritative claims.

Stage-10R report: `reviews/STAGE_10R_MANUSCRIPT_REFRESH_CESD_2026-09-04.md`.

## Institutional / novelty interpretation

- `s_C` is coalition-level additional harmonization depth.
- singleton blocs have no internal harmonization margin.
- the exact cross-bloc `1/2` coefficient is a stylized normalization.
- strategic product re-differentiation is a model prediction, not an established empirical fact.
- the strongest novelty attack remains Ruiz (2004) + Gandal–Shy (2001); only the nested FULL-only interaction result is claimable.

## Explicit exclusions

The frozen baseline excludes:

- relative-profit objectives;
- private interoperability investment;
- endogenous network intensity;
- direct policy costs;
- transfers/side payments;
- lobbying;
- dynamics;
- endogenous topology choice;
- additional countries;
- heterogeneous national consumer-surplus incidence;
- alternative spatial geometries;
- empirical estimation.

No excluded element may enter the manuscript without theory-change control.

## Required next gate

Execute:

1. **Stage 11R — Repeated Robustness / Referee Attack Gate** on the repaired v2 manuscript.

Stage 6 novelty re-kill need not be repeated unless Stage 11R or a later stage changes the mechanism or contribution.

Stage 12 remains blocked until Stage 11R returns `GO TO JOURNAL POSITIONING`.

## Current verdict

**STAGE 10R COMPLETE — FULL DRAFT REFRESHED UNDER v2.**

Proceed to Stage 11R. No theory changes are authorized before the repeated referee gate.