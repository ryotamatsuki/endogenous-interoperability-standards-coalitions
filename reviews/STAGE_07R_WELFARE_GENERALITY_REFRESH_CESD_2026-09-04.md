# Stage 7R — Welfare / Generality Refresh: C-ESD

Date: 2026-09-04
Canonical workflow: `ryotamatsuki/research-paper-workflow` v1.1
Release SHA: `488e5ab06c207909296a7564eaf9066f7f94319c`
Template: `templates/STAGE_07_WELFARE_GENERALITY.md`
Trigger: Stage 4R continuation-existence / policy-stage repair

## 1. Executive verdict

**GO TO STAGE 8R — THEORY RE-FREEZE.**

The Stage-4R action-set clarification does not alter the equilibrium path, the exact welfare identities, the national rent-capture mechanism, the global-welfare wedge, or the private/social product-positioning wedge. The historical Stage-7 substantive conclusions survive.

The repaired policy variable is now strictly coalition-level additional harmonization depth: non-singleton blocs choose `s_C in [0,s_bar]`; singleton blocs have `s_C=0`. At the canonical witness `(t_bar,v,gamma,s_bar)=(1,0.04,0.11,0.25)`, repaired policy choices remain `s_I*=0.25`, `s_12*=0.25`, and all singleton depths equal zero.

## 2. Exact welfare accounting after repair

The exact consumer-surplus identity remains

`CS = A + v q'G_rho q - sum_i p_i q_i - TC`.

Firm profit remains

`Pi_i = p_i q_i - C_i^D`.

National welfare remains

`W_i = CS/3 + Pi_i`.

Hence for a prospective SU member,

`Delta_M = Delta Pi_M + Delta CS/3`.

The member prefers SU to IS iff

`Delta Pi_M > -Delta CS/3`.

Global welfare remains

`GW = A + v q'G_rho q - TC - sum_i C_i^D`,

because price payments cancel as transfers.

These identities are unaffected by the action-set repair.

## 3. Canonical repaired-witness decomposition

Stage-7R verification recomputes welfare from the repaired Stage-4R policy continuation, not from the historical two-dimensional SU policy routine.

At the repaired canonical witness:

- per-country CS component: `Delta CS/3 ≈ -0.0325785`;
- domestic-firm profit component: `Delta Pi_M ≈ +0.0341498`;
- member national-welfare change: `Delta_M ≈ +0.0015713`.

Thus the SU member ranking is still driven by domestic producer-rent capture overcoming a larger consumer-side loss in absolute value.

## 4. Global welfare

The repaired witness yields the same global-welfare values as Stage 7, net of the common baseline utility constant `A`:

- `GW_IS ≈ -0.0225000`;
- `GW_SU ≈ -0.0586685`;
- `GW_SW ≈ -0.0700000`.

Hence

`GW_IS > GW_SU > GW_SW`.

The decentralized national-government coalition game can therefore select SU even though IS yields higher global welfare at the witness. This remains a real-resource/network comparison, not price-transfer accounting.

## 5. Private versus social re-differentiation

Holding the repaired canonical SU policy at `s_12=0.25`, outsider singleton depth is zero by definition.

The inherited member distance is

`D0 = 1/3`.

The repaired private equilibrium remains

`D_private ≈ 0.497533`.

The constrained social-location benchmark remains

`D_social ≈ 0.431427`.

Therefore

`D_private > D_social > D0`.

Some re-differentiation is socially useful after regional harmonization, but private firms over-re-differentiate relative to the constrained social benchmark.

## 6. Interaction result remains the source of the welfare reversal

The Stage-4R repaired interaction signs remain

`Delta_M^(B-T) < 0`,

`Delta_M^(B-X) < 0`,

`Delta_M^(FULL) > 0`.

Numerically at the witness:

- `Delta_M^(B-T) ≈ -0.010167`;
- `Delta_M^(B-X) ≈ -0.000434`;
- `Delta_M^(FULL) ≈ +0.001571`.

Thus neither endogenous coalition harmonization depth alone nor endogenous product location alone crosses the national-welfare threshold. Their interaction does.

## 7. Adjustment-cost generality

The quadratic redesign cost remains a tractable baseline rather than the conceptual source of the mechanism. For a differentiable strictly convex repositioning cost `C(d)` with `C(0)=C'(0)=0`, the private SU condition remains conceptually

`MB_SU(d;s,v) = C'(d)`.

The Stage-4R repair changes the policy action set but not the SU marginal repositioning force. Hence the same economic intermediate-curvature logic remains:

1. high adjustment-cost curvature suppresses strategic re-differentiation and leaves `Delta_M<0`;
2. intermediate curvature permits a producer-rent gain sufficient to cross the member-welfare threshold;
3. very low curvature can generate order-changing location behavior and requires the global continuation checks now built into Stage 4R.

The repaired upper welfare threshold at `v=0.04`, `s_bar=0.25` remains

`gamma_W ≈ 0.132983`.

The Stage-7R verification confirms that the repaired IS and SU policy optima remain at the cap at this threshold.

The old phrase `gamma_GBR` should not be treated as a closed-form primitive threshold. The repaired continuation verification supersedes the earlier selected-branch-only lower-bound discussion for the canonical witness.

## 8. Institutional refresh

The primary-source classifications from Stage 7 remain unchanged. See:

- `literature/STAGE7_CESD_INSTITUTIONAL_VALIDATION.md`;
- `literature/STAGE7R_CESD_INSTITUTIONAL_REFRESH.md`.

The Stage-4R clarification improves the interpretation of `s_C`: it is additional harmonization depth conditional on a formal coalition/compatibility relation. A singleton has no internal harmonization pair and therefore no positive depth action.

The exact cross-bloc formula remains a stylized model normalization. Strategic product re-differentiation remains a model prediction rather than a documented empirical fact in the audited institutions.

## 9. Generality audit

The repaired mechanism continues to require five economic objects:

1. a formal compatibility or recognition relation;
2. a non-singleton coalition-level harmonization-depth margin;
3. network/access value linked to formal compatibility;
4. a separate horizontal product characteristic on which firms can reposition;
5. decentralized national/regional objectives that include domestic producer rents.

The mechanism does not claim generality to singleton policies with an independent harmonization-depth instrument. That object was removed by Stage 4R because it was economically misclassified.

The EV-charging and digital-messaging examples remain distinct institutional analogues for the policy-controlled interoperability margin; neither is evidence that strategic re-differentiation has already occurred.

## 10. Empirical predictions retained

1. deeper coalition harmonization reduces interface differentiation within the bloc while member firms increase differentiation on non-standardized dimensions;
2. the repositioning response is stronger under partial/regional harmonization than under symmetric industry-wide harmonization;
3. lower but non-negligible redesign costs strengthen the response;
4. national support for SU can coexist with consumer losses when domestic producer rents rise sufficiently;
5. outsiders can lose from regionalization;
6. a nationally stable regional coalition can coexist with globally preferable international standardization.

## 11. Policy scope and limits

No new policy instrument is introduced. The model does not justify subsidies, transfers, lobbying, antitrust remedies, or product-design mandates beyond the modeled standards-depth margin.

The result also does not imply that SU is generally inefficient or that IS globally dominates for all parameters. The global-welfare ranking remains witness-specific.

## 12. Remaining major concerns

1. The `1/2` cross-bloc coefficient remains a normalization and should receive bounded sensitivity analysis or disciplined claim wording before final submission.
2. National consumer incidence remains symmetric (`CS/3`).
3. Institutional evidence validates interoperability policy margins, not the predicted product-space response.
4. Ruiz (2004) + Gandal–Shy (2001) remains the main novelty synthesis attack.
5. Journal fit remains unresolved until repeated Stage 11.

None is a Stage-7R fatal blocker.

## 13. Stage-7R verdict

**GO TO STAGE 8R — THEORY RE-FREEZE.**

The welfare/generality package is preserved after the Stage-4R repair. Stage 8R should re-freeze the corrected action set and update proof-status/claim boundaries. No new extension is authorized during re-freeze.
