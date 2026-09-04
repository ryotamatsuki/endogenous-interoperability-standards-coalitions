# C-ESD Policy-Map Hardening Decisions

Date: 2026-09-04

These decisions resolve the D-036 conditional gate. They are authoritative together with `decisions/DECISION_LOG.md` until the next consolidation pass.

## D-037 — Freeze one policy scalar per formal standards bloc

Decision: **ACCEPTED**

For every bloc `C in rho`, use one standard coherence/specificity depth

`s_C in [0,s_bar]`, with `s_bar<t_bar`.

The realized standard-induced Hotelling/Salop friction is pairwise rather than represented by a single scalar under SU.

## D-038 — Freeze regime-neutral pairwise friction map

Decision: **ACCEPTED**

If `i,j` are in the same bloc `C`,

`tau_ij=t_bar-s_C`.

If they are in different blocs `C,D`,

`tau_ij=t_bar+(s_C+s_D)/2`.

The `1/2` cross coefficient is pinned down by the SU pure-redistribution normalization: one internal pair falls by one unit while two cross pairs each rise by one-half, preserving mean pairwise friction from the member-bloc depth margin when outsider specificity is held at zero.

No free regime-specific external-discrimination coefficient is allowed in the Stage-4 baseline.

## D-039 — Freeze bloc-Nash government policy rule

Decision: **ACCEPTED**

After formal partition `rho`, all standards blocs choose their depths simultaneously.

Bloc `C` maximizes

`Omega_C=sum_{i in C} W_i`.

Therefore:

- IS: one three-country bloc chooses `s_I`;
- SU_12: bloc `{1,2}` chooses `s_12` and singleton `{3}` chooses `s_3`;
- SW: each singleton government chooses its own `s_i`.

In the symmetric main model, members of a multi-country bloc have identical continuation welfare, so sum maximization is equivalent to representative-member welfare maximization and does not require transfers or bargaining weights.

## D-040 — Freeze network-depth separation

Decision: **ACCEPTED**

Formal partition `rho` determines the network compatibility graph as in the Stage-3 Salop diagnostic. The network coefficient `v` is held fixed with respect to `s_C` in the Stage-4 baseline.

Do not make network intensity another continuous function of government depth during Stage 4. That is a later robustness extension only if the baseline survives.

## D-041 — C-ESD conditional gate resolution

Decision: **GO -> GO TO STAGE 4 MINIMAL MODEL**

The single unresolved architecture question in D-036 is resolved.

Freeze Stage-4 timing as

`rho -> s*(rho) -> x*(rho,s*) -> p*(rho,s*,x*) -> W_i -> coalition stability`.

Required Stage-4 benchmarks:

- `B-EXO/B-X`: all depths fixed at zero, endogenous product locations;
- `B-T`: endogenous depths, product locations fixed at inherited anchors;
- `FULL`: endogenous depths and endogenous product locations.

Stage 4 must prove existence/feasibility/global best responses and determine whether FULL creates a government-welfare or coalition-stability result unavailable in B-T and B-X separately.

This GO does not assert that a stability reversal exists. If it does not, Stage 4 must return NO-GO rather than change the frozen policy map.

Do not add relative profit, private interoperability investment, endogenous network intensity, policy costs, lobbying, transfers, dynamics, topology choice or additional countries during Stage 4.
