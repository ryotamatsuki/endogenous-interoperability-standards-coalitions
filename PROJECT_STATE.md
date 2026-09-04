# Project State

Last updated: 2026-09-04

## Canonical status

- Project: Endogenous Interoperability and Standards Coalitions
- Last completed stage: **Stage 6R2 — Post-Repair Novelty Re-Kill**
- Stage-6R2 report: `reviews/STAGE_06R2_POST_REPAIR_NOVELTY_REKILL_CESD_2026-09-04.md`
- Stage-6R2 decisions: `decisions/STAGE6R2_CESD_DECISIONS.md`
- Stage-6R2 closest-paper matrix: `literature/STAGE6R2_CESD_CLOSEST_PAPER_MATRIX.md`
- Stage-6R2 search log: `literature/STAGE6R2_CESD_SEARCH_LOG.md`
- Canonical model freeze: `theory/THEORY_FREEZE_CESD_2026-09-04_v2.md`
- Current model-freeze ID: **`CESD-THEORY-FREEZE-2026-09-04-v2`**
- Model primitives under v2: **STILL FROZEN**
- Main-contribution freeze under v2: **NOT YET RESTORED**
- Stage-6R2 verdict: **CONDITIONAL GO — NARROWER CLAIM REQUIRED**
- Novelty confidence: **MEDIUM**
- Current canonical route: **contribution/benchmark refresh -> repeated Stage 11R**
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

## Stage-11R contribution-identification finding remains binding

Stage 11R introduced `B-EQ`: non-singleton harmonization depths are exogenous and fixed at the FULL equilibrium values while product locations remain endogenous. Because FULL chooses the cap for both IS and SU at the canonical witness,

`Delta_M^(B-EQ)=Delta_M^(FULL)>0`.

Therefore the old headline that policy endogeneity and product-position endogeneity are jointly necessary for the reversal is **not identified**. `B-X0` remains an auxiliary zero-harmonization benchmark only.

## Stage-6R2 novelty finding

A hostile multi-literature search re-opened Gandal & Shy (2001), Ruiz (2004), Klimenko (2009), compatibility × endogenous-differentiation papers, standards-coalition models, and the 2024–2026 interoperability frontier.

No directly absorbing result was located in the audited search as of 2026-09-04. The strongest reconstruction threat is **Gandal & Shy (2001) + Ruiz (2004)**:

- Gandal-Shy supplies the three-country standards-union / national-welfare / coalition architecture;
- Ruiz supplies government standards policy -> endogenous product characteristics -> prices and excessive differentiation.

However, Ruiz's endogenous-location extension reports qualitatively similar government-policy outcomes rather than a standards-policy ranking reversal, and Gandal-Shy has no post-policy endogenous product-repositioning stage. The surviving result is therefore not an immediate proposition-level corollary of the audited predecessors.

The 2024–2026 frontier further kills any setup-level claim: Huang et al. (2026) covers weighted interoperability-network design; Kretschmer et al. (2025) covers strategic response to mandated interoperability. Neither audited record contains the C-ESD national standards-coalition ranking reversal.

## Surviving contribution after Stage 6R2

The only authorized main contribution language is the narrower result-level claim:

> **Allowing firms to strategically re-differentiate after a standards policy can reverse the national-welfare ranking between international standardization and a regional standards union relative to a fixed-position evaluation of the same standards architecture, making the regional union stable through producer-rent gains despite member consumer losses and lower global welfare than under international standardization.**

The central causal comparison is **B-T versus FULL**. `B-EQ` must be acknowledged explicitly. No claim may state that endogenous policy depth itself is necessary for the reversal at the canonical witness.

## Permanently killed novelty claims

No novelty claim is authorized for:

1. government standards policy affecting product differentiation;
2. compatibility/network effects interacting with differentiation;
3. partial compatibility or standards-union stability;
4. continuous compatibility policy;
5. strategic response to interoperability regulation;
6. coalition versus industry-wide interoperability affecting price/welfare;
7. Salop + network effects + compatibility;
8. endogenous positioning under network effects;
9. producer-rent versus consumer-surplus conflict generally;
10. regional standards coalitions;
11. the coalition-level harmonization-depth instrument itself;
12. joint necessity of harmonization-depth endogeneity and product-position endogeneity at the current witness.

Prohibited language includes `first model`, `first paper`, `first to show`, and `novel framework` unless a later audit provides substantially stronger evidence.

## Mathematical status

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

## Required next sequence

1. Refresh manuscript contribution language and benchmark interpretation around the Stage-6R2 surviving claim.
2. Conduct a renewed freeze/full-paper decision if required by the workflow.
3. Rerun **Stage 11R — Repeated Robustness / Referee Attack Gate** against the refreshed manuscript.
4. Stage 12 remains blocked until the repeated referee gate returns `GO TO JOURNAL POSITIONING`.

## Current verdict

**STAGE 6R2 COMPLETE — CONDITIONAL NOVELTY SURVIVAL UNDER A NARROWER RESULT-LEVEL CLAIM.**

Do not modify the repaired v2 model to recover the superseded two-endogeneity narrative.
