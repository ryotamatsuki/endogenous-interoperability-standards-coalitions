# Stage 1 — Source & Mathematical Audit

Date: 2026-09-04  
Repository: `ryotamatsuki/endogenous-interoperability-standards-coalitions`  
Canonical workflow: `ryotamatsuki/research-paper-workflow` v1.1  
Workflow release SHA: `488e5ab06c207909296a7564eaf9066f7f94319c`  
Template: `templates/STAGE_01_AUDIT.md`

## 1. Executive audit verdict

**Canonical verdict: `GO TO NOVELTY GATE`.**

Stage 1 does **not** validate the original model idea. It materially narrows and corrects it.

The audit establishes five points.

1. Continuous / partial compatibility followed by differentiated product-market competition is an old and crowded modeling object. It cannot be the paper's contribution.
2. The project's own frozen benchmark, `private-compatibility-standards-coalitions`, already has the timing `formal government partition -> private adoption -> competition -> national welfare -> coalition stability`. Therefore the Stage-0 claim that actor/timing separation itself might be new is rejected.
3. Klimenko (2009) already studies continuous partial technical compatibility together with government compatibility policies, international competition, national policy incentives, and international coordination. Continuous compatibility plus a government layer is therefore also not enough.
4. The provisional scalar comparison `a_o* versus â` is not a valid primitive formulation. Government deviation changes the formal regime and therefore generally changes the private continuation equilibrium. Coalition stability must first compare regime-specific continuation values. A scalar `â` may be introduced only if monotonicity and uniqueness of a root are later proved.
5. A symbolic re-audit of Stadler, Tobler Trexler & Unsorg (2022) reproduces their price equilibrium and symmetric compatibility FOC exactly, but finds that the paper's stated restrictions are not sufficient to make the reported interior stationary point a local maximum for every admissible installed base. This is a direct warning that the present project must prove SOC/global best-response conditions and corners rather than infer equilibrium from a symmetric FOC.

The residual project is therefore a **generalization/unification candidate**:

> Does a continuous, privately chosen post-agreement interoperability implementation margin change the stability of a government standards coalition in a way that cannot be obtained from the binary private-adoption coalition model or from continuous compatibility/government-policy models separately?

This is sufficiently precise to send to Stage 2, where it should face an aggressive whole-game absorption test. Novelty is **not** established.

---

## 2. Canonical source / benchmark model map

### 2.1 Own binary standards-coalition benchmark

Source: `ryotamatsuki/private-compatibility-standards-coalitions/docs/CANONICAL_MODEL.md`.

The frozen model has three countries and three domestic firms. Governments determine a formal standards partition `rho`. Firms then make private standard-adoption decisions, followed by Cournot competition. National welfare is `CS_i + Pi_i`, and coalition stability is evaluated from government continuation payoffs.

Its canonical timing is already:

`rho -> a*(rho,F) -> q*(rho,a*) -> W_i(rho,F) -> S(F)`.

Important consequence: the new project cannot claim novelty from separating government formal standardization from later private compatibility behavior. That structure already exists in the user's frozen paper. The new project can only be a substantive continuous generalization if the continuous implementation margin produces a new strategic or welfare result.

**Classification:** `CORRECT benchmark / binding nested comparison`.

### 2.2 Stadler, Tobler Trexler & Unsorg (2022)

Source: *The Perpetual Trouble with Network Products Why IT Firms Choose Partial Compatibility*, Networks and Spatial Economics 22, 903–913, DOI `10.1007/s11067-022-09572-x`.

Players: two firms.  
Timing: compatibility `k_i in [0,1]` first; prices second.  
Consumers: Hotelling-style horizontal differentiation with quadratic distance loss and fulfilled expectations.  
Network size:

`g_i = b + q_i + k_i (b + q_j)`.

Consumer surplus/utility from product `i`:

`u0 + beta g_i - p_i - alpha (x-x_i)^2`.

Assumptions reported in the paper include `b>=0`, `alpha>=0`, and `beta in [0,alpha/3]`.

Coordination cost:

`gamma k_i^2 / 2`.

The paper also studies a common compatibility choice by firms through an SDO-type arrangement. The decision makers remain firms, not national governments.

**Classification:** very close continuous-compatibility benchmark; not whole-game absorption of the residual country-coalition question.

### 2.3 Foros & Hansen (2001)

Source: *Competition and compatibility among Internet Service Providers*, Information Economics and Policy 13(4), 411–425, DOI `10.1016/S0167-6245(01)00044-0`, together with the accessible closely related precursor model.

Players: ISPs.  
Timing: interconnection/compatibility quality first; Hotelling price competition second.  
Network effects: yes.  
Private-versus-welfare investment comparison: yes.

In the accessible model representation, market shares depend on the composite

`t - beta(1-k)`.

Thus the substitutability coefficient can be written

`sigma = 1/[2(t-beta(1-k))]`.

This is a direct example of the reparameterization problem: falling transport cost `t` and rising compatibility `k` enter the product-market allocation through the same effective substitutability term.

**Classification:** `CORRECT benchmark`; strong evidence that a transport-cost-only interpretation of interoperability is not a distinct mechanism.

### 2.4 Toshimitsu (2018)

Source: *Strategic Compatibility Choice, Network Alliance, and Welfare*, Journal of Industry, Competition and Trade 18(2), 245–252, DOI `10.1007/s10842-017-0264-1`.

The accessible abstract and introduction establish differentiated Cournot competition, network externalities, strategic compatibility choice, multiple imperfect/perfect compatibility equilibria, and construction of a stable/socially optimal network alliance. The introduction states that compatibility choices tend to be made by providers unless policy intervention occurs.

The alliance is therefore a provider/firm-side compatibility institution rather than a coalition of countries evaluating national participation/deviation payoffs.

**Classification:** `CLOSE / component-and-mechanism overlap`; exact full-equation audit deferred because a fully accessible version was not obtained in this run. This does not block Stage 1 because no project theorem relies on its equations; Stage 2 must obtain the full paper before a final absorption verdict.

### 2.5 Gandal & Shy (2001)

Source: *Standardization policy and international trade*, Journal of International Economics 53(2), 363–383, DOI `10.1016/S0022-1996(00)00067-2`.

Players: governments/countries and domestic firms.  
Government object: recognition of foreign standards and formation of standardization unions.  
Environment: horizontal differentiation, conversion costs and/or network effects.  
Coalition concept: countries may form a standardization union with common recognition policy toward nonmembers.

Compatibility/recognition is essentially binary in the relevant institutional margin; the model does not endogenize a continuous post-agreement firm implementation intensity.

**Classification:** `CORRECT government-coalition benchmark / not whole-game absorption`.

### 2.6 Klimenko (2009) — highest newly identified Stage-1 risk

Sources:

- *Policies and international trade agreements on technical compatibility for industries with network externalities*, Journal of International Economics 77(2), 151–166, DOI `10.1016/j.jinteco.2008.08.005`.
- *Strategic interoperability standards and trade taxes*, International Review of Economics & Finance 18(4), 539–551, DOI `10.1016/j.iref.2008.09.015`.

These papers are especially important because they explicitly model partially incompatible domestic and foreign products, network effects, government standards/policies toward the **degree** of technical compatibility, compatibility-enhancing effort/investment, national strategic incentives, and international coordination/agreements.

Klimenko (2009 JIE) explicitly contrasts its continuous framework with Gandal & Shy, noting that the latter does not allow partial incompatibility. The home government can impose a minimum compatibility standard on the foreign product while another government can use a tax/subsidy linked to compatibility-enhancing effort; the paper then analyzes international coordination of compatibility policies.

**Classification:** `VERY HIGH-RISK benchmark`. It preempts any claim that adding governments, international policy, or agreements to continuous interoperability is itself new. The residual distinction must involve endogenous **membership/stability of a standards coalition** combined with private continuation implementation, not simply an international compatibility agreement.

### 2.7 Other occupied families

- de Palma, Leruth & Regibeau (1999): partial compatibility + network externalities + endogenous product design.
- Garcia (2016): compatibility choice before Bertrand competition in differentiated network industries.
- Jeon, Menicucci & Nasr (2023): dynamic compatibility, switching costs and data portability.
- Huang, Tan, Teh & Zhou (2026): weighted interoperability network among competing platforms with pricing and welfare.
- Peitz (2026): continuous partial compatibility as a share of functionalities with industry-wide network effects.

These sources make Salop, network, switching-cost, topology, and platform routes highly crowded. Stage 2 must use them as kill sources, not decorative citations.

---

## 3. Equation-by-equation audit — Stadler et al. (2022)

The full accessible source was reconstructed in SymPy from primitive demand and profit equations. Reproducibility artifact:

`verification/stage01_stadler_sympy.py`.

### 3.1 Expected demand

Using fulfilled expectations, the published demand is

`D_i = 1/2 + [p_j-p_i + beta(1+2b)(k_i-k_j)/2] / [2alpha-beta(2-k_i-k_j)]`.

Given `beta <= alpha/3` and `k_i,k_j in [0,1]`, the denominator is strictly positive for `alpha>0`.

**Audit:** `CORRECT` as entered from the source.

### 3.2 Price subgame

Firm `i` maximizes

`pi_i = (p_i-c)D_i - gamma k_i^2/2`.

Solving the two price FOCs symbolically gives

`p_i = c + alpha - beta[3-2k_i-k_j-b(k_i-k_j)]/3`,

exactly matching the published equation.

The own second derivative with respect to price is negative because demand is linear in own price with a negative slope and the denominator above is positive.

**Audit:** `CORRECT`.

### 3.3 Reduced profit and symmetric first-stage FOC

Substituting the price equilibrium into profit and differentiating with respect to own compatibility, then imposing `k_1=k_2=k`, yields exactly

`d pi_i/d k_i |sym = beta(5+4b)/12 - gamma k`.

Thus the reported stationary root

`k_FOC = beta(5+4b)/(12 gamma)`

is algebraically correct.

**Audit:** `CORRECT AS A SYMMETRIC FOC`.

### 3.4 Own second-order condition

The own second derivative of reduced profit at a symmetric profile is

`[-36 alpha gamma + 4 b^2 beta^2 + 4 b beta^2 + beta^2 - 36 beta gamma k + 36 beta gamma] / [36(alpha+beta k-beta)]`.

At the reported interior root, SymPy simplifies the expression to

`2 gamma[-18 alpha gamma + 2 b^2 beta^2 - 4 b beta^2 - 7 beta^2 + 18 beta gamma] / [3(12 alpha gamma + 4 b beta^2 + 5 beta^2 - 12 beta gamma)]`.

Under `alpha >= 3 beta` and an interior candidate, the relevant denominator is positive. A local maximum therefore additionally requires

`18 gamma(alpha-beta) > beta^2(2b^2-4b-7)`.

This condition is **not** implied by the paper's stated interiority condition alone,

`gamma > beta(5+4b)/12`,

for unrestricted `b>=0`.

### 3.5 Exact counterexample

Take

`alpha=3, beta=1, b=10, gamma=303/80=3.7875, c=0`.

These values satisfy the paper's reported preference restriction `beta<=alpha/3`, `b>=0`, and its interiority inequality because

`beta(5+4b)/12 = 3.75 < 3.7875`.

The reported root is

`k_FOC = 100/101 ≈ 0.990099`,

so it is interior. But the own second derivative at that point is positive, approximately

`0.309354`.

Holding the rival at `100/101`, the reduced-profit diagnostic gives approximately:

- `pi_i(k_i=0) = 0.188669`,
- `pi_i(k_i=100/101) = -0.361386`,
- `pi_i(k_i=1) = -0.361371`.

Thus the stationary root is not a best response in this admissible parameter example.

### 3.6 Classification of the reported SPNE formula

The paper states an overall SPNE compatibility rule

`k* = min{beta(5+4b)/(12gamma),1}`.

The symbolic audit shows that the formula is correctly obtained from the symmetric FOC, but the published parameter restrictions displayed around the model and the interiority condition are not sufficient for the root to be a maximum for all `b>=0`.

**Audit classification:** `AMBIGUOUS / OVERSTATED AS A GLOBAL SPNE CLAIM` unless an additional restriction ensuring own concavity/global optimality is imposed. This is not an allegation that the economically emphasized low-installed-base cases fail; it is a scope/verification issue in the globally stated formula.

### 3.7 Coordination cost

The quadratic cost `gamma k_i^2/2` is explicitly assumed and economically described as coordination cost. It is mathematically legitimate, but for the present project it cannot be imported merely because it generates curvature/interiority.

**Audit classification for reuse here:** `CORRECT BUT ECONOMICALLY AD HOC UNTIL INDEPENDENTLY MICROFOUNDED`.

---

## 4. Foros-type reparameterization audit

In the accessible related Foros–Hansen representation, compatibility/interconnection quality `k` enters market shares through

`sigma = 1/[2(t-beta(1-k))]`.

The symmetric price can be written

`p = c + t - beta(1-k)`,

and symmetric operating profit is

`pi = [t-beta(1-k)]/2`.

Exact differentiation gives

`d pi/dk = beta/2 > 0`

in the costless compatibility case.

The crucial Stage-1 implication is not the sign itself. It is that the product-market effect of `k` is summarized by the same composite term as transport cost. If the new project only writes `t_eff=t(a)` and adds no independent formal-state/implementation channel, interoperability is a change of variable rather than a new primitive.

**Audit classification:** transport-cost-only interoperability route = `CORRECT BUT ECONOMICALLY COSMETIC` as a candidate contribution.

---

## 5. SOC / feasibility / participation audit for the new project

No canonical functional-form model exists yet, so no project equilibrium can honestly be certified at Stage 1. The correct output is a set of binding verification requirements.

For any later continuous implementation game, the following are mandatory:

1. prove the downstream product-market equilibrium and its domain;
2. substitute it into firm profit without changing regimes or consumer populations;
3. derive full unilateral best responses in `a_i`, not only a symmetric FOC;
4. verify SOC/concavity or use KKT/global comparison;
5. solve `a_i=0` and `a_i=1` corners;
6. check asymmetric deviations from symmetric profiles;
7. distinguish technical/implementation costs from algebraic curvature devices;
8. recompute national welfare from primitive utility/profit definitions;
9. include all regime-specific implementation costs and transfers consistently;
10. evaluate government participation/deviation after substituting the appropriate continuation equilibrium for each formal state.

---

## 6. Parameter-interpretation audit

### 6.1 `a` cannot be presumed to be a single scalar

If firms choose individually, the primitive object is a vector `a`. A scalar `a_o*` is authorized only after symmetry or aggregation is proved.

### 6.2 `a` cannot simultaneously stand for unrelated channels without identification

The current notes mention switching cost, mismatch/transport cost, accessible network size, complement access, and technical compliance cost. These are distinct primitives. A later minimal model must choose one primary economic channel and add another only if necessary for the surviving theorem.

### 6.3 Cost curvature requires an independent interpretation

A convex cost may represent engineering effort, certification, API maintenance, testing across implementations, licensing, organizational coordination, or another real technology. Its shape cannot be selected solely to guarantee `0<a<1`.

### 6.4 Formal coalition state must matter independently

If `rho` merely renames a value of `a`, the government layer is cosmetic. Formal membership must change a feasible set, required baseline, cost, recognition rule, market access condition, ownership/welfare incidence, or another primitive mapping.

---

## 7. Welfare / participation / coalition-stability audit

### 7.1 Correct primitive stability object

The Stage-0 threshold notation is too strong. Let `a*(rho;theta)` be the private implementation continuation equilibrium under formal state `rho`, and let `y*` be the subsequent market equilibrium. Define

`V_i(rho;theta) = W_i(rho,a*(rho;theta),y*(rho,a*(rho;theta));theta)`.

For an admissible unilateral government deviation `rho'`, the relevant condition is

`Delta_i(rho,rho';theta) = V_i(rho;theta)-V_i(rho';theta)`.

The coalition is stable only if all required `Delta_i >= 0` conditions hold.

This mirrors the logic already present in the binary frozen benchmark and remains valid for a continuous extension.

### 7.2 Why `â` is not primitive

A government deviation changes `rho`; therefore it generally changes firms' feasible implementation choices, incentives, and equilibrium `a*`. Comparing one common scalar `a` across the member and deviation regimes can silently hold the continuation game fixed when it should change.

A threshold `â` may be defined later only if, after substituting the deviation continuation, the membership payoff difference is continuous and monotone in a scalar member-side implementation statistic and has a unique root.

Until that is proved, the research question should be stated using `Delta_i`, not `a_o* ≷ â`.

### 7.3 National welfare definition

The own binary benchmark uses domestic consumer surplus plus the worldwide profit of the domestic firm, net of private adoption cost. A continuous extension need not copy this convention, but it must make ownership and cross-border surplus incidence explicit and apply the same convention to all formal regimes.

---

## 8. Correct / ad hoc / incorrect / ambiguous claim table

| Object / inherited claim | Stage-1 classification | Reason |
|---|---|---|
| Continuous compatibility can be endogenous | `CORRECT / OLD` | Established by multiple prior models |
| Compatibility before price competition | `CORRECT / OLD` | Stadler, Foros, Garcia and others |
| Interior partial compatibility is a novelty signal | `INCORRECT` | Already explicit in close literature |
| Stadler price equilibrium | `CORRECT` | Exact SymPy re-derivation |
| Stadler symmetric compatibility FOC | `CORRECT` | Exact SymPy re-derivation |
| Stadler reported `k*` as global SPNE under only displayed restrictions | `AMBIGUOUS / OVERSTATED` | Additional SOC/global-best-response restriction needed; exact counterexample found |
| Quadratic compatibility cost as automatic modeling choice | `CORRECT BUT ECONOMICALLY AD HOC` | Needs independent interpretation for this project |
| Interoperability only as `t -> t(a)` | `CORRECT BUT ECONOMICALLY COSMETIC` | Can be absorbed into an effective substitutability coefficient |
| Actor/timing separation `government partition -> private choice -> market -> welfare -> stability` is new | `INCORRECT` | Already present in the user's frozen binary benchmark |
| Government policy + continuous partial compatibility is new | `INCORRECT` | Klimenko (2009) directly occupies this family |
| `â` necessarily exists as a scalar stability threshold | `INCORRECT / UNPROVED` | Deviations change continuation equilibria; monotonicity/root must be proved |
| Coalition stability should use regime-specific continuation values | `CORRECT` | Required by subgame-perfect/backward-induction logic |
| Continuous implementation inside an endogenous government coalition may yield a new full-game result | `AMBIGUOUS / RESEARCHABLE` | Precise residual question; novelty requires Stage 2 whole-game kill test |

---

## 9. Audited residual game for novelty search

Stage 2 must hold fixed the following representation recorded in `model/AUDITED_STAGE1_REPRESENTATION.md`:

1. governments/countries determine or face a formal standards coalition/partition `rho`;
2. firms subsequently choose a regime-dependent continuous implementation vector `a`;
3. firms compete in a downstream market;
4. national welfare is evaluated consistently;
5. government coalition stability compares each formal regime with its own private/market continuation equilibrium.

No Salop, network-effect, cost, aggregator, or competition functional form is frozen.

The direct residual question is:

> **Does endogenizing a continuous post-agreement private interoperability implementation margin inside a government standards-coalition game generate a coalition-stability result that is unavailable in both the binary private-adoption coalition benchmark and continuous compatibility/government-policy models considered separately?**

---

## 10. Exact inputs for Stage 2 novelty search

Stage 2 must perform whole-game comparison, not keyword counting, against at least four benchmark groups.

### B0 — own binary private-adoption coalition model

`private-compatibility-standards-coalitions` is a mandatory nested benchmark. Determine whether the continuous model does anything beyond smoothing its fixed-cost thresholds.

### B1 — continuous private compatibility

At minimum:

- Stadler, Tobler Trexler & Unsorg (2022);
- Foros & Hansen (2001);
- de Palma, Leruth & Regibeau (1999);
- Garcia (2016);
- Toshimitsu (2018);
- Jeon, Menicucci & Nasr (2023).

### B2 — government continuous compatibility / international coordination

At minimum:

- Klimenko (2009 JIE);
- Klimenko (2009 IREF);
- Ji & Daitoh (2008) on interconnection agreement and policy intervention;
- related international compatibility-policy papers found through those citations.

### B3 — government standards coalitions / unions

At minimum:

- Gandal & Shy (2001);
- later work on technical compatibility standards and international trade agreements;
- the current frozen private-adoption paper as the closest direct nested implementation.

For each, compare players, objective functions, control rights over compatibility, timing, continuous versus binary choice, product-market game, national/world welfare, agreement/coalition formation, and deviation/stability concept.

The strongest kill question is:

> Can the proposed model be reconstructed simply by taking the binary coalition model B0, replacing binary private adoption by a standard continuous compatibility-investment block from B1/B2, and obtaining the same stability logic after a smooth threshold substitution?

If yes, return `NO-GO` at Stage 2.

---

## 11. Final verdict and next-stage contract

### Verdict

**`GO TO NOVELTY GATE`**

Reason: Stage 1 has produced a mathematically coherent residual game and corrected the threshold/stability formulation. No surviving project theorem has been asserted. The remaining uncertainty is predominantly novelty/absorption rather than a source-math inconsistency, which is exactly the function of Stage 2.

### Stage-2 contract

Stage 2 may:

- retrieve and compare the closest full literature;
- test whole-game absorption;
- determine whether the project is a meaningful generalization/unification;
- kill the branch if continuous implementation only smooths or relabels known results.

Stage 2 may **not**:

- add dynamics, asymmetric countries, endogenous locations, multiple network layers, or another mechanism merely to escape prior art;
- assume `â` exists;
- restore `Salop + network effects + endogenous a` as a contribution claim;
- alter the frozen theory of `private-compatibility-standards-coalitions`;
- choose a curvature term to manufacture interiority.

If Stage 2 returns `GO`, only then may Stage 3 search for the smallest mechanism that produces a genuinely new full-game result.
