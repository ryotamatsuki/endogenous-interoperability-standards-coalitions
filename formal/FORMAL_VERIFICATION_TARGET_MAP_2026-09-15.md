# Formal Verification Target Map — Stage 7.5A

Date: 2026-09-15

Final applicability decision: **FORMALIZATION APPLICABLE**.

The project uses targeted Lean formalization. It does not attempt to encode the complete continuous economic game.

| Claim ID | Paper object | Proof-critical component | Lean target | Explicitly excluded component | Assurance gain |
|---|---|---|---|---|---|
| Q1 | exact B-FIX cutoff | rational factorization, denominator/polynomial signs, cutoff sign | `bFix_factorization`, `bFix_delta_pos_iff`, `bFix_delta_at_cutoff` | derivation of the exact welfare formulas from demand/pricing primitives | kernel-check exact `1/15` threshold on the audited interval |
| Q2 | IS upper-depth sufficient condition | cross-curvature derivative sign for `v>1/18`; negative `dW/dc`; sign composition | `isCrossDerivative_neg`, `isWelfareDerivative_neg`, `welfareDepthDerivative_pos` | proof that the symmetric-anchor continuation is the relevant global location continuation | kernel-check exact sign chain and sufficient-condition logic |
| Q8 | strict coalition blocking | all deviators strictly gain; a weak loss defeats a strict block | `pair_strict_block`, `no_strict_block_if_member_not_gain` | numerical welfare comparisons and full deviation correspondence | kernel-check logical mapping from certified inequalities to strict blocking |

## Deliberately non-formalized high-value objects

The following remain certified by independent Stage-4A / Stage-7R adversarial computation rather than Lean:

- affine-demand construction from the economic primitives and the full KKT demand correspondence;
- complete continuous product-location strategy domain;
- global whole-circle unilateral best responses;
- alternative-equilibrium / multiplicity search;
- numerical FULL location and policy equilibria;
- numerical root `v_FULL≈.1196400688`;
- stable-set computation using all partition-specific continuation values;
- Stage-7R nonlinear-`chi` robustness exercise;
- institutional interpretation of standards depth.

These exclusions are intentional. Encoding a numerical solver output as a Lean hypothesis would not formally certify the equilibrium search that produced it.

## Statement-fidelity rule

A Lean theorem in this project certifies only the encoded algebra, inequality, or blocking implication. Manuscript text must not say that Lean certifies the complete Nash correspondence, location-equilibrium uniqueness, policy equilibrium, FULL cutoff, or stable standards partition.
