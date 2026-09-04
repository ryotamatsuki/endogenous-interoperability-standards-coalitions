# Project State

Last updated: 2026-09-04

## Canonical status

- Project: Endogenous Interoperability and Standards Coalitions
- Last completed stage: **Stage 11 — Robustness / Referee Attack Gate**
- Stage-11 report: `reviews/STAGE_11_REFEREE_GATE_CESD_2026-09-04.md`
- Stage-11 decisions: `decisions/STAGE11_CESD_DECISIONS.md`
- Stage-10 manuscript merge reviewed: `bcad75cdc1e87c54cd2ecfd73559a1e6c96d4c68`
- Historical freeze specification: `theory/THEORY_FREEZE_CESD_2026-09-04.md`
- Historical freeze ID: `CESD-THEORY-FREEZE-2026-09-04-v1`
- Stage-11 verdict: **REOPEN EARLIER STAGE — STAGE 4R CONTINUATION-EXISTENCE / POLICY-STAGE REPAIR**
- Current canonical stage: **Stage 4R — Continuation-Existence / Policy-Stage Repair**
- Core C-ESD mechanism: **SURVIVES PROVISIONALLY**
- Historical theory freeze: **SUSPENDED pending repair and re-freeze**
- Production manuscript submission-ready: **NO**
- Stage 12 journal positioning authorized: **NO**
- Target journal: **UNRESOLVED pending repeated Stage 11**

## Canonical workflow

- Repository: `ryotamatsuki/research-paper-workflow`
- Version: `v1.1`
- Release SHA: `488e5ab06c207909296a7564eaf9066f7f94319c`
- Stage-11 template: `templates/STAGE_11_REFEREE_GATE.md`
- Stage-11 checklist: `checklists/REFEREE_ATTACK_CHECKLIST.md`

## Project boundary

`ryotamatsuki/private-compatibility-standards-coalitions` remains the frozen institutional IS/SU/SW benchmark B0 and must not be modified.

C-ESD does not algebraically nest B0. B0 is an institutional/coalition benchmark only.

## Historical frozen game under repair

Timing:

`rho -> bloc depths s_C -> pairwise Tau(rho,s) -> product locations x_i -> prices -> W_i -> coalition stability`.

Policy map:

- same bloc `C`: `tau_ij=t_bar-s_C`;
- different blocs `C,D`: `tau_ij=t_bar+(s_C+s_D)/2`;
- bloc `C` maximizes `sum_{i in C} W_i`;
- standards blocs choose depths simultaneously.

Formal partition determines the compatibility graph. Firms choose costly horizontal product repositioning on a unit Salop circle after observing policy depth. National welfare is `W_i=CS/3+Pi_i`. Coalition stability uses strict-blocking exclusive-membership logic.

No new primitive is authorized during Stage 4R unless formal theory-change control is triggered.

## Main contribution candidate under repair

The project continues to target only the interaction-induced coalition-stability reversal:

`Delta_M^(B-T)<0`,

`Delta_M^(B-X)<0`,

`Delta_M^(FULL)>0`.

At the historical Stage-8 witness `(t_bar,v,gamma,s_bar)=(1,0.04,0.11,0.25)` the on-path signs were:

- `Delta_M^(B-T)=-0.010167`;
- `Delta_M^(B-X)=-0.000434`;
- `Delta_M^(FULL)=+0.001571`.

The canonical on-path FULL SU location equilibrium survives a stronger Stage-11 interval-wise continuous whole-circle unilateral-best-response audit.

However, these historical values are **not currently submission-authoritative** because the Stage-11 policy-continuation audit exposed an off-path SPNE gap.

## Stage-11 blocking mathematical finding

The historical Stage-4 policy routine evaluates depth deviations through a fixed-order `loc_nash` candidate before checking whether that candidate is a global location Nash equilibrium.

At the historical primitives with `s_12=0.25`, outsider-depth deviations sufficiently above roughly `s_3≈0.143` leave the selected regular location branch. At the explicit off-path policy profile

`(s_12,s_3)=(0.25,0.20)`,

the fixed-order continuation admits a profitable order-changing location deviation. The Stage-11 audit also finds no alternative regular **interior pure** location Nash candidate across all cyclic orders and circular-anchor branches at that profile.

Therefore the continuation-value map required to prove a pure-strategy SPNE is not established on the full historical policy action set. Stage 12 is blocked.

Canonical Stage-11 diagnostic:

- `verification/stage11_cesd_referee_audit.py`.

## Bounded repair lead — not yet frozen

A preliminary Stage-11 repair diagnostic keeps `t_bar=1`, `v=0.04`, `gamma=0.11` and reduces the policy cap to `s_bar=0.20`.

It preserves the desired signs approximately:

- `Delta_M^(B-T)≈-0.008984`;
- `Delta_M^(B-X)≈-0.000434`;
- `Delta_M^(FULL)≈+0.001049`.

The selected SU policy is again `(s_12,s_3)=(s_bar,0)`. A dense 21×21 audit of the SU policy square `[0,0.20]^2` found no selected-branch whole-circle continuation failure.

This is only a **repair candidate**. Stage 4R must derive or otherwise justify a continuation-regularity restriction independently of the desired welfare sign; `s_bar=0.20` may not be adopted merely because it restores the result.

## Stage 4R mandatory contract

Stage 4R must, without changing the core mechanism:

1. construct a continuation-value map that uses only actual downstream location-price equilibria after every feasible policy deviation;
2. establish a defensible sufficient policy-domain/regularity restriction, or explicitly solve the problematic off-path continuations;
3. re-solve IS, SU and SW policy-stage Nash equilibria with global best responses, corners/KKT and multiplicity checks;
4. continuously audit whole-circle location best responses, not only coarse grids;
5. re-test `Delta_M^(B-T)<0`, `Delta_M^(B-X)<0`, `Delta_M^(FULL)>0`;
6. document existence/uniqueness/selection of continuation equilibria sufficiently to support the claimed solution concept.

Preferred first route: test whether a principled upper bound on `s_bar` can guarantee the regular pure continuation domain while preserving the mechanism.

## Other Stage-11 attacks retained for later response

- Ruiz (2004) + Gandal–Shy (2001) remains the strongest novelty synthesis attack; only the result-level FULL-only reversal survives provisionally.
- The `1/2` cross-bloc coefficient is a normalization and must not be sold as a primitive empirical fact.
- Formal regime membership fixes the network graph while depth changes `Tau`; `s=0` therefore means zero *additional depth*, not zero compatibility.
- `CS/3` is a transparent symmetry device and an external-validity limitation.
- Institutional examples validate policy-controlled interface standards, not the exact cross-bloc derivative or observed strategic re-differentiation.
- Reported CS/world-welfare levels should be labeled net of the common baseline utility `A`.
- IJIO-level fit is unresolved until the mathematics is repaired and Stage 11 is passed again.

## Affected-stage routing after Stage 4R

If Stage 4R passes and changes the canonical cap/witness or regularity domain, rerun at least:

1. Stage 7 — Welfare / Generality;
2. Stage 8 — Theory Freeze;
3. Stage 9 — Repository / Reproducibility Setup;
4. Stage 10 — Section-by-Section Paper Construction;
5. Stage 11 — Robustness / Referee Attack Gate.

Stage 6 novelty re-kill need not be repeated for a pure regularity/cap repair unless the economic mechanism or surviving contribution changes.

## Current verdict

**REOPEN EARLIER STAGE — STAGE 4R CONTINUATION-EXISTENCE / POLICY-STAGE REPAIR.**

This is not a project NO-GO. The core interaction survives provisionally, and Stage-11 diagnostics show a plausible bounded repair. But the existing manuscript is not submission-ready because the claimed SPNE is not established over the full historical policy action set.

## Next action

Execute Stage 4R exactly under the mandatory contract above. Do not proceed to Stage 12 until a repeated Stage 11 returns `GO TO JOURNAL POSITIONING`.
