# Stage 7R — Alternative-Realization Robustness Review

Date: 2026-09-15

Branch: `revival/stage00-coalition-repositioning`

## 1. Executive verdict

**GO — RETURN TO STAGE 7.5 FOR SHORT REPEAT DECISION.**

The single robustness exercise authorized by Stage 7.5 passes without adding any new economic primitive or retuning parameters after observing the result.

The baseline linear realized-interoperability map

`chi(s)=s/s_bar`

was replaced only for this robustness exercise by the pre-specified smooth concave map

`chi_alt(s)=2(s/s_bar)-(s/s_bar)^2`.

All other objects are unchanged: players, timing, coalition/blocking rule, `Tau` map, demand, product-location technology, redesign cost, pricing continuation, national-welfare accounting, and the higher-redesign-cost test value `gamma=.10`.

After re-optimizing standards depth from zero under the alternative map, product repositioning still shifts the SU-versus-IS coalition-blocking threshold materially relative to the fixed-position benchmark.

## 2. Why policy had to be re-solved

The alternative map preserves

`chi_alt(0)=0`, `chi_alt(s_bar)=1`,

but has

`chi_alt'(s_bar)=0`.

Therefore the baseline upper-bound policy choices could not be copied into the robustness exercise. IS and SU depth choices were re-optimized under both B-FIX and FULL.

This is important because the robustness result is not mechanically inherited from the fact that the two realization functions agree at full depth.

## 3. Re-optimized threshold result

At `gamma=.10`, the alternative-realization blocking thresholds are approximately

- `v_FIX_alt = .05133198`;
- `v_FULL_alt = .10666955`.

Hence

`v_FULL_alt > v_FIX_alt`.

The gap is about `.05534`, so the threshold-shift mechanism remains economically material under the concave alternative realization map.

The direction of the blocking condition is unchanged: SU members prefer SU at lower `v` and cease to prefer it after the relevant cutoff. Therefore the larger FULL cutoff means that allowing repositioning expands the range in which a bilateral standards union can block IS relative to the fixed-position policy game.

## 4. Transparent same-primitive witness

Choose the pre-declared higher-cost environment `gamma=.10` and the round value `v=.08`, which lies strictly between the two re-estimated thresholds.

After policy re-optimization:

### B-FIX

- IS depth: approximately `.17777483`;
- SU member-bloc depth: approximately `.19091946`;
- SU outsider depth: `.25`;
- `W_M(SU)-W(IS) approximately -2.05416e-4`.

Thus IS is not pair-blocked by SU.

### FULL

- IS depth: approximately `.17777483`;
- SU member-bloc depth: `.25`;
- SU outsider depth: `.25`;
- `W_M(SU)-W(IS) approximately +1.95579e-4`.

Thus an SU pair strictly prefers the bilateral union to IS.

The qualitative B-FIX/FULL coalition difference therefore survives the alternative realization function at the same primitives.

## 5. Selection-safety attack

Because the low-`gamma` baseline model previously exhibited an omitted crossing equilibrium, Stage 7R also attacks alternative-equilibrium risk rather than relying only on the symmetric construction branch.

The verifier uses a full three-firm FOC system, dispersed multi-starts including the historical crossing seed, and whole-circle unilateral best-response checks.

Declared attacked histories:

- `v in {.06,.08,.10,.11}`;
- `s_12 in {0,.0625,.125,.1875,.25}`;
- `s_3=.25`;
- `gamma=.10`;
- alternative concave `chi_alt`.

Across all 20 histories, the attack retains exactly one global-BR pure-strategy SU location Nash equilibrium per history.

This is finite adversarial robustness evidence, not an analytic uniqueness theorem for all nonlinear realization functions or all parameter values.

## 6. Stage-7.5 blocker resolution

The prior Stage-7.5 blocker was:

> the surviving coalition-threshold mechanism had not yet survived a credible alternative functional formulation.

That blocker is now resolved.

The alternative specification changes a substantively relevant primitive mapping — how implementation depth translates into realized interoperability — and forces different endogenous standards-depth choices. Nevertheless the central result survives:

`optimized standards depth -> post-policy repositioning -> shifted government blocking threshold`.

The result is therefore not solely an artifact of the baseline linear realization map.

## 7. Scope discipline

Stage 7R does **not** establish:

- robustness to arbitrary monotone `chi` functions;
- robustness to a different demand system;
- robustness to non-cosine product proximity;
- robustness to asymmetric countries;
- analytic global uniqueness;
- exact quantitative threshold invariance.

The defensible statement is only that the core threshold mechanism survives one pre-specified, economically credible nonlinear realization map after full policy re-optimization and equilibrium-selection attack.

## 8. Evidence artifact

Primary reproducible artifact:

`verification/stage07r_alternative_realization_robustness.py`.

Verified outputs from the Stage-7R execution:

- `v_FIX_alt approximately .05133198`;
- `v_FULL_alt approximately .10666955`;
- at `v=.08`: B-FIX member difference approximately `-.000205416`;
- at `v=.08`: FULL member difference approximately `+.000195579`;
- B-FIX policies approximately `s_IS=.17777483`, `s_12=.19091946`, `s_3=.25`;
- FULL policies approximately `s_IS=.17777483`, `s_12=.25`, `s_3=.25`;
- alternative-equilibrium stress histories attacked: `20`;
- retained global-BR SU Nash count at every attacked history: `1`.

## 9. Canonical verdict

**GO.**

Routing: **REPEAT STAGE 7.5 — FULL-THEORY FREEZE DECISION.**

No other robustness modification is authorized or needed before that repeat decision.
