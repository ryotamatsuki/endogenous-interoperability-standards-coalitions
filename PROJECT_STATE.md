# Project State

Last updated: 2026-09-04

## Canonical status

- Project: Endogenous Interoperability and Standards Coalitions
- Last completed stage: **Stage 7 — Welfare / Generality**
- Stage-7 report: `reviews/STAGE_07_WELFARE_GENERALITY_CESD_2026-09-04.md`
- Stage-7 institutional validation: `literature/STAGE7_CESD_INSTITUTIONAL_VALIDATION.md`
- Stage-7 verification: `verification/stage07_cesd_welfare_generality.py`
- Stage-7 decisions: `decisions/STAGE7_CESD_DECISIONS.md`
- C-ESD canonical verdict: **GO TO STAGE 7.5**
- Current canonical stage: **Stage 7.5 — Freeze Decision**
- Current route: C1 TERMINATED / C2 TERMINATED / C-RP TERMINATED / C-ESD SURVIVED STAGE 7
- Production manuscript authorized: NO
- Theory frozen: NO
- Target journal: UNRESOLVED

## Canonical workflow

- Repository: `ryotamatsuki/research-paper-workflow`
- Version: `v1.1`
- Release SHA: `488e5ab06c207909296a7564eaf9066f7f94319c`
- Stage-7 template: `templates/STAGE_07_WELFARE_GENERALITY.md`
- Stage-7 route on GO: Stage 7.5 — Freeze Decision

## Frozen project boundary

`ryotamatsuki/private-compatibility-standards-coalitions` remains the frozen Stage-8 mandatory institutional/coalition benchmark B0 and must not be modified.

C-ESD does not algebraically nest B0. B0 remains an institutional IS/SU/SW coalition benchmark only.

## Frozen C-ESD game

C-ESD — **Endogenous Standard Differentiation × Strategic Product Repositioning**.

Timing:

`rho -> bloc depths s_C -> pairwise Tau(rho,s) -> product locations x_i -> prices -> W_i -> coalition stability`.

Policy map:

- same bloc `C`: `tau_ij=t_bar-s_C`;
- different blocs `C,D`: `tau_ij=t_bar+(s_C+s_D)/2`;
- bloc `C` maximizes `sum_{i in C} W_i`; blocs choose simultaneously.

Formal partition determines the compatibility network; network coefficient `v` is fixed with respect to depth. No direct policy cost exists.

Consumers are uniform on a unit Salop circle and each country owns one third of consumer mass. Firm redesign/repositioning cost in the baseline is

`gamma d_c(x_i,h_i)^2/2`,

with anchors `h=(1/6,1/2,5/6)`.

## Stage-6 surviving main contribution

Only the following novelty claim remains authorized:

> **Interaction-induced coalition-stability reversal.** Endogenous government standard depth and endogenous firm product positioning each separately leave international standardization stable, but together induce regional-standardization members to re-differentiate enough to reverse their national-welfare ranking and destabilize international standardization in favor of regional standards unions.

At the canonical witness:

`Delta_M^(B-T)=-0.010167`,

`Delta_M^(B-X)=-0.000434`,

`Delta_M^(FULL)=+0.001571`.

## Stage-7 welfare decomposition

Exact national member condition:

`Delta_M = Delta Pi_M + Delta CS/3`.

At `(t_bar,v,gamma,s_bar)=(1,0.04,0.11,0.25)`:

- `Delta CS/3=-0.0325785`;
- `Delta Pi_M=+0.0341498`;
- `Delta_M=+0.0015713`.

Thus the coalition reversal is a domestic-producer-rent effect that narrowly outweighs the member consumer loss.

## Stage-7 global welfare result

Exact global identity:

`GW=A+v q'Gq-TC-sum_i C_i^D`.

Price payments cancel globally as transfers.

At the witness:

- `GW_IS=-0.0225000`;
- `GW_SU=-0.0586685`;
- `GW_SW=-0.0700000`.

Hence the decentralized stable SU set is globally welfare-inferior to IS in the canonical region.

## Stage-7 private/social location wedge

At fixed canonical SU policy `(s_12,s_3)=(0.25,0)`:

- inherited member distance: `0.333333`;
- constrained social-location distance: `0.431427`;
- private equilibrium member distance: `0.497533`.

Firms therefore over-re-differentiate relative to the constrained social benchmark.

## Stage-7 generality condition

The quadratic redesign cost provides tractability but is not the conceptual source of the mechanism. For a regular convex repositioning cost, the Stage-3 SU marginal operating-profit force produces positive re-differentiation when `C'(0)=0` and local curvature is finite.

The reversal requires an intermediate effective adjustment-cost curvature:

1. too high -> repositioning too weak -> `Delta_M<0`;
2. intermediate -> domestic rent gain exceeds member CS loss -> `Delta_M>0`;
3. too low -> global location jumps can invalidate the selected branch.

For `v=0.04,s_bar=0.25`, the upper welfare threshold is

`gamma_W=0.132983`,

while the audited global-best-response transition is around `gamma≈0.10`.

## Institutional validation

Primary-source analogues:

- EU AFIR EV-charging rules: policy-controlled technical interoperability margin — **ESTABLISHED**; strategic product repositioning — **UNVERIFIED**.
- EU DMA Article 7 messaging interoperability: technical interoperability interfaces — **ESTABLISHED**; strategic non-interface repositioning — **UNVERIFIED**.
- EU common-charger rules: common USB-C interface — **ESTABLISHED**; post-standardization re-differentiation — **UNVERIFIED**.

These sources support theoretical plausibility, not empirical proof of the C-ESD response.

## Stage-6 killed claims remain dead

Do not claim novelty from:

- government standards policy affecting product characteristics;
- continuous government compatibility policy;
- Salop + network effects + compatibility;
- partial compatibility / SU stability itself;
- strategic response to interoperability in a broad sense;
- coalitional interoperability price/welfare effects.

## Stage-7 verdict

**GO TO STAGE 7.5.**

## Next action

Execute **Stage 7.5 — Freeze Decision**.

Stage 7.5 may not add extensions. It must decide whether the surviving theorem/welfare package is sufficiently sharp to freeze for theory development and later manuscript investment.