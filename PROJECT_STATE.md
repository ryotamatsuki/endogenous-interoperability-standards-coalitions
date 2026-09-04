# Project State

Last updated: 2026-09-04

## Canonical status

- Project: Endogenous Interoperability and Standards Coalitions
- Last completed supplementary gate: **Stage 6R2 — Post-Repair Novelty Re-Kill**
- Stage-6R2 report: `reviews/STAGE_06R2_POST_REPAIR_NOVELTY_REKILL_CESD_2026-09-04.md`
- Stage-6R2 matrix: `literature/STAGE6R2_CESD_CLOSEST_PAPER_MATRIX.md`
- Stage-6R2 search log: `literature/STAGE6R2_CESD_SEARCH_LOG.md`
- Stage-6R2 decisions: `decisions/STAGE6R2_CESD_DECISIONS.md`
- Stage-6R2 verdict: **CONDITIONAL GO — NARROWER CLAIM REQUIRED**
- Stage-6R2 novelty confidence: **MEDIUM**
- Prior downstream gate: **Stage 11R — Repeated Robustness / Referee Attack Gate — COMPLETE**
- Stage-11R report: `reviews/STAGE_11R_REFEREE_GATE_CESD_2026-09-04.md`
- Stage-11R decisions: `decisions/STAGE11R_CESD_DECISIONS.md`
- Canonical model freeze: `theory/THEORY_FREEZE_CESD_2026-09-04_v2.md`
- Current model-freeze ID: **`CESD-THEORY-FREEZE-2026-09-04-v2`**
- Model primitives under v2: **STILL FROZEN**
- Main-contribution freeze under v2: **SUSPENDED — MUST BE RE-FROZEN AROUND NARROWER CLAIM**
- Production manuscript submission-ready: **NO**
- Stage 12 journal positioning authorized: **NO**
- Target journal: **UNRESOLVED**

Stage 6R2 does not roll back or invalidate the fact that Stage 11R was completed. It resolves the novelty re-kill that Stage 11R itself required. Because Stage 11R identified a benchmark-identification failure in the old contribution label, the next action is contribution re-freeze/manuscript refresh followed by a **repeated referee gate**; Stage 11R cannot simply be treated as passed under the old wording.

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

Stage 11R introduced a hostile benchmark `B-EQ`:

- non-singleton harmonization depths are **exogenous**;
- they are fixed at the FULL equilibrium values (`s_I=s_SU=s_bar`);
- product locations remain endogenous.

Because FULL itself chooses the cap for both IS and SU, `B-EQ` is exactly the same downstream game as FULL at the canonical witness.

Therefore:

`Delta_M^(B-EQ)=Delta_M^(FULL)>0`.

Canonical diagnostic: `verification/stage11r_cesd_referee_audit.py`.

### Binding implication

The superseded headline

> policy endogeneity alone and product-position endogeneity alone leave IS stable, while their interaction makes SU stable

is **not identified by the canonical witness**. Policy endogeneity is not necessary for the reversal because exogenously fixing policy at the FULL equilibrium depth reproduces FULL.

`B-X0` remains a legitimate zero-harmonization benchmark, but it cannot establish necessity of policy endogeneity.

## Stage-6R2 novelty result

### Final verdict

**CONDITIONAL GO — NARROWER CLAIM REQUIRED.**

**Novelty confidence: MEDIUM.**

No directly absorbing result was located in the audited search through 2026-09-04. This is an audited-search conclusion, not a priority proof.

### Surviving result-level contribution

> **Policy-induced strategic re-differentiation coalition-stability reversal.** There exists a regular parameter region in which a regional harmonization policy that is not preferred to international standardization when product positions are fixed becomes nationally preferred once firms can reposition after the same standards architecture, because member re-differentiation raises domestic producer rents enough to overturn the IS–SU welfare ranking and stabilize the regional standards union.

The central identifying comparison is **B-T versus FULL / B-EQ at the witness**.

`B-X0` is auxiliary. `B-EQ` must be explicitly acknowledged in any contribution statement so the paper does not overclaim policy-endogeneity necessity.

## Stage-6R2 closest-paper findings

### Strongest strategic-timing threat

**Ruiz (2004), *Mix-and-Match and International Standardization Policy*.**

Ruiz already has government standards recognition -> endogenous product characteristics -> price competition -> national welfare and finds excessive strategic differentiation. It therefore kills broad timing/ingredient novelty. Its endogenous-characteristics extension nevertheless preserves the qualitative government-policy equilibrium rather than delivering the C-ESD regional/international coalition-ranking reversal.

### Strongest institutional/network threat

**Gandal & Shy (2001), *Standardization Policy and International Trade*.**

It already has three countries, standardization unions, network effects/conversion costs, national welfare and participation incentives. It lacks post-policy endogenous product repositioning.

### Strongest post-Stage-4R repaired-instrument/stability threat

**Takarada, Kawabata, Yanase & Kurata (2020), *Standards Policy and International Trade: Multilateralism versus Regionalism*.**

This newly elevated closest paper already has three countries, continuous standards, regional and multilateral harmonization, joint regional standard choice, national welfare, and core/blocking. A regional standards agreement can be the only regime in the core while the world-welfare-maximizing multilateral agreement is blocked.

Therefore coalition-level common harmonization and regional-versus-multilateral standards stability are not setup novelty.

Also important:

- Kawabata & Takarada (2021), *Deep Trade Agreements and Harmonization of Standards*;
- Stadler, Trexler & Unsorg (2022), *The Perpetual Trouble with Network Products Why IT Firms Choose Partial Compatibility*.

### 2024–2026 frontier

**Huang, Tan, Teh & Zhou (2026), *A Network Approach to Interoperability*** is the strongest current interoperability-network/welfare paper. It studies weighted industry-wide and coalitional interoperability, prices and welfare, but its current paper explicitly leaves endogenous formation of interoperability coalitions for future research and contains no post-policy horizontal product-positioning stage or national-government IS/SU stability.

**Kretschmer, Rasch, Shekhar & Wenzel (2025), *Strategic Response to Mandated Interoperability*** kills generic strategic-response novelty but studies data collection/privacy spillovers rather than product-space repositioning or standards-coalition stability.

No 2024–2026 direct absorber was located.

## Ruiz + Gandal–Shy synthesis status

The synthesis attack is serious and must remain explicit:

- Gandal–Shy supplies the three-country standards-union/network/national-welfare architecture;
- Ruiz supplies government policy -> endogenous horizontal characteristics -> price competition and excessive differentiation.

This makes the combined setup unsurprising.

However, the surviving result is not an immediate corollary of their propositions. Ruiz itself reports qualitative policy robustness after endogenizing product characteristics, while Gandal–Shy contains no post-policy repositioning stage. Obtaining the C-ESD result requires solving the new continuation and showing that policy-induced member re-differentiation raises domestic producer rents enough to cross the IS/SU national-welfare/blocking threshold.

Composite classification: **STRUCTURALLY VERY CLOSE**, not `ABSORBS` or `NEAR-ABSORBS` under the canonical result-level rule.

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

No `first model`, `first paper`, `first to show`, or `novel framework` wording is authorized.

## Assumption-driven-result boundary

The exact cross-bloc `1/2` coefficient remains a stylized normalization.

The strongest defense against “the friction map mechanically creates the result” is that `B-T` uses the same map but yields `Delta_M<0`. Thus the map alone does not mechanically select SU.

However:

- `B-X0` cannot prove policy endogeneity is necessary;
- `B-EQ` reproduces FULL;
- the current verification chain does **not** establish that the mechanism disappears at `v=0`.

Therefore a no-network disappearance claim is not authorized.

## Mathematical status after Stage 6R2

The theory is unchanged. Stage 6R2 is a novelty/identification gate only.

Resolved and still authoritative:

- v1 singleton-depth/off-path continuation defect;
- canonical whole-circle location-best-response concern;
- price equilibrium/concavity block;
- welfare identities and world-welfare normalization;
- Stage-11R `B-EQ` identification correction.

Still limited but disclosed:

- full repaired policy-domain continuation validity is computational at canonical primitives rather than a global analytic theorem;
- the exact cross-bloc `1/2` coefficient is a stylized normalization;
- `CS/3` is a symmetric-incidence assumption;
- alternative demand geometries and reversed timing are not solved;
- `v=0` mechanism disappearance has not been established.

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

Literature/decision authority added by Stage 6R2:

1. `reviews/STAGE_06R2_POST_REPAIR_NOVELTY_REKILL_CESD_2026-09-04.md`;
2. `literature/STAGE6R2_CESD_CLOSEST_PAPER_MATRIX.md`;
3. `literature/STAGE6R2_CESD_SEARCH_LOG.md`;
4. `decisions/STAGE6R2_CESD_DECISIONS.md`.

## Required next sequence

1. **Re-freeze the main contribution** around the narrower Stage-6R2 result without changing the v2 theory.
2. **Refresh the production manuscript** contribution/novelty language and benchmark discussion, explicitly acknowledging `B-EQ` and adding Takarada et al. (2020) / Kawabata & Takarada (2021) to the closest literature.
3. **Repeat the referee/robustness gate** on the narrowed claim.
4. Stage 12 remains blocked until the repeated gate returns `GO TO JOURNAL POSITIONING`.

## Current verdict

**STAGE 6R2 COMPLETE — NOVELTY SURVIVES ONLY IN A NARROWER FORM.**

**CONDITIONAL GO — NARROWER CLAIM REQUIRED; NOVELTY CONFIDENCE MEDIUM.**

Do not change the repaired v2 model. Do not restore the superseded two-endogeneity narrative. The next work is contribution re-freeze and manuscript positioning repair, followed by a repeated referee gate.