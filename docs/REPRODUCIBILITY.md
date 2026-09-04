# Reproducibility Guide

Theory authority: `CESD-THEORY-FREEZE-2026-09-04-v2`.

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
make verify   # Stage-4/4R + Stage-7/7R verification + v2 freeze consistency
make outputs  # regenerate manuscript-facing CSV/TeX from repaired Stage-7R chain
make paper    # regenerate outputs and compile paper/main.pdf
make all      # verify + outputs + paper
```

Generated table files under `tables/generated_results.*` are intentionally not committed and must never be hand edited.

## Source-of-truth chain

1. `theory/THEORY_FREEZE_CESD_2026-09-04_v2.md` — submission-authoritative theory freeze.
2. `theory/PROPOSITION_REGISTER_CESD_2026-09-04_v2.md` — proof-status authority.
3. `theory/PARAMETER_WELFARE_VERIFICATION_REGISTER_CESD_2026-09-04_v2.md` — parameter/welfare authority.
4. `verification/stage04_cesd_minimal.py` — baseline algebra and historical benchmark implementation.
5. `verification/stage04r_cesd_continuation_repair.py` — repaired action sets, whole-circle continuation validity, and policy optimization.
6. `verification/stage07_cesd_welfare_generality.py` — exact welfare utilities used by the refresh.
7. `verification/stage07r_cesd_welfare_refresh.py` — repaired welfare decomposition, global-welfare comparison, private/social location wedge, and `gamma_W`.
8. `scripts/generate_outputs.py` — serialization only; manuscript-facing numbers are taken from Stage 7R, which uses Stage 4R.
9. `paper/` — manuscript source; Stage 10R must refresh it to v2 before repeated Stage 11.

## Repaired policy semantics

The policy variable is additional within-coalition harmonization depth. Non-singleton blocs choose depth in `[0,s_bar]`; singleton blocs have depth `0` by definition. A policy-stage welfare value is admissible only when the downstream location profile is a verified whole-circle Nash continuation.

## Historical freeze

The earlier freeze is retained only as provenance. It is not a production authority and must not drive tests, generated tables, or manuscript claims.

## Reproducibility rule

If a reported number changes, first identify which v2 verification object generated it. Do not patch tables or manuscript numbers manually. A theory-changing numerical difference requires theory change control and re-running the affected research stages.
