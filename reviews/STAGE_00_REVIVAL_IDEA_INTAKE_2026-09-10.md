# Stage 0 — Revival Idea / Motivation Intake

Date: 2026-09-10

> Canonical authority: `ryotamatsuki/research-paper-workflow/GOVERNANCE.md` -> `THEORY_PAPER_RESEARCH_PIPELINE.md` -> `templates/STAGE_00_IDEA_INTAKE.md`.
>
> Workflow version: v2.1, authority commit `f48984013898696f010f0437a8cfed6b5b54bdc2`.

## 1. Executive verdict

**GO TO AUDIT.**

The terminated historical paper should not be revived as-is, but the residual economic question remains researchable and nontrivial. The strongest surviving puzzle is not whether compatibility can induce later differentiation; that broad mechanism is already close to prior art. The live question is whether, once standards blocs can themselves optimally choose standards depth, firms' post-policy product repositioning can still alter the equilibrium set or stability of standards coalitions.

The PR #65 branch provides a useful starting source because it shows a reproducible fixed-depth welfare reversal, while the 2026-09-10 diagnostic indicates that endogenous policy adjustment absorbs that reversal at the canonical witness. This creates a concrete falsifiable puzzle rather than a desired conclusion.

No new model primitive is selected at Stage 0.

## 2. Project context

- Historical working title: **Standards Coalitions and Strategic Product Repositioning**
- Revival working title: **Standards Coalitions, Policy Adjustment, and Strategic Product Repositioning**
- Research topic: international / intergovernmental standards coalitions with endogenous standards depth and post-policy firm product repositioning
- Source branch: PR #65 / `stage04r4a-affine-demand-bertrand-novelty`
- Source head: `9f19a82e28415b571a086693323a3377f286fd73`
- Revival branch: `revival/stage00-coalition-repositioning`
- Contemplated historical journal family: industrial organization / standards / coalition formation; IJIO is context only, not a design target at this stage

## 3. Phenomenon vs proposed explanation

### 3.1 Phenomenon

Standards cooperation changes more than compatibility. After governments or standards blocs choose a standards regime and its depth, firms may adjust product characteristics to soften or redirect subsequent product-market competition.

The PR #65 source architecture shows that, at a fixed positive standards depth, allowing firms to reposition can reverse an SU-member's welfare ranking between a bilateral standards union and international standardization.

However, once the standards-depth instrument is itself returned to the policy game, the international-standardization bloc can adjust its depth. At the canonical witness this policy response removes the fixed-depth welfare reversal before it becomes a coalition-stability reversal.

### 3.2 Proposed explanation

The working explanation is **policy-adjustment absorption**: an upstream bloc-level policy instrument may substitute for, offset, or neutralize the downstream competitive effect created by endogenous product repositioning.

This explanation is provisional. Stage 1 must determine whether the absorption result is a genuine structural property, a local numerical feature, or an artifact of the inherited PR #65 primitives.

## 4. Actors / decisions / frictions / outcomes

### Actors

- governments / standards blocs;
- one national firm associated with each country in the minimal three-country architecture;
- consumers represented by the inherited quadratic-utility demand system in the source model.

### Decisions

- coalition / standards partition;
- bloc standards depth;
- firm product repositioning;
- downstream prices.

### Frictions

- standards-induced adaptation / differentiation friction;
- network / compatibility effects;
- costly product repositioning;
- strategic interaction between bloc policy and firm design.

### Outcomes

- product positions;
- prices and quantities;
- profits and consumer surplus;
- national welfare;
- bloc policy choices;
- blocking incentives and the stable standards-coalition set.

## 5. Theoretical contribution vs application motivation

### Potential theoretical contribution

The candidate contribution is a conditions-for-effectiveness result about **when an endogenous policy instrument absorbs or preserves a downstream strategic-design channel** in coalition formation.

The relevant novelty unit is not the existence of compatibility-induced differentiation. It is the full feedback:

`standards coalition -> endogenous standards depth -> post-policy product repositioning -> Bertrand competition -> national welfare -> coalition blocking/stability`,

with a result showing when repositioning is or is not indispensable for the equilibrium coalition outcome.

### Application / institutional motivation

Technical standards, interoperability agreements, compatibility alliances, platform/API standards, charging standards, communications standards, and related harmonization arrangements often specify both membership and the depth/specificity of common rules. Firms then retain design margins after policy choices are observed. The model seeks a general strategic result rather than a case-specific institutional description.

## 6. Candidate mechanisms

The following are **candidate explanations to audit**, not authorized model changes.

### M1 — Depth-dependent interoperability benefit

A deeper standard may increase realized interoperability or network value, not merely alter product substitutability. If the policy instrument has a genuine direct benefit, the IS bloc may no longer optimally neutralize repositioning by collapsing depth to zero.

Strategic question: does the joint effect of depth on interoperability and design incentives create a coalition-ranking effect that cannot be replicated with fixed product positions?

Risk: if the direct benefit is parameterized solely to prevent `s_I=0`, the mechanism is ad hoc.

### M2 — Market-size or home-market asymmetry

Countries may differ in market size or home demand. Repositioning then changes the distribution of competitive gains and losses across coalition members rather than only aggregate symmetric welfare.

Strategic question: can policy depth no longer offset repositioning for every prospective member simultaneously, generating coalition composition effects?

Risk: generic heterogeneity may produce thresholds without creating a genuinely new strategic mechanism.

### M3 — Heterogeneous repositioning costs

Firms may differ in the cost of redesigning products after a standards agreement. A standards coalition could therefore redistribute competitive pressure toward firms that can or cannot reposition cheaply.

Strategic question: can coalition membership become endogenous to firms' redesign flexibility even after blocs choose standards depth optimally?

Risk: heterogeneity must not directly hard-code the desired coalition ranking.

### M4 — Nontransferable coalition policy conflict

A standards bloc may contain governments with aligned membership but different preferred standards depths because repositioning shifts national profits and consumer surplus differently. A single common depth then creates an internal policy-conflict margin.

Strategic question: does endogenous repositioning change whether a proposed bloc can sustain a common standard when member objectives are not perfectly aggregable?

Risk: bargaining weights or transfers could become arbitrary implementation devices.

### M5 — Installed-base / nonlinear network feedback

The value of compatibility may depend nonlinearly on coalition size or installed base. Repositioning changes competition while network value changes discretely or nonlinearly with coalition composition.

Strategic question: can the interaction generate an open region in which fixed-position and endogenous-position coalition stability differ?

Risk: nonlinear network effects are heavily studied and may absorb novelty or create result-by-curvature.

### M6 — Multi-market repositioning

Standards may be shared across markets while firms reposition products differently across national markets or segments. Policy depth is common but the competitive response is not.

Strategic question: does a common standards instrument fail to offset heterogeneous downstream repositioning responses, leaving a coalition-level residual effect?

Risk: dimensionality and tractability may become disproportionate to the core question.

## 7. Main prior-art risks

Stage 0 treats the following threats as binding inputs to Stage 1/2 rather than re-litigating them here:

- Woeckener (1999): compatibility decisions followed by horizontal product differentiation; generic compatibility-induced differentiation is not a viable headline novelty claim.
- Gabszewicz / Marini / Tarola alliance-formation work: coalition structure can interact with later product differentiation and prices.
- Baake and Boom (2001): compatibility / network effects with endogenous product characteristics and price competition.
- Barrett and Yang (2001): international standards, redesign costs, network effects, and product competition.
- Farahat and Perakis (2010): nonnegative affine-demand Bertrand continuation is infrastructure, not contribution.
- Ushchev and Zenou (2018): network-shaped substitutability and Bertrand outcomes are not themselves novel.
- modern endogenous-product-design / affine-demand work, including the Rodrigues (2026) threat identified in the historical audit.

The surviving novelty question is therefore whole-game and theorem-level, not component-level.

## 8. Evidence that would make the phenomenon economically important

The project becomes economically important only if at least one of the following survives rigorous model and literature audit:

1. there is an open parameter region in which the stable coalition set differs between fixed-product and endogenous-repositioning models after every bloc optimally chooses standards depth;
2. repositioning shifts a coalition-stability threshold in a nontrivial and sign-characterizable way;
3. policy adjustment fully absorbs repositioning under identifiable conditions, but fails under a separate economically interpretable condition, yielding a clean absorption / non-absorption theorem;
4. private coalition stability and social desirability diverge specifically because product repositioning changes incidence across coalition members and outsiders.

A mere nonzero location response, small welfare-level change, or calibrated sign reversal at exogenous policy depth is insufficient.

## 9. Recommended research route

**Theory route.**

The live question concerns equilibrium sequencing, endogenous policy, firm strategic design, welfare, and coalition stability. The immediate task is to establish the structural source of the policy-adjustment absorption result and determine whether any economically defensible mechanism survives the literature frontier. Empirical interpretation can be developed later if the theory yields a clean comparative theorem.

The project should leave the theory pipeline if Stage 1/2 shows that the residual question is either a numerical artifact or already structurally contained in prior work.

## 10. One-sentence falsifiable research question

> **When standards blocs choose standards depth optimally before firms reposition products, under what economically defensible conditions does post-policy product repositioning change the stable standards-coalition set rather than being absorbed by the blocs' policy adjustment?**

This question is falsified as a paper project if the effect is always absorbed in the defensible model class, is an immediate corollary of prior theory, or requires ad hoc primitives / parameter engineering to obtain a coalition reversal.

## 11. Initial literature and source map for Stage 1/2

### Source-model audit family

- PR #65 affine-demand architecture and verification scripts;
- `model/STAGE3R_CESD_POLICY_MAP.md`;
- Stage 4R4A continuation / novelty records;
- Woeckener novelty re-kill record;
- historical Salop continuation failure records;
- canonical terminated main-branch records for comparison only.

### Literature families

- international standardization and standards unions;
- compatibility choice and network externalities;
- endogenous horizontal / vertical product differentiation;
- endogenous product design under Bertrand competition;
- coalition formation and coalition stability;
- standards depth / harmonization intensity;
- policy instruments with downstream strategic adjustment;
- R&D / compatibility alliances when they contain a strategically equivalent feedback.

## 12. Required Stage 1 inputs

Stage 1 must audit at minimum:

1. `decisions/REVIVAL_2026-09-10_DECISION_RECORD.md`;
2. `verification/stage04r4a_affine_bertrand_gate.py`;
3. `verification/stage04r4a_affine_bertrand_ci.py`;
4. `model/STAGE3R_CESD_POLICY_MAP.md`;
5. `reviews/STAGE_04R4A_AFFINE_DEMAND_BERTRAND_CONTINUATION_NOVELTY_2026-09-05.md`;
6. `reviews/STAGE_04R4A_NOVELTY_REKILL_WOECKENER_2026-09-05.md`;
7. the relevant canonical main-branch Stage 4R4B termination record, if distinct from the PR #65 branch;
8. the closest literature needed to interpret any inherited modeling primitive.

Stage 1 must reconstruct from first principles:

- demand / utility and parameter interpretation;
- Bertrand continuation;
- repositioning game;
- bloc standards-depth game;
- welfare accounting;
- strict coalition blocking / stability rule;
- the 2026-09-10 policy-adjustment absorption diagnostic.

In particular, Stage 1 must convert the current numerical absorption diagnostic into repository-reproducible evidence and determine whether `s_I*=0` follows from a structural derivative/sign property or only from the canonical normalization.

## 13. Stage 0 kill-test result

- Descriptive-only project: **PASS** — the question is strategic and welfare-based.
- Known comparative static under a new label: **PASS CONDITIONALLY** — generic compatibility-induced differentiation is known and explicitly excluded; coalition-level policy absorption/non-absorption remains for Stage 2 audit.
- Parameterization exercise: **PASS CONDITIONALLY** — revival is prohibited from searching parameters merely to restore SU dominance.
- Old model with modern labels: **PASS CONDITIONALLY** — Stage 2 must test whole-game absorption.
- No plausible strategic mechanism: **PASS** — policy adjustment and downstream strategic design create a coherent feedback problem.

## 14. Canonical Stage 0 verdict

**GO TO AUDIT.**

## 15. Next-stage contract

Stage 1 may **audit and re-derive** the inherited PR #65 architecture and the policy-adjustment absorption result. It may correct errors, expose missing assumptions, and classify inherited claims.

Stage 1 may **not**:

- add market asymmetry, heterogeneous repositioning costs, depth-dependent network benefits, bargaining, nonlinear network effects, or multi-market structure;
- change the demand system merely to recover a coalition reversal;
- tune parameters until SU becomes stable;
- inherit old Stage 4 / theory-freeze / manuscript / journal-selection passing status.

All candidate mechanisms M1-M6 remain unselected until Stage 2 novelty audit and Stage 3 mechanism search authorize a minimal candidate.
