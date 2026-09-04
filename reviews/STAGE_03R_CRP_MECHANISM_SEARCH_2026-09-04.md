# Stage 3 Re-entry — C-RP Relative-Profit-Induced Interoperability Restraint

Date: 2026-09-04
Repository: `ryotamatsuki/endogenous-interoperability-standards-coalitions`
Workflow: `ryotamatsuki/research-paper-workflow` v1.1
Release SHA: `488e5ab06c207909296a7564eaf9066f7f94319c`

## 1. Executive verdict

**Canonical verdict: `NO-GO`.**

**Route: remain at Stage 3; do not execute Stage 4 for C-RP.**

C-RP was a plausible response to the failures of C1 and C2 because interoperability can raise rival firms' profits, while a relative-profit firm dislikes rival gains. The mechanism survives the consumer-surplus integrability test but fails the strategic-feedback test.

With a fixed global reference set and the natural integrable bilateral technology `A_ij=a_i+a_j-a_i a_j`, relative-performance concern does not make implementation weaker under the broader IS coalition than under SU. The direct relative-profit implementation-spillover effect cancels from the IS/SU marginal-return ratio when the downstream Cournot stage is held fixed. When relative profit is applied consistently to both implementation and quantity decisions, the larger-coalition implementation advantage becomes stronger, not weaker.

A 6,000-point full-game diagnostic found zero cases of the desired implementation ordering or stability reversal.

## 2. Candidate and feedback loop

Candidate name: **C-RP — Relative-Profit-Induced Interoperability Restraint**.

Intended loop:

`formal coalition -> interoperability spillovers to rivals -> relative-profit penalty -> regime-specific implementation -> product competition -> national welfare -> government stability`.

Firm objective:

`U_i=Pi_i-(alpha/2)sum_{j!=i}Pi_j`, `0<=alpha<1`.

The reference set is fixed globally. Coalition-dependent reference groups were rejected ex ante because they would change firm preferences mechanically when a country changes formal coalition.

Government objective remains

`W_i=CS_i+Pi_i`.

## 3. Targeted prior-art mini-search

C-RP enters a heavily occupied investment/spillover literature.

### Matsumura, Matsushima and Cato (2013)

`Competitiveness and R&D competition revisited`, Economic Modelling 31:541-547, DOI `10.1016/j.econmod.2012.12.016`.

The paper studies a two-stage R&D game in which firms maximize relative profit, finds a non-monotone relation between competitiveness/relative-profit weight and R&D, and extends the analysis to oligopoly and joint R&D.

Implication: `relative profit changes strategic investment` is old.

### Shibata (2014)

`Market structure and R&D investment spillovers`, Economic Modelling 43:321-329, DOI `10.1016/j.econmod.2014.08.014`.

This paper explicitly extends Matsumura et al. by adding R&D spillovers and formulates the firm objective as own profit minus a fraction of rival profit.

Implication: `relative-profit objective x investment spillover` is already direct prior art at the component/mechanism level.

### Sun and Zhao (2024)

`Relative performance evaluation in spillover networks`, Games and Economic Behavior 145:285-311, DOI `10.1016/j.geb.2024.03.009`.

This paper studies effort spillovers together with relative-performance compensation in a networked multi-agent contracting problem.

Implication: spillover structure interacting with RPE is an active general mechanism family.

### Other occupied components

- Hotelling competition with RPE already studies product differentiation under relative performance.
- Relative-performance strategic competition in product markets is longstanding.
- Knowledge-spillover Cournot models with relative-profit maximization also exist.

Therefore C-RP could survive only through a new government standards-coalition continuation/stability result, not through its ingredients.

## 4. Minimal architecture

Three firms/countries. Regimes:

- `IS={{1,2,3}}`;
- `SU_12={{1,2},{3}}`.

Bilateral effective interoperability:

`A_ij=a_i+a_j-a_i a_j`.

Inverse demand in each national market:

`p_i=1-Q+v sum_{j in C_i(rho),j!=i}A_ij q_j`.

Implementation cost:

`kappa a_i^2/2`.

Firm objective:

`U_i=Pi_i-(alpha/2)sum_{j!=i}Pi_j`.

Timing:

`rho -> a -> q -> W -> stability`.

## 5. Consumer-side integrability

Because `A_ij=A_ji`,

`partial p_i/partial q_j = partial p_j/partial q_i = -1+vA_ij`.

A quasilinear representative consumer utility exists:

`U_cons(q;a)=Q-Q^2/2+v sum_{i<j}A_ij q_i q_j`.

Thus C-RP repairs C1's off-equilibrium consumer-surplus defect.

## 6. Reduced-form exact diagnostic under consistent full RP

Let

`z=v(2a-a^2)`.

At a symmetric implementation profile, the RP-Cournot continuation quantities are:

### IS

`q_I=1/[4-alpha-(2-alpha)z]`.

### SU

`q_M=(alpha+2)/[8-4z+2alpha(1+z)-alpha^2]`,

`q_O=[2-2z+alpha(1+z)]/[8-4z+2alpha(1+z)-alpha^2]`.

The exact symmetric implementation marginal returns, before the term `kappa a`, are:

`MB_I = 3 v (2-alpha)(1-a)[2+alpha(1-z)][4+alpha(alpha-2)(1-z)] / {[4-2z-alpha(1-z)]^3 [2+2z+alpha(1-z)]}`,

`MB_U = 3 v (2-alpha)(1-a)(alpha+2)^3(alpha^2-2alpha+4) / {2[8-4z+2alpha(1+z)-alpha^2]^3}`.

At `alpha=0`,

`MB_I/MB_U=2/(1+z)`,

which exactly recovers the C2 marginal-return ordering.

A dense interval grid over `alpha in [0,0.999]`, `z in [0,1/4]` found the minimum ratio equal to `1.6`, at the profit-maximizing baseline. The ratio rises toward approximately 2 as `alpha` becomes large in the regular range.

Diagnostic conclusion: consistent relative-profit competition does not generate `MB_I<MB_U`; it strengthens the broader-coalition implementation incentive relative to SU.

## 7. Artifact benchmark — isolate direct rival-profit penalty

The proposed economic intuition was that interoperability raises rival profit and relative-profit firms therefore restrain implementation more in a larger coalition.

To isolate exactly this channel, freeze the downstream product-market equilibrium at ordinary-profit Cournot and apply relative profit only to the implementation-stage evaluation.

Then

`MB_I^impl = 3v(1-a)(2-alpha z)/[2(1+z)(2-z)^3]`,

`MB_U^impl = 3v(1-a)(2-alpha z)/[4(2-z)^3]`.

Therefore

`MB_I^impl/MB_U^impl = 2/(1+z)`.

The relative-profit parameter `alpha` cancels exactly.

This is the decisive kill result for the proposed mechanism. The direct rival-profit penalty does not create the regime-differential implementation effect required by C-RP. The only new effect from applying RP consistently is the familiar tougher product-market competition channel, and that channel moves the IS/SU implementation ratio in the wrong direction.

## 8. Numerical full-game diagnostic

Artifact: `verification/stage03r_crp_diagnostic.py`.

Grid:

- 20 values of `v` in `[0.005,0.25]`;
- 10 values of `alpha` in `[0,0.95]`;
- 30 log-spaced values of `kappa` in `[10^-3,10]`;
- 6,000 valid points.

Results:

- `a_IS<a_SU`: **0**;
- `Delta_3^endo<0`: **0**;
- stability reversal relative to the same endogenous model at `alpha=0`: **0**;
- stability reversal relative to costless/exogenous full interoperability at the same `alpha`: **0**.

The minimum observed `a_IS-a_SU` remained positive. The minimum `Delta_3^endo` remained positive and approached zero only where interoperability itself became economically negligible.

Numerics support the Stage-3 mechanism rejection but are not presented as a global impossibility theorem.

## 9. Candidate-proposition kill table

| Candidate proposition | Diagnostic result | Status |
|---|---|---|
| Bilateral C-RP preserves a coherent CS/welfare microfoundation | Symmetric cross partials | `SURVIVES` |
| RP penalizes rival-profit spillovers from implementation | Yes at the objective level | `SURVIVES AS INGREDIENT` |
| The direct RP implementation penalty is stronger under IS relative to SU | IS/SU ratio independent of alpha when product stage is fixed | `REJECTED` |
| Full RP can generate `a_IS<a_SU` | No signal; exact marginal-return ratio remains >1 on regular grid | `REJECTED` |
| C-RP can make `Delta_3<0` in the diagnostic domain | 0/6000 | `REJECTED` |
| C-RP creates stability reversal vs alpha=0 | 0/6000 | `REJECTED` |
| C-RP creates reversal vs costless full interoperability | 0/6000 | `REJECTED` |
| Full-game result exceeds known RP-investment-spillover components | No surviving stability result | `REJECTED` |

## 10. Why alternative C-RP variants are not authorized rescues

### Coalition-dependent reference group

Using only formal coalition partners in the relative-profit comparator would mechanically change preferences when coalition membership changes. It also creates an endogenous-peer/reference-set mechanism distinct from C-RP. Rejected as a rescue.

### Endogenous alpha / managerial contracting

Allowing owners or boards to choose the RPE weight adds a delegation/contracting stage and moves toward the RPE-contract literature. This is a distinct mechanism.

### Capacity, scope cost, dilution, shared gateway

These were already identified after C2 as distinct mechanism families. Combining them with RP would not test C-RP alone.

## 11. Nested benchmark comparison

- `alpha=0` recovers the smooth bilateral C2 diagnostic exactly.
- Fixing implementation exogenously leaves an RP-Cournot standards-regime comparison, but no new implementation feedback remains.
- Applying RP only at implementation leaves the IS/SU implementation ratio unchanged from C2.
- Removing the government stability stage yields a standard relative-profit strategic-investment problem, directly exposed to Matsumura–Matsushima–Cato and Shibata.

The full architecture therefore fails the Stage-3 generalization test: no new qualifying stability result survives the interaction.

## 12. Canonical verdict

`NO-GO`

C-RP is terminated as a standalone mechanism candidate.

## 13. Routing / next-stage contract

Do **not** execute Stage 4 for C-RP because the user-authorized condition was `Stage 3R GO -> Stage 4` and the Stage-3R verdict is `NO-GO`.

Remain at Stage 3. Any continuation must compare a genuinely distinct mechanism, such as shared interoperability infrastructure/gateway or another candidate, against the prior-art and minimality constraints. Do not combine C-RP with those mechanisms without a fresh Stage-3 selection.