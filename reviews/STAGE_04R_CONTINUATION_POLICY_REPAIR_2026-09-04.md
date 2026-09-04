# Stage 4R — Continuation-Existence / Policy-Stage Repair: C-ESD

Date: 2026-09-04
Trigger: Stage 11 `REOPEN EARLIER STAGE`
Stage-11 report: `reviews/STAGE_11_REFEREE_GATE_CESD_2026-09-04.md`
Historical theory freeze: `CESD-THEORY-FREEZE-2026-09-04-v1` (suspended)

## 1. Executive verdict

**REPAIR PASSES — CORE MECHANISM PRESERVED.**

The Stage-11 fatal off-path SPNE gap is repaired by correcting the policy action set rather than by tuning the canonical policy cap or adding a new cost/instrument.

The continuous policy variable `s_C` is now defined strictly as **within-coalition harmonization depth**. Therefore only non-singleton standards coalitions may choose positive depth; singleton blocs have the degenerate action `{0}`.

This removes the historically problematic SU-outsider depth deviations because a singleton outsider has no internal harmonization margin to deepen. It also removes meaningless positive-depth choices in `SW`, where all blocs are singletons.

The pairwise friction map, network graph, product-location game, price game, welfare definition, coalition-stability rule, and canonical equilibrium path are unchanged.

At the canonical witness `(t_bar,v,gamma,s_bar)=(1,0.04,0.11,0.25)` the repaired game retains

`Delta_M^(B-T)<0`, `Delta_M^(B-X)<0`, and `Delta_M^(FULL)>0`,

with the same equilibrium policies and product locations as the historical witness up to numerical tolerance.

Route after Stage 4R: **Stage 7R — Welfare / Generality Refresh**, followed by re-freeze and downstream refreshes. Stage 12 remains blocked until repeated Stage 11 passes.

---

## 2. Stage-11 failure being repaired

The historical policy game allowed every formal bloc to choose `s_C in [0,s_bar]`, including singleton blocs.

Under `SU_12`, that gave the outsider a continuous `s_3` choice. Stage 11 showed that at the historical primitives with `(s_12,s_3)=(0.25,0.20)`, the fixed-order continuation used by Stage 4 is not a whole-circle location Nash equilibrium. The outsider-depth jump problem begins around `s_3≈0.143` when `s_12=0.25`.

Because those off-path values were used inside policy best responses, the historical continuation-value map did not establish a pure-strategy SPNE over the full policy action set.

The on-path historical SU witness itself remained a true whole-circle location Nash equilibrium.

---

## 3. Repair: harmonization depth exists only inside coalitions

The repaired feasible action set is

\[
\mathcal S_C(\rho)=
\begin{cases}
[0,\bar s], & |C|\ge2,\\
\{0\}, & |C|=1.
\end{cases}
\]

Economic interpretation: `s_C` measures the extent to which members of a common standards coalition harmonize their interface/standard beyond the baseline formal recognition relation. A singleton has no partner with whom to harmonize and therefore has no such continuous margin.

This interpretation is more precise than the historical “coherence / specificity” wording, which inadvertently allowed a singleton to use the harmonization variable as a national differentiation instrument.

### IS

The grand coalition chooses

\[
s_I\in[0,\bar s].
\]

All bilateral frictions are

\[
\tau_{ij}=\bar t-s_I.
\]

### SU_12

Only the member coalition chooses

\[
s_{12}\in[0,\bar s],
\]

while outsider depth is fixed by definition at

\[
s_3=0.
\]

Hence

\[
\tau_{12}=\bar t-s_{12},
\qquad
\tau_{13}=\tau_{23}=\bar t+\frac{s_{12}}2.
\]

The intended mechanism is preserved exactly: deeper regional harmonization reduces member-member standard differentiation and raises relative member-outsider separation.

### SW

All blocs are singletons, so

\[
s_1=s_2=s_3=0.
\]

Pairwise friction equals the baseline `t_bar`. SW remains distinct through the formal compatibility/network graph `G_SW=I`.

This also clarifies that `s=0` means **zero additional harmonization depth conditional on the formal regime**, not zero compatibility or zero institutional differentiation.

---

## 4. Why the repair is not parameter tuning

Stage 11 found a preliminary numerical workaround using `s_bar=0.20`. Stage 4R rejects that as the primary repair.

The canonical cap remains

\[
\bar s=0.25.
\]

The repair instead removes an instrument that is not meaningful under the clarified economic definition of `s_C`.

This matters for identification of the mechanism:

- no direct policy cost is added;
- no new convexity is added;
- no parameter is chosen because it produces the preferred sign;
- the equilibrium-path policies already satisfied `s_3^{SU}=0` and `s_i^{SW}=0` historically;
- the headline equilibrium values therefore do not move.

---

## 5. Downstream continuation solver

The new canonical Stage-4R verification is

`verification/stage04r_cesd_continuation_repair.py`.

For every feasible policy value used in the repaired policy stage, it requires a true downstream continuation.

The audit has four layers.

### 5.1 Conditional candidate

For a fixed cyclic order, the existing linear FOC system generates the conditional product-location candidate.

### 5.2 Continuous whole-circle best responses

For each firm, the deviation problem is solved over the entire circle. The circle is split at rival locations and redesign-cost kink points, and each interval is optimized continuously rather than on a coarse location grid.

### 5.3 All-order / anchor-branch enumeration

On a dense policy-depth grid the audit enumerates all six cyclic orders and circular anchor branches and identifies all regular interior stationary candidates. At the canonical parameter vector, every audited feasible IS and SU depth has exactly one candidate satisfying the whole-circle Nash test. SW also has one regular whole-circle location equilibrium.

### 5.4 Policy-depth x deviation-location global audit

As an independent check, differential-evolution searches jointly over

\[
(s,z)\in[0,\bar s]\times[0,1]
\]

for each firm, maximizing the unilateral deviation gain

\[
\pi_i(z;x_{-i}^*(s),s)-\pi_i(x_i^*(s);x_{-i}^*(s),s).
\]

For both IS and SU, the maximum gain for every firm is zero up to numerical precision at the canonical parameter vector. Thus the selected continuation does not cease to be a whole-circle location Nash equilibrium anywhere on the repaired feasible depth interval.

---

## 6. Repaired policy stage

The policy game is now globally one-dimensional in each regime with a non-singleton coalition.

### IS

The grand coalition maximizes total member welfare over `s_I in [0,s_bar]`.

At the canonical witness the global optimum is

\[
s_I^*=0.25.
\]

This is consistent with the exact symmetric expression under IS: lower effective friction raises the grand coalition objective over the relevant domain.

### SU

The two-country union globally maximizes

\[
W_1^{SU}(s)+W_2^{SU}(s)
\]

over `s in [0,s_bar]`. The outsider has no continuous depth action.

The global optimum is

\[
s_{12}^*=0.25.
\]

The full policy interval is continuation-regular under the canonical witness.

### SW

There is no continuous depth action because all blocs are singletons:

\[
s^{SW}=0.
\]

The country-level coalition decision remains at the earlier regime-selection stage.

---

## 7. Repaired canonical witness

The canonical parameter vector remains

\[
(\bar t,v,\gamma,\bar s)=(1,0.04,0.11,0.25).
\]

The repaired FULL policies are unchanged:

\[
s_I^*=0.25,
\qquad
s_{12}^*=0.25,
\qquad
s^{SW}=0.
\]

Under `SU_12`, the FULL location equilibrium remains approximately

\[
x^{SU}=(0.084567,0.582100,0.833333).
\]

Thus member firms still move apart relative to their inherited anchors while the outsider remains at its anchor.

---

## 8. Mandatory nested benchmarks after repair

### B-T

Government harmonization depth is endogenous under the repaired action set while product locations are fixed at inherited anchors.

The member comparison remains approximately

\[
\Delta_M^{B-T}=-0.010167<0.
\]

### B-X

All non-singleton harmonization depths are fixed at zero while product locations are endogenous.

The member comparison remains approximately

\[
\Delta_M^{B-X}=-0.000434<0.
\]

### FULL

Both non-singleton coalition depth and product positioning are endogenous.

The member comparison remains approximately

\[
\Delta_M^{FULL}=+0.001571>0.
\]

Therefore

\[
\boxed{
\Delta_M^{B-T}<0,
\quad
\Delta_M^{B-X}<0,
\quad
\Delta_M^{FULL}>0
}
\]

survives the continuation repair.

---

## 9. Coalition stability after repair

The repaired equilibrium values retain the historical ranking at the canonical witness:

\[
W_M^{SU}>W^{IS}>W_O^{SU},
\qquad
W_M^{SU}>W^{SW}.
\]

Hence:

- in B-T and B-X, prospective SU members do not jointly block IS;
- in FULL, each prospective pair strictly prefers SU to IS;
- an SU is not unanimously blocked by IS because the members prefer staying in SU;
- SU members do not prefer dissolution to SW.

By symmetry, the repaired FULL stability set remains

\[
\mathcal S^{FULL}=\{SU_{12},SU_{13},SU_{23}\},
\]

whereas the two nested benchmarks continue to select IS.

---

## 10. Existence, uniqueness and selection status

At the canonical witness, Stage 4R now verifies:

1. regular interior price equilibrium for every feasible repaired policy depth;
2. a whole-circle location Nash continuation for every feasible repaired IS and SU depth;
3. exactly one regular interior whole-circle location equilibrium on the audited dense policy grid across all cyclic orders and circular anchor branches;
4. no profitable unilateral location deviation in joint global policy-depth/deviation-location optimization;
5. a global scalar policy optimum in IS and SU;
6. no continuous policy decision in SW.

This is sufficient to repair the specific pure-strategy SPNE gap identified by Stage 11 at the canonical constructive witness.

The project still does not claim a global analytic classification of continuation existence for every parameter vector. The main result remains a constructive regular-region result.

---

## 11. What changed and what did not

### Changed

- feasible action set for singleton standards blocs;
- interpretation of `s_C` is narrowed to within-coalition harmonization depth;
- policy verification now requires actual downstream whole-circle Nash continuation at every feasible policy value used by the policy stage;
- policy optimization is global on the repaired action set.

### Unchanged

- IS/SU/SW formal regimes;
- pairwise friction formula;
- coefficient `1/2`;
- network graph by regime;
- Salop geometry;
- redesign cost;
- pricing game;
- national welfare;
- strict-blocking coalition stability;
- canonical parameter vector;
- canonical equilibrium path;
- headline interaction result;
- Stage-6 novelty position.

---

## 12. Theory-change implications

Because the historical Stage-8 freeze explicitly said that every standards bloc chooses a continuous depth, the historical freeze must be refreshed.

This is a bounded action-set correction rather than a new mechanism. The affected downstream stages are:

1. Stage 7R — Welfare / Generality Refresh;
2. Stage 8R — Theory Re-Freeze;
3. Stage 9R — Reproducibility Refresh;
4. Stage 10R — Manuscript Refresh;
5. Stage 11R — repeated Referee Attack Gate.

Stage 6 novelty re-kill need not be repeated unless a later stage changes the economic mechanism or surviving contribution.

---

## 13. Remaining Stage-11 attacks

The continuation/SPNE attack is repaired, but the following attacks remain for later stages/referee rerun:

- Ruiz (2004) + Gandal–Shy (2001) synthesis risk;
- sensitivity/claim discipline around the `1/2` cross-bloc coefficient;
- binary formal network graph versus continuous additional harmonization depth must be explained clearly;
- symmetric `CS/3` incidence remains an external-validity limitation;
- institutional evidence validates policy-controlled interoperability, not the exact cross-bloc derivative or observed re-differentiation;
- welfare levels should be described net of the common baseline utility `A`;
- IJIO fit remains unresolved until repeated Stage 11.

None of these remaining attacks requires undoing the Stage-4R repair.

---

## 14. Final Stage-4R verdict

**REPAIR PASSES — GO TO STAGE 7R WELFARE / GENERALITY REFRESH.**

The fatal Stage-11 off-path continuation problem arose from giving singleton blocs a harmonization-depth instrument. Correcting the action set removes the invalid subgames, restores a coherent pure-strategy continuation map on the canonical policy domain, and leaves the core C-ESD interaction result unchanged.
