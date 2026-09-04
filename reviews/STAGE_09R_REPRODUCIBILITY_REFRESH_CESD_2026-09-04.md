# Stage 9R — Repository / Reproducibility Refresh: C-ESD

Date: 2026-09-04
Canonical workflow: `ryotamatsuki/research-paper-workflow` v1.1
Workflow SHA: `488e5ab06c207909296a7564eaf9066f7f94319c`
Submission-authoritative freeze: `CESD-THEORY-FREEZE-2026-09-04-v2`

## Executive verdict

**REPRODUCIBILITY REFRESH READY — GO TO STAGE 10R MANUSCRIPT REFRESH.**

Stage 9R changes no theory. It migrates the production/reproducibility path from the superseded pre-repair freeze to the repaired v2 freeze and verified Stage-4R / Stage-7R continuation chain.

## Production authority after refresh

1. `theory/THEORY_FREEZE_CESD_2026-09-04_v2.md` — theory authority.
2. `theory/PROPOSITION_REGISTER_CESD_2026-09-04_v2.md` — proof-status authority.
3. `theory/PARAMETER_WELFARE_VERIFICATION_REGISTER_CESD_2026-09-04_v2.md` — parameter/welfare authority.
4. `verification/stage04r_cesd_continuation_repair.py` — repaired action sets and downstream whole-circle continuation validity.
5. `verification/stage07r_cesd_welfare_refresh.py` — repaired welfare/generality outputs.
6. `scripts/generate_outputs.py` — serialization from Stage 7R only; no model reimplementation.
7. `docs/STAGE10R_WRITING_CONTRACT.md` — manuscript-refresh contract.

Historical pre-repair freeze/materials remain provenance only.

## Changes completed

### Freeze consistency

`tests/test_freeze_consistency.py` now checks the v2 freeze/registers, repaired singleton action-set semantics, Stage-4R/7R verification artifacts, and the Stage-10R writing contract. It also forbids the superseded freeze ID in active production documentation/generation paths.

### Manuscript-facing output generation

`generate_outputs.py` no longer serializes pre-repair Stage-4 / Stage-7 objects directly. It imports `stage07r_cesd_welfare_refresh.py`, which in turn uses the repaired Stage-4R continuation and policy evaluation.

Generated rows therefore come from the repaired chain for:

- `Delta_M^(B-T)`;
- `Delta_M^(B-X)`;
- `Delta_M^(FULL)`;
- member CS and domestic-profit components;
- IS/SU/SW global welfare, explicitly net of common baseline utility `A`;
- private/social SU member distance;
- `gamma_W`.

### Documentation/provenance

README, reproducibility guidance, and provenance now identify v2 as the sole submission-oriented authority and explain the repaired policy semantics: only non-singleton blocs choose additional within-coalition harmonization depth; singleton depth equals zero.

The old Stage-10 writing contract is marked historical and Stage 10R has a new v2 contract.

## CI / build result

On PR #47, the reproducibility workflow passed all steps on the Stage-9R candidate head:

1. Python 3.12 setup — PASS;
2. pinned Python dependencies — PASS;
3. `make verify` including Stage 4R / Stage 7R and v2 freeze consistency — PASS;
4. repaired manuscript-facing output generation — PASS;
5. LaTeX environment installation — PASS;
6. manuscript PDF build via `latexmk` — PASS.

Thus the repaired v2 results can be reproduced and the existing manuscript source still compiles before its Stage-10R content refresh.

## Theory-change audit

No player, timing, policy map, utility, network structure, cost, welfare definition, equilibrium concept, benchmark, proposition, numerical witness, or contribution claim was changed in Stage 9R.

The only substantive production change is source-of-truth routing from superseded pre-repair objects to repaired v2 verification objects.

## Remaining work

The manuscript text itself still reflects pre-repair wording in places. Stage 10R must:

- replace any implication that singleton blocs choose positive depth;
- describe `s_C` as additional within-coalition harmonization depth;
- state that policy evaluation requires verified downstream whole-circle location Nash continuations;
- align proposition wording with the v2 proof-status register;
- label reported global-welfare levels net of common `A`;
- retain the narrow FULL-only interaction contribution and all Stage-11 referee risks.

## Canonical verdict

**STAGE 9R PASS — REPRODUCIBILITY / PRODUCTION AUTHORITY MIGRATED TO v2.**

Proceed to **Stage 10R — Manuscript Refresh**. No theory changes are authorized there.