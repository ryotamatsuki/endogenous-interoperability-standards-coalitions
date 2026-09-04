# Stage 2 — Literature Frontier / Novelty Kill Gate

> Canonical authority: `ryotamatsuki/research-paper-workflow` v1.1 at `488e5ab06c207909296a7564eaf9066f7f94319c` → `GOVERNANCE.md` → `THEORY_PAPER_RESEARCH_PIPELINE.md` → `templates/STAGE_02_NOVELTY_GATE.md`.

## Project context

- Topic: endogenous post-agreement interoperability implementation inside international standards coalitions
- Core question: Does endogenizing a continuous post-agreement private interoperability implementation margin inside a government standards-coalition game generate a coalition-stability result unavailable in both binary private-adoption coalition models and continuous compatibility/government-policy models considered separately?
- Canonical audited representation: `model/AUDITED_STAGE1_REPRESENTATION.md`
- Stage 1 verdict: `GO TO NOVELTY GATE`
- Target journal: `UNRESOLVED`
- Current date: 2026-09-04

## Frozen game skeleton

For each formal regime/partition `rho`, firms choose a regime-specific continuous implementation vector `a*(rho;theta)`, then product-market competition occurs. Government continuation value is `V_i(rho;theta)`, and stability against deviation to `rho'` is evaluated by

`Delta_i(rho,rho';theta) = V_i(rho;theta) - V_i(rho';theta)`.

Neither a scalar private optimum nor a scalar coalition threshold may be presumed.

## Mandatory nested benchmarks

- B0 — `private-compatibility-standards-coalitions`: government formal partition → binary private adoption → Cournot → national welfare → stability.
- B1 — continuous private compatibility: Stadler et al. (2022), Foros & Hansen (2001), de Palma et al. (1999), Garcia (2016), Toshimitsu (2018), Jeon et al. (2023).
- B2 — government continuous-compatibility policy / international coordination: Klimenko (2009 JIE; 2009 IREF).
- B3 — government standardization unions: Gandal & Shy (2001).
- B4 — firm standards-coalition formation: Economides & Skrzypacz (2003).
- B5 — modern coalition/platform interoperability: Ding, Ko & Shen (2022), Huang, Tan, Teh & Zhou (2026), and relevant 2025–2026 interoperability papers.

## Mandatory Stage 2 tests

1. Compare components and whole games separately.
2. Determine whether any single prior model reproduces the full player/objective/strategy/timing/continuation/stability architecture after relabeling.
3. Determine whether the intended stability result would nevertheless be an immediate corollary of a prior theorem.
4. Construct an explicit nested-benchmark map.
5. Identify one strategic feedback that is endogenous only in the proposed full architecture.
6. State one candidate theorem/threshold/ranking/sign reversal/equilibrium-region result that would be unavailable in every nested benchmark alone.
7. Search seminal, classic, modern, 2020–current, and current working-paper literature; perform backward/forward and same-author/synonym searches where feasible.
8. Treat Economides–Skrzypacz (2003) as a high-priority threat despite its firm-coalition rather than government-coalition objective.
9. Treat Klimenko (2009) as the high-priority international-policy threat.
10. Treat Huang et al. (2026) as the high-priority current interoperability-network threat.

## Hard kill test

Return `NO-GO` if the candidate is merely B0 with a known continuous compatibility block substituted for binary adoption and the only effect is a smoothed or relabeled threshold.

## Allowed surviving route

A generalization/unification route may survive only if regime-dependent private implementation creates a new feedback into national coalition participation/deviation payoffs, with at least one nontrivial candidate result not available in B0–B5 alone.

## Required output

Save the report as `reviews/STAGE_02_NOVELTY_KILL_GATE_2026-09-04.md`, create `literature/NESTED_BENCHMARK_MAP.md`, update the prior-art ledger, decision log, and project state, and choose exactly one canonical verdict:

- `GO` → `GO TO MECHANISM SEARCH`
- `CONDITIONAL GO`
- `NO-GO`
