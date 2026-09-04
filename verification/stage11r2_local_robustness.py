"""Repeated Stage 11R frozen-model local robustness audit.

This script does not change the model. It pre-specifies a compact perturbation set
around the canonical witness and recomputes B-T and FULL globally under the repaired
v2 action set. The purpose is to test whether the sign reversal is more than a
single numerical witness.

Pre-specified points (chosen before execution):
- canonical: (v,gamma,sbar)=(0.040,0.110,0.250)
- one-at-a-time perturbations:
  v in {0.035,0.045}; gamma in {0.105,0.115}; sbar in {0.225,0.275}
- joint perturbations:
  low joint=(0.035,0.105,0.225)
  high joint=(0.045,0.115,0.275)

Every point is reported. No invalid or sign-failing point is silently dropped.
"""
from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
P = ROOT / "verification" / "stage04r_cesd_continuation_repair.py"
spec = importlib.util.spec_from_file_location("s4r", P)
s4r = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(s4r)

POINTS = [
    ("canonical", 0.040, 0.110, 0.250),
    ("v_low",     0.035, 0.110, 0.250),
    ("v_high",    0.045, 0.110, 0.250),
    ("gamma_low", 0.040, 0.105, 0.250),
    ("gamma_high",0.040, 0.115, 0.250),
    ("sbar_low",  0.040, 0.110, 0.225),
    ("sbar_high", 0.040, 0.110, 0.275),
    ("joint_low", 0.035, 0.105, 0.225),
    ("joint_high",0.045, 0.115, 0.275),
]


def solve_point(label: str, vv: float, gamma: float, sbar: float):
    try:
        s_i_bt, is_bt = s4r.global_policy_optimum("IS", vv=vv, gamma=gamma, sbar=sbar, full=False)
        s_u_bt, su_bt = s4r.global_policy_optimum("SU", vv=vv, gamma=gamma, sbar=sbar, full=False)
        s_i_f, is_f = s4r.global_policy_optimum("IS", vv=vv, gamma=gamma, sbar=sbar, full=True)
        s_u_f, su_f = s4r.global_policy_optimum("SU", vv=vv, gamma=gamma, sbar=sbar, full=True)
    except Exception as exc:
        return {
            "label": label, "v": vv, "gamma": gamma, "sbar": sbar,
            "status": "invalid", "error": repr(exc),
        }

    if any(z is None for z in (is_bt, su_bt, is_f, su_f)):
        return {
            "label": label, "v": vv, "gamma": gamma, "sbar": sbar,
            "status": "invalid", "error": "missing continuation",
        }

    d_bt = float(su_bt[0][0] - is_bt[0][0])
    d_full = float(su_f[0][0] - is_f[0][0])
    reversal = d_bt < 0.0 < d_full
    return {
        "label": label, "v": vv, "gamma": gamma, "sbar": sbar,
        "status": "reversal" if reversal else "no_reversal",
        "d_bt": d_bt, "d_full": d_full,
        "s_i_bt": float(s_i_bt), "s_u_bt": float(s_u_bt),
        "s_i_full": float(s_i_f), "s_u_full": float(s_u_f),
    }


if __name__ == "__main__":
    rows = [solve_point(*p) for p in POINTS]
    print("STAGE 11R2 LOCAL ROBUSTNESS — PRE-SPECIFIED GRID")
    for r in rows:
        print(r)

    base = rows[0]
    assert base["status"] == "reversal"
    assert abs(base["d_bt"] - (-0.010167)) < 5e-4
    assert abs(base["d_full"] - 0.001571) < 5e-4

    valid = [r for r in rows if r["status"] != "invalid"]
    reversals = [r for r in valid if r["status"] == "reversal"]
    print(f"valid_points={len(valid)}/{len(rows)}")
    print(f"reversal_points={len(reversals)}/{len(valid)}")
    print("STAGE 11R2 ROBUSTNESS SCRIPT COMPLETE")
