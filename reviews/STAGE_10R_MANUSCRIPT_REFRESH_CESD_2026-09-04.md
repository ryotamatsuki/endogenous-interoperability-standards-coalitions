# Stage 10R — Manuscript Refresh: C-ESD

Date: 2026-09-04
Canonical workflow: `ryotamatsuki/research-paper-workflow` v1.1
Workflow SHA: `488e5ab06c207909296a7564eaf9066f7f94319c`
Submission-authoritative freeze: `CESD-THEORY-FREEZE-2026-09-04-v2`

## Verdict

**FULL DRAFT REFRESHED UNDER v2 — GO TO STAGE 11R REPEATED ROBUSTNESS / REFEREE ATTACK GATE.**

Stage 10R changes no theory. It refreshes the Stage-10 manuscript so that every model, equilibrium, result, welfare, proof-status, and computation statement matches the repaired v2 freeze and the Stage-4R / Stage-7R production chain.

## Manuscript changes

1. **Policy action set repaired in the text.** `s_C` is now stated consistently as additional within-coalition harmonization depth conditional on the formal regime. Only non-singleton blocs choose `s_C in [0,s_bar]`. Singleton blocs have `s_C=0` by definition and no positive depth instrument.
2. **SU wording repaired.** Under `SU_12`, the member coalition chooses `s_12`; outsider country 3 is a singleton with `s_3=0` by definition. Cross-bloc frictions are therefore `tau_13=tau_23=t_bar+s_12/2`.
3. **SW wording repaired.** Standards war has three singleton blocs and therefore no continuous harmonization-depth policy stage.
4. **Timing repaired.** The policy stage contains only non-singleton harmonization-depth choices; in the present three-country game there is one scalar policy choice under IS, one under each SU, and none under SW.
5. **SPNE continuation wording strengthened.** Policy-stage welfare is evaluated only using downstream location continuations that pass the whole-circle unilateral best-response test after re-solving the price subgame. The canonical full feasible IS/SU policy domain is computationally audited at the canonical primitives.
6. **Proof-status boundary preserved.** Weighted-Laplacian demand, regular price equilibrium, fixed-order location characterization, national-welfare decomposition, and global-welfare identity remain analytic. The FULL-only coalition reversal remains a constructive regular-region result, and full-policy-domain continuation validity remains computational at the canonical primitives rather than a global analytic theorem.
7. **Unsupported v1 robustness wording removed.** The manuscript no longer relies on the old 23/27 and 108/125 neighborhood-count language as submission-authoritative evidence, and it no longer presents a numerical lower `gamma_GBR≈0.10` as if it were part of the v2 frozen result.
8. **World-welfare levels clarified.** Numerical levels are explicitly reported as `GW_rho-A`, net of the common baseline utility `A`.
9. **Appendix computation authority repaired.** Manuscript-facing computation now points to `verification/stage04r_cesd_continuation_repair.py` followed by `verification/stage07r_cesd_welfare_refresh.py` and `scripts/generate_outputs.py`.
10. **Literature/novelty boundary unchanged.** No ingredient-level novelty claim was introduced. The contribution remains the nested FULL-only interaction-induced coalition-ranking reversal.

## Headline result retained

At the canonical witness `(t_bar,v,gamma,s_bar)=(1,0.04,0.11,0.25)`:

- `Delta_M^(B-T)≈-0.010167<0`;
- `Delta_M^(B-X)≈-0.000434<0`;
- `Delta_M^(FULL)≈+0.001571>0`.

Thus B-T and B-X select international standardization while FULL makes the three two-country standardization unions stable and international standardization pair-blockable.

The welfare mechanism is unchanged:

- `Delta CS/3≈-0.0325785`;
- `Delta Pi_M≈+0.0341498`;
- `Delta_M≈+0.0015713`.

World-welfare levels are reported net of `A`:

- `GW_IS-A≈-0.0225000`;
- `GW_SU-A≈-0.0586685`;
- `GW_SW-A≈-0.0700000`.

## Production audit

The manuscript refresh covers:

- `paper/main.tex`;
- Introduction;
- Model;
- Equilibrium Characterization;
- Main Results;
- Welfare, Incidence, and Generality;
- Related Literature;
- Conclusion;
- Proofs and Verification Details appendix.

On the manuscript-content head of PR #49, the reproducibility workflow passed:

- frozen verification gates;
- repaired manuscript-facing output generation;
- LaTeX installation;
- full manuscript PDF build.

The final metadata head must pass the same workflow before merge.

## Stage-11R attack surface

Stage 11R must repeat the hostile review on the repaired manuscript, with particular attention to:

1. whether every policy deviation invoked by the manuscript has a valid downstream continuation under the repaired action set;
2. whether the constructive/open-region wording overstates what Stage 4R proves computationally;
3. whether the coalition stability logic is complete under strict blocking and exclusive membership;
4. whether national versus world-welfare incidence is stated without conflating transfers and real resource costs;
5. whether Ruiz (2004) + Gandal–Shy (2001), or other prior art, absorbs the narrow FULL-only interaction result;
6. whether the paper is strong enough for journal positioning without adding post-freeze theory.

## Final decision

**STAGE 10R PASS — FULL DRAFT REFRESHED UNDER v2.**

Proceed to Stage 11R after final-head CI passes. No theory changes are authorized.