# Stage 3 C-ESD Policy-Map Hardening

Date: 2026-09-04
Canonical workflow: `ryotamatsuki/research-paper-workflow` v1.1
Release SHA: `488e5ab06c207909296a7564eaf9066f7f94319c`

## Executive verdict

**GO -> GO TO STAGE 4 MINIMAL MODEL.**

The single unresolved architecture question from the prior C-ESD `CONDITIONAL GO` has been resolved without adding a new mechanism, a policy cost, relative profit, private interoperability investment, dynamics, or regime-specific free parameters.

The Stage-4 baseline now has one regime-neutral rule mapping the formal standards partition and one scalar depth/specificity choice per standards bloc into pairwise standard-induced Hotelling/Salop frictions.

The central C-ESD mechanism remains:

`rho -> bloc standard depth -> pairwise standard friction -> firm product repositioning -> prices -> national welfare -> coalition stability`.

This GO is an authorization to test the complete model. It is **not** a finding that a coalition-stability reversal is true.

## 1. Problem being hardened

The previous Stage-3R diagnostic established a firm-side result:

- simple two-firm Hotelling is killed by scale invariance;
- symmetric two-firm network effects do not rescue it;
- three-firm SU compatibility asymmetry generates a strict strategic repositioning force;
- lower common friction strengthens that SU force;
- an anchored Salop witness gives `dx*/dt != 0`.

But `t_SU` was not a well-defined scalar because SU has two pair types: member-member and member-outsider.

The hardening task was therefore to define one non-arbitrary policy map and one policy decision rule for IS, SU and SW.

## 2. Selected policy primitive

For each standards bloc `C` in the formal partition `rho`, introduce

`s_C in [0,s_bar]`, `s_bar<t_bar`.

Interpret `s_C` as the coherence/specificity depth of the bloc's standard.

The realized product-space standard friction is pairwise and denoted `tau_ij`.

This is the minimum departure from the user's original scalar-`t` intuition that is required by SU: a single realized `t` cannot simultaneously describe a lower member-member friction and a higher member-outsider friction.

## 3. Frozen mapping

If `i` and `j` belong to the same bloc `C`,

`tau_ij = t_bar-s_C`.

If they belong to different blocs `C` and `D`,

`tau_ij = t_bar+(s_C+s_D)/2`.

The same mapping applies under every partition.

### IS

`tau_12=tau_13=tau_23=t_bar-s_I`.

### SU_12

`tau_12=t_bar-s_12`,

`tau_13=tau_23=t_bar+(s_12+s_3)/2`.

Thus deeper bloc-12 standardization lowers differentiation between 1 and 2 while increasing differentiation between either member and outsider 3.

### SW

`tau_ij=t_bar+(s_i+s_j)/2` for every pair.

National standard specificity increases cross-country standard differentiation.

## 4. Why this is not a regime-specific assumption

The map depends only on whether two countries are in the same formal bloc and on the two relevant bloc depths. It does not contain an `IS` coefficient, an `SU` coefficient, or an `SW` coefficient.

Relabelling countries relabels the matrix and changes nothing else.

At zero depth,

`s_C=0 for every C`,

all partitions give

`tau_12=tau_13=tau_23=t_bar`.

This provides a clean C-ESD exogenous-policy benchmark.

## 5. Why the cross slope is exactly 1/2

A free `eta` multiplying cross-bloc friction would create an avoidable extra parameter and invite a referee claim that the SU result is tuned through external discrimination.

Instead normalize the SU depth margin as a redistribution of pairwise standard differentiation.

For `SU_12`, with outsider specificity fixed at zero, raising `s_12` by `ds`:

- reduces the single internal pair friction by `ds`;
- raises two external pair frictions symmetrically.

If each external pair rises by `lambda ds`, preservation of mean pairwise friction requires

`-1+2 lambda=0`,

so

`lambda=1/2`.

Hence, holding `s_3=0`,

`tau_12+tau_13+tau_23=3 t_bar`.

This property is economically useful: SU integration does not mechanically improve or worsen average standard differentiation. It **reallocates** differentiation from inside the bloc to its boundary. Any welfare result must come from who is made closer/farther and from endogenous firm repositioning, not from a built-in average-friction shift.

## 6. Policy decision rule

After a formal partition is fixed, every standards bloc chooses one depth scalar.

Bloc `C` solves

`max_{s_C in [0,s_bar]} Omega_C`,

where

`Omega_C = sum_{i in C} W_i`.

Blocs choose simultaneously, taking other bloc depths as given and anticipating the location and price continuation equilibrium.

Thus:

- IS: the unique bloc `{1,2,3}` chooses `s_I`;
- SU_12: bloc `{1,2}` chooses `s_12`, while singleton `{3}` chooses `s_3`;
- SW: the three singleton governments choose `s_1,s_2,s_3` noncooperatively.

This is a Nash game among standards blocs.

In the symmetric main model, members of a multi-country bloc have identical continuation welfare, so maximizing the bloc sum is equivalent to maximizing the common member welfare. No transfers or bargaining weights are required in the baseline.

The institutional interpretation is consistent with standardization-union models in which a union sets a common standards policy toward members/nonmembers, while nonmembers retain their national policy.

## 7. Network externality freeze

The formal partition continues to determine the network-compatibility graph:

- IS: all firms belong to one network;
- SU: the two members share a network and the outsider does not;
- SW: three separate networks.

The network-effect coefficient `v` is held fixed with respect to `s_C` in the Stage-4 baseline.

This is deliberate. Letting depth simultaneously alter both `tau_ij` and the size of the network benefit would create two continuous policy channels and make it harder to identify the strategic repositioning mechanism.

Depth-dependent network strength may be examined only later as robustness.

## 8. Policy costs

No direct convex policy cost is added to force an interior `s_C`.

If the government optimum is at a boundary, that is an admissible Stage-4 result.

Any future policy cost would need an independent institutional/technological interpretation and cannot be used to rescue the theorem.

## 9. National welfare and continuation values

Retain

`W_i=CS_i+Pi_i`,

with foreign-firm profit excluded from country `i`'s welfare.

Stage 4 must microfound national consumer allocation in the Salop implementation and define worldwide domestic-firm profit consistently before coalition comparisons are certified.

For each partition,

`V_i(rho)=W_i(rho,s*(rho),x*(rho,s*),p*(rho,s*,x*))`.

Coalition blocking/deviation tests use these regime-specific continuation values.

## 10. Correct benchmark interpretation

The C-ESD zero-depth benchmark is

`all s_C=0`.

This recovers exogenous equal pairwise standard friction `t_bar` within the new spatial model.

It does **not** algebraically recover the frozen B0 paper, which uses different demand primitives, conversion cost `c`, network value and binary private adoption cost `F`.

B0 remains the mandatory institutional/coalition benchmark.

## 11. Stage-4 frozen benchmark decomposition

Stage 4 must compare:

### B-EXO / B-X

`all s_C=0`, firms choose locations, then prices.

### B-T

blocs choose `s_C`, product locations fixed at inherited anchors, then prices.

### FULL

blocs choose `s_C`, firms choose locations, then prices.

The FULL model only qualifies as a contribution if the endogenous-policy x endogenous-location interaction changes a government-welfare or coalition-stability result unavailable from B-T and B-X separately.

## 12. Referee attacks considered

### Attack A — external discrimination is assumed

Response: SU depth is normalized to preserve mean pairwise friction when outsider specificity is held at zero. One internal pair becomes closer and two external pairs become equally farther; the `1/2` coefficient is pinned down by this redistribution condition.

### Attack B — coalition objective is arbitrary

Response: in the symmetric baseline, all members have identical welfare, so sum maximization, equal-weight bargaining and maximizing representative-member welfare coincide.

### Attack C — outsider should also have a policy

Response: it does. Every formal bloc, including a singleton, chooses `s_C` under the same rule.

### Attack D — a scalar t was promised

Response: under IS a scalar friction remains sufficient; under SU it is mathematically impossible for one realized scalar to represent both lower member-member and higher member-outsider differentiation. The minimum coherent generalization is one scalar policy depth per bloc plus a derived pairwise friction matrix.

### Attack E — network depth should also be continuous

Response: that is a separate extension. The baseline intentionally fixes network intensity conditional on formal membership to identify C-ESD cleanly.

## 13. Literature check relevant to the policy rule

The policy rule is institutionally consistent with the existing standards literature rather than being introduced solely for this model. Gandal and Shy's standardization-union framework explicitly allows a union to set a common standardization policy toward nonmembers. The mutual-recognition/harmonization literature likewise treats recognition/harmonization as government-level or intergovernmental policy arrangements.

This does not establish novelty. It supports the institutional admissibility of bloc-level policy choice.

## 14. Verification

`verification/stage03r_cesd_policy_map.py` checks:

- IS symmetry;
- SU within/cross signs;
- SW pairwise aggregation;
- zero-depth partition invariance;
- exact SU mean-friction preservation;
- `lambda=1/2` normalization.

Local execution: PASS.

## 15. Final verdict

**GO -> GO TO STAGE 4 MINIMAL MODEL.**

The C-ESD conditional architecture question is resolved.

Freeze for Stage 4:

`rho -> bloc depths s_C -> pairwise Tau(rho,s) -> firm locations x_i -> prices -> W_i -> coalition stability`.

Do not add relative profit, private interoperability investment, endogenous network intensity, policy costs, dynamics, lobbying, transfers or additional countries at Stage 4.

Stage 4 must now determine whether the fully specified game actually has a valid equilibrium and whether endogenous product repositioning changes coalition stability relative to B-T and B-X. Failure of that theorem-level test is a Stage-4 NO-GO, not grounds to modify the frozen map silently.
