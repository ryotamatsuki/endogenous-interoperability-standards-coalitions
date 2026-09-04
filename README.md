# Endogenous Interoperability and Standards Coalitions

Theory paper on endogenous standards depth, strategic product repositioning, network effects, national welfare, and standards-coalition stability.

## Canonical status

- Theory freeze: `CESD-THEORY-FREEZE-2026-09-04-v1`
- Workflow: `ryotamatsuki/research-paper-workflow` v1.1
- Workflow SHA: `488e5ab06c207909296a7564eaf9066f7f94319c`
- Current production route: Stage 9 reproducibility setup → Stage 10 manuscript construction
- Recommended journal level: IJIO / field-journal full paper

The sole authorized main contribution is the interaction-induced coalition-stability reversal documented in the Stage-8 freeze. Do not infer novelty from individual ingredients.

## Repository map

- `theory/` — frozen theory specification, propositions, parameter/welfare/verification register
- `verification/` — canonical Stage-4 and Stage-7 mathematical/numerical checks
- `scripts/` — deterministic serialization/generation utilities only
- `tests/` — cheap production/freeze consistency gates
- `paper/` — modular LaTeX manuscript scaffold
- `references/` — BibTeX source
- `tables/` — generated manuscript-facing tables (not hand edited)
- `literature/` — prior-art and institutional evidence records
- `reviews/` — canonical stage reports
- `decisions/` — research and production decisions
- `docs/REPRODUCIBILITY.md` — environment and commands
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

`make verify` executes the frozen Stage-4 equilibrium/global-deviation checks, Stage-7 welfare/generality checks, and Stage-8 freeze-consistency test. `make outputs` generates manuscript-facing CSV/TeX directly from those verification modules. `make paper` compiles the current manuscript scaffold using `latexmk`.

## Theory change control

The theory is frozen. Any change to players, timing, policy map, utility/demand, costs, equilibrium concept, proposition statements, welfare claims, or post-freeze exclusions requires a formal theory-change record and re-running the affected workflow gates. Stage 10 may write; it may not silently redesign the model.
