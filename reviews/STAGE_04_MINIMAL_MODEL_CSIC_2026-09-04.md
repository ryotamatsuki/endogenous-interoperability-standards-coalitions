# Stage 4 — Minimal Model Gate: Coalition-Scope Implementation Crowd-Out

Date: 2026-09-04  
Repository: `ryotamatsuki/endogenous-interoperability-standards-coalitions`  
Canonical workflow: `ryotamatsuki/research-paper-workflow` v1.1  
Workflow release SHA: `488e5ab06c207909296a7564eaf9066f7f94319c`  
Template: `templates/STAGE_04_MINIMAL_MODEL.md`

## 1. Executive verdict

**Canonical verdict: `NO-GO`.**

**Route: terminate C1 and return to Stage 3 before any new mechanism is tested.**

The Stage-3 preferred mechanism, Coalition-Scope Implementation Crowd-Out (CSIC), does not survive the frozen minimal model.

The negative result is strong rather than marginal:

1. the exact implementation game yields `a_IS* >= a_SU*`, not the desired `a_IS* < a_SU*`;
2. the one-sided implementation demand system is not integrable under unilateral implementation deviations, so the stated national consumer-surplus objective lacks a coherent global microfoundation;
3. an implementation-induced stability reversal appears only if the full-implementation benchmark is forced to bear the quadratic implementation cost, in which case the reversal is mechanically driven by avoiding that cost;
4. under a costless/exogenous full-interoperability benchmark, both the benchmark and endogenous model favor IS throughout the audited weak-network domain.

C1 therefore does not generate the new reach-versus-competition-exposure feedback selected at Stage 3. Repair would require a substantive change such as bilateral interoperability, which is explicitly outside Stage 4 and belongs back at Stage 3.

## 2. Exact model

Three countries/firms `i=1,2,3`, three identical national markets, all firms active in every market.

Regimes:

- `rho^IS={{1,2,3}}`;
- `rho_12^SU={{1,2},{3}}`.

Implementation `a_i in [0,1]` is chosen after the formal regime and before Cournot quantities.

In market `k`:

`p_i^k=1-Q^k+v a_i sum_{j in C_i(rho),j!=i}q_j^k`.

Cost:

`C_i(a_i)=kappa a_i^2/2`.

Firm objective:

`Pi_i=sum_k p_i^k q_i^k-kappa a_i^2/2`.

Government objective was intended to be `W_i=CS_i+Pi_i`.

Primary exact regularity domain:

`0<v<=1/4`, `kappa>0`.

This is the weak-network domain aligned with benchmark B0. The Cournot and marginal-return identities themselves hold more broadly wherever denominators and quantities are well behaved.

## 3. Demand / technology derivation

No new utility primitive was authorized at Stage 3. The Stage-4 demand audit therefore checks whether the proposed inverse demands can themselves be gradients of a quasilinear representative utility.

For formal partners 1 and 2,

`partial p_1/partial q_2=-1+va_1`,

`partial p_2/partial q_1=-1+va_2`.

Their difference is

`v(a_1-a_2)`.

Because the implementation game requires unilateral deviations with `a_1 != a_2`, cross partials are not symmetric on the relevant strategy space. No `C^2` scalar utility `U(q;a)` can satisfy `p_i=partial U/partial q_i` globally.

Classification: **fatal welfare/microfoundation defect for the frozen one-sided primitive**.

## 4. Backward-induction equilibrium — Cournot stage

### IS

Let

`D_I=2+v(a_1+a_2+a_3)-v^3a_1a_2a_3`.

Then

`q_1^I=[1+2va_1+v^2(a_1a_2+a_1a_3-a_2a_3)]/(2D_I)`,

with cyclic counterparts.

At `a_1=a_2=a_3=a`,

`q_I=1/[2(2-va)]`.

### SU_12

`q_1^U=(1+va_1)/[4+v(a_1+a_2)-2v^2a_1a_2]`,

`q_2^U=(1+va_2)/[4+v(a_1+a_2)-2v^2a_1a_2]`,

`q_3^U=(1-v^2a_1a_2)/[4+v(a_1+a_2)-2v^2a_1a_2]`.

At `a_1=a_2=a`,

`q_M=1/[2(2-va)]`,

`q_O=(1-va)/[2(2-va)]`.

In both regimes, own inverse-demand slope is `-1`, so the Cournot FOC implies `p_i=q_i` at an interior quantity equilibrium. With three identical markets, reduced operating profit is `3q_i^2`.

## 5. SOC / existence / uniqueness

At a symmetric implementation profile, define the marginal operating-profit returns

`MB_I(a)=3v(3-va)/[2(2-va)^3(1+va)]`,

`MB_U(a)=9v/[4(2-va)^3(1+va)]`.

Interior implementation requires `kappa a=MB_R(a)`.

Define

`K_I(a)=MB_I(a)/a`,

`K_U(a)=MB_U(a)/a`.

On `0<v<=1/4`, `0<a<=1`,

`K_I'(a)<0`, `K_U'(a)<0`.

With rivals fixed, the exact own `K_own(x;b)` is also strictly decreasing in own `x` for `0<v<1`, so own reduced profit is single-peaked and the associated best response is global rather than merely first-order.

The own SOC at an interior symmetric stationary point is strictly negative throughout the audited domain.

Thus the symmetric continuation equilibrium is well characterized by a full-implementation corner or the unique interior symmetric root.

## 6. Full equilibrium and feasibility region

Define boundary values

`kappa_bar_I=3v(3-v)/[2(2-v)^3(1+v)]`,

`kappa_bar_U=9v/[4(2-v)^3(1+v)]`.

Then

`a_I*=1` for `kappa<=kappa_bar_I`; otherwise `a_I*` is the unique root in `(0,1)` of

`2kappa a(2-va)^3(1+va)=3v(3-va)`.

Similarly,

`a_U*=1` for `kappa<=kappa_bar_U`; otherwise `a_U*` is the unique root in `(0,1)` of

`4kappa a(2-va)^3(1+va)=9v`.

The SU outsider has no interoperability partner and therefore chooses

`a_3^U=0`.

All reported symmetric Cournot quantities are positive on `0<v<=1/4`.

## 7. Participation / corners

There is no firm-entry or government participation constraint inside the frozen continuation game. The relevant boundary is implementation `a_i in [0,1]`.

`a=0` is not optimal for a coalition member when `v>0` because the marginal implementation benefit at zero is positive.

`a=1` is the symmetric global best-response corner under the threshold conditions stated above.

The singleton SU outsider uniquely chooses `a_3=0` because implementation has no revenue benefit but a positive cost.

## 8. Comparative statics

The exact comparison is

`K_I(a)/K_U(a)=2(3-va)/3`.

Therefore `K_I(a)>K_U(a)` for every common `a` in the audited domain.

Because both `K` functions are decreasing, the symmetric equilibrium ordering is

`a_I*>=a_U*`,

strict whenever they are not both at the upper corner.

This is the opposite of CSIC crowd-out.

The model creates a stronger private marginal incentive to implement interoperability when the coalition is broader.

## 9. Mechanism decomposition

The intended C1 mechanism required two effects of larger formal scope:

1. larger interoperability/network reach — raises implementation incentives;
2. greater exposure to competition from interoperable rivals — lowers implementation incentives.

The frozen one-sided primitive contains effect 1 but does not put effect 2 into firm i's own implementation choice. Increasing `a_i` raises only firm i's own inverse-demand network term. Rival firms benefit from their own `a_j`, not from `a_i`.

Thus the algebra correctly reports **scope-induced crowd-in**, because the selected primitive never encoded the intended bilateral competition exposure.

This is not an algebraic accident; it is a mechanism misspecification.

## 10. Candidate-proposition kill table

| Candidate proposition | Result | Status |
|---|---|---|
| Cournot continuation has closed-form interior solution | Verified exactly | `PROVED` |
| Symmetric implementation equilibrium can be characterized by corner/interior threshold | Verified on `0<v<=1/4` | `PROVED` |
| `a_IS*<a_SU*` | Exact opposite: `a_IS*>=a_SU*` | `REJECTED` |
| One-sided inverse demand supports coherent consumer surplus for implementation deviations | Cross-partial condition fails | `REJECTED` |
| Endogenous implementation can make country 3 prefer SU in regular domain | Equilibrium-consistent diagnostic gives `Delta_3^endo>0` everywhere | `REJECTED` |
| Endogenous vs full implementation yields robust sign reversal | Only under cost-bearing full mandate | `REJECTED AS MECHANICAL` |
| Full model yields a C1 result unavailable in nested benchmarks | No surviving C1 result | `REJECTED` |

## 11. Consumer surplus and welfare

Because the full inverse-demand system is non-integrable for asymmetric implementation profiles, the model does not possess a globally valid CS object as written.

For diagnostics only, after fixing a symmetric realized profile, the corresponding symmetric inverse-demand matrix is integrable.

Let `x=va`.

At IS:

`CS_I=(9-6x)/[8(2-x)^2]`.

At SU:

`CS_U=(9-8x+x^2)/[8(2-x)^2]`.

Country 3 diagnostic welfare is

`W_3^I=(15-6x_I)/[8(2-x_I)^2]-kappa a_I^2/2`,

`W_3^U=(15-20x_U+7x_U^2)/[8(2-x_U)^2]`.

These expressions cannot cure the missing off-equilibrium utility representation.

## 12. Private vs social decision

A proper private-social comparison is not admissible because the social objective is not globally microfounded over the implementation strategy space.

The equilibrium-consistent diagnostic nevertheless shows that the private continuation response does not destabilize IS in the regular domain.

## 13. Limiting cases

As `kappa -> infinity`, both member implementation levels approach zero and the IS/SU welfare difference approaches zero from above in the diagnostic representation.

As implementation costs become low enough, both IS and SU members reach `a=1`; the implementation ordering becomes equality at the common upper corner.

As `v -> 0+`, implementation incentives vanish and the regime distinction vanishes continuously.

No limit produces the desired `a_I<a_U` within the audited weak-network domain.

## 14. Nested-benchmark recovery and comparison

- **B1:** fixing `rho` yields a standard continuous private implementation/compatibility game. This is recovered directly.
- **B3:** fixing implementation exogenously at full compatibility removes the private implementation stage and leaves a government regime comparison.
- **B0:** restricting `a` to `{0,1}` creates a binary implementation game, but the one-sided compatibility primitive is not identical to B0's symmetric compatible-group microfoundation. Hence exact nesting is weaker than Stage 3 hoped.
- **B4:** collapsing government and firm objectives removes the national-welfare coalition layer, but no new CSIC result survives to exploit that distinction.

## 15. Full-model-only result table

No qualifying positive full-model-only result survives.

The only sign reversal found is benchmark-dependent cost avoidance, not a new strategic feedback.

## 16. Numerical counterexample / region audit

Reproducible script:

`verification/stage04_csic_sympy.py`.

Grid:

- 25 `v` values in `(0,1/4]`;
- 240 log-spaced `kappa` values from `10^-4` to `10`;
- 6,000 total draws.

Results:

- `a_I<a_U`: 0;
- `Delta_3^endo<0`: 0;
- reversal vs cost-bearing `a=1` mandate: 2,428;
- reversal vs costless/exogenous full interoperability: 0.

Illustration `v=0.2`, `kappa=0.25`:

`a_I*=0.4600655`, `a_U*=0.2306753`,

`Delta_3^endo=0.0082137`,

`Delta_3^full,cost=-1/36`,

`Delta_3^full,tech=0.0972222`.

The numerical audit confirms, but does not establish, the exact analytical conclusions.

## 17. Artefact audit

Three artefact risks were tested.

1. **Artificial curvature:** quadratic cost is not what kills or creates crowd-out; the marginal-benefit ordering already runs opposite to C1.
2. **Benchmark-cost artefact:** the only sign reversal is generated when the full benchmark is forced to bear `kappa/2` at `a=1`.
3. **Demand artefact:** one-sided implementation destroys cross-derivative symmetry off the symmetric path, so consumer surplus is not structurally defined.

## 18. Exact diagnosed blocker(s)

There is more than one blocker, so Stage 5 is not authorized.

The decisive economic blocker is that the one-sided implementation primitive does not contain the intended competition-exposure channel and yields the opposite implementation ordering.

Independently, the same primitive lacks a coherent welfare microfoundation for unilateral implementation deviations.

Repairing either issue by bilateralizing interoperability changes the strategic architecture and must return to Stage 3.

## 19. Canonical stage verdict

`NO-GO`

## 20. Routing / next-stage contract

Terminate the C1 Stage-4 branch as a failed mechanism test.

Any continuation must re-enter **Stage 3 — Candidate Mechanism Search** and select or redesign a genuinely distinct mechanism. Per the Stage-3 contract, C2 may not be silently grafted onto C1.

Do not proceed to Stage 5 or Stage 6 from C1.
