# Repeat Stage 4A — Independent Mathematical Adversarial Certification Gate

Date: 2026-09-15

Workflow: `ryotamatsuki/research-paper-workflow` v2.1.

Branch: `revival/stage00-coalition-repositioning`.

Stage-4R authority: `reviews/STAGE_04R_REVIVAL_C1_MULTIPLICITY_REPAIR_2026-09-10.md`.

Independent repeat artifact: `verification/stage04a_repeat_high_gamma_red_team.py`.

## 1. Executive verdict

**GO — MATHEMATICAL ADVERSARIAL CERTIFICATION PASS.**

The first Stage 4A correctly found low-repositioning-cost SU location multiplicity and reopened Stage 4. Stage 4R retained that counterexample and narrowed the candidate theorem domain to a higher-redesign-cost region without adding a selection rule or changing the C1 model.

The repeat Stage 4A independently reconstructs the model from primitives and attacks the repaired region. It finds no selection-dependent continuation at the repaired witness or in the declared higher-`gamma` stress domain. The repaired B-FIX versus FULL blocking/stability difference survives.

This PASS is intentionally narrower than the original Stage-4 claim. It does **not** certify uniqueness for all `gamma`, all policy histories, or the entire continuous parameter space. The low-`gamma` crossing equilibrium remains a binding permanent counterexample.

## 2. Independent reconstruction

The repeat red-team implementation does not import or call the Stage-4 or Stage-4R production solvers. It separately reconstructs:

- the `Tau` standards-friction map;
- the C1 realized-interoperability map;
- the quadratic-demand matrix `K`;
- affine Bertrand prices and quantities;
- quadratic circular repositioning costs;
- equal-population national welfare;
- the full three-firm location FOC system;
- whole-circle unilateral location deviations;
- SU policy-deviation continuations;
- SU-member blocking thresholds against IS.

The old crossing seed is included deliberately in every relevant alternative-equilibrium attack.

## 3. Permanent low-gamma failure remains

At FULL-SU full depth with `(v,gamma)=(.12,.03)`, the independent repeat code again finds at least two global-BR pure-strategy location equilibria.

Therefore all old low-`gamma` selection-free statements remain revoked. Nothing in this repeat audit rehabilitates the original `.03` theorem scope.

Classification: **MULTIPLE — PERMANENT REGRESSION**.

## 4. Higher-gamma alternative-equilibrium audit

### 4.1 Full-depth stress box

For

- `v in {.09,.10,.11,.12,.13}`;
- `gamma in {.08,.10,.12}`;
- FULL-SU depth `(.25,.25)`,

the independent full-system multi-start search plus whole-circle BR test retains exactly one attacked pure-strategy Nash equilibrium at each of the 15 points.

A nonpreferred FOC root appears in at least one attack (`v=.12,gamma=.08`), but it fails a finite unilateral-deviation test and is not a Nash equilibrium. Thus the repeat audit distinguishes stationary-point multiplicity from equilibrium multiplicity.

### 4.2 Policy-history stress audit

The red-team also attacks 81 SU histories:

- `v in {.10,.11,.12}`;
- `gamma in {.08,.10,.12}`;
- nine material depth histories spanning zero, intermediate, and full depths along both bloc-policy dimensions.

Every attacked history has exactly one retained global-BR pure-strategy Nash equilibrium under the declared search protocol.

### 4.3 All headline partitions at repaired witness

At `(v,gamma)=(.11,.10)` and full equilibrium depths, independent multi-start attacks find one global-BR location equilibrium for each of:

- IS: anchors `(1/6,1/2,5/6)`;
- SW: anchors `(1/6,1/2,5/6)`;
- SU: approximately `(.14246245,.52420422,.83333333)`.

Equilibrium-set status for the repaired headline histories: **UNIQUE IN THE INDEPENDENT ADVERSARIAL SEARCH / NO ALTERNATIVE PURE NASH FOUND**.

The manuscript may not promote this to a global analytic uniqueness theorem over all parameter values.

## 5. Candidate-deviation audit

The repaired SU equilibrium survives whole-circle unilateral deviations for all three firms. The IS and SW anchor equilibria likewise survive whole-circle attacks at the repaired witness.

The old crossing-equilibrium configuration is explicitly seeded. At `gamma=.10` it is not retained as a global-BR Nash equilibrium.

Status: **PASS**.

## 6. Policy-continuation audit

At `(v,gamma)=(.11,.10)`, each material unilateral SU depth deviation is re-solved downstream.

A 51-point full-domain audit gives:

- SU member-bloc welfare strictly increasing in `s_12` holding `s_3=.25`;
- outsider welfare strictly increasing in `s_3` holding `s_12=.25`.

Thus the repaired FULL-SU policy candidate remains

`(s_12,s_3)=(.25,.25)`.

IS upper-depth choice follows from the exact surviving condition `v>1/18`.

The prior Stage-4R SW deviation completion is not contradicted by the independent location-equilibrium attack; SW at the repaired witness remains at full singleton depth and anchors.

Status: **PASS FOR REPAIRED HEADLINE DOMAIN**.

## 7. Welfare and blocking audit

At `(v,gamma)=(.11,.10)` the independent reconstruction gives approximately:

- `W_IS=.1432822599`;
- `W_SU_member=.1433644618`;
- `W_SU_outsider=.1419734070`;
- `W_SW=.1425185185`.

Hence:

- a prospective pair strictly prefers SU to IS;
- SU members strictly prefer SU to SW;
- the outsider prefers IS to SU, so the grand coalition does not strictly block SU;
- a cross-SU deviation contains an incumbent member who is not strictly better off under the symmetric relabeling.

Under the frozen strict-blocking correspondence, the FULL stable set at the repaired witness is

`{SU_12,SU_13,SU_23}`.

For B-FIX at the same `v`, the exact fixed-position threshold is `1/15`; since `.11>1/15`, prospective SU members do not block IS. Thus B-FIX retains IS while FULL admits the bilateral SUs.

Status: **PASS**.

## 8. Independent threshold reconstruction

At `gamma=.10`, the repeat implementation independently obtains:

- `v_FIX=1/15=.0666666667`;
- `v_EXO-HIST≈.0993400329`;
- `v_FULL≈.1196400688`.

Therefore

`v_FIX < v_EXO-HIST < v_FULL`.

The repaired witness `.11` lies strictly between `v_EXO-HIST` and `v_FULL`.

The conceptual headline remains B-FIX versus FULL: post-policy repositioning shifts the SU-vs-IS blocking threshold after policy optimization. B-EXO-HIST is auxiliary and does not establish a generic necessity result for endogenous policy choice.

Status: **PASS**.

## 9. Quantifier / scope certificate

The strongest certified scope after the repeat audit is deliberately limited:

1. low `gamma` is **not** selection-free;
2. a declared higher-`gamma` stress domain around the repaired point survives independent alternative-equilibrium attacks;
3. the repaired witness has strict welfare/blocking inequalities and an independently reproduced threshold ordering;
4. the project may claim a **higher-redesign-cost regular region / computationally certified continuation class**, not global uniqueness over all `gamma`;
5. any future analytic uniqueness threshold must be separately proved before being called necessary or sufficient.

The repeat audit finds no correctness blocker requiring another model repair. Remaining generality questions belong to later quantifier/generality and formal-verification gates rather than being hidden Stage-4 equilibrium failures.

## 10. Headline theorem-certificate table

| Claim | Repeat Stage-4A state | Scope |
|---|---|---|
| P1 affine-demand / Bertrand continuation | `PASS` | retained Stage-4A domain |
| P2 post-policy outward repositioning | `PASS` | repaired higher-`gamma` continuation; low-gamma multiplicity separately recorded |
| P3 IS policy condition `v>1/18` | `PASS` | exact sufficient condition |
| P4 B-FIX vs FULL stable/blocking difference | `PASS` | repaired headline witness and declared higher-gamma stress domain |
| P5 repaired FULL threshold `≈.11964007` | `PASS` | `gamma=.10`, repaired continuation class |
| P6 global uniqueness for all parameters | `NOT CLAIMED` | prohibited overstatement |
| P7 low-gamma selection-free reversal | `FAIL / PERMANENTLY REVOKED` | multiplicity regression |

## 11. Indifference / selection audit

No new equilibrium-selection rule is used.

The repeat PASS does not rely on:

- nearest-anchor selection;
- order preservation;
- no-crossing restrictions;
- best-response-dynamics selection;
- welfare/Pareto selection;
- risk dominance.

Strict blocking continues to require strict gain for all deviators. Symmetric relabeling ties therefore do not create a strict cross-SU block.

Status: **PASS**.

## 12. Evidence ledger

| Claim | Attack | Artifact | Result | Limitation |
|---|---|---|---|---|
| low-gamma multiplicity | old crossing seed + full-system multi-start + whole-circle BR | `verification/stage04a_repeat_high_gamma_red_team.py` | reproduced | low-gamma claim remains dead |
| repaired SU continuation | independent multi-start, random starts, old crossing seed, finite global BR | same | one attacked Nash at witness | not a global analytic theorem |
| higher-gamma continuation robustness | 15 full-depth points + 81 policy histories | same | no alternative pure Nash found | declared stress domain only |
| IS/SW alternatives | independent full-system multi-start at witness | same | one attacked Nash each | headline domain |
| SU policy equilibrium | downstream re-solution on 51-point unilateral grids | same | upper boundaries survive | numerical global audit, not closed form |
| FULL threshold | independent root reconstruction | same | `.1196400688` | gamma fixed at `.10` |
| stable-set logic | recompute all relevant strict-blocking inequalities | this review + verifier | bilateral SUs stable in FULL | symmetric 3-country model |

## 13. Formal-verification applicability

**FORMALIZATION APPLICABLE.**

The preliminary target map remains:

1. exact B-FIX factorization and `v_FIX=1/15`;
2. exact IS welfare derivative and upper-depth sufficient condition `v>1/18`;
3. welfare inequalities -> strict-blocking logical implications;
4. threshold-ordering algebra where it can be isolated from numerical location continuation;
5. any later analytic sufficient condition delimiting the high-`gamma` uniqueness domain.

The global continuous location correspondence remains outside the current Lean target map and is separately covered by adversarial numerical/global-BR certification. Formal implementation is still pending until the theorem scope is stable enough for Stage 7.5A.

## 14. Permanent regressions

Both files remain mandatory:

- `verification/stage04a_independent_multiplicity_red_team.py` — original low-gamma counterexample;
- `verification/stage04a_repeat_high_gamma_red_team.py` — repaired-domain independent attack.

Future changes must keep the former failing the low-gamma uniqueness claim and the latter passing the repaired scope.

## 15. Canonical verdict and routing

**GO — MATHEMATICAL ADVERSARIAL CERTIFICATION PASS.**

Route: **Stage 6 — Novelty Re-Kill**.

This PASS does not authorize theory freeze, journal selection, manuscript rehabilitation, or submission. Stage 6 must now re-kill novelty against the *repaired*, narrower high-`gamma` theorem rather than the superseded low-`gamma` result.
