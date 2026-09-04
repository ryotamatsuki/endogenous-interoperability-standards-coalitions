# Stage 4R Decisions — C-ESD

Date: 2026-09-04
Trigger: Stage 11 off-path continuation/SPNE failure

## D-073 — Singleton blocs have no harmonization-depth instrument

`s_C` is defined strictly as within-coalition harmonization depth.

Feasible action set:

`S_C=[0,s_bar]` for `|C|>=2`, and `S_C={0}` for `|C|=1`.

This replaces the historical interpretation under which singleton blocs could choose positive depth.

## D-074 — Pairwise friction technology is unchanged

The historical mapping remains:

- same bloc: `tau_ij=t_bar-s_C`;
- different blocs: `tau_ij=t_bar+(s_C+s_D)/2`.

Under `SU_12`, singleton outsider depth is zero, so

`tau_12=t_bar-s_12`,

`tau_13=tau_23=t_bar+s_12/2`.

Under `SW`, all depths are zero and pairwise friction equals `t_bar`.

## D-075 — Do not repair by tuning s_bar

The historical cap `s_bar=0.25` is retained at the canonical witness. The preliminary Stage-11 `s_bar=0.20` route is rejected as the primary repair because the off-path failure arose from an economically misclassified singleton instrument, not from the equilibrium-path union depth itself.

## D-076 — Policy continuation values must use actual downstream Nash equilibria

No policy payoff may be evaluated from a fixed-order location stationary point unless that point passes continuous whole-circle unilateral best-response checks.

The Stage-4R verification additionally enumerates cyclic orders / anchor branches on a dense feasible-depth grid and audits the entire feasible policy-depth x unilateral-location space by global numerical optimization.

## D-077 — Repaired policy stage is globally one-dimensional

- IS: grand coalition globally chooses one scalar `s_I in [0,s_bar]`;
- SU: the two-country union globally chooses one scalar `s_12 in [0,s_bar]`; outsider singleton has no continuous depth action;
- SW: no continuous depth action because all blocs are singletons.

This removes the invalid coordinate policy game involving an SU outsider and eliminates the Stage-11 off-path subgames.

## D-078 — Canonical equilibrium path is unchanged

At `(t_bar,v,gamma,s_bar)=(1,0.04,0.11,0.25)` the repaired policy solution remains

- `s_I=0.25`;
- `s_12=0.25`, outsider depth `0`;
- `s_SW=0`.

The FULL SU product-location equilibrium remains approximately `(0.084567,0.582100,0.833333)`.

## D-079 — Headline interaction survives

The repaired game preserves

`Delta_M^(B-T)<0`,

`Delta_M^(B-X)<0`,

`Delta_M^(FULL)>0`.

Canonical values remain approximately `-0.010167`, `-0.000434`, and `+0.001571`, respectively.

## D-080 — Theory status and rerouting

The action-set correction is bounded but substantive enough to suspend the historical Stage-8 freeze until refreshed. It does not change the core mechanism or surviving novelty claim.

After Stage 4R passes, rerun/refresh:

1. Stage 7 — Welfare / Generality;
2. Stage 8 — Theory Freeze;
3. Stage 9 — Reproducibility;
4. Stage 10 — Paper Construction;
5. Stage 11 — Referee Gate.

Stage 6 novelty re-kill is not required unless the economic mechanism changes.
