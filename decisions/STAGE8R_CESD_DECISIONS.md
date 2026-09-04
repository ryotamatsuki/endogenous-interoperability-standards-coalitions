# Stage 8R Decisions — C-ESD

Date: 2026-09-04
Freeze ID: `CESD-THEORY-FREEZE-2026-09-04-v2`

## D-041 — Supersede v1 with repaired v2 freeze

Decision: `CESD-THEORY-FREEZE-2026-09-04-v2` is the submission-authoritative theory specification. v1 remains provenance only.

Reason: Stage 11 exposed an off-path continuation gap caused by giving singleton blocs positive harmonization-depth instruments; Stage 4R repaired that action set and Stage 7R confirmed the welfare package survives.

## D-042 — Harmonization depth exists only inside non-singleton coalitions

Decision:

- `s_C in [0,s_bar]` for `|C|>=2`;
- `s_C=0` for `|C|=1`.

Interpretation: `s_C` is additional within-coalition harmonization depth conditional on formal regime membership.

## D-043 — Pairwise friction map remains unchanged

Decision:

- same bloc: `tau_ij=t_bar-s_C`;
- different blocs: `tau_ij=t_bar+(s_C+s_D)/2`.

Under SU with singleton outsider, cross-bloc friction is `t_bar+s_SU/2`.

The `1/2` coefficient remains a normalization, not a structural empirical claim.

## D-044 — Actual continuation equilibrium required inside policy evaluation

Decision: Policy-stage welfare may not be computed from a fixed-order stationary location candidate unless that candidate is a genuine downstream whole-circle location Nash equilibrium.

Stage 4R continuation verification is canonical evidence for the witness.

## D-045 — Headline contribution remains unchanged

Decision: retain only

`Delta_M^(B-T)<0`,

`Delta_M^(B-X)<0`,

`Delta_M^(FULL)>0`

as the main contribution candidate. No ingredient-level novelty claim is revived.

## D-046 — Proof-status discipline strengthened

Decision:

- demand, regular price equilibrium, fixed-order location characterization, national-welfare identity, and world-welfare identity: `PROVED`;
- SU re-differentiation and FULL-only reversal: `CONDITIONAL`;
- repaired full-policy-domain continuation validity at canonical primitives, witness global-welfare ranking, and private/social location wedge: `NUMERICALLY SUPPORTED ONLY`.

No closed-form global parameter-space theorem is claimed.

## D-047 — Remove structural lower gamma_GBR language from v2

Decision: do not freeze an approximate lower `gamma_GBR` threshold as a structural object. Use Stage 4R direct continuation verification for canonical regularity. Retain `gamma_W≈0.132983` as an audited upper welfare threshold on the selected branch.

## D-048 — Welfare levels explicitly net of baseline utility A

Decision: any reported numerical CS/GW levels must be described as net of the common baseline utility `A`; welfare differences and rankings are unaffected.

## D-049 — Downstream route

Decision: Stage 8R verdict is `THEORY FROZEN — GO TO STAGE 9R`. Stage 9R must refresh reproducibility pointers to v2; Stage 10R must refresh manuscript language; Stage 11R must pass before Stage 12 journal positioning.
