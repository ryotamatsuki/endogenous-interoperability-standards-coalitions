# Stage 4R4A — Affine-Demand Bertrand Continuation & Novelty Gate

Date: 2026-09-06
Canonical workflow: `ryotamatsuki/research-paper-workflow` v1.2
Parent stage: Stage 3R4

## 1. Executive verdict

**GO — CONTINUE WITHIN STAGE 4 TO POLICY/WELFARE/COALITION RECONSTRUCTION.**

The affine-demand re-foundation passes the continuation gate that killed the spatial architectures. A single pre-registered quadratic-utility map yields a nonempty parameter region in which demand is globally well posed, products are gross substitutes, and every upstream history has a unique Bertrand continuation under the Farahat–Perakis nonnegative affine-demand extension.

Endogenous repositioning also survives as a nondegenerate strategic margin. At an exact SU_12 anchor witness, the member firms have opposite nonzero location gradients and deeper union standardization strengthens their outward repositioning incentive.

The novelty classification is **DISTINCT BUT NARROW / SURVIVES FOR FULL-GAME TEST ONLY**. Affine demand, endogenous product design, compatibility, network effects, and compatibility-induced differentiation are all prior art. The only potentially publishable contribution left is the three-country government-standards-bloc game in which bloc policy depth is chosen before costly horizontal repositioning and the resulting Bertrand/welfare effects feed back into coalition stability.

No old welfare or coalition result is restored by this verdict.

## 2. Frozen Stage 4R4A map

For `i != j`, define smooth characteristic distance

`delta_ij(x)=1-cos(2*pi*(x_i-x_j))`.

The representative-consumer utility is

`U(q)=a*1'q - (1/2) q'B q + (v/2) q'G_rho q`, `q>=0`,

with

`B_ii=1`,

`B_ij=beta/[1+tau_ij(rho,s)+delta_ij(x)]`.

The standards-depth map `tau_ij(rho,s)` and the formal network matrix `G_rho` are inherited unchanged from `model/STAGE3R_CESD_POLICY_MAP.md`.

Effective curvature is

`K=B-vG_rho`.

The circle is now a product-characteristic space only. Consumers are not allocated to Salop arcs.

## 3. Gate A — demand well-posedness: PASS

Since `delta_ij in [0,2]` and `tau_ij in [t_bar-s_bar,t_bar+s_bar]`, let

`m_min=1/(3+t_bar+s_bar)`,

`m_max=1/(1+t_bar-s_bar)`,

`k_min=beta*m_min-v`,

`k_max=beta*m_max`.

Impose the sufficient global region

`0<v<beta*m_min`,

`2*k_max<1`,

`k_min>k_max^2`.

Then every off-diagonal element of `K` lies in `[k_min,k_max]`. Symmetric strict diagonal dominance implies `K` is positive definite for every admissible regime, policy-depth vector, and product-location profile.

For a symmetric 3x3 unit-diagonal matrix, the off-diagonal inverse formula is

`H_ij=(k_ik*k_jk-k_ij)/det(K)`, `H=K^{-1}`.

The inequality `k_min>k_max^2` makes all off-diagonal `H_ij` strictly negative. Therefore the induced affine demand has negative own-price effects and positive cross-price effects globally: the products are gross substitutes.

This region is nonempty. The exact verification normalization

`t_bar=1`, `s_bar=1/4`, `beta=1/5`, `v=1/50`

gives

`m_min=4/17`, `m_max=4/7`, `k_min=23/850`, `k_max=4/35`,

and satisfies both strict inequalities.

## 4. Gate B — global Bertrand continuation: PASS

With `H=K^{-1}` and positive quantities,

`q=H(a*1-p)`.

For one zero-cost product per firm, each price FOC is

`q_i-p_i H_ii=0`.

Let `D=diag(H_ii)`. The unique positive stationary solution is

`p*=(D+H)^(-1) H(a*1)`,

with

`q*=D p*`.

The maintained sign structure makes `D+H` a positive-definite matrix with nonpositive off-diagonal elements. Prices and equilibrium quantities are positive for `a>0`.

The economically relevant global demand object is not the negative-demand affine formula. Farahat and Perakis (2010, *Operations Research Letters*, DOI 10.1016/j.orl.2010.04.006) derive the nonnegative extension from quadratic representative-consumer utility and establish existence and uniqueness of Bertrand equilibrium for differentiated substitute products; the equilibrium coincides with the affine-demand equilibrium. The global sufficient inequalities above verify the substitute structure for every upstream history in this model.

Continuation classification throughout the maintained region:

`SOLVED_EQUILIBRIUM`.

There is no `None`/NaN/nonconvergence branch in the theoretical continuation object.

## 5. Gate C — endogenous repositioning: PASS FOR MINIMAL-MODEL EXISTENCE/NONDEGENERACY

Write displacement `y_i in [-1/2,1/2]`, `x_i=(h_i+y_i) mod 1`, with inherited repositioning cost `gamma*y_i^2/2`.

Because the chordal characteristic map is smooth and the matrix inverses are uniformly nonsingular in the maintained region, operating profit after Bertrand continuation is `C^2` on the compact displacement cube.

Define

`M=max_i sup_y |d^2 pi_i^B/d y_i^2|`.

Then `M<infinity`. For the open sufficient region `gamma>M`, every firm's payoff is strictly concave in its own displacement. Compact convex strategy sets plus own-payoff concavity give existence of a pure repositioning Nash equilibrium for every standards history.

This is a sufficient existence region; Stage 4R4B must assess economically useful values rather than treating large `gamma` as a free existence patch.

### Exact nondegeneracy audit

At SU_12, inherited anchors, and the transparent normalization above, exact matrix differentiation gives member 1's operating-profit displacement derivative

at `s_12=0`:

`-32149849595931108145632*sqrt(3)*pi / 486430409433760152272091875 < 0`,

and at `s_12=1/4`, `s_3=0`:

`-75651293074675407069532145098524269426176*sqrt(3)*pi / 86562062983525181197181659883980660200145203 < 0`.

The latter is strictly more negative. Member 2 is the mirror image and the outsider derivative is exactly zero at the inherited anchors.

Thus positive-depth SU integration strengthens the member firms' local incentive to differentiate outward in this witness. The location margin is not mechanically pinned.

Authority: `verification/stage04r4a_affine_bertrand_gate.py`.

## 6. Gate D — hostile novelty re-attack: NARROW PASS

### 6.1 Farahat–Perakis (2010)

They absorb the continuation architecture. Nonnegative affine demand and unique Bertrand pricing are **not contributions**.

### 6.2 Ushchev–Zenou (2018), Games and Economic Behavior

They model a product-variety network whose edges describe substitutability and derive a unique Bertrand equilibrium. This absorbs any claim that network-shaped substitutability and prices are new.

What they do not supply is this project's government standards-bloc depth game followed by costly firm repositioning that changes the competitive network and then feeds into coalition stability.

### 6.3 Baake–Boom (2001), IJIO

They analyze endogenous quality, network externalities, compatibility, and subsequent price competition. This is a serious threat: generic compatibility × endogenous differentiation is already known.

Their timing and object differ materially: firms choose inherent quality and later mutually agree on an adapter in a duopoly. The present surviving route has a government/bloc standards architecture and continuous depth chosen first, followed by firms' costly horizontal repositioning and a three-country coalition-stability comparison.

### 6.4 Cheng–Huang (2025), Journal of Economics

They explicitly show that compatibility/network externalities interact with quality competition and can expand vertical product differentiation. Therefore the statement “compatibility induces more differentiation” is **not novel** and must not be a headline claim.

### 6.5 Rodrigues (2026), `Endogenous Product Design: A Linear Demand Approach`

This February/April 2026 preprint is a direct modern threat to the affine redesign. It develops linear demand in which product characteristics themselves determine competitive interactions under Bertrand competition for arbitrary finite products/firms/attributes.

Accordingly, the paper cannot claim novelty from characteristics-dependent affine demand or endogenous design under Bertrand.

### 6.6 Barrett–Yang (2001), Journal of International Economics

They connect international standards, redesign costs, network effects and multi-attribute competition and show rational incentives for incompatibility. This absorbs broad international-standardization/redesign motivation.

### 6.7 Surviving full-game claim

The only claim that survives this audit is narrow:

> A formal standards coalition chooses continuous standard depth; this redistributes pairwise standard-induced differentiation across bloc boundaries; firms then strategically reposition horizontal product characteristics at a cost; repositioning changes the subsequent Bertrand competitive system; and those continuation effects may change government welfare and coalition stability.

Neither the affine-demand architecture nor the local outward-repositioning sign is sufficient. Stage 4R4B must produce an actual welfare/stability result unavailable in both the fixed-position and zero-depth benchmarks. If it does not, terminate the paper.

Novelty classification after Gate D: **DISTINCT BUT NARROW — NOT YET IJIO-SUFFICIENT**.

## 7. Candidate proposition table

| Candidate proposition | Stage 4R4A result |
|---|---|
| A1: Demand is globally well posed over all upstream histories | **PASS** in the stated sufficient region |
| A2: Bertrand continuation is globally complete and unique | **PASS** using the nonnegative affine-demand theorem plus verified gross-substitute structure |
| A3: Repositioning is not mechanically zero | **PASS**; exact SU anchor gradients are nonzero for members |
| A4: Standards depth changes repositioning incentives | **PASS at exact mechanism witness**; deeper SU makes the outward gradient strictly stronger |
| A5: Compatibility-induced differentiation is novel | **KILL**; close prior art exists |
| A6: Endogenous design under linear demand is novel | **KILL**; Rodrigues (2026) directly covers the broad architecture |
| A7: Standards-bloc depth × post-policy repositioning × coalition stability is distinct | **SURVIVES NARROWLY; requires Stage 4R4B welfare/stability theorem** |

## 8. What is still prohibited

The following historical spatial-model quantities remain non-authoritative:

- old policy-depth optima;
- old location equilibria;
- `Delta_M^(B-T)` and `Delta_M^(FULL)`;
- old CS/profit decomposition;
- old world-welfare ordering;
- old coalition-stability theorem.

None may be ported numerically into the affine model.

## 9. Stage 4R4A status

This is a project-specific subgate under canonical Stage 4. It is **not** a completed canonical Stage 4 verdict and does not route to Stage 6 yet.

Subgate verdict:

**GO — CONTINUE WITHIN STAGE 4.**

Next formal project substage:

**Stage 4R4B — Affine-Demand Policy, Welfare, Reversal & Coalition Reconstruction.**

Stage 4R4B must solve the actual bloc-depth and repositioning continuation, derive consumer surplus/profits/national welfare from the new quadratic utility, compare `B-T`, `B-X`, and `FULL`, and require at least one full-model welfare or coalition-stability result that is unavailable from either benchmark separately.

If Stage 4R4B fails that test, terminate the paper rather than returning to another continuation architecture.
