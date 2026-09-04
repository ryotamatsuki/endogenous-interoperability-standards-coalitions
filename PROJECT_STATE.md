# Project State

Last updated: 2026-09-04

## Canonical status

- Project: Endogenous Interoperability and Standards Coalitions
- Last completed stage: Stage 3 Re-entry — C-RP Relative-Profit-Induced Interoperability Restraint
- C-RP execution status: COMPLETED
- C-RP report: `reviews/STAGE_03R_CRP_MECHANISM_SEARCH_2026-09-04.md`
- C-RP canonical verdict: `NO-GO`
- Current canonical stage: Stage 3 — Candidate Mechanism Search
- Current route: theory candidate — C1 TERMINATED / C2 TERMINATED / C-RP TERMINATED / DISTINCT MECHANISM REQUIRED
- Stage 4 authorized for C-RP: NO
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

Stage-2 killed ingredient-level novelty claims remain binding.

## Prior failed mechanisms

### C1 — Coalition-Scope Implementation Crowd-Out

Stage 4 verdict: **NO-GO**.

The one-sided implementation primitive generated `a_IS>=a_SU`, omitted the intended competition-exposure channel, failed off-equilibrium consumer-surplus integrability, and produced only a mechanical cost-bearing benchmark reversal.

### C2 — Bilateral Implementation Public-Good / Free-Riding

Stage 3 re-entry verdict: **NO-GO**.

The integrable bilateral technology `A_ij=a_i+a_j-a_i a_j` repaired C1's welfare defect but still generated stronger implementation incentives under IS; standard public-good free-riding did not produce a larger-coalition collapse or stability reversal.

## C-RP question

C-RP asked whether a fixed global relative-profit objective could turn the positive rival-profit spillover from interoperability into a sufficiently strong private implementation penalty under the broader formal coalition.

Preferred firm objective:

`U_i=Pi_i-(alpha/2)sum_{j!=i}Pi_j`, `0<=alpha<1`.

The reference set was fixed globally and deliberately kept independent of the formal coalition.

The C2 bilateral technology was reused only as an integrable technology:

`A_ij=a_i+a_j-a_i a_j`.

Government objective remained actual national welfare:

`W_i=CS_i+Pi_i`.

## C-RP prior-art burden

C-RP entered a crowded family:

- Matsumura, Matsushima and Cato (2013): two-stage R&D under relative-profit objectives, oligopoly and joint R&D;
- Shibata (2014): relative-profit/competition parameter together with R&D investment spillovers;
- Sun and Zhao (2024): relative performance evaluation with effort spillovers in networks.

Therefore only a new government standards-coalition stability result could qualify.

## C-RP exact reduced diagnostic

Let

`z=v(2a-a^2)`.

Under consistent relative-profit quantity competition:

`q_I=1/[4-alpha-(2-alpha)z]`,

`q_M=(alpha+2)/[8-4z+2alpha(1+z)-alpha^2]`,

`q_O=[2-2z+alpha(1+z)]/[8-4z+2alpha(1+z)-alpha^2]`.

Symmetric implementation marginal returns are recorded in `model/STAGE3R_CRP_MECHANISM.md` and reproduced by `verification/stage03r_crp_diagnostic.py`.

At `alpha=0`, the exact ratio collapses to the C2 benchmark:

`MB_I/MB_U=2/(1+z)>1`.

On a dense diagnostic grid over `alpha in [0,0.999]`, `z in [0,1/4]`, the minimum ratio remained `1.6`. Relative-performance concern did not overturn the larger-coalition implementation advantage.

## Decisive artifact test

Holding the downstream product market at ordinary-profit Cournot and applying relative profit only to the implementation evaluation gives

`MB_I^impl=3v(1-a)(2-alpha z)/[2(1+z)(2-z)^3]`,

`MB_U^impl=3v(1-a)(2-alpha z)/[4(2-z)^3]`.

Hence

`MB_I^impl/MB_U^impl=2/(1+z)`,

exactly independent of `alpha`.

Thus the direct rival-profit penalty itself does not create the required regime-differential implementation restraint. Applying relative profit consistently to the quantity stage adds the familiar tougher-competition channel, which moves the IS/SU implementation ratio further in the wrong direction.

## Numerical audit

Artifact: `verification/stage03r_crp_diagnostic.py`.

6,000 points over:

- `v in [0.005,0.25]`;
- `alpha in [0,0.95]`;
- `kappa in [10^-3,10]`.

Results:

- `a_IS<a_SU`: 0;
- `Delta_3^endo<0`: 0;
- stability reversal relative to `alpha=0`: 0;
- stability reversal relative to costless/exogenous full interoperability at the same `alpha`: 0.

## C-RP disposition

**C-RP — TERMINATED / NO-GO AT STAGE 3 RE-ENTRY.**

C-RP preserves a coherent welfare microfoundation but fails the strategic-feedback test. It generates no qualifying implementation-induced coalition-stability result beyond known relative-profit investment/spillover mechanisms.

Do not proceed to Stage 4 on C-RP.

Do not rescue C-RP by making the relative-profit reference group coalition-dependent, endogenizing `alpha`, or adding capacity/scope costs, shared gateways, topology, dynamics, or policy instruments. Those are distinct mechanisms.

## Next action

Remain at **Stage 3 — Candidate Mechanism Search**.

If the project continues, run a fresh comparison of genuinely distinct candidates. A shared interoperability infrastructure / common gateway remains one possible candidate, but it must be compared against C3 national-incidence/rent-shifting and any other surviving mechanism rather than automatically promoted.