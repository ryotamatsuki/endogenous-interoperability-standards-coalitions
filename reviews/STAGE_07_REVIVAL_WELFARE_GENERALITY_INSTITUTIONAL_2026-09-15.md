# Stage 7 — Welfare / Generality / Institutional Validation Review

Date: 2026-09-15

Branch: `revival/stage00-coalition-repositioning`

## Executive verdict

**GO — GO TO STAGE 7.5 FULL-THEORY FREEZE DECISION.**

Stage 7 validates the repaired higher-`gamma` contribution as economically interpretable and institutionally defensible, while narrowing its welfare and generality language.

The paper's main economic object remains the B-FIX versus FULL change in the SU-vs-IS national-welfare blocking threshold after endogenous standards-depth optimization. The result should be framed as an organizational/coalition consequence of post-policy product repositioning, not as a generic consumer-welfare case for regional standards.

## Welfare finding

At `(v,gamma)=(.11,.10)`, the FULL SU member's gain relative to IS decomposes as:

- domestic profit: about `+7.085e-5`;
- domestic consumer-surplus share: about `+1.136e-5`;
- national welfare: about `+8.220e-5`.

By contrast, with product positions fixed, the SU member loses about `3.730e-4` in national welfare relative to IS.

Therefore the threshold reversal is driven mainly by restored domestic producer rents after strategic repositioning. Consumer surplus modestly reinforces the FULL ranking at the repaired witness rather than driving it.

## Private / national ranking

At `gamma=.10`, the Stage-7 diagnostic obtains:

- domestic-firm profit indifference around `v=.1180578`;
- national-welfare indifference around `v=.1196401`.

Hence a small interval exists in which the government still prefers SU even after the domestic firm would prefer IS. This is a secondary welfare wedge and confirms that the coalition problem is not just a relabeled firm-profit game.

## Economic magnitude

The local level welfare difference is small, but the organizational threshold effect is not. FULL raises the blocking threshold from `1/15≈.06667` in B-FIX to about `.11964` at `gamma=.10`, an increase of roughly `.05297` or 79% relative to the B-FIX cutoff.

The paper should emphasize the change in the domain of coalition viability, not the small welfare difference at one calibration.

## Institutional validation

**PASS WITH QUALIFICATION.**

ETSI's testing architecture explicitly distinguishes which capabilities/options/functions an implementation supports and uses those statements to select conformance/interoperability tests. This supports an intensive-margin interpretation of realized interoperability rather than a purely binary compatibility indicator.

SAE J3400 and U.S. Joint Office materials likewise treat EV charging interoperability as involving physical, electrical, functional, communication, safety, and performance dimensions rather than connector shape alone.

The model's linear realization map `chi(s)=s/s_bar` is nevertheless a reduced-form normalization. The paper may use standards profiles, supported functions, implementation completeness, and interoperability testing as institutional motivation, but may not claim that real standards bodies literally choose the model's scalar `s`.

## Generality verdict

The mechanism can be stated without industry-specific labels if the environment contains:

1. an intensive standards/interoperability margin;
2. a compatibility benefit from deeper implementation;
3. competition compression from deeper harmonization;
4. a separate costly post-policy design margin;
5. domestic-profit-plus-consumer-surplus government objectives;
6. a selection-safe continuation region.

No theorem is currently established for arbitrary demand systems, arbitrary realization functions, asymmetric countries, or arbitrary redesign costs. Three-country symmetry, quadratic demand, cosine proximity, linear realization, and the reported numerical thresholds remain model-specific.

## Predictions retained for later manuscript use

- deeper harmonization should induce re-differentiation on nonstandardized dimensions;
- greater redesign flexibility should expand regional-coalition viability within the selection-safe region;
- very low redesign costs can create multiple product-position equilibria;
- firm-profit and national-welfare coalition rankings can diverge near the threshold;
- fixed-product policy evaluations can understate regional standards-union viability.

These are theoretical predictions, not empirical findings.

## Exposition triage

Main figure: `Delta_M(v)=W_M(SU)-W(IS)` for B-FIX versus FULL at `gamma=.10`, marking the two threshold crossings.

Main table: welfare decomposition across IS, B-FIX SU, and FULL SU at the repaired witness.

Appendix/secondary material: high-`gamma` threshold sensitivity, low-`gamma` multiplicity, and institutional mapping of standards depth.

## Kill tests

- Welfare as pure transfer accounting: **PASS**; both profit and consumer-surplus terms move, though profit dominates.
- Institutional primitive unsupported: **PASS WITH QUALIFICATION**; intensive realized interoperability is defensible, linearity is normalization.
- Generality merely relabeling: **PASS**; the strategic chain can be expressed independently of a specific industry.
- Policy claim exceeds assumptions: **PASS only under narrow wording**; no universal standards-policy recommendation is authorized.
- Visual result depends on uncertified computation: **PASS subject to later Stage 10/14 regeneration from certified code**.

## Canonical verdict

**GO.**

Routing: **STAGE 7.5 — FULL-THEORY FREEZE DECISION.**

Stage 7.5 must decide whether this narrow but certified threshold mechanism is substantial enough for full-paper investment. It may not broaden the theorem scope beyond the repeat Stage-4A certificate or resurrect killed Stage-6 contribution language.
