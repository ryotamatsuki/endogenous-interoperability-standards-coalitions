# Stage 3 Re-entry — C2 Bilateral Implementation Public-Good / Free-Riding

Date: 2026-09-04  
Repository: `ryotamatsuki/endogenous-interoperability-standards-coalitions`  
Canonical workflow: `ryotamatsuki/research-paper-workflow` v1.1  
Release SHA: `488e5ab06c207909296a7564eaf9066f7f94319c`

## 1. Executive verdict

**Canonical verdict: `NO-GO` for C2.**

**Route: remain at Stage 3 for any further distinct mechanism. Do not proceed to Stage 4 on C2.**

C2 was re-evaluated as an independent mechanism after C1's Stage-4 failure. The re-entry separates five possible meanings of 'bilateral implementation free-riding' and tests the strongest smooth variant that preserves the national-welfare microfoundation.

The result is negative for a substantive reason:

1. the classic `max/min` and converter/consensus technologies are already directly exposed to old compatibility literature;
2. independent pairwise contribution games do not create regime-dependent per-link implementation when primitives are identical across links;
3. a standard coalition-wide voluntary public good lowers individual effort but, under conventional concavity/convexity, raises aggregate provision as coalition size grows;
4. the most defensible smooth bilateral substitute-contribution technology, `A_ij=a_i+a_j-a_i a_j`, repairs C1's integrability defect but yields a strictly stronger private implementation return under three-country IS than under two-country SU throughout the weak-network domain;
5. a 6,000-point diagnostic finds no `a_IS<a_SU`, no endogenous incentive for country 3 to leave IS, and no sign reversal relative to costless/full interoperability.

A positive C2 result can be manufactured only by importing a different mechanism — capacity constraints, scope diseconomies, averaging/dilution, coalition-wide shared infrastructure, or coalition-specific cost terms. That would violate the Stage-3 requirement to assess C2 on its own.

Therefore C2 is not promoted to the Minimal Model Gate.

---

## 2. Why C2 was worth re-opening

C1 failed partly because its one-sided implementation variable raised only the implementing firm's network term. Bilateralizing implementation was therefore an economically natural next question, not an algebraic rescue. A valid C2 model would ideally satisfy all of the following:

- a firm's implementation helps a bilateral interoperability relationship, not only itself;
- this benefit creates private underprovision/free-riding;
- the same technology operates under IS and SU;
- coalition membership changes the continuation implementation equilibrium;
- the implementation response can change government coalition stability;
- inverse demand remains integrable so `CS_i` and `W_i=CS_i+Pi_i` are well defined.

The re-entry asks whether all six can be achieved without another mechanism.

---

## 3. Targeted prior-art mini-audit

### 3.1 Farrell & Saloner (1992)

*Converters, Compatibility, and the Control of Interfaces*, Journal of Industrial Economics 40(1):9–35.

Converter provision, partial compatibility, interface control and private incentives are already core objects. This makes unilateral converter provision an old mechanism rather than a new one.

### 3.2 Choi (1997)

*The Provision of (Two-way) Converters in the Transition Process to a New Incompatible Technology*, Journal of Industrial Economics 45(2):139–153.

Converter providers ignore positive benefits conferred on users of the rival technology. Thus a private externality/underprovision story around converter effort is already explicit.

### 3.3 de Palma, Leruth & Regibeau (1999)

*Partial Compatibility with Network Externalities and Double Purchase*, Information Economics and Policy 11(2):209–227, DOI `10.1016/S0167-6245(99)00006-2`.

Firms make design choices determining the degree of compatibility before quantity competition. The equilibrium depends on the degree of consensus required to increase standardization. This is a direct threat to any contribution based on how bilateral consent maps private choices into effective compatibility.

### 3.4 Garcia & Vergari (2016)

*Revealing Incentives for Compatibility Provision in Vertically Differentiated Network Industries*, JEMS 25(3):720–749, DOI `10.1111/jems.12146`.

Their discussion makes the technology distinction explicit: when no firm can veto compatibility, final compatibility can be represented by the maximum of firms' noncooperative choices; when both have veto power, the final degree is the minimum. This sharply limits novelty from choosing `max` or `min` as the C2 aggregator.

### 3.5 Klimenko (2009)

*Policies and International Trade Agreements on Technical Compatibility for Industries with Network Externalities*, Journal of International Economics 77(2):151–166, DOI `10.1016/j.jinteco.2008.08.005`.

Private compatibility-enhancing activity, government compatibility policy, international competition and cooperative international policy are already combined. C2 can survive only through self-enforcing government coalition stability with a separate private continuation game, not through underprovision alone.

### 3.6 Malueg & Schwartz (2006)

*Compatibility Incentives of a Large Network Facing Multiple Rivals*, Journal of Industrial Economics 54(4):527–567, DOI `10.1111/j.1467-6451.2006.00299.x`.

The number of rivals and network strength already enter compatibility incentives in a multiple-rival setting, with ambiguous effects. This raises the burden on any claim that coalition size alone creates a new compatibility incentive.

### Evidence limitation

Garcia–Vergari is accessible at model/introduction level for the max/min veto distinction. The de Palma, Farrell–Saloner, Choi and Malueg–Schwartz comparisons here rely on publisher/author abstracts plus the prior Stage-1/2 audit rather than a fresh line-by-line proof audit. This is enough for Stage-3 mechanism selection but not for a future proposition-level novelty claim.

---

## 4. C2 technology comparison

| Variant | Economic interpretation | Regime-specific intensive feedback? | Prior-art risk | Stage-3 disposition |
|---|---|---:|---:|---|
| `max{a_i,a_j}` | either endpoint can unilaterally supply converter support | possibly asymmetric, but volunteer-style | VERY HIGH | REJECT |
| `min{a_i,a_j}` / `a_i a_j` | both endpoints required / weakest link | coordination, not pure free-riding | VERY HIGH | REJECT |
| separate `e_ij,e_ji` per link | bilateral public good on each link | NO if links are independent and identical | HIGH | REJECT |
| standard coalition public good `G=sum e_i` | all members benefit from total contribution | aggregate provision rises with group size under standard assumptions | GENERIC | REJECT |
| smooth bilateral OR `A_ij=a_i+a_j-a_i a_j` | substitutable overlapping interface/converter coverage | YES, and integrable | HIGH but best pure-C2 test | TESTED / FAILS |
| average/dilution, capacity, scope cost | larger coalition stretches implementation resources | YES | changes mechanism | NOT C2 |

---

## 5. General public-good sign check

Consider the canonical voluntary-contribution form

`pi_i=B(G)-c(e_i)`, `G=sum_i e_i`,

with `B'>0`, `B''<=0`, `c'>0`, `c''>0`.

At a symmetric interior equilibrium with group size `n`, write individual effort as `G_n/n`. The FOC is

`B'(G_n)=c'(G_n/n)`.

Treating `n` continuously and differentiating gives

`dG_n/dn = [c''(G_n/n) G_n/n^2]/[c''(G_n/n)/n-B''(G_n)] > 0`.

Thus the classic large-group free-riding effect does not imply that effective total interoperability falls when a coalition becomes larger. Individual effort can fall while aggregate provision rises.

To make the grand coalition's effective implementation lower than a smaller coalition's, one must add a dilution/normalization or capacity technology. That is a different mechanism.

---

## 6. Strongest pure-C2 diagnostic: smooth bilateral OR

Define bilateral effective interoperability

`A_ij=1-(1-a_i)(1-a_j)=a_i+a_j-a_i a_j`.

The technology is symmetric, smooth, bounded in `[0,1]`, has substitutable contributions, and makes rival effort reduce the marginal effect of own effort. It is the cleanest free-riding representation that does not rely on nonsmooth `max`.

Use a B0-style Cournot diagnostic:

`p_i=1-Q+v sum_{j in C_i(rho),j!=i} A_ij q_j`,

with `C_i(a_i)=kappa a_i^2/2`.

Because `A_ij=A_ji`, cross partials satisfy

`partial p_i/partial q_j=partial p_j/partial q_i=-1+vA_ij`.

Therefore this bilateral model has a coherent quasilinear representative utility and repairs C1's welfare defect.

At a symmetric member profile `a`, let

`x=v(2a-a^2)`.

The exact marginal operating-profit returns are

`MB_I(a)=3v(1-a)/[(1+x)(2-x)^3]`,

`MB_U(a)=3v(1-a)/[2(2-x)^3]`.

The exact ratio is

`MB_I/MB_U=2/(1+x)`.

On `0<v<=1/4`, `x<=1/4`, hence

`MB_I/MB_U>=8/5>1`.

So at every common interior implementation level in the audited domain, a member of the three-country IS coalition has a larger marginal incentive to implement than a member of the two-country SU coalition.

This natural bilateralization again points to **implementation crowd-in**, not a free-riding collapse of the larger coalition.

---

## 7. Numerical full-game diagnostic

Artifact: `verification/stage03r_c2_diagnostic.py`.

The script:

- derives the IS/SU Cournot systems symbolically;
- verifies the marginal-return formulas and exact ratio;
- verifies cross-partial symmetry;
- solves symmetric implementation conditions numerically;
- constructs consumer surplus from the integrable utility;
- compares country 3's IS continuation welfare with its SU-outsider continuation welfare;
- compares endogenous implementation with costless/exogenous full interoperability.

Grid:

- `v`: 50 points from `0.005` to `0.25`;
- `kappa`: 120 log-spaced points from `10^-3` to `10`;
- total: 6,000 points.

Results:

- `a_IS<a_SU`: 0;
- `Delta_3^endo<0`: 0;
- endogenous/full-tech sign reversal: 0.

This does not prove impossibility outside the diagnostic domain. It is enough for Stage 3 to conclude that the most defensible pure-C2 smooth technology lacks a positive signal strong enough to justify a full Stage-4 investment.

---

## 8. Why no alternative C2 is promoted

### `max`

This directly reproduces the unilateral/no-veto converter family and tends toward volunteer/asymmetric provision. A theorem would be driven by an old technology choice.

### `min` / product

This turns C2 into weakest-link coordination/strategic complementarity and is already anticipated by the veto/consensus literature. It is not the public-good free-riding mechanism being tested.

### independent pairwise contributions

Without a common resource constraint, each link solves the same game under IS and SU; coalition size only changes the count of links. There is no new regime-dependent intensive response.

### average or dilution aggregator

This can make larger groups look worse because each member mechanically receives a smaller weight. The desired sign is built into the aggregator rather than generated by strategic free-riding.

### common engineering capacity / convex cost across all links

This can create a real coalition-size effect but is a scope/capacity mechanism. It belongs to a new Stage-3 candidate, not C2.

### coalition-wide gateway/shared implementation artifact

A common infrastructure technology such as `A_C=1-product_i(1-a_i)` can generate stronger large-group contribution substitution, and in reduced form can even make effective `A_C` lower for three contributors than two in some parameter regions. But one member's effort then improves a coalition-wide shared artifact rather than a bilateral endpoint relationship. This is a distinct **common interoperability infrastructure** mechanism and should be separately compared with C3/C4 if the project continues.

---

## 9. Candidate proposition kill table

| Candidate proposition | Stage-3 result | Status |
|---|---|---|
| Bilateralization repairs C1's welfare microfoundation | symmetric OR technology gives exact cross-partial symmetry | SURVIVES |
| Pure bilateral free-riding makes grand-coalition implementation weaker | strongest smooth OR diagnostic gives stronger IS marginal return | REJECTED |
| Standard public-good free-riding makes effective provision fall with coalition size | aggregate `G_n` rises under standard concavity/convexity | REJECTED |
| Independent bilateral links create regime-specific implementation intensity | per-link game is invariant without a common constraint | REJECTED |
| Endogenous C2 implementation destabilizes IS relative to costless full compatibility | zero reversals in 6,000-point regular-domain diagnostic | NO POSITIVE SIGNAL |
| A pure C2 architecture merits Stage 4 | no | REJECTED |

---

## 10. Canonical Stage-3 re-entry verdict

`NO-GO` — C2 bilateral implementation public-good/free-riding.

C2 is terminated as the next minimal mechanism.

This verdict does **not** terminate the project. It says that a pure bilateral free-riding mechanism cannot be promoted without importing another economic primitive.

## 11. Routing

Remain at **Stage 3 — Candidate Mechanism Search** for any further work.

Do not proceed to Stage 4 with C2.

The next genuine mechanism search, if authorized, should compare rather than automatically select:

- C3 national-incidence / cross-border rent-shifting;
- a newly separated common-interoperability-infrastructure contribution game;
- any other mechanism that survives Stage-2 prior-art constraints.

Do not combine them silently.
