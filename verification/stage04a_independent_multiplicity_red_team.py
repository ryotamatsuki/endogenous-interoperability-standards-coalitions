"""Stage 4A independent mathematical red-team for the revival C1 model.

This verifier is intentionally separate from the Stage-4 production solvers.
It reconstructs the C1 terminal location game from primitives, solves the
location first-order system from many initial conditions, and then subjects
every candidate root to a whole-circle unilateral best-response audit.

Purpose: test the alternative-equilibrium question, not merely candidate
deviations around the Stage-4 preferred branch.

Permanent regression discovered by Stage 4A:
At SU full depths, the terminal location subgame has at least two distinct
pure-strategy Nash equilibria at the headline parameter points.  Their national
welfare rankings relative to IS differ, so the Stage-4 stable-set and blocking-
threshold claims are not equilibrium-selection invariant.
"""
from __future__ import annotations

import math
import numpy as np
from numpy.linalg import inv, solve
from scipy.optimize import minimize_scalar, root

A = 2.0
B = 10.0
C0 = 0.30
LAM = 0.50
TBAR = 1.0
SBAR = 0.25
H = np.array([1 / 6, 1 / 2, 5 / 6], dtype=float)
PAIRS = ((0, 1), (0, 2), (1, 2))


def tau(reg: str, s) -> np.ndarray:
    s = np.atleast_1d(np.asarray(s, dtype=float))
    T = np.zeros((3, 3))
    if reg == "IS":
        vals = {(0, 1): 1 - s[0], (0, 2): 1 - s[0], (1, 2): 1 - s[0]}
    elif reg == "SU":
        vals = {
            (0, 1): 1 - s[0],
            (0, 2): 1 + (s[0] + s[1]) / 2,
            (1, 2): 1 + (s[0] + s[1]) / 2,
        }
    elif reg == "SW":
        vals = {
            (0, 1): 1 + (s[0] + s[1]) / 2,
            (0, 2): 1 + (s[0] + s[2]) / 2,
            (1, 2): 1 + (s[1] + s[2]) / 2,
        }
    else:
        raise ValueError(reg)
    for (i, j), z in vals.items():
        T[i, j] = T[j, i] = z
    return T


def realized_interoperability(reg: str, s) -> np.ndarray:
    s = np.atleast_1d(np.asarray(s, dtype=float))
    M = np.zeros((3, 3))
    if reg == "IS":
        for i, j in PAIRS:
            M[i, j] = M[j, i] = s[0] / SBAR
    elif reg == "SU":
        M[0, 1] = M[1, 0] = s[0] / SBAR
    elif reg != "SW":
        raise ValueError(reg)
    return M


def phi(z: float) -> float:
    return 0.5 * (1.0 + math.cos(2.0 * math.pi * z))


def circular_displacement(z: float, h: float) -> float:
    return ((z - h + 0.5) % 1.0) - 0.5


def k_matrix(reg: str, s, x, v: float) -> np.ndarray:
    x = np.asarray(x, dtype=float) % 1.0
    T = tau(reg, s)
    M = realized_interoperability(reg, s)
    K = np.eye(3) * B
    for i, j in PAIRS:
        K[i, j] = K[j, i] = C0 + LAM * phi(x[i] - x[j]) / T[i, j] - v * M[i, j]
    return K


def price_quantity(reg: str, s, x, v: float):
    K = k_matrix(reg, s, x, v)
    D = inv(K)
    p = solve(D + np.diag(np.diag(D)), D @ (np.ones(3) * A))
    q = D @ (np.ones(3) * A - p)
    assert np.min(p) > 0 and np.min(q) > 0
    return p, q, K


def profit(reg: str, s, x, v: float, gamma: float) -> np.ndarray:
    p, q, _ = price_quantity(reg, s, x, v)
    d = np.array([circular_displacement(x[i], H[i]) for i in range(3)])
    return p * q - 0.5 * gamma * d * d


def welfare(reg: str, s, x, v: float, gamma: float) -> np.ndarray:
    p, q, K = price_quantity(reg, s, x, v)
    cs = 0.5 * float(q @ K @ q)
    return cs / 3.0 + profit(reg, s, x, v, gamma)


def location_foc(reg: str, s, x, v: float, gamma: float, eps: float = 1e-6) -> np.ndarray:
    x = np.asarray(x, dtype=float)
    out = np.zeros(3)
    for i in range(3):
        xp = x.copy(); xp[i] += eps
        xm = x.copy(); xm[i] -= eps
        out[i] = (profit(reg, s, xp, v, gamma)[i] - profit(reg, s, xm, v, gamma)[i]) / (2 * eps)
    return out


def whole_circle_gap(i: int, reg: str, s, x, v: float, gamma: float, n: int = 1001) -> float:
    x = np.asarray(x, dtype=float).copy()
    current = float(profit(reg, s, x, v, gamma)[i])

    def payoff(z: float) -> float:
        xx = x.copy(); xx[i] = z % 1.0
        return float(profit(reg, s, xx, v, gamma)[i])

    grid = np.linspace(0.0, 1.0, n, endpoint=False)
    vals = np.array([payoff(z) for z in grid])
    step = 1.0 / n
    best = float(vals.max())
    for k in np.argsort(vals)[-10:]:
        c = grid[k]
        r = minimize_scalar(lambda z: -payoff(z), bounds=(c - 2 * step, c + 2 * step), method="bounded")
        best = max(best, -float(r.fun))
    return best - current


def distinct_nash(reg: str, s, v: float, gamma: float, nstarts: int = 40):
    rng = np.random.default_rng(20260910)
    starts = [H.copy()] + [rng.random(3) for _ in range(nstarts)]
    equilibria = []
    for x0 in starts:
        ans = root(lambda x: location_foc(reg, s, x, v, gamma), x0, method="hybr")
        if not ans.success:
            continue
        x = ans.x % 1.0
        gaps = np.array([whole_circle_gap(i, reg, s, x, v, gamma, n=361) for i in range(3)])
        if gaps.max() > 2e-6:
            continue
        if not any(np.max(np.abs(((x - y + 0.5) % 1.0) - 0.5)) < 2e-4 for y in equilibria):
            equilibria.append(x)
    return equilibria


def audit_point(v: float, gamma: float):
    eqs = distinct_nash("SU", [SBAR, SBAR], v, gamma)
    assert len(eqs) >= 2, (v, gamma, eqs)
    eqs = sorted(eqs, key=lambda x: x[0])

    # Re-audit two distinct equilibria at high resolution.
    for x in eqs[:2]:
        gaps = [whole_circle_gap(i, "SU", [SBAR, SBAR], x, v, gamma, n=1001) for i in range(3)]
        assert max(gaps) < 2e-7, (v, gamma, x, gaps)

    wis = float(welfare("IS", [SBAR], H, v, gamma)[0])
    member_diffs = [float(welfare("SU", [SBAR, SBAR], x, v, gamma)[0] - wis) for x in eqs]
    assert max(member_diffs) > 0
    assert min(member_diffs) < 0
    return eqs, wis, member_diffs


if __name__ == "__main__":
    for v, gamma in ((0.08, 0.03), (0.12, 0.03)):
        eqs, wis, diffs = audit_point(v, gamma)
        print(f"v={v:.3f}, gamma={gamma:.3f}, IS W={wis:.9f}")
        for k, (x, d) in enumerate(zip(eqs, diffs), 1):
            print(f"  SU equilibrium {k}: x={x}, member SU-IS={d:+.9f}")
    print("STAGE 4A COUNTEREXAMPLE CONFIRMED: SU LOCATION MULTIPLICITY CHANGES WELFARE RANKING")
