# Repeat Stage 4A Theorem Certificates — Revival C1

Date: 2026-09-15

Status: **INDEPENDENT ADVERSARIAL CERTIFICATION PASS FOR REPAIRED SCOPE**

## C1-P1 — Affine-demand / Bertrand continuation

Exact scope: repaired threshold domain inherited from Stage 4.

State: **PASS**.

Evidence: independent reconstruction in `verification/stage04a_repeat_high_gamma_red_team.py` plus prior Stage-4A regularity attack. No new price-continuation contradiction found.

Limitation: no claim beyond the stated positive regular domain.

## C1-P2 — Repaired SU location continuation

Exact claim: at the repaired witness `(v,gamma)=(.11,.10)` and equilibrium SU depth `(.25,.25)`, the full-circle location game has one pure-strategy Nash equilibrium retained by the independent adversarial protocol, approximately

`(.14246245,.52420422,.83333333)`.

State: **PASS FOR REPAIRED COMPUTATIONAL SCOPE**.

Candidate-deviation audit: PASS by whole-circle unilateral search.

Alternative-equilibrium audit: PASS in the declared high-gamma stress protocol; no alternative pure Nash retained at the witness, across 15 full-depth stress points, or across 81 material SU policy histories.

Indifference audit: not triggered by zero output/zero profit; all headline prices and quantities are positive.

Selection/refinement: no auxiliary selection rule is used.

Permanent exclusion: low-gamma uniqueness is false and remains revoked.

## C1-P3 — IS upper-depth sufficient condition

Exact claim:

`v>1/18` is sufficient for IS welfare to increase throughout the allowed depth interval on the certified symmetric-anchor continuation, hence `s_I=s_bar`.

State: **PASS**.

Proof type: exact symbolic sign result inherited from Stage 1/4 and unaffected by the multiplicity repair.

## C1-P4 — Repositioning-induced blocking/stability difference

Exact repaired claim: at `(v,gamma)=(.11,.10)`, under the frozen strict-blocking correspondence and each partition's repaired continuation,

- B-FIX retains IS against SU pair blocking;
- FULL has the three bilateral SUs as stable partitions.

State: **PASS**.

Evidence:

- exact B-FIX threshold `v_FIX=1/15`;
- independently reconstructed repaired FULL continuation;
- strict welfare inequalities `W_M^SU>W^IS` and `W_M^SU>W^SW`;
- outsider welfare below IS, preventing grand-coalition strict block;
- symmetry plus strict blocking prevents cross-SU relabeling ties from blocking.

Limitation: symmetric three-country model and repaired higher-gamma continuation class.

## C1-P5 — Repaired threshold ordering

At `gamma=.10`:

- `v_FIX=1/15=.0666666667`;
- `v_EXO-HIST≈.0993400329`;
- `v_FULL≈.1196400688`.

State: **PASS FOR REPAIRED SCOPE**.

The conceptual contribution should use B-FIX versus FULL. B-EXO-HIST is auxiliary and must not be used to claim generic necessity of policy endogeneity.

## C1-P6 — Global uniqueness over all gamma

State: **FAIL / NOT CLAIMED**.

Reason: the permanent low-gamma crossing equilibrium is a valid counterexample.

## Formal-verification applicability

State: **FORMALIZATION APPLICABLE**.

Future Stage-7.5A targets:

1. `v_FIX=1/15` exact factorization;
2. IS derivative and `v>1/18` sufficient condition;
3. strict-welfare-inequality to blocking/stability logic;
4. exact threshold-ordering algebra separable from numerical location continuation;
5. any later analytic high-gamma uniqueness condition.

No formal-verification PASS is claimed at Stage 4A repeat.

## Final certificate state

All headline repaired claims: **PASS WITH EXPLICIT SCOPE**.

Superseded low-gamma selection-free claims: **FAIL / PERMANENTLY REVOKED**.
