# Revival Stage 3 — Candidate Mechanism Matrix

Date: 2026-09-10

Branch: `revival/stage00-coalition-repositioning`

Workflow: `ryotamatsuki/research-paper-workflow` v2.1 at `f48984013898696f010f0437a8cfed6b5b54bdc2`.

Binding inputs:

- `reviews/STAGE_01_REVIVAL_SOURCE_MATHEMATICAL_AUDIT_2026-09-10.md`;
- `reviews/STAGE_02_REVIVAL_NOVELTY_GATE_2026-09-10.md`;
- `docs/REVIVAL_STAGE2_PRIOR_ART_MATRIX_2026-09-10.md`.

## 1. Search objective

The search is not for a parameterization under which `SU > IS`. It asks which **single minimal economic mechanism**, if any, can make post-policy product repositioning survive endogenous standards-depth adjustment and have a coalition-stability consequence unavailable in fixed-position and exogenous-depth benchmarks.

The Stage-1 blocker is structural in PR #65: coalition membership activates the full network/compatibility term through `G(rho)`, while continuous depth changes `Tau(rho,s)` and hence competitive substitutability but does not increase realized interoperability. Under symmetric IS this makes welfare strictly decrease with depth and yields `s_I*=0`.

## 2. Ex-ante scoring rule

Weights are fixed before ranking:

- whole-game novelty / prior-art survival: 25;
- mechanism clarity: 15;
- minimality and analytical tractability: 20;
- welfare / coalition-stability leverage: 15;
- institutional plausibility: 10;
- empirical bridge: 5;
- referee defensibility: 10.

Total: 100.

Scores are architecture-screening judgments, not evidence that the desired theorem exists.

## 3. Candidate table

| ID | Candidate | Minimal strategic logic | Score / 100 | Gate view |
|---|---|---|---:|---|
| C1 | **Realized interoperability depth** | The same bloc depth that compresses standard-based differentiation also raises the fraction/intensity of interoperability actually realized within the bloc. Repositioning can then reduce the competitive cost of deeper interoperability and change bloc policy incentives. | **92** | TOP 1 |
| C2 | Multi-market common standard | One common bloc depth applies across several markets while firms can reposition differently by market; a single policy instrument cannot generally absorb all downstream competitive responses. | 82 | TOP 2, high complexity |
| C3 | Home-market incidence / asymmetric national surplus | Repositioning changes the incidence of consumer and producer gains across countries, so a common bloc depth cannot neutralize every member's incentive simultaneously. | 77 | TOP 3, heterogeneity risk |
| C4 | Heterogeneous redesign flexibility | Firms differ in repositioning cost; standards depth induces asymmetric repositioning and member-specific coalition payoffs. | 73 | reject as leading mechanism |
| C5 | Internal coalition depth conflict | Members have distinct preferred common depths, and repositioning changes those preferred depths and participation constraints. | 72 | requires another source of asymmetry |
| C6 | Installed-base / coalition-size nonlinear interoperability | The value of deeper interoperability depends on coalition size or installed base, potentially creating size-dependent policy feedback. | 71 | curvature / network-literature risk |
| C7 | Sequential accession after depth commitment | A bloc sets depth before an outsider chooses whether to accede; repositioning changes accession incentives and commitment value. | 68 | timing complexity, not minimal |
| C8 | Endogenous standard technical direction | A coalition chooses not only depth but the characteristic center/direction of a standard, after which firms reposition. | 66 | adds a second strategic policy dimension |
| C9 | Firm implementation/compliance effort before repositioning | Firms choose effective implementation intensity after bloc depth and before product positioning. | 64 | close to Klimenko / Guo-Liu-Nault and adds an action layer |
| C10 | Scope × depth two-dimensional standardization | Coalition chooses which attributes are common and how deeply, while firms reposition on residual attributes. | 61 | strong overlap with own SSDI and excessive dimensionality |

## 4. Candidate details

### C1 — Realized interoperability depth

**One-sentence mechanism.** Formal coalition membership creates the institutional possibility of interoperability, but technical depth determines how much interoperability is actually realized; the same depth also compresses differentiation, and firms may reposition to mitigate that competitive cost.

**Feedback loop.** `coalition -> depth -> realized interoperability + competitive compression -> repositioning -> effective substitutability -> optimal depth -> national welfare -> coalition stability`.

**Endogenous margins.** Bloc depth, firm product locations, prices, coalition blocking.

**Minimum new primitive.** Replace the PR #65 depth-invariant off-diagonal compatibility/network term with a monotone within-bloc realization map `chi(s_C)` using the *same* scalar depth already present. No new action or player is required.

**Closest threats.** Klimenko (continuous compatibility policy), Woeckener (compatibility before location), Huang–Tan–Teh–Zhou (interoperability strength/configuration), SSDI (continuous standardization -> downstream response -> policy reversal).

**Expected nontrivial result class.** An absorption/non-absorption condition comparing the marginal interoperability benefit of depth with its marginal competition effect; endogenous repositioning shifts that condition and may shift a blocking/stability threshold relative to `B-FIX`.

**Welfare content.** Direct interoperability gains, consumer-surplus/competition effect, profits, repositioning costs, national incidence, coalition stability.

**Interpretation.** Technical standards vary in completeness, protocol coverage, conformance specificity, implementation fidelity, backward compatibility, and cross-vendor functionality. A nominal agreement need not deliver full interoperability at zero depth.

**Tractability risk.** Low to moderate: the source affine-demand structure can be retained and the new channel enters one pairwise term.

**Fatal referee attack.** "You added a direct benefit solely to stop `s_I=0`." Stage 4 must defeat this by treating `chi(s)` as the technical meaning of depth, using a simple pre-specified form, and proving a FULL-only interaction result rather than relying on positive depth itself.

### C2 — Multi-market common standard

**Mechanism.** A single international standard depth applies across markets, while product positioning and competitive pressure can differ by market; one policy instrument is therefore generically insufficient to undo all repositioning effects.

**Loop.** `coalition -> common depth -> market-specific repositioning -> market-specific competition -> aggregated national welfare -> depth -> coalition`.

**New primitive.** A second market/segment with a common standards policy and market-specific product positioning.

**Threats.** International harmonization/trade models, multiproduct/multimarket repositioning, coalition policy with common instruments.

**Expected result.** Instrument-insufficiency theorem or threshold showing that fixed-position and endogenous-position coalition rankings differ because the common depth cannot neutralize heterogeneous market responses.

**Welfare.** Strong.

**Interpretation.** Telecom/API/charging standards are shared across national or application markets even though competitive positioning differs locally.

**Risk.** State space and continuation burden roughly multiply; easy referee attack is that complexity, not the standards mechanism, generates the result.

**Targeted literature check.** Casella's standards-coalition work and Schmidt–Steingress harmonization/trade work confirm that standards span countries/products and affect adaptation costs, but the Stage-2 search did not identify the same common-depth + market-specific repositioning + coalition-stability theorem. This does not establish novelty; it only keeps C2 viable as a fallback architecture.

### C3 — Home-market incidence / asymmetric national surplus

**Mechanism.** Product repositioning changes where surplus accrues, so bloc aggregate policy adjustment cannot generally make every prospective member indifferent in the same way.

**Loop.** `coalition -> depth -> repositioning -> home/foreign demand incidence -> heterogeneous national welfare -> common-depth choice -> blocking`.

**New primitive.** Home bias or unequal national consumer weights.

**Threats.** International IO/trade models with home bias and standards; generic asymmetric coalition models.

**Expected result.** Repositioning changes which pair can block or changes the member participation constraint before it changes aggregate bloc welfare.

**Welfare.** Strong, with explicit distributional incidence.

**Interpretation.** Countries differ in domestic installed base, demand composition, or ownership exposure.

**Risk.** The referee may view the result as ordinary asymmetry. It is unacceptable if the only purpose of home bias is to split otherwise equal payoffs.

### C4 — Heterogeneous redesign flexibility

**Mechanism.** Different `gamma_i` values create asymmetric strategic adaptation and coalition payoffs.

**Why rejected as leader.** The workflow explicitly warns that "another heterogeneity parameter" is not a mechanism by itself. Without an independently motivated strategic interaction, C4 risks being result-by-heterogeneity.

### C5 — Internal coalition depth conflict

**Mechanism.** Repositioning changes member-specific preferred depths and therefore whether a common standard can satisfy all members.

**Why not selected.** Under the symmetric source architecture members have identical objectives, so policy conflict requires an additional asymmetry or bargaining/consent primitive. It therefore needs at least two changes to become active.

### C6 — Installed-base / coalition-size nonlinear interoperability

**Mechanism.** The marginal benefit of depth rises or falls with coalition size/installed base.

**Why not selected.** It can easily become curvature engineering. Network-size effects are also central in established standards literature. A clean result would be possible, but C1 captures the missing direct interoperability meaning of depth more minimally.

### C7 — Sequential accession after depth commitment

**Mechanism.** Depth is a commitment instrument that affects outsider accession after firms reposition.

**Why not selected.** It changes the coalition-formation protocol and adds history dependence before the baseline interaction has been exhausted. Stage 3 prohibits dynamics/timing merely to obtain a desired result.

### C8 — Endogenous standard technical direction

**Mechanism.** Governments choose a standard's location/direction in characteristic space and firms reposition around it.

**Why not selected.** The second policy dimension creates a potentially interesting new paper but is not a minimal repair of the audited absorption puzzle.

### C9 — Firm implementation/compliance effort

**Mechanism.** Effective interoperability depends on post-policy firm implementation effort.

**Why not selected.** This inserts another endogenous stage and approaches Klimenko and Guo–Liu–Nault. The whole-game novelty burden becomes harder, not easier.

### C10 — Scope × depth

**Mechanism.** Governments choose the set of standardized attributes and harmonization depth, after which firms reposition on residual attributes.

**Why rejected.** It is too close to the author's SSDI research program on standardization scope and downstream strategic reallocation and requires a two-dimensional policy problem. It risks both self-overlap and uncontrolled complexity.

## 5. TOP 3 deep-dive ranking

### TOP 1 — C1 Realized interoperability depth

Reasons:

1. directly addresses the Stage-1 economic defect rather than the numerical sign;
2. uses the already-existing depth variable rather than adding a player or action;
3. produces a natural marginal-benefit / marginal-competition trade-off;
4. creates a specific role for repositioning: firms can attenuate the competitive cost of deeper interoperability;
5. admits clean fixed-position versus endogenous-position nested benchmarks;
6. offers an interpretable absorption/non-absorption threshold without requiring asymmetry.

### TOP 2 — C2 Multi-market common standard

Strongest backup because it creates a genuine policy-instrument insufficiency mechanism. It is not selected because continuation, welfare, and coalition-stability complexity are much higher.

### TOP 3 — C3 Home-market incidence

Strong coalition-stability leverage because blocking depends on individual national payoffs. It is not selected because the mechanism can collapse into generic asymmetry unless an independent empirical/institutional reason is built in.

## 6. Preferred candidate

**C1 — REALIZED INTEROPERABILITY DEPTH.**

The preferred redesign does not add a separate "benefit parameter" to rescue the old result. It changes the technical interpretation of the already-existing depth variable so that formal membership and realized interoperability are not identical objects.

A minimal implementation is:

- retain one depth `s_C` for each standards bloc;
- retain the existing pairwise friction map `Tau(rho,s)` as the competitive/adaptation side of standard depth;
- for two firms in the same multi-country bloc, let realized compatibility/network intensity be `chi(s_C)`, where `chi` is increasing and bounded;
- across different blocs, retain zero cross-bloc compatibility in the minimal baseline;
- retain costly product positioning and the affine-demand Bertrand continuation.

Stage 4 should start with the simplest pre-specified normalization, preferably a linear realization map after normalizing depth to `[0,1]`. Nonlinearity is robustness only and may not be used to manufacture a reversal.

## 7. Reduced-form coherence check

Under symmetric IS and fixed anchor positions, write the common off-diagonal effective curvature as

`c(s) = c0 + lambda*phi_bar/(t_bar-s) - v*chi(s)`.

From Stage 1,

`dW_IS/dc < 0`.

Therefore

`dc/ds = lambda*phi_bar/(t_bar-s)^2 - v*chi'(s)`

creates a genuine marginal trade-off:

- if the competitive-compression term dominates, deeper standardization raises effective substitutability and policy adjustment tends toward the lower-depth boundary;
- if the interoperability-realization term dominates, deeper standardization can reduce effective substitutability / increase consumer compatibility value and the lower-bound result need not hold.

With endogenous repositioning, `phi_bar` is replaced by `phi(x_i(s)-x_j(s))`. When firms move apart after deeper standardization, the induced reduction in proximity can attenuate the marginal competitive cost of depth. This creates a FULL-only term in the bloc policy derivative that is absent when positions are fixed.

This sign logic is sufficient for Stage 3 coherence. It is **not** a Stage-4 theorem and does not imply that a coalition reversal exists.

## 8. Required Stage-4 kill tests for C1

C1 proceeds only if all of the following survive:

1. the affine demand/price continuation is globally valid on the new policy-location domain;
2. `chi(s)` has an independent technical interpretation and is fixed before looking for a reversal;
3. a nonzero repositioning response occurs over an open parameter region;
4. `B-FIX` and `FULL` choose different depth or have different blocking incentives because of repositioning, not because `chi(s)` alone changes the old ranking;
5. at least one coalition-stability threshold, blocking comparison, or stable partition differs between `B-FIX` and `FULL` on a nondegenerate region;
6. removing endogenous positioning destroys that headline result;
7. the result is not obtainable from the SSDI policy-reversal logic by relabeling R&D allocation as product location;
8. no parameter search is allowed to use `SU stable` or `SU > IS` as the optimization target.

## 9. Matrix verdict

**ONE PREFERRED MINIMAL MECHANISM SURVIVES: C1 REALIZED INTEROPERABILITY DEPTH.**

Route to Stage 4 Minimal Model. C2 and C3 are retained only as documented rejected/back-up architectures and may not be mixed into C1 during Stage 4.