# Stage 7.5A — Generality / Quantifier Red-Team + Formal Verification Gate

Date: 2026-09-15

Branch: `revival/stage00-coalition-repositioning`

Workflow authority: `ryotamatsuki/research-paper-workflow` v2.1.

## 1. Scope-red-team result

The economic theorem set survives the quantifier/generalization audit, but only after tightening several phrases that appeared in earlier construction-stage records.

The paper is **not** licensed to claim analytic uniqueness on a continuous high-`gamma` region, generic robustness, or a theorem for arbitrary realization functions. The strongest licensed scope is a baseline symmetric three-country result at the independently audited higher-redesign-cost witness/domain, together with one named nonlinear-realization robustness exercise.

The word `region` is prohibited when it could be read as an analytically characterized open parameter set. Use `audited higher-redesign-cost domain`, `audited stress set`, or a named witness/finite test set as appropriate.

## 2. Formal quantifier table

| Claim | Maximum mathematical quantifier | Evidence class | State |
|---|---|---|---|
| B-FIX cutoff | for every `v in [.06,.16]`, `Delta_FIX(v)>0 iff v<1/15`; equality at `1/15` | exact symbolic + targeted Lean | PASS subject to clean formal build |
| IS `1/18` condition | for every `s in [0,.25]`, `v>1/18` is sufficient for the certified symmetric-anchor sign chain favoring greater depth | exact symbolic + targeted Lean | PASS subject to clean formal build |
| repaired location continuation | at the named witness and declared finite Stage-4A stress histories, the adversarial protocol retained one global-BR pure Nash | independent numerical/global-deviation audit | PASS; not analytic uniqueness |
| baseline FULL cutoff | at `gamma=.10` on the audited continuation, numerical root `v_FULL≈.1196400688` | independent numerical root + global-BR audit | PASS as numerical certificate |
| stable-partition difference | at `(v,gamma)=(.11,.10)` under frozen strict blocking, B-FIX retains IS while FULL bilateral SUs are stable | exact+computational certificate | PASS at witness |
| low-`gamma` multiplicity | there exist audited low-`gamma` histories with at least two pure Nash and different welfare rankings | independent counterexample | PASS; rules out global uniqueness |
| nonlinear-`chi` robustness | for one pre-specified concave `chi_alt`, at `gamma=.10` the numerical threshold ordering and same-primitives coalition difference survive | finite numerical robustness | PASS; not function-class theorem |
| welfare decomposition | at repaired witness, producer-rent term dominates the positive FULL-SU member welfare difference | numerical accounting | PASS at witness |

Full claim-level details are frozen in `theorem_certificates/STAGE075A_REVIVAL_C1_SCOPE_CERTIFICATES_2026-09-15.md`.

## 3. Equilibrium-set / selection audit

The first Stage 4A found a genuine crossing equilibrium at low redesign cost. It remains an admissible equilibrium and permanent regression artifact. No refinement, closest-anchor rule, no-crossing restriction, welfare selection, or dynamic selection has been added.

Repeat Stage 4A and Stage 7R use alternative-equilibrium searches plus whole-circle unilateral best responses. Their result is finite adversarial evidence over declared histories. It is not a proof that the full equilibrium correspondence is unique on an open parameter neighborhood.

Therefore:

- `the unique equilibrium` is prohibited except when explicitly referring to the single equilibrium retained by a named finite audit protocol;
- `selection-free for sufficiently high gamma` is prohibited;
- `selection-safe higher-gamma region` is replaced by `independently audited higher-redesign-cost domain/witness`;
- the low-`gamma` multiplicity result may be used to show global uniqueness is false, but not to claim multiplicity for every low `gamma`.

## 4. Assumption-dependence audit

Economically essential ingredients for the current result:

1. an intensive interoperability/harmonization margin;
2. compatibility benefit from deeper implementation;
3. competitive compression from deeper harmonization;
4. a separate costly post-policy product-design/repositioning margin;
5. national objectives combining domestic consumer surplus and producer profit;
6. strict coalition blocking evaluated using complete partition-specific continuations;
7. an audited continuation at the point where a selection-independent welfare comparison is reported.

Baseline-specific tractability/normalization objects:

- three symmetric countries;
- quadratic representative-consumer demand;
- circular one-dimensional product geometry;
- cosine proximity;
- linear baseline `chi(s)=s/s_bar`;
- equal national consumer populations;
- inherited anchor locations and numerical normalizations.

No theorem is licensed for arbitrary demand, arbitrary `chi`, country asymmetry, arbitrary product geometry, or arbitrary redesign cost.

## 5. Selection/refinement provenance audit

No new selection rule is present in the repaired theory. The low-`gamma` crossing equilibrium is not removed. The higher-cost results are reported only on histories where the independent attacks did not retain an alternative pure Nash.

This treatment is symmetric: the same whole-circle/global-BR criterion is applied to preferred and inconvenient roots. FOC roots defeated by finite deviations are not counted as Nash equilibria.

## 6. Function-class / counterexample audit

The project makes no broad theorem over the class of all increasing or concave realization maps. Stage 7R supplies exactly one nonbaseline map,

`chi_alt(s)=2(s/s_bar)-(s/s_bar)^2`,

and is classified as numerical robustness evidence.

The permanent low-`gamma` crossing equilibrium is the binding counterexample to any global uniqueness statement. Because no arbitrary-demand or arbitrary-function theorem is claimed, no stronger function-class counterexample theorem is required for PASS.

## 7. Baseline versus robustness versus general theorem

- Baseline exact theorem: B-FIX `1/15` threshold and IS sign/sufficient-condition core.
- Baseline independently certified computational result: repaired FULL continuation, FULL root, stable-set difference.
- Robustness evidence: the one pre-specified concave `chi_alt` exercise.
- General theorem: none over demand/realization/product-geometry function classes.

The paper must keep these categories separate in theorem labels, abstract/introduction prose, and robustness discussion.

## 8. Welfare-selection audit

National welfare is `CS/3 + domestic firm profit` under the explicit equal-population/equal-country accounting convention. It is not a planner objective over unrestricted allocations.

At the repaired witness the relevant partition continuations pass the repeat Stage-4A equilibrium-set attack, so the reported welfare ranking is licensed for that audited continuation. Low-`gamma` welfare rankings are selection dependent and may not be written as model-unique implications.

## 9. Benchmark-definition audit

- `B-FIX` is the otherwise identical policy/coalition game with product positions fixed at inherited anchors.
- `B-EXO-HIST` is an auxiliary historical exogenous-depth benchmark only.
- `FULL` restores endogenous post-policy repositioning.

None is a `first best` or `second best`. No planner benchmark is used in the headline result. `Constrained efficient` is also prohibited unless a separate planner problem is introduced and solved.

## 10. Claim-scope wording certificate

Maximum defensible contribution wording:

> In the symmetric three-country baseline model, post-policy product repositioning can remain consequential after standards blocs optimize interoperability depth. At an independently audited higher-redesign-cost witness, restoring repositioning shifts the bilateral-union versus international-standardization national-welfare blocking cutoff relative to the fixed-position benchmark and changes the stable partition. The qualitative cutoff shift also survives one pre-specified concave alternative mapping from standards depth to realized interoperability.

Prohibited stronger wording includes:

- `generically`;
- `for all sufficiently high redesign costs`;
- `the unique equilibrium` without a named finite audit scope;
- `robust to concave/monotone realization functions`;
- `arbitrary demand systems`;
- `arbitrary asymmetric countries`;
- `the FULL cutoff is analytically .11964`;
- `Lean formally verifies the complete economic model`.

## 11. Evidence ledger

| Claim | Attack | Artifact | Surviving limitation |
|---|---|---|---|
| B-FIX exact cutoff | exact factorization/sign audit + Lean target | `verification/stage04_revival_c1_minimal_model.py`; `formal/StandardsCoalitionFormal/{Core,Threshold}.lean` | baseline audited interval |
| IS sign condition | exact symbolic derivative + Lean target | Stage-4 verifier; `formal/StandardsCoalitionFormal/{Policy,Welfare}.lean` | symmetric-anchor baseline continuation; sufficient only |
| repaired FULL continuation | independent multistart + whole-circle BR | `verification/stage04a_repeat_high_gamma_red_team.py` | finite audited histories, no analytic uniqueness theorem |
| low-`gamma` multiplicity | clean-room alternative-root search + global BR | `verification/stage04a_independent_multiplicity_red_team.py` | existential audited counterexample |
| nonlinear realization | full policy re-optimization + multistart attack | `verification/stage07r_alternative_realization_robustness.py` | one named alternative map |
| strict blocking | logical audit + Lean target | `formal/StandardsCoalitionFormal/Blocking.lean` | welfare inequalities themselves remain external inputs |

## 12. Formal-verification boundary

Applicability: **FORMALIZATION APPLICABLE**.

Target map: `formal/FORMAL_VERIFICATION_TARGET_MAP_2026-09-15.md`.

Lean intentionally certifies only exact algebra/sign/blocking logic. The continuous Nash correspondence, global deviation search, numerical FULL cutoff, policy equilibrium, and Stage-7R robustness remain outside the formal model and retain their independent computational certificates.

The Formal Verification Gate is closed only when the pinned Lean 4.33.1 / mathlib v4.33.1 project builds cleanly, placeholder/axiom audits pass, and the final formal certificate records the successful CI run. Until that evidence exists, Stage 7.5A cannot issue `GO`.

## 13. Scope-red-team verdict apart from formal build

**PASS.** No remaining headline claim requires broader quantifiers than the evidence supports after the wording downgrades above.

The only remaining gate condition at the time this review record was initialized is the clean formal build/certificate. The canonical final Stage-7.5A verdict must be recorded only after that condition is resolved.
