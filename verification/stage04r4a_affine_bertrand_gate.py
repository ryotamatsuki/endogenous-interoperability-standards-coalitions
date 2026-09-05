"""Stage 4R4A — affine-demand Bertrand continuation and novelty witness.

This is the first executable gate for the post-spatial re-foundation.
It deliberately preserves the old policy maps Tau(reg,s) and G(reg), while
replacing discrete Salop allocation with a representative-consumer quadratic
utility.  For fixed history (reg,s,x):

    U(q)-p'q = a 1'q - 1/2 q' K q - p'q,  q >= 0,

where K has diagonal b and pairwise off-diagonal entries

    c_ij = c0 + lam * phi(x_i-x_j)/Tau_ij - v G_ij,
    phi(z) = (1+cos(2*pi*z))/2.

The direct interior demand matrix is D=K^{-1}; the chosen primitive box makes
D a symmetric Z-matrix, so products are gross substitutes in prices.
Nonnegative demand is evaluated from the KKT system, never by allowing
negative quantities.

The script checks:
1. analytic global bounds implying K >> 0 and substitute signs;
2. positive closed-form Bertrand candidate over adversarial histories;
3. direct KKT/global-price-deviation checks against that candidate;
4. global location best responses for the canonical IS and SU histories;
5. a fixed-location vs endogenous-repositioning member-welfare reversal;
6. local robustness of that reversal over a 3x3 (v,gamma) box.

The Bertrand existence/uniqueness theorem used in the paper-facing Stage 4R4A
record is Farahat and Perakis (2010).  This script is an independent numerical
regression and does not substitute failed optimization for equilibrium evidence.
"""
from __future__ import annotations

import itertools
import math
import numpy as np
from numpy.linalg import eigvalsh, inv, solve
from scipy.optimize import minimize_scalar

# ---------------------------------------------------------------------------
# Frozen Stage 4R4A primitives.  These are architecture-test parameters, not
# a claim that the old witness survives unchanged.
# ---------------------------------------------------------------------------
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
    if reg == "SW":
        return np.eye(3)
    if reg == "SU":
        return np.array([[1, 1, 0], [1, 1, 0], [0, 0, 1]], dtype=float)
    raise ValueError(reg)


def Tau(reg: str, s, tbar: float = TBAR) -> np.ndarray:
    """Old standards-depth map, retained exactly at the architecture gate."""
    s = np.atleast_1d(np.asarray(s, dtype=float))
    T = np.zeros((3, 3))
    if reg == "IS":
        vals = {(0, 1): tbar - s[0], (0, 2): tbar - s[0], (1, 2): tbar - s[0]}
    elif reg == "SU":
        vals = {
            (0, 1): tbar - s[0],
            (0, 2): tbar + (s[0] + s[1]) / 2,
            (1, 2): tbar + (s[0] + s[1]) / 2,
        }
    elif reg == "SW":
        vals = {
            (0, 1): tbar + (s[0] + s[1]) / 2,
            (0, 2): tbar + (s[0] + s[2]) / 2,
            (1, 2): tbar + (s[1] + s[2]) / 2,
        }
    else:
        raise ValueError(reg)
    for (i, j), z in vals.items():
        T[i, j] = T[j, i] = z
    return T


def phi(z: float) -> float:
    """Smooth circular proximity kernel in [0,1]."""
    return 0.5 * (1.0 + math.cos(2.0 * math.pi * z))


def circ_delta(x: float, h: float) -> float:
    return ((x - h + 0.5) % 1.0) - 0.5


def K_matrix(reg: str, s, x, v: float = V) -> np.ndarray:
    x = np.mod(np.asarray(x, dtype=float), 1.0)
    T = Tau(reg, s)
    GG = G(reg)
    K = np.eye(3) * B
    for i, j in PAIRS:
        cij = C0 + LAM * phi(x[i] - x[j]) / T[i, j] - v * GG[i, j]
        K[i, j] = K[j, i] = cij
    return K


# ---------------------------------------------------------------------------
# Gate A: analytic global primitive bounds.
# Across the admissible policy box, Tau_ij in [3/4,5/4], phi in [0,1], and
# G_ij in {0,1}.  Thus every off-diagonal c_ij lies in [C_MIN,C_MAX].
# The inequalities below imply:
# - strict diagonal dominance and SPD of K;
# - every off-diagonal cofactor of K^{-1} is negative;
# - every row sum of K^{-1} is positive.
# ---------------------------------------------------------------------------
TAU_MIN = TBAR - SBAR
TAU_MAX = TBAR + SBAR
C_MIN = C0 - V
C_MAX = C0 + LAM / TAU_MIN
assert TAU_MIN == 0.75 and TAU_MAX == 1.25
assert C_MIN > 0
assert B > 2 * C_MAX
assert B * C_MIN > C_MAX**2
assert B - 2 * C_MAX + C_MIN > 0


def interior_price(reg: str, s, x, v: float = V):
    K = K_matrix(reg, s, x, v=v)
    D = inv(K)
    rhs = D @ (np.ones(3) * A)
    p = solve(D + np.diag(np.diag(D)), rhs)
    q = D @ (np.ones(3) * A - p)
    return p, q, K, D


def demand_kkt(reg: str, s, x, p, v: float = V) -> np.ndarray:
    """Exact finite active-set solution of the consumer quadratic program."""
    p = np.asarray(p, dtype=float)
    K = K_matrix(reg, s, x, v=v)
    r = np.ones(3) * A - p
    candidates = []
    for mask in range(1 << 3):
        S = [i for i in range(3) if mask & (1 << i)]
        q = np.zeros(3)
        if S:
            KSS = K[np.ix_(S, S)]
            qS = solve(KSS, r[S])
            q[S] = qS
            if np.any(qS < -1e-10):
                continue
        grad = K @ q - r
        I = [i for i in range(3) if i not in S]
        if I and np.any(grad[I] < -1e-10):
            continue
        # Complementarity on active coordinates.
        if S and np.max(np.abs(grad[S])) > 1e-8:
            continue
        obj = 0.5 * q @ K @ q - r @ q
        candidates.append((obj, q))
    assert candidates, "consumer KKT problem unexpectedly unresolved"
    candidates.sort(key=lambda z: z[0])
    return candidates[0][1]


def operating_profit(i: int, reg: str, s, x, p, v: float = V) -> float:
    q = demand_kkt(reg, s, x, p, v=v)
    return float(p[i] * q[i])


def global_price_gap(i: int, reg: str, s, x, pstar, v: float = V) -> float:
    """Direct global one-price deviation audit with KKT demand."""
    pstar = np.asarray(pstar, dtype=float)
    cur = operating_profit(i, reg, s, x, pstar, v=v)

    def neg(z):
        pp = pstar.copy()
        pp[i] = z
        return -operating_profit(i, reg, s, x, pp, v=v)

    # Above A+2 there is no reason to search: own demand is already zero in
    # all tested histories and margins are nonnegative.  Include endpoints and
    # a dense scan before local refinement so kinks cannot be silently skipped.
    grid = np.linspace(0.0, A + 2.0, 401)
    vals = np.array([neg(z) for z in grid])
    best_val = -np.inf
    for k in np.argsort(vals)[:8]:
        lo = max(0.0, grid[k] - 0.02)
        hi = min(A + 2.0, grid[k] + 0.02)
        r = minimize_scalar(neg, bounds=(lo, hi), method="bounded")
        best_val = max(best_val, -float(r.fun))
    best_val = max(best_val, -float(vals.min()))
    return best_val - cur


# Adversarial histories for Gates A-B: endpoints, coincident products, former
# hostile location history, and deterministic pseudo-random histories.
rng = np.random.default_rng(20260905)
histories = []
for reg, s in (("IS", [0.0]), ("IS", [SBAR]), ("SU", [0.0, 0.0]), ("SU", [SBAR, 0.0]), ("SW", [0, 0, 0]), ("SW", [SBAR, SBAR, SBAR])):
    histories.extend(
        [
            (reg, s, H.copy()),
            (reg, s, np.array([0.4, 0.5, 5 / 6])),
            (reg, s, np.array([0.2, 0.2, 0.8])),
            (reg, s, np.array([0.0, 0.5, 0.5])),
        ]
    )
for _ in range(40):
    reg = ("IS", "SU", "SW")[int(rng.integers(0, 3))]
    if reg == "IS":
        s = [float(rng.uniform(0, SBAR))]
    elif reg == "SU":
        s = [float(rng.uniform(0, SBAR)), float(rng.uniform(0, SBAR))]
    else:
        s = list(rng.uniform(0, SBAR, 3))
    histories.append((reg, s, rng.uniform(0, 1, 3)))

for reg, s, x in histories:
    p, q, K, D = interior_price(reg, s, x)
    assert eigvalsh(K).min() > B - 2 * C_MAX - 1e-10
    off = D - np.diag(np.diag(D))
    assert np.max(off) <= 1e-12
    assert np.min(D @ np.ones(3)) > 0
    assert np.min(p) > 0 and np.min(q) > 0
    assert np.max(np.abs(q - np.diag(np.diag(D)) @ p)) < 1e-9

# Direct global deviation audit on representative difficult histories.
for reg, s, x in [
    ("IS", [SBAR], H),
    ("SU", [SBAR, 0.0], H),
    ("IS", [SBAR], np.array([0.4, 0.5, 5 / 6])),
    ("SU", [SBAR, 0.0], np.array([0.4, 0.5, 5 / 6])),
    ("SW", [0, 0, 0], np.array([0.2, 0.2, 0.8])),
]:
    p, q, _, _ = interior_price(reg, s, x)
    for i in range(3):
        assert global_price_gap(i, reg, s, x, p) < 2e-7


# ---------------------------------------------------------------------------
# Gate C: global location best responses.
# ---------------------------------------------------------------------------
def profits(reg: str, s, x, v: float = V, gamma: float = GAMMA) -> np.ndarray:
    p, q, _, _ = interior_price(reg, s, x, v=v)
    delta = np.array([circ_delta(x[i], H[i]) for i in range(3)])
    return p * q - 0.5 * gamma * delta**2


def location_br(i: int, reg: str, s, x, v: float = V, gamma: float = GAMMA):
    x = np.asarray(x, dtype=float).copy()

    def neg(z):
        xx = x.copy()
        xx[i] = z % 1.0
        return -float(profits(reg, s, xx, v=v, gamma=gamma)[i])

    grid = np.linspace(0.0, 1.0, 361, endpoint=False)
    vals = np.array([neg(z) for z in grid])
    best = (None, np.inf)
    step = 1.0 / len(grid)
    for k in np.argsort(vals)[:8]:
        center = grid[k]
        # Handle circle endpoint by evaluating local intervals in [0,1].
        lo = max(0.0, center - 2 * step)
        hi = min(1.0, center + 2 * step)
        r = minimize_scalar(neg, bounds=(lo, hi), method="bounded", options={"xatol": 1e-12})
        if r.fun < best[1]:
            best = (float(r.x % 1.0), float(r.fun))
    return best[0], -best[1]


def location_nash(reg: str, s, v: float = V, gamma: float = GAMMA):
    x = H.copy()
    for _ in range(120):
        old = x.copy()
        for i in range(3):
            x[i] = location_br(i, reg, s, x, v=v, gamma=gamma)[0]
        if np.max(np.abs(x - old)) < 5e-10:
            break
    cur = profits(reg, s, x, v=v, gamma=gamma)
    gaps = []
    for i in range(3):
        _, best = location_br(i, reg, s, x, v=v, gamma=gamma)
        gaps.append(best - cur[i])
    return x, cur, np.asarray(gaps)


IS_X, IS_PI, IS_GAPS = location_nash("IS", [SBAR])
SU_X, SU_PI, SU_GAPS = location_nash("SU", [SBAR, 0.0])
SW_X, SW_PI, SW_GAPS = location_nash("SW", [0.0, 0.0, 0.0])

assert np.max(np.abs(IS_X - H)) < 2e-5
assert np.max(np.abs(SW_X - H)) < 2e-5
assert SU_X[0] < H[0] - 0.02
assert SU_X[1] > H[1] + 0.02
assert abs(SU_X[2] - H[2]) < 2e-5
assert max(IS_GAPS.max(), SU_GAPS.max(), SW_GAPS.max()) < 2e-7


def welfare(reg: str, s, x, v: float = V, gamma: float = GAMMA):
    p, q, K, _ = interior_price(reg, s, x, v=v)
    cs = 0.5 * float(q @ K @ q)
    pi = profits(reg, s, x, v=v, gamma=gamma)
    W = cs / 3.0 + pi
    return W, cs, pi, p, q


# Gate D result-level witness: at fixed anchors an SU member prefers IS, but
# allowing strategic repositioning reverses that member ranking.
IS_FIXED = welfare("IS", [SBAR], H)
SU_FIXED = welfare("SU", [SBAR, 0.0], H)
IS_FULL = welfare("IS", [SBAR], IS_X)
SU_FULL = welfare("SU", [SBAR, 0.0], SU_X)

DELTA_FIXED = float(SU_FIXED[0][0] - IS_FIXED[0][0])
DELTA_FULL = float(SU_FULL[0][0] - IS_FULL[0][0])
assert DELTA_FIXED < -1e-4
assert DELTA_FULL > 1e-4
assert SU_FULL[0][2] < IS_FULL[0][2]  # outsider loses under the bilateral standard

# Small ex-ante local box around the architecture witness.  This is not a
# substitute for later policy/coalition robustness; it only checks that the
# repositioning reversal is not a knife-edge numerical artifact.
ROBUST = []
for vv, gg in itertools.product((0.07, 0.08, 0.09), (0.025, 0.03, 0.035)):
    ix, _, ig = location_nash("IS", [SBAR], v=vv, gamma=gg)
    sx, _, sg = location_nash("SU", [SBAR, 0.0], v=vv, gamma=gg)
    wi_t = welfare("IS", [SBAR], H, v=vv, gamma=gg)[0][0]
    ws_t = welfare("SU", [SBAR, 0.0], H, v=vv, gamma=gg)[0][0]
    wi_f = welfare("IS", [SBAR], ix, v=vv, gamma=gg)[0][0]
    ws_f = welfare("SU", [SBAR, 0.0], sx, v=vv, gamma=gg)[0][0]
    ok = (
        ws_t < wi_t
        and ws_f > wi_f
        and sx[0] < H[0] - 0.02
        and sx[1] > H[1] + 0.02
        and max(ig.max(), sg.max()) < 5e-7
    )
    ROBUST.append(ok)
assert sum(ROBUST) == 9


if __name__ == "__main__":
    print("Stage 4R4A analytic bounds:")
    print("  tau range:", TAU_MIN, TAU_MAX)
    print("  off-diagonal K range:", C_MIN, C_MAX)
    print("  SPD margin lower bound:", B - 2 * C_MAX)
    print("Canonical location equilibria:")
    print("  IS:", IS_X, "gaps", IS_GAPS)
    print("  SU:", SU_X, "gaps", SU_GAPS)
    print("  SW:", SW_X, "gaps", SW_GAPS)
    print("Member welfare difference SU-IS at fixed anchors:", DELTA_FIXED)
    print("Member welfare difference SU-IS with repositioning:", DELTA_FULL)
    print("Local reversal robustness:", sum(ROBUST), "/", len(ROBUST))
    print("STAGE 4R4A CONTINUATION/REPOSITIONING WITNESS PASS")
