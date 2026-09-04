"""Stage 4R continuation-existence / policy-stage repair for C-ESD.

Repair motivated by Stage 11:
- s_C is reinterpreted strictly as *within-coalition harmonization depth*;
- non-singleton standards blocs choose s_C in [0, s_bar];
- singleton blocs have the degenerate action set {0}.

Hence:
- IS: the grand coalition chooses s_I;
- SU_12: only coalition {1,2} chooses s_12; outsider 3 has s_3=0;
- SW: all blocs are singletons, so all depths equal zero.

The pairwise friction map is unchanged. This removes the invalid outsider-depth
off-path subgames identified in Stage 11 without changing the equilibrium path at
the canonical witness. The script strengthens continuation verification by using
continuous whole-circle unilateral best responses and all-order stationary-candidate
audits, then re-solves the policy stage globally on the repaired action sets.
"""
from __future__ import annotations

import importlib.util
import itertools
from pathlib import Path

import numpy as np
from numpy.linalg import LinAlgError, solve
from scipy.optimize import differential_evolution, minimize_scalar

ROOT = Path(__file__).resolve().parents[1]
P = ROOT / "verification" / "stage04_cesd_minimal.py"
spec = importlib.util.spec_from_file_location("s4", P)
s4 = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(s4)

H = s4.H.copy()
V = 0.04
GAMMA = 0.11
SBAR = 0.25
T_BAR = 1.0
TOL = 1e-8


def repaired_policy_vector(reg: str, depth: float = 0.0):
    """Map the repaired scalar/non-choice policy action to legacy Tau arguments."""
    if reg == "IS":
        return [float(depth)]
    if reg == "SU":
        # Outsider singleton has no within-coalition harmonization margin.
        return [float(depth), 0.0]
    if reg == "SW":
        return [0.0, 0.0, 0.0]
    raise ValueError(reg)


def best_deviation_continuous(pos, reg, s, vv, gamma, i):
    """Continuous one-firm whole-circle best response, split at order/kink points."""
    cur = s4.profits_general(pos, reg, s, vv, gamma)
    if cur is None:
        return None
    cuts = {0.0, 1.0, float((H[i] + 0.5) % 1)}
    for j in range(3):
        if j != i:
            cuts.add(float(np.mod(pos[j], 1)))
    cuts = sorted(cuts)

    def profit_at(z):
        pp = np.array(pos, float)
        pp[i] = z % 1
        pr = s4.profits_general(pp, reg, s, vv, gamma)
        return None if pr is None else float(pr[i])

    best_val = -1e100
    best_z = None
    for a, b in zip(cuts[:-1], cuts[1:]):
        lo, hi = a + 1e-9, b - 1e-9
        if hi <= lo:
            continue

        def obj(z):
            val = profit_at(z)
            return 1e12 if val is None else -val

        r = minimize_scalar(
            obj, bounds=(lo, hi), method="bounded",
            options={"xatol": 1e-11, "maxiter": 300},
        )
        for z in (lo, hi, r.x):
            val = profit_at(z)
            if val is not None and val > best_val:
                best_val, best_z = val, z
    return best_val - float(cur[i]), best_z


def affine_b_for_order(order):
    ref = np.empty(3)
    for k, i in enumerate(order):
        ref[i] = (0.12, 0.43, 0.77)[k]
    b_ref, _ = s4.base_general(ref)
    eps = 1e-6
    B = np.zeros((3, 3))
    for j in range(3):
        rp, rm = ref.copy(), ref.copy()
        rp[j] += eps
        rm[j] -= eps
        bp, _ = s4.base_general(rp)
        bm, _ = s4.base_general(rm)
        B[:, j] = (bp - bm) / (2 * eps)
    return b_ref - B @ ref, B


def stationary_candidates_all_orders(reg, s, vv, gamma):
    """Enumerate regular interior stationary candidates over all order/anchor branches."""
    mm = s4.matrices(reg, s, vv)
    if mm is None:
        return []
    _, _, M, K = mm
    out = []
    for order in itertools.permutations(range(3)):
        b0, B = affine_b_for_order(order)
        c, R = K @ b0, K @ B
        for shifts in itertools.product([-1, 0, 1], repeat=3):
            anchor = H + np.array(shifts)
            Aeq = np.zeros((3, 3))
            rhs = np.zeros(3)
            ok = True
            for i in range(3):
                z = 2 * M[i, i] * R[i, i]
                if 2 * M[i, i] * R[i, i] ** 2 - gamma >= -1e-10:
                    ok = False
                    break
                Aeq[i, :] = z * R[i, :]
                Aeq[i, i] -= gamma
                rhs[i] = -(z * c[i] + gamma * anchor[i])
            if not ok:
                continue
            try:
                x = solve(Aeq, rhs)
            except LinAlgError:
                continue
            if np.any(x <= 1e-8) or np.any(x >= 1 - 1e-8):
                continue
            if tuple(np.argsort(x)) != tuple(order):
                continue
            delta = x - anchor
            if np.any(delta < -0.5 - 1e-7) or np.any(delta > 0.5 + 1e-7):
                continue
            if s4.profits_general(x, reg, s, vv, gamma) is None:
                continue
            gaps = np.array([
                best_deviation_continuous(x, reg, s, vv, gamma, i)[0]
                for i in range(3)
            ])
            out.append((x, gaps, order, shifts))
    return out


def selected_continuation(reg, depth, vv=V, gamma=GAMMA, full=True):
    """Return a verified downstream continuation on the repaired action set."""
    s = repaired_policy_vector(reg, depth)
    if not full:
        out = s4.welfare(reg, s, vv, gamma, False)
        if out is None:
            return None
        return out
    x = s4.loc_nash(reg, s, vv, gamma, True)
    if x is None:
        return None
    out = s4.welfare(reg, s, vv, gamma, True)
    if out is None:
        return None
    gaps = [best_deviation_continuous(x, reg, s, vv, gamma, i)[0]
            for i in range(3)]
    if max(gaps) > TOL:
        return None
    return out


def global_policy_optimum(reg, vv=V, gamma=GAMMA, sbar=SBAR, full=True):
    """Global scalar policy optimization on the repaired action set."""
    if reg == "SW":
        return 0.0, selected_continuation("SW", 0.0, vv, gamma, full)

    def objective(z):
        out = selected_continuation(reg, float(z), vv, gamma, full)
        if out is None:
            return -1e100
        W = out[0]
        return float(W.sum()) if reg == "IS" else float(W[0] + W[1])

    # Differential evolution provides an independent global search; endpoints are included explicitly.
    de = differential_evolution(
        lambda z: -objective(float(z[0])),
        bounds=[(0.0, sbar)], seed=11, popsize=12, maxiter=80,
        tol=1e-10, polish=True,
    )
    candidates = [(0.0, objective(0.0)), (sbar, objective(sbar)),
                  (float(de.x[0]), objective(float(de.x[0])))]
    depth = max(candidates, key=lambda z: z[1])[0]
    return depth, selected_continuation(reg, depth, vv, gamma, full)


def max_policy_continuation_gain(reg, vv=V, gamma=GAMMA, sbar=SBAR):
    """Max unilateral location gain jointly over every feasible policy depth and circle point."""
    assert reg in ("IS", "SU")
    maxima = []
    for i in range(3):
        def neg_gain(y):
            depth, z = float(y[0]), float(y[1])
            s = repaired_policy_vector(reg, depth)
            x = s4.loc_nash(reg, s, vv, gamma, True)
            if x is None:
                return 1e6
            cur = s4.profits_general(x, reg, s, vv, gamma)
            pp = np.array(x, float)
            pp[i] = z % 1
            dev = s4.profits_general(pp, reg, s, vv, gamma)
            if cur is None or dev is None:
                return 1e6
            return -(float(dev[i]) - float(cur[i]))

        r = differential_evolution(
            neg_gain, bounds=[(0.0, sbar), (0.0, 1.0)],
            seed=100 + i, popsize=12, maxiter=100, tol=1e-9, polish=True,
        )
        maxima.append(-float(r.fun))
    return np.array(maxima)


# ---------- Repair semantics ----------
assert repaired_policy_vector("SU", 0.20) == [0.20, 0.0]
assert repaired_policy_vector("SW", 0.20) == [0.0, 0.0, 0.0]

# ---------- Every feasible policy depth has a global whole-circle continuation ----------
# Direct global search over policy depth x unilateral-deviation location.
SU_global_gains = max_policy_continuation_gain("SU")
IS_global_gains = max_policy_continuation_gain("IS")
assert np.max(SU_global_gains) < 1e-7
assert np.max(IS_global_gains) < 1e-7

# All-order uniqueness audit on a dense depth grid.
for reg in ("IS", "SU"):
    for depth in np.linspace(0.0, SBAR, 51):
        s = repaired_policy_vector(reg, depth)
        candidates = stationary_candidates_all_orders(reg, s, V, GAMMA)
        ne = [c for c in candidates if np.max(c[1]) < TOL]
        assert len(ne) == 1, (reg, depth, len(ne))

# SW has no continuous policy choice and its unique regular location equilibrium is valid.
sw_candidates = stationary_candidates_all_orders("SW", [0.0, 0.0, 0.0], V, GAMMA)
sw_ne = [c for c in sw_candidates if np.max(c[1]) < TOL]
assert len(sw_ne) == 1

# ---------- Repaired policy stage ----------
sI_F, IS_F = global_policy_optimum("IS", full=True)
sU_F, SU_F = global_policy_optimum("SU", full=True)
sW_F, SW_F = global_policy_optimum("SW", full=True)
sI_T, IS_T = global_policy_optimum("IS", full=False)
sU_T, SU_T = global_policy_optimum("SU", full=False)
sW_T, SW_T = global_policy_optimum("SW", full=False)

assert abs(sI_F - SBAR) < 1e-7
assert abs(sU_F - SBAR) < 1e-7
assert abs(sW_F) < 1e-12
assert abs(sI_T - SBAR) < 1e-7
assert abs(sU_T - SBAR) < 1e-7
assert abs(sW_T) < 1e-12

# B-X keeps all non-singleton depths fixed at zero.
IS_X = selected_continuation("IS", 0.0, full=True)
SU_X = selected_continuation("SU", 0.0, full=True)
SW_X = selected_continuation("SW", 0.0, full=True)
assert all(z is not None for z in (IS_F, SU_F, SW_F, IS_T, SU_T, SW_T, IS_X, SU_X, SW_X))

# ---------- Headline interaction and coalition stability ----------
dBT = float(SU_T[0][0] - IS_T[0][0])
dBX = float(SU_X[0][0] - IS_X[0][0])
dFULL = float(SU_F[0][0] - IS_F[0][0])
assert dBT < 0
assert dBX < 0
assert dFULL > 0

# FULL: SU member > IS > SU outsider and SU member > SW.
assert SU_F[0][0] > IS_F[0][0] > SU_F[0][2]
assert SU_F[0][0] > SW_F[0][0]
# Benchmarks: IS beats SU for prospective members.
assert IS_T[0][0] > SU_T[0][0]
assert IS_X[0][0] > SU_X[0][0]

# Repair leaves the canonical equilibrium path and headline values unchanged to numerical precision.
assert np.allclose(SU_F[1], s4.SU_F[1], atol=1e-8)
assert abs(dBT - (-0.0101670733)) < 2e-6
assert abs(dBX - (-0.000434)) < 2e-6
assert abs(dFULL - 0.0015713) < 2e-6

if __name__ == "__main__":
    print("Stage 4R repaired action sets: singleton depth = 0 by definition")
    print("continuation max gains SU:", SU_global_gains)
    print("continuation max gains IS:", IS_global_gains)
    print("policy optima FULL IS/SU/SW:", sI_F, sU_F, sW_F)
    print("policy optima B-T IS/SU/SW:", sI_T, sU_T, sW_T)
    print("Delta member B-T/B-X/FULL:", dBT, dBX, dFULL)
    print("FULL SU locations:", SU_F[1])
    print("STAGE 4R REPAIR: PASS")
