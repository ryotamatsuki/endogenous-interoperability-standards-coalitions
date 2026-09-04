# Project State

Last updated: 2026-09-04

## Canonical status

- Project: Endogenous Interoperability and Standards Coalitions
- Last completed stage: Stage 3 C-ESD Policy-Map Hardening
- Hardening report: `reviews/STAGE_03R_CESD_POLICY_MAP_HARDENING_2026-09-04.md`
- Policy-map source of truth: `model/STAGE3R_CESD_POLICY_MAP.md`
- Hardening decisions: `decisions/STAGE3R_CESD_POLICY_MAP_DECISIONS.md`
- C-ESD canonical verdict: `GO -> GO TO STAGE 4 MINIMAL MODEL`
- Current canonical stage: **Stage 4 — Minimal Model**
- Current route: C1 TERMINATED / C2 TERMINATED / C-RP TERMINATED / C-ESD SELECTED FOR STAGE 4
- Stage 4 authorized for C-ESD: YES
- Production manuscript authorized: NO
- Theory frozen: NO
- Target journal: UNRESOLVED

## Canonical workflow

- Repository: `ryotamatsuki/research-paper-workflow`
- Version: `v1.1`
- Release SHA: `488e5ab06c207909296a7564eaf9066f7f94319c`
- Stage 4 template: `templates/STAGE_04_MINIMAL_MODEL.md`

## Frozen project boundary

`ryotamatsuki/private-compatibility-standards-coalitions` remains the frozen Stage-8 mandatory institutional/coalition benchmark B0 and must not be modified.

C-ESD is not currently claimed to algebraically nest B0. B0 has different demand primitives, conversion cost `c`, network value and binary private adoption cost `F`.

## C-ESD selected mechanism

C-ESD — **Endogenous Standard Differentiation × Strategic Product Repositioning**.

Frozen feedback:

`rho -> standards-bloc depth choices s_C -> pairwise standard frictions Tau(rho,s) -> firm product locations x_i -> downstream prices -> national welfare -> coalition stability`.

The government policy variable is not private interoperability investment.

Relative profit is excluded from the Stage-4 baseline.

## Stage-3 firm-side findings that remain binding

### Simple Hotelling: killed

In full-coverage quadratic Hotelling,

`pi1=t(x2-x1)(2+x1+x2)^2/18`,

so the common transport coefficient factors out of the location objective. Firm location best responses are independent of `t`.

A symmetric two-firm network extension also fails to create `dx*/dt != 0`.

### Three-firm Salop SU asymmetry: positive

With the Stage-3 compatibility network and `r=v/t`, equal spacing has zero unilateral location gradient under IS and SW. Under `SU_12`, the member gradient is

`r(3r-2)(12r-7)/[6(2r-1)(6r-5)^2] < 0`

for `0<r<1/2`.

Lower standard friction therefore strengthens SU-member strategic re-differentiation.

Anchored Salop diagnostics with substantive redesign cost also produced `dx*/dt != 0` under SU.

## Frozen policy-depth object

For each formal standards bloc `C in rho`, choose

`s_C in [0,s_bar]`, with `s_bar<t_bar`.

Interpret `s_C` as the coherence/specificity depth of bloc C's standard.

The realized standard-induced friction is pairwise.

### Same bloc

If `i,j in C`,

`tau_ij=t_bar-s_C`.

### Different blocs

If `i in C`, `j in D`, `C != D`,

`tau_ij=t_bar+(s_C+s_D)/2`.

The mapping is label-invariant and common to IS, SU and SW.

## Explicit regime maps

### IS

One bloc `{1,2,3}` chooses `s_I`:

`tau_12=tau_13=tau_23=t_bar-s_I`.

### SU_12

Bloc `{1,2}` chooses `s_12`; singleton `{3}` chooses `s_3`:

`tau_12=t_bar-s_12`,

`tau_13=tau_23=t_bar+(s_12+s_3)/2`.

Thus deeper SU integration makes member standards closer while making the member-outsider boundaries more differentiated.

Holding `s_3=0`,

`tau_12+tau_13+tau_23=3 t_bar`.

Hence the SU member-bloc depth margin redistributes pairwise standard differentiation rather than mechanically changing its mean.

### SW

Three singleton governments choose `s_1,s_2,s_3`:

`tau_12=t_bar+(s_1+s_2)/2`,

`tau_13=t_bar+(s_1+s_3)/2`,

`tau_23=t_bar+(s_2+s_3)/2`.

## Why the cross coefficient is fixed at 1/2

The Stage-4 baseline does not contain a free external-discrimination parameter.

Under `SU_12`, increasing `s_12` lowers one internal pair friction with derivative `-1` and raises two cross-bloc pair frictions symmetrically. Requiring the member-bloc depth margin by itself to preserve mean pairwise friction gives

`-1+2 lambda=0`,

so

`lambda=1/2`.

A generalized lambda may be considered only as later robustness if the baseline survives.

## Government / bloc policy game

After formal partition `rho` is fixed, all standards blocs choose their depths simultaneously.

Bloc `C` maximizes

`Omega_C=sum_{i in C} W_i`.

Therefore the policy-depth equilibrium is a Nash equilibrium among formal standards blocs.

- IS: the three-country bloc chooses `s_I`;
- SU_12: bloc `{1,2}` chooses `s_12`; singleton `{3}` chooses `s_3`;
- SW: each singleton government chooses `s_i`.

In the symmetric baseline, members of a multi-country bloc have identical continuation welfare, so bloc-sum maximization is equivalent to representative-member welfare maximization. No transfers or bargaining weights are introduced.

## Network-effect freeze

Formal partition determines the compatibility network as in the Stage-3 Salop diagnostic.

The network coefficient `v` is held fixed with respect to `s_C` during Stage 4.

Do not make network intensity another continuous policy channel during Stage 4.

## Policy cost freeze

Do not add a direct convex government policy cost merely to generate an interior `s_C`.

Boundary depth equilibria are admissible.

## National welfare

Retain

`W_i=CS_i+Pi_i`,

with foreign-firm profits excluded from national welfare.

Stage 4 must fully microfound national consumer surplus and worldwide domestic-firm profit under the selected Salop implementation before any coalition-stability theorem is certified.

## Stage-4 timing

`rho -> s*(rho) -> x*(rho,s*) -> p*(rho,s*,x*) -> W_i -> coalition stability`.

## Required Stage-4 benchmarks

### B-EXO / B-X

All `s_C=0`; firms choose locations; then price competition.

### B-T

Blocs choose `s_C`; product locations are fixed at inherited anchors; then price competition.

### FULL

Blocs choose `s_C`; firms choose locations; then price competition.

The FULL architecture qualifies only if endogenous policy × endogenous product repositioning generates a government-welfare or coalition-stability implication unavailable in B-T and B-X separately.

## Stage-4 mandatory kill tests

Stage 4 must verify:

1. downstream price equilibrium;
2. full market coverage / demand positivity and any required participation conditions;
3. location best responses, SOC/global optimum, ordering changes and corners;
4. policy-depth best responses and boundary solutions;
5. existence and uniqueness/multiplicity of the bloc-depth equilibrium;
6. consumer surplus and national welfare microfoundation;
7. IS/SU/SW continuation values;
8. coalition blocking/deviation conditions;
9. B-T vs B-X vs FULL decomposition;
10. whether any stability reversal is structural rather than an artifact of the redesign cost or boundary restriction.

## Stage-4 no-hybridization rule

Do not add:

- relative-profit objectives;
- private interoperability investment;
- endogenous network intensity;
- extra policy costs;
- lobbying;
- transfers;
- dynamics;
- topology choice;
- additional countries.

If the frozen C-ESD model fails the Stage-4 theorem test, return `NO-GO` rather than modifying the mechanism silently.

## Next action

Execute **Stage 4 — Minimal Model** for the frozen C-ESD architecture.
