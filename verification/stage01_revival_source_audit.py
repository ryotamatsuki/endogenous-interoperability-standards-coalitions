"""Stage 1 revival source audit for PR #65 affine-demand architecture.

Workflow role: source/mathematical audit only. This script does not authorize a
new mechanism and is not an independent Stage-4A certificate.

It reconstructs from primitives:
1. the symmetric IS continuation and an exact symbolic welfare derivative;
2. the historical fixed-depth welfare reversal;
3. global location-BR diagnostics over the IS policy interval;
4. the endogenous-depth absorption diagnostic for the canonical witness;
5. the pre-specified (v,gamma) local box as a diagnostic, not a theorem.

The main analytic finding is conditional on the symmetric-anchor IS
continuation: because standards depth changes Tau but not the compatibility
network G, deeper IS raises the common cross-curvature c(s) while creating no
separate direct depth benefit. National welfare then strictly decreases in c,
so s_I*=0 on the allowed interval.
"""
from __future__ import annotations

import itertools
import math
import numpy as np
import sympy as sp
from numpy.linalg import inv, solve
from scipy.optimize import brentq, minimize_scalar

A = 2.0
B = 10.0
C0 = 0.30
LAM = 0.50
V = 0.08
GAMMA = 0.03
TBAR = 1.0
SBAR = 0.25
H = np.array([1 / 6, 1 / 2, 5 / 6], dtype=float)
PAIRS = ((0, 1), (0, 2), (1, 2))


def G(reg: str) -> np.ndarray:
    if reg == "IS":
        return np.ones((3, 3))
    if reg == "SU":
        return np.array([[1, 1, 0], [1, 1, 0], [0, 0, 1]], dtype=float)
    if reg == "SW":
        return np.eye(3)
    raise ValueError(reg)


def Tau(reg: str, s) -> np.ndarray:
    s = np.atleast_1d(np.asarray(s, dtype=float))
    T = np.zeros((3, 3))
    if reg == "IS":
        vals = {(0, 1): TBAR - s[0], (0, 2): TBAR - s[0], (1, 2): TBAR - s[0]}
    elif reg == "SU":
        vals = {
            (0, 1): TBAR - s[0],
            (0, 2): TBAR + (s[0] + s[1]) / 2,
            (1, 2): TBAR + (s[0] + s[1]) / 2,
        }
    elif reg == "SW":
        vals = {
            (0, 1): TBAR + (s[0] + s[1]) / 2,
            (0, 2): TBAR + (s[0] + s[2]) / 2,
            (1, 2): TBAR + (s[1] + s[2]) / 2,
        }
    else:
        raise ValueError(reg)
    for (i, j), z in vals.items():
        T[i, j] = T[j, i] = z
    return T


def phi(z: float) -> float:
    return 0.5 * (1.0 + math.cos(2.0 * math.pi * z))


def circ_delta(z: float, h: float) -> float:
    return ((z - h + 0.5) % 1.0) - 0.5


def K_matrix(reg: str, s, x, v: float = V) -> np.ndarray:
    x = np.mod(np.asarray(x, dtype=float), 1.0)
    T = Tau(reg, s)
    GG = G(reg)
    K = np.eye(3) * B
    for i, j in PAIRS:
        K[i, j] = K[j, i] = C0 + LAM * phi(x[i] - x[j]) / T[i, j] - v * GG[i, j]
    return K


def price_quantity(reg: str, s, x, v: float = V):
    K = K_matrix(reg, s, x, v=v)
    D = inv(K)
    rhs = D @ (np.ones(3) * A)
    p = solve(D + np.diag(np.diag(D)), rhs)
    q = D @ (np.ones(3) * A - p)
    assert np.min(p) > 0 and np.min(q) > 0
    return p, q, K


def profits(reg: str, s, x, v: float = V, gamma: float = GAMMA) -> np.ndarray:
    p, q, _ = price_quantity(reg, s, x, v=v)
    d = np.array([circ_delta(x[i], H[i]) for i in range(3)])
    return p * q - 0.5 * gamma * d**2


def welfare(reg: str, s, x, v: float = V, gamma: float = GAMMA):
    p, q, K = price_quantity(reg, s, x, v=v)
    cs = 0.5 * float(q @ K @ q)
    return cs / 3.0 + profits(reg, s, x, v=v, gamma=gamma)


def global_location_br(i: int, reg: str, s, x, v: float = V, gamma: float = GAMMA):
    x = np.asarray(x, dtype=float).copy()

    def payoff(z):
        xx = x.copy()
        xx[i] = z % 1.0
        return float(profits(reg, s, xx, v=v, gamma=gamma)[i])

    grid = np.linspace(0.0, 1.0, 361, endpoint=False)
    vals = np.array([payoff(z) for z in grid])
    step = 1.0 / len(grid)
    best = float(vals.max())
    for k in np.argsort(vals)[-8:]:
        center = grid[k]
        lo = max(0.0, center - 2 * step)
        hi = min(1.0, center + 2 * step)
        r = minimize_scalar(lambda z: -payoff(z), bounds=(lo, hi), method="bounded")
        best = max(best, -float(r.fun))
    return best - payoff(x[i])


# A. Exact symmetric-IS reconstruction.
aa, bb, cc = sp.symbols("a b c", positive=True)
p_sym = aa * (bb - cc) / (2 * bb)
q_sym = aa * (bb + cc) / (2 * bb * (bb + 2 * cc))
W_sym = aa**2 * (3 * bb**2 + 2 * bb * cc - cc**2) / (8 * bb**2 * (bb + 2 * cc))
dWdc = sp.factor(sp.diff(W_sym, cc))
target = -aa**2 * (2 * bb**2 + bb * cc + cc**2) / (4 * bb**2 * (bb + 2 * cc) ** 2)
assert sp.simplify(dWdc - target) == 0

ss = sp.symbols("s", real=True)
c_is = sp.Rational(22, 100) + sp.Rational(1, 8) / (1 - ss)
dcds = sp.factor(sp.diff(c_is, ss))
assert sp.simplify(dcds - sp.Rational(1, 8) / (1 - ss) ** 2) == 0

for sval in (0.0, SBAR):
    cnum = C0 + LAM * 0.25 / (TBAR - sval) - V
    p, q, _ = price_quantity("IS", [sval], H)
    assert np.max(np.abs(p - float(p_sym.subs({aa: A, bb: B, cc: cnum})))) < 1e-11
    assert np.max(np.abs(q - float(q_sym.subs({aa: A, bb: B, cc: cnum})))) < 1e-11

for sval in np.linspace(0.0, SBAR, 11):
    gaps = [global_location_br(i, "IS", [sval], H) for i in range(3)]
    assert max(gaps) < 2e-7

W_IS_0 = float(welfare("IS", [0.0], H)[0])
W_IS_BAR = float(welfare("IS", [SBAR], H)[0])
assert W_IS_0 > W_IS_BAR


# B. Historical fixed-depth reversal, freshly reconstructed.
def location_nash(reg: str, s, v: float = V, gamma: float = GAMMA):
    x = H.copy()
    for _ in range(80):
        old = x.copy()
        for i in range(3):
            def obj(z):
                xx = x.copy()
                xx[i] = z % 1.0
                return -float(profits(reg, s, xx, v=v, gamma=gamma)[i])
            grid = np.linspace(0.0, 1.0, 121, endpoint=False)
            vals = np.array([obj(z) for z in grid])
            step = 1.0 / len(grid)
            best = (grid[int(np.argmin(vals))], float(vals.min()))
            for k in np.argsort(vals)[:5]:
                center = grid[k]
                lo = max(0.0, center - 2 * step)
                hi = min(1.0, center + 2 * step)
                r = minimize_scalar(obj, bounds=(lo, hi), method="bounded")
                if r.fun < best[1]:
                    best = (float(r.x % 1.0), float(r.fun))
            x[i] = best[0]
        if np.max(np.abs(x - old)) < 1e-8:
            break
    gaps = [global_location_br(i, reg, s, x, v=v, gamma=gamma) for i in range(3)]
    assert max(gaps) < 3e-6
    return x


IS_BAR_X = location_nash("IS", [SBAR])
SU_BAR_X = location_nash("SU", [SBAR, 0.0])
fixed_diff = float(welfare("SU", [SBAR, 0.0], H)[0] - welfare("IS", [SBAR], H)[0])
full_diff = float(welfare("SU", [SBAR, 0.0], SU_BAR_X)[0] - welfare("IS", [SBAR], IS_BAR_X)[0])
assert fixed_diff < -1e-4
assert full_diff > 1e-4
assert abs(SU_BAR_X[0] - 0.14039) < 2e-4
assert abs(SU_BAR_X[1] - 0.52628) < 2e-4


# C. Endogenous-depth absorption diagnostic.
def dprofit_dx1_at_symmetric(d: float, s12: float, s3: float, v: float, gamma: float):
    x = np.array([H[0] - d, H[1] + d, H[2]])
    z = x[0]
    h = 1e-6
    xp = x.copy(); xp[0] = z + h
    xm = x.copy(); xm[0] = z - h
    return (profits("SU", [s12, s3], xp, v=v, gamma=gamma)[0]
            - profits("SU", [s12, s3], xm, v=v, gamma=gamma)[0]) / (2 * h)


def symmetric_su_location(s12: float, s3: float, v: float = V, gamma: float = GAMMA):
    grid = np.linspace(-0.03, 0.08, 111)
    vals = np.array([dprofit_dx1_at_symmetric(d, s12, s3, v, gamma) for d in grid])
    roots = []
    for k in range(len(grid) - 1):
        if vals[k] == 0 or vals[k] * vals[k + 1] < 0:
            roots.append(brentq(
                lambda d: dprofit_dx1_at_symmetric(d, s12, s3, v, gamma),
                grid[k], grid[k + 1]
            ))
    assert roots, "no symmetric SU location candidate found"
    d = min(roots, key=abs)
    return np.array([H[0] - d, H[1] + d, H[2]])


pgrid = np.linspace(0.0, SBAR, 101)
for s3 in (0.0, 0.0625, 0.125, 0.1875, SBAR):
    vals = np.array([welfare("SU", [s12, s3], H)[0] for s12 in pgrid])
    assert int(np.argmax(vals)) == 0
for s12 in (0.0, 0.0625, 0.125, 0.1875, SBAR):
    vals = np.array([welfare("SU", [s12, s3], H)[2] for s3 in pgrid])
    assert int(np.argmax(vals)) == len(pgrid) - 1

SU_POLICY_X = symmetric_su_location(SBAR, SBAR)
for i in range(3):
    assert global_location_br(i, "SU", [SBAR, SBAR], SU_POLICY_X) < 3e-6
W_SU_POLICY = welfare("SU", [SBAR, SBAR], SU_POLICY_X)
full_policy_diff = float(W_SU_POLICY[0] - W_IS_0)
assert full_policy_diff < 0

coarse = np.linspace(0.0, SBAR, 6)
member_values = []
for s12 in coarse:
    x = symmetric_su_location(s12, SBAR)
    member_values.append(float(welfare("SU", [s12, SBAR], x)[0]))
outsider_values = []
for s3 in coarse:
    x = symmetric_su_location(SBAR, s3)
    outsider_values.append(float(welfare("SU", [SBAR, s3], x)[2]))
assert np.all(np.diff(member_values) > 0)
assert np.all(np.diff(outsider_values) > 0)

box_diffs = []
for vv, gg in itertools.product((0.07, 0.08, 0.09), (0.025, 0.03, 0.035)):
    wis = float(welfare("IS", [0.0], H, v=vv, gamma=gg)[0])
    x = symmetric_su_location(SBAR, SBAR, v=vv, gamma=gg)
    wsu = welfare("SU", [SBAR, SBAR], x, v=vv, gamma=gg)
    diff = float(wsu[0] - wis)
    mvals = []
    ovals = []
    for z in coarse:
        xm = symmetric_su_location(z, SBAR, v=vv, gamma=gg)
        xo = symmetric_su_location(SBAR, z, v=vv, gamma=gg)
        mvals.append(float(welfare("SU", [z, SBAR], xm, v=vv, gamma=gg)[0]))
        ovals.append(float(welfare("SU", [SBAR, z], xo, v=vv, gamma=gg)[2]))
    assert np.all(np.diff(mvals) > 0)
    assert np.all(np.diff(ovals) > 0)
    assert diff < 0
    box_diffs.append(diff)


if __name__ == "__main__":
    print("IS symmetric dW/dc =", dWdc)
    print("IS W(s=0), W(s=sbar) =", W_IS_0, W_IS_BAR)
    print("fixed-depth SU-IS difference =", fixed_diff)
    print("endogenous-location fixed-depth SU-IS difference =", full_diff)
    print("SU fixed-depth location =", SU_BAR_X)
    print("FULL policy candidate SU location =", SU_POLICY_X)
    print("FULL policy candidate member SU-IS difference =", full_policy_diff)
    print("local-box FULL candidate differences =", min(box_diffs), max(box_diffs))
    print("STAGE 1 REVIVAL SOURCE AUDIT PASS")
