# Project State

Last updated: 2026-09-04

## Canonical status

- Project: Endogenous Interoperability and Standards Coalitions
- Working title: **Standards Coalitions and Strategic Product Repositioning**
- Canonical workflow: `ryotamatsuki/research-paper-workflow` v1.1
- Workflow release SHA: `488e5ab06c207909296a7564eaf9066f7f94319c`
- Theory freeze: **`CESD-THEORY-FREEZE-2026-09-04-v2`**
- Theory status: **FROZEN — unchanged**
- Stage 11R2: **COMPLETE — GO TO JOURNAL POSITIONING**
- Stage 12: **COMPLETE — PRIMARY JOURNAL SELECTED: IJIO**
- Stage 13: **IN PROGRESS — IJIO FULL-PAPER INTEGRATION**
- Primary target journal: **International Journal of Industrial Organization (IJIO)**
- Submission ladder: **IJIO -> Review of Industrial Organization -> Journal of Industry, Competition and Trade**
- Optional stretch: **The Journal of Industrial Economics**
- Stage 14 submission QA authorized: **NO — pending Stage 13 CI/build closure**

## Frozen contribution

> **Allowing firms to reposition after a standards policy can reverse the member-country welfare ranking between international standardization and a regional standards union relative to a fixed-position evaluation of the same standards architecture, making the regional union stable through producer-rent gains even though member consumers lose and world welfare remains higher under international standardization.**

## Frozen mechanism

Standards architecture -> changed effective competitive distances -> post-policy product repositioning -> softer competition and member producer-rent gain -> national welfare reversal -> coalition-stability reversal.

Endogenous harmonization-depth choice is not part of the necessary causal chain.

## Central identification hierarchy

1. **B-T vs FULL / B-EQ** — central identifying comparison.
2. **B-X0** — auxiliary zero-additional-harmonization benchmark only.
3. **B-EQ** — mandatory disclosure showing policy-depth endogeneity is not necessary at the witness.

The superseded claim that policy endogeneity and product-position endogeneity are jointly necessary is permanently unauthorized.

## Canonical model and witness

Timing:

`rho -> harmonization depths of non-singleton blocs -> pairwise Tau(rho,s) -> product locations x_i -> prices -> W_i -> coalition stability`.

Policy action set:

- `s_C in [0,s_bar]` if `|C|>=2`;
- `s_C=0` if `|C|=1`.

Pairwise friction map:

- same bloc `C`: `tau_ij=t_bar-s_C`;
- different blocs `C,D`: `tau_ij=t_bar+(s_C+s_D)/2`.

Canonical witness:

`(t_bar,v,gamma,s_bar)=(1,0.04,0.11,0.25)`.

FULL policy choices:

- `s_I*=0.25`;
- `s_12*=0.25`.

FULL `SU_12` locations:

`x_SU≈(0.084567,0.582100,0.833333)`.

Welfare-ranking values:

- `Delta_M^(B-T)≈-0.010167`;
- `Delta_M^(B-X0)≈-0.000434`;
- `Delta_M^(B-EQ)=Delta_M^(FULL)≈+0.001571`.

Member welfare decomposition:

- `Delta CS/3≈-0.0325785`;
- `Delta Pi_M≈+0.0341498`;
- `Delta_M≈+0.0015713`.

World welfare:

`GW_IS > GW_SU > GW_SW` at the canonical witness.

## Stage 11R2 robustness closure

Pre-specified local audit over `v`, `gamma`, and `s_bar`:

- `valid_points=9/9`;
- `reversal_points=9/9`;
- every tested point satisfies `Delta_M^(B-T) < 0 < Delta_M^(FULL)`.

This closes the principal knife-edge witness attack locally. It does not establish global robustness or generality across alternative demand systems, reversed timing, or `v=0`.

## Stage 13 IJIO integration

Implemented on branch `stage13-ijio-full-paper-integration`:

1. integrated the full nine-point pre-specified robustness table into Main Results;
2. aligned Introduction and Conclusion with the verified local robustness evidence;
3. preserved B-T vs FULL/B-EQ as the central benchmark hierarchy;
4. reorganized Related Literature by conceptual relationship rather than paper-by-paper cataloguing;
5. updated appendix verification authority through Stage 11R2;
6. added the current Elsevier-style generative-AI declaration reflecting actual manuscript-preparation use of ChatGPT;
7. made no change to primitives, timing, policy map, welfare definition, equilibrium concept, canonical witness, or substantive theory.

Authority:

- `reviews/STAGE_13_IJIO_FULL_PAPER_INTEGRATION_2026-09-04.md`
- `decisions/STAGE13_CESD_DECISIONS.md`

## Permanently prohibited claims

Do not claim novelty from setup ingredients alone, including government standards policy, compatibility/network effects, partial compatibility, continuous harmonization, strategic response to interoperability, Salop/network structures, endogenous positioning under network effects, regional standards coalitions, or regional blocking of multilateral standards.

Do not use `first model`, `first paper`, `first to show`, `novel framework`, or equivalent priority language.

Do not claim that policy-depth endogeneity is necessary.

## Assumption and generality boundary

Essential within the verified mechanism:

- post-policy horizontal product repositioning;
- standards-induced changes in competitive distances;
- domestic producer rents in national welfare;
- coalition stability based on member national welfare.

Not established as essential:

- harmonization-depth endogeneity;
- `v>0`;
- exact cross-bloc `1/2` coefficient;
- specific harmonization cap.

Tractability features remain the symmetric three-country circular structure, `CS/3` incidence, exact pairwise friction normalization and bounded harmonization depth.

No broad generality claim over alternative demand systems or reversed timing is authorized.

## Current verdict

**STAGE 13 IN PROGRESS — INTEGRATION COMPLETE IN CONTENT; CI/BUILD CONFIRMATION REQUIRED BEFORE STAGE 14.**
