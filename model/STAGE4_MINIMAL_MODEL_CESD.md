# Stage 4 Minimal Model — C-ESD

Date: 2026-09-04
Status: **GO**

## 1. Frozen game

C-ESD — **Endogenous Standard Differentiation × Strategic Product Repositioning**.

Timing:

`rho -> bloc depths s_C -> Tau(rho,s) -> product locations x_i -> prices p_i -> W_i -> coalition stability`.

Formal partition:

`rho in {IS, SU_12, SU_13, SU_23, SW}`.

Stage-3 policy map is unchanged:

- same bloc `C`: `tau_ij=t_bar-s_C`;
- different blocs `C,D`: `tau_ij=t_bar+(s_C+s_D)/2`;
- `0<=s_C<=s_bar<t_bar`;
- blocs choose depths simultaneously, with `Omega_C=sum_{i in C} W_i`.

No policy cost, relative-profit objective, private interoperability investment, endogenous network intensity, transfer, lobbying, dynamics, topology choice or extra country is added.

## 2. Salop consumer microfoundation

There is a unit circle of product characteristics and unit consumer mass. Country of origin is independent of product taste: each country owns one third of the uniform consumer population. This is the minimal symmetric national-CS allocation required to define `W_i`; it introduces no country-specific taste asymmetry.

Firm anchors are

`h=(1/6,1/2,5/6)`.

Firm `i` chooses `x_i` and pays substantive redesign/repositioning cost

`C_i^D=gamma d_c(x_i,h_i)^2/2`,

where `d_c` is circular distance.

On the Salop arc connecting adjacent products `i,j`, let the arc length be `ell_ij`, and let `y` be distance from `i`. Consumer utility is

`u_i=A-p_i-tau_ij y+v n_i`,

`u_j=A-p_j-tau_ij(ell_ij-y)+v n_j`,

where

`n=G_rho q`.

Compatibility graphs:

- IS: `G_IS=11'`;
- SU_12: `G_SU=[[1,1,0],[1,1,0],[0,0,1]]`;
- SW: `G_SW=I`.

`A` is sufficiently large for full coverage. Since it adds the same constant to all national welfare values, it is suppressed in comparisons.

The indifferent consumer on arc `ij` is

`y_ij=ell_ij/2+[p_j-p_i+v(n_i-n_j)]/(2 tau_ij)`.

Interior demand requires `0<y_ij<ell_ij` on every arc.

## 3. Weighted-Laplacian demand

Let `L(Tau)` be the weighted graph Laplacian with edge weight

`w_ij=1/tau_ij`.

Let `b(x)` be the zero-price/no-network Voronoi share vector. Then the demand system is exactly

`q=b-(1/2)L p+(v/2)L G_rho q`.

Define

`A_rho=I-(v/2)L G_rho`,

`D=-(1/2) A_rho^{-1} L`.

Then

`q=A_rho^{-1}b+D p`.

This nests the Stage-3 homogeneous diagnostic: if every `tau_ij=t`, then `L=(3I-J)/t`.

## 4. Price equilibrium

With zero marginal production cost, operating profit is `p_i q_i`. Because demand is affine in prices,

`d pi_i/dp_i=q_i+D_ii p_i`.

If `D_ii<0`, the own-price SOC is

`d^2 pi_i/dp_i^2=2D_ii<0`.

Define

`M=diag(-1/D_ii)`.

The price FOCs imply

`p=M q`.

Hence

`q=K b`,

where

`K=(I-DM)^{-1} A_rho^{-1}`.

Thus, on the regular domain where `A_rho`, `I-DM` are nonsingular, `D_ii<0`, quantities/prices are positive and all arc boundaries are interior, the price Nash equilibrium is unique.

## 5. Location equilibrium for a fixed cyclic ordering

For cyclic order `1 -> 2 -> 3 -> 1`,

`b(x)=b0+B x`,

with

`b0=(1/2,0,1/2)'`,

and

`B=[[0,1/2,-1/2],[-1/2,0,1/2],[1/2,-1/2,0]]`.

Since `q=K b`, write

`q=c+R x`, `c=K b0`, `R=K B`.

Because `p=Mq`, operating profit is

`pi_i^o=M_ii q_i^2`.

Net firm profit is

`Pi_i=M_ii(c_i+R_i x)^2-gamma(x_i-h_i)^2/2`.

The location FOC is linear:

`2 M_ii R_ii (c_i+R_i x)-gamma(x_i-h_i)=0`.

The own-location SOC is

`2 M_ii R_ii^2-gamma<0`.

Therefore, conditional on a cyclic ordering, the location game is a linear system and has a unique Nash point whenever the coefficient matrix is nonsingular and the SOCs hold.

Stage 4 does not treat this conditional solution as globally sufficient. Every reported witness is also checked against unilateral deviations over the entire circle, including deviations that change the cyclic ordering.

## 6. Consumer surplus and national welfare

Aggregate consumer surplus (dropping common constant `A`) is obtained arc by arc. For arc `ij` with boundary `y_ij`,

`CS_ij=(-p_i+v n_i)y_ij-tau_ij y_ij^2/2`

`      +(-p_j+v n_j)(ell_ij-y_ij)-tau_ij(ell_ij-y_ij)^2/2`.

`CS=sum_edges CS_ij`.

National consumer surplus is `CS/3` by the symmetric national taste normalization.

National welfare is

`W_i=CS/3+Pi_i`.

Foreign-firm profit is excluded.

## 7. Exact symmetric IS and SW blocks

When all products are equally spaced and all pairwise frictions equal `t`:

### IS

`q_i=1/3`, `p_i=t/3`.

The common network size is one, so

`W_i^IS=v/3-t/36`.

Since under IS `t=t_bar-s_I`,

`d W_i^IS/ds_I=1/36>0`.

Therefore

`boxed{s_I^*=s_bar}`.

### Symmetric SW

`q_i=1/3`,

`p_i=(2t-3v)/6`.

The symmetric welfare block is

`W_i^SW=v/9-t/36`.

At the Stage-4 witness and its audited neighborhood, the singleton-government best response is strictly `s_i=0`; unilateral positive specificity lowers national welfare both with fixed and endogenous locations.

## 8. SU strategic repositioning

For `SU_12`, define

`a=tau_12=t_bar-s_12`,

`b=tau_13=tau_23=t_bar+(s_12+s_3)/2`.

Symmetry implies a continuation of the form

`x_1=h_1-d`,

`x_2=h_2+d`,

`x_3=h_3`,

on the regular interior branch.

The exact location FOCs are generated by the linear system in Section 5. In particular, the member displacement is strictly positive in the Stage-4 region: deeper bloc standardization reduces `a`, raises `b`, and the compatible pair moves away from each other and toward the outsider's niche.

This is the strategic re-differentiation channel selected in Stage 3.

## 9. Nested benchmarks

Use identical primitives throughout.

### B-X / B-EXO

`all s_C=0`; locations endogenous.

### B-T

bloc depths endogenous; locations fixed at `h`.

### FULL

bloc depths and locations endogenous.

The Stage-4 contribution test is whether FULL changes coalition stability relative to both B-T and B-X.

## 10. Strict-blocking coalition stability

Retain B0's strict-blocking exclusive-membership logic.

Let

- `W_I` be common IS welfare;
- `W_M` be SU-member welfare;
- `W_O` be SU-outsider welfare;
- `W_W` be common SW welfare.

IS is blocked by a pair if `W_M>W_I`, and by a singleton if `W_O>W_I`.

A symmetric SU is blocked by IS only if all three countries strictly gain, i.e. `W_I>W_M` and `W_I>W_O`. It is broken to SW only if a member can strictly gain, `W_W>W_M`. Alternative SU pair deviations do not strictly block a symmetric SU because the incumbent member would remain at the same member payoff.

SW is blocked by IS if `W_I>W_W` for all countries, or by an SU-forming pair when `W_M>W_W`.

## 11. Stage-4 witness

Normalize

`t_bar=1`,

and take

`boxed{v=0.04, gamma=0.11, s_bar=0.25}`.

All reported price equilibria are interior; all own price/location SOCs hold; and whole-circle one-firm deviation searches find no profitable location jump.

### B-T

Policy equilibrium:

- IS: `s_I=0.25`;
- SU_12: `(s_12,s_3)=(0.25,0)`;
- SW: `(0,0,0)`.

Welfare:

| regime | member / country 1 | outsider / country 3 |
|---|---:|---:|
| IS | -0.007500 | -0.007500 |
| SU | -0.017667 | -0.025410 |
| SW | -0.023333 | -0.023333 |

Hence IS is uniquely stable.

### B-X

All depth choices fixed at zero.

Welfare:

| regime | member / country 1 | outsider / country 3 |
|---|---:|---:|
| IS | -0.014444 | -0.014444 |
| SU | -0.014878 | -0.033413 |
| SW | -0.023333 | -0.023333 |

Again IS is uniquely stable.

### FULL

Policy equilibrium:

- IS: `s_I=0.25`;
- SU_12: `(s_12,s_3)=(0.25,0)`;
- SW: `(0,0,0)`.

SU location equilibrium:

`x^SU=(0.084567, 0.582100, 0.833333)`.

Thus the member-member product distance rises from `1/3` to about `0.49753` on their direct arc. The outsider remains at its inherited anchor.

Welfare:

| regime | member / country 1 | outsider / country 3 |
|---|---:|---:|
| IS | -0.007500 | -0.007500 |
| SU | **-0.005929** | -0.046811 |
| SW | -0.023333 | -0.023333 |

Therefore

`W_M^FULL > W_I^FULL > W_O^FULL`,

and

`W_M^FULL > W_W^FULL`.

The pair of prospective SU members strictly blocks IS. Conversely, the grand coalition cannot block SU because its two members would lose by moving to IS, and a member does not gain by breaking to SW.

Hence

`boxed{S_FULL={SU_12,SU_13,SU_23}}`.

By contrast,

`boxed{S_B-T=S_B-X={IS}}`.

This is the required full-model-only coalition-stability reversal.

## 12. Mechanism decomposition

The reversal does not come from policy choice alone:

`B-T: W_M-W_I = -0.010167 < 0`.

It does not come from location choice alone:

`B-X: W_M-W_I = -0.000434 < 0`.

Only their interaction gives

`FULL: W_M-W_I = +0.001571 > 0`.

The economic chain is:

1. SU depth lowers internal standard friction and raises bloc-boundary friction;
2. that network/friction asymmetry changes the product-location best-response network;
3. SU members strategically re-differentiate in ordinary product space;
4. the repositioning raises member operating profit enough to reverse their national coalition preference;
5. the outsider is harmed, so IS cannot strictly block the resulting SU.

Thus the headline result is not an immediate corollary of either benchmark separately.

## 13. Openness / numerical region

The exact witness inequalities are strict. Continuation equilibrium objects are continuous on the audited regular branch.

A local audit over

- `v in {0.035,0.040,0.045}`;
- `gamma in {0.105,0.110,0.115}`;
- `s_bar in {0.225,0.250,0.275}`

finds 23 of 27 grid points with all three properties:

1. `W_M^FULL>W_I^FULL`;
2. `W_M^B-T<W_I^B-T`;
3. `W_M^B-X<W_I^B-X`;

and with no profitable whole-circle unilateral location deviation at the FULL SU continuation.

A wider 5x5x5 audit around the same region found 108 of 125 passing points. These numerical counts are evidence of a non-knife-edge region, not a substitute for the exact witness and continuity argument.

## 14. Corners and failure region

Low `gamma` can invalidate a local SU stationary point: the outsider may profitably jump to another part of the circle. Stage 4 explicitly found such counterexamples and excludes them from the regular equilibrium region.

This is not repaired by adding another cost or constraint. The admissible Stage-4 region requires the calculated continuation to pass the whole-circle best-response check.

Policy corners are allowed. In the witness region, the equilibrium policy profile naturally has `s_I=s_bar`, `s_12=s_bar`, `s_3=0`, and `s_i^SW=0` without a direct policy cost.

## 15. Candidate proposition disposition

1. **Strategic repositioning:** SURVIVES.
2. **Policy offset / re-differentiation:** SURVIVES in SU.
3. **Regime-specific optimal depth:** SURVIVES.
4. **Endogenous policy can change coalition stability:** SURVIVES.
5. **Endogenous policy × endogenous location interaction is essential:** SURVIVES; B-T and B-X each predict IS, FULL predicts SU.
6. **All local stationary points are equilibria:** REJECTED; low-gamma global-deviation counterexamples exist.
7. **B0 is algebraically nested:** REJECTED; B0 remains an institutional benchmark only.

## 16. Canonical Stage-4 verdict

**GO**.

C-ESD passes the Minimal Model Gate without changing the Stage-3 frozen policy map.

Route:

`GO -> Stage 6 Novelty Re-Kill`.

Stage 6 receives the actual derived result unchanged:

> Endogenous standards depth and endogenous product repositioning interact to reverse standards-coalition stability: in a nonempty regular region, policy-only and location-only benchmarks select IS, while the FULL continuation makes regional SU stable and IS blockable by a pair.
