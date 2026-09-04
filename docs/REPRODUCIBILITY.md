# Reproducibility Guide

Theory authority: `CESD-THEORY-FREEZE-2026-09-04-v1`.

## Environment

- Python: 3.12
- Python dependencies: `requirements.txt`
- LaTeX: `latexmk` plus a standard TeX Live distribution with `amsmath`, `amsthm`, `booktabs`, `natbib`, `hyperref`, and `geometry`.

Recommended setup:

```bash
python3.12 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## One-command gates

```bash
make verify   # Stage-4 and Stage-7 verification + freeze consistency
make outputs  # regenerate manuscript-facing CSV/TeX from verification modules
make paper    # regenerate outputs and compile paper/main.pdf
make all      # verify + outputs + paper
```

Generated table files under `tables/generated_results.*` are intentionally not committed and must never be hand edited.

## Source-of-truth chain

1. `theory/THEORY_FREEZE_CESD_2026-09-04.md` — theory authority.
2. `theory/PROPOSITION_REGISTER_CESD_2026-09-04.md` — proof-status authority.
3. `verification/stage04_cesd_minimal.py` — equilibrium / benchmark / global-BR checks.
4. `verification/stage07_cesd_welfare_generality.py` — welfare decomposition and social-location checks.
5. `scripts/generate_outputs.py` — serialization only; it must not reimplement model logic.
6. `paper/` — manuscript source; Stage 10 may write against the freeze only.

## Reproducibility rule

If a reported number changes, first identify which frozen verification object generated it. Do not patch tables or manuscript numbers manually. A theory-changing numerical difference requires theory change control and re-running the affected research stages.
