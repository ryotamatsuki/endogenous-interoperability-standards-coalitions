# Stage 7.5A Claim-Scope / Quantifier Certificates — Revival C1

Date: 2026-09-15

Workflow: `ryotamatsuki/research-paper-workflow` v2.1.

Canonical baseline: linear realized-interoperability map `chi(s)=s/s_bar`. Stage 7R's concave `chi_alt` is robustness evidence only.

## Q1 — Exact B-FIX blocking cutoff

Formal claim:

For every `v in [3/50,4/25]` in the frozen baseline B-FIX continuation, the prospective SU-member national-welfare difference `Delta_FIX(v)` satisfies

`Delta_FIX(v)>0 iff v<1/15`,

and `Delta_FIX(1/15)=0`.

Quantifiers: universal over the stated one-dimensional audited interval only.

Maturity: exact symbolic theorem. Lean target: `bFix_delta_pos_iff`, `bFix_delta_at_cutoff`.

Maximum prose: **The baseline fixed-position benchmark has exact SU-versus-IS member cutoff `v_FIX=1/15` on the audited threshold interval.**

Prohibited: global cutoff for all real `v`; arbitrary-demand theorem; statement about FULL.

State: PASS, subject to the Stage-7.5A formal build certificate.

## Q2 — IS upper-depth sufficient condition

Formal claim:

Under the frozen baseline symmetric-anchor IS continuation, for every `s in [0,1/4]`, if `v>1/18`, then the pairwise cross-curvature derivative with respect to standards depth is strictly negative. Together with the exact negative derivative of symmetric IS welfare with respect to cross-curvature, this is sufficient for IS welfare to rise with depth over that interval and hence for the upper depth to be optimal on that continuation.

Quantifiers: universal over `s in [0,1/4]`; sufficient condition in `v`, not necessary-and-sufficient.

Maturity: exact symbolic sign chain. Lean targets: `isCrossDerivative_neg`, `isWelfareDerivative_neg`, `welfareDepthDerivative_pos`.

Maximum prose: **`v>1/18` is a sufficient baseline condition for the symmetric IS continuation to favor the upper standards depth.**

Prohibited: `1/18` is necessary; arbitrary realization map; asymmetric-country theorem.

State: PASS, subject to the Stage-7.5A formal build certificate.

## Q3 — Repaired FULL blocking/stability result

Formal/computational claim:

At the baseline witness `(v,gamma)=(.11,.10)`, under the frozen strict-blocking correspondence and the independently audited partition-specific continuation:

- B-FIX retains IS against bilateral-SU pair blocking;
- FULL has the three bilateral SUs as stable partitions.

Equilibrium-set quantifier: at this witness, one pure-strategy location Nash is retained for IS, SU, and SW by the repeat Stage-4A adversarial search. The certificate does **not** prove analytic uniqueness of the complete equilibrium correspondence.

Maturity: independently certified computational result plus exact B-FIX threshold and strict welfare inequalities.

Maximum prose: **At the certified higher-redesign-cost witness, endogenous product repositioning changes the stable standards partition relative to the fixed-position benchmark.**

Prohibited: `the unique equilibrium`; `for all sufficiently high gamma`; `generically`; selection-free for all parameters.

State: PASS for the stated audited witness.

## Q4 — Baseline FULL numerical cutoff

Claim:

At `gamma=.10` in the baseline model, the independently reconstructed SU-member welfare-difference root on the audited continuation is approximately

`v_FULL=.1196400688`.

The exact B-FIX cutoff is `1/15`. Hence the baseline audited comparison has `v_FULL>v_FIX`.

Quantifiers: numerical root on the stated continuation/domain; not a closed-form or all-parameter theorem.

Maturity: independent numerical/root/global-BR certification, not Lean theorem.

Maximum prose: **At `gamma=.10`, the audited baseline FULL cutoff is about `.11964`, compared with exact B-FIX cutoff `1/15`.**

Prohibited: structural constant; analytic formula; global unique root outside the audited continuation.

State: PASS as independently certified numerical result.

## Q5 — Low-redesign-cost multiplicity boundary

Claim:

At specific audited low-redesign-cost histories including `(v,gamma)=(.08,.03)` and `(.12,.03)` at full SU depth, at least two economically distinct pure-strategy location Nash equilibria survive whole-circle unilateral best-response attacks, and their national-welfare rankings can differ.

Quantifier: existential counterexample at audited points.

Maturity: independent counterexample / permanent regression artifact.

Maximum prose: **Low redesign costs can generate location-equilibrium multiplicity; therefore global uniqueness is false in the baseline model.**

Prohibited: all low gamma imply multiplicity; an analytic bifurcation threshold has been proved.

State: PASS as counterexample certificate.

## Q6 — Alternative realization robustness

Claim:

For the one pre-specified robustness map

`chi_alt(s)=2(s/s_bar)-(s/s_bar)^2`,

with policy re-optimized from zero at `gamma=.10`, the numerical blocking cutoffs satisfy approximately

`v_FIX_alt=.05133198 < v_FULL_alt=.10666955`.

At `(v,gamma)=(.08,.10)`, B-FIX has a negative SU-member difference while FULL has a positive one. Twenty declared SU policy histories retain one global-BR pure Nash under the Stage-7R attack.

Quantifier: one named nonlinear map and finite attacked histories only.

Maturity: numerical robustness evidence, not a function-class theorem.

Maximum prose: **The qualitative blocking-threshold shift survives one pre-specified smooth concave alternative mapping from standards depth to realized interoperability.**

Prohibited: robust to arbitrary monotone/concave `chi`; generic functional-form robustness.

State: PASS as robustness evidence.

## Q7 — Welfare decomposition

Claim:

At `(v,gamma)=(.11,.10)`, the FULL-SU member gain relative to IS is approximately `8.22e-5`, decomposed into about `+7.085e-5` domestic profit and `+1.136e-5` domestic consumer-surplus share.

Quantifier: one certified numerical witness.

Maturity: numerical welfare-accounting diagnostic.

Maximum prose: **At the repaired witness, the reversal is mainly a domestic-producer-rent effect, with a smaller positive consumer-surplus contribution.**

Prohibited: producer rents always dominate; consumer surplus always rises.

State: PASS for witness interpretation.

## Q8 — Strict-blocking logic

Formal claim:

Given the frozen definition that a coalition strictly blocks iff every member strictly gains, two strict bilateral welfare gains imply a bilateral strict block, while one member with a weak loss rules out strict blocking.

Quantifiers: generic over welfare functions on the three-country player set, conditional on the strict-block definition.

Maturity: logical theorem. Lean targets: `pair_strict_block`, `no_strict_block_if_member_not_gain`.

Maximum prose: use only as logic mapping certified welfare inequalities to the model's frozen blocking concept.

Prohibited: claiming Lean proves the welfare inequalities or complete stable partition by itself.

State: PASS, subject to formal build certificate.

## Equilibrium-set / selection certificate

- No equilibrium-selection or refinement rule is used in the repaired baseline.
- The historical crossing equilibrium at low `gamma` remains in the model and is not removed.
- Repeat Stage 4A found no second global-BR pure Nash at the repaired witness and declared higher-`gamma` stress histories, but this is finite adversarial evidence rather than an analytic uniqueness theorem.
- Manuscript wording must avoid unqualified `the unique equilibrium`, `globally unique`, `for all sufficiently high gamma`, and `regardless of equilibrium selection`.

## Benchmark terminology certificate

- `B-FIX`: fixed-product-position policy benchmark. It is not a planner optimum or first best.
- `B-EXO-HIST`: auxiliary exogenous-depth historical benchmark. It does not establish generic necessity of policy endogeneity.
- `FULL`: endogenous coalition-depth plus post-policy repositioning continuation.
- Welfare comparisons are national welfare under decentralized partition-specific continuations, not social-planner optima.
- `first best` and `second best` are not authorized labels for these objects.

## Generality classification

- Exact theorem: B-FIX cutoff and baseline IS sign condition.
- Independently certified numerical/computational result: repaired FULL continuation, stable-set difference, FULL root.
- Numerical robustness: Stage 7R concave `chi_alt` exercise.
- Counterexample boundary: low-`gamma` multiplicity.
- Not established: arbitrary demand, arbitrary `chi`, arbitrary product geometry, asymmetric countries, global equilibrium uniqueness, or generic comparative statics in redesign cost.

## Maximum contribution wording entering freeze

> In the symmetric three-country baseline model, post-policy product repositioning can remain consequential after standards blocs optimize interoperability depth. At an independently audited higher-redesign-cost witness, restoring repositioning shifts the bilateral-union versus international-standardization national-welfare blocking cutoff relative to the fixed-position benchmark and changes the stable partition. The qualitative cutoff shift also survives one pre-specified concave alternative mapping from standards depth to realized interoperability.

Any stronger universal or generic wording requires a new theorem and downstream recertification.
