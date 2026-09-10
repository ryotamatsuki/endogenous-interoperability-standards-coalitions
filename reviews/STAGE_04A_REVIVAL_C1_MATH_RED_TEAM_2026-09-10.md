# Stage 4A — Independent Mathematical Adversarial Certification Gate

Date: 2026-09-10

Workflow: `ryotamatsuki/research-paper-workflow` v2.1 at `f48984013898696f010f0437a8cfed6b5b54bdc2`.

Branch: `revival/stage00-coalition-repositioning`.

Stage-4 authority: `reviews/STAGE_04_REVIVAL_C1_MINIMAL_MODEL_2026-09-10.md`.

Independent regression artifact: `verification/stage04a_independent_multiplicity_red_team.py`.

## 1. Executive adversarial verdict

**NO-GO / REOPEN STAGE 4.**

The Stage-4 preferred SU location equilibrium is a valid pure-strategy Nash equilibrium at the audited headline points, but it is **not the only pure-strategy location equilibrium**. An independent clean-room multi-start solver, followed by whole-circle unilateral best-response attacks, finds a second economically distinct SU location Nash equilibrium at the same policy history and primitives.

The two equilibria yield opposite signs for the prospective SU-member welfare difference relative to IS. Therefore the Stage-4 claims that FULL has exactly the three bilateral SUs stable and that the FULL blocking threshold is uniquely about `.133687` are not equilibrium-selection invariant. The upstream policy game is also not selection-free because a bloc deviation changes a continuation subgame that may itself have multiple equilibria.

This is exactly the Stage-4A failure mode distinguished by the workflow: candidate-deviation verification of one equilibrium does not certify uniqueness or selection-free welfare.

Earliest affected stage: **Stage 4 — Minimal Model / equilibrium characterization**.

No new primitive or selection rule is authorized by this audit.

## 2. Independent reconstruction

The red-team implementation was written independently from the Stage-4 production location solver. It reconstructs from the C1 primitives:

- the pairwise `Tau` map;
- realized interoperability `M`;
- quadratic-demand matrix `K`;
- affine Bertrand continuation;
- repositioning-cost profit;
- equal-population national welfare.

Location candidates are obtained by solving the full three-firm first-order system from many random initial conditions. Each root is then tested against a dense whole-circle unilateral best response for every firm. A root is retained only if no unilateral deviation improves profit beyond the audit tolerance.

The red-team does not call `stage04_revival_c1_minimal_model.py`, its symmetric SU root routine, or its preferred-branch selector.

## 3. Fatal alternative-equilibrium finding

At full SU depth `(s_12,s_3)=(.25,.25)` and `(v,gamma)=(.08,.03)`, at least two distinct pure-strategy location Nash equilibria survive high-resolution whole-circle deviation tests.

### E1 — Stage-4 preferred outward equilibrium

`x approximately (.13544022,.53122644,.83333333)`.

National welfare:

- SU member: about `.14320705`;
- SU outsider: about `.14182976`.

IS welfare at its Stage-4 policy is about `.14275239`.

Hence on E1:

`W_M(SU)-W(IS) > 0`.

This reproduces the Stage-4 preferred branch.

### E2 — omitted crossing equilibrium

`x approximately (.47774332,.18892335,.83333333)`.

National welfare:

- SU member: about `.14061475`;
- SU outsider: about `.14296880`.

At the same IS continuation:

`W_M(SU)-W(IS) < 0`.

High-resolution unilateral best-response gaps for E2 are at numerical zero (approximately machine precision), and each firm's own-location second derivative is negative at the candidate. E2 is therefore not a mere stationary point defeated by a finite deviation.

The two member firms have crossed far past their inherited anchors. The Stage-4 production solver's symmetric-near-anchor branch did not enumerate this equilibrium; its subsequent whole-circle deviation check only established that E1 is a Nash equilibrium, not that E1 is unique.

## 4. The problem persists at the headline interaction point

At `(v,gamma)=(.12,.03)` and the same full SU depths, the independent audit again finds two distinct pure-strategy location Nash equilibria.

Preferred branch:

`x approximately (.135247,.531420,.833333)`,

with member welfare about `.143577`, above IS welfare about `.143460`.

Alternative branch:

`x approximately (.478405,.188262,.833333)`,

with member welfare about `.140983`, far below IS.

Thus the Stage-4 illustrative claim

`B-FIX -> IS, B-EXO-HIST -> IS, FULL -> SU`

holds under the preferred SU continuation but fails as a selection-free statement. Under the alternative SU continuation, prospective members do not prefer SU to IS.

## 5. Local robustness does not cure multiplicity

The omitted second equilibrium is not confined to one calibration. Independent multi-start searches find both the outward and crossing SU equilibria at the pre-existing redesign-cost values `gamma in {.025,.03,.035}` for `v=.08` and also at `v=.12`.

Therefore the nine-point Stage-4 local sign table cannot be interpreted as robustness of a unique equilibrium result. It is robustness of one selected continuation branch unless and until the complete equilibrium correspondence is characterized.

## 6. Candidate-deviation audit

### Preferred E1

PASS as an **existence** claim at the audited points. Dense whole-circle unilateral searches reproduce no profitable location deviation.

### Alternative E2

PASS as an additional equilibrium at the audited points. Dense whole-circle unilateral searches likewise find no profitable deviation.

Consequence: the candidate-deviation audit validates both equilibria and therefore strengthens, rather than resolves, the multiplicity objection.

## 7. Alternative-equilibrium / multiplicity audit

Status for the relevant SU location subgame:

**MULTIPLE.**

The equilibrium-set audit has not yet established that E1 and E2 are the only equilibria. It is sufficient for the present Stage-4A verdict that at least two equilibria exist and that welfare differs materially across them.

Because the Stage-4 manuscript-facing statements use a selection-free continuation welfare, the absence of a complete equilibrium correspondence is a correctness blocker.

## 8. Indifference / tie audit

All attacked price/quantity histories have strictly positive prices and quantities; no zero-demand or zero-profit indifference is used to generate E2.

There is a separate coalition-level tie issue: under a relabel-invariant selection, a member moving from one symmetric SU to another can be indifferent. Stage 4 used strict blocking, so such a tie does not block. However, once the SU continuation itself is multiple, symmetry of equilibrium **sets** does not by itself impose the same branch selection across different relabeled SUs. Any claim that cross-SU deviations contain an indifferent incumbent therefore requires an explicit relabel-invariant selection rule or an equilibrium-correspondence statement. No such rule is currently part of the model.

## 9. Equilibrium-selection / refinement audit

No equilibrium-selection or refinement rule is frozen in the Stage-4 model.

In particular, the following possible rules are **not currently model assumptions** and may not be invoked retroactively:

- select the equilibrium closest to inherited anchors;
- preserve product order / prohibit crossings;
- select the equilibrium reached from anchors under best-response dynamics;
- choose the Pareto-dominant or welfare-dominant equilibrium;
- choose a risk-dominant or stable-dynamics equilibrium.

Introducing any such rule requires an explicit economic justification and workflow routing. Stage 4A does not choose one.

## 10. Upstream policy-continuation consequence

The multiplicity is not confined to a terminal welfare comparison. Policy blocs choose depth before the location game, so policy payoffs depend on which downstream location equilibrium is selected after every policy deviation.

Stage-4 policy verification followed the preferred symmetric-near-anchor continuation. The alternative-equilibrium audit shows that at least some material SU policy histories possess another continuation with materially different member and outsider welfare.

Accordingly the claims

- `(s_12,s_3)=(s_bar,s_bar)` is the selection-free FULL SU policy equilibrium;
- `v_FULL` is a unique model-implied blocking threshold;
- FULL has a unique stable-partition implication,

are **UNRESOLVED / FALSE AS SELECTION-FREE CLAIMS** until the full continuation correspondence is characterized.

A preliminary continuation along the omitted branch also changes policy incentives substantially, confirming that this is not a harmless terminal multiplicity. Stage 4 must reconstruct the policy game over the equilibrium correspondence rather than assume E1 after every deviation.

## 11. Bertrand continuation audit

The red-team reconstructed the affine Bertrand continuation independently and additionally ran multi-start global price best-response dynamics with KKT nonnegative demand at representative IS, preferred-SU, omitted-SU, and hostile histories. The audited histories converged to the same positive interior price equilibrium from dispersed starts; no second price equilibrium was found in this attack.

The Stage-4A failure is therefore not a discovered price-continuation defect. The fatal issue is the upstream product-location multiplicity and its welfare/policy consequence.

## 12. Headline theorem-certificate table

| Claim | Stage-4A state | Reason |
|---|---|---|
| P1 global affine-demand regularity / Bertrand continuation | `PASS WITH STATED DOMAIN` | uniform matrix bounds survive; independent price attack found no contradiction |
| P2 standards-contingent repositioning | `PASS AS EXISTENCE ONLY` | preferred outward equilibrium exists, but is not unique |
| P3 IS realized-interoperability policy trade-off | `PASS` | exact symbolic sign logic unaffected by SU multiplicity |
| P4 B-FIX vs FULL stable-set reversal | `FAIL AS SELECTION-FREE CLAIM` | alternative SU equilibrium reverses member welfare sign |
| P5 ordered blocking thresholds / FULL-only interval | `FAIL AS MODEL-UNIQUE CLAIM` | `v_FULL` and EXO/FULL welfare roots depend on SU equilibrium branch |
| P6 nested-benchmark identification | `CONDITIONAL / NOT CERTIFIED` | depends on P4/P5 selection-free continuation values |

## 13. Welfare-selection / benchmark audit

The equal-country welfare accounting `W_i=CS/3+Pi_i` is internally consistent under the Stage-4 explicit population/ownership convention.

The problem is not accounting. It is **welfare-selection robustness**: the SU member welfare at identical primitives and policy depth differs materially across valid location equilibria.

Therefore any welfare or stability statement must say whether it applies to:

- all SU equilibria;
- one explicitly selected equilibrium;
- best/worst equilibrium welfare;
- an equilibrium correspondence with a robust blocking concept.

Stage 4 currently does none of these.

## 14. Evidence ledger

| Claim | Attack | Artifact | Result | Surviving limitation |
|---|---|---|---|---|
| preferred SU location is Nash | independent FOC root + whole-circle finite deviations | `verification/stage04a_independent_multiplicity_red_team.py` | PASS | existence only |
| SU location uniqueness / selection-free continuation | random multi-start alternative-root search + global BR audit | same artifact | FAIL | at least two equilibria; full set not yet enumerated |
| canonical FULL welfare ranking | evaluate both valid SU equilibria against same IS continuation | same artifact | FAIL selection-free | signs differ by equilibrium |
| FULL stable-set reversal | recompute blocking implication under both SU welfare branches | this review + verifier | FAIL selection-free | branch-selection rule absent |
| FULL blocking threshold | track distinct SU equilibrium branches over headline `v` interval | independent Stage-4A calculations recorded here | FAIL model-unique | preferred branch root not equilibrium invariant |
| Bertrand candidate | independent KKT/global price BR multi-start attack at high-stakes histories | Stage-4A audit calculation | survives attack | no new global theorem beyond stated domain |

## 15. Formal-verification applicability

**FORMALIZATION APPLICABLE.**

This project has proof-critical algebra, threshold inequalities, equilibrium conditions, and selection-sensitive case logic. Lean 4/mathlib is the preferred later proof assistant under workflow v2.1.

Preliminary target map for Stage 7.5A if the project later returns to a certified theorem scope:

1. exact B-FIX factorization and threshold `v_FIX=1/15`;
2. exact IS derivative and policy sufficient condition `v>1/18`;
3. algebraic welfare identities used in blocking comparisons;
4. exact logical implications from certified welfare inequalities to strict-blocking stable sets;
5. if Stage 4 later obtains analytic equilibrium-branch conditions, formalize the branch-condition inequalities and threshold ordering.

The continuous global location-equilibrium correspondence is not declared formally certified by this target map; numerical/global-deviation certification remains separately necessary.

Formal verification is **not yet implemented or passed**. The applicability decision and target map are the only Stage-4A formalization outputs.

## 16. Permanent regression test

The omitted crossing equilibrium is now a permanent regression requirement:

`verification/stage04a_independent_multiplicity_red_team.py`.

Any Stage-4 repair must reproduce or explicitly eliminate this equilibrium through a justified model/refinement change. It may not disappear merely because a preferred solver starts near the anchors.

## 17. Exact blocker and earliest affected stage

Blocker:

> **The full-circle SU product-location subgame has multiple pure-strategy Nash equilibria with materially different national welfare, but Stage 4 treated one preferred continuation branch as if it supplied selection-free welfare, policy, threshold, and coalition-stability values.**

Earliest affected stage: **Stage 4 — Minimal Model**.

This is a mathematical equilibrium-characterization defect, not a Stage-2 novelty failure and not yet evidence that C1's economic mechanism is false.

## 18. Canonical verdict and routing

**NO-GO / REOPEN STAGE 4.**

Required Stage-4 repair task before any repeat of Stage 4A:

1. characterize the relevant SU location-equilibrium correspondence over the policy/threshold domain;
2. determine whether policy and coalition results are invariant across all relevant equilibria;
3. if they are not invariant, state and economically justify any proposed selection/refinement before using it;
4. re-solve the policy game under the correct continuation object;
5. restate the threshold/stability theorem with exact selection quantifiers;
6. rerun Stage 4 construction verification and then repeat Stage 4A independently.

Stage 6, Stage 7.5A, theory freeze, journal selection, and manuscript rehabilitation remain blocked.
