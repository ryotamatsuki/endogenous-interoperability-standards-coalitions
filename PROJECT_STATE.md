# Project State

Last updated: 2026-09-06

## Canonical status

- Project: Endogenous Interoperability and Standards Coalitions
- Working title: **Standards Coalitions and Strategic Product Repositioning**
- Canonical workflow: `ryotamatsuki/research-paper-workflow` **v1.2**
- Workflow release SHA: `944e6bace951e13645b02200a63bf25363dc7242`
- Previous theory freeze: `CESD-THEORY-FREEZE-2026-09-04-v2` — **REOPENED / NON-AUTHORITATIVE**
- Theory status: **TERMINATED — AFFINE-DEMAND RE-FOUNDATION FIXES CONTINUATION BUT FAILS THE FULL-GAME CONTRIBUTION GATE**
- Stage 5RR: **NO-GO — linear localized continuation terminated**
- Stage 4R3Q: **NO-GO — pure-quadratic localized continuation terminated**
- Stage 3R4: **GO — affine-demand Bertrand re-foundation selected**
- Stage 4R4A: **GO — continuation/demand/repositioning subgate passed**
- Stage 4R4B: **NO-GO — policy/welfare/coalition reconstruction yields no full-model-only result**
- Canonical Stage 4: **NO-GO**
- Stage 5 authorized: **NO**
- Stage 6 authorized: **NO**
- New theory freeze authorized: **NO**
- Stage 11R2: **STALE / NON-AUTHORITATIVE**
- Stage 12 journal positioning: **STALE / submission authorization revoked**
- Stage 13: **CLOSURE REVOKED**
- Stage 14 submission QA authorized: **NO**
- Submission status: **DO NOT SUBMIT**

## Terminated spatial architectures

Three pure-strategy spatial price-continuation implementations were permanently terminated:

1. unrestricted all-product linear Salop;
2. explicit localized linear competition;
3. explicit localized pure-quadratic competition.

The affine-demand Bertrand re-foundation was then tested as a genuinely distinct continuation architecture.

## Affine-demand architecture that survived continuation

Consumers are not allocated to Salop arcs. The circle is a smooth product-characteristic space.

`delta_ij(x)=1-cos(2*pi*(x_i-x_j))`.

Representative-consumer utility is

`U(q)=a*1'q-(1/2)q'Bq+(v/2)q'G_rho q`, `q>=0`,

with

`B_ii=1`,

`B_ij=beta/[1+tau_ij+delta_ij]`,

and

`K=B-vG_rho`.

Under the Stage 4R4A sufficient inequalities, demand is globally well posed and gross-substitute, and the nonnegative affine-demand Bertrand equilibrium is unique for every admissible upstream history.

Thus the original fatal continuation-equilibrium defect is repaired in this architecture.

## Stage 4R4B welfare definition

At the quadratic representative-consumer optimum,

`CS=(1/2)q'Kq`.

Because the inherited model has three symmetric countries and no home-bias or market-size primitive,

`CS_i=CS/3`.

National welfare is

`W_i=CS/3+p_i q_i-gamma y_i^2/2`.

No additional policy cost, transfer, home bias, bargaining weight, or country asymmetry is introduced.

## Stage 4R4B exact / verified result

Frozen transparent normalization:

`t_bar=1`, `s_bar=1/4`, `beta=1/5`, `v=1/50`, `a=1`, `gamma=1/5`.

### B-T

For `SU_12`, fixed inherited positions and outsider depth `s_3=1/4`, the member-bloc welfare derivative with respect to `s_12` is strictly negative over the full interval `[0,1/4]`.

The exact derivative numerator is degree 16 after rational simplification. After mapping the policy interval to `[0,1]`, all 17 Bernstein coefficients are strictly negative.

Therefore

` s_12^{BT}=0 `.

### FULL SU

Locations are re-solved at every audited policy value and accepted only after unrestricted unilateral global best-response checks on `[-1/2,1/2]`.

Member-bloc welfare remains decreasing in `s_12`, while outsider welfare rises with `s_3`.

Canonical FULL SU policy outcome:

`(s_12*,s_3*)=(0,1/4)`.

The member firms nevertheless reposition outward:

`y approximately (-0.002833,+0.002833,0)`.

Approximate national welfare:

`W_SU^FULL approximately (0.353837,0.353837,0.349450)`.

Thus repositioning is nondegenerate but does not reverse the union bloc's policy incentive.

### B-X

With zero continuous depth and endogenous locations,

`W_SU^BX approximately (0.353389,0.353389,0.348681)`.

### IS

The IS bloc selects `s_I*=0`; symmetry pins positions at the inherited anchors.

`W_IS approximately (0.357552,0.357552,0.357552)`.

### SW

The FULL singleton-depth game is audited with location re-solved after unilateral depth deviations. Each singleton selects maximal depth in the canonical symmetric equilibrium:

`(s_1*,s_2*,s_3*)=(1/4,1/4,1/4)`.

`W_SW^FULL approximately (0.350582,0.350582,0.350582)`.

## Coalition-stability result

At the frozen affine witness, every country strictly prefers IS to the relevant SU and SW continuation in each of

- `B-T`;
- `B-X`;
- `FULL`.

Therefore the grand IS coalition is stable and SU/SW are blocked by the grand coalition in all three architectures.

The FULL stability conclusion is already present in the nested benchmarks. Endogenous repositioning changes welfare levels but not the policy or coalition ranking.

This fails the canonical Stage-4 requirement for a substantive full-model-only result.

## Wider hostile audit

A broader regular-parameter diagnostic varied `beta`, `v`, and `gamma` over cells satisfying the Stage 4R4A demand-regularity inequalities. SU member welfare remained decreasing over the audited union-depth grid when the outsider chooses maximal specificity. No positive member-depth region emerged.

This is diagnostic evidence, not a general theorem. It is recorded to prevent post-hoc parameter search aimed at manufacturing the desired reversal.

## Final contribution assessment

The affine architecture establishes that

- globally complete Bertrand continuation is feasible;
- standards depth changes product-repositioning incentives;
- product repositioning can be nonzero.

But the only surviving interaction is a small quantitative welfare-level effect. It does not generate a new policy ordering, welfare reversal, or coalition-stability theorem.

Given prior art on compatibility-induced differentiation and endogenous design under linear demand, this is not enough for the intended IJIO contribution.

## Canonical verdict

**STAGE 4R4B NO-GO — CANONICAL STAGE 4 NO-GO — TERMINATE THIS PAPER.**

Do not proceed to Stage 5, Stage 6, theory freeze, journal-positioning refresh, or submission QA.

Do not automatically return to Stage 3 for another continuation architecture. Stage 3R4 explicitly made termination the default if this full-game reconstruction failed.

Any future reuse of the standards-depth / repositioning idea must begin as a distinct Stage 0 research question or separate paper.

Authorities:

- `model/STAGE4R4A_AFFINE_DEMAND_BERTRAND.md`
- `verification/stage04r4a_affine_bertrand_gate.py`
- `verification/stage04r4b_policy_welfare_coalition.py`
- `verification/stage04r4b_sw_full_policy_check.py`
- `reviews/STAGE_04R4B_AFFINE_POLICY_WELFARE_COALITION_RECONSTRUCTION_2026-09-06.md`
- `decisions/STAGE04R4B_CESD_DECISIONS.md`
