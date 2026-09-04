# Stage 3R Candidate — Relative-Profit-Induced Interoperability Restraint

Date: 2026-09-04
Status: **REJECTED AT STAGE 3 RE-ENTRY / NO-GO**

## Proposed mechanism

The candidate attempted to exploit the fact that interoperability can raise rival firms' profits. If firms maximize relative rather than absolute profit, this creates an additional negative term in the private implementation incentive.

The clean preferred objective was

`U_i = Pi_i - (alpha/2) sum_{j!=i} Pi_j`, `0<=alpha<1`,

with a fixed global reference set. The reference set was deliberately kept independent of formal coalition membership to avoid mechanically changing preferences when the standards partition changes.

## Neutral bilateral technology

The C2 integrable bilateral technology was retained as a technology only:

`A_ij = a_i + a_j - a_i a_j = 1-(1-a_i)(1-a_j)`.

Inverse demand:

`p_i=1-Q+v sum_{j in C_i(rho),j!=i} A_ij q_j`.

Because `A_ij=A_ji`, cross effects are symmetric and the consumer side is integrable:

`U_cons(q;a)=Q-Q^2/2+v sum_{i<j} A_ij q_i q_j`.

Thus C-RP does not inherit C1's welfare-microfoundation defect.

## Exact symmetric quantity continuation under full RP

Let

`z = v(2a-a^2)`.

Under IS:

`q_I = 1/[4-alpha-(2-alpha)z]`.

Under `SU_12` with symmetric member implementation `a`:

`q_M = (alpha+2)/[8-4z+2alpha(1+z)-alpha^2]`,

`q_O = [2-2z+alpha(1+z)]/[8-4z+2alpha(1+z)-alpha^2]`.

These expressions use the relative-profit objective consistently in the quantity stage.

## Exact symmetric implementation marginal returns

Before subtracting `kappa a`, the Stage-1 implementation marginal return under IS is

`MB_I = 3 v (2-alpha)(1-a)[2+alpha(1-z)][4+alpha(alpha-2)(1-z)] / {[4-2z-alpha(1-z)]^3 [2+2z+alpha(1-z)]}`.

Under SU for a coalition member:

`MB_U = 3 v (2-alpha)(1-a)(alpha+2)^3(alpha^2-2alpha+4) / {2[8-4z+2alpha(1+z)-alpha^2]^3}`.

At `alpha=0`, their ratio collapses exactly to the C2 result

`MB_I/MB_U = 2/(1+z)`.

On the regular diagnostic domain `0<=alpha<1`, `0<v<=1/4`, `0<=a<=1`, the numerical interval audit found

`MB_I/MB_U >= 1.6`,

with the minimum attained at the profit-maximizing baseline `alpha=0`, `z=1/4`. Positive relative-performance concern does not overturn the larger-coalition implementation advantage; it tends to increase the ratio.

## Artifact benchmark — RP only in implementation objective

To isolate the proposed direct rival-profit-spillover channel, hold the downstream quantity stage at ordinary-profit Cournot and use relative profit only to evaluate implementation.

Then

`MB_I^impl = 3v(1-a)(2-alpha z)/[2(1+z)(2-z)^3]`,

`MB_U^impl = 3v(1-a)(2-alpha z)/[4(2-z)^3]`.

Therefore

`MB_I^impl/MB_U^impl = 2/(1+z)`,

which is completely independent of `alpha`.

This is the decisive mechanism diagnostic: the direct relative-profit penalty attached to rival gains scales implementation incentives but does not generate the required regime-differential reversal. When RP is also allowed to alter the Cournot subgame, the IS/SU marginal-return ratio moves further above one rather than below it.

## Prior-art burden

The candidate also faces a crowded prior family:

- Matsumura, Matsushima and Cato (2013), `Competitiveness and R&D competition revisited`, Economic Modelling 31:541-547, DOI `10.1016/j.econmod.2012.12.016`, studies two-stage R&D under relative-profit objectives, oligopoly and joint R&D.
- Shibata (2014), `Market structure and R&D investment spillovers`, Economic Modelling 43:321-329, DOI `10.1016/j.econmod.2014.08.014`, explicitly combines investment spillovers with a relative-profit/competition parameter.
- Sun and Zhao (2024), `Relative performance evaluation in spillover networks`, Games and Economic Behavior 145:285-311, DOI `10.1016/j.geb.2024.03.009`, studies effort spillovers together with relative-performance compensation in networks.

Therefore `relative profit changes investment when investment affects rivals` is not available as a contribution claim. Only a new government standards-coalition stability result could have saved C-RP.

## Numerical diagnostic

A 6,000-point grid was run over:

- `v in [0.005,0.25]`;
- `alpha in [0,0.95]`;
- `kappa in [10^-3,10]`.

Results:

- `a_IS<a_SU`: 0;
- `Delta_3^endo<0`: 0;
- stability reversal relative to the same model at `alpha=0`: 0;
- stability reversal relative to costless/exogenous full interoperability at the same `alpha`: 0.

The minimum recorded `Delta_3^endo` was positive and approached zero only near vanishing interoperability effects / very high implementation cost.

## Disposition

**NO-GO.**

C-RP repairs the bilateral welfare structure but does not create the desired regime-dependent implementation restraint. The direct implementation-spillover channel cancels from the IS/SU ratio in the implementation-only benchmark, while consistent full relative-profit competition strengthens rather than reverses the IS implementation incentive.

Do not proceed to Stage 4 on C-RP.

Do not rescue the mechanism by making the relative-profit reference group coalition-dependent, endogenizing `alpha`, adding capacity/scope costs, or introducing a shared gateway. Those are distinct mechanisms requiring a new Stage-3 comparison.