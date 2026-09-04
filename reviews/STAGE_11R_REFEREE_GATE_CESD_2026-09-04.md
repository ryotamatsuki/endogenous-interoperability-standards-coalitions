# Stage 11R — Repeated Robustness / Referee Attack Gate: C-ESD

Date: 2026-09-04
Canonical workflow: `ryotamatsuki/research-paper-workflow` v1.1
Workflow SHA: `488e5ab06c207909296a7564eaf9066f7f94319c`
Freeze under attack: `CESD-THEORY-FREEZE-2026-09-04-v2`
Stage-10R manuscript merge SHA: `09e2c6e638d4594413981a309a0f657b456b61bc`

## 1. Executive referee-gate verdict

**REOPEN EARLIER STAGE — STAGE 6R2 CONTRIBUTION RE-KILL / BENCHMARK IDENTIFICATION REPAIR.**

The repaired v2 model survives the mathematical attack that killed the first Stage-11 draft. Singleton blocs no longer possess spurious positive harmonization-depth instruments; the repaired action sets remove the previously invalid outsider-depth subgames; Stage-4R verifies whole-circle location Nash continuations over the repaired IS/SU policy domains at the canonical primitives and globally re-solves the scalar policy problems. The welfare accounting and the canonical coalition-ranking numbers remain internally consistent.

However, Stage 11R identifies a different and more fundamental problem with the *label of the contribution*. The manuscript and v2 freeze claim a FULL-only interaction of **policy endogeneity** and **location endogeneity**: B-T (endogenous policy, fixed locations) selects IS; B-X (zero depth, endogenous locations) selects IS; FULL (endogenous policy and endogenous locations) selects SU.

At the canonical witness, the repaired policy optima are

- `s_I*=s_bar`,
- `s_SU*=s_bar`.

Therefore consider the referee benchmark `B-EQ`, in which harmonization depths are **not endogenous** but are fixed exogenously at the FULL equilibrium values (`s_I=s_SU=s_bar`), while product locations remain endogenous. `B-EQ` is literally the same downstream game as FULL at the canonical witness. Hence

`Delta_M^(B-EQ)=Delta_M^(FULL)>0`.

This is verified in `verification/stage11r_cesd_referee_audit.py`.

The implication is exact: **policy endogeneity is not necessary for the canonical reversal.** What the existing calculations identify is that a positive/regional harmonization policy, when followed by endogenous strategic product repositioning, can reverse the coalition ranking relative to a fixed-location evaluation. B-T versus FULL identifies the strategic repositioning effect after policy. B-X at zero depth is a useful zero-harmonization benchmark, but it does not establish that the *endogeneity* of policy is an essential interacting margin.

This does not kill the economic model. It kills the current frozen contribution wording and therefore blocks Stage 12. The project must re-kill novelty around the narrower surviving claim and re-freeze the contribution before journal positioning.

---

## 2. Referee A — Novelty / mechanism

### A1. Headline benchmark-identification attack

**Attack:** The paper claims a two-endogenous-margin interaction, but its B-X benchmark changes the *level* of harmonization depth from the FULL equilibrium value to zero. Because FULL policy choices sit at the cap, an exogenous-depth benchmark fixed at the FULL values reproduces FULL exactly.

**Severity:** **FATAL TO THE CURRENT CONTRIBUTION CLAIM; NOT FATAL TO THE MODEL.**

**Evidence:**

1. Stage-4R globally re-solves the repaired policy stage and obtains `s_I*=s_SU*=s_bar=0.25`.
2. `verification/stage11r_cesd_referee_audit.py` defines `B-EQ`: fix IS/SU depth exogenously at `s_bar`, leave product locations endogenous.
3. The script verifies equality of FULL and B-EQ welfare vectors, product locations, and member gain to numerical tolerance.
4. Therefore `Delta_M^(B-EQ)=Delta_M^(FULL)=+0.001571...`.
5. The current Stage-7.5/8/10R claim says policy endogeneity alone and location endogeneity alone fail, while their interaction succeeds. That wording attributes necessity to policy endogeneity that the canonical equilibrium does not demonstrate.

**Can the paper answer now?** Not under the current v2 contribution freeze.

**Required fix:** Reframe the main result around the effect actually identified:

> A standards policy that compresses within-union differentiation can induce strategic product re-differentiation; allowing that post-policy repositioning can reverse the national coalition ranking relative to the fixed-location policy evaluation and stabilize a regional standards union.

B-T versus FULL is the clean main comparison. B-X at zero depth may remain as an auxiliary zero-harmonization benchmark, but it cannot be used to prove that policy *endogeneity* is essential. Add B-EQ or an equivalent observation explicitly so a referee cannot reconstruct the objection independently.

**Does the fix reopen theory?** No primitive needs to change, but the frozen main contribution and novelty claim must be reopened. Route to Stage 6R2 and then re-freeze.

**Resolved?** NO at Stage 11R.

### A2. Ruiz (2004) + Gandal–Shy (2001) synthesis attack under the narrower claim

**Attack:** Once policy endogeneity is removed from the novelty claim, the surviving result may look even closer to a synthesis of Ruiz's policy-to-product-characteristics timing and Gandal–Shy's standards-union architecture.

**Severity:** MAJOR; must be re-killed after A1 reframing.

**Evidence:**

- Gandal & Shy (2001), *Standardization Policy and International Trade*, already analyze three countries, standardization unions, network effects/conversion costs, national welfare, and union incentives.
- Ruiz (2004), *Mix-and-Match and International Standardization Policy*, explicitly studies government recognition policy followed by endogenous product characteristics and prices; his endogenous-characteristics extension does not generate the present three-country coalition-stability reversal.
- Klimenko (2009) already studies continuous government compatibility policy with network externalities.

**Current answer:** No located paper directly establishes the narrower result: post-policy endogenous horizontal repositioning reverses an IS/SU coalition ranking relative to the same policy evaluated at fixed product positions.

**Required fix:** Stage 6R2 must attack this exact narrower claim, not the superseded 'two endogenous margins' claim.

**Does the fix reopen theory?** NO model change; YES contribution/novelty freeze.

### A3. Current-frontier interoperability attack

**Attack:** Recent work already studies coalitional interoperability and strategic responses to mandated interoperability.

**Severity:** MAJOR BUT FIXABLE by positioning.

**Evidence:**

- Huang, Tan, Teh & Zhou (2026), *A Network Approach to Interoperability*, studies weighted interoperability networks, industry-wide versus coalitional interoperability, prices and welfare. It does not include post-policy endogenous horizontal product repositioning or government IS/SU/SW stability generated by that repositioning.
- Kretschmer, Rasch, Shekhar & Wenzel (2025), *Strategic Response to Mandated Interoperability: Privacy Spillovers in Network Markets*, makes a strategic-response-to-interoperability claim, but the response is data/privacy behavior rather than product-space re-differentiation and it has no international standards-coalition stability result.

**Required fix:** The refreshed literature section after Stage 6R2 should cite these frontier papers to avoid any broad claim that strategic response to interoperability is new.

**Does the fix reopen theory?** NO.

### A4. Result-built-into-assumption / policy-map attack

**Attack:** SU depth mechanically lowers within-bloc friction and raises cross-bloc friction, so the repositioning force may be built into the map.

**Severity:** MAJOR LIMITATION, not fatal to the narrower result.

**Evidence:** B-T uses the identical policy map but still selects IS; hence the map alone does not generate the coalition reversal. The exact cross-bloc coefficient `1/2` remains a stylized normalization.

**Required fix:** Retain explicit conditional wording: the mechanism requires within-bloc compression together with relative bloc-boundary separation. Do not claim invariance to arbitrary policy maps.

**Does the fix reopen theory?** NO for claim discipline; YES if the baseline map is changed.

---

## 3. Referee B — Assumptions / mathematics

### B1. Original Stage-11 off-path continuation attack

**Attack:** Policy-stage deviations may be evaluated using non-Nash downstream location candidates.

**Severity:** Previously fatal; **RESOLVED under v2 at the canonical primitives.**

**Evidence:** Stage-4R removes singleton depth instruments, searches continuous whole-circle unilateral deviations, enumerates all cyclic orders and circular-anchor branches on a 51-point depth grid, and globally re-solves the repaired scalar policy stage. The previous invalid profile `(s_12,s_3)=(0.25,0.20)` is not feasible because the singleton outsider has no depth instrument.

**Required fix:** None to the baseline action set. Keep Stage-4R in the production verification chain.

### B2. Continuum certification versus computational support

**Attack:** 'Every feasible policy depth' is not an analytic theorem. The code combines dense-grid all-order enumeration with global numerical searches.

**Severity:** MAJOR LIMITATION, correctly disclosed; not independently fatal.

**Evidence:** v2 explicitly classifies full-policy-domain continuation validity as `NUMERICALLY SUPPORTED ONLY`, and the appendix says it is computational at the canonical primitives rather than a global analytic theorem.

**Required fix:** Preserve this proof-status boundary. Do not call the continuation result an analytic SPNE existence theorem for the entire parameter space.

**Does the fix reopen theory?** NO.

### B3. Policy corner / no direct policy cost

**Attack:** The policy stage is at the upper cap for both IS and SU. This makes the phrase 'endogenous depth is essential' especially vulnerable and raises the question whether the policy stage adds more than selecting a boundary value.

**Severity:** **MAJOR and directly supports A1.**

**Evidence:** Stage-4R obtains `s_I*=s_SU*=s_bar` in B-T and FULL. No direct policy cost is included.

**Required fix:** Do not sell the paper as showing that endogenous policy choice itself is essential. The policy stage remains a coherent institutional feature of the model, but the contribution must be attributed to post-policy strategic repositioning and coalition-ranking feedback.

**Does the fix reopen theory?** NO primitive change needed.

### B4. FOC versus global location equilibrium

**Severity:** RESOLVED at the canonical repaired policy domain computationally.

Stage-4R whole-circle tests explicitly go beyond fixed-order FOCs. Low-cost branches that fail global best response are not silently accepted.

### B5. Price equilibrium, feasibility, SOC and welfare accounting

**Severity:** RESOLVED on the stated regular domain.

The weighted-Laplacian demand system is affine; `D_ii<0` supplies strict own-price concavity; the location FOCs/SOCs are correctly labeled conditional; welfare identities exactly cancel price transfers globally.

### B6. Corner/KKT attack

**Severity:** RESOLVED computationally for the canonical policy problem.

Global scalar policy optimization includes endpoints explicitly. The remaining issue is interpretation of the cap optimum, not omitted KKT arithmetic.

---

## 4. Referee C — Welfare / institution / generality

### C1. Welfare-is-mechanical attack

**Severity:** RESOLVED.

`Delta_M=Delta Pi_M+Delta CS/3` shows the national SU gain is a domestic producer-rent effect that narrowly outweighs member consumer loss. World welfare removes price transfers and retains network value, adaptation/transport losses and redesign cost. The two rankings therefore encode distinct incidence rather than a bookkeeping tautology.

### C2. World-welfare normalization

**Severity:** RESOLVED.

Stage 10R now reports numerical levels as `GW-A`; rankings are unaffected by the common baseline utility.

### C3. Symmetric national consumer incidence

**Severity:** MAJOR LIMITATION, not fatal.

`CS/3` is internally consistent with the symmetric residence/taste assumption but cannot support heterogeneous-country incidence claims.

**Required fix:** Keep the limitation explicit. No heterogeneity extension is required at this gate.

### C4. Institutional primitive and external validity

**Severity:** MAJOR BUT FIXABLE by disciplined scope.

Real interoperability and standards rules establish policy-controlled interface/compatibility margins, but they do not generally imply the exact model derivative that deeper regional harmonization raises outsider separation, nor do they establish observed strategic re-differentiation. The manuscript already treats the latter as a prediction.

**Required fix:** Preserve the 'stylized bloc-specific architecture' language. Add primary institutional citations only as validation of the policy primitive, not as evidence for the predicted repositioning response.

### C5. Alternative demand/timing attack

**Severity:** MAJOR LIMITATION, not fatal to a narrowly stated theory paper.

No alternative geometry or reversed policy/firm timing is solved. Government commitment before repositioning and a separate horizontal product margin are essential assumptions and must remain labeled as such.

---

## 5. Referee D — Journal / exposition

### D1. Claim inflation

**Attack:** Introduction, abstract and freeze language currently overstate what B-T/B-X/FULL identify by calling the result a joint-endogeneity reversal.

**Severity:** FATAL TO CURRENT EXPOSITION because it is the headline contribution.

**Required fix:** Rewrite the headline around **policy-induced strategic re-differentiation changing coalition stability**, not around necessity of policy endogeneity. The zero-depth B-X benchmark may remain descriptive, but the paper must acknowledge that fixing depth exogenously at the FULL cap reproduces FULL at the canonical witness.

### D2. Journal contribution strength

**Severity:** UNRESOLVED pending A1/A2 repair.

A three-country constructive theory result with exact welfare decomposition and a clear strategic-repositioning mechanism can plausibly remain field-journal material. But journal positioning cannot be evaluated on a contribution claim that the paper's own equilibrium values refute. Stage 12 remains blocked.

### D3. Numerical-not-proof / exposition

**Severity:** MAJOR BUT MANAGEABLE.

The paper now distinguishes analytic results from computational witness/continuation claims. After contribution reframing, the main result should preferably be called a 'constructive result' rather than allowing proposition terminology to imply a global analytic theorem.

---

## 6. Consolidated severity table

| Attack | Severity | Status |
|---|---|---|
| A1 joint-endogeneity benchmark identification | **FATAL to current contribution claim** | UNRESOLVED |
| A2 Ruiz + Gandal–Shy under narrower claim | MAJOR | RE-KILL REQUIRED |
| A3 current-frontier interoperability literature | MAJOR BUT FIXABLE | BOUNDED |
| A4 policy-map specificity | MAJOR LIMITATION | DISCLOSABLE |
| B1 v1 off-path continuation gap | formerly FATAL | RESOLVED |
| B2 computational continuum certification | MAJOR LIMITATION | DISCLOSED |
| B3 policy cap/no policy cost | MAJOR | FEEDS A1 |
| B4 FOC vs whole-circle equilibrium | formerly FATAL risk | RESOLVED COMPUTATIONALLY |
| B5 price/welfare math | MINOR/RESOLVED | RESOLVED |
| C1 welfare accounting | RESOLVED | RESOLVED |
| C3 symmetric CS incidence | MAJOR LIMITATION | DISCLOSABLE |
| C4 institution/external validity | MAJOR BUT FIXABLE | BOUNDED |
| D1 headline claim inflation | **FATAL to current exposition** | UNRESOLVED |
| D2 journal level | UNRESOLVED | STAGE 12 BLOCKED |

---

## 7. Required fixes

1. **Reopen the contribution, not the model.** The repaired v2 primitives remain intact.
2. Route to **Stage 6R2 — Contribution Re-Kill / Benchmark Identification Repair**.
3. Re-kill the narrower candidate claim:
   - standards policy is evaluated under fixed product positions;
   - allowing post-policy strategic product repositioning can reverse the IS/SU national-welfare ranking and stabilize SU;
   - this can occur even though consumers lose and global welfare favors IS.
4. Retain B-T as the central causal benchmark.
5. Retain B-X(0-depth) only as an auxiliary zero-harmonization benchmark; do not interpret it as proving policy endogeneity is necessary.
6. Add `B-EQ` (exogenous FULL-equilibrium depth with endogenous locations) or an equivalent transparent statement. At the canonical witness `B-EQ=FULL`.
7. Re-run novelty against Ruiz (2004), Gandal–Shy (2001), Klimenko (2009), Huang et al. (2026), and Kretschmer et al. (2025) using the narrower claim.
8. If the narrower claim survives, conduct a new freeze decision and refresh abstract/introduction/results/conclusion before another referee gate.

---

## 8. Theory-change implications

No change to players, timing, policy map, utility, network structure, redesign cost, welfare, action sets or coalition-stability rules is presently required.

The **contribution freeze is invalidated**, not the repaired model. `CESD-THEORY-FREEZE-2026-09-04-v2` remains the authority for model primitives and numerical objects but is **suspended as submission authority for the main contribution statement** until the contribution is re-killed and re-frozen.

---

## 9. Resolved versus unresolved attacks

### Resolved

- original singleton-depth/off-path continuation defect;
- canonical whole-circle location best-response defect;
- price FOC/concavity block;
- welfare accounting and world-welfare normalization;
- empirical overclaim that repositioning is already observed.

### Unresolved

- necessity/identification of policy endogeneity in the headline result;
- novelty strength of the narrower repositioning-induced coalition-reversal claim;
- journal level after that reframing.

---

## 10. Final verdict and Stage-12 contract

**VERDICT: REOPEN EARLIER STAGE — STAGE 6R2 CONTRIBUTION RE-KILL / BENCHMARK IDENTIFICATION REPAIR.**

Stage 12 is **not authorized**.

The next stage must not alter the repaired model merely to recover the old two-endogeneity narrative. It must test whether the narrower result-level contribution survives prior art and remains full-paper worthy. Only after a new contribution freeze and manuscript refresh may Stage 11 be repeated again.
