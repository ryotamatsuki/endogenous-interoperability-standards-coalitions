# Proposition Register — C-ESD v2

Freeze ID: `CESD-THEORY-FREEZE-2026-09-04-v2`
Date: 2026-09-04

Proof-status vocabulary:

- `PROVED`
- `CONDITIONAL`
- `NUMERICALLY SUPPORTED ONLY`
- `REJECTED`

## P1 — Weighted-Laplacian demand and unique regular price equilibrium

**Status: PROVED.**

On the regular domain,

`q=b-(1/2)Lp+(v/2)LG_rho q`,

`A_rho=I-(v/2)LG_rho`,

`D=-(1/2)A_rho^{-1}L`,

`q=A_rho^{-1}b+Dp`.

With zero marginal production cost, the price FOCs imply `p=Mq`, `M=diag(-1/D_ii)`, and

`q=(I-DM)^{-1}A_rho^{-1}b`.

When the stated regularity conditions hold, the interior price Nash equilibrium is unique.

## P2 — Conditional location system on a fixed cyclic order

**Status: PROVED.**

For a fixed cyclic order, `b(x)=b0+Bx`, hence `q=c+Rx`. The location FOCs form a linear system and the own-location SOC is

`2M_ii R_ii^2-gamma<0`.

This is an analytic branch characterization only. A conditional fixed-order solution is not automatically a global location Nash equilibrium.

## P3 — SU strategic re-differentiation

**Status: CONDITIONAL.**

On the selected regular SU branch, deeper coalition harmonization creates an outward member-location incentive and, at the canonical witness, members move apart in product space. The repaired action set does not alter this force.

Approved form: regular-branch mechanism statement with continuation/global-BR conditions explicit.

Not approved: universal re-differentiation for every parameterization or every local stationary point.

## P4 — Repaired FULL-only coalition-stability reversal

**Status: CONDITIONAL.**

Canonical sign pattern:

`Delta_M^(B-T)<0`,

`Delta_M^(B-X)<0`,

`Delta_M^(FULL)>0`.

At `(t_bar,v,gamma,s_bar)=(1,0.04,0.11,0.25)`:

- `Delta_M^(B-T)≈-0.010167`;
- `Delta_M^(B-X)≈-0.000434`;
- `Delta_M^(FULL)≈+0.001571`.

Under the repaired policy action set, Stage 4R verifies actual downstream whole-circle location Nash continuations over the entire feasible IS and SU policy-depth domains at the canonical witness, and globally re-solves the scalar policy stage. FULL yields stable two-country SUs while B-T and B-X select IS.

Approved form: **constructive repaired-SPNE regular-domain result**.

Not approved: closed-form global theorem over all primitive parameter values.

Reason for `CONDITIONAL`: the result is established on a computationally verified regular domain rather than by an analytic global classification of all location-order and parameter regimes.

## P5 — Exact national member welfare threshold

**Status: PROVED.**

For a prospective SU member,

`Delta_M=Delta Pi_M+Delta CS/3`.

Thus SU is preferred to IS iff

`Delta Pi_M>-Delta CS/3`.

## P6 — Exact global welfare identity

**Status: PROVED.**

`CS=A+v q'G_rho q-sum_i p_i q_i-TC`,

so

`GW=A+v q'G_rho q-TC-sum_i C_i^D`.

Price payments cancel globally as transfers.

## P7 — Global-welfare ranking at canonical witness

**Status: NUMERICALLY SUPPORTED ONLY.**

Reported net of common baseline utility `A`:

`GW_IS≈-0.0225000`,

`GW_SU≈-0.0586685`,

`GW_SW≈-0.0700000`.

Hence `GW_IS>GW_SU>GW_SW` at the canonical witness only.

## P8 — Private over-re-differentiation relative to constrained social location choice

**Status: NUMERICALLY SUPPORTED ONLY.**

At canonical SU policy:

- inherited member distance `1/3`;
- constrained social distance `≈0.431427`;
- private equilibrium distance `≈0.497533`.

Approved form: witness-specific second-best comparison.

## P9 — Adjustment-cost interpretation

**Status: CONDITIONAL.**

The quadratic baseline is not conceptually necessary for positive SU re-differentiation. For a regular differentiable strictly convex cost with `C(0)=C'(0)=0` and finite local curvature, the same positive SU marginal operating-profit force can induce positive repositioning.

At `v=0.04`, `s_bar=0.25`, the upper welfare threshold on the audited branch is

`gamma_W≈0.132983`.

No structural closed-form lower `gamma_GBR` threshold is frozen in v2. Canonical regularity is established directly by Stage 4R continuation verification.

## P10 — Repaired policy-stage continuation validity at canonical primitives

**Status: NUMERICALLY SUPPORTED ONLY.**

At canonical primitives and under the repaired action set:

- every feasible IS/SU policy depth audited by Stage 4R admits the selected regular whole-circle location continuation;
- global joint searches over policy depth and unilateral deviation location find no profitable deviation to numerical tolerance;
- all-order/anchor enumeration on a dense 51-point depth grid finds exactly one regular interior whole-circle location equilibrium at every audited IS/SU depth;
- SW has one regular whole-circle location equilibrium and no depth choice.

Approved form: computational continuation-validity statement for the canonical constructive result.

Not approved: analytic existence/uniqueness theorem for all parameter vectors.

## Rejected proposition / novelty set

### R1 — Every local location stationary point is a Nash equilibrium

**Status: REJECTED.** Low-curvature/order-changing counterexamples exist historically.

### R2 — Singleton blocs choose positive harmonization depth

**Status: REJECTED in v2.** `s_C` is within-coalition harmonization depth; singleton action is `{0}`.

### R3 — B0 is algebraically nested by C-ESD

**Status: REJECTED.** B0 is an institutional coalition benchmark only.

### R4 — Partial SU stability is novel

**Status: REJECTED as novelty claim.** Prior art contains partial standards-union stability.

### R5 — Government standards policy affecting product characteristics is novel

**Status: REJECTED as novelty claim.** Ruiz-type prior art kills this claim.

### R6 — Salop + network effects + compatibility is novel

**Status: REJECTED as novelty claim.** Prior art kills this claim.

## Manuscript theorem-label rule

Only `PROVED` items may be presented as analytic propositions within their explicitly stated domain.

`CONDITIONAL` items must state the regularity/branch/continuation qualification in the proposition or immediately adjacent text.

`NUMERICALLY SUPPORTED ONLY` items must be presented as computational results, verified witnesses, examples, or quantitative illustrations.

`REJECTED` items may not re-enter the contribution set without reopening the relevant stage.
