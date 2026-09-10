# Revival Stage 1 — Audited Source Representation

Date: 2026-09-10

Status: **FROZEN FOR STAGE 2 NOVELTY COMPARISON ONLY — NOT A NEW THEORY FREEZE**

Workflow authority: `ryotamatsuki/research-paper-workflow` v2.1 at `f48984013898696f010f0437a8cfed6b5b54bdc2`.

Source branch: `revival/stage00-coalition-repositioning`, descended from PR #65 head `9f19a82e28415b571a086693323a3377f286fd73`.

This file reconstructs what the PR #65 affine-demand branch actually assumes and supports. It does not authorize a new mechanism, restore the historical manuscript, or inherit any prior Stage 4/8/11/12/13 status.

## 1. Players, regimes, timing, and strategies

There are three countries and one firm owned by each country. Formal standards partitions are

`rho in {IS, SU_12, SU_13, SU_23, SW}`.

The source policy map defines one standards-depth choice `s_C in [0,s_bar]` for each standards bloc `C` in the realized partition. Blocs choose depths simultaneously after the formal partition is fixed. A bloc maximizes the sum of its members' continuation national welfare.

The audited timing is therefore

`rho -> s(rho) -> x -> p -> q,CS,profits -> national welfare -> blocking/stability comparison`.

Product positions satisfy `x_i in S^1`. Firms inherit anchors

`h=(1/6,1/2,5/6)`

and incur repositioning cost

`gamma d_c(x_i,h_i)^2/2`.

Prices are nonnegative.

### Source conflict: singleton depth

The stale Salop manuscript says singleton blocs have no positive depth instrument, while the later Stage-3 policy map and PR #65 `Tau(reg,s)` implementation allow singleton depths under SU/SW. Because PR #65 explicitly retained the later `Tau` policy map, the revival source representation uses the later policy-map convention for audit purposes.

The stale manuscript's singleton-depth statement is therefore **not authoritative for the revival branch**.

## 2. Standards-depth and compatibility objects

For firms `i,j`, let `C(i)` be their standards bloc. The later policy map sets

- within the same bloc `C`: `Tau_ij=t_bar-s_C`;
- across blocs `C != D`: `Tau_ij=t_bar+(s_C+s_D)/2`.

The compatibility graph is discrete:

- `G(IS)=11'`;
- `G(SU_12)` has the `1-2` compatible block and country 3 as singleton;
- `G(SW)=I`;
- other bilateral unions are relabelings.

Crucially, the network-effect coefficient `v G(rho)` is **independent of standards depth** in the PR #65 architecture.

## 3. Representative-consumer demand system

Conditional on `(rho,s,x,p)`, quantities solve

`max_{q>=0} a 1'q - (1/2) q'K(rho,s,x)q - p'q`.

The source curvature matrix is

`K_ii=b`,

`K_ij=c0 + lambda phi(x_i-x_j)/Tau_ij(rho,s) - v G_ij(rho)`,

where

`phi(z)=[1+cos(2*pi*z)]/2`.

At the PR #65 witness,

- `a=2`, `b=10`, `c0=.30`, `lambda=.50`, `v=.08`;
- `gamma=.03`, `t_bar=1`, `s_bar=.25`.

Across the stated policy/location domain, the source bounds give `Tau_ij in [3/4,5/4]` and positive bounded cross-curvatures. The sufficient inequalities

`b>2c_max`,

`b c_min>c_max^2`,

`b-2c_max+c_min>0`

make `K` positive definite and support the gross-substitute sign pattern of `D=K^{-1}` used by the source continuation.

Nonnegative demand is defined by the KKT active-set solution, not by allowing negative affine quantities.

## 4. Bertrand continuation

When all quantities are interior,

`q=D(a1-p)`, with `D=K^{-1}`.

With zero marginal cost and one product per firm, firm `i`'s price FOC is

`q_i-D_ii p_i=0`.

Hence the simultaneous interior candidate is

`p*=[D+diag(D)]^{-1}D(a1)`.

The PR #65 verification layer evaluates nonnegative demand through KKT active sets and attacks representative global unilateral price deviations. Stage 1 re-derived the interior formula and reproduced the canonical positive-price/positive-quantity continuations.

This source result is **correct within the stated regularity architecture**. It is not promoted here to a new independent global-uniqueness theorem; Stage 4A would have to certify any future headline SPNE claim independently.

## 5. Product-repositioning game

Firm `i`'s continuation profit is

`Pi_i=p_i*q_i - gamma d_c(x_i,h_i)^2/2`.

At the historical fixed-depth comparison:

- `IS, s_I=s_bar`: the anchor profile is reproduced as a whole-circle location Nash equilibrium;
- `SU_12, (s_12,s_3)=(s_bar,0)`: members reposition outward while the outsider remains at its anchor.

The fresh Stage-1 verifier reproduces

`x_SU approximately (0.140386,0.526280,0.833333)`.

Thus the nonzero standards-contingent repositioning result is a valid computational source fact.

## 6. Consumer surplus and national welfare

At an interior consumer optimum,

`CS = (1/2) q'Kq`.

Net firm profit includes the repositioning cost above. The inherited national-welfare convention is

`W_i = CS/3 + Pi_i`.

The old Salop manuscript supplied the interpretation that each country contains one third of the consumer population and residence is independent of product taste. The affine re-foundation replaced the spatial demand system with a representative consumer but retained `CS/3`.

Accordingly, `CS/3` is **mathematically consistent if the equal-country consumer aggregation assumption is retained explicitly**. It is not derived from the affine demand system alone. Any future model must state the equal-country market/population aggregation explicitly before using national-welfare or coalition-stability claims.

## 7. Exact Stage-1 diagnosis of IS policy depth

At the symmetric IS anchor profile all pairwise circular proximities satisfy

`phi=1/4`.

Define the common off-diagonal curvature

`c(s)=c0 + lambda/[4(t_bar-s)] - v`.

For a three-product symmetric curvature matrix with diagonal `b` and common off-diagonal `c`, the Bertrand continuation is

`p = a(b-c)/(2b)`,

`q = a(b+c)/[2b(b+2c)]`.

Per-country welfare under the retained equal-consumer-share convention is

`W_IS(c)=a^2(3b^2+2bc-c^2)/[8b^2(b+2c)]`.

Direct differentiation yields

`dW_IS/dc = -a^2(2b^2+bc+c^2)/[4b^2(b+2c)^2] < 0`

for the positive regular domain, while

`dc/ds = lambda/[4(t_bar-s)^2] > 0`.

Therefore, **conditional on the symmetric-anchor IS continuation**, 

`dW_IS/ds < 0`

throughout the admissible interval and the IS bloc selects

`s_I*=0`.

The fresh verifier additionally checks the anchor profile against whole-circle unilateral location deviations at eleven policy nodes from `0` to `s_bar`.

### Interpretation

This is not a canonical-parameter accident. It is generated by the architecture: coalition membership already switches on the full discrete compatibility graph `G(IS)`, while additional depth does not increase `vG`; depth only changes `Tau` and thereby raises competitive substitutability in the PR #65 curvature map.

Thus the observed IS lower-bound policy choice is **structural within this source architecture**, although the all-`s` global location-equilibrium statement remains numerically rather than analytically certified.

## 8. Fixed-depth welfare reversal

Fresh Stage-1 reconstruction reproduces the historical PR #65 result:

- fixed product positions at `(s_I,s_12,s_3)=(s_bar,s_bar,0)` give
  `W_member(SU)-W(IS) approximately -0.0002086344`;
- endogenous locations at those same fixed depths give
  `W_member(SU)-W(IS) approximately +0.0002663570`.

This is a real computational sign reversal at exogenous policy depths. It is not a theorem about the endogenous-depth game.

## 9. Endogenous-depth absorption diagnostic

Using the later policy-map convention, Stage 1 reconstructs the 2026-09-10 policy diagnostic.

At the canonical point:

- IS selects the lower boundary `s_I=0` on the audited symmetric continuation and gives
  `W_i(IS) approximately 0.1434896983`;
- the symmetry-reduced FULL SU candidate at `(s_12,s_3)=(s_bar,s_bar)` has
  `x_SU approximately (0.135440,0.531226,0.833333)` and
  `W_member(SU) approximately 0.1432070478`;
- hence
  `W_member(SU)-W_i(IS) approximately -0.0002826505`.

The verifier finds the expected boundary policy directions on finite grids: member welfare rises with `s_12` along `s_3=s_bar`, outsider welfare rises with `s_3` along `s_12=s_bar`, while the fixed-position benchmark has the member bloc choosing the opposite lower boundary. Across the pre-specified `v x gamma` 3-by-3 box, the FULL candidate member-minus-IS differences remain negative, from approximately `-0.0001863` to `-0.0003791`.

Evidence maturity: **reproducible diagnostic plus exact IS derivative**, not a global analytic theorem for the full SU policy game.

## 10. Coalition blocking / stability concept

The historical manuscript defines strict-blocking, exclusive-membership comparisons and explicitly states two important transitions:

- IS is blocked by an `SU_ij` pair if both prospective members strictly prefer the SU continuation;
- an existing SU is blocked by IS only if all three countries strictly gain from moving to IS.

The later policy-map record says coalition comparisons must use the continuation equilibrium of each alternative partition.

However, the inherited materials do not provide a single fully explicit transition/consent correspondence covering every ordered pair among `IS`, all three SUs, and `SW` after the affine re-foundation. Therefore the **complete stable-partition operator is AMBIGUOUS at Stage 1**.

For the current absorption diagnosis, the relevant IS-versus-SU blocking comparison is sufficiently specified. Before any Stage-4 coalition-stability theorem, the revival must freeze the complete admissible blocking correspondence and consent rule.

## 11. Claim classification

| Inherited object / claim | Stage-1 classification | Reason |
|---|---|---|
| Quadratic representative-consumer demand with KKT nonnegativity | `CORRECT` | Re-derived; convex/concave structure and source implementation align. |
| Uniform positive-definiteness / substitute-sign restrictions | `CORRECT` | Sufficient source inequalities are coherent on the frozen box. |
| Interior Bertrand FOC and closed form | `CORRECT` | Re-derived from `q=D(a1-p)`. |
| Full global Bertrand uniqueness for every history | `CORRECT` as source infrastructure, not newly independently certified | Source architecture and checks support it; future headline SPNE needs Stage 4A. |
| Nonzero SU repositioning at fixed depth | `CORRECT` | Fresh whole-circle BR reconstruction reproduces it. |
| Fixed-depth member-welfare reversal | `CORRECT` computationally | Fresh verifier reproduces both strict signs. |
| `s_I*=0` at the canonical point | `CORRECT` and structurally explained | Exact derivative is negative on the symmetric-anchor continuation. |
| Interpretation of depth as additional interoperability/coherence | `CORRECT BUT ECONOMICALLY AD HOC` in PR #65 mapping | Depth does not raise the network-benefit term; it mainly changes competitive substitutability. |
| `CS/3` national allocation | `AMBIGUOUS` unless equal-country aggregation is explicitly retained | Valid under the inherited equal-population interpretation, not implied by affine demand alone. |
| Singleton-depth rule in stale manuscript | `INCORRECT / STALE FOR PR #65 REVIVAL` | Conflicts with later policy map and `Tau` implementation. |
| FULL SU boundary policy candidate `(s_bar,s_bar)` | `AMBIGUOUS` as a theorem | Supported by finite-grid policy diagnostics, not a continuous global proof. |
| Full stable-coalition reversal under PR #65 | `INCORRECT at the canonical diagnostic` | Endogenous IS depth removes the fixed-depth reversal. |
| Old Salop welfare/stability theorems | `INCORRECT / STALE FOR THIS ARCHITECTURE` | They do not transfer to affine demand. |

## 12. Surviving research question

The source audit sharpens the revival puzzle:

> **Is policy-adjustment absorption a general property of standards-depth / repositioning games, or is it caused by the PR #65 separation in which formal coalition membership supplies compatibility benefits while continuous depth only changes competitive substitutability?**

This is a question for literature and mechanism audit, not a permission to add a direct depth benefit.

A publishable revival would require an economically justified architecture in which product repositioning remains indispensable for coalition-level results after every bloc optimizes its allowed policy instrument, or a theorem characterizing when policy adjustment necessarily absorbs repositioning.

## 13. Stage-2 input map

Stage 2 must compare the audited result against at least:

- Woeckener (1999) and compatibility-before-product-design work;
- standards-coalition formation / network-competition work, including Economides-Skrzypacz and Gandal-Shy lines;
- endogenous differentiation / coalition or alliance models;
- government compatibility-policy / harmonization-depth models;
- the user's own `private-compatibility-standards-coalitions` as a nested coalition benchmark;
- the user's own `standardization-scope-direction-innovation` as internal prior art on a regulator-chosen continuous standardization margin inducing a downstream strategic firm response;
- related policy-adjustment / strategic-response models in industrial organization.

Stage 2 must test whole-game and theorem absorption. It may not treat the combination of familiar ingredients as novelty by itself.

## 14. Stage-1 routing

This audited representation contains a verified residual question and a reproducible source diagnosis. No new primitive has been authorized.

**ROUTE: GO TO STAGE 2 — LITERATURE FRONTIER / NOVELTY KILL GATE.**
