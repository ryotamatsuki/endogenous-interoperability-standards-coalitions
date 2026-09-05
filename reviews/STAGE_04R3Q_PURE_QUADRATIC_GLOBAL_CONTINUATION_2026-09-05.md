# Stage 4R3Q — Pure-Quadratic Global Continuation Minimal Model Gate

Date: 2026-09-05
Canonical workflow: `ryotamatsuki/research-paper-workflow` v1.2
Prior stage: Stage 3R3 — `GO`
Selected architecture: pure-quadratic localized circular competition

## 1. Executive verdict

**NO-GO.**

The pure-quadratic localized continuation architecture fails the lexicographically first continuation-existence gate. At the same feasible off-path IS location history that killed the linear architectures, the quadratic localized price subgame has **no pure Nash equilibrium**.

This result is enough to reject Q1. Stage 4R3Q therefore stops immediately. Location best responses, policy choice, welfare, reversal, and coalition stability are not re-solved under this architecture.

## 2. Tested primitives

No second repair is added.

At IS with `s_I=1/4`, all pair frictions are `tau=3/4`. At the feasible distinct location profile

`x=(2/5,1/2,5/6)`,

the clockwise arc lengths are

`ell_01=1/10`, `ell_12=1/3`, `ell_20=17/30`.

Consumers on each arc compare only the two products bounding that arc. On an arc `(i,j)` of length `ell`, utilities are

`u_i=A-p_i-tau*y^2+v*n_i`,

`u_j=A-p_j-tau*(ell-y)^2+v*n_j`.

Under IS the network term is common across products and cancels from pairwise choice. The raw share of firm `i` on the arc is therefore

`ell/2 + (p_j-p_i)/(2*tau*ell)`,

clipped to `[0,ell]`.

Hence an arc-share kink occurs when

`p_i-p_j = +/- tau*ell^2`.

## 3. Interior stationary candidate is not Nash

Solving the three interior price FOCs gives the unique stationary candidate

`p=(816/17975, 1167/28760, 7939/86280)`

or approximately

`(0.0453964, 0.0405772, 0.0920132)`.

Firm 0's profit at that candidate is

`208896/12924025 ≈ 0.0161634`.

Its exact global best response is instead

`p_0'=95727/575200 ≈ 0.166424`,

which yields

`539038737/16542752000 ≈ 0.0325846`.

Thus the regular interior branch is not a price Nash equilibrium even after replacing linear distance by pure quadratic distance.

## 4. Exact pure-equilibrium nonexistence certificate

The failure is not inferred from the stationary candidate alone.

For each arc, the relevant active status is one of:

- left firm gets zero;
- interior split;
- left firm gets the whole arc.

There are therefore `3^3=27` global arc active states.

Holding rival prices fixed, each firm's total demand is the sum of two clipped affine functions of its own price. Own-price profit is therefore continuous and piecewise quadratic on the nonnegative price domain.

Every global best response must lie at one of six necessary candidate modes:

1. interior FOC;
2. `p_i=0`;
3–6. one of four incident arc-share kinks.

The exact verifier `verification/stage04r3q_quadratic_price_nonexistence.py` enumerates every combination of the 27 global active states and these six necessary optimality equations per firm. It solves all nonsingular systems with exact SymPy rational arithmetic and then checks every surviving candidate against the exact global best-response correspondence.

Results:

- nonsingular candidate systems solved: **2440**;
- pure price Nash equilibria found: **0**.

No `None`, optimizer nonconvergence, invalid branch, NaN, or numerical failure is used as negative evidence.

## 5. Why the classical quadratic-existence intuition does not rescue this architecture

Stage 3R3 selected quadratic curvature because it is a recognized existence remedy in standard spatial price competition. That rationale was legitimate as a candidate-selection criterion, but it was never treated as a theorem for this model.

The actual architecture here combines three firms, circular localized consideration, unequal off-path arc lengths, and the project's policy-dependent pair-friction structure. The exact hostile-history calculation shows that these features are enough for the selected localized price game to retain a pure-continuation failure.

Therefore the paper may cite the classical quadratic literature as motivation for why this candidate was tested, but it may not cite that literature as establishing continuation existence here.

## 6. Canonical gate result

Stage 3R3 Q1 was:

> every feasible distinct location profile required by unilateral location deviations admits a pure price Nash equilibrium under localized quadratic transport.

Q1 is false because the feasible history `x=(2/5,1/2,5/6)`, `s_I=1/4` has no pure price Nash equilibrium.

Under the Stage 3R3 contract, one such history kills the architecture immediately.

## 7. What is not claimed

This stage does **not** show that:

- no mixed price equilibrium exists;
- every quadratic spatial-competition model lacks a pure equilibrium;
- the standards/repositioning research question is intrinsically impossible;
- no alternative competition architecture can work.

It establishes only what is needed for the gate: the selected pure-quadratic localized architecture cannot support the intended pure-strategy SPNE.

## 8. Downstream status

Not authorized:

- location-equilibrium reconstruction;
- policy-depth equilibrium;
- welfare decomposition;
- regime-ranking reversal;
- coalition-stability theorem;
- new theory freeze;
- IJIO submission.

All old numerical results remain historical diagnostics only.

## 9. Verdict and routing

**STAGE 4R3Q NO-GO — DO NOT SUBMIT.**

Do not harden or patch this architecture inside Stage 5.

Return to **Stage 3R4 — Continuation Architecture Re-Selection II** if the project is to continue.

The reserve candidates inherited from Stage 3R3 are:

1. mixed-price continuation under the original linear architecture;
2. a broader redesign of the competition stage with global pure-equilibrium existence.

Any new Stage 3 choice must be evaluated as a distinct architecture, not as another local patch designed around the hostile history.
