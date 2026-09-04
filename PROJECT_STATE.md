# Project State

Last updated: 2026-09-04

## Canonical status

- Project: Endogenous Interoperability and Standards Coalitions
- Last completed stage: Stage 3 Re-entry — C2 Bilateral Implementation Public-Good / Free-Riding
- C2 re-entry execution status: COMPLETED
- C2 report: `reviews/STAGE_03R_C2_REEVALUATION_2026-09-04.md`
- C2 canonical verdict: `NO-GO`
- Current canonical stage: Stage 3 — Candidate Mechanism Search
- Current route: theory candidate — C1 TERMINATED / C2 TERMINATED / DISTINCT MECHANISM REQUIRED
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

This project remains independent from `private-compatibility-standards-coalitions`. That paper remains benchmark B0 and must not be modified here.

## Stage-2 restrictions remain binding

No future pivot may claim novelty from continuous compatibility, interiority, network effects plus compatibility, downstream competition after compatibility, private/social compatibility wedges, standards coalition formation, government standardization unions, government compatibility policy/international coordination, coalition-proof partial compatibility, or pairwise/weighted interoperability by themselves.

## C1 disposition — binding

C1 — Coalition-Scope Implementation Crowd-Out (CSIC) — failed Stage 4 and is **TERMINATED / NO-GO**.

The frozen one-sided demand generated `a_IS*>=a_SU*`, lacked the intended competition-exposure channel, failed the off-equilibrium consumer-surplus microfoundation, and produced only a mechanical cost-bearing benchmark reversal.

Do not repair or reuse C1 silently.

## C2 re-entry question

C2 asked whether bilateral post-agreement implementation creates a public-good/free-riding problem strong enough to make regime-specific private interoperability reverse government coalition stability.

Core loop tested:

`rho -> bilateral contribution game -> effective interoperability -> product competition -> national welfare -> stability`.

## C2 technology audit

### Classic max/min routes

- `A_ij=max{a_i,a_j}`: unilateral/no-veto converter provision; heavily exposed to de Palma–Leruth–Regibeau and Garcia–Vergari.
- `A_ij=min{a_i,a_j}` or product analogues: mutual-veto / weakest-link coordination rather than pure free-riding; also heavily exposed to the consensus/veto literature.

Neither is promoted.

### Independent pairwise contributions

With identical independent links and no common capacity/scope cost, a given pair solves the same implementation game under IS and SU. Coalition size changes the number of links but not per-link implementation intensity. This does not supply the required regime-dependent intensive continuation feedback.

### Standard coalition-wide public good

For `pi_i=B(G)-c(e_i)`, `G=sum e_i`, with `B''<=0` and `c''>0`, symmetric aggregate provision satisfies

`dG_n/dn>0`.

Ordinary free-riding can lower individual effort but does not by itself make effective aggregate implementation fall when coalition size increases.

## Strongest pure-C2 diagnostic

The most defensible smooth bilateral substitute-contribution technology is

`A_ij=a_i+a_j-a_i a_j`.

It has symmetric bilateral effects and repairs C1's integrability problem:

`partial p_i/partial q_j=partial p_j/partial q_i=-1+vA_ij`.

Using B0-style Cournot inverse demand

`p_i=1-Q+v sum_{j in C_i(rho),j!=i}A_ij q_j`,

and `kappa a_i^2/2`, define at symmetric member implementation `a`

`x=v(2a-a^2)`.

Exact private marginal operating-profit returns are

`MB_I(a)=3v(1-a)/[(1+x)(2-x)^3]`,

`MB_U(a)=3v(1-a)/[2(2-x)^3]`.

Therefore

`MB_I/MB_U=2/(1+x)`.

On the regular weak-network domain `0<v<=1/4`, `x<=1/4`, so

`MB_I/MB_U>=8/5>1`.

The natural smooth bilateral free-riding model therefore gives a stronger implementation incentive under three-country IS than under two-country SU, not a larger-coalition implementation collapse.

## C2 numerical diagnostic

Artifact: `verification/stage03r_c2_diagnostic.py`.

6,000 points over

- `v in [0.005,0.25]`;
- `kappa in [10^-3,10]`.

Results:

- `a_IS<a_SU`: 0;
- `Delta_3^endo<0`: 0;
- sign reversal against costless/exogenous full interoperability: 0.

This is diagnostic rather than a global impossibility proof, but it provides no positive signal sufficient for Stage 4.

## C2 disposition

**C2 — Bilateral Implementation Public-Good / Free-Riding: TERMINATED / NO-GO AT STAGE 3 RE-ENTRY.**

Reasons:

1. its primitive converter/consensus technologies are already well occupied;
2. independent bilateral links do not create the required coalition-size intensive feedback;
3. standard public-good free-riding does not make aggregate implementation decline with group size under standard assumptions;
4. the strongest natural smooth bilateral technology gives implementation crowd-in and no stability reversal in the audited regular domain;
5. variants that can force the desired sign require a new mechanism such as dilution, common capacity/scope costs, or coalition-wide shared infrastructure.

Do not proceed to Stage 4 on C2.

## Potential distinct mechanism identified but not selected

A **common interoperability infrastructure / shared gateway** contribution game is conceptually distinct from bilateral C2. A coalition-wide technology such as `A_C=1-product_i(1-a_i)` can generate stronger contribution substitution and may produce different coalition-size behavior, but one member's effort then improves a shared coalition artifact rather than a bilateral endpoint relationship.

This must be treated as a new Stage-3 candidate and compared against C3 rather than silently relabeled as C2.

## Next action

Remain at Stage 3.

If the project continues, run a fresh candidate comparison among at least:

- C3 — national-incidence / cross-border rent-shifting;
- common interoperability infrastructure / shared gateway contribution;
- any other genuinely distinct mechanism surviving Stage-2 prior-art constraints.

Do not automatically promote C3 and do not combine mechanisms before selection.
