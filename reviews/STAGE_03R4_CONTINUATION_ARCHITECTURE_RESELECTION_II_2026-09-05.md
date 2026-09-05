# Stage 3R4 — Continuation Architecture Re-Selection II

Date: 2026-09-05
Canonical workflow: `ryotamatsuki/research-paper-workflow` v1.2
Prior stage: Stage 4R3Q — `NO-GO`

## 1. Executive verdict

**GO — ABANDON THE SPATIAL PRICE-CONTINUATION ARCHITECTURE AND TEST A QUADRATIC-UTILITY / AFFINE-DEMAND BERTRAND RE-FOUNDATION.**

The project has now killed three variants of the same location-then-spatial-price family at a feasible off-path history: unrestricted linear Salop, localized linear competition, and localized pure-quadratic competition. A fourth curvature or consideration-set patch would be model engineering rather than disciplined repair.

The original linear model with mixed-price continuation is theoretically legitimate but is not selected. The upstream game requires a continuation expected-profit object for every relevant three-firm off-path location history, with policy-dependent pair frictions and network feedback. Existence of a mixed equilibrium is not enough: multiplicity, support changes, and equilibrium selection would enter location and policy payoffs. That changes the technical center of gravity of the paper more than a clean competition-stage re-foundation.

The selected architecture keeps Bertrand price competition, endogenous product repositioning, standards/compatibility, network effects, welfare, and coalition formation, but replaces discrete spatial market allocation with a globally defined differentiated-product demand system derived from strictly concave quadratic utility.

## 2. Binding inherited failures

The following architectures are terminated for the intended pure-strategy SPNE:

1. unrestricted all-product linear Salop continuation;
2. explicit localized linear continuation;
3. explicit localized pure-quadratic continuation.

At `s_I=1/4`, `x=(2/5,1/2,5/6)`, both localized variants have zero pure price Nash equilibria under exact finite candidate enumeration.

This repeated failure is architecture-level evidence. The next candidate must not retain the same clipped local-market price game.

## 3. Candidate set and ranking criteria

Weights fixed before ranking:

- globally complete continuation / uniqueness: 30%
- preservation of standards × repositioning mechanism: 20%
- tractability / reproducibility: 15%
- novelty survival against closest IO literature: 15%
- welfare / coalition interpretability: 10%
- institutional defensibility: 10%

### Candidate table

| Candidate | Core change | Continuation prospect | Mechanism preservation | Main risk | Verdict |
|---|---|---:|---:|---|---|
| A. Mixed-price continuation under original linear spatial game | Keep primitives, allow mixed pricing at bad histories | Existence plausible in principle | Very high | expected continuation payoff/selection for every 3-firm off-path history becomes the paper | **RESERVE / NOT SELECTED** |
| B. Quadratic representative-consumer / affine-demand Bertrand | Replace discrete spatial allocation with globally defined differentiated demand; keep prices | High; strong existence/uniqueness literature | High-medium | close product-variety-network and compatibility literature | **SELECTED** |
| C. Logit/nested-logit Bertrand | Smooth discrete choice | High | Medium-low | pairwise standards-friction map becomes unnatural; redesigns consumer interpretation | KILL as first redesign |
| D. Cournot differentiated products | Replace price stage with quantity competition | High | Medium | loses price-competition mechanism and changes welfare incidence | RESERVE |
| E. Sequential/Stackelberg price stage | Change timing among firms | Medium/high | Medium | arbitrary role asymmetry introduced solely for existence | KILL |
| F. Secure-strategy/non-Nash solution concept | Keep spatial primitives, change equilibrium concept | Solves some nonexistence issues | High | nonstandard equilibrium concept is a larger referee liability than the original problem | KILL |
| G. Regulated/fixed markups | Remove strategic price continuation | High | Low | removes too much IO content | KILL |
| H. Terminate project | Preserve no further sunk-cost bias | Certain | n/a | forgoes potentially distinct standards×repositioning mechanism | SECOND-BEST if Stage 4R4A fails |

## 4. Why mixed pricing is not selected

Mixed strategies are not an illegitimate workaround. Classical Hotelling work shows that randomized-price equilibria can exist when pure price equilibria fail, and Osborne–Pitchik construct an SPNE with pure locations and mixed prices in the two-firm linear Hotelling model.

But the present project requires a substantially harder object:

- three firms rather than two;
- a circle rather than a line;
- policy-dependent compatibility/friction structure;
- endogenous network effects;
- every unilateral location deviation, not only the equilibrium location pair;
- an expected continuation payoff suitable for location, standards-depth, welfare, and coalition-stability calculations.

A proof that *some* mixed price equilibrium exists at every history would still be insufficient if equilibrium payoffs are non-unique. A selection rule added after the fact would be a new primitive with direct consequences for the upstream game.

**Verdict:** preserve mixed pricing as a theoretical reserve, but do not spend the current paper on characterizing a three-firm mixed-price correspondence.

## 5. Selected architecture: quadratic utility / affine-demand Bertrand

### 5.1 Economic interpretation

The circle remains a product-characteristic space used to define pairwise proximity and strategic repositioning, but consumers are no longer partitioned into local arcs. Instead, differentiated products are substitutes in a representative-consumer demand system.

A strictly concave quadratic utility generates globally defined demands. Pairwise product proximity and standards compatibility enter the substitution matrix. Network compatibility enters as a positive cross-consumption/network term. Firms choose prices after standards policy and product repositioning.

This preserves the substantive loop:

`standards architecture -> effective pairwise compatibility/substitutability -> repositioning incentives -> Bertrand prices/profits -> national welfare -> coalition stability`.

It removes the discontinuous whole-market capture logic responsible for the repeated continuation failures.

### 5.2 Minimal Stage 4 skeleton

Let `q >= 0` be the vector of product quantities. For a fixed standards regime `rho`, depth `s`, and product positions `x`, consumer gross utility is provisionally

`U(q;rho,s,x) = a' q - (1/2) q' B(rho,s,x) q + (v/2) q' G_rho q`,

where:

- `a` is the baseline willingness-to-pay vector;
- `B(rho,s,x)` is symmetric and captures own-demand curvature and pairwise substitutability;
- closer product positions increase relevant off-diagonal substitutability;
- standards compatibility affects the same pairwise competitive environment through a pre-specified map, not an ex-post existence restriction;
- `G_rho` is the standards/network compatibility matrix already conceptually present in the project;
- the effective curvature matrix is `K(rho,s,x)=B(rho,s,x)-v G_rho`.

Stage 4 must choose the **simplest pre-registered pairwise map** from circular distance and standards depth into `B_ij`, then prove `K` is positive definite over the entire admissible strategy domain used upstream. No parameter restriction may be chosen merely by searching for the old reversal.

Consumer demand is the solution of

`max_{q>=0} U(q;rho,s,x) - p' q`.

Firms choose `p_i >= 0` simultaneously. Repositioning cost remains `gamma d_c(x_i,h_i)^2/2` at the location stage.

### 5.3 Why this is a recognized IO architecture

This is not an ad-hoc mathematical smoothing device. Relevant prior art includes:

- Caplin–Nalebuff-style/discrete-choice and later uniqueness results for differentiated-product Bertrand price equilibria;
- Farahat–Perakis (2010), who derive a nonnegative extension of affine demand from quadratic representative-consumer utility and prove existence and uniqueness of Bertrand equilibrium;
- Ushchev–Zenou (2018), who construct a product-variety network with linear-quadratic preferences and obtain a unique Bertrand–Nash equilibrium.

Therefore the continuation architecture itself is standard enough to defend. It must **not** be claimed as the paper's novelty.

## 6. Closest prior-art threats created by the redesign

The redesign raises a new novelty risk that is more serious than in Stage 3R3.

### Ushchev and Zenou (2018)

Their product-variety network directly models varieties as nodes linked by substitutability and proves a unique Bertrand equilibrium. A paper that merely says “standards change edges in a product network” would be too close and should be killed.

### Compatibility + product differentiation literature

Baake and Boom (2001) study compatibility decisions, network externalities, endogenous product quality/differentiation, and price competition. Toshimitsu (2016) studies differentiated price/quantity competition with network compatibility effects. Barrett and Yang (2001) connect international product standards, redesign costs, network effects, and multi-attribute competition.

Accordingly, the surviving contribution cannot be generic compatibility + network effects + differentiation.

### Required full-game distance

The project survives only if Stage 4R4A can show that the following **joint strategic loop** is not already absorbed:

1. a standards coalition chooses compatibility/harmonization architecture;
2. firms then strategically reposition product characteristics at a cost;
3. repositioning changes the substitutability network on which subsequent Bertrand competition occurs;
4. the induced profit/consumer-surplus changes feed back into coalition stability or standards incentives;
5. a substantive ranking/reversal or stability threshold exists only because repositioning is endogenous.

If this loop collapses to an immediate corollary of product-variety networks or existing compatibility/differentiation models, terminate the paper.

## 7. Rejected architectures

### Logit / nested logit

These provide attractive price-equilibrium properties, but standard product-specific utility makes the existing pairwise compatibility map less natural. The paper would need to redesign both demand and standards primitives simultaneously.

### Cournot

Technically cleaner, but switching from price to quantity competition changes an economically central strategic margin. It remains a reserve only if the selected Bertrand re-foundation fails for a reason specific to Bertrand.

### Sequential prices

Spatial-competition literature uses sequential roles as an existence remedy, but an exogenous leader/follower ordering among symmetric countries/firms would be difficult to justify institutionally.

### Secure strategies or alternative equilibrium concepts

A nonstandard equilibrium concept would make the paper harder, not easier, to position at IJIO. The canonical objective is a conventional equilibrium architecture with globally defined continuation.

## 8. Stage 4R4A lexicographic kill tests

Next formal stage: **Stage 4R4A — Affine-Demand Bertrand Continuation & Novelty Gate**.

The tests are lexicographic:

### Gate A — Demand well-posedness

1. Specify one minimal map `(rho,s,x) -> B` before numerical search.
2. Prove strict concavity / positive definiteness of `K=B-vG` over the full admissible upstream strategy domain.
3. Define nonnegative demand globally; no interior-demand-only shortcut.

### Gate B — Price continuation

4. Prove or exactly certify existence and uniqueness (or payoff uniqueness) of Bertrand equilibrium for every feasible upstream history.
5. Handle zero-demand products and active-set changes explicitly.
6. `None`, NaN, failed optimization, or invalid active set is `UNRESOLVED`, never an unprofitable deviation.

### Gate C — Endogenous repositioning

7. Only after Gates A–B pass, solve the location/repositioning game globally.
8. Verify that endogenous repositioning is nontrivial rather than mechanically pinned at anchors or maximal differentiation.

### Gate D — novelty kill

9. Re-attack Ushchev–Zenou (2018), Baake–Boom (2001), Barrett–Yang (2001), and differentiated network-compatibility literature using the *actual solved full game*.
10. Require one theorem/result that is unavailable when either standards coalition choice or repositioning is removed.

### Gate E — continuation value

11. Only if A–D pass may policy depth, welfare, reversal, and coalition stability be recomputed.
12. Survival of any old numerical sign is irrelevant to acceptance.

## 9. Success and termination rule

Stage 4R4A returns `GO` only if:

- demand is globally well-defined;
- the Bertrand continuation is globally complete and payoff-unique;
- a nondegenerate repositioning equilibrium exists;
- the full standards-coalition × repositioning interaction survives the closest prior-art attack.

If any one of these fails, the default recommendation is **TERMINATE THIS PAPER**, not another Stage 3 repair cycle. Cournot remains conceptually possible, but after four failed continuation architectures a further refoundation would face severe sunk-cost/model-search concerns.

## 10. Canonical verdict

**GO — GO TO MINIMAL MODEL.**

Selected architecture: **quadratic representative-consumer / nonnegative affine-demand Bertrand with endogenous product repositioning and standards-dependent pairwise substitutability/network structure**.

Next formal stage: **Stage 4R4A — Affine-Demand Bertrand Continuation & Novelty Gate**.
