# Stage 4R — Multiplicity / Selection Characterization Repair

Date: 2026-09-10

Workflow: `ryotamatsuki/research-paper-workflow` v2.1.

Branch: `revival/stage00-coalition-repositioning`.

## 1. Executive verdict

**GO — REPEAT STAGE 4A.**

Stage 4A correctly falsified the prior low-`gamma` selection-free claim. Stage 4R does not impose a closest-anchor, no-crossing, dynamics-based, welfare-based, or risk-dominance selection rule. Instead it preserves the crossing equilibrium and narrows the candidate theorem domain using the existing repositioning-cost curvature `gamma`.

Construction evidence shows that the omitted crossing equilibrium is a low-adjustment-cost phenomenon in the audited region. At a conservative higher-cost point `(v,gamma)=(.11,.10)`, extensive full-system multi-start search finds a single SU location Nash equilibrium at the headline full-depth history, and the coalition-stability effect survives.

The repaired claim is therefore ready for a fresh independent Stage-4A attack. It is not yet mathematically certified.

## 2. Binding failure retained

At `(v,gamma)=(.12,.03)` and SU full depths, the permanent Stage-4A regression still returns at least two global-BR pure-strategy location equilibria. Stage 4R explicitly asserts this before testing the repaired region.

The low-`gamma` stable-set and threshold claims remain revoked as selection-free results.

## 3. Equilibrium-correspondence search

The repair verifier solves the full three-firm location FOC system from dispersed starts and then checks each retained root against whole-circle unilateral deviations.

A declared lower-bound construction audit at `gamma=.05` covers 18 histories:

- `v in {.07,.11,.13}`;
- policy points `(s_12,s_3)` equal to `(0,0)`, `(.05,.20)`, `(.125,.125)`, `(.20,.05)`, `(.25,0)`, and `(.25,.25)`.

No alternative global-BR SU equilibrium is found at any of those histories.

This result is deliberately classified as **construction evidence only**. It does not prove a continuous uniqueness region and does not make `.05` an analytic bifurcation threshold.

## 4. Conservative repaired point

The headline repair point is

`(v,gamma)=(.11,.10)`.

This point is chosen away from the observed low-cost multiplicity frontier rather than at the smallest numerical value that happens to remove the crossing branch.

At FULL SU depth `(s_12,s_3)=(.25,.25)`, a 33-start full-system search including the old crossing seed finds one global-BR Nash candidate:

`x_SU approximately (.14246245,.52420422,.83333333)`.

The old crossing seed no longer converges to a second global-BR equilibrium.

## 5. Welfare / stability at the repaired point

Approximate national welfare is

- IS: `.1432822599` per country;
- FULL SU member: `.1433644618`;
- FULL SU outsider: `.1419734070`;
- FULL SW: `.1425185185` per country.

Hence a prospective SU pair strictly prefers SU to IS, while SU members also prefer SU to SW. The outsider is worse off under SU than under IS, so the grand coalition does not strictly block the SU. Under symmetry and the strict-blocking rule, the construction stable set is the three bilateral SUs.

In B-FIX at the same `v`, the exact threshold `1/15` has already been crossed, so IS is not pair-blocked by SU. Thus the core repositioning-essential B-FIX/FULL coalition difference survives after moving away from the multiplicity region.

## 6. Policy stage re-solution

IS: the exact sufficient condition `v>1/18` remains valid, so `s_I=.25` at `v=.11`.

SU: with downstream location re-solved, the member objective is strictly increasing over a 21-point full-domain scan in `s_12` holding `s_3=.25`; the outsider objective is likewise strictly increasing in `s_3` holding `s_12=.25`. Construction policy candidate: `(.25,.25)`.

SW: after re-solving the symmetric downstream location continuation following unilateral singleton-depth deviations, national welfare is strictly increasing over the 21-point scan. Construction policy candidate: `(.25,.25,.25)`.

These are not substitutes for the fresh Stage-4A global policy attack.

## 7. Repaired threshold comparison

At `gamma=.10`:

- `v_FIX = 1/15 = .0666666667` exactly;
- `v_EXO-HIST approximately .0993400328`;
- `v_FULL approximately .1196400688`.

Thus

`v_FIX < v_EXO-HIST < v_FULL`.

The repaired illustration `v=.11` satisfies

`v_EXO-HIST < .11 < v_FULL`.

Consequently the construction outcomes are:

- B-FIX: IS stable against SU pair blocking;
- B-EXO-HIST: IS stable against SU pair blocking;
- FULL: SU pair blocks IS.

However, Stage 4R narrows the conceptual headline to the **repositioning-induced shift between B-FIX and FULL after endogenous policy optimization**. B-EXO-HIST remains an auxiliary pre-existing benchmark. The paper may not claim that endogenous policy choice is generically necessary merely because this one exogenous-depth history fails to reproduce FULL.

## 8. Why the repair is not an ad hoc selection

No equilibrium is removed by fiat. The strategy set remains the full circle, crossings remain allowed, and the low-`gamma` crossing equilibrium remains part of the model.

The repair uses only an existing economically interpretable parameter: `gamma` is the curvature of the real product-redesign cost. The mathematical issue discovered by Stage 4A is itself about insufficient adjustment friction permitting a large leapfrog equilibrium. It is therefore legitimate to ask whether a higher-friction domain yields a unique continuation while preserving the economic effect.

The subsequent welfare/stability test is conditional on that unchanged model.

## 9. Candidate theorem scope after repair

The strongest defensible Stage-4R candidate is:

> There exists a higher-repositioning-cost regular region of the unchanged C1 model in which the relevant SU location continuation is selection-free, and allowing post-policy product repositioning strictly shifts the SU-vs-IS blocking threshold relative to the otherwise identical fixed-position policy game.

At construction level, `(v,gamma)=(.11,.10)` is an interior witness for the coalition-ranking difference and `gamma=.05` is a lower audit point at which the declared finite equilibrium-set search finds no alternative equilibrium.

The words `unique`, `region`, and `selection-free` remain **candidate quantifiers** until repeat Stage 4A independently certifies them.

## 10. Candidate-proposition status

| Claim | Stage 4R status |
|---|---|
| low-gamma SU multiplicity exists | `PASS / PERMANENT REGRESSION` |
| no ad hoc selection is needed for repaired point | `PASS at construction level` |
| repaired SU equilibrium at `(.11,.10)` | `CONSTRUCTION PASS; alternative-equilibrium search found one` |
| SU/SW/IS upper-depth policy candidates at repaired point | `CONSTRUCTION PASS` |
| B-FIX threshold `1/15` | `RETAINED EXACT` |
| repaired FULL threshold about `.11964007` | `CONSTRUCTION PASS` |
| B-FIX vs FULL stable/blocking difference at `(.11,.10)` | `CONSTRUCTION PASS` |
| continuous uniqueness/open-region theorem | `NOT YET CERTIFIED — STAGE 4A TARGET` |

## 11. Artifact / evidence ledger

Primary repair verifier:

`verification/stage04r_multiplicity_safe_region.py`.

Model-scope record:

`model/REVIVAL_STAGE4R_C1_MULTIPLICITY_REPAIR_2026-09-10.md`.

Permanent old counterexample retained:

`verification/stage04a_independent_multiplicity_red_team.py`.

The repair verifier was independently executed during Stage 4R construction and returned:

- low-gamma multiplicity count: `2`;
- no-alternative declared safe-grid histories: `18`;
- repaired SU location: approximately `(.14246245,.52420422,.83333333)`;
- `W_IS=.1432822599`, `W_SU_member=.1433644618`, `W_SU_outsider=.1419734070`, `W_SW=.1425185185`;
- thresholds `.06666667`, `.09934003`, `.11964007`.

## 12. Formal-verification status

The Stage-4A applicability decision remains **FORMALIZATION APPLICABLE**. No Lean PASS is claimed yet. The eventual target map must include the exact fixed threshold, the IS policy inequality, welfare-to-blocking logic, and any analytic uniqueness/high-`gamma` condition that survives repeat Stage 4A.

## 13. Canonical verdict

**GO — REPEAT STAGE 4A INDEPENDENT MATHEMATICAL ADVERSARIAL CERTIFICATION.**

This GO certifies only that Stage 4 has a non-ad-hoc construction repair worth independently attacking. It does not restore theory freeze, Stage 6, journal selection, or submission authorization.

## 14. Repeat Stage-4A contract

The independent recheck must specifically:

1. search for non-symmetric and crossing SU equilibria at and around `(v,gamma)=(.11,.10)`;
2. attack the claimed higher-`gamma` uniqueness region rather than only the single witness;
3. re-solve policy deviations under any additional equilibrium found;
4. independently recompute the B-FIX and FULL blocking thresholds;
5. verify stable-set logic under the full strict-blocking correspondence;
6. fail the repair if welfare/stability again depends on equilibrium selection.
