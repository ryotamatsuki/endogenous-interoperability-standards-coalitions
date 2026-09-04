# Endogenous Interoperability and Standards Coalitions

Theory paper on endogenous standards depth, strategic product repositioning, network effects, national welfare, and standards-coalition stability.

## Canonical status

- Theory freeze: `CESD-THEORY-FREEZE-2026-09-04-v2`
- Workflow: `ryotamatsuki/research-paper-workflow` v1.1
- Workflow SHA: `488e5ab06c207909296a7564eaf9066f7f94319c`
- Current production route: Stage 9R reproducibility refresh -> Stage 10R manuscript refresh -> Stage 11R referee gate
- Journal positioning: unresolved until repeated Stage 11R

The sole authorized main contribution is the interaction-induced coalition-stability reversal documented in the v2 freeze. Do not infer novelty from individual ingredients.

The repaired policy object is **additional within-coalition harmonization depth**: non-singleton standards blocs choose depth, while singleton blocs have no positive depth instrument. Production claims must use verified downstream whole-circle location Nash continuations.

## Repository map

- `theory/` — frozen v2 theory specification, propositions, parameter/welfare/verification register
- `verification/` — Stage-4/4R and Stage-7/7R mathematical/numerical checks
- `scripts/` — deterministic serialization/generation utilities only
- `tests/` — v2 production/freeze consistency gates
- `paper/` — modular LaTeX manuscript source pending Stage 10R refresh
- `references/` — BibTeX source
- `tables/` — generated manuscript-facing tables (not hand edited)
- `literature/` — prior-art and institutional evidence records
- `reviews/` — canonical stage reports
- `decisions/` — research and production decisions
- `docs/REPRODUCIBILITY.md` — environment and commands
- `docs/STAGE10R_WRITING_CONTRACT.md` — manuscript-refresh contract
- `PROVENANCE.md` — project lineage and source-of-truth boundaries

## Reproduce

Python 3.12 is recorded in `.python-version`; Python packages are pinned in `requirements.txt`.

```bash
python3.12 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
make verify
make outputs
make paper
```

Or run the full gate:

```bash
make all
```

`make verify` executes Stage-4 baseline checks, the Stage-4R repaired policy/continuation audit, Stage-7 welfare checks, the Stage-7R repaired welfare refresh, and the v2 freeze-consistency test. `make outputs` generates manuscript-facing CSV/TeX from the repaired Stage-7R chain. `make paper` compiles the current manuscript source using `latexmk`.

## Theory change control

The theory is frozen under v2. Any change to players, timing, policy map, utility/demand, costs, equilibrium concept, proposition statements, welfare claims, or post-freeze exclusions requires a formal theory-change record and re-running the affected workflow gates. Stage 10R may refresh writing; it may not silently redesign the model.
