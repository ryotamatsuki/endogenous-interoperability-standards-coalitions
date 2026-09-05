# Stage 4R4A C-ESD Decisions

Date: 2026-09-06

## Canonical decisions

1. The spatial consumer-allocation architecture remains terminated.
2. Stage 4R4A freezes one affine-demand map:
   - `delta_ij=1-cos(2*pi*(x_i-x_j))`;
   - `B_ii=1`;
   - `B_ij=beta/[1+tau_ij+delta_ij]`;
   - `K=B-vG_rho`.
3. The existing standards-depth map `tau_ij(rho,s)` and formal network matrix `G_rho` are retained.
4. The sufficient global regularity region is defined by
   - `0<v<beta*m_min`;
   - `2*k_max<1`;
   - `k_min>k_max^2`,
   with `m_min=1/(3+t_bar+s_bar)`, `m_max=1/(1+t_bar-s_bar)`, `k_min=beta*m_min-v`, `k_max=beta*m_max`.
5. In this region, demand is strictly concave and gross-substitute for every admissible upstream history.
6. The Bertrand continuation uses the globally nonnegative affine-demand extension derived from quadratic representative-consumer utility. It is not permissible to use negative quantities as economic demand.
7. Price continuation status in the maintained region is `SOLVED_EQUILIBRIUM`; no failed solver/branch may stand in for a deviation check.
8. Repositioning remains `y_i in [-1/2,1/2]` with cost `gamma*y_i^2/2`.
9. For `gamma>M`, where `M` is the global own-curvature bound on operating profit, the repositioning game has a pure equilibrium by own strict concavity.
10. Exact SU_12 anchor differentiation shows the member repositioning gradient is nonzero and becomes more outward at positive depth; this is a mechanism witness only.
11. The following contribution claims are permanently prohibited:
    - affine/nonnegative demand as novelty;
    - unique Bertrand pricing as novelty;
    - product-variety networks as novelty;
    - generic compatibility plus endogenous differentiation as novelty;
    - generic compatibility-induced differentiation as novelty;
    - endogenous product design under linear demand as novelty.
12. Modern prior-art threats that must remain in the record include Farahat–Perakis (2010), Ushchev–Zenou (2018), Baake–Boom (2001), Barrett–Yang (2001), Cheng–Huang (2025), and Rodrigues (2026).
13. The only surviving contribution route is the full three-country government standards-bloc depth -> post-policy costly horizontal repositioning -> Bertrand welfare -> coalition-stability interaction.
14. Novelty classification remains `DISTINCT BUT NARROW` and is not yet sufficient for IJIO.
15. All old spatial-model policy, welfare, reversal and coalition-stability numbers remain historical only.
16. Stage 4R4A is a project subgate, not canonical Stage 4 completion.

## Verdict

**STAGE 4R4A GO — CONTINUE WITHIN STAGE 4.**

Next project substage:

**Stage 4R4B — Affine-Demand Policy, Welfare, Reversal & Coalition Reconstruction.**

Stage 4R4B must generate at least one welfare or coalition-stability result that requires both endogenous standards depth and endogenous repositioning. Failure terminates the paper rather than authorizing another architecture search.
