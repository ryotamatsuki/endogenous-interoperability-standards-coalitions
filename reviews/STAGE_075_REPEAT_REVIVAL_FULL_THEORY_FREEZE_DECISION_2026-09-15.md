# Repeat Stage 7.5 — Full-Theory Freeze Decision

Date: 2026-09-15

Branch: `revival/stage00-coalition-repositioning`

Workflow: `ryotamatsuki/research-paper-workflow` v2.1.

## 1. Executive verdict

**GO — GO TO STAGE 7.5A GENERALITY / QUANTIFIER RED-TEAM + FORMAL VERIFICATION GATE.**

The sole blocker identified in the first Stage 7.5 has been resolved. The surviving coalition-threshold mechanism now survives one pre-specified, economically credible alternative functional formulation of realized interoperability without introducing any new primitive, changing the game architecture, or retuning parameters after observing the result.

The project therefore qualifies for full-paper investment. This is not yet a theory freeze. Stage 7.5A remains mandatory and must certify theorem scope, quantifiers, robustness language, benchmark terminology, and the embedded Formal Verification Gate before Stage 8 can be entered.

## 2. Status of the prior blocker

Prior blocker:

> The surviving coalition-threshold mechanism had not yet survived any credible alternative functional formulation outside the baseline quadratic-demand / circular-location / cosine-proximity / linear-realization architecture.

Stage 7R replaced only the baseline realization map

`chi(s)=s/s_bar`

for a robustness exercise by the pre-specified concave map

`chi_alt(s)=2(s/s_bar)-(s/s_bar)^2`.

All other primitives, timing, coalition/blocking rule, demand system, product-location technology, redesign cost, pricing continuation, and welfare accounting were held fixed.

The blocker is therefore **RESOLVED**.

## 3. Alternative-formulation result carried into this decision

At `gamma=.10`, Stage 7R re-optimized policy from zero under the alternative realization map and obtained approximately:

- `v_FIX_alt=.05133198`;
- `v_FULL_alt=.10666955`.

Hence

`v_FULL_alt > v_FIX_alt`.

At the same-primitive witness `(v,gamma)=(.08,.10)`:

- B-FIX: `W_M(SU)-W(IS)≈-.000205416`;
- FULL: `W_M(SU)-W(IS)≈+.000195579`.

Thus the qualitative coalition comparison reverses when product repositioning is restored even under the nonlinear realization map.

Stage 7R also attacked 20 material SU policy histories with dispersed full-system multi-starts plus whole-circle unilateral-deviation checks and retained one global-BR pure SU location Nash at each attacked history.

This is sufficient for the Stage-7.5 alternative-formulation criterion. It is not a theorem for arbitrary realization functions.

## 4. Full-paper investment test

### 4.1 Notation-free mechanism

**PASS.**

The core result can be stated without model-specific notation:

> When deeper interoperability raises compatibility benefits but compresses product differentiation, firms may strategically re-differentiate after policy is chosen. That response can preserve domestic producer rents enough to alter governments' coalition-blocking incentives, so fixed-product analyses can misstate the stability domain of standards coalitions even when standards depth is optimized endogenously.

### 4.2 Strategic novelty

**PASS, NARROWLY.**

Stage 6 has already killed setup novelty and component-level claims. The surviving object is specifically the B-FIX versus FULL government blocking-threshold shift after endogenous standards-depth optimization.

No exact prior theorem or one-paper relabeling has been identified for this result. The strongest live novelty threat remains the Menegaki–Serfes 2026 standards/coalition program and must be rechecked later if a fuller public version appears.

### 4.3 Welfare / organizational substance

**PASS.**

In the certified baseline higher-`gamma` region, product repositioning changes not merely a local profit number but the government coalition-blocking threshold from the fixed-position cutoff `1/15≈.06667` to about `.11964` at `gamma=.10`.

At the repaired witness, the national-welfare reversal is driven mainly by restored domestic producer rents with a smaller positive consumer-surplus contribution. The paper therefore has an organizational/welfare result rather than a pure firm-profit comparative static.

### 4.4 Institutional relevance

**PASS WITH QUALIFICATION.**

The intensive realized-interoperability margin is institutionally defensible in environments with multiple functions/options/interfaces and implementation/conformance testing. The scalar and functional forms remain reduced-form representations and must not be presented as literal standards-body engineering measures.

### 4.5 Alternative-formulation robustness

**PASS.**

The result survives one pre-specified nonlinear realization map that changes endogenous policy choices materially. This resolves the only prior Stage-7.5 blocker.

## 5. Maximum defensible contribution entering Stage 7.5A

The paper may proceed with the following candidate contribution statement:

> In a government standards-coalition game with endogenous interoperability depth, costly post-policy product repositioning can remain consequential after policy adjustment. In a selection-safe higher-redesign-cost region, allowing repositioning shifts the bilateral-union versus international-standardization national-welfare blocking threshold relative to the otherwise identical fixed-position policy game and can therefore change the stable standards partition. The mechanism also survives one pre-specified concave alternative mapping from standards depth to realized interoperability.

This statement is still subject to Stage 7.5A quantifier and wording certification.

## 6. Claims that remain prohibited

The project may not claim, absent new proof, that:

- the location equilibrium is globally unique for all parameters;
- the mechanism holds for arbitrary demand systems;
- the result holds for arbitrary monotone or concave realization functions;
- the result holds under arbitrary country asymmetry;
- lower redesign costs monotonically strengthen the result globally;
- the numerical thresholds are structural constants;
- the low-`gamma` region is selection-free;
- endogenous policy is generically necessary based solely on the B-EXO-HIST comparison;
- continuous standards depth or coalition stability is itself novel.

## 7. Stage 7.5A mandatory contract

Stage 7.5A must now:

1. rewrite every headline claim in explicit quantifier form;
2. distinguish proved baseline statements from finite numerical robustness evidence;
3. preserve the low-`gamma` multiplicity counterexample as a scope boundary;
4. audit all uniqueness/globality wording;
5. distinguish the canonical linear baseline from the nonlinear Stage-7R robustness specification;
6. certify benchmark labels and welfare language;
7. produce a claim-scope ledger with maximum defensible manuscript wording and prohibited stronger wording;
8. close the Formal Verification Gate.

Formal verification remains **APPLICABLE**. At minimum the proof-critical exact core should target:

- baseline B-FIX factorization and `v_FIX=1/15`;
- baseline IS welfare derivative and sufficient condition `v>1/18`;
- exact logical implications from strict welfare comparisons to coalition blocking/stability;
- exact algebraic threshold-ordering components that do not depend on numerically solved location continuations.

Numerical global-equilibrium claims, multiplicity search, and continuous location-policy correspondence remain outside any narrow Lean certificate unless explicitly formalized.

## 8. Canonical verdict

**GO.**

Routing: **STAGE 7.5A — GENERALITY / QUANTIFIER RED-TEAM + FORMAL VERIFICATION GATE.**

Full-paper investment is authorized. Theory freeze is **not** authorized yet. Stage 8 remains blocked until Stage 7.5A passes and the Formal Verification Gate is closed with `FORMAL VERIFICATION PASS` or a valid claim-specific `FORMALIZATION NOT APPLICABLE — REASON RECORDED` state. For this project, the current applicability record makes targeted formalization the expected route.