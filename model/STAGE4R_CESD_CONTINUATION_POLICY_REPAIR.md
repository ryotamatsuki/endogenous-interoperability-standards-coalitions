# Stage 4R — C-ESD Continuation-Existence / Policy-Stage Repair

Date: 2026-09-04
Stage-11 trigger: off-path continuation failure under the historical policy action set
Historical freeze: `CESD-THEORY-FREEZE-2026-09-04-v1` (suspended)

## 1. Repair principle

The Stage-11 failure came from allowing every formal standards bloc, including a singleton, to choose a continuous depth variable. That interpretation mixed two distinct objects: *within-coalition harmonization depth* and *national standard specificity*.

Stage 4R removes that ambiguity. The continuous variable `s_C` is defined strictly as the depth of harmonization undertaken **within a standards coalition**. Consequently,

\[
\mathcal S_C(\rho)=
\begin{cases}
[0,\bar s], & |C|\ge 2,\\
\{0\}, & |C|=1.
\end{cases}
\]

This is an action-set correction, not a new economic channel.

## 2. Pairwise friction map

The Stage-3/4 friction map is unchanged:

\[
\tau_{ij}(\rho,s)=
\begin{cases}
\bar t-s_C, & i,j\in C,\\
\bar t+\dfrac{s_C+s_D}{2}, & i\in C,\ j\in D,\ C\ne D.
\end{cases}
\]

The repair changes only the feasible value of `s_C` for singleton blocs.

### IS

The grand coalition is non-singleton and chooses

\[
s_I\in[0,\bar s],
\qquad
\tau_{12}=\tau_{13}=\tau_{23}=\bar t-s_I.
\]

### SU_12

The two-country coalition chooses

\[
s_{12}\in[0,\bar s],
\]

while outsider 3 is a singleton and therefore has

\[
s_3\equiv 0.
\]

Thus

\[
\tau_{12}=\bar t-s_{12},
\qquad
\tau_{13}=\tau_{23}=\bar t+\frac{s_{12}}{2}.
\]

The intended within-bloc convergence / cross-bloc divergence mechanism is unchanged.

### SW

Every bloc is a singleton, so

\[
s_1=s_2=s_3\equiv0,
\qquad
\tau_{12}=\tau_{13}=\tau_{23}=\bar t.
\]

The SW regime remains distinct through the compatibility/network graph `G_SW=I`; `s=0` means zero *additional harmonization depth*, not zero formal incompatibility.

## 3. Why this repair is preferable to lowering s_bar

Stage 11 found that lowering `s_bar` to 0.20 could numerically avoid the historical off-path failure. Stage 4R does **not** adopt that repair.

The historical failure occurred only because the SU outsider was given an instrument `s_3` that has no within-coalition harmonization content. Removing that instrument follows directly from the interpretation of `s_C` and leaves the historical cap `s_bar=0.25` untouched.

Thus the repair is not selected by the desired welfare sign and does not narrow the canonical witness region merely to force equilibrium existence.

## 4. Repaired timing

\[
\rho
\rightarrow
\{s_C:|C|\ge2\}
\rightarrow
\Tau(\rho,s)
\rightarrow
x
\rightarrow
p
\rightarrow
W
\rightarrow
\text{coalition stability}.
\]

Only non-singleton standards coalitions have a continuous depth decision.

## 5. Continuation requirement

For every feasible depth after the repair, Stage 4R requires an actual downstream location-price Nash equilibrium.

The canonical verification therefore:

1. computes the conditional location candidate;
2. checks continuous unilateral deviations over the entire Salop circle;
3. enumerates all cyclic orders and circular-anchor branches on a dense depth grid to detect alternative regular stationary equilibria;
4. rejects a continuation if the selected candidate is not a whole-circle location Nash equilibrium;
5. solves the remaining scalar policy problem globally.

The policy stage never assigns a welfare value to a fixed-order candidate that fails the global location-best-response test.

## 6. Canonical witness after repair

The historical witness remains

\[
(\bar t,v,\gamma,\bar s)=(1,0.04,0.11,0.25).
\]

Because the historical equilibrium already had

\[
s_3^{SU}=0,
\qquad
s_i^{SW}=0,
\]

the equilibrium path is unchanged by the action-set repair.

The repaired global policy solutions remain

\[
s_I^*=0.25,
\qquad
s_{12}^*=0.25,
\qquad
s^{SW}=0.
\]

The FULL SU location equilibrium remains approximately

\[
x^{SU}=(0.084567,0.582100,0.833333).
\]

## 7. Headline result after repair

The repaired game preserves

\[
\Delta_M^{B-T}<0,
\qquad
\Delta_M^{B-X}<0,
\qquad
\Delta_M^{FULL}>0.
\]

At the canonical witness the values remain numerically the same, up to solver tolerance, as before Stage 11:

- `Delta_M^(B-T) ≈ -0.010167`;
- `Delta_M^(B-X) ≈ -0.000434`;
- `Delta_M^(FULL) ≈ +0.001571`.

Hence the core interaction-induced coalition-stability reversal survives the repair.

## 8. Theory-change classification

This is a **bounded action-set clarification** that requires theory re-freeze because the historical freeze stated that every standards bloc chose a depth. It does not alter:

- the IS/SU/SW partition set;
- the pairwise friction mapping;
- the compatibility/network graphs;
- firm product positioning;
- price competition;
- national welfare;
- coalition-stability logic;
- the equilibrium path at the canonical witness;
- the surviving novelty claim.

Affected stages after Stage 4R: Stage 7 welfare/generality refresh, Stage 8 re-freeze, Stage 9 reproducibility refresh, Stage 10 manuscript refresh, and repeated Stage 11 referee gate. Stage 6 novelty re-kill need not be repeated unless a later repair changes the economic mechanism.
