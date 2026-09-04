# Project State

Last updated: 2026-09-04

## Canonical status

- Project: Endogenous Interoperability and Standards Coalitions
- Last completed stage: Stage 3 — Candidate Mechanism Search
- Stage 3 execution status: COMPLETED
- Stage 3 report: `reviews/STAGE_03_MECHANISM_SEARCH_2026-09-04.md`
- Stage 3 canonical verdict: `GO`
- Stage 3 route: `GO TO MINIMAL MODEL`
- Current canonical stage: Stage 4 — Minimal Model
- Stage 4 status: AUTHORIZED / NOT YET RUN
- Current route: theory candidate — GENERALIZATION / UNIFICATION ONLY
- Selected mechanism: **Coalition-Scope Implementation Crowd-Out (CSIC)**
- Production manuscript authorized: NO
- Theory frozen: NO
- Target journal: UNRESOLVED

## Canonical workflow reference

- Repository: `ryotamatsuki/research-paper-workflow`
- Version: `v1.1`
- Release SHA: `488e5ab06c207909296a7564eaf9066f7f94319c`
- Stage 3 template: `templates/STAGE_03_MECHANISM_SEARCH.md`
- Next template: `templates/STAGE_04_MINIMAL_MODEL.md`

## Frozen project boundary

This project remains independent from `private-compatibility-standards-coalitions`. That paper remains benchmark B0 and must not be modified here.

## Stage-2 restrictions remain binding

No later stage may claim novelty from continuous compatibility, interiority, network effects plus compatibility, downstream competition after compatibility, private/social compatibility wedges, standards coalition formation, government standardization unions, government compatibility policy/international coordination, coalition-proof partial compatibility, or pairwise/weighted interoperability by themselves.

## Stage-3 candidate search result

Ten candidates were compared using fixed ex-ante weights:

- whole-game prior-art survival 25%;
- theorem sharpness 20%;
- tractability 20%;
- mechanism clarity 15%;
- welfare content 10%;
- institutional relevance 10%.

TOP 3:

1. **C1 — Coalition-scope network/reach vs competition exposure** — selected.
2. C2 — bilateral implementation public-good/free-riding — fallback only.
3. C3 — national-incidence/cross-border rent-shifting — rejected as core mechanism but retained in welfare accounting where mechanically present.

Scoring and diagnostic artifact:

`verification/stage03_candidate_scoring.py`.

## Selected mechanism — Coalition-Scope Implementation Crowd-Out

A formal standards coalition changes the number/scope of interoperability partners reached by a firm's implementation. Broader scope may raise interoperability/network value but also magnify the product-market rent loss from making more rivals effectively compatible. Firms maximize profit while governments evaluate national welfare.

Required feedback:

`rho -> interoperability scope -> a*(rho) -> downstream equilibrium -> W_i(rho) -> government deviation incentives`.

The same implementation technology and cost function must apply under every formal regime. Regime dependence must be derived from coalition scope and the downstream game, not imposed through regime-specific cost coefficients.

## Stage-4 minimal skeleton

Players:

- countries/governments `1,2,3`;
- one domestic firm per country;
- symmetric national consumer markets, with all firms active in each market.

Formal regimes for the first test:

- `rho^IS={{1,2,3}}`;
- `rho_12^SU={{1,2},{3}}`, interpreted as the continuation after country 3 leaves IS.

Timing:

1. formal regime fixed;
2. firms choose `a_i in [0,1]`;
3. Cournot competition;
4. national welfare;
5. government deviation/stability comparison.

First downstream candidate:

`p_i^k = 1 - Q^k + v a_i sum_{j in C_i(rho),j!=i} q_j^k`.

First implementation-cost candidate:

`C(a_i)=kappa a_i^2/2`.

Both are Stage-4 test primitives, not frozen results.

## Stage-4 headline objects

Private continuation equilibrium:

`a*(rho)`.

Government stability:

`Delta_3^endo = W_3(rho^IS;a*(rho^IS)) - W_3(rho_12^SU;a*(rho_12^SU))`.

Benchmark:

`Delta_3^full` under fixed/full implementation and, where cleanly recoverable, a binary B0-style implementation benchmark.

## Stage-4 required candidate results

1. verified implementation equilibrium under each regime, including SOC/KKT/global/corners;
2. genuine regime dependence of `a*(rho)` from coalition scope;
3. preferably a nonempty region with `a_IS* < a_SU*` — coalition-scope implementation crowd-out;
4. **headline kill test:** a nonempty region with
   `sign Delta_3^endo != sign Delta_3^full`;
5. proof that any reversal is not merely a smooth relabeling of a B0 threshold.

## Hard kill / no-rescue rule

Return NO-GO for C1 if the selected minimal model:

- needs arbitrary curvature solely for interiority;
- makes the scope effect an assumed regime coefficient rather than a derived market effect;
- only smooths B0's binary threshold;
- produces no stability reversal or comparably sharp new full-game result;
- requires importing bilateral free-riding, trade policy, switching costs, topology, dynamics, installed bases, extra countries, or other Stage-3 candidates to work.

If C1 fails, return to Stage 3 before testing C2. Do not hybridize mechanisms silently.

## Next action

Instantiate and execute Stage 4 — Minimal Model using only the CSIC skeleton in `model/STAGE3_PREFERRED_MECHANISM.md`.
