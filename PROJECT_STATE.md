# Project State

Last updated: 2026-09-04

## Canonical status

- Project: Endogenous Interoperability and Standards Coalitions
- Working title: **Standards Coalitions and Strategic Product Repositioning**
- Canonical workflow: `ryotamatsuki/research-paper-workflow` v1.1
- Workflow release SHA: `488e5ab06c207909296a7564eaf9066f7f94319c`
- Theory freeze: **`CESD-THEORY-FREEZE-2026-09-04-v2`**
- Theory status: **FROZEN — unchanged**
- Production manuscript refresh: **COMPLETE AND MERGED**
- Repeated referee gate: **Stage 11R2 COMPLETE**
- Stage 11R2 final verdict: **GO TO JOURNAL POSITIONING**
- Stage 12 journal positioning: **COMPLETE ON `stage12-journal-positioning`**
- Stage 12 verdict: **PRIMARY JOURNAL SELECTED — GO TO INTEGRATION**
- Primary target journal: **International Journal of Industrial Organization (IJIO)**
- Default submission ladder: **IJIO -> Review of Industrial Organization -> Journal of Industry, Competition and Trade**
- Optional stretch: **The Journal of Industrial Economics**
- Next formal stage: **Stage 13 — Full Paper Integration for IJIO**

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

The pre-specified local parameter-region audit varied `v`, `gamma`, and `s_bar` separately and jointly before results were observed.

GitHub Actions workflow run `33874450205` completed successfully with:

- `valid_points=9/9`;
- `reversal_points=9/9`.

Every pre-specified point satisfies:

`Delta_M^(B-T) < 0 < Delta_M^(FULL)`.

This closes the principal knife-edge numerical-witness attack. It does not establish global robustness or generality across alternative demand systems, reversed timing, or `v=0`.

Authority: `reviews/STAGE_11R2_FINAL_CLOSURE_CESD_2026-09-04.md`.

## Stage 12 journal positioning

Primary target: **International Journal of Industrial Organization**.

Reason: the paper is fundamentally an IO theory paper about strategic product repositioning, price competition and welfare after standards policy; IJIO explicitly welcomes theoretical work on strategic behavior, market structure, regulation and technological change, and recent IJIO work confirms active interoperability/network-effects fit.

Journal ladder:

1. Optional stretch — **The Journal of Industrial Economics**
2. Primary — **International Journal of Industrial Organization**
3. Realistic fallback — **Review of Industrial Organization**
4. Safety net — **Journal of Industry, Competition and Trade**

`Information Economics and Policy` was considered but excluded from the main ladder because choosing it would push the paper toward an unnecessarily digital/information-industry-specific framing.

Authority:

- `reviews/STAGE_12_JOURNAL_POSITIONING_CESD_2026-09-04.md`
- `decisions/STAGE12_CESD_DECISIONS.md`

## Permanently prohibited claims

Do not claim novelty from the setup ingredients alone, including government standards policy, compatibility/network effects, partial compatibility, continuous harmonization, strategic response to interoperability, Salop/network structures, endogenous positioning under network effects, regional standards coalitions, or regional blocking of multilateral standards.

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

## Stage 13 contract

Stage 13 may integrate and polish the full manuscript for IJIO, but may not change the frozen theory without reopening an earlier stage.

Stage 13 must:

1. foreground strategic post-policy product repositioning;
2. keep B-T vs FULL/B-EQ as the central comparison;
3. integrate the 9/9 robustness result into the manuscript/appendix;
4. preserve the consumer-loss / producer-rent / world-welfare decomposition;
5. retain explicit closest-paper differentiation;
6. preserve limitation language around normalization and scope;
7. add the current Elsevier generative-AI disclosure reflecting actual use;
8. keep CI/reproducibility green.

## Current verdict

**STAGE 12 COMPLETE — PRIMARY JOURNAL SELECTED: IJIO — GO TO STAGE 13 FULL PAPER INTEGRATION.**
