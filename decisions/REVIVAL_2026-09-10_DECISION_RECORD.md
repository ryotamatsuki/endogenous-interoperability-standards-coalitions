# Revival Decision Record — PR #65 Affine-Demand Branch

Date: 2026-09-10

## 1. Authority and scope

This record opens a **new revival branch** from the historical PR #65 head without changing `main`, without merging PR #65, and without revoking the canonical historical termination on `main`.

- Source repository: `ryotamatsuki/endogenous-interoperability-standards-coalitions`
- Source branch / PR: `stage04r4a-affine-demand-bertrand-novelty` / PR #65
- Source head: `9f19a82e28415b571a086693323a3377f286fd73`
- Revival branch: `revival/stage00-coalition-repositioning`
- Governing workflow: `ryotamatsuki/research-paper-workflow` v2.1
- Workflow authority commit: `f48984013898696f010f0437a8cfed6b5b54bdc2`

Under workflow v2.1, a previous `NO-GO` may be revisited only through a genuinely distinct pivot at the appropriate earlier stage. Negative results, rejected branches, and stale freezes remain preserved. No later-stage certification is inherited by this revival branch.

## 2. Question 1 — Is the PR #65 welfare reversal mathematically real?

### Verdict

**YES AS A STAGE-4 FIXED-DEPTH COMPUTATIONAL RESULT; NOT YET A GENERAL THEOREM.**

The committed PR #65 verifier constructs demand from the quadratic representative-consumer problem, solves the Bertrand continuation, checks direct global one-price deviations at adversarial histories, computes whole-circle product-location best responses, and verifies the following strict member-welfare sign reversal at the frozen Stage-4 witness:

- fixed product positions: `W_1(SU_12)-W_1(IS) < 0`;
- endogenous repositioning: `W_1(SU_12)-W_1(IS) > 0`.

The committed assertions require margins larger than `1e-4` in absolute value and reproduce the sign reversal throughout the pre-specified `3 x 3` local box

`v in {0.07,0.08,0.09}` x `gamma in {0.025,0.030,0.035}`.

The historical canonical approximate values are:

- fixed-depth/fixed-position difference: about `-2.086e-4`;
- fixed-depth/endogenous-position difference: about `+2.664e-4`;
- bilateral-union location equilibrium: approximately `(0.14039, 0.52628, 0.83333)` versus anchors `(1/6,1/2,5/6)`.

Evidence maturity: **repository-reproduced computational witness**, not an analytic theorem over an open parameter domain.

## 3. Question 2 — Was PR #65 abandoned because of a fatal mathematical defect that justified PR #66?

### Verdict

**NO SUCH FATAL DEFECT IS CURRENTLY DOCUMENTED.**

Repository history shows that PR #65 and the later affine-demand redesign leading to PR #66 were parallel descendants of the post-spatial re-foundation rather than a simple correction chain in which #66 fixes a proved defect in #65.

PR #65 itself remains a conditional-go branch: its continuation and nondegenerate repositioning checks passed, while publication-level novelty remained conditional on a coalition-level result. The record does not identify a counterexample invalidating the PR #65 fixed-depth welfare reversal.

Nevertheless, PR #65 has real unresolved burdens that can rationally motivate a cleaner redesign:

1. full continuation validity must be established for every policy history relevant to the endogenous standards-depth game, not only the canonical histories used for the Stage-4 witness;
2. the generic compatibility-to-differentiation mechanism is absorbed by close prior literature, especially Woeckener (1999), so the welfare witness alone is not a sufficient publication contribution;
3. the PR #65 functional form contains more architecture-specific primitives than the later parsimonious affine redesign, increasing theorem and referee-defense burden.

These are **tractability / certification / novelty risks**, not evidence that the PR #65 witness was false.

## 4. Question 3 — Does the PR #65 architecture deliver a stable-coalition reversal once standards depth is endogenous?

### Current diagnostic verdict

**NO AT THE CANONICAL WITNESS; THE STAGE-4 REVERSAL IS ABSORBED BY POLICY ENDOGENEITY.**

A 2026-09-10 independent diagnostic extended the PR #65 architecture conceptually to the policy game specified in `model/STAGE3R_CESD_POLICY_MAP.md`:

`rho -> s*(rho) -> x*(rho,s*) -> p*(rho,s*,x*) -> W -> coalition stability`.

The diagnostic found the following qualitative pattern at the PR #65 canonical parameters:

- under IS, the bloc prefers the lower boundary `s_I = 0`;
- under SU, endogenous repositioning improves member welfare and pushes the bilateral-bloc depth upward, but the resulting member welfare remains below IS welfare once IS is allowed to choose its own depth;
- hence IS is not blocked by the bilateral union at the canonical witness;
- the same qualitative failure was observed across the local `(v,gamma)` box used by PR #65 for its Stage-4 robustness check.

Approximate full-game diagnostic values at the canonical point were:

- `W_i(IS) ~= 0.14348970` at `s_I*=0`;
- `W_member(SU) ~= 0.14320705` at the candidate bilateral-depth equilibrium;
- therefore `W_member(SU)-W_i(IS) ~= -2.83e-4`.

Interpretation: the fixed-depth reversal is real, but IS can undo the disadvantage created by the fixed `s_I=s_bar` comparison by optimally reducing its standards depth. The policy response therefore absorbs the product-repositioning advantage before it becomes a coalition-stability reversal.

### Evidence maturity warning

The numerical values in this subsection originated as an independent diagnostic outside the historical PR #65 verification chain. Under workflow v2.1 they are **not yet a theorem or formal certification**. Stage 1 must reconstruct and commit a reproducible policy-depth diagnostic before these values may support a headline claim. The qualitative failure is the working blocker for the revival, not a frozen theorem.

## 5. Structural blocker opened by this record

The revival does **not** ask how to tune PR #65 until SU wins. The research puzzle is instead:

> Why does endogenous standards-depth adjustment absorb the welfare effect of post-standard product repositioning, and under what economically defensible conditions can repositioning remain consequential for coalition formation after every standards bloc optimizes its policy depth?

Working label: **policy-adjustment absorption problem**.

This label is descriptive and is not yet a proposition.

## 6. What is preserved

Preserve as historical evidence:

- PR #65 demand and Bertrand architecture;
- the fixed-depth repositioning equilibrium;
- the fixed-depth member-welfare reversal;
- the Woeckener novelty re-kill;
- all earlier Salop continuation failures;
- the canonical termination history on `main`.

None of these may be silently rewritten or deleted.

## 7. What is explicitly not inherited

The revival branch does **not** inherit passing status from historical:

- Stage 4 / 4R4A;
- Stage 7.5 / old theory freezes;
- Stage 11 / 11R2;
- Stage 12 journal choice;
- Stage 13 manuscript integration;
- any submission authorization.

The contemplated IJIO route may be remembered as context only. It is not a Stage-0 success criterion and may not distort model design.

## 8. Workflow routing decision

Because the old canonical project terminated and the remaining problem concerns the research question and mechanism architecture rather than one already-authorized primitive change, workflow v2.1 requires re-entry at an earlier stage.

**ROUTE: REVIVAL BRANCH -> STAGE 0 IDEA / MOTIVATION INTAKE.**

Stage 0 must preserve the policy-adjustment absorption puzzle, generate multiple economically distinct candidate explanations, and send a falsifiable research question plus audit plan to Stage 1. It must not select a preferred functional-form repair or search parameters for a desired coalition reversal.
