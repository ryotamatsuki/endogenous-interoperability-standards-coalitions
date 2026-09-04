"""Stage 7R welfare/generality refresh after the Stage-4R action-set repair.

The Stage-4R repair changes only the policy action set: singleton blocs have
harmonization depth 0 by definition. This script recomputes the Stage-7 welfare
objects using the repaired verified continuations and checks whether the prior
welfare/generality conclusions survive.
"""
from __future__ import annotations

import importlib.util
from pathlib import Path

import numpy as np
from scipy.optimize import brentq

ROOT = Path(__file__).resolve().parents[1]


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


s4r = load("stage04r", ROOT / "verification" / "stage04r_cesd_continuation_repair.py")
s7 = load("stage07", ROOT / "verification" / "stage07_cesd_welfare_generality.py")

V = s4r.V
GAMMA = s4r.GAMMA
SBAR = s4r.SBAR

# Re-solve repaired policy stage.
sI, IS_cont = s4r.global_policy_optimum("IS", V, GAMMA, SBAR, True)
sU, SU_cont = s4r.global_policy_optimum("SU", V, GAMMA, SBAR, True)
sW, SW_cont = s4r.global_policy_optimum("SW", V, GAMMA, SBAR, True)
assert abs(sI - SBAR) < 1e-7
assert abs(sU - SBAR) < 1e-7
assert abs(sW) < 1e-12

# Welfare decomposition is recomputed from the repaired policy vectors.
IS = s7.decompose("IS", s4r.repaired_policy_vector("IS", sI), V, GAMMA, True)
SU = s7.decompose("SU", s4r.repaired_policy_vector("SU", sU), V, GAMMA, True)
SW = s7.decompose("SW", s4r.repaired_policy_vector("SW", sW), V, GAMMA, True)

# Exact accounting identities remain valid.
for Z in (IS, SU, SW):
    assert abs(Z["payments"] - Z["op"].sum()) < 1e-10
    assert abs(Z["GW"] - (Z["nv"] - Z["tc"] - Z["redesign"].sum())) < 1e-10

# National member decomposition and rent-capture interpretation.
dCS = (SU["cs"] - IS["cs"]) / 3
dPI = SU["pi"][0] - IS["pi"][0]
dW = SU["W"][0] - IS["W"][0]
assert abs(dW - (dCS + dPI)) < 1e-10
assert dCS < 0 < dPI
assert dW > 0

# Historical Stage-7 witness values survive the repaired action set.
assert abs(dCS - (-0.0325785)) < 2e-6
assert abs(dPI - 0.0341498) < 2e-6
assert abs(dW - 0.0015713) < 2e-6
assert abs(IS["GW"] - (-0.0225000)) < 2e-6
assert abs(SU["GW"] - (-0.0586685)) < 2e-6
assert abs(SW["GW"] - (-0.0700000)) < 2e-6
assert IS["GW"] > SU["GW"] > SW["GW"]

# Private/social product-positioning wedge at the repaired SU policy.
XSP, GWSP = s7.social_x("SU", s4r.repaired_policy_vector("SU", sU), V, GAMMA)
Dprivate = SU["x"][1] - SU["x"][0]
Dsocial = XSP[1] - XSP[0]
D0 = s7.H[1] - s7.H[0]
assert Dprivate > Dsocial > D0
assert GWSP > SU["GW"]
assert abs(Dprivate - 0.497533) < 2e-6
assert abs(Dsocial - 0.431427) < 2e-6

# Repaired upper welfare threshold. Singleton depth is fixed at zero throughout.
def delta_member_repaired(gamma: float, vv: float = V, sbar: float = SBAR) -> float:
    # In the audited threshold neighborhood the coalition optimum remains the cap;
    # verify this at the computed root below.
    S = s7.decompose("SU", s4r.repaired_policy_vector("SU", sbar), vv, gamma, True)
    I = s7.decompose("IS", s4r.repaired_policy_vector("IS", sbar), vv, gamma, True)
    return float(S["W"][0] - I["W"][0])


gamma_W = brentq(lambda g: delta_member_repaired(g), 0.13, 0.14)
assert abs(gamma_W - 0.13298301564) < 1e-6
sI_g, _ = s4r.global_policy_optimum("IS", V, gamma_W, SBAR, True)
sU_g, _ = s4r.global_policy_optimum("SU", V, gamma_W, SBAR, True)
assert abs(sI_g - SBAR) < 1e-6
assert abs(sU_g - SBAR) < 1e-6

# Stage-4R interaction signs continue to be the source of the welfare reversal.
dBT = float(s4r.SU_T[0][0] - s4r.IS_T[0][0])
dBX = float(s4r.SU_X[0][0] - s4r.IS_X[0][0])
dFULL = float(s4r.SU_F[0][0] - s4r.IS_F[0][0])
assert dBT < 0 and dBX < 0 and dFULL > 0

if __name__ == "__main__":
    print("Stage 7R repaired policies IS/SU/SW:", sI, sU, sW)
    print("member dCS/3, dPi, dW:", dCS, dPI, dW)
    print("global welfare IS/SU/SW:", IS["GW"], SU["GW"], SW["GW"])
    print("private/social/inherited distances:", Dprivate, Dsocial, D0)
    print("repaired gamma_W:", gamma_W)
    print("interaction B-T/B-X/FULL:", dBT, dBX, dFULL)
    print("STAGE 7R WELFARE REFRESH: PASS")
