"""Production consistency gate for the Stage-8R v2 theory freeze."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

state = (ROOT / "PROJECT_STATE.md").read_text(encoding="utf-8")
freeze = (ROOT / "theory" / "THEORY_FREEZE_CESD_2026-09-04_v2.md").read_text(encoding="utf-8")
props = (ROOT / "theory" / "PROPOSITION_REGISTER_CESD_2026-09-04_v2.md").read_text(encoding="utf-8")
params = (ROOT / "theory" / "PARAMETER_WELFARE_VERIFICATION_REGISTER_CESD_2026-09-04_v2.md").read_text(encoding="utf-8")
generator = (ROOT / "scripts" / "generate_outputs.py").read_text(encoding="utf-8")

V2 = "CESD-THEORY-FREEZE-2026-09-04-v2"
V1 = "CESD-THEORY-FREEZE-2026-09-04-v1"

for text in (state, freeze, props, params, generator):
    assert V2 in text, V2

for token in [
    "Delta_M^(B-T)<0",
    "Delta_M^(B-X)<0",
    "Delta_M^(FULL)>0",
]:
    assert token in state or token in freeze or token in props, token

# Repaired policy semantics must be explicit in the canonical freeze/state.
combined = state + "\n" + freeze
assert "singleton" in combined.lower()
assert "s_C=0" in combined or "s_C = 0" in combined
assert "additional within-coalition harmonization depth" in combined

for path in [
    ROOT / "verification" / "stage04_cesd_minimal.py",
    ROOT / "verification" / "stage04r_cesd_continuation_repair.py",
    ROOT / "verification" / "stage07_cesd_welfare_generality.py",
    ROOT / "verification" / "stage07r_cesd_welfare_refresh.py",
    ROOT / "paper" / "main.tex",
    ROOT / "references" / "references.bib",
    ROOT / "docs" / "STAGE10R_WRITING_CONTRACT.md",
]:
    assert path.exists(), path

# Manuscript-facing serialization must use the repaired verification chain.
assert "stage07r_cesd_welfare_refresh.py" in generator
assert "stage04_cesd_minimal.py" not in generator
assert "stage07_cesd_welfare_generality.py" not in generator

# Superseded v1 may remain in historical records, but never as production authority.
production_paths = [
    ROOT / "README.md",
    ROOT / "docs" / "REPRODUCIBILITY.md",
    ROOT / "PROVENANCE.md",
    ROOT / "scripts" / "generate_outputs.py",
    ROOT / "docs" / "STAGE10R_WRITING_CONTRACT.md",
]
for path in production_paths:
    text = path.read_text(encoding="utf-8")
    assert V2 in text, path
    assert V1 not in text, path

print("v2 freeze consistency: PASS")
