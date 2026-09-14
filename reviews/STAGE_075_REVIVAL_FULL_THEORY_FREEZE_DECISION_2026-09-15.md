# Stage 7.5 — Full-Theory Freeze Decision

Date: 2026-09-15

Branch: `revival/stage00-coalition-repositioning`

Workflow: `ryotamatsuki/research-paper-workflow` v2.1.

## 1. Executive verdict

**CONDITIONAL GO — RETURN TO STAGE 7 FOR ONE BOUNDED ROBUSTNESS TEST.**

The revival now contains a narrow, certified, potentially publishable full-paper mechanism rather than merely a solved calibration. The result survives independent mathematical red-team review, a current novelty re-kill, welfare decomposition, and institutional validation. It can be stated without model-specific notation and has a substantive organizational implication: downstream strategic product repositioning can change which standards coalition can block another even after standards depth is endogenously optimized.

However, one material full-paper blocker remains. The surviving result has not yet been shown to survive any credible alternative functional formulation outside the current quadratic-demand / circular-location / cosine-proximity / linear-realization baseline. The workflow explicitly asks whether the contribution survives at least one credible alternative formulation already tested. That condition is not yet met.

This is the only Stage-7.5 blocker. No new economic mechanism is authorized.

## 2. Can the contribution be stated without model notation?

**YES.**

Maximum notation-free statement:

> When deeper interoperability both raises compatibility benefits and intensifies product-market competition, firms may respond after the standard is chosen by redesigning products along dimensions that remain flexible. That redesign can preserve domestic producer rents enough to alter governments' incentives to remain in, leave, or form a standards coalition. Consequently, a policy analysis that fixes product design can misstate coalition-stability thresholds even when governments already optimize standards depth.

This is the core economic contribution. It does not depend for its verbal statement on the exact `K`, `Tau`, `phi`, or `chi` notation.

## 3. Minimal causal / strategic chain

The minimal chain is:

`interoperability depth`

`-> compatibility benefit + competitive compression`

`-> costly post-policy product re-differentiation`

`-> domestic profit and consumer surplus`

`-> national welfare`

`-> strict coalition blocking / stable partition`.

The indispensable interaction is not merely that standards affect product design. It is that the downstream design response changes the **government coalition-blocking threshold after the upstream policy instrument has already been optimized**.

## 4. Essential assumptions versus normalization / tractability

### Economically essential for the current mechanism

1. an intensive interoperability / harmonization margin;
2. a compatibility or interoperability benefit that rises with implementation depth;
3. a competition-compression effect from deeper harmonization;
4. a separate product-design margin chosen after standards policy;
5. positive but finite redesign cost;
6. government objectives that include domestic market surplus rather than only firm profit;
7. a coalition/blocking concept comparing complete continuation equilibria;
8. a continuation region in which equilibrium selection does not overturn welfare rankings.

### Baseline normalizations / tractability devices not yet shown essential

- three symmetric countries;
- quadratic representative-consumer demand;
- circular one-dimensional product space;
- cosine proximity `phi`;
- linear realization `chi(s)=s/s_bar`;
- equal national consumer populations;
- the exact anchors and numerical normalization;
- the exact numerical threshold values.

These devices are not authorized as general economic claims merely because the core mechanism can be described without them.

## 5. Welfare / organizational substance

**PASS.**

At the repaired witness `(v,gamma)=(.11,.10)`, FULL SU member welfare exceeds IS by about `8.22e-5`, while the otherwise identical fixed-position SU falls below IS by about `3.73e-4`.

The welfare-level difference is modest, but the organizational threshold shift is economically material:

`v_FIX = 1/15 ≈ .06667`

versus

`v_FULL ≈ .11964` at `gamma=.10`.

Thus the main substantive object is not the level gain at one calibration. It is the large change in the domain over which a bilateral standards union can strictly block international standardization.

The Stage-7 decomposition also shows that the effect is not pure transfer accounting: both domestic producer profit and the domestic consumer-surplus share move, with producer-rent preservation supplying most of the reversal.

## 6. Novelty / referee-value test

**PASS, narrowly.**

Stage 6 killed generic claims about compatibility-induced differentiation, continuous standards depth, standards breadth/depth and coalition stability, coalition-induced downstream strategy, and regional-versus-multilateral standards stability.

The surviving contribution is narrower:

> costly post-policy product repositioning shifts a government standards-coalition blocking threshold relative to the fixed-position policy benchmark after endogenous standards-depth optimization.

No exact prior theorem or one-paper relabeling producing this result has been identified. The strongest current novelty threat remains the 2026 Menegaki–Serfes standards/coalition program and must be rechecked later if a fuller public version appears.

A skeptical field referee could therefore see a real strategic-feedback result rather than setup novelty, provided the paper demonstrates that the result is not an artifact of the baseline functional form.

## 7. Alternative-formulation test

**FAIL / NOT YET SATISFIED.**

What has been tested so far is substantial but remains inside one functional architecture:

- different `v` values;
- different redesign-cost `gamma` values;
- complete policy-depth deviations;
- low-`gamma` multiplicity versus higher-`gamma` selection-safe regions;
- fixed-position versus endogenous-position benchmarks;
- independent equilibrium solvers and alternative-equilibrium searches.

What has **not** yet been tested is a credible alternative formulation of a baseline functional object such as:

- a nonlinear monotone realized-interoperability map replacing linear `chi`;
- a non-cosine smooth product-proximity function;
- another defensible demand curvature specification that preserves the same economic ingredients.

The absence of such a test prevents a Stage-7.5 `GO` under the canonical workflow's full-paper criterion.

## 8. Exactly one authorized repair

Return to Stage 7 for **one bounded robustness exercise only**.

Preferred test:

> Replace the linear realization map `chi(s)=s/s_bar` with one pre-specified smooth monotone alternative that preserves `chi(0)=0` and `chi(s_bar)=1`, without changing players, timing, coalition rule, product-position technology, or adding any primitive. Re-solve B-FIX and FULL and test whether the qualitative blocking-threshold shift survives without parameter retuning.

Recommended pre-specified alternative:

`chi_alt(s)=2(s/s_bar)-(s/s_bar)^2` for `s in [0,s_bar]`.

Rationale: this is a simple concave implementation-completeness map with diminishing marginal realized interoperability. It preserves endpoints and does not mechanically encode the desired coalition result.

Passing requirement:

- equilibrium and policy continuation remain well defined on a declared selection-safe higher-`gamma` test region;
- `v_FULL_alt > v_FIX_alt` or an equivalent strict B-FIX/FULL coalition-blocking difference survives;
- no parameter may be tuned after observing the result merely to restore the headline ranking;
- if the result fails, Stage 7.5 must reassess whether the paper is baseline-specific rather than silently adding another mechanism.

No second robustness modification is authorized in this cycle.

## 9. Full-paper investment decision conditional on repair

If the single alternative-realization test passes, the project is suitable for full-paper investment and should return directly to Stage 7.5 for a short repeat decision, then proceed to Stage 7.5A.

If it fails materially, the project should not receive full-theory-freeze authorization merely because the baseline is mathematically correct; the correct route is to reconsider scope or classify the result as baseline-specific.

## 10. Formal-verification interaction

Formalization remains **APPLICABLE** but is not the blocker at this stage. Stage 7.5A remains responsible for closing the Formal Verification Gate.

Current high-value formal targets remain:

- exact B-FIX threshold `v_FIX=1/15`;
- exact IS welfare derivative / sufficient upper-depth condition `v>1/18`;
- logical mapping from strict welfare inequalities to blocking/stability;
- exact algebraic components of any threshold ordering that survive final scope certification.

The alternative-formulation robustness test is an economic-scope test and is not replaced by Lean.

## 11. Canonical verdict

**CONDITIONAL GO.**

Exact blocker: **the surviving coalition-threshold mechanism has not yet survived a credible alternative functional formulation.**

Earliest affected stage: **Stage 7 — Generality / robustness validation.**

Routing: **Stage 7R — one bounded alternative-realization robustness test, then repeat Stage 7.5.**

Theory freeze, Stage 7.5A, Stage 8, manuscript rehabilitation, journal positioning, and submission authorization remain blocked until this single condition is resolved.