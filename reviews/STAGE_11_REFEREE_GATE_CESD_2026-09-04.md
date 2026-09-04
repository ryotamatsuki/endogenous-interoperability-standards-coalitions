# Stage 11 — Robustness / Referee Attack Gate: C-ESD

Date: 2026-09-04
Canonical workflow: `ryotamatsuki/research-paper-workflow` v1.1
Workflow SHA: `488e5ab06c207909296a7564eaf9066f7f94319c`
Stage-10 manuscript SHA under attack: `bcad75cdc1e87c54cd2ecfd73559a1e6c96d4c68`
Theory freeze under attack: `CESD-THEORY-FREEZE-2026-09-04-v1`

## 1. Executive verdict

**REOPEN EARLIER STAGE — STAGE 4R CONTINUATION-EXISTENCE / POLICY-STAGE REPAIR.**

The core C-ESD mechanism is **not killed** by the hostile review. The canonical on-path SU witness survives a stronger continuous whole-circle unilateral-location audit, the welfare identities remain correct, and the Ruiz (2004) + Gandal–Shy (2001) synthesis attack still does not directly absorb the FULL-only coalition-ranking reversal.

However, the current manuscript claims subgame-perfect Nash equilibrium for the policy-location-price game while the Stage-4 policy routine evaluates some off-path standards-depth deviations using a fixed-order location candidate that is **not** a global location Nash equilibrium. At the canonical witness primitives with `s_12=0.25`, outsider-depth deviations around and above `s_3≈0.143` trigger profitable order-changing location jumps. At the explicit off-path profile `(s_12,s_3)=(0.25,0.20)`, the fixed-order continuation fails the whole-circle best-response test; an all-cyclic-order enumeration of interior stationary candidates finds no regular pure location Nash equilibrium.

Therefore the current continuation-value map used at the policy stage is not established on the full policy action set. The paper cannot presently claim a pure-strategy SPNE of the full sequential game. This is a mathematical validity issue, not a presentational detail.

A bounded repair appears viable. A Stage-11 diagnostic with the same `v=0.04` and `gamma=0.11` but a smaller policy cap `s_bar=0.20` preserves the headline signs:

- `Delta_M^(B-T)≈-0.008984 < 0`;
- `Delta_M^(B-X)≈-0.000434 < 0`;
- `Delta_M^(FULL)≈+0.001049 > 0`.

A dense 21×21 audit of the SU policy square `[0,0.20]^2` found no whole-circle continuation failure on the selected interior branch. This is evidence for a repair route, **not** a substitute for the Stage-4R proof/verification required below.

Submission preparation and Stage 12 journal positioning are blocked until the continuation-existence gap is repaired and the affected stages are rerun.

---

## 2. Referee A — Novelty and mechanism

### A1. Classic-result / Ruiz + Gandal–Shy synthesis attack

**Attack:** The paper is just Ruiz (2004) plus Gandal–Shy (2001): government standards policy, then endogenous product characteristics, embedded in a three-country standards-union model.

**Severity:** MAJOR BUT FIXABLE.

**Evidence:**

- Gandal & Shy (2001) already contain three countries, standardization unions, network effects, national welfare and government incentives to form an SU.
- Ruiz (2004) already lets governments choose standards recognition before firms choose product characteristics and prices, and explicitly studies excessive endogenous differentiation.
- Klimenko (2009) already contains continuous government compatibility policy, network externalities and international policy coordination.

**Can the paper answer now?** Yes, narrowly.

**Current answer:** The paper does not claim ingredient novelty. The surviving result is the nested interaction statement: B-T and B-X each leave IS preferred while FULL reverses the member ranking and stabilizes SU. Ruiz does not contain the coalition game; Gandal–Shy does not contain the post-policy endogenous product-positioning margin; Klimenko does not contain the IS/SU/SW stability reversal through repositioning.

**Required fix:** Keep all novelty language result-level. In the introduction and literature section, state explicitly that the contribution is the *sign reversal relative to both nested benchmarks*, not the timing, continuous compatibility, network effects, endogenous differentiation, or SU stability separately.

**Does the fix reopen theory?** NO.

**Resolved?** YES, subject to mathematical repair of the result itself.

### A2. No-new-mechanism attack

**Attack:** The model merely combines two known margins and reports a different number.

**Severity:** MINOR / RESOLVED.

**Evidence:** The mandatory B-T and B-X benchmarks use the same underlying market structure and each fails to generate the reversal. The FULL sign change isolates a strategic interaction that neither margin generates alone.

**Required fix:** Retain B-T and B-X in the main text and do not demote them to an appendix.

**Does the fix reopen theory?** NO.

### A3. Result-built-into-policy-map attack

**Attack:** The rule `tau_12=t_bar-s_12` and `tau_13=tau_23=t_bar+(s_12+s_3)/2` mechanically creates an SU advantage and therefore builds the result into the primitives.

**Severity:** MAJOR BUT FIXABLE.

**Evidence:** The B-T benchmark uses the same policy map but still gives `Delta_M^(B-T)<0`; therefore the map alone is not sufficient for the reversal. The exact coefficient `1/2` is already classified as a normalization rather than a structural claim. Nevertheless, no manuscript robustness currently varies the cross-bloc coefficient.

**Required fix after Stage-4R:** either (i) provide a bounded sensitivity audit around the `1/2` coefficient, or (ii) state the result explicitly conditional on the within-bloc/cross-bloc asymmetry and avoid claiming coefficient generality.

**Does the fix reopen theory?** Sensitivity analysis around a frozen normalization requires controlled robustness work; changing the baseline mapping requires theory change.

**Resolved?** PARTLY.

### A4. Binary network graph versus continuous depth

**Attack:** At `s_C=0`, formal SU membership still changes the network graph even though pairwise standard frictions revert to the baseline. The model therefore mixes a binary compatibility relation with a continuous depth margin.

**Severity:** MAJOR BUT FIXABLE conceptually.

**Evidence:** `G_rho` is fixed by regime while `s_C` changes `Tau`; the network coefficient does not vary with depth.

**Current response:** This can be coherent if regime membership establishes a basic compatibility/recognition relation and `s_C` measures additional harmonization depth conditional on that relation.

**Required fix:** Say this explicitly in the model and institutional discussion. Do not describe `s=0` as “zero interoperability.”

**Does the fix reopen theory?** NO if interpretive only. YES if network intensity is made continuous in `s`.

---

## 3. Referee B — Assumptions and mathematics

### B1. On-path whole-circle location equilibrium

**Attack:** The reported SU location profile may only solve the fixed-order FOCs.

**Severity:** FATAL if true; **RESOLVED for the canonical on-path witness**.

**Evidence:** Stage 11 replaces the Stage-4 grid-only witness check with continuous one-dimensional best-response maximization on every order/kink interval. At `(t_bar,v,gamma,s_bar)=(1,0.04,0.11,0.25)` and `(s_12,s_3)=(0.25,0)`, all three continuous whole-circle deviation gaps are numerically zero to machine precision. Thus the canonical on-path SU location profile is a genuine global unilateral location best response.

**Required fix:** Preserve the stronger continuous check in the repaired verification pipeline.

**Does the fix reopen theory?** NO.

### B2. Off-path continuation / SPNE attack — central failure

**Attack:** A policy-stage Nash equilibrium requires well-defined continuation equilibria after every unilateral standards-depth deviation. The current `su_policy` routine computes welfare from `loc_nash`, which is a fixed-order stationary solution, but does not require it to pass the whole-circle global-best-response test before using that welfare in policy best responses.

**Severity:** **FATAL TO THE CURRENT DRAFT.**

**Evidence:**

1. `verification/stage04_cesd_minimal.py::su_policy` calls `welfare`, and `welfare` calls the fixed-order `loc_nash` candidate.
2. Whole-circle checking is applied only after the selected witness is obtained; it is not part of the continuation-value function used for every policy deviation.
3. Stage-11 continuous audit finds that with `(s_12,s_3)=(0.25,0.20)` the fixed-order candidate has a profitable order-changing deviation.
4. Enumerating all interior stationary candidates across all six cyclic orders and circular-anchor branches finds no regular pure location Nash equilibrium at that off-path profile.
5. The outsider-jump problem begins at approximately `s_3≈0.143` when `s_12=0.25`.

**Can the paper answer now?** NO.

**Why this matters:** The manuscript states that the solution concept is subgame-perfect Nash equilibrium. An on-path location equilibrium is not sufficient; continuation strategies must be sequentially rational after off-path policy choices as well. The current policy payoff map uses objects that cease to be downstream Nash equilibria on part of the policy action set.

**Required fix:** Reopen Stage 4. Choose one of the following and verify it fully:

- **Preferred repair:** impose/derive a policy-depth cap or regularity condition under which every policy profile in the feasible IS/SU/SW policy domains admits the required regular pure location continuation, then solve the policy game using only true continuation equilibria.
- Solve and select the alternative/mixed/nonregular location equilibria for the problematic off-path subgames.
- Formally change the solution concept/action domain and rerun theory change control.

The first route is preferred because it leaves the mechanism intact.

**Does the fix reopen theory?** YES — Stage 4 at minimum; Stage 7/8/9/10 must subsequently be refreshed if the canonical witness or regularity domain changes.

**Resolved?** NO.

### B3. Bounded repair feasibility

**Attack:** The fatal continuation problem may destroy the headline result once repaired.

**Severity:** MAJOR BUT PRELIMINARILY ANSWERED.

**Evidence:** Stage-11 diagnostic at `s_bar=0.20`, keeping `v=0.04` and `gamma=0.11`, gives

`Delta_M^(B-T)≈-0.008984`,

`Delta_M^(B-X)≈-0.000434`,

`Delta_M^(FULL)≈+0.001049`.

The selected SU policy remains `(s_12,s_3)=(0.20,0)`. A 21×21 continuous whole-circle audit of the SU policy square reports no invalid selected-branch continuation.

**Interpretation:** The core interaction is likely salvageable without changing the economic mechanism.

**Required fix:** Stage 4R must upgrade this preliminary grid evidence into the canonical continuation-existence/policy-equilibrium verification and determine a defensible regularity bound rather than choosing `0.20` solely because it works numerically.

**Does the fix reopen theory?** YES, for parameter/regularity re-freeze.

### B4. Policy-stage equilibrium verification

**Attack:** IS and SW policy choices are hard-coded at the witness and SU uses coordinate optimization from one initial point; uniqueness and global policy best responses are under-documented.

**Severity:** MAJOR BUT FIXABLE.

**Evidence:** Stage-4 code sets `IS_F=welfare("IS",[SBAR],...)` and `SW_F=welfare("SW",[0,0,0],...)` rather than solving a generic policy equilibrium routine. Stage-11 scans support the intended directions: IS welfare rises toward `s_bar`, a unilateral SW singleton-depth increase lowers own welfare, and SU member welfare is maximized at the upper cap when outsider depth is zero.

**Required fix in Stage 4R:** derive the IS policy optimum analytically where possible; implement global policy best-response checks for SW and SU over the repaired continuation domain; test multiple starting points or characterize uniqueness.

**Does the fix reopen theory?** NO new primitive, but it is Stage-4 mathematics.

### B5. Numerical-not-proof / open-neighborhood wording

**Attack:** The manuscript says continuity gives an open regular neighborhood, but the neighborhood whole-circle audits use coarse location grids, and the policy continuation map is not valid on the full current action set.

**Severity:** MAJOR BUT FIXABLE after B2.

**Evidence:** The canonical witness now passes a continuous whole-circle audit, but the Stage-4 23/27 and 108/125 neighborhood statements use grid-based deviation searches.

**Required fix:** After Stage-4R, run continuous whole-circle best-response checks on the parameter neighborhood used to support the regular-region claim, and establish persistence of the policy best responses/continuation equilibrium rather than relying on the fixed-order branch alone.

**Does the fix reopen theory?** NO new primitive; YES affected verification/proof-status records.

### B6. Price block / demand block

**Attack:** FOCs may not characterize a price Nash equilibrium.

**Severity:** RESOLVED.

**Evidence:** On the stated regular domain demand is affine in own price, `D_ii<0` gives strict own-price concavity, and nonsingularity of the FOC system gives a unique interior price solution. Stage-4 symbolic checks reproduce the symmetric IS/SW closed forms.

### B7. Welfare-level normalization

**Attack:** The model assumes a large common baseline utility `A`, but reported world-welfare levels are negative because verification omits the common `A` constant.

**Severity:** MINOR.

**Evidence:** The code integrates welfare net of the common `A`; rankings and differences are unaffected.

**Required fix:** State that reported CS/GW levels are net of the common baseline utility `A`, or normalize `A=0` for reported welfare levels after imposing full coverage separately.

**Does the fix reopen theory?** NO.

---

## 4. Referee C — Welfare and institutional coherence

### C1. “Welfare is mechanical transfer accounting” attack

**Severity:** RESOLVED.

**Evidence:** The national member condition is exactly `Delta_M=Delta Pi_M+Delta CS/3`, while global welfare cancels price payments and retains only network value, transport/adaptation losses, and redesign costs. The national SU preference is therefore a distributional producer-rent effect, whereas the global ranking is a real-resource/network comparison. These are economically distinct objects.

### C2. Symmetric `CS/3` incidence

**Severity:** MAJOR LIMITATION, not fatal.

**Evidence:** Country of residence is independent of product taste and each country contains one third of the uniform consumer mass. This makes `CS/3` internally consistent, but it removes national demand asymmetries and may strengthen the producer-rent interpretation.

**Required fix:** Keep it explicit as a symmetry device and avoid claims about heterogeneous-country incidence. Any heterogeneous national-consumer extension is post-freeze theory work, not a referee-response add-on.

**Does the fix reopen theory?** NO for disclosure; YES for extension.

### C3. Institutional primitive

**Attack:** Real interoperability rules establish common technical specifications but do not generally imply that deeper regional integration mechanically raises absolute incompatibility with outsiders.

**Severity:** MAJOR BUT FIXABLE in interpretation.

**Evidence:** EU AFIR and similar rules verify that governments can mandate technical interoperability specifications. They do not by themselves verify the model's cross-bloc derivative or the predicted strategic product re-differentiation. Gandal–Shy provides a closer standards-union rationale for common policy toward nonmembers.

**Required fix:** Present the model as a stylized bloc-specific standards architecture, not as a literal description of every interoperability mandate. Cite primary institutional sources in the manuscript and explicitly label strategic re-differentiation as a prediction rather than a documented fact.

**Does the fix reopen theory?** NO if wording only.

### C4. Alternative demand / timing / external validity

**Severity:** MAJOR LIMITATION, bounded by claim discipline.

**Evidence:** No alternative demand geometry or reversed timing has been solved. Government commitment before product repositioning is essential to the mechanism.

**Required fix:** State the commitment timing and separate horizontal repositioning margin as essential assumptions. Do not add a new geometry during referee repair unless later required by the selected journal.

**Does the fix reopen theory?** NO for disclosure; YES for robustness extension.

---

## 5. Referee D — Journal fit and exposition

### D1. IJIO contribution strength

**Attack:** A three-firm symmetric model with a constructive numerical regular-region result may be too thin for IJIO, especially given strong overlap with Ruiz, Gandal–Shy and Klimenko.

**Severity:** MAJOR BUT FIXABLE / journal-positioning risk.

**Current assessment:** If the continuation/SPNE gap is repaired and the regular region is verified with a defensible parameter condition, the interaction result plus national/global welfare wedge is potentially field-journal quality. In the current mathematical state it is not submission-ready to IJIO or any comparable theory/IO outlet.

**Required fix:** repair mathematics first; then Stage 11 must be rerun before Stage 12. Stage 12 should choose the journal based on the surviving result rather than preserving IJIO as a target by assumption.

### D2. Claim inflation

**Severity:** MAJOR only where SPNE/open-region language exceeds the current proof; otherwise RESOLVED.

The introduction and main-results section are commendably explicit that the headline reversal is constructive rather than a global theorem. The remaining overclaim is the unqualified SPNE language given B2.

### D3. Exposition

**Severity:** MINOR.

The manuscript is structurally clear. Required exposition fixes after the mathematical repair are: define what `s=0` means under an SU; explain the policy-map normalization more carefully; state welfare levels net of `A`; add primary citations for institutional examples; and make the continuation-existence regularity condition visible before the policy equilibrium is stated.

---

## 6. Consolidated severity table

| Attack | Severity | Current status | Theory reopen? |
|---|---|---|---|
| Ruiz + Gandal–Shy synthesis | MAJOR BUT FIXABLE | narrow result-level distinction survives | No |
| No-new-mechanism | MINOR / RESOLVED | B-T/B-X isolate interaction | No |
| Result built into `tau` map | MAJOR BUT FIXABLE | B-T shows map alone insufficient | robustness may require control |
| Binary network graph vs continuous depth | MAJOR BUT FIXABLE | needs explicit interpretation | No if wording |
| Canonical SU whole-circle BR | RESOLVED | continuous audit passes | No |
| **Off-path continuation / SPNE** | **FATAL CURRENT DRAFT** | **unresolved** | **Yes — Stage 4R** |
| Policy-stage global/unique best responses | MAJOR BUT FIXABLE | partially audited | Stage 4R math |
| Open-neighborhood numerical proof status | MAJOR BUT FIXABLE | incomplete until continuation repair | verification rerun |
| Price/demand system | RESOLVED | analytic regular-domain proof holds | No |
| Welfare accounting | RESOLVED | exact identities hold | No |
| Welfare `A` normalization | MINOR | wording fix | No |
| `CS/3` national incidence | MAJOR LIMITATION | transparent symmetry device | No unless extended |
| Institutional cross-bloc interpretation | MAJOR BUT FIXABLE | source supports policy margin, not all derivatives | No if wording |
| Alternative demand/timing | MAJOR LIMITATION | not tested | theory extension if pursued |
| IJIO fit | MAJOR RISK | reassess after repair | No |

---

## 7. Required repair contract

### Mandatory Stage 4R work

1. **Continuation existence before policy optimization.** The policy payoff map may only evaluate downstream objects that are actual location-price equilibria. No fixed-order stationary candidate may be used as a policy-deviation payoff unless it passes the global location-Nash check.
2. **Policy-domain regularity.** Establish a defensible sufficient restriction on `s_bar` (or otherwise solve off-path continuations) so that every relevant IS/SU/SW policy profile has a well-defined regular continuation equilibrium. Do not choose a cap solely because it reproduces the desired result.
3. **Global policy best responses.** Re-solve IS, SU and SW depth games on the repaired continuation map, including corners/KKT and multiplicity checks.
4. **Main interaction re-test.** Require again `Delta_M^(B-T)<0`, `Delta_M^(B-X)<0`, `Delta_M^(FULL)>0`.
5. **Continuous whole-circle audit.** Replace the coarse-grid global-deviation check for the canonical neighborhood with interval-wise continuous best-response maximization or an equivalent certified procedure.
6. **If the repaired witness changes:** rerun Stage 7 welfare decomposition/generality, Stage 8 theory freeze, Stage 9 generated-output provenance, and Stage 10 manuscript construction before repeating Stage 11.

### Preferred repair direction

The preliminary `s_bar=0.20` diagnostic is the leading candidate because the mechanism survives and the sampled SU policy square remains regular. Stage 4R must nevertheless establish the regularity restriction independently of the desired welfare sign.

---

## 8. Theory-change implications

- A smaller canonical `s_bar` plus an explicit continuation-regularity restriction changes the frozen parameter/witness package and therefore requires Stage 4R and a new Stage-8 freeze after affected welfare stages are rerun.
- If off-path mixed/nonregular location equilibria are introduced, the solution concept changes materially and a broader theory re-audit is required.
- If continuous network intensity, transfers, alternative geometry, or new policy costs are added, this exceeds the bounded repair and must reopen the corresponding earlier mechanism/novelty stages.

The preferred repair does **not** change the core economic mechanism: government bloc depth still affects standard friction, firms still reposition after policy, and the contribution remains the FULL-only coalition-ranking reversal.

---

## 9. Resolved versus unresolved attacks

### Resolved now

- canonical on-path whole-circle location equilibrium;
- weighted-Laplacian demand and regular price equilibrium;
- exact national-welfare decomposition;
- exact global-welfare transfer cancellation;
- ingredient-level novelty overclaim;
- direct claim that SU stability itself is new.

### Unresolved and blocking

- full off-path continuation equilibrium needed for SPNE;
- policy-stage equilibrium on a valid continuation map;
- open regular-region proof after continuation repair.

### Unresolved but non-blocking once mathematics is fixed

- coefficient sensitivity / result-built-in attack;
- binary graph versus continuous-depth interpretation;
- institutional cross-bloc interpretation;
- `CS/3` external validity;
- journal fit.

---

## 10. Final Stage-11 verdict

**REOPEN EARLIER STAGE — STAGE 4R CONTINUATION-EXISTENCE / POLICY-STAGE REPAIR.**

This is **not** a project NO-GO. The Stage-11 repair diagnostic indicates that the headline interaction survives under a smaller, apparently regular policy cap. But the current Stage-10 draft is not mathematically submission-ready because its claimed SPNE is not established on the full current policy action set.

## 11. Next-stage contract

Do **not** execute Stage 12 yet.

Return to a bounded Stage 4R with the following sole objective:

> construct a globally valid continuation-equilibrium map for all feasible standards-depth policy deviations, re-solve the bloc-depth Nash game, and verify whether the FULL-only coalition-stability reversal survives without using non-equilibrium off-path location candidates.

If Stage 4R passes, rerun the affected Stage 7/8/9/10 records and then repeat Stage 11. Only a repeated Stage-11 `GO TO JOURNAL POSITIONING` authorizes Stage 12.
