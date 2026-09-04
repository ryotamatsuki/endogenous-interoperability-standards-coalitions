"""Stage 11R hostile referee diagnostic for the repaired v2 C-ESD manuscript.

This audit targets the identification of the headline contribution.  The frozen
manuscript calls the result a FULL-only interaction of *policy endogeneity* and
*location endogeneity*.  At the canonical witness, however, the repaired policy
optima for both IS and SU are the upper cap.  Therefore a benchmark that fixes
non-singleton harmonization depths exogenously at those FULL equilibrium values
and leaves product locations endogenous must reproduce FULL exactly.

The script documents that fact reproducibly.  It does not change the model.
"""
from __future__ import annotations

import importlib.util
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
P = ROOT / "verification" / "stage04r_cesd_continuation_repair.py"
spec = importlib.util.spec_from_file_location("s4r", P)
s4r = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(s4r)

# Repaired FULL policy optima at the canonical witness.
sI, IS_F = s4r.global_policy_optimum("IS", full=True)
sU, SU_F = s4r.global_policy_optimum("SU", full=True)
assert abs(sI - s4r.SBAR) < 1e-7
assert abs(sU - s4r.SBAR) < 1e-7

# Referee benchmark B-EQ: policy depth is NOT endogenous.  It is fixed at the
# FULL equilibrium value, while product locations remain endogenous.
IS_EQ = s4r.selected_continuation("IS", s4r.SBAR, full=True)
SU_EQ = s4r.selected_continuation("SU", s4r.SBAR, full=True)
assert IS_EQ is not None and SU_EQ is not None

# Because FULL itself chooses the cap, B-EQ and FULL are the same downstream
# games and therefore have the same locations, welfare and coalition ranking.
assert np.allclose(IS_EQ[0], IS_F[0], atol=1e-10)
assert np.allclose(SU_EQ[0], SU_F[0], atol=1e-10)
assert np.allclose(IS_EQ[1], IS_F[1], atol=1e-10)
assert np.allclose(SU_EQ[1], SU_F[1], atol=1e-10)

d_eq = float(SU_EQ[0][0] - IS_EQ[0][0])
d_full = float(SU_F[0][0] - IS_F[0][0])
assert abs(d_eq - d_full) < 1e-10
assert d_eq > 0

# Existing frozen benchmarks remain as reported.
d_bt = float(s4r.SU_T[0][0] - s4r.IS_T[0][0])
d_bx0 = float(s4r.SU_X[0][0] - s4r.IS_X[0][0])
assert d_bt < 0
assert d_bx0 < 0

if __name__ == "__main__":
    print("FULL policy optima IS/SU:", sI, sU)
    print("B-T member gain:", d_bt)
    print("B-X(0-depth) member gain:", d_bx0)
    print("B-EQ(exogenous FULL-depth) member gain:", d_eq)
    print("FULL member gain:", d_full)
    print("STAGE 11R IDENTIFICATION ATTACK: CONFIRMED")
    print("Policy endogeneity is not necessary at the canonical witness; positive")
    print("harmonization depth interacting with endogenous repositioning is sufficient.")
