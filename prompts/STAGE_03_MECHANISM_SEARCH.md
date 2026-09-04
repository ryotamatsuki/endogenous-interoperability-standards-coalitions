# Stage 3 — Candidate Mechanism Search

> Canonical authority: `ryotamatsuki/research-paper-workflow` v1.1 at `488e5ab06c207909296a7564eaf9066f7f94319c` → `GOVERNANCE.md` → `THEORY_PAPER_RESEARCH_PIPELINE.md` → `templates/STAGE_03_MECHANISM_SEARCH.md`.

## 0. Role

Act as a research director selecting the minimum economically meaningful generalization, not a feature list.

## 1. Binding Stage-2 object

The only surviving research architecture is:

`government formal regime rho -> regime-specific private continuous interoperability implementation a*(rho) -> downstream competition -> national welfare -> participation/deviation stability`.

Primitive stability:

`Delta_i(rho,rho';theta)=V_i(rho;theta)-V_i(rho';theta)`.

Preferred theorem target:

`sign Delta_i^endo != sign Delta_i^benchmark` on a nonempty parameter region.

## 2. Binding killed claims

Do not treat any of the following as a contribution: continuous compatibility, interior compatibility, network effects plus compatibility, compatibility before competition, private/social compatibility wedges, standards coalition formation, government standardization unions, government compatibility policy/international coordination, coalition-proof partial compatibility, pairwise/weighted interoperability.

## 3. Mandatory nested benchmarks

- B0: `private-compatibility-standards-coalitions`.
- B1: continuous private compatibility literature.
- B2: Klimenko-type government compatibility policy/international coordination.
- B3: Gandal–Shy government standardization unions.
- B4: Economides–Skrzypacz standards-coalition formation.
- B5: current platform/network interoperability frontier.

## 4. Candidate search

Generate 8–12 genuinely different candidate mechanisms. For each record:

1. one-sentence mechanism;
2. feedback loop;
3. endogenous margins;
4. minimum players/timing;
5. minimum new interaction relative to Stage 2;
6. closest prior-art threat;
7. expected theorem/reversal;
8. welfare content;
9. institutional interpretation;
10. tractability risk;
11. fatal referee attack;
12. nested benchmarks;
13. recovery restrictions;
14. strategic interaction unique to full architecture;
15. result unavailable in nested benchmarks.

## 5. Scoring rule — fixed ex ante

Score each candidate from 0–10 using:

- whole-game prior-art survival: 25%;
- theorem sharpness: 20%;
- tractability: 20%;
- mechanism clarity: 15%;
- welfare content: 10%;
- institutional relevance: 10%.

Do not alter weights after seeing scores.

## 6. Verification discipline

No full Stage-4 algebra is required. Use reduced-form/sign prototypes only to test internal coherence. A desired reversal must not be inserted directly into government payoff assumptions.

Any convex implementation cost requires an independent engineering/compliance interpretation and remains a viability device, never a novelty claim.

Transport-cost-only interoperability is not admissible as the preferred mechanism.

## 7. Selection rule

Select TOP 3 and then one preferred minimal mechanism. Prefer a mechanism in which the same economic primitives operate under every formal regime and `rho` changes the set/scope of interoperability relationships, rather than one that obtains the result by assigning unrelated regime-specific technologies.

## 8. Stage-4 contract

Stage 4 receives exactly one skeleton. It must:

- use the minimum number of countries/firms needed for government coalition stability;
- solve private implementation and downstream competition under every relevant regime;
- verify SOC/KKT/global best responses and corners;
- substitute regime-specific `a*(rho)` into national welfare;
- compare endogenous and benchmark stability signs;
- recover mandatory nested benchmarks where feasible;
- return NO-GO if the result is only a smoothed B0 threshold.

## 9. Required output

Save:

- `reviews/STAGE_03_MECHANISM_SEARCH_2026-09-04.md`;
- `model/STAGE3_PREFERRED_MECHANISM.md`;
- update `PROJECT_STATE.md` and `decisions/DECISION_LOG.md`.

Final verdict must be one of `GO -> GO TO MINIMAL MODEL`, `CONDITIONAL GO`, or `NO-GO`.