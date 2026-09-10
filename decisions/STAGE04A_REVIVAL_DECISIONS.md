# Stage 4A Revival Decisions

Date: 2026-09-10

Workflow: `ryotamatsuki/research-paper-workflow` v2.1.

Branch: `revival/stage00-coalition-repositioning`.

## Decision 1 — Stage-4A verdict

**NO-GO / REOPEN STAGE 4.**

The C1 mechanism is not rejected economically at this gate. The correctness blocker is an omitted alternative equilibrium in the SU product-location subgame.

## Decision 2 — binding counterexample

At `(s_12,s_3)=(.25,.25)` and `(v,gamma)=(.08,.03)`, two distinct pure-strategy SU location Nash equilibria survive independent whole-circle unilateral best-response audits:

1. preferred outward branch
   `x≈(.13544022,.53122644,.83333333)`;
2. omitted crossing branch
   `x≈(.47774332,.18892335,.83333333)`.

The first gives `W_M(SU)>W(IS)` while the second gives `W_M(SU)<W(IS)`.

The same qualitative multiplicity appears at the Stage-4 interaction point `(v,gamma)=(.12,.03)`.

Permanent regression artifact:

`verification/stage04a_independent_multiplicity_red_team.py`.

## Decision 3 — claims retained

Retain provisionally:

- global affine-demand regularity on the stated Stage-4 primitive box;
- existence of the preferred outward SU repositioning equilibrium;
- exact IS marginal policy trade-off and the sufficient `v>1/18` upper-depth condition;
- exact B-FIX threshold component `v_FIX=1/15`.

These objects are not sufficient to proceed while the FULL continuation is selection-sensitive.

## Decision 4 — claims revoked / reopened

Reopen and revoke Stage-4 certification of the following as selection-free model claims:

- `FULL stable set = {SU_12,SU_13,SU_23}`;
- the nine-point stable-set reversal as a unique equilibrium implication;
- `v_FULL≈.13368738` as a unique model-implied threshold;
- the ordered threshold result `v_FIX<v_EXO<v_FULL` as a selection-free theorem;
- the statement that B-FIX and B-EXO-HIST jointly identify a FULL-only stable partition without an equilibrium-selection qualification;
- the FULL SU upper-depth policy equilibrium as a selection-free continuation result.

## Decision 5 — no silent refinement

The following are not authorized as implicit fixes:

- closest-anchor selection;
- no-crossing/order preservation;
- best-response-dynamics selection from anchors;
- Pareto/welfare dominance;
- risk dominance;
- arbitrary branch selection.

Any selection/refinement must be explicitly economically justified, applied symmetrically, and routed through the workflow.

## Decision 6 — Stage-4 repair contract

Reopened Stage 4 must:

1. characterize the relevant SU location equilibrium correspondence over the policy and threshold domain;
2. determine whether the policy/stability result is invariant across all relevant equilibria;
3. if not invariant, determine whether a standard/economically defensible refinement is part of the intended economic model;
4. re-solve bloc policy choices under the correct continuation object;
5. restate blocking/stability and threshold results with exact equilibrium-selection quantifiers;
6. preserve the crossing equilibrium as a permanent regression case;
7. return `NO-GO` if no defensible, non-ad-hoc resolution preserves a substantive FULL-only coalition result.

## Decision 7 — downstream routing

Stage 6 novelty re-kill is blocked.

Stage 7.5A formal verification implementation is not yet authorized because theorem scope is unstable, although Stage 4A records `FORMALIZATION APPLICABLE` and a preliminary target map.

Theory freeze, journal selection, manuscript rehabilitation, and submission remain blocked.

## Canonical route

`Stage 4 GO -> Stage 4A FAIL -> REOPEN STAGE 4 (multiplicity / selection characterization)`.
