# Stage 4 Minimal Model — Coalition-Scope Implementation Crowd-Out

Date: 2026-09-04  
Status: **AUDITED / C1 FAILS**

## 1. Frozen primitives

Three countries and one firm per country. There are three identical national markets. Every firm serves every market.

Formal regimes:

- international standardization: `rho^IS={{1,2,3}}`;
- regional standardization union after country 3 leaves: `rho_12^SU={{1,2},{3}}`.

Timing:

`rho -> a -> Cournot q -> consumer outcome -> national welfare -> stability`.

Implementation:

`a_i in [0,1]`.

In market `k`:

`p_i^k = 1-Q^k + v a_i sum_{j in C_i(rho), j!=i} q_j^k`.

Firm i pays the same regime-independent implementation cost

`kappa a_i^2/2`.

Firm objective:

`Pi_i=sum_k p_i^k q_i^k-kappa a_i^2/2`.

The clean regularity domain used for the exact comparison is

`0<v<=1/4`, `kappa>0`, `a_i in [0,1]`.

This matches the weak-network domain of benchmark B0 and guarantees simple positivity/monotonicity results. Several algebraic identities below hold on the larger domain `va<1`.

## 2. Cournot continuation — IS

For arbitrary `a_1,a_2,a_3`, define

`D_I=2+v(a_1+a_2+a_3)-v^3 a_1 a_2 a_3`.

The exact quantity of firm 1 in each national market is

`q_1^I=[1+2va_1+v^2(a_1a_2+a_1a_3-a_2a_3)]/(2D_I)`,

with cyclic expressions for firms 2 and 3.

Because the own inverse-demand slope is `-1`, the Cournot FOC gives `p_i=q_i` at every interior continuation equilibrium. Hence total operating profit across the three identical markets is `3 q_i^2`.

At a symmetric implementation profile `a_1=a_2=a_3=a`,

`q_I(a)=1/[2(2-va)]`.

## 3. Cournot continuation — SU_12

For arbitrary member implementations `a_1,a_2`,

`q_1^U=(1+va_1)/[4+v(a_1+a_2)-2v^2a_1a_2]`,

`q_2^U=(1+va_2)/[4+v(a_1+a_2)-2v^2a_1a_2]`,

`q_3^U=(1-v^2a_1a_2)/[4+v(a_1+a_2)-2v^2a_1a_2]`.

At `a_1=a_2=a`,

`q_M(a)=1/[2(2-va)]`,

`q_O(a)=(1-va)/[2(2-va)]`.

The singleton outsider has no eligible interoperability partner, so its revenue is independent of `a_3`. With `kappa>0`, its unique implementation choice is therefore

`a_3^U=0`.

## 4. Reduced implementation game

At a symmetric profile, the private marginal operating-profit return to own implementation is

`MB_I(a)=3v(3-va)/[2(2-va)^3(1+va)]`,

under IS, and

`MB_U(a)=9v/[4(2-va)^3(1+va)]`,

for an SU member.

An interior symmetric implementation equilibrium solves

`kappa a=MB_R(a)`.

Equivalently define

`K_I(a)=3v(3-va)/[2a(2-va)^3(1+va)]`,

`K_U(a)=9v/[4a(2-va)^3(1+va)]`.

Then the interior equations are `K_R(a)=kappa`.

### 4.1 Global own best responses

With rivals fixed at a common `b`, firm 1's Cournot quantity is a linear-fractional function of its own implementation `x`.

Under IS,

`q_1^I(x;b)=[1-bv+2vx]/[2(2+vx-bv^2x)]`.

Under SU,

`q_1^U(x;b)=(1+vx)/[4+v(x+b)-2bv^2x]`.

Define the ratio of own marginal operating-profit benefit to `x` as `K_own(x;b)`. Exact differentiation gives `dK_own/dx<0` for `0<v<1`, `0<b<=1`, `0<x<=1`. Thus the own reduced profit is single-peaked: the global best response is `x=1` when the derivative remains nonnegative at 1 and otherwise the unique interior root.

### 4.2 Symmetric corners and interior roots

Define

`kappa_bar_I=3v(3-v)/[2(2-v)^3(1+v)]`,

`kappa_bar_U=9v/[4(2-v)^3(1+v)]`.

The symmetric continuation candidate is

- `a_I*=1` if `kappa<=kappa_bar_I`, otherwise the unique interior root of
  `2 kappa a(2-va)^3(1+va)=3v(3-va)`;
- `a_U*=1` if `kappa<=kappa_bar_U`, otherwise the unique interior root of
  `4 kappa a(2-va)^3(1+va)=9v`.

On `0<v<=1/4`, both `K_I` and `K_U` are strictly decreasing. The exact derivatives are

`K_I'(a)=-3v[2a^3v^3-7a^2v^2+3]/[a^2(av-2)^4(av+1)^2]<0`,

`K_U'(a)=9v[5a^2v^2-2]/[4a^2(av-2)^4(av+1)^2]<0`.

The own SOC evaluated at an interior symmetric stationary point is

`SOC_I=-3v(av-3)(av-1)/[a(av-2)^4(av+1)]<0`

for `av<1`, and

`SOC_U=9v[6a^2v^2-av-4]/[8a(av-2)^4(av+1)^2]<0`

whenever `av<(1+sqrt(97))/12`, hence throughout `0<v<=1/4`.

## 5. The selected CSIC crowd-out proposition is false

The key exact ratio is

`K_I(a)/K_U(a)=2(3-va)/3`.

Therefore, for `0<va<=1/4`,

`K_I(a)>K_U(a)`

at every common implementation level.

Since both functions are strictly decreasing, their interior roots satisfy

`a_I*>a_U*`.

Corners preserve the weak ordering:

`a_I*>=a_U*`,

with equality only when both are at full implementation.

Thus the Stage-3 target

`a_I*<a_U*`

cannot occur in the audited regular domain. The primitive generates **coalition-scope implementation crowd-in**, not crowd-out.

Economic reason: `a_i` raises only firm i's own network/demand term. It does not directly raise rivals' network value. Enlarging the coalition therefore expands firm i's private reach without introducing the intended direct competition-exposure cost of its own implementation.

## 6. Demand-integrability / consumer-surplus failure

For partner firms 1 and 2 under IS,

`partial p_1 / partial q_2 = -1+v a_1`,

`partial p_2 / partial q_1 = -1+v a_2`.

Hence

`partial p_1/partial q_2 - partial p_2/partial q_1 = v(a_1-a_2)`.

A twice continuously differentiable quasilinear representative utility `U(q;a)` with `p_i=partial U/partial q_i` would require equality of these cross derivatives. The condition fails for exactly the unilateral asymmetric implementation deviations needed to define firms' Stage-2 best responses.

Therefore the one-sided inverse-demand primitive does **not** provide a globally coherent consumer-surplus object for the implementation game. This is not a cosmetic issue because national welfare `W_i=CS_i+Pi_i` is the headline government objective.

## 7. Symmetric-profile welfare diagnostic only

For diagnostic purposes only, a potential can be constructed after fixing a symmetric realized implementation profile.

Let `x=va`.

At symmetric IS,

`CS_I(x)=(9-6x)/[8(2-x)^2]`.

At symmetric SU,

`CS_U(x)=(9-8x+x^2)/[8(2-x)^2]`.

Country 3's national welfare under IS at symmetric `a_I` is

`W_3^I=(15-6x_I)/[8(2-x_I)^2]-kappa a_I^2/2`,

where `x_I=va_I`.

As the SU outsider,

`W_3^U=(15-20x_U+7x_U^2)/[8(2-x_U)^2]`,

where `x_U=va_U` is the implementation of each remaining SU member and the outsider itself chooses `a_3=0`.

These formulas are **equilibrium-consistent diagnostics**, not a repair of the missing global utility microfoundation.

## 8. Endogenous stability diagnostic

For an interior IS equilibrium define `mu=kappa/v^2`. The IS FOC implies

`mu=3(3-x)/[2x(2-x)^3(1+x)]`.

After substitution,

`G_I(x)=W_3^I=-3(2x^3-5x^2-5x+10)/[8(x-2)^3(x+1)]`.

On `0<x<=1/4`,

`G_I'(x)=3x(x^3-x^2-9x+5)/[4(x-2)^4(x+1)^2]>0`,

and `G_I(0)=15/32`.

For the SU outsider define

`B(x)=(7x^2-20x+15)/[8(x-2)^2]`.

Then

`B'(x)=-(4x-5)/[4(x-2)^3]<0`

on `0<x<=1/4`, with `B(0)=15/32`.

Thus every interior endogenous continuation satisfies

`W_3^I>15/32>W_3^U`.

If IS is at the full-implementation corner, its equilibrium condition `kappa<=kappa_bar_I` implies the same strict inequality by bounding its implementation cost with the boundary FOC value.

Therefore, throughout the audited regular domain,

`Delta_3^endo=W_3^I-W_3^U>0`.

The endogenous model does not produce an unstable IS coalition for country 3.

## 9. Full-implementation benchmarks

Two benchmark interpretations matter.

### 9.1 Cost-bearing full-implementation mandate

Set eligible firms' `a=1` and make them bear the same real implementation cost. Country 3's IS-versus-SU payoff difference is

`Delta_3^full,cost = 7v/[8(2-v)] - kappa/2`.

It becomes negative when

`kappa>7v/[4(2-v)]`.

Since `Delta_3^endo>0`, a sign reversal exists for sufficiently large `kappa`.

But this reversal is mechanical: the benchmark forces country 3's firm to buy full implementation and pay `kappa/2`, while the endogenous model allows the firm to reduce implementation expenditure. It does not arise from the C1 reach-versus-competition-exposure mechanism.

### 9.2 Costless/exogenous full interoperability technology

If full interoperability is treated as a fixed technological benchmark rather than a mandated costly private effort, then

`Delta_3^full,tech = 7v/[8(2-v)]>0`.

This has the same sign as `Delta_3^endo` everywhere in the audited domain. There is no stability reversal.

The supposed headline reversal therefore depends on benchmark cost accounting rather than the selected strategic mechanism.

## 10. Numerical audit

`verification/stage04_csic_sympy.py` evaluates 6,000 parameter-grid points over

- `v in (0,1/4]` (25 values),
- `kappa in [10^-4,10]` (240 log-spaced values).

Diagnostic results:

- `a_I<a_U`: 0 cases;
- `Delta_3^endo<0`: 0 cases;
- sign reversal relative to cost-bearing mandated full implementation: 2,428 cases;
- sign reversal relative to costless/exogenous full interoperability: 0 cases.

Example `v=1/5`, `kappa=1/4`:

- `a_I*=0.4600655`;
- `a_U*=0.2306753`;
- `Delta_3^endo=0.0082137>0`;
- `Delta_3^full,cost=-1/36<0`;
- `Delta_3^full,tech=0.0972222>0`.

The numerical work confirms the exact sign logic; it is not used as proof.

## 11. Stage-4 conclusion

C1 fails for three independent reasons:

1. the selected primitive yields `a_I*>=a_U*`, the opposite of coalition-scope implementation crowd-out;
2. the one-sided implementation inverse demand is not integrable under unilateral implementation deviations, so the national consumer-surplus objective is not globally microfounded;
3. the only observed stability reversal is against a benchmark that forces costly full implementation, and the reversal disappears under a costless/exogenous full-interoperability benchmark.

No authorized Stage-4 modification can repair these failures without changing the mechanism. In particular, making interoperability bilateral would be a substantive return to Stage 3 and overlaps the C2/free-riding family.

**Stage-4 verdict: `NO-GO` for C1.**

Route: terminate C1 and return to Stage 3 before selecting or redesigning a genuinely distinct mechanism.
