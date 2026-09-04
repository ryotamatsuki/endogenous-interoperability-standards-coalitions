# Stage 11R2 — Repeated Robustness / Referee Attack Gate

Date: 2026-09-04

Canonical workflow: `ryotamatsuki/research-paper-workflow` v1.1 @ `488e5ab06c207909296a7564eaf9066f7f94319c`

Canonical template: `templates/STAGE_11_REFEREE_GATE.md`

Canonical checklist: `checklists/REFEREE_ATTACK_CHECKLIST.md`

Repository: `ryotamatsuki/endogenous-interoperability-standards-coalitions`

Theory freeze: `CESD-THEORY-FREEZE-2026-09-04-v2`

Object under attack: production manuscript after PR #54 / merge SHA `c5559e710c053e3637483b27e08608e719bb8102`.

## 1. Executive referee-gate verdict

**CONDITIONAL GO — bounded major fixes.**

The refreshed manuscript survives the identification attack that killed the former joint-endogeneity headline. The paper now correctly identifies the central comparison as B-T versus FULL/B-EQ and explicitly concedes that endogenous harmonization-depth choice is not necessary at the canonical witness. The mathematical verification chain continues to support the canonical witness, the welfare accounting is internally coherent, and the closest-paper discussion is materially stronger.

No currently identified attack is `FATAL` to the narrower contribution. However, Stage 12 is **not yet authorized** because one major robustness burden remains unresolved: the national-welfare sign reversal is quantitatively small (`Delta_M^(FULL)≈+0.0015713`) and has not yet been demonstrated over an explicit economically meaningful parameter neighborhood. The manuscript's continuity argument establishes a nonempty local neighborhood conditional on persistence of the selected regular continuation branch, but a hostile referee can still reasonably characterize the result as a knife-edge numerical witness until that neighborhood is mapped computationally.

The required fix is bounded and does not require theory change: run a pre-specified local parameter-region robustness exercise around the canonical witness, preserving the frozen model, and report the region in which B-T remains negative while FULL remains positive together with policy-depth choices and continuation validity. If this exercise fails materially, reopen contribution assessment; if it passes, Stage 11R2 can be closed with `GO TO JOURNAL POSITIONING` without modifying theory.

## 2. Referee A — novelty and mechanism

### Attack A1 — classic-result / closest-paper synthesis

**Attack:** Gandal & Shy (2001) supplies the three-country standards-union, national-welfare, network, and coalition architecture; Ruiz (2004) supplies standards policy followed by endogenous product characteristics and price competition; Takarada et al. (2020) supplies regional-versus-multilateral standards harmonization, national welfare, and blocking. A referee may argue that the present model is merely the direct synthesis of these known ingredients.

**Severity:** MAJOR BUT FIXABLE.

**Evidence:** The refreshed Introduction and Related Literature explicitly acknowledge these components and no longer claim setup novelty. Stage 6R2 found the composite predecessor set structurally very close but did not identify a paper that directly establishes the result-level reversal from fixed positions to post-policy horizontal repositioning.

**Can the paper answer now?** Mostly yes.

**Required fix:** Keep the contribution strictly result-level. In the final journal version, state the closest-paper distinction in one compact paragraph: the paper does not contribute standards unions, continuous harmonization, endogenous characteristics, or strategic regulatory response separately; it contributes the equilibrium-ranking implication that allowing horizontal repositioning after a standards architecture can reverse the member-country IS/SU ranking relative to a fixed-position evaluation of that same architecture.

**Does the fix reopen theory?** NO.

### Attack A2 — no-new-mechanism / built-in result

**Attack:** The pairwise friction map mechanically lowers within-bloc friction and raises cross-bloc friction, so outward product repositioning and a regional advantage may be built into assumptions.

**Severity:** MAJOR BUT FIXABLE.

**Evidence:** The same friction map under B-T gives `Delta_M^(B-T)≈-0.010167`; therefore the map alone does not generate the positive regional ranking. B-EQ reproduces FULL at the witness, showing that the decisive margin is downstream product repositioning at the relevant harmonization depth, not policy-depth endogeneity.

**Can the paper answer now?** Yes for identification at the witness.

**Required fix:** Preserve the B-T vs B-EQ/FULL hierarchy and avoid language implying a theorem that the friction map generically induces reversal.

**Does the fix reopen theory?** NO.

### Attack A3 — same theorem hidden in prior work

**Attack:** Ruiz (2004) already has policy -> endogenous characteristics -> price competition -> welfare and excessive differentiation; perhaps the present reversal is already embedded there.

**Severity:** MINOR to MAJOR depending on referee.

**Evidence:** Ruiz's endogenous-characteristics extension is a strong downstream-mechanism predecessor, but Stage 6R2 found that its qualitative policy equilibrium is preserved rather than reversed by endogenous characteristics. The present result requires the induced repositioning effect to cross the national-welfare IS/SU threshold and alter coalition stability.

**Can the paper answer now?** Yes, subject to cautious wording.

**Required fix:** Do not claim a new strategic-response mechanism in the abstract. Claim the coalition-ranking consequence.

**Does the fix reopen theory?** NO.

## 3. Referee B — assumptions and mathematics

### Attack B1 — numerical witness presented as proof

**Attack:** Proposition 1 states existence of a nonempty regular parameter region, but the paper provides one canonical witness plus a conditional continuity statement rather than an explicit region.

**Severity:** MAJOR BUT FIXABLE.

**Evidence:** The manuscript correctly labels the result constructive, reports strict inequalities, and conditions the local-neighborhood statement on persistence of the selected regular continuation branch. Yet the positive FULL margin is only about `0.0015713`.

**Can the paper answer now?** Not fully.

**Required fix:** Add a local parameter-region audit around `(t_bar,v,gamma,s_bar)=(1,0.04,0.11,0.25)`. At minimum perturb `v`, `gamma`, and `s_bar` separately and jointly over a pre-declared compact grid; for each valid point recompute B-T and FULL policy optima, verify downstream location equilibrium by whole-circle unilateral deviations, and record whether `Delta_M^(B-T)<0<Delta_M^(FULL)`. Report invalid continuation points rather than silently dropping them.

**Does the fix reopen theory?** NO.

### Attack B2 — FOC versus actual equilibrium / order-changing deviations

**Attack:** Circular location models can have order-changing deviations, so stationary locations need not be Nash equilibria.

**Severity:** RESOLVED / MINOR residual.

**Evidence:** `verification/stage04r_cesd_continuation_repair.py` checks continuous whole-circle unilateral deviations and audits relevant cyclic-order / anchor branches over feasible policy depths at the canonical primitives before global scalar policy optimization. CI for the refreshed production manuscript passed the frozen verification chain.

**Can the paper answer now?** Yes at the canonical witness and audited policy domain.

**Required fix:** None beyond preserving the computational-status disclosure.

**Does the fix reopen theory?** NO.

### Attack B3 — boundary / KKT / policy cap

**Attack:** Both IS and SU choose `s_bar=0.25`, so the result may be an artifact of a binding harmonization cap.

**Severity:** MAJOR BUT FIXABLE.

**Evidence:** B-EQ shows that endogenous choice of the cap is not necessary for the reversal, but it does not show that the numerical value `0.25` is nonessential. Stage 7.5R explicitly classified the specific cap as not established as essential.

**Can the paper answer now?** Partially.

**Required fix:** Include `s_bar` in the local robustness map. Record whether the policy optima remain at the cap and whether the ranking survives when the cap is moderately lower/higher within the regular domain.

**Does the fix reopen theory?** NO.

### Attack B4 — functional-form dependence

**Attack:** The exact cross-bloc `1/2` coefficient, circular Salop geometry, quadratic redesign cost, and symmetric three-country setup may drive the result.

**Severity:** MAJOR BUT FIXABLE as a disclosure issue; potentially FATAL only if the paper claims broad generality.

**Evidence:** The contribution freeze already classifies the cross-bloc `1/2`, symmetric geometry, and `CS/3` incidence as tractability/normalization features and explicitly forbids broad generality claims. Alternative demand geometries are unsolved.

**Can the paper answer now?** Yes if claim scope stays narrow.

**Required fix:** No new extension in Stage 11R2. Add one sentence in limitations that alternative demand geometry and alternative friction mappings remain outside the verified result.

**Does the fix reopen theory?** NO.

### Attack B5 — alternative timing

**Attack:** If firms choose locations before standards policy, the repositioning mechanism disappears by construction.

**Severity:** MINOR provided timing is institutionally interpreted correctly.

**Evidence:** The paper's question is explicitly post-policy product adaptation. Reversed timing is a different economic question, not a robustness test that the current proposition must pass.

**Can the paper answer now?** Yes.

**Required fix:** Keep the institutional interpretation focused on redesign/repositioning after standards architecture becomes known.

**Does the fix reopen theory?** NO.

### Attack B6 — network effect necessity

**Attack:** Is `v>0` actually needed, or is the network-effect ingredient ornamental?

**Severity:** MAJOR BUT FIXABLE as contribution-scope clarification.

**Evidence:** Stage 7.5R explicitly states that `v>0` has not been established as essential and that disappearance at `v=0` has not been shown.

**Can the paper answer now?** Yes if the paper does not claim network effects are necessary.

**Required fix:** Include low-`v` perturbations in the parameter robustness exercise if computationally regular. Do not claim mechanism disappearance at `v=0` without evidence.

**Does the fix reopen theory?** NO.

## 4. Referee C — welfare and institution

### Attack C1 — welfare reversal is mechanical transfer accounting

**Attack:** The regional union wins nationally only because domestic producer profits enter national welfare; this may be a relabeling of transfers rather than a substantive welfare result.

**Severity:** MINOR to MAJOR.

**Evidence:** At the witness, `Delta CS/3≈-0.0325785` while `Delta Pi_M≈+0.0341498`, yielding `Delta_M≈+0.0015713`. The decomposition is economically substantive because national governments value resident producer rents while price transfers cancel only in global welfare. Global welfare ranks `IS>SU>SW`.

**Can the paper answer now?** Yes.

**Required fix:** Continue to characterize the mechanism as distributional political economy, not as a Pareto improvement.

**Does the fix reopen theory?** NO.

### Attack C2 — consumer-surplus incidence `CS/3`

**Attack:** Equal incidence of aggregate consumer surplus across countries may mechanically affect the national ranking.

**Severity:** MAJOR BUT FIXABLE as limitation.

**Evidence:** `CS/3` is explicitly frozen as a symmetric-incidence assumption, not a general theorem.

**Can the paper answer now?** Partially.

**Required fix:** State that the precise national-welfare threshold is incidence-sensitive. Do not infer robustness to asymmetric consumer ownership/incidence.

**Does the fix reopen theory?** NO for disclosure; YES if an asymmetric-incidence extension is added, which is not required here.

### Attack C3 — institutional specificity

**Attack:** The pairwise friction map may not correspond to any particular standards institution.

**Severity:** MAJOR BUT FIXABLE.

**Evidence:** The map is a reduced-form representation of within-bloc harmonization lowering compatibility/standard distance while creating relative separation from outsiders. It should not be presented as a literal legal rule.

**Can the paper answer now?** Yes with disciplined interpretation.

**Required fix:** Use examples only illustratively. Avoid claiming the exact `1/2` cross-bloc spillover is empirically calibrated.

**Does the fix reopen theory?** NO.

### Attack C4 — external validity

**Attack:** Three symmetric countries and one domestic firm each may be too stylized for broad policy claims.

**Severity:** MINOR if the contribution is framed as theory; MAJOR if policy prescriptions are broad.

**Evidence:** The refreshed manuscript is already constructive and explicitly disclaims global generality.

**Can the paper answer now?** Yes.

**Required fix:** Maintain theory-first language: fixed-product evaluations can mis-rank coalition incentives in the model; do not claim they generally do so empirically.

**Does the fix reopen theory?** NO.

## 5. Referee D — journal and exposition

### Attack D1 — insufficient contribution for a strong field journal

**Attack:** The result may be too narrow because the model combines known ingredients and the reversal is currently supported by a small numerical margin.

**Severity:** MAJOR BUT FIXABLE.

**Evidence:** Novelty confidence is MEDIUM; the strongest contribution is result-level rather than setup-level. The robustness map is therefore central to journal positioning.

**Can the paper answer now?** Not fully.

**Required fix:** Complete the bounded parameter-region robustness exercise before Stage 12. Journal selection must be based on the surviving demonstrated breadth, not the desired outlet.

**Does the fix reopen theory?** NO.

### Attack D2 — claim inflation

**Attack:** The manuscript could still be read as saying policy endogeneity causes the reversal.

**Severity:** RESOLVED.

**Evidence:** Abstract/Introduction/Main Results/Conclusion now explicitly state that B-EQ reproduces FULL at the witness and endogenous harmonization choice is not necessary.

**Can the paper answer now?** Yes.

**Required fix:** Preserve this language.

**Does the fix reopen theory?** NO.

### Attack D3 — exposition burden

**Attack:** Four benchmark labels may obscure the central economics.

**Severity:** MINOR.

**Evidence:** B-T vs FULL/B-EQ is now clearly central and B-X0 is explicitly auxiliary.

**Can the paper answer now?** Yes.

**Required fix:** In the final journal edit, explain B-T and B-EQ in prose before displaying all benchmark notation.

**Does the fix reopen theory?** NO.

## 6. Consolidated severity table

| Attack | Severity | Resolved now? | Required action |
|---|---|---:|---|
| Closest-paper synthesis | MAJOR BUT FIXABLE | Mostly | Keep result-level positioning |
| Result built into friction map | MAJOR BUT FIXABLE | Yes at witness | Preserve B-T/B-EQ identification |
| Hidden Ruiz equivalence | MINOR/MAJOR | Yes | Narrow wording |
| Numerical witness / small margin | MAJOR BUT FIXABLE | **No** | Explicit parameter-region map |
| FOC vs equilibrium | MINOR residual | Yes | Preserve whole-circle verification |
| Binding cap | MAJOR BUT FIXABLE | **No** | Include `s_bar` robustness |
| Functional form | MAJOR BUT FIXABLE | Yes by scope | Limitation disclosure |
| Alternative timing | MINOR | Yes | Interpret post-policy adaptation |
| Network effect necessity | MAJOR BUT FIXABLE | Partly | Include low-`v` perturbation; no necessity claim |
| Welfare as transfer accounting | MINOR/MAJOR | Yes | Distributional interpretation |
| `CS/3` incidence | MAJOR BUT FIXABLE | Yes by scope | Explicit incidence sensitivity |
| Institutional reduced form | MAJOR BUT FIXABLE | Yes by scope | No literal calibration claim |
| External validity | MINOR | Yes by scope | No broad empirical claim |
| Journal sufficiency | MAJOR BUT FIXABLE | **No** | Robustness before Stage 12 |
| Policy-endogeneity claim inflation | RESOLVED | Yes | Preserve B-EQ disclosure |

## 7. Required fixes

### Binding fix R11R2-1 — local parameter-region robustness

Run a frozen-model robustness map around the canonical witness. Pre-specify perturbations before inspecting results. Required dimensions:

- `v` around `0.04`;
- `gamma` around `0.11`;
- `s_bar` around `0.25`.

For every evaluated point:

1. solve B-T policy choices globally on the repaired action set;
2. solve FULL policy choices globally;
3. verify selected location continuations against whole-circle unilateral deviations;
4. record `Delta_M^(B-T)` and `Delta_M^(FULL)`;
5. record IS/SU optimal depths and whether either hits the cap;
6. classify the point as reversal / no reversal / invalid continuation;
7. do not discard invalid or sign-failing points.

Minimum success condition for Stage-12 authorization: a transparent nontrivial neighborhood, not a single adjacent point, in which `Delta_M^(B-T)<0<Delta_M^(FULL)` and continuation verification passes. The exact grid width is a computational design choice but must be declared in the verification file before execution.

### Bounded manuscript fixes after robustness

- Add a compact robustness paragraph/table.
- Add a limitations sentence on alternative demand geometry/friction mappings.
- Preserve B-EQ identification language.
- Do not add a new theoretical extension unless robustness fails and formal theory-change control is triggered.

## 8. Theory-change implications

No current required fix changes the theory freeze. The theory remains `CESD-THEORY-FREEZE-2026-09-04-v2`.

If the local robustness map fails to find a nontrivial region, the response must **not** be to tune primitives opportunistically. Reopen Stage 7.5R contribution assessment and, if necessary, Stage 6 novelty/contribution positioning. Any new demand system, alternative friction map, asymmetric incidence, or altered timing is a substantive extension and requires formal theory-change control.

## 9. Resolved versus unresolved attacks

### Resolved

- former joint-endogeneity identification error;
- B-EQ interpretation;
- canonical whole-circle deviation concern;
- welfare accounting at the witness;
- setup-novelty overclaim;
- claim that endogenous policy depth is necessary;
- B-X0 misuse as a necessity test.

### Unresolved but bounded

- explicit parameter-region breadth around the small positive national-welfare margin;
- sensitivity to the harmonization cap within the same frozen model;
- resulting journal-level sufficiency.

No unresolved `FATAL` attack is identified at this stage.

## 10. Verdict and Stage 12 contract

**Final verdict: `CONDITIONAL GO` — bounded major fixes.**

Stage 12 remains **BLOCKED**.

The only binding pre-Stage-12 task is the frozen-model local parameter-region robustness package described in R11R2-1 plus the corresponding bounded manuscript disclosure. If that package establishes a nontrivial verified reversal region, close repeated Stage 11R with `GO TO JOURNAL POSITIONING`. If it does not, reopen contribution assessment rather than altering theory ad hoc.
