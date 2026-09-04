# Stage 4 — Minimal Model Gate: C-ESD

Date: 2026-09-04
Canonical workflow: `ryotamatsuki/research-paper-workflow` v1.1
Release SHA: `488e5ab06c207909296a7564eaf9066f7f94319c`

## Executive verdict

**GO -> Stage 6 Novelty Re-Kill.**

C-ESD survives Stage 4. The frozen Stage-3 architecture generates a genuine FULL-only coalition-stability reversal without adding policy costs, relative profit, private interoperability investment, endogenous network intensity, transfers, dynamics, topology choice or extra countries.

The surviving theorem candidate is:

> In a nonempty regular parameter region, government standard-depth choice alone (B-T) and strategic product-location choice alone (B-X) each leave international standardization uniquely stable, while their interaction in the FULL game induces regional-standardization members to re-differentiate sufficiently strongly that a pair strictly prefers SU to IS. The stable set switches from IS to the three symmetric SUs.

## 1. Exact model

Formal regime:

`rho in {IS,SU_12,SU_13,SU_23,SW}`.

Frozen policy map:

- same bloc `C`: `tau_ij=t_bar-s_C`;
- different blocs `C,D`: `tau_ij=t_bar+(s_C+s_D)/2`;
- bloc policy Nash: `max_{s_C} sum_{i in C} W_i`.

Firm anchors:

`h=(1/6,1/2,5/6)`.

Firm redesign/repositioning cost:

`gamma d_c(x_i,h_i)^2/2`.

Formal compatibility graph determines network size; the network coefficient `v` is fixed with respect to policy depth.

## 2. Demand microfoundation

Consumers are uniformly distributed on a unit Salop circle. National origin is independent of product taste; each country owns one third of consumer mass. This supplies the minimal symmetric national-CS allocation needed for `W_i=CS_i+Pi_i`.

On arc `ij`, utility is

`u_i=A-p_i-tau_ij y+v n_i`,

`u_j=A-p_j-tau_ij(ell_ij-y)+v n_j`.

The boundary is

`y_ij=ell_ij/2+[p_j-p_i+v(n_i-n_j)]/(2tau_ij)`.

Let `L(Tau)` be the weighted Laplacian with `w_ij=1/tau_ij`. Then

`q=b-(1/2)Lp+(v/2)LGq`.

Thus

`q=A_rho^{-1}b+Dp`,

where

`A_rho=I-(v/2)LG`,

`D=-(1/2)A_rho^{-1}L`.

This is the exact heterogeneous-friction extension of the Stage-3 homogeneous Salop diagnostic.

## 3. Price stage

Price FOC:

`q_i+D_ii p_i=0`.

Price SOC:

`2D_ii<0`.

Set

`M=diag(-1/D_ii)`.

Then

`p=Mq`,

`q=Kb`,

`K=(I-DM)^{-1}A_rho^{-1}`.

Therefore the regular price subgame has a unique Nash equilibrium when the listed matrices are nonsingular, `D_ii<0`, prices/quantities are positive and all Salop boundaries are interior.

## 4. Location stage

For a fixed cyclic ordering,

`b=b0+Bx`.

Hence

`q=c+Rx`,

and

`Pi_i^operating=M_ii(c_i+R_i x)^2`.

The location FOC is linear:

`2M_iiR_ii(c_i+R_i x)-gamma(x_i-h_i)=0`.

The own SOC is

`2M_ii R_ii^2-gamma<0`.

The conditional location Nash point is therefore obtained from a linear system.

Stage 4 additionally searches the entire circle for each firm's unilateral deviation. This matters: some low-gamma stationary points fail the global test because the outsider can jump to a different cyclic-order region. Such points are rejected rather than repaired.

## 5. Exact symmetric benchmark blocks

At equal spacing and common pairwise friction `t`:

### IS

`q_i=1/3`, `p_i=t/3`,

`W_i^IS=v/3-t/36`.

Since `t=t_bar-s_I`,

`s_I^*=s_bar` exactly.

### SW

`q_i=1/3`,

`p_i=(2t-3v)/6`,

`W_i^SW=v/9-t/36`.

At the Stage-4 witness and audited neighborhood, each singleton's global policy best response is `s_i=0` in both B-T and FULL.

## 6. SU continuation

For `SU_12`,

`tau_12=t_bar-s_12`,

`tau_13=tau_23=t_bar+(s_12+s_3)/2`.

On the regular symmetric branch,

`x_1=h_1-d`,

`x_2=h_2+d`,

`x_3=h_3`,

with `d>0` under the selected mechanism region. Thus members re-differentiate in ordinary product space as their standards become internally closer and externally farther from the outsider.

## 7. National welfare

Aggregate CS is integrated exactly arc by arc. National consumers receive one third of aggregate CS. Domestic firm worldwide operating profit net of redesign cost is included; foreign profit is excluded:

`W_i=CS/3+Pi_i`.

The omitted gross-utility constant is common to all regimes and has no effect on policy or stability comparisons.

## 8. Nested benchmarks

- `B-T`: policy depths endogenous; locations fixed at anchors.
- `B-X`: all policy depths fixed at zero; locations endogenous.
- `FULL`: both policy depths and locations endogenous.

B0 remains the mandatory institutional IS/SU/SW coalition benchmark but is not algebraically nested because its demand/adoption primitives differ.

## 9. Stage-4 witness

Normalize `t_bar=1` and set

`v=0.04`,

`gamma=0.11`,

`s_bar=0.25`.

### B-T

Policy equilibrium:

- IS: `s_I=0.25`;
- SU: `(s_12,s_3)=(0.25,0)`;
- SW: `(0,0,0)`.

Continuation welfare:

`W_IS=-0.007500`,

`W_SU_member=-0.017667`,

`W_SU_outsider=-0.025410`,

`W_SW=-0.023333`.

Thus IS is uniquely stable.

### B-X

At zero policy depth:

`W_IS=-0.014444`,

`W_SU_member=-0.014878`,

`W_SU_outsider=-0.033413`,

`W_SW=-0.023333`.

Again IS is uniquely stable.

### FULL

Policy equilibrium remains

- IS: `s_I=0.25`;
- SU: `(s_12,s_3)=(0.25,0)`;
- SW: `(0,0,0)`.

But SU firms reposition to approximately

`x^SU=(0.084567,0.582100,0.833333)`.

Continuation welfare becomes

`W_IS=-0.007500`,

`W_SU_member=-0.005929`,

`W_SU_outsider=-0.046811`,

`W_SW=-0.023333`.

Therefore

`W_SU_member > W_IS > W_SU_outsider`,

and

`W_SU_member > W_SW`.

A pair strictly blocks IS by forming an SU. IS cannot strictly block an existing SU because the two incumbent members would lose. Breaking SU to SW is also unprofitable for a member.

Hence

`S_FULL={SU_12,SU_13,SU_23}`.

By contrast,

`S_B-T=S_B-X={IS}`.

## 10. Full-model-only interaction

At the witness:

`Delta_M^(B-T)=W_M-W_I=-0.010167<0`,

`Delta_M^(B-X)=-0.000434<0`,

but

`Delta_M^(FULL)=+0.001571>0`.

Therefore neither endogenous policy nor endogenous positioning alone generates the headline coalition result. The sign reversal is generated by their interaction.

## 11. Mechanism

The equilibrium chain is:

`SU depth`
`-> lower member-member standard friction + higher bloc-boundary friction`
`-> asymmetric network/competition incentives`
`-> member firms re-differentiate in product space`
`-> member profit rises relative to IS`
`-> national coalition preference reverses`
`-> IS becomes pair-blockable while SU becomes stable`.

This is not a mean-friction artifact: the Stage-3 policy map normalizes the SU depth margin to redistribute pairwise differentiation rather than mechanically improve average pairwise friction.

## 12. Comparative statics / parameter region

The witness inequalities are strict. A local grid over

- `v in {0.035,0.040,0.045}`;
- `gamma in {0.105,0.110,0.115}`;
- `s_bar in {0.225,0.250,0.275}`

produces the FULL-only sign reversal and passes whole-circle SU location best-response checks at 23 of 27 points.

A wider 5x5x5 audit around the same region produced 108 of 125 passing points.

The effect strengthens when the induced re-differentiation response is sufficiently large but not so large that the location stationary point loses global optimality.

## 13. Counterexample / failure audit

Stage 4 found a genuine failure region at low `gamma`. There, the local SU stationary point can satisfy FOCs/SOCs within one ordering but the outsider has a profitable discrete jump around the circle. Those points are excluded from the regular equilibrium region.

This validates the Stage-1 warning that a symmetric/location FOC is not enough.

No extra curvature or location constraint is introduced to rescue those points.

## 14. Candidate-proposition kill table

| Candidate | Verdict | Reason |
|---|---|---|
| Government policy changes product positioning | SURVIVES | SU location response is nonzero |
| Firms re-differentiate after deeper SU standardization | SURVIVES | member distance increases |
| Regime-specific optimal depth | SURVIVES | IS/SU/SW policy profiles differ |
| Endogenous policy changes coalition stability | SURVIVES | FULL stability differs from B-X |
| Endogenous positioning is essential | SURVIVES | FULL differs from B-T |
| FULL-only interaction result | SURVIVES | B-T and B-X both choose IS; FULL chooses SU |
| Every local stationary point is an equilibrium | KILLED | low-gamma outsider jump counterexamples |
| Literal B0 algebraic nesting | KILLED | primitives differ |

## 15. Artefact audit

The reversal is not generated by:

- a direct policy cost: none exists;
- a transfer: none exists;
- relative profit: absent;
- endogenous network intensity: absent;
- an arbitrary SU-only coefficient: the policy map is regime-neutral;
- mean-friction improvement: the SU normalization redistributes differentiation;
- a local FOC only: the witness passes whole-circle unilateral location scans.

## 16. Canonical verdict

**GO**.

Route:

**Stage 6 — Novelty Re-Kill.**

Stage 6 must attack the actual surviving proposition, not the earlier ingredient claims:

> Endogenous government standard depth and endogenous firm product repositioning interact to reverse the stability of international versus regional standards coalitions, even though each strategic margin separately selects international standardization.
