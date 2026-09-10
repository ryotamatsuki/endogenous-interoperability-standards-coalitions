# Stage 4A Adversarial Theorem Certificates — Revival C1

Date: 2026-09-10

Status: **STAGE-4A CERTIFICATION RECORD — OVERALL FAIL / REOPEN STAGE 4**

Workflow authority: `ryotamatsuki/research-paper-workflow` v2.1.

Independent evidence: `verification/stage04a_independent_multiplicity_red_team.py`.

## P1 — Global affine-demand / Bertrand continuation

Exact claim: on the Stage-4 primitive domain `v in [0.06,0.16]`, `s_C in [0,1/4]`, and full-circle locations, the quadratic demand matrix is positive definite under the stated sufficient inequalities and the attacked high-stakes histories possess the positive affine Bertrand equilibrium used downstream.

Quantifiers: global matrix-domain statement; price-equilibrium independent attacks at representative material histories.

Candidate-deviation audit: PASS at attacked histories via direct nonnegative-demand/KKT best responses.

Alternative-equilibrium audit: no alternative price equilibrium found in dispersed multi-start attacks at the headline histories.

Boundary/active-set audit: nonnegative demand semantics retained; no zero-demand equilibrium used in the headline histories.

Independent reconstruction: PASS.

Evidence maturity: analytic matrix bounds plus independent numerical global price attack.

State: **PASS WITH STATED DOMAIN/SCOPE.** No broader theorem beyond the encoded affine-demand architecture is certified here.

## P2 — Standards-contingent repositioning

Exact claim certified: there exists a pure-strategy SU location equilibrium near `(.13544,.53123,.83333)` at the canonical full-depth history, and the two members move away from their anchors.

Quantifier: existence at audited parameter/policy points; not uniqueness.

Candidate-deviation audit: PASS via dense whole-circle unilateral best responses.

Alternative-equilibrium audit: **MULTIPLE**. A second pure-strategy equilibrium exists near `(.47774,.18892,.83333)` at `(v,gamma)=(.08,.03)` and persists at other headline points.

Welfare robustness: NOT invariant across equilibria.

State: **PASS AS EXISTENCE ONLY; FAIL AS UNIQUE OR SELECTION-FREE CHARACTERIZATION.**

## P3 — IS realized-interoperability policy trade-off

Exact claim: at symmetric IS anchors,

`dW_IS/dc<0`,

`dc/ds=lambda*(1/4)/(t_bar-s)^2-v/s_bar`,

so `v>1/18` is sufficient for welfare to increase throughout the admissible depth interval and for the upper boundary to be optimal conditional on the symmetric-anchor continuation.

Quantifiers: sufficient-condition result on the stated affine baseline; not necessary globally outside that continuation.

Independent reconstruction: PASS.

Alternative-equilibrium attack: no second IS location Nash was found in the headline attack; no contradiction to the Stage-4 IS branch was found.

State: **PASS WITH THE STATED CONDITIONAL SCOPE.**

## P4 — B-FIX vs FULL stable-set reversal

Stage-4 claim: at the canonical/local points, B-FIX has stable set `{IS}` while FULL has exactly `{SU_12,SU_13,SU_23}`.

Candidate-deviation audit of Stage-4 preferred SU continuation: PASS.

Alternative-equilibrium audit: FAIL. The same SU subgame admits a second global-BR Nash equilibrium with member welfare below IS and below SW.

At `(v,gamma)=(.08,.03)`:

- preferred SU equilibrium member welfare about `.14320705` > IS about `.14275239`;
- omitted SU equilibrium member welfare about `.14061475` < IS and < SW about `.14251852`.

Therefore the stable-set conclusion changes with continuation equilibrium selection.

State: **FAIL AS SELECTION-FREE CLAIM.**

Earliest affected stage: Stage 4.

## P5 — Ordered blocking thresholds and FULL-only interaction interval

Stage-4 claim: `v_FIX=1/15 < v_EXO-HIST≈.111545 < v_FULL≈.133687`, giving a FULL-only interval and, at `v=.12,gamma=.03`, B-FIX/B-EXO-HIST `{IS}` versus FULL bilateral SUs.

Exact B-FIX component: survives; `v_FIX=1/15` is not affected by location multiplicity because positions are fixed.

EXO/FULL components: not selection invariant. The omitted SU branch yields a materially different welfare curve; over the audited `[.06,.16]` range the omitted branch remains below IS in the independent attack rather than sharing the preferred-branch root.

FULL upstream policy continuation is also selection-sensitive because policy deviations lead to location subgames with multiple equilibria.

State: **FAIL AS A UNIQUE MODEL-IMPLIED THRESHOLD ORDERING.**

The preferred-branch roots may remain valid conditional-on-selection numerical objects, but they are not certified model-level thresholds.

## P6 — Nested-benchmark identification

Stage-4 claim: both endogenous policy and repositioning are needed because neither B-FIX nor B-EXO-HIST reproduces the FULL stable partition in the interaction interval.

This depends on P4/P5's selection-free FULL continuation. Since those fail, the identification theorem is not currently certified.

State: **CONDITIONAL / NOT CERTIFIED.**

## Multiplicity certificate

Equilibrium-set status for the headline SU full-depth location subgame: **MULTIPLE**.

At least two distinct pure-strategy Nash equilibria are independently reproduced. Completeness of the equilibrium set is not yet established. Because welfare differs across the observed equilibria, completeness and/or a justified equilibrium-selection/refinement rule is material for every upstream policy and coalition claim.

## Indifference/refinement certificate

No zero-demand/zero-profit terminal indifference creates the discovered multiplicity.

No order-preservation, closest-anchor, dynamic-stability, risk-dominance, or welfare-selection refinement is part of the frozen Stage-4 model. None may be used to discard the crossing equilibrium without explicit re-authorization and symmetric application.

## Formal-verification applicability

Decision: **FORMALIZATION APPLICABLE**.

Preliminary Lean targets after Stage-4 repair:

- exact B-FIX factorization and `1/15` root;
- IS derivative and `1/18` sufficient condition;
- exact welfare-to-blocking logical implications;
- any analytic branch-condition or threshold-ordering inequalities that survive the repaired equilibrium correspondence.

Formal verification is not yet implemented and therefore is not a passing formal-verification state. The formal gate remains scheduled for Stage 7.5A after theorem scope stabilizes.

## Overall Stage-4A certificate

**FAIL — NO-GO / REOPEN STAGE 4.**

Primary blocker: omitted SU location equilibrium multiplicity changes national welfare and invalidates selection-free policy, threshold, and coalition-stability conclusions.
