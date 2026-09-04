# Stage 3 Re-entry — C-ESD Mechanism Search / Kill Gate

Date: 2026-09-04
Repository: `ryotamatsuki/endogenous-interoperability-standards-coalitions`
Workflow: `ryotamatsuki/research-paper-workflow` v1.1 @ `488e5ab06c207909296a7564eaf9066f7f94319c`

## Executive verdict

# **CONDITIONAL GO — REMAIN AT STAGE 3**

C-ESD survives the firm-side mechanism kill but is **not authorized for Stage 4**.

The cheap Hotelling architectures fail: when government policy enters only as a common transport/mismatch coefficient, the downstream profit objective scales in `t`, so firm location best responses do not respond to `t`. A symmetric two-firm network-effect extension also cancels from the location incentive.

A distinct positive mechanism appears in a three-firm Salop representation that respects the IS/SU/SW compatibility topology. Under IS and SW, equal spacing has zero unilateral location gradient by symmetry. Under `SU12`, where firms 1 and 2 share a network and firm 3 is the outsider, the compatible members have a nonzero exact incentive to move apart. Lower standard-induced friction `t` strengthens this re-differentiation incentive through `r=v/t`.

With an economically interpretable inherited product/technology position and redesign/repositioning cost, a numerical Nash witness produces `dx*/dt != 0` under SU while IS/SW remain at their symmetric anchors.

The candidate nevertheless cannot pass to Stage 4 because the government policy variable is not yet institutionally unique under SU. A single scalar `t` does not say which within-bloc and cross-bloc frictions are chosen, by whom, or how the choice maps back to the frozen B0 benchmark. Until that single architecture question is resolved, `t_IS*`, `t_SU*`, `t_SW*`, national welfare, and coalition deviations are not well-defined.

---

## 1. Candidate and strategic loop

C-ESD:

**Endogenous Standard Differentiation × Strategic Product Repositioning**.

Desired full loop:

`rho in {IS,SU,SW} -> government standard-differentiation policy -> firm locations x -> prices -> national welfare -> coalition stability`.

`t` is government-controlled standard-induced switching/adaptation/differentiation friction. `t down` means deeper interoperability/standardization.

`x_i` is firm `i`'s horizontal product-position choice.

Relative profit is excluded from the core Stage-3R model.

---

## 2. Candidate comparison

| Candidate | Core specification | Mechanism result | Prior-art / math risk | Stage-3R disposition |
|---|---|---|---|---|
| A | 2-firm quadratic Hotelling, endogenous `t`, endogenous `x` | `t` scales profits; `x*` independent of `t`; boundary differentiation | mechanism collapses | **KILL** |
| B | A + symmetric market-share network effect | exact cancellation; same symmetric location gradient | network term does not generate policy response | **KILL** |
| C | 3-firm Salop + IS/SU/SW compatibility networks, no anchor | SU creates exact nonzero repositioning force | corners / location degeneracy | **POSITIVE DIAGNOSTIC, NOT SUFFICIENT** |
| D | C + inherited product/technology anchors and redesign cost | SU members reposition outward; response strengthens as `t` falls | redesign cost is substantive prior-art-exposed primitive | **PREFERRED CONDITIONAL CANDIDATE** |

Preferred Stage-3 candidate: **D**, subject to one unresolved government-policy mapping.

---

## 3. Kill of the naive Hotelling model

For full-coverage quadratic Hotelling with `x1<x2`, the price subgame gives

`q1=(2+x1+x2)/6`,

`q2=(4-x1-x2)/6`,

`p1=t(x2-x1)(2+x1+x2)/3`,

`p2=t(x2-x1)(4-x1-x2)/3`.

Thus

`pi1=t(x2-x1)(2+x1+x2)^2/18`.

`t` factors out of the location objective. Therefore changing government standard friction changes price/profit levels but not the location best response.

At `x1=a`, `x2=1-a`,

`d pi1/dx1 = -t(4a+1)/6 < 0`.

The standard quadratic model gives maximum differentiation and no `dx*/dt` channel.

This is a structural scale-invariance kill, not a numerical failure.

---

## 4. Network effects do not rescue the two-firm line

Let a symmetric market-share network effect produce an effective relative-network term `delta=v_n(1-lambda)`. With

`H=t(x2-x1)-delta>0`,

the exact symmetric own-location gradient remains

`d pi1/dx1 = -t(4a+1)/6`.

The network term cancels.

Therefore the desired mechanism does not arise from merely adding `network effect` to the two-firm Hotelling line.

---

## 5. Three-firm Salop diagnostic

The standards-coalition architecture itself creates a useful asymmetry under SU.

Use a unit circle, linear mismatch loss, full coverage, and a market-share network term. Let

`H3=3I-J`,

and represent compatible network membership by matrix `G`.

Demand can be written

`q = b(x) - H3 p/(2t) + v H3 G q/(2t)`.

Compatibility matrices:

- IS: all products share one network;
- SW: each product has a separate network;
- SU12: products 1 and 2 share a network, product 3 is the outsider.

Set

`r=v/t`.

At equal spacing, with `x3=0<x1=1/3<x2=2/3`, exact symbolic differentiation yields

`(1/t) d pi1/dx1 = 0` for IS,

`(1/t) d pi1/dx1 = 0` for SW,

and for SU12

`(1/t) d pi1/dx1 = r(3r-2)(12r-7)/[6(2r-1)(6r-5)^2]`.

For

`0<r<1/2`,

this is strictly negative.

Firm 1 moves left, away from its compatible partner firm 2 and toward the outsider's side of product space. By symmetry the other compatible member moves right. The compatible pair therefore re-differentiates in product space.

Moreover the derivative of this normalized gradient with respect to `r` is negative throughout the audited regular interval. Since `r=v/t`, reducing `t` strengthens the SU repositioning force.

This passes the core qualitative Stage-3 mechanism test:

`government-induced compatibility depth -> regime-specific firm repositioning`.

---

## 6. Anchored-circle regularization

An unrestricted location game risks corners and ordering changes. The preferred minimal regularization is an inherited product/technology position `h_i` with redesign cost

`gamma(x_i-h_i)^2/2`.

This has a concrete interpretation: firms inherit brand, architecture, interface and complementary-design positions and must spend resources to move away from them.

However:

- it is not a novelty source;
- redesign costs already appear in international-standards literature;
- Stage 4 must prove that the result is not generated mechanically by the curvature term;
- global best responses and ordering/corner deviations remain mandatory.

The diagnostic derives the local SU concavity threshold

`gamma > r^2 t(3r-2)(12r-7)^2/[4(2r-1)(6r-5)^2(9r-5)^2]`.

---

## 7. Numerical mechanism witness

With

`h=(1/6,1/2,5/6)`, `v=0.05`, `gamma=0.5`,

the location-Nash diagnostic produces:

- IS: firms remain at the equally spaced anchors for `t=0.5,1,2`;
- SW: firms remain at the equally spaced anchors for `t=0.5,1,2`;
- SU12:
  - `t=0.5`: approximately `(0.15597,0.51069,0.83333)`;
  - `t=1.0`: approximately `(0.15668,0.50999,0.83333)`;
  - `t=2.0`: approximately `(0.15699,0.50968,0.83333)`.

The member-member distance increases above `1/3` and increases further as `t` falls. Thus government standardization triggers endogenous product-space re-differentiation in the asymmetric SU regime.

This is a witness only, not a theorem or policy equilibrium.

---

## 8. Network-effect necessity

The Stage-3 prompt asked whether network externality could be dropped.

Answer for the preferred architecture: **no**.

Without the compatibility-network asymmetry, the selected circle diagnostic does not generate the SU-specific location force. Network effects are therefore necessary for the currently surviving mechanism.

This does not revive `network effects + compatibility` as an ingredient-level novelty claim; Stage 2 permanently killed that claim.

---

## 9. Prior-art kill audit

### Ruiz (2004)

*Mix-and-Match and International Standardization Policy* is a severe threat. Governments choose foreign-standard recognition, then firms can endogenously choose product characteristics, followed by price competition. The policy result remains robust to endogenous product characteristics.

Therefore C-ESD cannot claim novelty from `government standards policy -> endogenous product differentiation`.

### Jonard & Schenk (2004)

*A note on compatibility and entry in a circular model of product differentiation* combines a circular product space, network goods, compatibility and differentiation. Compatibility makes goods closer substitutes while enlarging network benefits. Importantly, explicit endogenous location choice that could counteract compatibility-induced differentiation loss is not their solved margin. This leaves a narrow firm-side window for C-ESD.

### Gandal & Shy (2001)

*Standardization policy and international trade* already has three countries, government recognition policies, standardization unions, horizontal differentiation, network effects/conversion costs and coalition incentives. IS/SU/SW-type institutional architecture is therefore not novel.

### Klimenko (2009)

Continuous government compatibility policy, network externalities and international agreements are already modeled. `endogenous compatibility depth chosen by governments` is not novel by itself.

### Baake & Boom (2001)

Endogenous product differentiation and compatibility/network effects are already jointly modeled, albeit with private compatibility and vertical quality differentiation.

### Wang & Lyu (2020)

Endogenous horizontal product positioning with network effects and an explicit compatibility-differentiation tradeoff is already available in a private platform setting.

### Barrett & Yang (2001)

International product standards, network effects and redesign costs are already jointly present; redesign cost is not a contribution.

### Brekke, Nuscheler & Straume (2006)

Regulation preceding endogenous location/quality choice is generic spatial-competition prior art. C-ESD must live or die on the standards-coalition-specific feedback.

**Prior-art conclusion:** no audited source in this pass reproduces the full three-country continuous policy-depth -> SU-specific repositioning -> national coalition-stability loop, but every component is crowded. A full interaction theorem is mandatory.

---

## 10. B0 nesting correction

The frozen B0 paper is not literally a fixed-`t` Hotelling/Salop model. Its consumer side uses a vertically indexed type, a network-value term, binary private standard adoption, incompatible-product cost `c`, and fixed adoption cost `F`.

Therefore the proposed statement

`B0 = new model with exogenous t`

is rejected as currently written.

B0 remains the mandatory **structural/institutional** standards-coalition benchmark. Whether C-ESD can be written as a true algebraic generalization requires a policy/primitive mapping that has not yet been established.

---

## 11. Nested benchmark status

### B-EXO / B-X

Exogenous standard-friction environment with endogenous locations is partially solved. It produces the key SU-specific repositioning diagnostic once network topology is included.

### B-T

Endogenous government standard policy with fixed product positions is **not yet uniquely defined** because the policy variable has not been mapped to within-bloc and cross-bloc frictions.

### FULL

Not yet authorized.

A full government welfare/stability test would be premature because different plausible policy maps generate different `t` objects under SU.

---

## 12. Single unresolved architecture question

The remaining condition is:

# **Freeze the continuous standard-policy / B0 benchmark mapping under IS, SU and SW.**

In particular answer jointly:

1. Is the policy primitive a scalar `t`, a compatibility intensity `s`, or a pairwise friction matrix `tau_ij` generated by one scalar intensity?
2. Under SU, which government/bloc chooses the member-member friction and what determines member-outsider friction?
3. Is the bloc decision cooperative among members, Nash among national governments, or imposed by a formal agreement rule?
4. How do IS and SW specialize the same policy primitive without arbitrary regime-specific functions?
5. What restriction/removal produces the relevant B0-style exogenous-policy benchmark?

These are aspects of one architecture choice, not five independent model extensions.

A promising parsimonious family to kill-test is

`tau_ij(rho,s)=t_bar - s` for same-bloc pairs,

`tau_ij(rho,s)=t_bar + eta s` for different-bloc pairs,

with IS/SU/SW differing only through the partition relation. But this is **not frozen** and must not be smuggled into Stage 4 without a separate Stage-3 check.

---

## 13. Candidate propositions

### P1 — Hotelling scale-invariance kill

In the standard full-coverage quadratic Hotelling benchmark without a regime-specific network topology, `t` is multiplicative in operating profits and product locations do not respond to `t`.

Status: **verified diagnostic**.

### P2 — SU-specific strategic re-differentiation

In the three-firm Salop network diagnostic, equal spacing is locally stationary under IS/SW but not under SU. On `0<v/t<1/2`, SU members have a strict outward repositioning incentive.

Status: **verified exact diagnostic**.

### P3 — Deeper standardization strengthens the SU repositioning force

The normalized SU member location gradient becomes more negative as `v/t` rises.

Status: **verified exact sign + numerical interval audit**.

### P4 — Endogenous policy changes coalition stability

There exists a nonempty region where endogenous policy plus endogenous repositioning changes the sign or topology of government coalition incentives relative to exogenous policy or fixed locations.

Status: **UNRESOLVED — this is the Stage-4-worthy theorem only if the policy map survives**.

---

## 14. Referee attacks

1. **Ruiz absorption:** policy followed by endogenous differentiation is old.
2. **Gandal–Shy absorption:** three-country standardization unions with network effects are old.
3. **Combination attack:** C-ESD merely overlays Ruiz on Gandal–Shy.
4. **Anchor-cost artifact:** strategic repositioning exists only because a quadratic redesign cost is chosen to regularize locations.
5. **policy-instrument artifact:** results are generated by an arbitrary rule that lowers within-bloc `t` and raises outsider `t`.
6. **B0 false nesting:** the new model is not actually a generalization of the frozen paper.
7. **welfare incompleteness:** product-space geometry may not map cleanly into three national consumer markets and domestic welfare.

The only successful response to attacks 1–3 is a full interaction result unavailable in the separate benchmarks.

---

## 15. Final Stage-3R verdict

# **CONDITIONAL GO**

C-ESD passes the mechanism-existence test but not the policy/stability test.

Why not NO-GO:

- there is an exact SU-only product-repositioning force generated by the three-country compatibility topology;
- the force varies with `t` through `v/t`;
- an anchored, economically interpretable location game has a concrete numerical `dx*/dt != 0` witness.

Why not GO:

- government policy is not uniquely defined under SU;
- national welfare and coalition deviations therefore cannot yet be compared;
- B0 is not literally recovered by fixing `t`;
- the required stability interaction theorem is still untested.

## 16. Next-stage contract

Remain at **Stage 3**.

Run one focused architecture hardening step only:

> choose and kill-test a single regime-neutral mapping from the formal partition and one continuous standardization intensity into pairwise standard-induced frictions, together with a clearly specified government/bloc decision rule.

If that mapping is economically defensible, recovers an exogenous-policy benchmark, and preserves the SU repositioning mechanism without arbitrary regime-specific primitives, change the verdict to `GO -> Stage 4 Minimal Model`.

If no such mapping survives, terminate C-ESD.

Do not add relative profit, private implementation, dynamics, topology choice, or further policy instruments during this conditional gate.