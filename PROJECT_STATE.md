# Project State

Last updated: 2026-09-10

## Canonical status for this branch

- Project: Endogenous Interoperability and Standards Coalitions — **revival track**
- Historical working title: **Standards Coalitions and Strategic Product Repositioning**
- Revival working title: **Standards Coalitions, Policy Adjustment, and Strategic Product Repositioning**
- Branch: `revival/stage00-coalition-repositioning`
- Source branch / PR: `stage04r4a-affine-demand-bertrand-novelty` / PR #65
- Source head: `9f19a82e28415b571a086693323a3377f286fd73`
- Canonical workflow: `ryotamatsuki/research-paper-workflow` **v2.1**
- Workflow authority commit: `f48984013898696f010f0437a8cfed6b5b54bdc2`
- Revival Stage 0: **GO TO AUDIT**
- Revival Stage 1: **GO TO NOVELTY GATE**
- Revival Stage 2: **GO — GO TO MECHANISM SEARCH**
- Next canonical stage: **Stage 3 — Candidate Mechanism Search**
- Submission authorization: **NO**
- Theory freeze: **NONE FOR REVIVAL TRACK**
- Historical IJIO target: **context only; not binding**

## Relationship to main and PR #65

This branch does not replace or rewrite either historical authority:

1. `main` preserves the canonical terminated history of the prior paper architecture.
2. PR #65 preserves the historical affine-demand conditional-go branch and its fixed-depth welfare-reversal witness.

The revival track starts from PR #65 solely to preserve useful source mathematics and provenance. It does not inherit old Stage 4, theory-freeze, hostile-referee, journal-selection, manuscript-integration, or submission passing status.

## Stage 0 authority

- `reviews/STAGE_00_REVIVAL_IDEA_INTAKE_2026-09-10.md`
- `decisions/REVIVAL_2026-09-10_DECISION_RECORD.md`

Stage 0 verdict: **GO TO AUDIT**.

Live research question:

> **When standards blocs choose standards depth optimally before firms reposition products, under what economically defensible conditions does post-policy product repositioning change the stable standards-coalition set rather than being absorbed by the blocs' policy adjustment?**

## Stage 1 authority

- `model/REVIVAL_STAGE1_AUDITED_REPRESENTATION_2026-09-10.md`
- `verification/stage01_revival_source_audit.py`
- `reviews/STAGE_01_REVIVAL_SOURCE_MATHEMATICAL_AUDIT_2026-09-10.md`
- `decisions/STAGE01_REVIVAL_DECISIONS.md`

Stage 1 verdict: **GO TO NOVELTY GATE**.

### Stage 1 binding findings

- The historical fixed-depth #65 welfare reversal is reproducible.
- Under the source architecture, IS lower-bound depth is structurally implied along the symmetric-anchor continuation: `dW_IS/ds<0`, hence `s_I*=0`.
- The economic source is the separation between a discrete compatibility graph `G(rho)` and a continuous depth variable that changes `Tau` / competitive substitutability but does not increase the direct compatibility/network benefit.
- This depth interpretation is mathematically coherent but **economically restrictive / ad hoc**.
- The endogenous-depth source diagnostic leaves IS preferred to SU, so no coalition reversal exists at the canonical #65 witness.
- National-welfare aggregation and the full blocking correspondence require explicit treatment before any later stability theorem.

## Stage 2 authority

- `docs/REVIVAL_STAGE2_PRIOR_ART_MATRIX_2026-09-10.md`
- `reviews/STAGE_02_REVIVAL_NOVELTY_GATE_2026-09-10.md`
- `decisions/STAGE02_REVIVAL_DECISIONS.md`

Stage 2 verdict: **GO — GO TO MECHANISM SEARCH**.

## Stage 2 main findings

### S2-1 — generic compatibility-induced differentiation is occupied

Woeckener (1999) is binding prior art for

`compatibility first -> later product differentiation -> softened competition`.

Ruiz (2004), Baake & Boom (2001), and related work further occupy broad claims that standards/compatibility and endogenous product characteristics interact.

### S2-2 — standards-coalition formation/stability is occupied

Gandal & Shy (2001), Economides & Skrzypacz (2003/2004), Takarada (2020), and related standards/trade work already analyze standards coalitions, network/competition tradeoffs, regional versus multilateral regimes, and blocking/stability questions.

### S2-3 — continuous government compatibility policy is occupied

Klimenko (2009) explicitly studies strategic government policy over partial technical compatibility in network industries.

### S2-4 — post-coalition endogenous action is also occupied

Guo, Liu & Nault (2024) analyze interoperability coalition formation followed by endogenous coalition resource investment and characterize equilibrium coalition size.

Huang, Tan, Teh & Zhou (2026) analyze interoperability strength/configuration, including coalition-based structures, and derive platform-pricing and welfare effects.

Therefore the revival cannot rely on `coalition -> later endogenous choice` or `coalitional interoperability -> competition/welfare` as novelty.

### S2-5 — own SSDI paper is binding internal prior art

`standardization-scope-direction-innovation` / **Standardization Scope and Endogenous Innovation Portfolios** already contains

`continuous standardization policy -> endogenous downstream strategic reallocation -> Bertrand competition -> welfare -> policy-ranking reversal`.

The revival therefore cannot claim novelty from that generic architecture. Its downstream margin must remain product repositioning, and its publication contribution must be at the coalition-stability / absorption-nonabsorption level.

### S2-6 — surviving theorem-level gap

No exact prior model or immediate theorem was identified that simultaneously delivers:

1. multilateral standards partition / coalition state;
2. endogenous bloc standards depth;
3. costly post-policy product repositioning;
4. downstream price competition;
5. national welfare;
6. coalition blocking/stability;
7. a theorem showing when policy adjustment absorbs repositioning versus when repositioning changes the stable coalition set or stability threshold relative to fixed product positions.

This is the only surviving novelty family and is classified **POTENTIALLY NOVEL, BUT NARROW AND RESULT-DEPENDENT**.

## Permanently killed revival claims

The revival may not use any of the following as headline novelty:

- standards induce firms to differentiate;
- compatibility can soften competition through product location;
- continuous compatibility / standardization policy is new;
- standards coalitions alter competition or welfare;
- regional vs multilateral standards can differ in stability;
- coalition structure changes later product choice and prices;
- continuous standardization policy changes a downstream strategic margin and reverses policy ranking;
- nonzero repositioning itself is a contribution;
- a fixed-depth SU/IS welfare reversal alone is sufficient.

## Surviving research object for Stage 3

> **Characterize absorption versus non-absorption of strategic product repositioning in a standards-coalition game with endogenous bloc policy depth, and determine whether non-absorption changes the stable coalition set, a stability threshold, blocking behavior, or a private/social stability wedge relative to an otherwise identical fixed-position benchmark.**

## Stage 3 mandatory comparison set

Stage 3 must treat as binding:

- Woeckener (1999);
- Gandal & Shy (2001);
- Economides & Skrzypacz (2003/2004);
- Ruiz (2004);
- Klimenko (2009);
- Takarada (2020);
- Guo, Liu & Nault (2024);
- Huang, Tan, Teh & Zhou (2026);
- product-repositioning literature;
- `private-compatibility-standards-coalitions`;
- `standardization-scope-direction-innovation`.

## Stage 3 contract

Stage 3 may generate and compare genuinely distinct mechanisms explaining why policy adjustment absorbs repositioning in #65 and what minimal economic condition might prevent complete absorption.

Stage 3 must:

1. give every candidate an independent economic rationale;
2. compare whole-game novelty, tractability, welfare content, and referee risk;
3. preserve fixed-position and exogenous-depth nested benchmarks;
4. reject any candidate whose only function is to force `s_I>0`;
5. reject parameter fishing for SU dominance;
6. reject any candidate needing multiple unrelated added primitives;
7. choose at most one preferred minimal architecture for Stage 4.

If no candidate survives, return `NO-GO` and terminate the revival branch.
