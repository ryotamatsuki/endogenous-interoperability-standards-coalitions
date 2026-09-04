# Stage 8R — Theory Re-Freeze: C-ESD

Date: 2026-09-04
Canonical workflow: `ryotamatsuki/research-paper-workflow` v1.1
Workflow SHA: `488e5ab06c207909296a7564eaf9066f7f94319c`

## Executive verdict

**THEORY FROZEN — GO TO STAGE 9R REPRODUCIBILITY REFRESH.**

New freeze ID:

`CESD-THEORY-FREEZE-2026-09-04-v2`

The historical v1 freeze is retained for provenance but is superseded for submission purposes.

## What changed from v1

Only the Stage-4R action-set clarification and its continuation-validity consequences enter v2:

- harmonization depth is defined strictly as additional within-coalition harmonization;
- non-singleton blocs choose `s_C in [0,s_bar]`;
- singleton blocs have `s_C=0`;
- policy-stage welfare may be evaluated only through actual downstream whole-circle location Nash continuations.

No friction formula, network graph, timing, price game, redesign cost, welfare objective, coalition-stability rule, canonical parameter vector, or headline equilibrium-path value changes.

## Canonical repaired regime map

- IS: grand coalition chooses `s_I in [0,s_bar]`;
- `SU_12`: coalition `{1,2}` chooses `s_12 in [0,s_bar]`; outsider singleton has no depth instrument;
- SW: all blocs are singletons and all depths equal zero.

Under `SU_12`:

`tau_12=t_bar-s_12`,

`tau_13=tau_23=t_bar+s_12/2`.

The within-bloc convergence / cross-bloc divergence mechanism is unchanged.

## Headline result retained

At `(t_bar,v,gamma,s_bar)=(1,0.04,0.11,0.25)`:

- `Delta_M^(B-T)≈-0.010167`;
- `Delta_M^(B-X)≈-0.000434`;
- `Delta_M^(FULL)≈+0.001571`.

B-T and B-X select IS; FULL makes the three two-country SUs stable and IS pair-blockable.

## Proof-status discipline

Analytic / `PROVED`:

- weighted-Laplacian demand system;
- unique regular interior price equilibrium;
- fixed-order location characterization;
- exact national-welfare decomposition;
- exact global-welfare identity.

`CONDITIONAL`:

- SU strategic re-differentiation on the regular branch;
- FULL-only coalition-stability reversal;
- general convex-cost mechanism interpretation.

`NUMERICALLY SUPPORTED ONLY`:

- repaired continuation validity over the full feasible policy-depth domain at canonical primitives;
- witness global-welfare ranking;
- witness private/social re-differentiation wedge.

No global analytic parameter-space theorem is claimed.

## Welfare package retained

`Delta_M=Delta Pi_M+Delta CS/3`.

At the witness:

- `Delta CS/3≈-0.0325785`;
- `Delta Pi_M≈+0.0341498`;
- `Delta_M≈+0.0015713`.

World welfare, reported net of common baseline utility `A`:

- `GW_IS≈-0.0225000`;
- `GW_SU≈-0.0586685`;
- `GW_SW≈-0.0700000`.

Private/social distances:

`D_private≈0.497533 > D_social≈0.431427 > 1/3`.

## Closest-paper / contribution boundary

The Ruiz (2004) + Gandal–Shy (2001) synthesis remains the strongest novelty attack. The paper may claim only the result-level interaction: policy depth and product positioning separately leave IS stable, while their interaction reverses the coalition ranking.

No ingredient-level novelty claim is revived.

## Explicit exclusions

No relative profit, private interoperability investment, endogenous network intensity, policy cost, transfers, lobbying, dynamics, topology choice, additional countries, heterogeneous national CS incidence, alternative spatial geometry, or empirical estimation may enter without theory-change control.

## Freeze files

- `theory/THEORY_FREEZE_CESD_2026-09-04_v2.md`
- `theory/PROPOSITION_REGISTER_CESD_2026-09-04_v2.md`
- `theory/PARAMETER_WELFARE_VERIFICATION_REGISTER_CESD_2026-09-04_v2.md`

## Next-stage contract

Stage 9R must update repository/reproducibility infrastructure so generated outputs, freeze-consistency tests, documentation, and manuscript build point to v2 rather than historical v1. It may not alter theory.

Stage 10R then refreshes manuscript wording and equations to the repaired action-set semantics. Stage 11R must be rerun before journal positioning.
