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
