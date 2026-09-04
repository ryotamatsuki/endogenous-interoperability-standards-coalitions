"""Stage 11 hostile mathematical audit for C-ESD.

This script does not change the frozen theory. It strengthens the whole-circle
best-response check at the canonical witness and audits off-path continuation
subgames relevant for the standards-depth Nash stage.

Key diagnostic: the canonical SU witness is a genuine whole-circle location
Nash equilibrium, but for sufficiently large outsider-depth deviations the
fixed-order continuation candidate used by the Stage-4 policy routine ceases
to be a global location Nash equilibrium. This creates an unresolved off-path
continuation/SPNE issue.

The script also records a bounded repair diagnostic: at the same v and gamma
with a smaller policy cap sbar=0.20, the headline B-T/B-X/FULL sign pattern
survives and a dense audit of the SU policy square finds no whole-circle
continuation failure on the selected interior branch. This is evidence that
the mechanism may survive a Stage-4 repair; it is not itself a new theorem.
"""
from __future__ import annotations

import importlib.util
import itertools
from pathlib import Path

import numpy as np
from numpy.linalg import LinAlgError, solve
from scipy.optimize import minimize_scalar

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "stage04", ROOT / "verification" / "stage04_cesd_minimal.py"
)
s4 = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(s4)

V = 0.04
GAMMA = 0.11
SBAR = 0.25
REPAIR_SBAR = 0.20
H = s4.H.copy()


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
            options={"xatol": 1e-11, "maxiter": 300}
        )
        for z in (lo, hi, r.x):
            val = profit_at(z)
            if val is not None and val > best_val:
                best_val, best_z = val, z
    return best_val - float(cur[i]), best_z


def affine_b_for_order(order):
    """Recover the piecewise-affine Voronoi map within one order."""
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
    b0 = b_ref - B @ ref
    return b0, B


def stationary_candidates_all_orders(reg, s, vv, gamma):
    """Enumerate interior stationary candidates over all cyclic orders/anchor branches."""
    mm = s4.matrices(reg, s, vv)
    if mm is None:
        return []
    _, _, M, K = mm
    out = []
    for order in itertools.permutations(range(3)):
        b0, B = affine_b_for_order(order)
        c, R = K @ b0, K @ B
        for shifts in itertools.product([-1, 0, 1], repeat=3):
            effective_anchor = H + np.array(shifts)
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
                rhs[i] = -(z * c[i] + gamma * effective_anchor[i])
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
            delta = x - effective_anchor
            if np.any(delta < -0.5 - 1e-7) or np.any(delta > 0.5 + 1e-7):
                continue
            if s4.profits_general(x, reg, s, vv, gamma) is None:
                continue
            gaps = [best_deviation_continuous(x, reg, s, vv, gamma, i)[0]
                    for i in range(3)]
            out.append((x, np.array(gaps), order, shifts))
    return out


# 1. Stronger on-path witness audit: continuous, not grid-only.
canonical_x = s4.SU_F[1]
canonical_gaps = np.array([
    best_deviation_continuous(canonical_x, "SU", s4.sF, V, GAMMA, i)[0]
    for i in range(3)
])
assert np.max(canonical_gaps) < 1e-8

# 2. Selected policy directions that remain regular on the audited branch.
is_vals = []
for z in np.linspace(0, SBAR, 26):
    w = s4.welfare("IS", [z], V, GAMMA, True)
    assert w is not None
    gaps = [best_deviation_continuous(w[1], "IS", [z], V, GAMMA, i)[0]
            for i in range(3)]
    assert max(gaps) < 1e-8
    is_vals.append(float(w[0][0] + w[0][1] + w[0][2]))
assert int(np.argmax(is_vals)) == len(is_vals) - 1

sw_vals = []
for z in np.linspace(0, SBAR, 26):
    s = [z, 0.0, 0.0]
    w = s4.welfare("SW", s, V, GAMMA, True)
    assert w is not None
    gaps = [best_deviation_continuous(w[1], "SW", s, V, GAMMA, i)[0]
            for i in range(3)]
    assert max(gaps) < 1e-8
    sw_vals.append(float(w[0][0]))
assert int(np.argmax(sw_vals)) == 0

su_member_vals = []
for z in np.linspace(0, SBAR, 26):
    s = [z, 0.0]
    w = s4.welfare("SU", s, V, GAMMA, True)
    assert w is not None
    gaps = [best_deviation_continuous(w[1], "SU", s, V, GAMMA, i)[0]
            for i in range(3)]
    assert max(gaps) < 1e-8
    su_member_vals.append(float(w[0][0] + w[0][1]))
assert int(np.argmax(su_member_vals)) == len(su_member_vals) - 1

# 3. Current-gap diagnostic: outsider-depth deviations can leave the regular
# pure location-equilibrium domain. At s3=.20, the Stage-4 fixed-order
# candidate is not a global best response and no alternative *interior*
# stationary candidate over all cyclic orders/anchor branches passes the
# continuous whole-circle best-response test.
offpath_s = [SBAR, 0.20]
offpath_w = s4.welfare("SU", offpath_s, V, GAMMA, True)
assert offpath_w is not None
offpath_local_gaps = np.array([
    best_deviation_continuous(offpath_w[1], "SU", offpath_s, V, GAMMA, i)[0]
    for i in range(3)
])
assert np.max(offpath_local_gaps) > 1e-4

candidates = stationary_candidates_all_orders("SU", offpath_s, V, GAMMA)
regular_pure_ne = [c for c in candidates if np.max(c[1]) < 1e-8]
assert len(regular_pure_ne) == 0

lo, hi = 0.13, 0.16
for _ in range(45):
    mid = 0.5 * (lo + hi)
    w = s4.welfare("SU", [SBAR, mid], V, GAMMA, True)
    assert w is not None
    gap = best_deviation_continuous(w[1], "SU", [SBAR, mid], V, GAMMA, 2)[0]
    if gap > 1e-9:
        hi = mid
    else:
        lo = mid
jump_onset = hi

# 4. Bounded repair diagnostic, not a theory change in this audit.
# At sbar=.20 the headline signs survive.
s_repair_f, su_repair_f = s4.su_policy(V, GAMMA, REPAIR_SBAR, True)
s_repair_t, su_repair_t = s4.su_policy(V, GAMMA, REPAIR_SBAR, False)
is_repair_f = s4.welfare("IS", [REPAIR_SBAR], V, GAMMA, True)
is_repair_t = s4.welfare("IS", [REPAIR_SBAR], V, GAMMA, False)
is_repair_x = s4.welfare("IS", [0], V, GAMMA, True)
su_repair_x = s4.welfare("SU", [0, 0], V, GAMMA, True)
repair_delta_t = float(su_repair_t[0][0] - is_repair_t[0][0])
repair_delta_x = float(su_repair_x[0][0] - is_repair_x[0][0])
repair_delta_f = float(su_repair_f[0][0] - is_repair_f[0][0])
assert repair_delta_t < 0
assert repair_delta_x < 0
assert repair_delta_f > 0
assert np.allclose(s_repair_f, [REPAIR_SBAR, 0], atol=1e-6)

# Dense SU policy-square diagnostic at the smaller cap.
repair_invalid = []
for s12 in np.linspace(0, REPAIR_SBAR, 21):
    for s3 in np.linspace(0, REPAIR_SBAR, 21):
        ss = [float(s12), float(s3)]
        w = s4.welfare("SU", ss, V, GAMMA, True)
        if w is None:
            repair_invalid.append((s12, s3, "ordered"))
            continue
        gaps = [best_deviation_continuous(w[1], "SU", ss, V, GAMMA, i)[0]
                for i in range(3)]
        if max(gaps) > 1e-8:
            repair_invalid.append((s12, s3, max(gaps)))
assert len(repair_invalid) == 0

if __name__ == "__main__":
    print("canonical continuous whole-circle gaps:", canonical_gaps)
    print("IS policy-grid argmax depth:", np.linspace(0, SBAR, 26)[np.argmax(is_vals)])
    print("SW unilateral policy-grid argmax depth:", np.linspace(0, SBAR, 26)[np.argmax(sw_vals)])
    print("SU member policy-grid argmax depth:", np.linspace(0, SBAR, 26)[np.argmax(su_member_vals)])
    print("off-path SU policy:", offpath_s)
    print("off-path fixed-order location gaps:", offpath_local_gaps)
    print("all-order interior stationary candidates:", len(candidates))
    print("all-order regular pure location NE:", len(regular_pure_ne))
    print("approx outsider-depth jump onset:", jump_onset)
    print("repair sbar:", REPAIR_SBAR)
    print("repair deltas B-T/B-X/FULL:", repair_delta_t, repair_delta_x, repair_delta_f)
    print("repair SU policy-square invalid grid points:", len(repair_invalid))
    print("STAGE-11 DIAGNOSTIC: current off-path SPNE gap; bounded Stage-4 repair appears viable")