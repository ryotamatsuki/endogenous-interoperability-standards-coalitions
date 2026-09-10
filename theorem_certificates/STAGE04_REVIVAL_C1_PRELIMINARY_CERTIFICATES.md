# Stage 4 Preliminary Theorem Certificates — Revival C1

Date: 2026-09-10

Status: **PRELIMINARY / CONSTRUCTION-LEVEL ONLY**

These certificates are inputs to Stage 4A. They are not independent certification and may not be cited as a final theory freeze.

## P1 — Global affine-demand / Bertrand continuation

### Statement

For the C1 minimal model on the audited threshold domain

`v in [0.06,0.16]`, `s_C in [0,1/4]`, `x_i on the full unit circle`,

with frozen primitives `b=10`, `c0=.30`, `lambda=.50`, `t_bar=1`, every off-diagonal cross-curvature lies in

`[0.14, 0.966666...]`.

The inequalities

`b>2c_max`, `b*c_min>c_max^2`, and `b-2c_max+c_min>0`

hold uniformly. The quadratic consumer problem is strictly concave and the affine substitute-demand sign structure used by the nonnegative Bertrand continuation holds over the full upstream strategy domain.

### Evidence maturity

- analytic uniform bounds;
- exact matrix-inequality arithmetic;
- KKT active-set demand evaluator;
- direct global one-price deviation regression at hostile histories.

### Status

`CONSTRUCTION PASS — GLOBAL PRIMITIVE DOMAIN; STAGE 4A MUST INDEPENDENTLY CERTIFY THE BERTRAND THEOREM APPLICATION AND OFF-PATH COMPLETENESS.`

## P2 — Standards-contingent product repositioning

### Statement

Under a bilateral union at positive/full depth, the two member firms move strictly away from each other while the outsider remains at its inherited anchor on the symmetric continuation. At `(v,gamma)=(0.08,0.03)` with `(s_12,s_3)=(1/4,1/4)`,

`x_SU approximately (0.135440,0.531226,0.833333)`

versus anchors

`(0.166667,0.500000,0.833333)`.

The candidate profile survives whole-circle unilateral best-response attacks.

### Quantifier / domain

Construction evidence is reported at the canonical point, the historical local `(v,gamma)` box, and threshold-critical points. No global closed-form location theorem is claimed.

### Status

`CONSTRUCTION PASS — NUMERICAL GLOBAL-BR CERTIFICATE AT AUDITED POINTS.`

## P3 — IS realized-interoperability policy trade-off

### Statement

At symmetric IS anchors,

`c_IS(s)=c0+lambda*(1/4)/(t_bar-s)-v*s/s_bar`.

For the symmetric affine Bertrand continuation,

`dW_IS/dc = -a^2(2b^2+bc+c^2)/[4b^2(b+2c)^2] < 0`.

Because

`dc_IS/ds=lambda*(1/4)/(t_bar-s)^2-v/s_bar`,

IS welfare is increasing throughout `[0,s_bar]` whenever

`v > s_bar*lambda*(1/4)/(t_bar-s_bar)^2 = 1/18`.

Hence `s_I*=s_bar` on that region, conditional on the globally verified symmetric-anchor location continuation.

### Status

`CONSTRUCTION PASS — EXACT SYMBOLIC POLICY CONDITION + GLOBAL LOCATION REGRESSION.`

## P4 — Repositioning-essential stable-partition reversal

### Statement

At the frozen canonical source point `(v,gamma)=(0.08,0.03)`, with each benchmark solved under its own authorized policy convention:

- `B-FIX` has stable set `{IS}`;
- `FULL` has stable set `{SU_12,SU_13,SU_23}`.

The same stable-set difference is reproduced at all nine points of the pre-existing local box

`v in {0.07,0.08,0.09}` x `gamma in {0.025,0.03,0.035}`.

### Status

`CONSTRUCTION PASS — STRICT COMPUTATIONAL STABILITY RESULT; RECTANGULAR-BOX QUANTIFIER NOT CLAIMED.`

## P5 — Ordered blocking thresholds and FULL-only interaction region

### Statement

Define the SU-member blocking threshold against IS as the value of network/interoperability strength `v` at which the prospective member is indifferent between the relevant SU continuation and IS.

On the threshold region where the audited policy choices are at the upper depth boundary:

1. `B-FIX` has exact member-indifference threshold

   `v_FIX=1/15=0.066666...`.

2. Under the pre-existing positive exogenous-depth benchmark `B-EXO-HIST`, at `gamma=.03`, the unique audited root is

   `v_EXO approximately 0.11154504`.

3. Under `FULL`, at `gamma=.03`, the unique audited root is

   `v_FULL approximately 0.13368738`.

Hence

`v_FIX < v_EXO < v_FULL`.

For the transparent interaction witness `v=.12`, `gamma=.03`:

- `B-FIX` stable set is `{IS}`;
- `B-EXO-HIST` stable set is `{IS}`;
- `FULL` stable set is `{SU_12,SU_13,SU_23}`.

Therefore both endogenous policy choice and product repositioning are needed to obtain the FULL stable-set outcome relative to the two binding nested benchmarks at the same primitives.

The threshold ordering also persists at the pre-existing redesign-cost points:

- `gamma=.025`: `v_EXO approximately .11264515 < v_FULL approximately .13493252`;
- `gamma=.030`: `.11154504 < .13368738`;
- `gamma=.035`: `.11048100 < .13247968`.

### Exact component

The `B-FIX` member-welfare difference has an exact rational factorization containing `(15v-1)` as the unique relevant sign-changing factor on the audited threshold interval, yielding the exact `1/15` threshold.

### Numerical/implicit component

The `B-EXO-HIST` and `FULL` thresholds use unique sign changes of smooth reduced member-welfare differences after re-solving the symmetric SU location equilibrium. The verifier checks strict monotonicity on a dense threshold grid and whole-circle unilateral location deviations at high-stakes points.

### Status

`CONSTRUCTION PASS — HEADLINE CANDIDATE FOR STAGE 4A.`

Stage 4A must specifically attack:

- uniqueness/globality of the SU location continuation throughout each threshold bracket;
- global bloc-depth deviations rather than finite-grid monotonicity alone;
- the threshold-root uniqueness claim;
- continuity/regularity needed for local open-neighborhood language;
- the newly frozen residual-membership blocking correspondence;
- whether any alternative equilibrium selection changes the threshold ordering.

## P6 — Nested-benchmark identification

### Statement

The FULL-only interaction interval is not generated by a single known component:

- removing product repositioning gives `B-FIX` and moves the blocking threshold down to `1/15`;
- removing endogenous depth and using the pre-existing positive-depth history gives `B-EXO-HIST` and moves the threshold to about `.111545` at `gamma=.03`;
- retaining both produces the higher FULL threshold about `.133687`.

Thus for `v` strictly between the B-EXO-HIST and FULL thresholds, neither benchmark reproduces the FULL stable partition.

### Status

`CONSTRUCTION PASS — NESTING/IDENTIFICATION CLAIM; NOVELTY REMAINS SUBJECT TO LATER RE-KILL.`
