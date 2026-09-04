"""Cheap consistency gate tying the production scaffold to the Stage-8 freeze."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
state = (ROOT / "PROJECT_STATE.md").read_text(encoding="utf-8")
freeze = (ROOT / "theory" / "THEORY_FREEZE_CESD_2026-09-04.md").read_text(encoding="utf-8")
generator = (ROOT / "scripts" / "generate_outputs.py").read_text(encoding="utf-8")

required = [
    "CESD-THEORY-FREEZE-2026-09-04-v1",
    "Delta_M^(B-T)<0",
    "Delta_M^(B-X)<0",
    "Delta_M^(FULL)>0",
]
for token in required:
    assert token in state or token in freeze, token

for path in [
    ROOT / "verification" / "stage04_cesd_minimal.py",
    ROOT / "verification" / "stage07_cesd_welfare_generality.py",
    ROOT / "paper" / "main.tex",
    ROOT / "references" / "references.bib",
]:
    assert path.exists(), path

assert "stage04_cesd_minimal.py" in generator
assert "stage07_cesd_welfare_generality.py" in generator
assert "CESD-THEORY-FREEZE-2026-09-04-v1" in generator
print("freeze consistency: PASS")
