# Project State

Last updated: 2026-09-04

## Canonical status

- Project: Endogenous Interoperability and Standards Coalitions
- Last completed gate: **Stage 7.5R — Renewed Contribution Freeze Decision**
- Stage-7.5R verdict: **GO TO FULL PAPER**
- Contribution freeze status: **RE-FROZEN — NARROWER CLAIM**
- Production manuscript refresh: **COMPLETE — pending PR/CI integration**
- Production refresh decisions: `decisions/PRODUCTION_MANUSCRIPT_REFRESH_2026-09-04.md`
- Novelty confidence carried forward: **MEDIUM**
- Prior novelty gate: **Stage 6R2 — Post-Repair Novelty Re-Kill — COMPLETE**
- Prior downstream referee gate: **Stage 11R — COMPLETE, but must be repeated on refreshed manuscript**
- Canonical model freeze: `theory/THEORY_FREEZE_CESD_2026-09-04_v2.md`
- Current model-freeze ID: **`CESD-THEORY-FREEZE-2026-09-04-v2`**
- Model primitives under v2: **STILL FROZEN**
- Production manuscript submission-ready: **NO — repeated Stage 11R required**
- Stage 12 journal positioning authorized: **NO**
- Target journal: **UNRESOLVED**

Stage 7.5R re-froze only the contribution. The production manuscript has now been refreshed around that narrower contribution without altering any primitive, timing, policy map, welfare definition, equilibrium concept, canonical witness, or verification chain. The next gate is repeated Stage 11R.

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

## Binding Stage-11R identification correction

Stage 11R introduced hostile benchmark `B-EQ`:

- non-singleton harmonization depths are exogenous;
- they are fixed at the FULL equilibrium values (`s_I=s_SU=s_bar`);
- product locations remain endogenous.

At the canonical witness FULL itself chooses the cap for both IS and SU. Hence `B-EQ` is the same downstream game as FULL and

`Delta_M^(B-EQ)=Delta_M^(FULL)>0`.

Therefore the superseded headline

> policy endogeneity alone and product-position endogeneity alone leave IS stable, while their interaction makes SU stable

is permanently unauthorized. Policy-depth endogeneity is not necessary for the reversal at the witness.

`B-X0` remains an auxiliary zero-additional-harmonization benchmark only.

## Stage-7.5R renewed contribution freeze

### Final verdict

**GO TO FULL PAPER.**

This verdict means full-paper continuation is justified under the narrower contribution. It is not journal-positioning authorization.

### Frozen one-sentence contribution

> **Allowing firms to reposition after a standards policy can reverse the member-country welfare ranking between international standardization and a regional standards union relative to a fixed-position evaluation of the same standards architecture, making the regional union stable through producer-rent gains even though member consumers lose and world welfare remains higher under international standardization.**

### Frozen mechanism

Standards architecture -> changed effective competitive distances -> post-policy product repositioning -> softer competition and member producer-rent gain -> national welfare reversal -> coalition-stability reversal.

Endogenous harmonization-depth choice is not part of the necessary causal chain.

### Central benchmark hierarchy

1. **B-T vs FULL / B-EQ** — central identifying comparison.
2. **B-X0** — auxiliary only.
3. **B-EQ** — mandatory disclosure showing that policy-depth endogeneity is not necessary at the witness.

## Production manuscript refresh — completed content changes

The production branch `stage10r-production-manuscript-refresh` now contains the following repairs:

1. Title changed to `Standards Coalitions and Strategic Product Repositioning`.
2. Abstract rewritten around the Stage-7.5R frozen claim and explicit B-EQ identification correction.
3. Introduction rewritten so the central result is fixed-position B-T versus post-policy repositioning in FULL/B-EQ.
4. Main Results adds B-EQ formally, demotes B-X0 to auxiliary status, and replaces the superseded two-endogeneity interpretation with a constructive post-policy coalition reversal.
5. Related Literature now foregrounds Gandal & Shy (2001), Ruiz (2004), Takarada et al. (2020), Kawabata & Takarada (2021), Klimenko (2009), and the 2025–2026 interoperability frontier.
6. Conclusion explicitly states that endogenous harmonization-depth choice is not necessary for the identified reversal.
7. Bibliography updated for the strengthened closest-paper set.
8. No theory or verified numerical result changed.

## Closest-paper burden retained from Stage 6R2

The refreshed manuscript positions explicitly against:

- Gandal & Shy (2001): three-country standards unions, network effects/conversion costs, national welfare, coalition incentives;
- Ruiz (2004): government standards policy -> endogenous product characteristics -> price competition -> national welfare and excessive differentiation;
- Takarada, Kawabata, Yanase & Kurata (2020): multilateralism versus regionalism, continuous standards, joint regional standards choice, national welfare and blocking;
- Kawabata & Takarada (2021): deep trade agreements and harmonization of standards;
- Huang, Tan, Teh & Zhou (2026): coalitional/industry-wide interoperability, prices and welfare;
- Kretschmer, Rasch, Shekhar & Wenzel (2025): strategic firm response to mandated interoperability.

No setup/ingredient novelty claim is authorized. The surviving distinction is result-level: post-policy horizontal repositioning can reverse the IS/SU member-country ranking relative to fixed product positions and thereby change coalition stability.

## Permanently killed novelty claims

The manuscript must not claim novelty from:

1. government standards policy affecting product differentiation;
2. compatibility/network effects interacting with differentiation;
3. partial compatibility / SU stability;
4. continuous government compatibility policy;
5. strategic firm response to interoperability regulation;
6. coalition versus industry-wide interoperability price/welfare effects;
7. Salop + network effects + compatibility;
8. endogenous product positioning under network effects;
9. producer-rent versus consumer-surplus conflict generally;
10. regional standards coalitions;
11. coalition-level common standards/harmonization intensity;
12. regional standards agreements blocking multilateral standards agreements.

No `first model`, `first paper`, `first to show`, `novel framework`, or equivalent priority language is authorized.

## Assumption boundary after Stage 7.5R

Essential within the verified mechanism:

- post-policy horizontal product repositioning;
- standards-induced changes in competitive distances;
- domestic producer rents in national welfare;
- coalition stability based on member national welfare.

Not established as essential:

- harmonization-depth endogeneity;
- `v>0`;
- the exact cross-bloc `1/2` coefficient;
- the specific harmonization cap.

Normalization / tractability features include the symmetric three-country circular structure, `CS/3` incidence, the exact pairwise friction normalization, and bounded harmonization depth.

No broad generality claim over alternative demand systems, reversed timing, or zero network effects is authorized.

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

## Mathematical / verification status

Theory is unchanged.

Active verification chain:

1. `verification/stage04r_cesd_continuation_repair.py`;
2. `verification/stage07r_cesd_welfare_refresh.py`;
3. `verification/stage11r_cesd_referee_audit.py`;
4. `tests/test_freeze_consistency.py`;
5. `scripts/generate_outputs.py`.

Still limited but disclosed:

- full repaired policy-domain continuation validity is computational at canonical primitives rather than a global analytic theorem;
- exact cross-bloc `1/2` is a stylized normalization;
- `CS/3` is a symmetric-incidence assumption;
- alternative demand geometries and reversed timing are not solved;
- `v=0` mechanism disappearance has not been established;
- the canonical national-welfare reversal is quantitatively small, making parameter-region robustness a key repeated-Stage-11R attack.

## Production authority

Stage 6R2 authority:

1. `reviews/STAGE_06R2_POST_REPAIR_NOVELTY_REKILL_CESD_2026-09-04.md`;
2. `literature/STAGE6R2_CESD_CLOSEST_PAPER_MATRIX.md`;
3. `literature/STAGE6R2_CESD_SEARCH_LOG.md`;
4. `decisions/STAGE6R2_CESD_DECISIONS.md`.

Stage 7.5R authority:

1. `reviews/STAGE_075R_CONTRIBUTION_REFREEZE_CESD_2026-09-04.md`;
2. `decisions/STAGE075R_CESD_DECISIONS.md`.

Production refresh authority:

1. `decisions/PRODUCTION_MANUSCRIPT_REFRESH_2026-09-04.md`;
2. refreshed `paper/main.tex` and manuscript sections;
3. refreshed `references/references.bib`.

## Required next sequence

1. Complete PR/CI verification of the production manuscript refresh.
2. **Repeat Stage 11R hostile referee / robustness gate** on the refreshed manuscript, especially the Ruiz + Gandal–Shy + Takarada synthesis attack, small-reversal/parameter-region robustness, and functional-form dependence.
3. Stage 12 remains blocked until repeated Stage 11R returns `GO TO JOURNAL POSITIONING`.

## Current verdict

**PRODUCTION MANUSCRIPT REFRESH COMPLETE — REPEATED STAGE 11R IS NEXT.**

Theory freeze `CESD-THEORY-FREEZE-2026-09-04-v2` remains unchanged.

Production manuscript is not yet submission-ready because the refreshed wording has not yet passed the repeated Stage 11R referee gate.
