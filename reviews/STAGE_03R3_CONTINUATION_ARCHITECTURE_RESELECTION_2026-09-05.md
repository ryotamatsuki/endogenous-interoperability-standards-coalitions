# Stage 3R3 — Continuation Architecture Re-Selection

Date: 2026-09-05
Canonical workflow: `ryotamatsuki/research-paper-workflow` v1.2
Prior stage: Stage 5RR — `NO-GO`

## 1. Executive verdict

**GO — SELECT PURE-QUADRATIC TRANSPORT FOR A NEW MINIMAL-MODEL KILL TEST.**

The linear-transport continuation architecture is terminated. Both unrestricted all-product choice and the explicit localized-consideration repair fail to provide the pure price continuation required by the location-first SPNE claim.

The preferred next architecture changes exactly one structural object: transport/adaptation disutility becomes strictly quadratic in distance. The standards policy map, network term, location timing, product repositioning cost, welfare ownership convention, and coalition game remain frozen until the new Stage 4 test says otherwise.

This verdict does **not** state that the old reversal survives. It selects the least distortive architecture that has a recognized theoretical rationale for restoring price-subgame existence.

## 2. Binding failure inherited from Stage 5RR

At feasible IS history `s_I=1/4`, `x=(2/5,1/2,5/6)`, the linear localized price game has no pure Nash equilibrium. The exact Stage 5RR verifier enumerates all 27 global arc active states and all necessary piecewise-quadratic best-response candidates and finds zero pure equilibria.

Therefore any candidate that preserves the same linear price architecture without an independently justified equilibrium device is rejected.

## 3. Ex-ante ranking criteria

Weights:

- continuation existence / equilibrium completeness: 30%
- preservation of the standards–repositioning mechanism: 20%
- tractability / reproducibility: 15%
- prior-art / novelty risk: 15%
- welfare and policy interpretability: 10%
- institutional defensibility: 10%

A candidate is killed regardless of weighted score if its existence fix is visibly engineered only to exclude the known counterexample.

## 4. Candidate architecture table

| Candidate | Core change | Existence prospect | Mechanism preservation | Tractability | Main fatal risk | Verdict |
|---|---|---:|---:|---:|---|---|
| A. Pure-quadratic transport | Replace linear distance disutility by `distance^2`; keep location→price timing | High relative to linear benchmark; classical existence remedy | High | Medium | heterogeneous pair friction may break standard existence theorem | **TOP 1** |
| B. Mixed price continuation | Keep linear transport; allow mixed-strategy price equilibrium at problematic histories | Conceptually possible | Very high | Very low | mixed continuation must be characterized for every off-path location and then integrated into location/policy payoffs | TOP 3 |
| C. Competition-stage redesign | Replace Bertrand continuation with a globally well-behaved competition stage, e.g. quantity/differentiated demand | High if chosen appropriately | Medium-low | Medium | becomes a different IO model; old pricing mechanism and welfare decomposition cease to be comparable | TOP 3 |
| D. Linear + small quadratic term | Add curvature but retain linear term | Medium/low | High | Medium | de Frutos–Hamoudi–Jarque show feasible locations with no price equilibrium outside special cases | **KILL** |
| E. Bounded repositioning radius | Restrict `x_i` to anchor neighborhoods chosen to avoid bad histories | High by construction if sufficiently tight | High | High | looks engineered to remove the counterexample; existence bought by strategy restriction | **KILL** |
| F. Convex production cost | Keep linear transport, add convex marginal cost | Medium/high in some Hotelling models | Medium | Medium | unrelated primitive repairs existence mechanically and contaminates welfare mechanism | **KILL** |
| G. Simultaneous location-price choice | Remove continuation requirement by choosing `x,p` simultaneously | Not a continuation problem | Medium-low | Medium | changes strategic timing and interpretation of repositioning after policy | KILL for this paper |
| H. Exogenous/fixed price or regulated markup | Eliminate strategic price subgame | High | Low | High | destroys core IO price competition content | **KILL** |
| I. Logit/random-utility demand | Smooth global demand with product-specific utility | High | Medium-low | Medium | pairwise standards-friction map no longer enters naturally without redesign | KILL for current paper |

## 5. Literature mini-search for new architecture family

### Pure quadratic transport

The existence problem is classical rather than specific to this project.

- d'Aspremont, Gabszewicz and Thisse (1979), *Econometrica*, replace Hotelling's linear transport structure with quadratic distance costs in the canonical remedy to price-equilibrium failure.
- Economides (1986), *Economics Letters*, explicitly notes that quadratic distance disutility yields price equilibria for arbitrary locations in the standard two-firm location-price problem.
- de Frutos, Hamoudi and Jarque (1999), *Regional Science and Urban Economics*, analyze the circle model with linear-quadratic transport costs. Their abstract reports a unique perfect equilibrium in the convex special case with zero linear term (pure quadratic), while outside the two special cases there are feasible locations for which the price subgame has no equilibrium.

These papers make pure quadratic curvature a recognized equilibrium-existence architecture rather than an ad hoc fix invented for this project.

### Mixed strategies

Mixed strategies are a legitimate route when pure price continuation fails, but they move the technical center of gravity of the paper. The location stage would require expected continuation profits for every unilateral location deviation, and multiplicity/selection would become central. This is too large a burden for the first repair candidate.

### Convex production costs

Dragone and Lambertini (2020), *Regional Science and Urban Economics*, show that sufficiently convex production costs can restore Hotelling equilibrium under linear transportation costs. This confirms feasibility as a theoretical remedy but also demonstrates why it is not preferred here: existence is restored by adding a production-cost channel unrelated to standards compatibility or repositioning.

## 6. TOP 3 deep dives

### TOP 1 — Pure-quadratic transport

**Mechanism logic.** Convex distance disutility makes aggressive capture of a remote market increasingly costly in delivered utility terms, reducing the non-quasiconcavity that destroys the linear price subgame.

**Strategic feedback.** Standards policy changes interoperability friction; firms reposition in product space; quadratic distance then changes local substitution and price competition; resulting profits feed back into the relocation incentive and coalition welfare.

**Endogenous margins.** Standards depth, locations, prices, network shares, coalition choice.

**Minimum change.** Distance exponent changes from 1 to 2. No fixed cost, new player, new policy instrument, or production-cost channel.

**Closest prior-art threat.** Classical quadratic Hotelling/Salop existence literature. This is a threat to novelty only if the paper claims transport curvature as a contribution. It must not. Curvature is a regularization primitive; the contribution must remain the standards-policy × endogenous-repositioning welfare/stability interaction.

**Expected result to kill-test.** Whether there exists a parameter region in which the fixed-position regime ranking differs from the endogenous-repositioning ranking after the price game is globally valid.

**Fatal risk.** The project uses heterogeneous pairwise interoperability frictions `tau_ij`. Standard pure-quadratic existence theorems do not automatically establish equilibrium under this heterogeneous policy-dependent structure. Stage 4 must prove or refute continuation completeness from primitives; literature citation is not enough.

### TOP 2 — Mixed price continuation under linear transport

**Mechanism logic.** Preserve the original linear differentiation model and complete problematic price subgames with mixed Nash equilibria.

**Strength.** Maximum preservation of the original economic primitives.

**Fatal risk.** The object needed upstream is not merely existence of some mixed price equilibrium. The location and policy stages require a well-defined expected-profit continuation at every relevant history. Multiplicity and equilibrium selection may make the SPNE correspondence unusable. This is a high-dimensional new paper architecture.

**Status.** Reserve only if pure quadratic fails.

### TOP 3 — Competition-stage redesign

**Mechanism logic.** Replace Bertrand location-price continuation with a differentiated-product competition block with global existence.

**Strength.** Can preserve standards compatibility and product repositioning conceptually.

**Fatal risk.** It changes the strategic object sufficiently that the old contribution may no longer be the same paper. The redesign could absorb the claimed result or shift it to a quantity/markup artifact.

**Status.** Last-resort re-foundation, not first repair.

## 7. Rejected candidates

### Linear + epsilon quadratic

Rejected because small curvature is not a generic existence guarantee. The 1999 circle-model taxonomy explicitly warns that outside special cases feasible locations with no price equilibrium remain.

### Bounded relocation radius

Rejected because the restriction would be chosen after observing exactly where continuation fails. Even if technologically interpretable, it would invite the fatal objection that the admissible strategy set is engineered around the theorem.

### Convex production costs

Rejected because a second economic channel unrelated to compatibility/repositioning would be introduced solely to repair existence.

### Simultaneous location and price

Rejected for this paper because the stated economic sequence—standards policy, product repositioning, then price competition—is substantively meaningful. Simultaneous `x,p` would answer a different strategic question.

### Fixed prices / regulated markups

Rejected because they eliminate too much Industrial Organization content and make producer-rent results less informative.

### Logit/random utility

Rejected as the first repair because the existing pairwise standards-friction map is not directly rationalized by standard product-specific random utility without redesigning the compatibility primitive.

## 8. Preferred minimal Stage 4 architecture

Stage 4R3Q should test **pure-quadratic localized circular competition first**, because it preserves the policy-dependent pairwise friction map exactly and changes only distance curvature.

For an arc of length `ell` between adjacent products `i,j`, a consumer at distance `y` from `i` has utilities

`u_i = A - p_i - tau_ij y^2 + v n_i`,

`u_j = A - p_j - tau_ij (ell-y)^2 + v n_j`.

Hence the raw pairwise boundary is

`y_ij = ell/2 + [p_j-p_i + v(n_i-n_j)] / [2 tau_ij ell]`,

with clipping to `[0,ell]` when a firm captures the full arc.

Everything else is frozen initially:

- 3 firms/countries on the unit circle;
- anchors `(1/6,1/2,5/6)`;
- regimes `IS, SU_12, SU_13, SU_23, SW`;
- the existing standards-depth map into `tau_ij`;
- network matrix `G_rho` and `n=G_rho q`;
- timing `rho -> s -> Tau -> x -> p`;
- quadratic repositioning cost `gamma d_c(x_i,h_i)^2/2`;
- national welfare convention unless the new equilibrium requires a separately documented ownership repair.

This is deliberately **not** yet called an all-product Salop model. Stage 4 must first determine whether the explicit localized quadratic game has a valid pure price continuation for every feasible location history. If it fails, it is killed immediately rather than patched.

## 9. Stage 4R3Q mandatory kill tests

1. Prove or exactly certify pure price equilibrium existence for every feasible positive-length location profile required by unilateral location deviations.
2. Define coincident-location and zero-length-arc cases explicitly; no `None` filtering.
3. Test the former hostile history `x=(2/5,1/2,5/6)` first.
4. Enumerate corners/full-arc capture and verify global price best responses.
5. If one feasible history has no required pure continuation, return `NO-GO` immediately.
6. Only after continuation completeness passes, solve location best responses.
7. Only after location equilibrium passes, re-solve policy, welfare, reversal, and coalition stability.
8. Do not use survival of the old numerical witness as a criterion for accepting the architecture.

## 10. Candidate propositions for Stage 4R3Q

- **Q1 (continuation existence):** For the policy-relevant parameter domain, every feasible distinct location profile admits a pure price Nash equilibrium under localized quadratic transport.
- **Q2 (global location equilibrium):** The induced continuation payoff yields a pure location equilibrium for each relevant standards regime/policy history.
- **Q3 (repositioning relevance):** Endogenous repositioning changes at least one substantive regime comparison relative to fixed positions on a nondegenerate parameter region.
- **Q4 (coalition implication):** Any surviving ranking reversal maps into a coalition-stability implication without relying on the failed linear branch.

Q1 is lexicographically prior. Failure of Q1 kills this architecture even if Q2–Q4 look numerically attractive on selected histories.

## 11. Canonical verdict

**GO — GO TO MINIMAL MODEL.**

Selected architecture: **pure-quadratic localized transport with the existing pairwise standards-friction map**.

Next formal stage: **Stage 4R3Q — Pure-Quadratic Global Continuation Minimal Model Gate**.

No alternative architecture may be added inside that Stage 4 test. If quadratic localized transport fails Q1, return to Stage 3 rather than stacking another existence repair.
