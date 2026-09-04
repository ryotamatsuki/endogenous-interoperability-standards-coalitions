# Parameter, Welfare & Verification Register — C-ESD

Freeze ID: `CESD-THEORY-FREEZE-2026-09-04-v1`
Date: 2026-09-04

## 1. Primitive parameter restrictions

- `t_bar>0`.
- `v>0`.
- `gamma>0`.
- For each bloc, `0<=s_C<=s_bar<t_bar`.
- `A` is sufficiently large to guarantee full market coverage on the regular domain.
- Baseline anchors are fixed at `h=(1/6,1/2,5/6)`.
- Zero marginal production cost is part of the frozen baseline.

## 2. Endogenous pairwise frictions

For every pair `i,j`:

- same bloc `C`: `tau_ij=t_bar-s_C`;
- different blocs `C,D`: `tau_ij=t_bar+(s_C+s_D)/2`.

The frozen primitive restriction `s_bar<t_bar` ensures positive within-bloc friction. Cross-bloc frictions are strictly positive automatically when `t_bar>0` and depths are nonnegative.

The `1/2` coefficient is frozen only as a baseline normalization. It must not be presented as a structural empirical restriction.

## 3. Regular price-domain restrictions

For each evaluated regime/policy/location profile:

1. `A_rho=I-(v/2)LG_rho` is nonsingular.
2. `I-DM` is nonsingular.
3. Every `D_ii<0`.
4. Equilibrium `q_i>0` for every firm.
5. Equilibrium `p_i>0` for every firm.
6. Every arc indifferent point satisfies `0<y_ij<ell_ij`.

For the symmetric SW closed form, `p_i=(2t-3v)/6`, so positive price requires `2t-3v>0`.

## 4. Regular location-domain restrictions

For every selected cyclic-order candidate:

1. the linear location system is nonsingular;
2. own-location SOCs satisfy `2M_ii R_ii^2-gamma<0`;
3. the candidate respects the evaluated cyclic-order branch when that branch representation is used;
4. the candidate passes whole-circle unilateral deviation checks permitting order changes.

A local stationary point failing item 4 is not an equilibrium and must be rejected.

## 5. Canonical witness

`t_bar=1`,

`v=0.04`,

`gamma=0.11`,

`s_bar=0.25`.

### B-T

- IS: `s_I=0.25`.
- `SU_12`: `(s_12,s_3)=(0.25,0)`.
- SW: `(0,0,0)`.
- stable set `{IS}`.
- `Delta_M=-0.010167`.

### B-X

- all policy depths fixed at zero.
- stable set `{IS}`.
- `Delta_M=-0.000434`.

### FULL

- IS: `s_I=0.25`.
- `SU_12`: `(s_12,s_3)=(0.25,0)`.
- SW: `(0,0,0)`.
- `x^SU=(0.084567,0.582100,0.833333)`.
- `Delta_M=+0.001571`.
- stable set `{SU_12,SU_13,SU_23}`.

## 6. Welfare register

### Exact aggregate consumer surplus

`CS=A+v q'G_rho q-sum_i p_i q_i-TC`.

### National welfare

`W_i=CS/3+Pi_i`.

### Exact prospective-member decomposition

`Delta_M=Delta Pi_M+Delta CS/3`.

SU is preferred by a prospective member iff

`Delta Pi_M>-Delta CS/3`.

Canonical witness components:

- `Delta CS/3=-0.0325785`;
- `Delta Pi_M=+0.0341498`;
- `Delta_M=+0.0015713`.

### Exact world welfare

`GW=A+v q'G_rho q-TC-sum_i C_i^D`.

Price payments cancel as transfers.

Canonical witness values:

- `GW_IS=-0.0225000`;
- `GW_SU=-0.0586685`;
- `GW_SW=-0.0700000`.

Witness ranking: `GW_IS>GW_SU>GW_SW`.

### Constrained social-location comparison at canonical SU policy

- inherited member distance: `0.333333`;
- constrained social distance: `0.431427`;
- private equilibrium distance: `0.497533`.

This is a second-best location comparison with downstream pricing and compatibility structure held decentralized/fixed.

## 7. Adjustment-cost register

Baseline cost:

`C_i^D=gamma d_c(x_i,h_i)^2/2`.

Stage-7 approved interpretation:

For a regular differentiable strictly convex `C(d)` satisfying `C(0)=C'(0)=0` and finite local curvature, the same positive SU marginal operating-profit force can induce positive re-differentiation.

The headline reversal requires intermediate effective curvature.

For `v=0.04,s_bar=0.25`:

- upper welfare threshold: `gamma_W=0.132983`;
- audited global-BR transition: approximately `gamma≈0.10`.

The latter is computational, not an analytic closed-form threshold.

## 8. Verification artifact map

### Analytic / symbolic

- `model/STAGE4_MINIMAL_MODEL_CESD.md`
  - weighted-Laplacian demand architecture;
  - price FOCs/SOCs and matrix equilibrium;
  - fixed-order location FOCs/SOCs;
  - exact symmetric IS/SW blocks;
  - welfare definitions.

- `verification/stage04_cesd_minimal.py`
  - SymPy verification of homogeneous IS/SW price and welfare formulas;
  - numerical continuation calculations;
  - whole-circle deviation audit;
  - B-T/B-X/FULL witness checks;
  - neighborhood parameter audit.

### Welfare / generality

- `reviews/STAGE_07_WELFARE_GENERALITY_CESD_2026-09-04.md`
  - exact CS/world-welfare identities;
  - national rent/consumer decomposition;
  - private/social location wedge;
  - general-convex-cost interpretation;
  - empirical predictions and institutional scope.

- `verification/stage07_cesd_welfare_generality.py`
  - witness welfare decomposition;
  - world-welfare accounting;
  - constrained social-location comparison;
  - threshold/general-region calculations.

### Novelty / contribution

- `reviews/STAGE_06_NOVELTY_REKILL_CESD_2026-09-04.md`
- `literature/STAGE6_CESD_CLOSEST_PAPER_MATRIX.md`
- `reviews/STAGE_075_FREEZE_DECISION_CESD_2026-09-04.md`

These define the allowed contribution language and remaining referee risks.

## 9. Approved robustness list

Already part of the frozen evidentiary package:

1. B-T benchmark.
2. B-X benchmark.
3. Whole-circle one-firm location-deviation checks.
4. 3x3x3 local parameter audit.
5. Wider 5x5x5 parameter audit.
6. Exact welfare accounting.
7. Constrained social location comparison.
8. Local regular-convex-adjustment-cost interpretation.

The following are not baseline robustness already established and cannot be implied as such:

- heterogeneous country consumer incidence;
- more than three countries;
- alternative spatial geometry;
- endogenous `v`;
- direct policy cost;
- transfers/side payments;
- relative-profit objectives;
- endogenous compatibility topology.

## 10. Verification-status summary

| Object | Status |
|---|---|
| Weighted demand system | analytic / `PROVED` |
| Regular price equilibrium | analytic / `PROVED` |
| Fixed-order location system | analytic / `PROVED` |
| Global location Nash at witness | computationally verified |
| SU re-differentiation on regular branch | `CONDITIONAL` |
| FULL-only reversal | `CONDITIONAL`, constructive regular-region result |
| National threshold identity | analytic / `PROVED` |
| World-welfare identity | analytic / `PROVED` |
| Witness world-welfare ranking | `NUMERICALLY SUPPORTED ONLY` |
| Witness private/social location wedge | `NUMERICALLY SUPPORTED ONLY` |
| Global `gamma_GBR` formula | not available / not claimed |

## 11. Freeze consistency rule

Any manuscript table, proposition, figure, or textual claim that uses a parameter value, welfare number, equilibrium object, or proof status not traceable to this register or the referenced canonical artifacts requires an explicit theory-change or reproducibility record before use.
