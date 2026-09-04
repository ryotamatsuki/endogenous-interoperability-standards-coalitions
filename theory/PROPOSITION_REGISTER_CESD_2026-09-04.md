# Proposition Register — C-ESD

Freeze ID: `CESD-THEORY-FREEZE-2026-09-04-v1`
Date: 2026-09-04

Proof-status vocabulary required by Stage 8:

- `PROVED`
- `CONDITIONAL`
- `NUMERICALLY SUPPORTED ONLY`
- `REJECTED`

The manuscript must use wording consistent with these classifications.

## P1 — Weighted-Laplacian demand and unique regular price equilibrium

**Status: PROVED.**

On the regular domain,

`q=b-(1/2)Lp+(v/2)LG_rho q`,

`A_rho=I-(v/2)LG_rho`,

`D=-(1/2)A_rho^{-1}L`,

`q=A_rho^{-1}b+Dp`.

With zero marginal production cost, price FOCs imply

`p=Mq`, `M=diag(-1/D_ii)`,

and

`q=(I-DM)^{-1}A_rho^{-1}b`.

When the stated regularity conditions hold, the interior price Nash equilibrium is unique.

Approved manuscript form: analytic proposition on the regular domain.

## P2 — Conditional location system on a fixed cyclic order

**Status: PROVED.**

For a fixed cyclic order, `b(x)=b0+Bx`, so `q=c+Rx`. Baseline net profit is quadratic in own location and the location FOCs form a linear system. The own-location SOC is

`2M_ii R_ii^2-gamma<0`.

Approved manuscript form: analytic characterization conditional on the cyclic order and regularity restrictions.

Not approved: treating the conditional solution alone as a global location equilibrium.

## P3 — SU strategic re-differentiation

**Status: CONDITIONAL.**

On the selected regular SU branch, deeper bloc integration creates a nonzero outward member-location incentive, while symmetric IS/SW inherited configurations have zero corresponding location force. At the canonical witness and audited regular region, SU members move apart in the horizontal product dimension.

The baseline quadratic model and whole-circle checks verify this on the selected regular branch. Stage 7 further shows that a regular convex adjustment cost with `C(0)=C'(0)=0` and finite curvature preserves the local positive re-differentiation force.

Approved manuscript form: regular-branch proposition / mechanism statement with the regularity condition stated explicitly.

Not approved: a universal theorem for every parameterization or every stationary point.

## P4 — FULL-only coalition-stability reversal

**Status: CONDITIONAL.**

Canonical sign pattern:

`Delta_M^(B-T)<0`,

`Delta_M^(B-X)<0`,

`Delta_M^(FULL)>0`.

At the canonical witness `(t_bar,v,gamma,s_bar)=(1,0.04,0.11,0.25)`:

- `Delta_M^(B-T)=-0.010167`;
- `Delta_M^(B-X)=-0.000434`;
- `Delta_M^(FULL)=+0.001571`.

The FULL SU continuation passes the audited whole-circle one-firm location-deviation test. Strict payoff inequalities and continuity on the selected regular branch imply a nonempty local region once regularity/global-BR validity is maintained. Nearby-grid audits support that the region is not knife-edge.

Approved manuscript form: **constructive regular-region result** or **verified open-region proposition**, explicitly conditional on the stated regular continuation/global-BR conditions.

Not approved: describing this as a closed-form global theorem over the whole parameter space.

Reason for `CONDITIONAL` rather than `PROVED`: the lower boundary at which whole-circle order-changing deviations cease to be profitable is computationally verified rather than globally characterized analytically.

## P5 — Exact national member welfare threshold

**Status: PROVED.**

For a prospective SU member,

`Delta_M = Delta Pi_M + Delta CS/3`.

Hence the member prefers SU to IS iff

`Delta Pi_M > -Delta CS/3`.

Approved manuscript form: exact identity and exact threshold conditional only on the frozen national welfare definition.

## P6 — Exact global welfare identity

**Status: PROVED.**

Aggregate consumer surplus satisfies

`CS=A+v q'G_rho q-sum_i p_i q_i-TC`.

Therefore

`GW=CS+sum_i Pi_i`

`  =A+v q'G_rho q-TC-sum_i C_i^D`.

Price payments cancel as transfers.

Approved manuscript form: exact welfare identity.

## P7 — Global-welfare ranking at the canonical witness

**Status: NUMERICALLY SUPPORTED ONLY.**

At the canonical witness:

`GW_IS=-0.0225000`,

`GW_SU=-0.0586685`,

`GW_SW=-0.0700000`.

Thus `GW_IS>GW_SU>GW_SW` at that witness.

Approved manuscript form: calibrated/theoretical-witness welfare comparison, not a universal welfare theorem.

## P8 — Private over-re-differentiation relative to constrained social location choice

**Status: NUMERICALLY SUPPORTED ONLY.**

At the fixed canonical SU policy `(s_12,s_3)=(0.25,0)`:

- inherited member distance `0.333333`;
- constrained social distance `0.431427`;
- private equilibrium distance `0.497533`.

Approved manuscript form: canonical-witness second-best comparison illustrating the private/social wedge.

Not approved: a global theorem that firms always over-re-differentiate.

## P9 — Intermediate adjustment-cost region

**Status: CONDITIONAL.**

Economic-region characterization:

`gamma_GBR(v,s_bar) < gamma < gamma_W(v,s_bar)`,

plus the two benchmark inequalities, is sufficient for the headline reversal on the selected regular branch.

For `v=0.04, s_bar=0.25`,

`gamma_W=0.132983`,

while the audited global-BR transition is approximately `gamma≈0.10`.

Approved manuscript form: mechanism interpretation and numerically delimited regular region.

Not approved: claiming a closed-form global expression for `gamma_GBR`.

## Rejected proposition set

### R1 — Every local location stationary point is a Nash equilibrium

**Status: REJECTED.**

Low-`gamma` counterexamples admit profitable whole-circle jumps.

### R2 — B0 is algebraically nested by C-ESD

**Status: REJECTED.**

B0 remains an institutional IS/SU/SW benchmark only.

### R3 — Partial standards-union stability is novel

**Status: REJECTED as a novelty claim.**

Killed by prior art.

### R4 — Government standards policy affecting product characteristics is novel

**Status: REJECTED as a novelty claim.**

Killed by Ruiz-type prior art.

### R5 — Salop + network effects + compatibility is novel

**Status: REJECTED as a novelty claim.**

Killed by prior art.

## Manuscript theorem-label rule

Only `PROVED` items may be presented as unconditional analytic propositions within their explicitly stated domain.

`CONDITIONAL` items must state the relevant regularity/branch/global-BR condition in the proposition or immediately adjacent text.

`NUMERICALLY SUPPORTED ONLY` items must be presented as verified witness results, computational propositions, examples, or quantitative illustrations—not as general analytic theorems.

`REJECTED` items must not re-enter the contribution set without reopening the relevant stage.
