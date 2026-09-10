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
- Next canonical stage: **Stage 2 — Literature Frontier / Novelty Kill Gate**
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

The candidate mechanisms recorded at Stage 0 remain unselected and unauthorized until Stage 3.

## Stage 1 authority

- `model/REVIVAL_STAGE1_AUDITED_REPRESENTATION_2026-09-10.md`
- `verification/stage01_revival_source_audit.py`
- `reviews/STAGE_01_REVIVAL_SOURCE_MATHEMATICAL_AUDIT_2026-09-10.md`
- `decisions/STAGE01_REVIVAL_DECISIONS.md`

Stage 1 verdict: **GO TO NOVELTY GATE**.

## Stage 1 main findings

### S1-1 — PR #65 fixed-depth reversal survives

Fresh reconstruction reproduces the historical fixed-depth result:

- fixed positions: `W_member(SU)-W(IS) approximately -0.0002086344`;
- endogenous product positions at the same fixed depths: approximately `+0.0002663570`;
- bilateral-union location: approximately `(0.140386,0.526280,0.833333)`.

Classification: **CORRECT computational source witness; not a general theorem**.

### S1-2 — IS lower-bound depth is structural in the source architecture

At symmetric IS anchors, all pair proximities satisfy `phi=1/4`. Define

`c(s)=c0+lambda/[4(t_bar-s)]-v`.

The symmetric Bertrand continuation gives

`p=a(b-c)/(2b)`,

`q=a(b+c)/[2b(b+2c)]`,

and retained per-country welfare

`W_IS(c)=a^2(3b^2+2bc-c^2)/[8b^2(b+2c)]`.

Exact differentiation yields

`dW_IS/dc=-a^2(2b^2+bc+c^2)/[4b^2(b+2c)^2]<0`,

while `dc/ds=lambda/[4(t_bar-s)^2]>0`.

Therefore `dW_IS/ds<0` on the positive regular domain conditional on the symmetric-anchor continuation, so the IS bloc selects `s_I*=0`.

The committed verifier also attacks whole-circle location deviations at eleven policy nodes across `[0,s_bar]` and finds no profitable deviation from the anchors.

This means the IS policy response is **not a canonical-parameter accident**.

### S1-3 — economic source of policy-adjustment absorption

The PR #65 mapping separates:

- formal coalition membership / compatibility benefit through the discrete graph `G(rho)`; and
- continuous standards depth through `Tau(rho,s)`.

The network-benefit term does not increase with depth. Under IS, deeper harmonization therefore raises competitive substitutability without adding a separate interoperability/network benefit.

Classification of this depth interpretation: **CORRECT BUT ECONOMICALLY AD HOC / RESTRICTIVE**.

No repair is authorized at Stage 1.

### S1-4 — endogenous-depth absorption diagnostic survives

At the canonical source point:

- `W_i(IS) approximately 0.1434896983` at `s_I=0`;
- the symmetry-reduced FULL SU candidate at `(s_12,s_3)=(s_bar,s_bar)` has member welfare approximately `0.1432070478`;
- `W_member(SU)-W_i(IS) approximately -0.0002826505`.

The old pre-specified `3 x 3` `(v,gamma)` box remains negative under the same candidate-policy diagnostic, with member-minus-IS gaps approximately from `-0.0001863` to `-0.0003791`.

Evidence maturity: **repository-reproducible diagnostic plus exact IS derivative; not a global analytic FULL-policy theorem**.

### S1-5 — source conflicts / limitations

1. The stale Salop manuscript says singleton blocs cannot choose positive depth, but the later Stage-3 policy map and PR #65 `Tau` implementation allow singleton depth. The revival source audit uses the later policy map.
2. `W_i=CS/3+Pi_i` is valid only if the inherited equal-country consumer aggregation is stated explicitly; the affine demand system alone does not derive the one-third split.
3. The inherited materials do not fully specify a post-affine blocking/consent correspondence for every ordered transition among `IS`, all SUs, and `SW`. The IS-vs-SU blocking comparison is clear, but a complete stable-partition operator must be frozen before any future Stage-4 stability theorem.
4. Old Salop policy, welfare, coalition-stability, freeze, and manuscript results remain stale and may not be reused.

## Refined research puzzle after Stage 1

> **Is policy-adjustment absorption a general property of standards-depth / strategic-repositioning games, or is it caused by the PR #65 separation in which coalition membership supplies compatibility benefits while continuous depth affects only competitive substitutability?**

The project may survive only if Stage 2 finds theorem-level room for an absorption/non-absorption result or for a whole-game coalition-stability effect that is not already known.

## Stage 2 mandatory comparison set

Stage 2 must audit at least:

- Woeckener (1999) and compatibility-before-product-design work;
- standards-coalition / network-competition literature;
- compatibility-policy and harmonization-depth literature;
- endogenous product differentiation / alliance literature;
- `private-compatibility-standards-coalitions` as an own nested benchmark;
- `standardization-scope-direction-innovation` / **Standardization Scope and Endogenous Innovation Portfolios** as own internal prior art on continuous standardization policy inducing a downstream strategic firm response.

The revival cannot claim novelty merely from:

- compatibility causing later differentiation;
- a continuous standardization policy changing firms' subsequent strategies;
- coalition structure changing product differentiation and prices;
- a calibrated fixed-depth welfare reversal.

Stage 2 must perform a whole-game/result-level absorption test.

## Next-stage contract

**Stage 2 — Literature Frontier / Novelty Kill Gate** may search and classify prior work against the audited Stage-1 representation. It may not add or select a new primitive.

If no model/result-level distinction survives, return `NO-GO`.

If a precise theorem-level gap survives, route to Stage 3 mechanism search. Only Stage 3 may compare the six Stage-0 candidate mechanisms and select a minimal architecture for Stage 4.
