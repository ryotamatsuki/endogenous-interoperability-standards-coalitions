# Project State

Last updated: 2026-09-04

## Canonical status

- Project: Endogenous Interoperability and Standards Coalitions
- Last completed stage: Stage 2 — Literature Frontier / Novelty Kill Gate
- Stage 2 execution status: COMPLETED
- Stage 2 report: `reviews/STAGE_02_NOVELTY_KILL_GATE_2026-09-04.md`
- Stage 2 canonical verdict: `GO`
- Stage 2 route: `GO TO MECHANISM SEARCH`
- Current canonical stage: Stage 3 — Candidate Mechanism Search
- Stage 3 status: AUTHORIZED / NOT YET RUN
- Current route: theory candidate — GENERALIZATION / UNIFICATION ONLY
- Production manuscript authorized: NO
- Theory frozen: NO
- Target journal: UNRESOLVED

## Canonical workflow reference

- Repository: `ryotamatsuki/research-paper-workflow`
- Version: `v1.1`
- Release SHA: `488e5ab06c207909296a7564eaf9066f7f94319c`
- Stage 2 template: `templates/STAGE_02_NOVELTY_GATE.md`
- Next template: `templates/STAGE_03_MECHANISM_SEARCH.md`

## Frozen project boundary

This project remains independent from `private-compatibility-standards-coalitions`. That frozen paper is benchmark B0 and must not be modified here.

## Stage 2 novelty verdict

The broad contribution is killed. No later stage may claim novelty from any of the following alone:

- continuous/partial interoperability;
- network effects plus product differentiation;
- interoperability before price/quantity competition;
- interior private interoperability;
- private-versus-welfare interoperability wedges;
- standards coalition formation;
- government standardization unions;
- coalition-proof partial compatibility;
- continuous compatibility plus government policy/international coordination;
- pairwise or weighted interoperability networks.

The literature audit found no single prior model that reproduces the complete Stage-1 audited whole game, but several models are structurally very close.

## Mandatory nested benchmarks after Stage 2

- **B0:** `private-compatibility-standards-coalitions` — government formal partition → binary private adoption → competition → national welfare → stability.
- **B1:** continuous private compatibility literature — Stadler et al.; Foros & Hansen; de Palma et al.; Garcia; Toshimitsu; Jeon et al.
- **B2:** government continuous compatibility / international coordination — Klimenko (2009 JIE and related work).
- **B3:** government standardization unions — Gandal & Shy (2001).
- **B4:** firm standards-coalition formation — Economides & Skrzypacz (2003).
- **B5:** modern coalition/platform interoperability — Ding, Ko & Shen (2022); Huang, Tan, Teh & Zhou (2026); related 2025–2026 interoperability papers.

See `literature/NESTED_BENCHMARK_MAP.md`.

## Strongest prior-art threat

A referee can reconstruct most of the intended architecture by combining:

1. B0 for the government coalition/private continuation/stability skeleton;
2. Klimenko-type models for continuous compatibility and government/international policy;
3. Economides–Skrzypacz for endogenous standards-coalition formation and the network-benefit versus intensified-competition trade-off.

Therefore a longer model is not enough. Stage 3 must produce a distinct full-game result.

## Only surviving Stage-3 research object

> Can regime-specific continuous private interoperability implementation reverse government coalition participation/deviation incentives relative to binary or exogenous-implementation benchmarks because a deviation changes the private continuation implementation equilibrium itself?

Primitive stability remains:

`Delta_i(rho,rho';theta) = V_i(rho;theta) - V_i(rho';theta)`.

Each continuation value must substitute its own verified private implementation equilibrium `a*(rho;theta)` or `a*(rho';theta)`.

## Stage-3 theorem target

Preferred target: **implementation-induced stability reversal**.

Find a nonempty parameter region in which

`sign Delta_i^endo(rho,rho';theta) != sign Delta_i^benchmark(rho,rho';theta)`.

A stronger target is a non-monotone or disconnected coalition-stability region in a primitive parameter that cannot occur in B0.

This is a candidate theorem, not an established result.

## Stage-3 hard kill condition

Return `NO-GO` if a minimal continuous implementation model only smooths/relabels B0's binary thresholds or reproduces a known Klimenko/Economides/Toshimitsu/Ding-style comparative static.

Do not rescue failure by adding topology, dynamics, switching costs, installed bases, extra countries, or arbitrary curvature.

## Next action

Instantiate and execute Stage 3 — Candidate Mechanism Search using the canonical v1.1 template.

Stage 3 may search only for the minimal mechanism generating a regime-dependent implementation feedback and a new stability result. It may not revive any Stage-2 killed claim.
