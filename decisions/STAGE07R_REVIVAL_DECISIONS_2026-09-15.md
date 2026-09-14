# Stage 7R Decision Record

Date: 2026-09-15

## Verdict

**GO — RETURN TO STAGE 7.5 FOR SHORT REPEAT DECISION.**

## Authorized robustness exercise completed

The only Stage-7.5-authorized alternative formulation was used:

`chi_alt(s)=2(s/s_bar)-(s/s_bar)^2`.

No other primitive, player, timing assumption, coalition rule, selection rule, policy cost, asymmetry, extra market, or parameter retuning was introduced.

## Binding result

At `gamma=.10`, after re-optimizing policy under the alternative realization map:

- `v_FIX_alt approximately .05133198`;
- `v_FULL_alt approximately .10666955`;
- therefore `v_FULL_alt > v_FIX_alt`.

At the transparent witness `v=.08`:

- B-FIX: `W_M(SU)-W(IS) approximately -.000205416`;
- FULL: `W_M(SU)-W(IS) approximately +.000195579`.

Thus the B-FIX/FULL coalition-blocking difference survives the nonlinear realization map.

## Policy changes under the alternative map

Because `chi_alt'(s_bar)=0`, policy depth changes materially relative to the baseline and was fully re-solved.

At `v=.08, gamma=.10`:

- B-FIX IS depth approximately `.17777483`;
- B-FIX SU member depth approximately `.19091946`;
- FULL IS depth approximately `.17777483`;
- FULL SU member depth `.25`;
- SU outsider depth `.25` in both benchmark and FULL.

The robustness result is therefore not inherited mechanically from the baseline full-depth solution.

## Selection-safety record

The alternative-realization verifier attacked 20 material FULL-SU policy histories using dispersed full-system multi-starts and whole-circle unilateral best-response checks. Exactly one global-BR pure SU location Nash was retained at each attacked history.

This is finite stress evidence only; no arbitrary-function or global analytic uniqueness theorem is created.

## Scope carried forward

The project may now state that the threshold/stability mechanism survives one credible pre-specified nonlinear realized-interoperability mapping.

It may not claim robustness to arbitrary monotone realization functions, arbitrary demand, arbitrary product geometry, asymmetric countries, or arbitrary redesign-cost environments.

## Routing

**NEXT: REPEAT STAGE 7.5 — FULL-THEORY FREEZE DECISION.**

Stage 7.5A and Stage 8 remain blocked until the repeat Stage 7.5 verdict is issued.