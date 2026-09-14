# Project State

Last updated: 2026-09-15

## Canonical status

- Project: Endogenous Interoperability and Standards Coalitions — revival track
- Branch: `revival/stage00-coalition-repositioning`
- Canonical workflow: `ryotamatsuki/research-paper-workflow` v2.1
- Selected mechanism: **C1 — Realized Interoperability Depth**
- Stage 4A repeat: **GO — MATHEMATICAL ADVERSARIAL CERTIFICATION PASS**
- Stage 6: **GO**
- Stage 7: **GO**
- Stage 7.5 first pass: **CONDITIONAL GO**
- Stage 7R: **GO — ALTERNATIVE-REALIZATION ROBUSTNESS PASS**
- Stage 7.5 repeat: **GO — FULL-PAPER INVESTMENT AUTHORIZED**
- Next stage: **Stage 7.5A — Generality / Quantifier Red-Team + Formal Verification Gate**
- Theory freeze: **NONE**
- Submission authorization: **NO**
- Formal verification: **APPLICABLE; TARGETED IMPLEMENTATION REQUIRED AT STAGE 7.5A**

## Frozen baseline

For `i!=j`,

`K_ij=c0+lambda*phi(x_i-x_j)/Tau_ij(rho,s)-v*M_ij(rho,s)`.

The canonical baseline uses linear realized interoperability `chi(s)=s/s_bar`. The Stage-7R concave map is robustness evidence only.

## Permanent scope boundary

At low redesign cost `gamma=.03`, the FULL-SU location game has multiple global-BR pure Nash equilibria with different welfare rankings. The low-gamma selection-free stability claim is therefore permanently revoked. Regression artifact:

`verification/stage04a_independent_multiplicity_red_team.py`.

## Certified higher-gamma baseline scope

Baseline repaired witness: `(v,gamma)=(.11,.10)`.

Approximate welfare:

- IS: `.1432822599`;
- FULL SU member: `.1433644618`;
- FULL SU outsider: `.1419734070`;
- FULL SW: `.1425185185`.

At `gamma=.10`:

- `v_FIX=1/15=.0666666667` exactly;
- `v_EXO-HIST≈.0993400329`;
- `v_FULL≈.1196400688`.

Repeat Stage 4A independently attacked multiplicity/global deviations on the declared higher-gamma stress domain. It did not prove uniqueness for all parameters.

## Surviving contribution

> In a government standards-coalition game with endogenous interoperability depth, costly post-policy product repositioning can remain consequential after policy adjustment. In a selection-safe higher-redesign-cost region, allowing repositioning shifts the bilateral-union versus international-standardization national-welfare blocking threshold relative to the otherwise identical fixed-position policy game and can therefore change the stable standards partition.

Generic compatibility-induced differentiation, continuous standards depth, standards breadth/depth, coalition-induced downstream choice, and regional-versus-multilateral stability remain killed as novelty claims.

## Stage 7R robustness

Alternative map:

`chi_alt(s)=2(s/s_bar)-(s/s_bar)^2`.

At `gamma=.10`, after re-optimizing policy:

- `v_FIX_alt≈.05133198`;
- `v_FULL_alt≈.10666955`.

At `(v,gamma)=(.08,.10)`:

- B-FIX: `W_M(SU)-W(IS)≈-.000205416`;
- FULL: `W_M(SU)-W(IS)≈+.000195579`.

Twenty material SU policy histories under the alternative map were attacked with dispersed multi-starts plus whole-circle unilateral deviations; one global-BR pure SU Nash was retained at each attacked history.

This closes the sole first-pass Stage-7.5 blocker. It does not establish robustness for arbitrary realization functions.

## Repeat Stage 7.5 authority

- review: `reviews/STAGE_075_REPEAT_REVIVAL_FULL_THEORY_FREEZE_DECISION_2026-09-15.md`
- decision: `decisions/STAGE075_REPEAT_REVIVAL_DECISIONS_2026-09-15.md`

Verdict: **GO — FULL-PAPER INVESTMENT AUTHORIZED.**

## Stage 7.5A contract

Stage 7.5A must:

1. state headline claims with explicit quantifiers and domains;
2. separate exact proof, numerical certification, finite robustness evidence, and conjecture;
3. preserve the low-gamma multiplicity boundary;
4. audit `unique`, `global`, `generic`, `region`, and robustness wording;
5. separate baseline theorem scope from Stage-7R robustness evidence;
6. produce a claim-scope ledger and maximum defensible manuscript wording;
7. close the Formal Verification Gate.

Targeted Lean 4/mathlib formalization is expected for the exact proof-critical core, including baseline `v_FIX=1/15`, the exact IS welfare derivative / sufficient condition `v>1/18`, and welfare-to-blocking logic. Lean must not be described as certifying the numerical global location-equilibrium correspondence unless that object is explicitly formalized.

## Current routing

**NEXT: STAGE 7.5A — GENERALITY / QUANTIFIER RED-TEAM + FORMAL VERIFICATION GATE.**

Stage 8 theory freeze and submission remain blocked until Stage 7.5A passes.