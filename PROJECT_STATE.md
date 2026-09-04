# Project State

Last updated: 2026-09-04

## Canonical status

- Project: Endogenous Interoperability and Standards Coalitions
- Last completed stage: Stage 3 Re-entry — C-ESD Endogenous Standard Differentiation × Strategic Product Repositioning
- C-ESD execution status: COMPLETED
- C-ESD report: `reviews/STAGE_03R_CESD_MECHANISM_SEARCH_2026-09-04.md`
- C-ESD canonical verdict: `CONDITIONAL GO`
- Current canonical stage: Stage 3 — Candidate Mechanism Search
- Current route: C1 TERMINATED / C2 TERMINATED / C-RP TERMINATED / C-ESD HELD AT CONDITIONAL GATE
- Stage 4 authorized for C-ESD: NO
- Production manuscript authorized: NO
- Theory frozen: NO
- Target journal: UNRESOLVED

## Canonical workflow reference

- Repository: `ryotamatsuki/research-paper-workflow`
- Version: `v1.1`
- Release SHA: `488e5ab06c207909296a7564eaf9066f7f94319c`
- Stage 3 template: `templates/STAGE_03_MECHANISM_SEARCH.md`
- Stage 4 template: `templates/STAGE_04_MINIMAL_MODEL.md`

## Frozen project boundary

`ryotamatsuki/private-compatibility-standards-coalitions` remains the frozen Stage-8 mandatory benchmark B0 and must not be modified here.

Important correction: B0 does not literally contain a Hotelling/Salop transport parameter `t` or endogenous product locations. C-ESD is therefore currently a structural/institutional extension of B0's IS/SU/SW coalition architecture, not an established algebraic nesting in which `t=bar t` exactly recovers B0.

Stage-2 killed ingredient-level novelty claims remain binding.

## Prior failed mechanisms

### C1 — Coalition-Scope Implementation Crowd-Out

Stage 4 verdict: **NO-GO**.

### C2 — Bilateral Implementation Public-Good / Free-Riding

Stage 3 re-entry verdict: **NO-GO**.

### C-RP — Relative-Profit-Induced Interoperability Restraint

Stage 3 re-entry verdict: **NO-GO**.

Do not repair, combine, or relabel these mechanisms to rescue C-ESD.

## C-ESD candidate identity

C-ESD asks whether the formal standards regime can affect a continuous government-controlled standard-differentiation / interoperability friction and thereby induce firms to reposition horizontally in product space before downstream competition.

Desired loop:

`rho in {IS,SU,SW} -> standard policy -> firm product locations -> prices -> national welfare -> coalition stability`.

`t` is a government standard-induced switching/adaptation/differentiation friction. It is not firm interoperability investment.

`x_i` is firm product location / differentiation.

Relative profit is not part of the core model.

## Stage-3R mathematical findings

### Model A — simple Hotelling without network effects: KILLED

In full-coverage quadratic Hotelling,

`pi1=t(x2-x1)(2+x1+x2)^2/18`.

`t` factors multiplicatively from the location objective. At `x1=a`, `x2=1-a`,

`d pi1/dx1=-t(4a+1)/6<0`.

The location equilibrium is independent of `t`; the desired `t -> x*(t)` feedback does not arise.

### Two-firm Hotelling plus symmetric network effects: KILLED

The exact symmetric own-location gradient remains

`-t(4a+1)/6`.

The network term cancels from the location incentive.

### Three-firm Salop with IS/SU/SW compatibility networks: POSITIVE

Let `r=v/t`. At equal spacing,

- IS member gradient: `0`;
- SW member gradient: `0`;
- SU12 member normalized gradient:

`r(3r-2)(12r-7)/[6(2r-1)(6r-5)^2]`.

On `0<r<1/2`, the SU gradient is strictly negative. The compatible pair has a strict incentive to move apart in product space, unlike symmetric IS/SW.

The normalized SU gradient becomes more negative as `r=v/t` rises, so lower `t` strengthens strategic re-differentiation.

### Anchored Salop witness: POSITIVE BUT SUBSTANTIVE

Preferred regularization uses inherited brand/technology positions `h_i` and redesign cost

`gamma(x_i-h_i)^2/2`.

This is a substantive product-design friction, not a novelty source and not an artificial interiority device.

For `h=(1/6,1/2,5/6)`, `v=0.05`, `gamma=0.5`, SU12 location Nash examples are approximately:

- `t=0.5`: `(0.15597,0.51069,0.83333)`;
- `t=1.0`: `(0.15668,0.50999,0.83333)`;
- `t=2.0`: `(0.15699,0.50968,0.83333)`.

The compatible pair re-differentiates more strongly as `t` falls. IS/SW remain at symmetric anchors in the same diagnostic.

Artifact: `verification/stage03r_cesd_diagnostic.py`.

## Network-effect status

Network effects are necessary for the currently surviving C-ESD diagnostic. The no-network and symmetric two-firm network versions fail.

This does not make `network effects + compatibility` a novelty claim.

## Prior-art status

Severe component overlap:

- Ruiz (2004): government standard recognition followed by endogenous product characteristics and price competition;
- Gandal & Shy (2001): three-country standardization unions, recognition policy, network effects/conversion costs;
- Klimenko (2009): continuous government compatibility policy, network effects and international agreements;
- Baake & Boom (2001): endogenous differentiation plus network externalities and compatibility;
- Wang & Lyu (2020): endogenous horizontal product positioning with network effects and compatibility/differentiation tradeoff;
- Barrett & Yang (2001): international standards, network effects and redesign costs;
- Brekke, Nuscheler & Straume (2006): regulation followed by endogenous spatial location/quality choices.

No audited source in the Stage-3R targeted search directly contains the full `three-country standards partition -> continuous policy depth -> SU-specific product repositioning -> national coalition stability` loop. This is a possible novelty window, not a finding.

## Single unresolved conditional-go requirement

Freeze one economically coherent **policy/benchmark mapping of continuous standard differentiation under IS/SU/SW**.

The unresolved object must jointly specify:

- whether policy is represented by scalar intensity `s`, scalar friction `t`, or a partition-generated pairwise matrix `tau_ij`;
- how the same regime-neutral rule generates within-bloc and cross-bloc frictions;
- who chooses the instrument under SU and whether bloc choice is cooperative or national-government Nash;
- how IS and SW are obtained from the same rule;
- what restriction/removal provides the relevant exogenous-policy/B0-style benchmark.

A single scalar `t_SU` is not sufficient unless it determines both member-member and member-outsider relationships without arbitrary regime-specific primitives.

A candidate family to kill-test, not yet frozen, is

`tau_ij(rho,s)=t_bar-s` for same-bloc pairs,

`tau_ij(rho,s)=t_bar+eta s` for different-bloc pairs.

## C-ESD disposition

**CONDITIONAL GO AT STAGE 3 RE-ENTRY.**

Why it survives:

1. a genuine SU-only strategic repositioning force exists analytically;
2. its strength responds to `t`;
3. an economically interpretable anchored-circle diagnostic gives `dx*/dt != 0`;
4. the mechanism is not present in symmetric IS/SW in the same diagnostic.

Why Stage 4 is not authorized:

1. government policy under SU is not yet uniquely defined;
2. national welfare and coalition deviations therefore cannot yet be audited;
3. a coalition-stability reversal has not been established;
4. B0 is not literally recovered by merely fixing `t`.

## Next action

Remain at Stage 3.

Run one focused architecture-hardening gate on the policy/benchmark mapping only. Do not add relative profit, private implementation, dynamics, topology choice, or additional policy instruments.

If the mapping survives and the FULL interaction produces a government coalition result unavailable from endogenous-policy-only and endogenous-location-only benchmarks, promote C-ESD to Stage 4 Minimal Model.

If the mapping fails, terminate C-ESD.