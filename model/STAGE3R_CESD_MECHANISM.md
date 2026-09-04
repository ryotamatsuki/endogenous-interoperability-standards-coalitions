# Stage 3R C-ESD Mechanism

Date: 2026-09-04
Status: **CONDITIONAL GO — remain at Stage 3**

## 1. Candidate identity

C-ESD is a distinct candidate:

**Endogenous Standard Differentiation × Strategic Product Repositioning**.

The intended full feedback is

`rho -> government standard-friction policy -> firm product locations -> downstream competition -> national welfare -> coalition stability`.

The policy variable is a standard-induced switching/adaptation/differentiation friction. It is not private interoperability investment. The firm variable is product location / product differentiation.

Relative-profit objectives are excluded from the baseline. They may be reconsidered only after the C-ESD core survives.

## 2. Important correction to the proposed B0 nesting claim

The frozen benchmark `ryotamatsuki/private-compatibility-standards-coalitions` does **not** literally contain a Hotelling/Salop transport parameter `t` or endogenous product locations. Its consumer primitive is `u + g_i^k - p_i^k`, with compatibility affecting network value and incompatible foreign products bearing marginal cost `c`; private adoption is binary with fixed cost `F`.

Therefore the identity

`B0 = C-ESD with t fixed`

is not literally true under the current B0 primitives.

B0 remains the mandatory institutional/coalition benchmark, but an exact algebraic nesting claim is prohibited unless Stage 3 resolves a defensible mapping between the new continuous friction policy and B0's binary compatibility/conversion-cost structure.

## 3. Model A kill — standard Hotelling without network effects

Consider a full-coverage quadratic Hotelling duopoly with firms at `x1<x2` and consumer mismatch loss `t(z-x_i)^2`.

The standard price subgame gives

`q1=(2+x1+x2)/6`,

`q2=(4-x1-x2)/6`,

`p1=t(x2-x1)(2+x1+x2)/3`,

`p2=t(x2-x1)(4-x1-x2)/3`.

Hence

`pi1=t(x2-x1)(2+x1+x2)^2/18`.

The policy parameter `t` is a pure multiplicative scale factor in the location objective. Thus firm location best responses are independent of `t` wherever the regular price equilibrium applies.

At a symmetric candidate `x1=a`, `x2=1-a`,

`d pi1/d x1 = -t(4a+1)/6 < 0`.

The firm moves to the boundary (maximum differentiation), and changing `t` does not alter the location choice.

**Conclusion:** Model A fails Kill 1. A government-controlled Hotelling transport coefficient alone does not generate the desired `t -> x*(t)` feedback.

Linear Hotelling has the analogous scale-invariance problem and additionally inherits the familiar location/price-equilibrium difficulties near co-location. It is not promoted.

## 4. Two-firm network extension also fails

Add a market-share network term and allow partial compatibility. Let the effective own-versus-rival network advantage be summarized by `delta=v_n(1-lambda)` and define

`H=t(x2-x1)-delta>0`.

The downstream equilibrium is

`q1=[t(x2-x1)(2+x1+x2)-3 delta]/[6H]`,

`p1=[t(x2-x1)(2+x1+x2)-3 delta]/3`.

Yet at `x1=a`, `x2=1-a`, exact differentiation gives

`d pi1/d x1 = -t(4a+1)/6`.

The symmetric network term cancels from the location incentive.

**Conclusion:** simply adding a symmetric network externality to the two-firm Hotelling line does not rescue the mechanism.

## 5. Positive diagnostic — three-firm Salop with regime-specific compatibility networks

A qualitatively different result appears once the three-country standards architecture creates an asymmetric compatibility network under `SU`.

Use a unit Salop circle with three firms and linear mismatch loss. For a given ordered location vector, let `b(x)` be the vector of zero-price Voronoi market shares. With market-share network effects, the demand system can be written

`q = b - H3 p/(2t) + v H3 G q/(2t)`,

where

`H3=3I-J`

and `G` maps product shares into compatible network sizes.

Use

- `G_IS = 11'` (all three compatible),
- `G_SW = I` (three separate networks),
- `G_SU12 = [[1,1,0],[1,1,0],[0,0,1]]` (firms 1 and 2 compatible; firm 3 outsider).

Let

`r=v/t`.

At equal spacing and with orientation `x3=0 < x1=1/3 < x2=2/3`, the normalized unilateral own-location operating-profit gradients are

`(1/t) d pi1/dx1 = 0` under IS,

`(1/t) d pi1/dx1 = 0` under SW,

while under `SU12`,

`(1/t) d pi1/dx1 = r(3r-2)(12r-7) / [6(2r-1)(6r-5)^2]`.

For the regular diagnostic domain

`0<r<1/2`,

this expression is strictly negative. The compatible member located at `1/3` wants to move toward the outsider and away from its compatible partner. The other coalition member moves in the opposite direction. Thus the compatible pair expands its product-space distance and compresses the outsider's niche.

This is a genuine **regime-specific strategic re-differentiation** effect:

- absent under symmetric IS;
- absent under symmetric SW;
- present under asymmetric SU.

Moreover,

`d/dr[(1/t)d pi1/dx1]`

is strictly negative on `0<r<1/2`. Since `r=v/t`, lowering `t` (deeper standardization / lower standard-induced friction) strengthens the SU repositioning incentive.

This passes the cheap mechanism test that the two-firm Hotelling models failed.

## 6. Why an unanchored circle is not yet a full model

The unanchored three-firm location game is not suitable for Stage 4 as written.

At symmetric IS/SW the equal-spacing location gradient is zero by symmetry; under SU the network asymmetry creates a strict directional force, but without a technologically meaningful repositioning friction or feasible product-design constraint, firms can be pushed toward ordering boundaries / corner configurations.

A symmetric stationary point is therefore not enough.

## 7. Preferred regularization — inherited product/technology anchors

A defensible candidate is an anchored Salop model. Give each firm an inherited brand/technology position `h_i` and allow it to choose `x_i` at redesign/repositioning cost

`C_i^D = gamma (x_i-h_i)^2/2`.

Interpretation: changing product architecture, interface design, brand positioning, or installed complementary design away from an inherited platform is costly.

This cost is **not** a novelty claim and must not be introduced merely to manufacture an interior optimum. Barrett–Yang-type standards models already use redesign costs. Stage 4 would have to defend it as an actual product-design friction and audit boundary alternatives.

For the SU member, local concavity at equal spacing requires `gamma` to dominate the convexity of operating profit. The exact local threshold derived by the diagnostic is

`gamma > r^2 t (3r-2)(12r-7)^2 / [4(2r-1)(6r-5)^2(9r-5)^2]`.

## 8. Numerical witness for strategic repositioning

Using inherited anchors

`h=(1/6,1/2,5/6)`,

`v=0.05`, `gamma=0.5`,

the numerical location Nash diagnostic gives approximately:

| regime | t | x1 | x2 | x3 | member distance x2-x1 |
|---|---:|---:|---:|---:|---:|
| IS | 0.5,1,2 | 0.16667 | 0.50000 | 0.83333 | 0.33333 |
| SW | 0.5,1,2 | 0.16667 | 0.50000 | 0.83333 | 0.33333 |
| SU12 | 0.5 | 0.15597 | 0.51069 | 0.83333 | 0.35472 |
| SU12 | 1.0 | 0.15668 | 0.50999 | 0.83333 | 0.35332 |
| SU12 | 2.0 | 0.15699 | 0.50968 | 0.83333 | 0.35269 |

Lower `t` induces stronger outward repositioning of the compatible pair. The response is partial: the product-space movement offsets some of the direct fall in standard-induced differentiation but does not mechanically force complete offset.

This is a mechanism witness, not a Stage-4 equilibrium theorem.

## 9. Network-effect necessity test

For the selected three-firm architecture, Model A without the compatibility-network channel does not produce the regime-specific location force. The asymmetry arises because SU changes which products share network value.

Therefore the current preferred minimal candidate is not `endogenous t x endogenous x` alone. It is:

**three-firm standards regime × network compatibility × endogenous product repositioning**.

Network externality is a necessary ingredient for the surviving diagnostic, though it is not itself a novelty claim.

## 10. Single unresolved architecture condition

The firm-side mechanism survives, but the government policy stage is not yet well-defined enough for Stage 4.

A single scalar `t_rho` is ambiguous under SU. There are at least two economically distinct pair types:

- the compatible member-member pair;
- member-outsider pairs.

Stage 3 must freeze exactly how formal standards policy maps into pairwise standard-induced frictions and who chooses them. Examples that must be compared rather than silently assumed include:

1. a bloc chooses an internal compatibility-depth instrument while external friction is inherited;
2. policy intensity `s` transforms a baseline friction matrix, lowering within-bloc friction and potentially raising cross-bloc friction;
3. governments choose pairwise recognition depth subject to the formal partition.

The selected map must also define IS and SW symmetrically, specify whether bloc choices are cooperative or noncooperative, and produce well-defined national continuation welfare.

This is one coherent unresolved architecture question: **the policy/benchmark mapping of continuous standard differentiation under IS/SU/SW**.

Until it is resolved, `t_IS*`, `t_SU*`, `t_SW*`, national `W_i`, and coalition deviations are not uniquely defined.

## 11. Nested-benchmark status

- `B-X` (exogenous standard friction, endogenous product positions): firm-side diagnostic is available.
- `B-T` (endogenous standard policy, fixed product positions): cannot be canonically solved until the policy map is frozen.
- `FULL` (endogenous policy and positions): not yet authorized.
- B0 is an institutional coalition benchmark, not yet a literal algebraic nested benchmark.

## 12. Stage-3R disposition

**CONDITIONAL GO.**

Positive findings:

1. standard two-firm Hotelling variants are killed cleanly rather than rescued ad hoc;
2. three-firm SU network asymmetry generates an exact, nonzero, regime-specific repositioning incentive;
3. lower `t` strengthens that incentive;
4. an economically interpretable inherited-position friction yields a stable numerical witness with `dx*/dt != 0` under SU;
5. IS/SW do not mechanically share the same repositioning force.

Why this is not `GO` yet:

1. the continuous government policy instrument is not uniquely mapped to the IS/SU/SW partition;
2. therefore national welfare and coalition-stability reversal cannot yet be audited;
3. B0 is not literally recovered by simply fixing `t`.

**Stage 4 is not authorized.** Resolve the policy/benchmark mapping at Stage 3. If a clean mapping survives and produces a full interaction result beyond fixed-location and fixed-policy benchmarks, promote C-ESD to Stage 4. Otherwise terminate it.