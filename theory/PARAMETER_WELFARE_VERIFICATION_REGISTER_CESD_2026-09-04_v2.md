# Parameter, Welfare & Verification Register — C-ESD v2

Freeze ID: `CESD-THEORY-FREEZE-2026-09-04-v2`
Date: 2026-09-04

## 1. Primitive parameter restrictions

- `t_bar>0`.
- `v>0`.
- `gamma>0`.
- `0<=s_bar<t_bar`.
- `s_C in [0,s_bar]` only for standards blocs with `|C|>=2`.
- `s_C=0` for singleton blocs.
- `A` sufficiently large for full coverage on the regular domain.
- Anchors fixed at `h=(1/6,1/2,5/6)`.
- Zero marginal production cost is part of the baseline.

## 2. Pairwise friction map

- same bloc `C`: `tau_ij=t_bar-s_C`;
- different blocs `C,D`: `tau_ij=t_bar+(s_C+s_D)/2`.

Under `SU_12`:

`tau_12=t_bar-s_12`,

`tau_13=tau_23=t_bar+s_12/2` because outsider singleton depth is zero.

The `1/2` coefficient is a frozen normalization, not an empirical structural parameter.

## 3. Regime-specific policy action sets

- IS: `s_I in [0,s_bar]`.
- `SU_12`: `s_12 in [0,s_bar]`; `s_3=0` by definition.
- SW: `s_1=s_2=s_3=0`.

This is submission-authoritative and supersedes the v1 rule allowing every bloc to choose positive depth.

## 4. Regular price-domain restrictions

For every evaluated regime/policy/location profile:

1. `A_rho=I-(v/2)LG_rho` is nonsingular.
2. `I-DM` is nonsingular.
3. `D_ii<0` for all firms.
4. Equilibrium `q_i>0`.
5. Equilibrium `p_i>0`.
6. Every arc indifferent point lies strictly inside the arc.

For symmetric SW, positive price requires `2t-3v>0`.

## 5. Regular location/continuation restrictions

A candidate continuation is valid only if:

1. the relevant fixed-order linear location system is nonsingular;
2. own-location SOCs satisfy `2M_ii R_ii^2-gamma<0`;
3. the candidate respects the represented cyclic order;
4. no firm has a profitable unilateral deviation anywhere on the circle;
5. policy-stage welfare is evaluated only using such valid downstream continuations.

Stage 4R is authoritative for the computational continuation audit at the canonical witness.

## 6. Canonical witness

`t_bar=1`,

`v=0.04`,

`gamma=0.11`,

`s_bar=0.25`.

### B-T

- IS: `s_I*=0.25`.
- `SU_12`: `s_12*=0.25`, outsider depth `0`.
- SW: no depth choice, all depths `0`.
- stable set `{IS}`.
- `Delta_M≈-0.010167`.

### B-X

- all non-singleton additional harmonization depths fixed at zero;
- formal regime-specific compatibility/network graphs retained;
- stable set `{IS}`;
- `Delta_M≈-0.000434`.

### FULL

- IS: `s_I*=0.25`;
- `SU_12`: `s_12*=0.25`, outsider depth `0`;
- SW: all depths `0`;
- `x^SU≈(0.084567,0.582100,0.833333)`;
- `Delta_M≈+0.001571`;
- stable set `{SU_12,SU_13,SU_23}`.

## 7. Repaired continuation verification

`verification/stage04r_cesd_continuation_repair.py` verifies at the canonical primitives:

1. continuous whole-circle location best responses over the feasible IS/SU depth intervals;
2. joint global search over depth and unilateral deviation location with no positive gain above tolerance;
3. all cyclic orders and circular-anchor branches on a dense 51-point depth grid;
4. exactly one regular whole-circle location equilibrium at every audited IS/SU depth;
5. one regular SW location equilibrium;
6. global scalar policy optimization on the repaired action sets;
7. B-T/B-X/FULL interaction signs and coalition-stability inequalities.

This is computational verification, not a global analytic existence theorem across all primitive parameters.

## 8. Exact welfare register

Aggregate consumer surplus:

`CS=A+v q'G_rho q-sum_i p_i q_i-TC`.

National welfare:

`W_i=CS/3+Pi_i`.

Prospective-member decomposition:

`Delta_M=Delta Pi_M+Delta CS/3`.

SU is preferred by a member iff

`Delta Pi_M>-Delta CS/3`.

Canonical witness components:

- `Delta CS/3≈-0.0325785`;
- `Delta Pi_M≈+0.0341498`;
- `Delta_M≈+0.0015713`.

World welfare:

`GW=A+v q'G_rho q-TC-sum_i C_i^D`.

Price payments cancel as transfers.

Witness values reported net of common baseline `A`:

- `GW_IS≈-0.0225000`;
- `GW_SU≈-0.0586685`;
- `GW_SW≈-0.0700000`.

Witness ranking: `GW_IS>GW_SU>GW_SW`.

## 9. Constrained social-location comparison

At canonical SU policy:

- inherited member distance `1/3`;
- constrained social distance `≈0.431427`;
- private equilibrium distance `≈0.497533`.

This is a second-best location comparison holding downstream pricing and compatibility structure decentralized/fixed.

## 10. Adjustment-cost register

Baseline:

`C_i^D=gamma d_c(x_i,h_i)^2/2`.

For interpretation only, a regular differentiable strictly convex cost satisfying `C(0)=C'(0)=0` and finite local curvature can preserve the positive SU repositioning force.

At `v=0.04`, `s_bar=0.25`:

- upper welfare threshold `gamma_W≈0.132983`.

No structural closed-form lower `gamma_GBR` threshold is frozen. Canonical regularity is established directly by Stage 4R.

## 11. Verification artifact map

### Core theory / continuation

- `model/STAGE4_MINIMAL_MODEL_CESD.md`
- `reviews/STAGE_04R_CONTINUATION_POLICY_REPAIR_2026-09-04.md`
- `model/STAGE4R_CESD_CONTINUATION_POLICY_REPAIR.md`
- `verification/stage04r_cesd_continuation_repair.py`

### Welfare / generality

- `reviews/STAGE_07R_WELFARE_GENERALITY_REFRESH_CESD_2026-09-04.md`
- `verification/stage07r_cesd_welfare_refresh.py`
- `literature/STAGE7R_CESD_INSTITUTIONAL_REFRESH.md`

### Novelty / contribution

- `reviews/STAGE_06_NOVELTY_REKILL_CESD_2026-09-04.md`
- `literature/STAGE6_CESD_CLOSEST_PAPER_MATRIX.md`

Historical v1 freeze and Stage-4/7 artifacts remain provenance records only where superseded by repaired v2 action-set language.

## 12. Verification-status summary

| Object | Status |
|---|---|
| Weighted demand system | analytic / `PROVED` |
| Regular price equilibrium | analytic / `PROVED` |
| Fixed-order location system | analytic / `PROVED` |
| Canonical repaired continuation validity over feasible policy depths | computational / `NUMERICALLY SUPPORTED ONLY` |
| SU re-differentiation on regular branch | `CONDITIONAL` |
| FULL-only reversal | `CONDITIONAL`, constructive repaired-SPNE result |
| National threshold identity | analytic / `PROVED` |
| World-welfare identity | analytic / `PROVED` |
| Witness world-welfare ranking | `NUMERICALLY SUPPORTED ONLY` |
| Witness private/social location wedge | `NUMERICALLY SUPPORTED ONLY` |
| Global lower regularity threshold formula | unavailable / not claimed |

## 13. Approved robustness list

Approved evidentiary support includes:

1. B-T benchmark.
2. B-X benchmark.
3. Repaired whole-circle continuation checks over feasible depth domains at canonical primitives.
4. Historical local parameter sensitivity where still consistent with v2 semantics.
5. Exact welfare accounting.
6. Constrained social-location comparison.
7. Local regular-convex-adjustment-cost interpretation.

Not established as baseline robustness:

- heterogeneous country consumer incidence;
- more than three countries;
- alternative spatial geometry;
- endogenous network coefficient;
- direct policy cost;
- transfers/side payments;
- relative-profit objectives;
- endogenous compatibility topology.

## 14. Freeze consistency rule

Any manuscript proposition, table, figure, parameter value, welfare number, action-set statement, or proof-status claim inconsistent with this v2 register requires explicit theory-change control. Where v1 and v2 conflict, v2 controls.
