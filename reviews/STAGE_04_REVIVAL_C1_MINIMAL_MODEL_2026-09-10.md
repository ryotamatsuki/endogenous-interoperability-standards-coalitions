# Stage 4 — Revival C1 Minimal Model Gate

Date: 2026-09-10

Workflow: `ryotamatsuki/research-paper-workflow` v2.1.

Branch: `revival/stage00-coalition-repositioning`.

Selected mechanism: **C1 — Realized Interoperability Depth**.

## 1. Executive verdict

**GO — GO TO STAGE 4A INDEPENDENT MATHEMATICAL ADVERSARIAL CERTIFICATION.**

The Stage-3 C1 architecture survives the construction gate without adding any unauthorized primitive. It repairs the source architecture's one-sided interpretation of standards depth by making the same depth variable determine both realized within-bloc interoperability and the standard-induced competitive compression that firms may counter through product repositioning.

Most importantly, the resulting FULL game produces a coalition-stability implication that is absent from both binding nested benchmarks.

At the transparent interaction point `(v,gamma)=(0.12,0.03)`:

- `B-FIX`: only IS is stable;
- `B-EXO-HIST`: only IS is stable;
- `FULL`: exactly the three bilateral standards unions are stable.

The result is not manufactured by adding a policy cost, asymmetry, nonlinear realization function, bargaining weight, extra market, or another strategic margin.

Stage-4 GO is construction-level only. Stage 4A must independently attack the global policy/location claims, threshold roots, and stability operator before any theory freeze or novelty re-kill.

## 2. Exact Stage-4 model

Authority:

`model/REVIVAL_STAGE4_C1_MINIMAL_MODEL_2026-09-10.md`.

The game is

`rho -> bloc depth s -> product positions x -> Bertrand prices p -> national welfare -> strict blocking/stability`.

For `i!=j`,

`K_ij=c0+lambda*phi(x_i-x_j)/Tau_ij(rho,s)-v*M_ij(rho,s)`.

The sole C1 change is

`M_ij=s_C/s_bar`

for two firms in the same multi-country bloc and zero across blocs. All other source primitives are retained.

## 3. Demand and continuation

On the audited threshold domain `v in [0.06,0.16]`, the global off-diagonal bounds are

`c_min=.14`, `c_max=.966666...`.

The inherited sufficient inequalities

`b>2c_max`,

`b*c_min>c_max^2`,

`b-2c_max+c_min>0`

continue to hold uniformly over the full policy box and full product circle.

The quadratic consumer problem is therefore strictly concave throughout the stated domain and retains the affine substitute-demand structure. Nonnegative demand is defined by KKT active sets. Representative hostile histories were tested against direct global one-price deviations with the KKT evaluator; no profitable price deviation was found.

Solver outcome at the audited Stage-4 continuation set: `SOLVED_EQUILIBRIUM`; no material `UNRESOLVED` or `NUMERICAL_FAILURE` was accepted as evidence.

Stage 4A must independently validate the theorem application and off-path completeness rather than reuse this solver.

## 4. Product-location equilibrium

At canonical `(v,gamma)=(.08,.03)` and FULL SU policy `(s_12,s_3)=(.25,.25)`,

`x_SU approximately (.135440,.531226,.833333)`.

The two members move outward relative to anchors `(1/6,1/2,5/6)` and the outsider remains at its anchor. Whole-circle unilateral best-response attacks return no profitable deviation at canonical, local-box, and threshold-critical histories.

IS remains at the symmetric anchors on the audited policy histories. SW is symmetric at the anchors when singleton depths are symmetric; an auxiliary verifier re-solves asymmetric SW location histories after unilateral singleton-depth deviations.

## 5. Policy equilibrium

### IS

At symmetric anchors,

`c_IS(s)=c0+lambda*(1/4)/(t_bar-s)-v*s/s_bar`.

The exact affine-Bertrand welfare derivative from Stage 1 remains

`dW_IS/dc<0`.

The policy derivative changes sign through

`dc_IS/ds=lambda*(1/4)/(t_bar-s)^2-v/s_bar`.

The sufficient condition for `s_I*=s_bar` throughout the policy interval is

`v>1/18`.

All Stage-4 blocking thresholds lie above this value.

### SU

For both B-FIX and FULL, global policy scans over the full interval, with downstream location re-solution in FULL, select

`(s_12,s_3)=(s_bar,s_bar)`

through the threshold region used for the headline comparison. The member and outsider objectives are strictly increasing across the audited grids at the high-stakes parameter points.

### SW

The completion verifier re-solves locations after unilateral singleton-depth deviations. At the audited canonical/local redesign-cost points, the global best response is the upper boundary `s_i=s_bar` when the other singleton depths are at `s_bar`.

These SU/SW global policy results are numerical construction evidence and are explicit Stage-4A attack targets.

## 6. Welfare and canonical stable-set reversal

At `(v,gamma)=(.08,.03)`:

- IS welfare: approximately `.14275239` per country;
- B-FIX SU member: approximately `.14263839`;
- B-FIX SU outsider: approximately `.14251249`;
- FULL SU member: approximately `.14320705`;
- FULL SU outsider: approximately `.14182976`;
- FULL SW: approximately `.14251852` per country.

Therefore:

`B-FIX stable set = {IS}`,

while

`FULL stable set = {SU_12,SU_13,SU_23}`.

The same stable-set reversal occurs at every point in the pre-existing local grid

`v in {.07,.08,.09}` x `gamma in {.025,.03,.035}`.

This is stronger than the historical #65 fixed-depth welfare reversal because each FULL partition is evaluated after the C1 policy game.

## 7. Nested-benchmark identification and threshold ordering

The stronger Stage-4 result uses the blocking threshold in interoperability strength `v`.

### B-FIX

At the relevant full-depth policy equilibrium, the prospective SU-member welfare difference relative to IS has an exact rational factorization with unique relevant sign-changing factor `(15v-1)`. Hence

`v_FIX=1/15 approximately .06666667`.

### B-EXO-HIST

Using the exogenous positive-depth history inherited from #65 — IS at `s_bar`, SU at `(s_bar,0)`, SW at zero depth — and allowing repositioning, the unique audited root at `gamma=.03` is

`v_EXO approximately .11154504`.

### FULL

With both depth and positioning endogenous, the unique audited root at `gamma=.03` is

`v_FULL approximately .13368738`.

Thus

`v_FIX < v_EXO < v_FULL`.

The B-EXO/FULL ordering survives the pre-existing redesign-cost values:

| gamma | v_EXO-HIST | v_FULL |
|---:|---:|---:|
| .025 | .11264515 | .13493252 |
| .030 | .11154504 | .13368738 |
| .035 | .11048100 | .13247968 |

This produces a strict FULL-only interaction interval. At the round point `v=.12,gamma=.03`, selected only after deriving the threshold ordering as an illustration:

- B-FIX -> `{IS}`;
- B-EXO-HIST -> `{IS}`;
- FULL -> `{SU_12,SU_13,SU_23}`.

Thus removing product repositioning destroys the FULL result, and removing endogenous depth under the binding pre-existing exogenous-depth benchmark also destroys it.

## 8. Coalition stability operator

Stage 1 identified the blocking correspondence as ambiguous, so Stage 4 freezes it explicitly.

A deviating coalition forms an exclusive bloc; nondeviators retain residual links where feasible. The alternative partition is always evaluated at its own complete continuation equilibrium. Blocking requires strict gain for every deviating country.

This yields the intended three-country transitions:

- IS -> an SU by pair secession; singleton secession leaves the residual pair as an SU;
- SU -> SW by a member leaving; -> another SU by a cross-pair; -> IS by the grand coalition;
- SW -> SU by a pair; -> IS by the grand coalition.

No same-partition move counts as a deviation.

At the FULL interaction point the SU members prefer their union to IS and SW, the outsider is worse off than under IS, cross-SU deviations contain one indifferent incumbent member by symmetry, and the grand coalition therefore cannot strictly block an SU. Each SU is stable.

## 9. Mechanism decomposition

The FULL result requires the interaction of:

1. realized-interoperability benefit of depth;
2. direct within-bloc competitive compression from depth;
3. strategic horizontal re-differentiation by member firms;
4. endogenous outsider specificity, which raises cross-bloc separation and changes the return to member repositioning.

B-FIX removes channel 3. B-EXO-HIST removes endogenous channel 4. The ordered thresholds show that the FULL result cannot be reduced to either benchmark in the identified interval.

## 10. Candidate-proposition kill table

| Candidate | Stage-4 result | Status |
|---|---|---|
| P1 global demand/Bertrand continuation | uniform regularity + KKT/global deviation regression | `PASS at construction level` |
| P2 standards-contingent repositioning | strict member outward movement + whole-circle BR | `PASS` |
| P3 policy absorption/non-absorption condition | exact IS marginal trade-off, upper-depth region | `PASS / partial analytic characterization` |
| P4 stable-partition reversal B-FIX vs FULL | `{IS}` vs three SUs on pre-existing local points | `PASS` |
| P5 FULL-only result vs B-FIX and B-EXO | ordered thresholds; v=.12 interaction witness | `PASS` |
| P6 broad/global parameter classification | not required at Stage 4 | `NOT CLAIMED` |

No candidate required an unauthorized feature repair.

## 11. Preliminary theorem certificates

Authority:

`theorem_certificates/STAGE04_REVIVAL_C1_PRELIMINARY_CERTIFICATES.md`.

P5 — the ordered blocking-threshold / FULL-only interaction result — is the headline candidate passed to Stage 4A.

## 12. Limiting / boundary checks

- `s=0` gives zero C1 realized off-diagonal interoperability and recovers the zero-depth limit.
- `s=s_bar` gives full within-bloc realized interoperability.
- the exact IS policy threshold `1/18` separates the simple upper-depth region from lower/interior policy behavior;
- all headline blocking thresholds are strictly above `1/18`, avoiding an IS-policy-regime switch inside the headline threshold comparison;
- policy boundaries are allowed outcomes; no policy cost was added to force interiority.

## 13. Solver/failure ledger

No material continuation used for the Stage-4 headline result is classified `UNRESOLVED` or `NUMERICAL_FAILURE`.

Construction solvers used:

- exact/symbolic affine-Bertrand algebra where available;
- finite KKT active-set demand for hostile price deviations;
- symmetric SU root reconstruction followed by whole-circle unilateral location best-response attacks;
- full-domain policy grids with local refinement / downstream re-solution for high-stakes bloc deviations;
- a separate SW unilateral-policy/location completion verifier.

Remaining proof maturity gaps are certification gaps, not hidden solver failures.

## 14. Permanent regression / historical failures

The revival continues to preserve:

- the historical Salop continuation failures;
- PR #65 fixed-depth result;
- Stage-1 policy-adjustment absorption result for the source architecture;
- main's canonical termination record.

The new C1 result does not rewrite those negatives.

## 15. Artefact audit

Created for Stage 4:

- `model/REVIVAL_STAGE4_C1_MINIMAL_MODEL_2026-09-10.md`;
- `verification/stage04_revival_c1_minimal_model.py`;
- `verification/stage04_revival_policy_completion.py`;
- `theorem_certificates/STAGE04_REVIVAL_C1_PRELIMINARY_CERTIFICATES.md`;
- this Stage-4 review;
- `decisions/STAGE04_REVIVAL_DECISIONS.md`.

The production manuscript remains stale and is not updated at Stage 4.

## 16. Exact residual risks for Stage 4A

Stage 4A must independently attack, rather than inherit:

1. global Bertrand theorem applicability at every stated upstream history;
2. all SU location equilibria inside the threshold brackets, including multiplicity;
3. global SU and SW policy best responses beyond finite-grid evidence;
4. uniqueness of `v_EXO` and `v_FULL` roots;
5. continuity/local-open-set language around the strict threshold ordering;
6. the residual-membership blocking correspondence and all admissible alternative partitions;
7. whether any alternative equilibrium selection changes the stable-set result.

A failure of any headline item at Stage 4A reopens or kills the construction; Stage 4A may not silently repair it.

## 17. Canonical verdict and route

**STAGE 4 VERDICT: GO.**

**ROUTE: GO TO STAGE 4A — INDEPENDENT MATHEMATICAL ADVERSARIAL CERTIFICATION GATE.**

No Stage 6, theory freeze, journal positioning, manuscript rehabilitation, or submission authorization is permitted before Stage 4A PASS and the later workflow gates.
