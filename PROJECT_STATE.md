# Project State

Last updated: 2026-09-04

## Canonical status

- Project: Endogenous Interoperability and Standards Coalitions
- Last completed stage: **Stage 11R — Repeated Robustness / Referee Attack Gate**
- Stage-11R report: `reviews/STAGE_11R_REFEREE_GATE_CESD_2026-09-04.md`
- Stage-11R decisions: `decisions/STAGE11R_CESD_DECISIONS.md`
- Canonical model freeze: `theory/THEORY_FREEZE_CESD_2026-09-04_v2.md`
- Current model-freeze ID: **`CESD-THEORY-FREEZE-2026-09-04-v2`**
- Model primitives under v2: **STILL FROZEN**
- Main-contribution freeze under v2: **SUSPENDED BY STAGE 11R**
- Stage-11R verdict: **REOPEN EARLIER STAGE — STAGE 6R2 CONTRIBUTION RE-KILL / BENCHMARK IDENTIFICATION REPAIR**
- Current canonical stage: **Stage 6R2 — Contribution Re-Kill / Benchmark Identification Repair**
- Production manuscript submission-ready: **NO**
- Stage 12 journal positioning authorized: **NO**
- Target journal: **UNRESOLVED**

## Canonical workflow

- Repository: `ryotamatsuki/research-paper-workflow`
- Version: `v1.1`
- Release SHA: `488e5ab06c207909296a7564eaf9066f7f94319c`

## Project boundary

`ryotamatsuki/private-compatibility-standards-coalitions` remains the frozen institutional IS/SU/SW benchmark B0 and must not be modified.

C-ESD does not algebraically nest B0. B0 is an institutional/coalition benchmark only.

## Repaired v2 game remains unchanged

Timing:

`rho -> harmonization depths of non-singleton blocs -> pairwise Tau(rho,s) -> product locations x_i -> prices -> W_i -> coalition stability`.

Policy action set:

- `s_C in [0,s_bar]` if `|C|>=2`;
- `s_C=0` if `|C|=1`.

Pairwise friction map:

- same bloc `C`: `tau_ij=t_bar-s_C`;
- different blocs `C,D`: `tau_ij=t_bar+(s_C+s_D)/2`.

Thus under `SU_12`:

- `tau_12=t_bar-s_12`;
- `tau_13=tau_23=t_bar+s_12/2`;
- outsider singleton depth is zero by definition.

Stage-4R continuation repair remains valid and production-authoritative for the repaired action set.

## Canonical witness remains unchanged

`(t_bar,v,gamma,s_bar)=(1,0.04,0.11,0.25)`.

FULL policy choices:

- `s_I*=0.25`;
- `s_12*=0.25`;
- SW has no continuous depth choice.

FULL `SU_12` product locations:

`x_SU≈(0.084567,0.582100,0.833333)`.

Existing welfare and coalition-ranking numbers remain numerically valid:

- `Delta_M^(B-T)≈-0.010167`;
- `Delta_M^(B-X0)≈-0.000434`;
- `Delta_M^(FULL)≈+0.001571`.

## Stage-11R contribution-identification finding

Stage 11R introduced a hostile benchmark `B-EQ`:

- non-singleton harmonization depths are **exogenous**;
- they are fixed at the FULL equilibrium values (`s_I=s_SU=s_bar`);
- product locations remain endogenous.

Because FULL itself chooses the cap for both IS and SU, `B-EQ` is exactly the same downstream game as FULL at the canonical witness.

Therefore:

`Delta_M^(B-EQ)=Delta_M^(FULL)>0`.

Canonical diagnostic: `verification/stage11r_cesd_referee_audit.py`.

### Implication

The old frozen headline

> policy endogeneity alone and product-position endogeneity alone leave IS stable, while their interaction makes SU stable

is **not identified by the canonical witness**. Policy endogeneity is not necessary for the reversal because exogenously fixing policy at the FULL equilibrium depth reproduces FULL.

B-X with zero additional depth remains a legitimate zero-harmonization benchmark, but it cannot be interpreted as establishing necessity of policy endogeneity.

## Surviving candidate contribution for Stage 6R2

The model may still support the narrower result-level contribution:

> **Policy-induced strategic product re-differentiation can reverse standards-coalition stability.** Evaluating standards policy with inherited/fixed product positions selects IS, while allowing firms to reposition after the same standards architecture can raise member producer rents enough to reverse the national IS/SU ranking and stabilize SU. At the canonical witness this occurs despite member consumer losses and despite world welfare favoring IS.

The central causal comparison becomes **B-T versus FULL**.

`B-X0` may remain auxiliary. `B-EQ` or an equivalent explicit statement must be acknowledged so the paper does not overclaim necessity of policy endogeneity.

## Novelty status reopened

The narrower candidate claim must be re-killed against at least:

- Gandal & Shy (2001), *Standardization Policy and International Trade*;
- Ruiz (2004), *Mix-and-Match and International Standardization Policy*;
- Klimenko (2009), *Policies and International Trade Agreements on Technical Compatibility for Industries with Network Externalities*;
- Huang, Tan, Teh & Zhou (2026), *A Network Approach to Interoperability*;
- Kretschmer, Rasch, Shekhar & Wenzel (2025), *Strategic Response to Mandated Interoperability: Privacy Spillovers in Network Markets*.

No ingredient-level novelty claim is authorized.

## Mathematical status after Stage 11R

Resolved:

- v1 singleton-depth/off-path continuation defect;
- canonical whole-circle location-best-response concern;
- price equilibrium/concavity block;
- welfare identities and world-welfare normalization.

Still limited but disclosed:

- full repaired policy-domain continuation validity is computational at canonical primitives rather than a global analytic theorem;
- the exact cross-bloc `1/2` coefficient is a stylized normalization;
- `CS/3` is a symmetric-incidence assumption;
- alternative demand geometries and reversed timing are not solved.

## Welfare package remains valid

At the witness:

- `Delta CS/3≈-0.0325785`;
- `Delta Pi_M≈+0.0341498`;
- `Delta_M≈+0.0015713`.

World welfare levels net of common baseline utility `A`:

- `GW_IS-A≈-0.0225000`;
- `GW_SU-A≈-0.0586685`;
- `GW_SW-A≈-0.0700000`.

Thus `GW_IS>GW_SU>GW_SW` at the witness.

Private/social member-product distances remain:

- inherited `1/3`;
- constrained social `≈0.431427`;
- private `≈0.497533`.

## Production / verification authority

Active verification chain:

1. `verification/stage04r_cesd_continuation_repair.py`;
2. `verification/stage07r_cesd_welfare_refresh.py`;
3. `verification/stage11r_cesd_referee_audit.py`;
4. `tests/test_freeze_consistency.py`;
5. `scripts/generate_outputs.py`.

The Stage-11R audit is expected to confirm the benchmark-identification objection; this is a successful hostile diagnostic, not a numerical failure.

## Required next sequence

1. **Stage 6R2 — Contribution Re-Kill / Benchmark Identification Repair** on the narrower claim.
2. If the narrower claim survives, conduct a renewed freeze/full-paper decision before restoring submission authority.
3. Refresh manuscript contribution language and benchmarks.
4. Repeat the referee gate.
5. Stage 12 remains blocked until a repeated referee gate returns `GO TO JOURNAL POSITIONING`.

## Current verdict

**STAGE 11R COMPLETE — MODEL SURVIVES, CURRENT CONTRIBUTION LABEL DOES NOT.**

Proceed to Stage 6R2. Do not change the repaired model merely to recover the superseded two-endogeneity narrative.
