# Stage 5RR — Localized-Competition Continuation Hardening

Date: 2026-09-05
Canonical workflow: `ryotamatsuki/research-paper-workflow` v1.2
Baseline main SHA: `7d8cc4b9d2b98daeab287481aea4271b62f52b4a`

## 1. Executive verdict

**NO-GO.**

The single Stage 4RR repair candidate — explicit localized competition in which consumers on each arc compare only the two products bounding that arc — does not restore a complete pure-strategy price continuation.

At the hostile feasible IS history `x=(2/5,1/2,5/6)`, `s_I=1/4`, the old interior price candidate remains vulnerable to a different exact deviation, and an exhaustive finite enumeration of every necessary pure best-response candidate finds no pure price Nash equilibrium.

This is not a failure of arithmetic at the canonical path. It is a continuation-existence failure at a feasible off-path location history needed by the location game.

## 2. Previous failure

Stage 4RR established that standard unrestricted all-product choice defeats the old local-interior price candidate through a large price cut. It therefore tested one bounded repair: make localized competition an explicit primitive.

The allowed Stage 5RR modification was exactly one change:

> Consumers located on a positive-length arc bounded by two firms consider only those two firms in the price subgame.

All policy, location, network, welfare, and coalition primitives were frozen.

## 3. Why this modification was economically defensible enough to test

Localized/limited-information competition is a recognized modeling device in the circular spatial-competition literature. In particular, de Frutos, Hamoudi and Jarque (2002, *Regional Science and Urban Economics*, 32(4), 531–540, DOI `10.1016/S0166-0462(01)00094-1`) explicitly analyze an oligopoly extension under limited consumer information in which consumers compare only the two closest firms.

However, their oligopoly section fixes firms at equidistant locations and does not solve the endogenous location-then-price problem required here. Thus the literature supports the primitive as recognizable but does not supply the missing continuation theorem.

## 4. Smallest revised price block

For an arc of length `ell_ij` between neighboring firms `i` and `j`, localized demand assigns the arc boundary

`y_ij = clip(ell_ij/2 + (p_j-p_i + v(N_i-N_j))/(2 tau_ij), 0, ell_ij)`.

Firm `i` receives `y_ij` from the clockwise `(i,j)` arc and the complementary/localized share from its other neighboring arc.

At IS, `G=1`, so `N_i=N_j` for all firms and the network term cancels from pairwise choice. At the hostile history the price game is therefore exactly a continuous piecewise-quadratic game with rational coefficients.

## 5. Exact counterexample after localization

Old candidate:

`p=(1/4,43/200,57/200)`.

Firm 1 (index 0) has old demand `1/3` and operating profit

`Pi_1 = (1/4)(1/3)=1/12 = 0.083333...`.

Let firm 1 raise its price to

`p_1'=71/200 = 0.355`.

It then optimally gives up the short arc of length `1/10` against firm 2, while retaining a localized share `71/300` on its long arc against firm 3. Hence

`q_1'=71/300`,

`Pi_1'=(71/200)(71/300)=5041/60000 = 0.0840166... > 1/12`.

Thus the old interior candidate is not a Nash equilibrium even under the localized primitive.

Authority: `verification/stage05rr_localized_price_nonexistence.py`.

## 6. Exhaustive pure-price-equilibrium audit

The localized IS price game at this history has three arcs. Each arc has exactly three active states:

1. first endpoint gets zero;
2. interior split;
3. first endpoint captures the whole arc.

Therefore there are `3^3=27` global arc active states.

For any fixed state, each firm's demand is affine in prices and profit is quadratic in its own price. A global nonnegative best response must therefore occur at one of:

- an interior FOC;
- `p_i=0`;
- one of the four incident-arc kinks `p_i-p_j=+/-tau*ell_ij`.

That gives six necessary optimality equations per firm. Stage 5RR enumerates all `27 * 6^3` state/mode combinations, solves every nonsingular three-equation system exactly with SymPy rationals, rejects negative-price candidates, and verifies every surviving solution against the exact global best-response correspondence.

Nonsingular systems solved exactly: **2440**.

Pure price Nash equilibria found: **0**.

The enumeration is finite and exhaustive for pure strategies because each firm's payoff is continuous and piecewise quadratic with kinks only at the four incident share-boundary prices plus the nonnegative-price boundary.

This does not rule out mixed price equilibria.

## 7. What changed relative to Stage 4RR

Stage 4RR showed only that the particular all-product undercutting deviation disappears under localized choice.

Stage 5RR establishes the stronger adverse result:

- a different profitable deviation remains at the old price candidate; and
- more importantly, there is no alternative pure price equilibrium at the hostile feasible history under the localized repair.

Therefore the original continuation-completeness blocker survives.

## 8. New artefact risks

None are used to reach the verdict. In particular:

- no failed solver call is counted as an unprofitable deviation;
- no numerical optimizer is used to establish nonexistence;
- no regular active branch is silently extrapolated;
- the hostile history is feasible under the original location strategy set;
- the conclusion is limited to pure price equilibrium at this history.

## 9. New closest-literature threat

The limited-information/localized-competition primitive is itself known, especially de Frutos, Hamoudi and Jarque (2002). Therefore adopting it would not add novelty. It was considered only as a repair device.

The closest-paper check also reinforces the NO-GO: the known result treats equidistant fixed locations and therefore does not provide a theorem that rescues pure price continuation after arbitrary endogenous location deviations.

## 10. Surviving propositions

No SPNE, coalition-stability, or headline reversal proposition is restored by Stage 5RR.

Conditional arithmetic on the former maintained branch remains historical diagnostic evidence only.

## 11. Remaining blocker

The blocker is no longer suitable for another Stage 5 modification. The one permitted repair has failed.

To continue the research, one must change a more fundamental element — for example transport-cost curvature, price equilibrium concept (mixed strategies), location strategy domain, or competition microfoundation. Any such move is a distinct mechanism/model architecture and must return to Stage 3 rather than being stacked onto Stage 5RR.

## 12. Canonical verdict and route

Canonical Stage 5 verdict: **NO-GO**.

Route: **return to Stage 3 for a distinct continuation architecture, or terminate this paper in its current form.**

Stage 6 novelty re-kill is not authorized. Stage 8 freeze remains open. Stage 13/14 remain blocked.
