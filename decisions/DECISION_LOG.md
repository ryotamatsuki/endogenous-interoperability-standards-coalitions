# Decision Log

## D-001 — Separate repository

Date: 2026-09-04
Decision: ACCEPTED

Create a separate repository for endogenous partial interoperability rather than modifying `private-compatibility-standards-coalitions`.

Reason: the prior standards-coalition paper has a separate frozen/canonical theory and submission path. Mixing a new Salop/network-effects/endogenous-`a_i` model into that record would blur provenance and invalidate freeze discipline.

## D-002 — Canonical workflow

Date: 2026-09-04
Decision: ACCEPTED

Use `ryotamatsuki/research-paper-workflow` v1.1 at release SHA `488e5ab06c207909296a7564eaf9066f7f94319c`.

## D-003 — Research repository before production manuscript

Date: 2026-09-04
Decision: ACCEPTED

Treat this as a research-development repository. Do not build the production manuscript structure before Stage 7.5 authorizes full-paper investment and Stage 8 freezes theory.

## D-004 — Early endogenous-interoperability kill gate

Date: 2026-09-04
Decision: REFINED BY STAGE 0 AND STAGE 1

Initialization required a nonempty parameter region with `0 < a_o* < 1` plus a distinct coalition/welfare threshold `â` whose ordering relative to `a_o*` changes a strategically meaningful equilibrium or welfare result.

Stage 0 established that interior compatibility is already old and therefore is a viability condition only. Stage 1 further established that neither `a_o*` nor `â` should be treated as primitive scalar objects. The primitive objects are regime-specific implementation equilibria `a*(rho;theta)` and government continuation-value differences `Delta_i(rho,rho';theta)`.

A scalar `â` is admissible only as a later derived threshold after monotonicity and uniqueness are proved.

## D-005 — Salop and network effects are candidates, not commitments

Date: 2026-09-04
Decision: ACCEPTED / STRENGTHENED

Use Salop differentiation and network effects as candidate mechanisms only. Close prior work already combines compatibility choice, horizontal differentiation, network effects, and downstream competition. They have no presumptive contribution value and should be dropped unless indispensable to a surviving full-game result.

## D-006 — No artificial interiority

Date: 2026-09-04
Decision: ACCEPTED / STRENGTHENED BY MATHEMATICAL AUDIT

Do not add convex interoperability cost or another curvature term solely to force an interior solution. Any such term requires an independent economic/technological interpretation and robustness check.

Stage 1's symbolic audit of Stadler et al. shows why this discipline matters: even a familiar quadratic compatibility cost plus a correct symmetric FOC does not remove the need to verify SOC/global best responses and corners.

## D-007 — Reject the original ingredient-combination contribution

Date: 2026-09-04
Decision: REJECTED AS CONTRIBUTION CLAIM

Do not claim novelty from `Salop + network effects + endogenous partial interoperability + price competition`.

## D-008 — Stage-0 surviving actor/timing object

Date: 2026-09-04
Decision: REJECTED AS NOVELTY CLAIM / RETAINED AS GAME SKELETON

Stage 0 retained:

`formal standards coalition / government membership -> privately controlled interoperability implementation -> downstream competition -> national welfare -> coalition participation/deviation stability`.

Stage 1 found that the project's own frozen benchmark already has the analogous timing with binary private adoption. Therefore actor/timing separation is not itself a contribution. It remains the skeleton in which a continuous generalization would have to generate a genuinely new result.

## D-009 — Interpretation of the government threshold

Date: 2026-09-04
Decision: REPLACED BY STAGE 1

Do not presume a scalar government threshold `â`.

Primitive stability condition:

`Delta_i(rho,rho';theta) = V_i(rho;theta) - V_i(rho';theta) >= 0`,

where each continuation value uses its own regime-specific private implementation and product-market equilibrium.

Only if a later model proves continuity, monotonicity, and a unique root may a scalar `â` be introduced as a derived representation.

## D-010 — Stage 0 verdict

Date: 2026-09-04
Decision: `GO TO AUDIT`

The broad original mechanism was substantially preempted, but a narrower research object justified a source and mathematical audit.

## D-011 — Own frozen paper is a mandatory nested benchmark

Date: 2026-09-04
Decision: ACCEPTED

Treat `ryotamatsuki/private-compatibility-standards-coalitions` as benchmark B0 in all later novelty analysis.

Its Stage-8 canonical model already contains:

`formal government partition -> private standard adoption -> Cournot competition -> national welfare -> coalition stability`.

The new project must not modify this frozen theory. It must recover or contrast it as a nested benchmark.

## D-012 — Klimenko (2009) is a mandatory continuous-government benchmark

Date: 2026-09-04
Decision: ACCEPTED

Treat Klimenko's 2009 papers on technical compatibility standards, compatibility-enhancing effort, strategic government policy and international agreements as benchmark B2.

Implication: `continuous partial compatibility + government policy + international coordination` is not a viable contribution claim. Any surviving result must depend on endogenous standards-coalition membership/stability and private continuation implementation in a way unavailable in Klimenko-type policy games.

## D-013 — Symmetric FOC is never sufficient for implementation equilibrium

Date: 2026-09-04
Decision: ACCEPTED

For any future endogenous interoperability choice, require SOC/concavity or KKT/global optimization, asymmetric unilateral deviations, feasibility, and boundary comparisons.

Reason: the Stage-1 SymPy audit exactly reproduced the Stadler et al. price equilibrium and symmetric first-stage FOC but produced an admissible parameter counterexample in which the reported interior stationary point has a positive own second derivative and is not a best response.

## D-014 — Freeze residual project as a generalization/unification candidate

Date: 2026-09-04
Decision: ACCEPTED FOR STAGE 2 ONLY

Freeze the Stage-2 comparison object as:

> Does endogenizing a continuous post-agreement private interoperability implementation margin inside a government standards-coalition game generate a coalition-stability result unavailable in both the binary private-adoption coalition benchmark and continuous compatibility/government-policy models considered separately?

No functional-form model is frozen.

## D-015 — Stage 1 verdict

Date: 2026-09-04
Decision: `GO TO NOVELTY GATE`

The audit produced a coherent residual game, corrected the stability formulation, and identified the necessary nested benchmarks. Remaining uncertainty is primarily whole-game prior-art absorption, which belongs to Stage 2.

Novelty remains UNRESOLVED.

## D-016 — Economides–Skrzypacz is a mandatory coalition benchmark

Date: 2026-09-04
Decision: ACCEPTED

Add Economides & Skrzypacz (2003), *Standards Coalitions Formation and Market Structure in Network Industries*, as benchmark B4.

Reason: it directly models endogenous technical-standards coalitions followed by oligopoly and makes coalition membership trade off network benefits against intensified competition. However, coalition members are firms, affiliation itself determines the common standard, and the objective is firm profit rather than national welfare. It does not contain a separate government coalition stage followed by an independent continuous private implementation choice.

## D-017 — Modern interoperability frontier is a mandatory benchmark family

Date: 2026-09-04
Decision: ACCEPTED

Add benchmark B5 covering Ding–Ko–Shen (2022), Huang–Tan–Teh–Zhou (2026), Bourreau–Raizonville–Thébaudin (2026), Ekmekci–White–Wu (2025), Kim (2026), and closely related current interoperability work.

Implication: pairwise, weighted, coalitional, platform, or regulated interoperability cannot be used as an easy novelty pivot.

## D-018 — Kill all ingredient-level novelty claims

Date: 2026-09-04
Decision: ACCEPTED

The following are permanently rejected as standalone contribution claims: continuous interoperability, interior interoperability, network effects plus compatibility, price competition after compatibility, private/social wedges, standards coalition formation, government standardization unions, coalition-proof partial compatibility, government compatibility policy, and weighted/pairwise interoperability.

They may appear only as modeling ingredients or nested benchmarks.

## D-019 — Stage-3 surviving mechanism target

Date: 2026-09-04
Decision: ACCEPTED FOR MECHANISM SEARCH ONLY

The only authorized Stage-3 mechanism is the regime-dependent private implementation feedback:

`rho -> a*(rho;theta) -> downstream equilibrium -> V_i(rho;theta) -> government deviation incentives`.

Preferred candidate theorem: **implementation-induced stability reversal**, meaning a nonempty parameter region in which endogenous continuous implementation changes the sign of a government's coalition participation/deviation payoff relative to a binary or exogenous-implementation benchmark.

A stronger admissible target is a non-monotone or disconnected stability region that cannot arise in B0.

## D-020 — Stage 2 verdict

Date: 2026-09-04
Decision: `GO` → `GO TO MECHANISM SEARCH`

No single audited prior model reproduces the complete government-coalition / distinct-private-continuous-implementation / downstream-competition / national-welfare / regime-specific-stability game after direct relabeling. The project therefore survives as a narrow generalization/unification candidate.

This is not a novelty finding. Stage 3 must produce a new full-game result. If a minimal model merely smooths or relabels B0 thresholds, return `NO-GO` rather than add complexity.

## D-021 — Fixed Stage-3 scoring rule

Date: 2026-09-04
Decision: ACCEPTED

Use ex-ante candidate weights: whole-game prior-art survival 25%, theorem sharpness 20%, tractability 20%, mechanism clarity 15%, welfare content 10%, institutional relevance 10%.

Ten candidates were scored under these weights. The reproducible scoring artifact is `verification/stage03_candidate_scoring.py`.

## D-022 — Select Coalition-Scope Implementation Crowd-Out

Date: 2026-09-04
Decision: ACCEPTED FOR STAGE 4 TEST

Select C1 — **Coalition-Scope Implementation Crowd-Out (CSIC)** — as the single preferred minimal mechanism.

Core loop:

`rho -> interoperability partner scope -> private a*(rho) -> downstream competition -> national welfare -> stability`.

Reason: C1 uses the same implementation technology under every regime and lets the formal coalition alter only the scope of interoperability relationships. It therefore gives the cleanest chance to derive, rather than assume, regime-dependent implementation and a stability reversal.

C2 bilateral implementation free-riding is ranked second and may be revisited only if C1 is formally rejected and the workflow returns to Stage 3. C3 national-incidence/rent-shifting is not a separate Stage-4 mechanism.

## D-023 — Freeze Stage-4 no-hybridization rule

Date: 2026-09-04
Decision: ACCEPTED

Stage 4 may test only C1. Do not import bilateral weakest-link/free-riding, coalition-dependent implementation costs, government compatibility floors, trade policy, private bypass, switching costs, dynamics, installed bases, directional link matrices, topology, or additional countries to rescue C1.

If C1 fails, report failure and return to Stage 3 before testing C2.

## D-024 — Stage 3 verdict

Date: 2026-09-04
Decision: `GO` → `GO TO MINIMAL MODEL`

Stage 3 identified one minimal implementable mechanism with a coherent full-game feedback and a diagnostic parameter region consistent with implementation-induced stability reversal. The diagnostic is not a theorem; Stage 4 must derive the effect from a genuine product-market model and kill C1 if it only smooths B0 or requires engineered curvature.

## D-025 — Stage-4 exact implementation ordering

Date: 2026-09-04
Decision: VERIFIED / C1 PREDICTION REJECTED

For the frozen one-sided Stage-4 demand primitive, the symmetric implementation equilibrium satisfies

`a_IS* >= a_SU*`

on the audited regular domain `0<v<=1/4`, with strict inequality unless both regimes are at full implementation.

Exact reason:

`K_I(a)/K_U(a)=2(3-va)/3>1`,

and both equilibrium maps are strictly decreasing in `a`.

Thus the model produces coalition-scope implementation crowd-in, not the selected CSIC crowd-out effect.

## D-026 — One-sided implementation demand fails the welfare microfoundation

Date: 2026-09-04
Decision: REJECTED AS CANONICAL WELFARE PRIMITIVE

Under the frozen inverse-demand primitive,

`partial p_i/partial q_j - partial p_j/partial q_i = v(a_i-a_j)`

for formal partners. Since implementation best responses require unilateral deviations with `a_i != a_j`, the inverse-demand system is not globally integrable into a `C^2` quasilinear representative utility.

Therefore `CS_i` and hence `W_i=CS_i+Pi_i` are not globally microfounded under C1 as written.

A bilateral repair would be a substantive mechanism change and is not authorized in Stage 4.

## D-027 — Reject the apparent full-implementation stability reversal

Date: 2026-09-04
Decision: REJECTED AS MECHANICAL

An equilibrium-consistent symmetric welfare diagnostic gives

`Delta_3^endo>0`

throughout `0<v<=1/4`, `kappa>0`.

A sign reversal arises only relative to a benchmark that mandates `a=1` and forces the IS firm to bear `kappa/2`:

`Delta_3^full,cost=7v/[8(2-v)]-kappa/2`.

When full interoperability is instead a costless/exogenous technological benchmark,

`Delta_3^full,tech=7v/[8(2-v)]>0`,

and no reversal exists.

The observed reversal is therefore implementation-cost avoidance, not the Stage-3 reach-versus-competition-exposure mechanism.

## D-028 — Stage 4 verdict for C1

Date: 2026-09-04
Decision: `NO-GO`

C1 is terminated.

Reasons:

1. its headline implementation crowd-out prediction is analytically false under the frozen primitive;
2. the intended competition-exposure channel is absent from own implementation incentives;
3. the one-sided inverse-demand system lacks a coherent off-equilibrium consumer-surplus microfoundation;
4. the only sign reversal is benchmark-cost accounting, not a new full-game strategic result.

Do not proceed to Stage 5 or Stage 6 from C1.

Any continuation must re-enter Stage 3 and explicitly select/redesign a genuinely distinct mechanism before further modeling.

## D-029 — Stage 3 re-entry verdict for C2

Date: 2026-09-04
Decision: `NO-GO`

C2 — bilateral implementation public-good/free-riding — is terminated as a standalone mechanism.

The strongest natural smooth bilateral technology `A_ij=a_i+a_j-a_i a_j` repairs C1's consumer-surplus integrability problem but gives stronger implementation incentives under IS than SU. Independent bilateral links do not create regime-dependent per-link implementation, and standard public-good free-riding does not make aggregate provision fall with coalition size under conventional assumptions. A 6,000-point diagnostic found no `a_IS<a_SU`, no `Delta_3<0`, and no reversal against costless full interoperability.

Do not proceed to Stage 4 on C2.

## D-030 — Stage 3 re-entry verdict for C-RP

Date: 2026-09-04
Decision: `NO-GO`

C-RP — Relative-Profit-Induced Interoperability Restraint — is terminated as a standalone mechanism.

Use the fixed global objective

`U_i=Pi_i-(alpha/2)sum_{j!=i}Pi_j`, `0<=alpha<1`,

rather than a coalition-dependent comparator.

The candidate preserves the bilateral welfare microfoundation but fails its strategic-feedback test. When RP is applied only to implementation while ordinary-profit Cournot is held fixed, the exact IS/SU implementation marginal-return ratio remains

`2/(1+z)`, `z=v(2a-a^2)`,

and is independent of `alpha`. Thus the direct rival-profit penalty does not create a regime-differential restraint. When RP is applied consistently to both implementation and quantity choices, the IS/SU marginal-return ratio remains above one and is weakly larger than at the profit-maximizing baseline over the audited regular domain.

A 6,000-point diagnostic over `v in [0.005,0.25]`, `alpha in [0,0.95]`, `kappa in [10^-3,10]` found zero cases of `a_IS<a_SU`, zero `Delta_3<0`, zero stability reversals relative to `alpha=0`, and zero reversals relative to costless full interoperability.

Prior-art pressure is also substantial because Matsumura–Matsushima–Cato already study two-stage R&D under relative profit, Shibata adds R&D spillovers to a relative-profit competition parameter, and Sun–Zhao study RPE with effort spillovers in networks.

Therefore the user-authorized `Stage 3R GO -> Stage 4` condition is not met. Do not execute Stage 4 for C-RP. Any further continuation requires a genuinely distinct Stage-3 mechanism.

## D-031 — Authorize C-ESD as a genuinely distinct Stage-3 pivot

Date: 2026-09-04
Decision: ACCEPTED FOR STAGE-3R TEST

C-ESD — Endogenous Standard Differentiation × Strategic Product Repositioning — is not a repair of C1, C2 or C-RP. Its strategic margin is government-controlled standard differentiation followed by firm product positioning.

For C-ESD, D-019's private-implementation target is superseded by the distinct loop

`rho -> government standard-friction policy -> product location -> downstream competition -> national welfare -> coalition stability`.

Stage-2 ingredient-level novelty restrictions remain binding.

## D-032 — Kill simple Hotelling policy-to-location mechanism

Date: 2026-09-04
Decision: KILLED

Under full-coverage quadratic Hotelling,

`pi1=t(x2-x1)(2+x1+x2)^2/18`,

so `t` is a multiplicative scale factor in the location objective. Firm location best responses do not depend on `t`.

A symmetric two-firm network extension also leaves the exact symmetric location gradient unchanged.

Do not proceed with a two-firm Hotelling model in which policy only changes a common transport coefficient.

## D-033 — Verify SU-specific Salop strategic repositioning

Date: 2026-09-04
Decision: VERIFIED STAGE-3 DIAGNOSTIC

For a three-firm Salop network diagnostic, equal spacing has zero unilateral location gradient under IS and SW. Under `SU12`, setting `r=v/t`, the member-1 normalized gradient is

`r(3r-2)(12r-7)/[6(2r-1)(6r-5)^2] < 0`

for `0<r<1/2`.

The gradient becomes more negative as `r` rises. Thus deeper standardization/lower `t` strengthens outward repositioning of compatible SU members.

This is a genuine regime-specific feedback not present in the killed two-firm models.

## D-034 — Anchored product positions are admissible only as a substantive primitive

Date: 2026-09-04
Decision: CONDITIONALLY ADMISSIBLE

Inherited brand/technology anchors with redesign cost

`gamma(x_i-h_i)^2/2`

may regularize the location game if interpreted as a real product-architecture/brand repositioning friction.

The cost is not a novelty claim and may not be calibrated merely to manufacture interiority or a stability reversal. Global best responses, ordering changes, corners and alternative cost forms must be audited at Stage 4 if C-ESD reaches it.

## D-035 — Reject literal B0 = fixed-t nesting claim

Date: 2026-09-04
Decision: REJECTED AS CURRENTLY STATED

The frozen B0 model has no literal Hotelling/Salop `t` or endogenous product-location stage. It uses network-value demand, incompatible-product marginal cost `c`, and binary private adoption with fixed cost `F`.

C-ESD may use B0 as the mandatory structural/institutional IS/SU/SW coalition benchmark. Do not claim exact algebraic nesting until a defensible continuous-policy-to-B0 mapping is established.

## D-036 — Stage 3R C-ESD verdict

Date: 2026-09-04
Decision: `CONDITIONAL GO` — REMAIN AT STAGE 3

The firm-side mechanism survives: three-firm SU compatibility-network asymmetry creates an exact `t`-dependent strategic repositioning force, and an anchored numerical witness gives `dx*/dt != 0`.

Stage 4 is not authorized because one architecture choice remains unresolved:

**the regime-neutral policy/benchmark mapping from IS/SU/SW plus one continuous standardization intensity into within-bloc and cross-bloc standard-induced frictions, together with the government/bloc decision rule.**

This mapping must define national welfare and coalition deviations without arbitrary regime-specific primitives and clarify the relationship to the exogenous-policy/B0 benchmark.

If the mapping survives and the FULL model produces a coalition-stability result unavailable from fixed-location and fixed-policy benchmarks, promote C-ESD to Stage 4. Otherwise terminate C-ESD.

Do not add relative profit, private implementation, dynamics, topology choice or other policy instruments during the conditional gate.