# Stage 3 Re-entry — C2 Bilateral Implementation Public-Good / Free-Riding

Date: 2026-09-04
Status: **RE-EVALUATED / NO MINIMAL SURVIVOR**

## 1. C2 mechanism identity

C2 was intended to be distinct from failed C1:

> effective interoperability is bilateral and one firm's implementation can benefit the rival endpoint as well as its own users, creating post-agreement free-riding or contribution substitution inside a formal standards coalition.

The desired full-game loop was

`rho -> bilateral contribution game -> effective interoperability -> product competition -> national welfare -> coalition stability`.

The mechanism is not allowed to rely on coalition-specific costs, engineering capacity constraints, economies/diseconomies of scope, topology, dynamics, government policy, or fixed-cost accounting to create the headline reversal.

## 2. Technology taxonomy

### C2-A — unilateral converter / max technology

`A_ij=max{a_i,a_j}`.

Economic meaning: either endpoint can unilaterally provide enough converter/interface support to determine the bilateral compatibility level.

Disposition: **REJECT AS CORE**.

Reason: this is exactly the veto/no-veto technology family already discussed in de Palma et al. and Garcia–Vergari. It also creates volunteer/free-rider asymmetry and nondifferentiable best responses. The public-good problem is old; adding a government coalition layer does not by itself create a new strategic result.

### C2-B — mutual-veto / weakest-link technology

`A_ij=min{a_i,a_j}` or smooth/complementary analogues such as `a_i a_j`.

Economic meaning: both endpoints must implement the interface; the weaker endpoint limits interoperability.

Disposition: **REJECT AS C2 FREE-RIDING MECHANISM**.

Reason: this is strategic complementarity / weakest-link coordination, not a pure free-riding mechanism. It is also directly exposed to the consensus/veto compatibility literature. Selecting min/product because it creates a desired coalition-size effect would make the technology assumption drive the theorem.

### C2-C — independent pairwise public goods

Each link `(i,j)` has separate contributions and effective compatibility `A_ij=Phi(e_ij,e_ji)`.

Disposition: **REJECT FOR LACK OF REGIME-SPECIFIC INTENSIVE FEEDBACK**.

With identical link primitives and no common capacity or scope cost, the equilibrium of a given pair is the same whether the pair sits inside a two-member or three-member formal coalition. Coalition size changes the number of links, not the equilibrium intensity on each link. The Stage-2 surviving contribution requires regime-dependent continuation implementation, not merely more copies of the same bilateral game.

Adding a common engineering budget or convex cost in total link effort would create a coalition-size effect, but that imports C4-style scope/capacity economics and is not pure C2.

### C2-D — standard coalition-wide voluntary public good

Let coalition members choose `e_i` and let effective implementation be total contribution `G=sum_i e_i`, with payoff

`pi_i=B(G)-c(e_i)`.

Disposition: **REJECT AS A SOURCE OF LARGER-COALITION IMPLEMENTATION DETERIORATION**.

At a symmetric interior Nash equilibrium, `B'(G_n)=c'(G_n/n)`. Treating coalition size `n` continuously,

`dG_n/dn = [c''(G_n/n) G_n/n^2] / [c''(G_n/n)/n - B''(G_n)] > 0`

under the standard assumptions `B''<=0`, `c''>0`.

Thus ordinary free-riding can lower individual effort while aggregate provision still rises with group size. A stability reversal obtained only by placing a fixed formal-coalition cost between the full-implementation and underprovided payoff levels would be a generic public-good-underprovision threshold, not a new interoperability mechanism.

### C2-E — smooth bilateral OR technology — strongest pure-C2 test

Use

`A_ij = a_i + a_j - a_i a_j = 1-(1-a_i)(1-a_j)`.

Interpretation: either endpoint may implement overlapping converter/interface functionality; duplicated coverage is not double-counted. Rival effort reduces the marginal contribution of own effort, giving a smooth free-riding / contribution-substitution channel.

This technology has three advantages:

1. bilateral symmetry `A_ij=A_ji`;
2. smooth unilateral deviations;
3. a coherent representative-utility microfoundation for B0-style inverse demand because cross-price/quantity derivatives are symmetric.

This is therefore the strongest minimal C2 candidate.

## 3. Diagnostic B0-style product-market test for C2-E

In each national market use

`p_i = 1-Q + v sum_{j in C_i(rho),j!=i} A_ij q_j`,

with `A_ij=a_i+a_j-a_i a_j` and implementation cost `kappa a_i^2/2`.

Compare

- `rho^IS={{1,2,3}}`;
- `rho_12^SU={{1,2},{3}}`.

At a symmetric member implementation level `a`, define

`x=v(2a-a^2)`.

The symmetric Cournot quantities are

`q_I=1/[2(2-x)]`,

`q_M=1/[2(2-x)]`,

`q_O=(1-x)/[2(2-x)]`.

The exact private marginal operating-profit returns to a member's implementation are

`MB_I(a)=3v(1-a)/[(1+x)(2-x)^3]`,

`MB_U(a)=3v(1-a)/[2(2-x)^3]`.

Hence

`MB_I(a)/MB_U(a)=2/(1+x)`.

On the weak-network domain `0<v<=1/4`, `0<=a<=1`, we have `0<=x<=1/4`, so

`MB_I/MB_U >= 8/5 > 1`.

Thus the natural smooth bilateral free-riding technology does **not** make private implementation weaker in IS. The larger coalition gives a strictly stronger marginal implementation return at every common interior `a` in the audited domain.

The implementation FOCs are

`kappa a = MB_I(a)` under IS,

`kappa a = MB_U(a)` under SU.

The diagnostic therefore predicts `a_IS*>a_SU*` on the regular domain rather than a larger-coalition free-riding collapse.

## 4. Welfare/microfoundation audit

Unlike failed C1, C2-E passes the integrability test. Since `A_ij=A_ji`,

`partial p_i/partial q_j = partial p_j/partial q_i = -1+v A_ij`.

A quasilinear representative utility exists:

`U(q;a)=sum_i q_i - 1/2 sum_i q_i^2 - sum_{i<j}q_i q_j + v sum_{linked i<j} A_ij q_i q_j`.

Therefore consumer surplus and national welfare can be defined coherently over unilateral implementation deviations.

This repairs C1's welfare defect, but it does not generate the desired C2 stability mechanism.

## 5. Numerical diagnostic

Reproducible artifact:

`verification/stage03r_c2_diagnostic.py`.

Grid:

- 50 values of `v` from `0.005` to `0.25`;
- 120 log-spaced values of `kappa` from `10^-3` to `10`;
- 6,000 parameter points.

For each point the script solves the symmetric implementation conditions under IS and SU and computes country 3's welfare difference using the integrable utility system.

Results:

- `a_IS<a_SU`: **0** cases;
- `Delta_3^endo<0`: **0** cases;
- sign reversal against costless/exogenous full interoperability: **0** cases.

This is diagnostic evidence, not a proof of a global theorem, but it gives no basis for promoting C2-E to Stage 4.

## 6. Why the apparently rescuing variants are not pure C2

A larger coalition can be made to reduce implementation by adding one of the following:

- average/dilution technology `A=(1/n)sum a_i`;
- a common engineering-capacity constraint across bilateral links;
- convex cost in total link support;
- coalition-wide gateway/public infrastructure with a technology different from bilateral endpoint implementation;
- coalition-size-dependent implementation costs.

These are substantive new mechanisms. They respectively introduce dilution, scope/capacity economics, or common infrastructure. They may be candidates in a fresh Stage-3 search, but they cannot be used to claim that C2 itself survived.

## 7. Prior-art position

C2's primitive contribution problem is already heavily occupied:

- Farrell & Saloner: converter provision and control of interfaces;
- Choi: converter provision ignores positive externalities to rival-technology users;
- de Palma–Leruth–Regibeau: partial compatibility depends on the degree of consensus required for standardization;
- Garcia–Vergari: explicit max versus min compatibility depending on veto power;
- Klimenko: private compatibility-enhancing activity alongside international government compatibility policy;
- Malueg–Schwartz: compatibility incentives when a network faces multiple compatible rivals.

No audited paper is claimed to contain the complete government-coalition stability game. The problem is instead that the **minimal new feedback C2 was supposed to contribute does not survive a natural bilateral implementation technology**. Alternative technologies that force it either reproduce known converter/consensus games or import another Stage-3 mechanism.

## 8. C2 disposition

**C2 — Bilateral Implementation Public-Good / Free-Riding: NO-GO at Stage 3 re-entry.**

Do not send C2 to Stage 4.

Do not repair it by adding capacity, dilution, topology, policy, dynamics, regime-specific costs, or a common gateway without reopening Stage 3 as a new mechanism search.
