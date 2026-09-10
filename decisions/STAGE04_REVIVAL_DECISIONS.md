# Stage 4 Revival Decisions — C1 Realized Interoperability Depth

Date: 2026-09-10

Workflow: `ryotamatsuki/research-paper-workflow` v2.1.

## D1 — Adopt the C1 Stage-4 construction object

For Stage 4 only, retain the PR #65 affine-demand architecture and replace the source depth-invariant off-diagonal compatibility term by the Stage-3-selected realized-interoperability map

`M_ij=s_C/s_bar`

within a multi-country bloc and zero across blocs.

No other primitive is changed.

## D2 — Keep the linear realization map

`chi(s)=s/s_bar` remains binding.

No nonlinear realization function, policy cost, asymmetry, home bias, bargaining, multi-market extension, heterogeneous repositioning cost, or second standards instrument is authorized.

## D3 — Freeze welfare interpretation

Use

`W_i=CS/3+Pi_i`

with an explicit equal-national-consumer-population interpretation and domestic ownership of firm `i`. This closes the Stage-1 attribution ambiguity for the Stage-4 object.

## D4 — Freeze the blocking correspondence

Use strict residual-membership blocking:

- a deviating coalition forms an exclusive bloc;
- nondeviators preserve residual links where feasible;
- the alternative partition is evaluated at its own policy/location/price continuation;
- every deviator must strictly gain.

This rule governs all Stage-4 stability calculations and is an explicit Stage-4A attack target.

## D5 — Canonical and threshold parameter discipline

Retain source primitives

`a=2, b=10, c0=.30, lambda=.50, t_bar=1, s_bar=.25`.

Retain source/local values

`v=.08, gamma=.03`

and the pre-existing local box

`v in {.07,.08,.09}`, `gamma in {.025,.03,.035}`.

For threshold characterization, allow `v in [.06,.16]`. This wider interval is used to bracket roots after the model is frozen; no other primitive is tuned against the coalition-ranking sign.

## D6 — Policy outcomes in the headline region

Construction verification supports the following upper-bound policy equilibrium throughout the threshold-critical region used for the headline result:

- IS: `s_I=s_bar`;
- SU: `(s_12,s_3)=(s_bar,s_bar)`;
- SW: `(s_1,s_2,s_3)=(s_bar,s_bar,s_bar)`.

IS has an exact sufficient threshold `v>1/18` for the upper-bound result. SU/SW best-response statements remain numerical construction results pending Stage 4A independent certification.

## D7 — Canonical stable-set reversal

At `(v,gamma)=(.08,.03)`:

`B-FIX stable set = {IS}`,

`FULL stable set = {SU_12,SU_13,SU_23}`.

The same difference is reproduced at all nine points of the pre-existing local `(v,gamma)` box.

## D8 — Headline threshold result

Use the SU-member indifference/blocking threshold against IS as the headline candidate object.

At `gamma=.03`:

- `v_FIX=1/15 approximately .06666667` exactly for B-FIX;
- `v_EXO-HIST approximately .11154504`;
- `v_FULL approximately .13368738`.

The strict ordering

`v_FIX < v_EXO-HIST < v_FULL`

is the central Stage-4 construction result.

The B-EXO/FULL ordering also survives `gamma=.025` and `.035`.

## D9 — FULL-only interaction witness

Use `v=.12, gamma=.03` only as a transparent illustration after the threshold ordering is established.

At that point:

- B-FIX -> `{IS}`;
- B-EXO-HIST -> `{IS}`;
- FULL -> `{SU_12,SU_13,SU_23}`.

This demonstrates a region in which neither binding nested benchmark reproduces the FULL stable partition.

## D10 — Historical #65 remains a predecessor, not a certification source

PR #65's fixed-depth welfare reversal remains preserved as historical evidence. The new Stage-4 result does not inherit old Stage 4/8/11/12/13/14 status and does not merge the revival branch into main.

## D11 — Stage-4 verdict

**GO.**

## D12 — Route

**GO TO STAGE 4A — INDEPENDENT MATHEMATICAL ADVERSARIAL CERTIFICATION GATE.**

Stage 4A must independently certify or defeat the construction. It may not repair the theory while certifying it.

No Stage 6, theory freeze, journal target, manuscript revival, or submission authorization is active.
