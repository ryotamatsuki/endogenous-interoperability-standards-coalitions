# Stage 1 — Source & Mathematical Audit

> Canonical authority: `ryotamatsuki/research-paper-workflow` v1.1 at `488e5ab06c207909296a7564eaf9066f7f94319c` → `GOVERNANCE.md` → `THEORY_PAPER_RESEARCH_PIPELINE.md` → `templates/STAGE_01_AUDIT.md`.

## Project context

- Working title: `Endogenous Interoperability and Standards Coalitions`
- Stage 0 verdict: `GO TO AUDIT`
- Stage 0 report: `reviews/STAGE_00_IDEA_INTAKE_2026-09-04.md`
- Source repository: `ryotamatsuki/endogenous-interoperability-standards-coalitions`
- Frozen benchmark repository: `ryotamatsuki/private-compatibility-standards-coalitions`
- Current date: 2026-09-04
- Target journal: `UNRESOLVED`

## Stage-0 surviving question to audit

When a formal standards coalition is chosen by governments/countries but firms retain post-agreement control over implementation-level interoperability, can the private implementation equilibrium alter national participation/deviation incentives and therefore coalition stability in a way not already implied by existing compatibility and standards models?

## Known blockers / high-risk sources

Audit at minimum:

1. Stadler, Tobler Trexler & Unsorg (2022), `10.1007/s11067-022-09572-x`.
2. Foros & Hansen (2001), `10.1016/S0167-6245(01)00044-0`.
3. Toshimitsu (2018), `10.1007/s10842-017-0264-1`.
4. de Palma, Leruth & Regibeau (1999), `10.1016/S0167-6245(99)00006-2`.
5. Garcia (2016), `10.1111/jems.12146`.
6. Jeon, Menicucci & Nasr (2023), `10.1257/mic.20200309`.
7. Gandal & Shy (2001), `10.1016/S0022-1996(00)00067-2`.
8. Klimenko (2009), `10.1016/j.jinteco.2008.08.005` and `10.1016/j.iref.2008.09.015`.
9. Huang, Tan, Teh & Zhou (2026), `A Network Approach to Interoperability`.
10. The frozen binary benchmark in `private-compatibility-standards-coalitions/docs/CANONICAL_MODEL.md`.

## Mandatory mathematical checks

- Re-derive the closest accessible endogenous-compatibility benchmark from primitives, not from reported formulas.
- Check price/quantity subgame FOCs, first-stage compatibility FOC, SOC, feasibility, corners, and global-best-response risk.
- Test whether a compatibility parameter is only a change of variable in a Hotelling/Salop substitutability coefficient.
- Do not treat a symmetric FOC as sufficient evidence of a Nash equilibrium.
- Do not introduce a convex implementation cost solely to obtain an interior solution.

## Mandatory conceptual checks

- Separate government formal-membership strategies from firm implementation strategies.
- Compare the proposed timing with the frozen binary benchmark. If the benchmark already has `formal partition -> private adoption -> competition -> national welfare -> stability`, do not claim actor/timing separation as new.
- Compare with Klimenko-type continuous compatibility policy models. Do not claim continuous government/firm compatibility interaction as new if already present.
- Replace the provisional scalar threshold formulation if necessary. Coalition stability must first be written using regime-specific continuation equilibria. A scalar `â` is admissible only after monotonicity and a unique root are established.

## Required output

1. Executive audit verdict.
2. Canonical source/benchmark model map.
3. Equation-by-equation audit of the closest tractable benchmark.
4. SOC / feasibility / global-best-response audit.
5. Parameter-interpretation and reparameterization audit.
6. Welfare / participation / coalition-stability audit.
7. Correct / ad hoc / incorrect / ambiguous claim table.
8. Audited residual game representation for Stage 2.
9. Exact novelty-search inputs.
10. Verdict and next-stage contract.

## Verdicts

Choose exactly one:

- `GO TO NOVELTY GATE`
- `CONDITIONAL GO` — one unresolved verification issue only
- `NO-GO`

Stage 2 may compare the frozen audited representation with prior art. It may not alter the game merely to improve novelty.