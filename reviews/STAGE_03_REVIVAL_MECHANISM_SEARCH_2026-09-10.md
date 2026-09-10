# Stage 3 — Revival Candidate Mechanism Search

Date: 2026-09-10

Workflow: `ryotamatsuki/research-paper-workflow` v2.1 at `f48984013898696f010f0437a8cfed6b5b54bdc2`.

Branch: `revival/stage00-coalition-repositioning`.

Stage-2 authority: `reviews/STAGE_02_REVIVAL_NOVELTY_GATE_2026-09-10.md`.

Candidate matrix: `docs/REVIVAL_STAGE3_CANDIDATE_MECHANISM_MATRIX_2026-09-10.md`.

Selected architecture: `model/REVIVAL_STAGE3_SELECTED_MECHANISM_2026-09-10.md`.

## 1. Executive verdict

**GO — GO TO MINIMAL MODEL.**

Ten genuinely different mechanism/generalization candidates were compared under an ex-ante weighted scoring rule. One candidate is sufficiently minimal, economically motivated, tractable, and distinct at the whole-game level to justify a Stage-4 kill test:

**C1 — Realized Interoperability Depth.**

The selection is narrow. It does not revive the old manuscript and does not establish a new theorem. Stage 4 must kill the architecture if the repositioning channel does not alter a coalition-level result relative to an otherwise identical fixed-position benchmark.

## 2. Binding Stage-2 constraints

Stage 3 treats the following novelty claims as permanently unavailable:

- compatibility can induce later differentiation;
- continuous standards/compatibility policy is new;
- coalition structure changes later product design/prices;
- regional vs multilateral standards can differ in stability;
- product repositioning costs are novel;
- an interoperability coalition with a later endogenous action is novel;
- continuous standardization changing a downstream strategic choice and policy ranking is novel, including because own SSDI already occupies that generic architecture.

The only admissible contribution route is a FULL-only absorption/non-absorption or coalition-stability result in which strategic repositioning is indispensable.

## 3. Candidate generation and ranking

The search considered ten candidates:

1. realized interoperability depth;
2. multi-market common standard;
3. home-market incidence / asymmetric national surplus;
4. heterogeneous redesign flexibility;
5. internal coalition depth conflict;
6. installed-base / coalition-size nonlinear interoperability;
7. sequential accession after depth commitment;
8. endogenous standard technical direction;
9. firm implementation/compliance effort;
10. scope × depth two-dimensional standardization.

The ex-ante weights were:

- whole-game novelty / prior-art survival 25%;
- mechanism clarity 15%;
- minimality / tractability 20%;
- welfare / coalition leverage 15%;
- institutional plausibility 10%;
- empirical bridge 5%;
- referee defensibility 10%.

Top scores:

- C1 Realized interoperability depth: **92/100**;
- C2 Multi-market common standard: **82/100**;
- C3 Home-market incidence: **77/100**.

Only C1 is selected.

## 4. Why C1 is preferred

Stage 1 identified the exact source of PR #65's policy-adjustment absorption: formal coalition membership activates the full compatibility/network term, while continuous depth alters competitive substitutability but produces no additional realized interoperability benefit.

C1 repairs the *economic meaning* of the same depth variable rather than adding an unrelated rescue parameter. Formal membership identifies the set of potential interoperable partners; technical depth determines the intensity/completeness of realized interoperability inside that set.

The same depth still compresses standard-based differentiation. Hence one policy variable creates a natural trade-off:

`more realized interoperability <-> stronger direct competitive compression`.

Product repositioning can then matter by attenuating the competitive side of that trade-off. This is precisely the interaction that is absent in the fixed-position benchmark.

## 5. Reduced-form coherence result

Under symmetric IS with fixed positions,

`c_FIX(s)=c0 + lambda*phi_bar/(t_bar-s) - v*chi(s)`.

Because Stage 1 established `dW_IS/dc<0`, the policy derivative no longer has the mechanically negative sign of PR #65. Instead,

`dc_FIX/ds=lambda*phi_bar/(t_bar-s)^2-v*chi'(s)`.

Thus the marginal interoperability benefit and competitive effect are explicitly opposed.

In FULL, product locations become functions of depth and the derivative of `phi(x_i(s)-x_j(s))/(t_bar-s)` contains an induced repositioning term. If members move apart, the fall in `phi` can reduce the marginal competitive cost of deeper standards. That term is absent in B-FIX.

This establishes internal coherence only. It does not establish that the term changes coalition stability.

## 6. Why the alternatives are not selected

### C2 Multi-market common standard

Potentially powerful because one policy instrument may not absorb market-specific repositioning, but it roughly multiplies the state space and continuation burden. It is retained only as a documented future architecture if C1 is terminated and a *new* Stage-0 project is later opened; it may not be appended inside the current Stage-4 attempt.

### C3 Home-market incidence

Could make coalition blocking more sensitive than aggregate welfare, but risks a standard "heterogeneity creates thresholds" result. The workflow prohibits treating added heterogeneity as a mechanism by itself.

### C4 / C5

Heterogeneous redesign costs or internal coalition policy conflict require asymmetry to become active and therefore are not one-change minimal architectures.

### C6

Nonlinear installed-base effects are plausible but highly vulnerable to curvature engineering and overlap with network-effects standards literature.

### C7 / C8

Accession timing or endogenous standard direction adds a new strategic layer before the baseline interaction is exhausted.

### C9

Firm implementation effort adds another endogenous continuation stage and moves toward Klimenko / Guo–Liu–Nault.

### C10

Scope × depth is both too complex and too close to own SSDI's standardization-scope research program.

## 7. Targeted prior-art check

C1 remains inside the literature families already audited at Stage 2: continuous compatibility policy, compatibility-before-product-design, interoperability strength, standards coalitions, and own SSDI. No new literature family is needed to justify C1.

A targeted check around the multi-market fallback found Casella's product-standards coalition work and Schmidt–Steingress on standards harmonization/trade, confirming that cross-country/product standards and adaptation costs are well established. That makes C2 empirically plausible but does not improve its minimality relative to C1.

No identified prior theorem in the Stage-2/3 search gives the specific C1 result target: an endogenous government standards-depth game in which post-policy product repositioning shifts the stable coalition set or stability threshold relative to a fixed-position benchmark.

## 8. Stage-4 exact model contract

Stage 4 must test only C1. Freeze:

- three countries / three firms;
- source standards partitions;
- source depth domain and `Tau` map;
- equal-country welfare incidence;
- inherited anchors and quadratic repositioning cost;
- quadratic representative-consumer affine demand;
- Bertrand price competition;
- one linear realized-interoperability map `chi(s)=s/s_bar`;
- strict coalition blocking/stability, with a complete transition/consent correspondence to be explicitly frozen before stability claims.

Stage 4 may impose transparent regularity inequalities. It may not add another substantive mechanism.

## 9. Stage-4 fatal kill tests

The minimal model must establish, or the revival terminates:

1. all-history demand/price continuation on the claimed domain;
2. a well-defined global product-location continuation for material policy histories;
3. standards-contingent repositioning on a nondegenerate region;
4. a difference between B-FIX and FULL caused by repositioning after depth optimization;
5. a coalition-level consequence: stable-partition difference, blocking reversal, stability-threshold shift, or private/social stability wedge;
6. indispensability: removing product repositioning removes the headline result;
7. result-level distance from Woeckener, Klimenko, Guo–Liu–Nault, Huang–Tan–Teh–Zhou, Takarada/Gandal–Shy, and own SSDI.

A positive optimal depth, nonzero repositioning, or welfare-level change alone does **not** pass Stage 4.

## 10. Canonical Stage-3 verdict

**GO — GO TO MINIMAL MODEL.**

Preferred minimal architecture: **C1 — Realized Interoperability Depth**.

## 11. Next-stage contract

Stage 4 must solve one minimal C1 architecture and the required B-FIX/B-EXO benchmarks. No parallel feature search is authorized.

If the C1 full game does not produce a repositioning-essential coalition-level result on a nondegenerate regular region, return `NO-GO` and terminate the current revival. Do not repair C1 by adding asymmetry, nonlinear network benefits, extra markets, bargaining, policy costs, or a second policy dimension within the same Stage-4 cycle.