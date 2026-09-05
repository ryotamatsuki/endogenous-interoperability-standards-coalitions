# Project State

Last updated: 2026-09-05

## Canonical status

- Project: Endogenous Interoperability and Standards Coalitions
- Working title: **Standards Coalitions and Strategic Product Repositioning**
- Canonical workflow: `ryotamatsuki/research-paper-workflow` **v1.2**
- Workflow release tag: `v1.2`
- Previous theory freeze: `CESD-THEORY-FREEZE-2026-09-04-v2`
- Theory status: **REOPENED — NEW CONTINUATION ARCHITECTURE SELECTED FOR MINIMAL-MODEL KILL TEST**
- Stage 5RR: **NO-GO — linear localized continuation terminated**
- Stage 3R3: **GO — pure-quadratic localized transport selected**
- Stage 11R2: **STALE / REOPENED downstream of continuation failure**
- Stage 12 journal positioning: **administratively complete, submission authorization suspended**
- Stage 13: **CLOSURE REVOKED**
- Stage 14 submission QA authorized: **NO**
- Primary intended target only if the rebuilt theory survives: **International Journal of Industrial Organization (IJIO)**

## Binding failure from the terminated architecture

The feasible hostile IS history

- `s_I=1/4`;
- `x=(2/5,1/2,5/6)`

has no pure Nash equilibrium in the linear localized price subgame. Stage 5RR established this by exact finite enumeration of all 27 arc active states and all necessary piecewise-quadratic best-response candidate equations, solving 2440 nonsingular candidate systems and finding zero pure equilibria.

Authorities:

- `verification/stage05rr_localized_price_nonexistence.py`
- `reviews/STAGE_05RR_LOCALIZED_COMPETITION_HARDENING_2026-09-05.md`
- `decisions/STAGE05RR_CESD_DECISIONS.md`

The linear all-product and linear localized architectures are therefore both non-authoritative for the paper's pure-strategy SPNE claim.

## Stage 3R3 architecture search

Stage 3R3 compared distinct continuation architectures rather than stacking another Stage 5 repair.

Rejected as the primary route:

- linear + small quadratic term: not a generic existence guarantee;
- bounded relocation radius: vulnerable to an engineered-strategy-set objection;
- convex production cost: unrelated existence-restoring channel;
- simultaneous location and price: changes the strategic question;
- fixed/regulated prices: removes too much IO content;
- standard logit/random utility: requires redesign of the existing pairwise compatibility primitive.

Reserve architectures:

- mixed price continuation under linear transport;
- broader redesign of the competition stage.

Selected architecture:

> **Pure-quadratic localized circular competition with the existing policy-dependent pair friction `tau_ij`.**

For an arc of length `ell` between adjacent products `i,j`, a consumer at distance `y` from `i` compares

`u_i = A - p_i - tau_ij y^2 + v n_i`,

`u_j = A - p_j - tau_ij (ell-y)^2 + v n_j`.

The raw boundary is therefore

`y_ij = ell/2 + [p_j-p_i + v(n_i-n_j)]/[2 tau_ij ell]`,

clipped to `[0,ell]` at full-arc capture.

Everything else remains frozen for the first minimal-model test: regimes, standards-depth map into `tau_ij`, network matrix, anchors, timing, repositioning cost, and welfare ownership convention.

## Literature rationale

Quadratic distance disutility is a recognized equilibrium-existence architecture in spatial competition rather than an assumption invented for this paper. d'Aspremont, Gabszewicz and Thisse (1979), Economides (1986), and de Frutos, Hamoudi and Jarque (1999) provide the relevant classical existence rationale.

However, those results do **not** certify this project's heterogeneous, policy-dependent pair-friction game. The new Stage 4 must prove or refute continuation completeness from the actual primitives.

## Stage 4R3Q contract

Next formal stage: **Stage 4R3Q — Pure-Quadratic Global Continuation Minimal Model Gate**.

Lexicographic gate:

1. Define the quadratic localized price game globally, including corners and coincident locations.
2. Test the former hostile location history first.
3. Establish or refute pure price continuation for every feasible location history required by unilateral location deviations.
4. No `None`, branch failure, or solver nonconvergence may be interpreted as an unprofitable deviation.
5. One feasible history with no required pure continuation returns `NO-GO` immediately.
6. Only after continuation completeness passes may the stage solve location best responses.
7. Only after the location game passes may policy, welfare, reversal, and coalition stability be recomputed.
8. Preservation of the old numerical reversal is not an acceptance criterion.

## What remains historical only

The following old-branch objects are not theorem/SPNE evidence:

- `Delta_M^(B-T)≈-0.010167`;
- `Delta_M^(FULL)≈+0.001571`;
- reported member welfare decomposition;
- reported world-welfare ordering;
- 9/9 local sign robustness conditional on the old linear branch.

## Current verdict

**STAGE 3R3 GO — DO NOT SUBMIT.**

Proceed to **Stage 4R3Q — Pure-Quadratic Global Continuation Minimal Model Gate**.
