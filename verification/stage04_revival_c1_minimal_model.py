"""Stage 4 revival minimal-model verifier: C1 Realized Interoperability Depth.

Workflow: research-paper-workflow v2.1, Stage 4 construction gate.
This script does not substitute for Stage 4A independent certification.

Binding architecture:
  partition rho -> bloc depths s -> product positions x -> Bertrand prices
  -> national welfare -> strict coalition blocking/stability.

C1 changes only realized interoperability. For i != j,
  K_ij = c0 + lambda*phi(x_i-x_j)/Tau_ij(rho,s) - v*M_ij(rho,s),
where within a multi-country bloc M_ij = chi(s_C)=s_C/s_bar and M_ij=0
across blocs. All other source primitives are retained.

The verifier establishes construction-level evidence for:
1. global affine-demand regularity on the audited parameter domain;
2. exact symmetric-IS policy calculus;
3. fixed-position, exogenous-depth, and FULL benchmark recovery;
4. whole-circle location best-response checks at high-stakes histories;
5. bloc-depth best-response checks;
6. a repositioning-essential coalition-stability reversal;
7. an ordered blocking-threshold shift B-FIX < B-EXO-HIST < FULL.
"""
from __future__ import annotations

import math
import numpy as np
import sympy as sp
from numpy.linalg import eigvalsh, inv, solve
from scipy.optimize import brentq, minimize_scalar

A = 2.0
B = 10.0
C0 = 0.30
LAM = 0.50
TBAR = 1.0
SBAR = 0.25
H = np.array([1 / 6, 1 / 2, 5 / 6], dtype=float)
PAIRS = ((0, 1), (0, 2), (1, 2))
V_CAN = 0.08
GAMMA_CAN = 0.03
V_BOX = (0.07, 0.08, 0.09)
GAMMA_BOX = (0.025, 0.03, 0.035)
V_THRESHOLD_AUDIT = (0.06, 0.16)


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


def M_matrix(reg: str, s) -> np.ndarray:
    """C1 realized interoperability, off-diagonal only."""
    s = np.atleast_1d(np.asarray(s, dtype=float))
    M = np.zeros((3, 3))
    if reg == "IS":
        m = s[0] / SBAR
        for i, j in PAIRS:
            M[i, j] = M[j, i] = m
    elif reg == "SU":
        m = s[0] / SBAR
        M[0, 1] = M[1, 0] = m
    elif reg != "SW":
        raise ValueError(reg)
    return M


def phi(z: float) -> float:
    return 0.5 * (1.0 + math.cos(2.0 * math.pi * z))


def circ_delta(z: float, h: float) -> float:
    return ((z - h + 0.5) % 1.0) - 0.5


def K_matrix(reg: str, s, x, v: float) -> np.ndarray:
    x = np.mod(np.asarray(x, dtype=float), 1.0)
    T = Tau(reg, s)
    M = M_matrix(reg, s)
    K = np.eye(3) * B
    for i, j in PAIRS:
        K[i, j] = K[j, i] = C0 + LAM * phi(x[i] - x[j]) / T[i, j] - v * M[i, j]
    return K


def price_quantity(reg: str, s, x, v: float):
    K = K_matrix(reg, s, x, v)
    D = inv(K)
    rhs = D @ (np.ones(3) * A)
    p = solve(D + np.diag(np.diag(D)), rhs)
    q = D @ (np.ones(3) * A - p)
    assert np.min(p) > 0 and np.min(q) > 0
    return p, q, K, D


def demand_kkt(reg: str, s, x, p, v: float) -> np.ndarray:
    K = K_matrix(reg, s, x, v)
    r = np.ones(3) * A - np.asarray(p, dtype=float)
    candidates = []
    for mask in range(8):
        S = [i for i in range(3) if mask & (1 << i)]
        q = np.zeros(3)
        if S:
            qS = solve(K[np.ix_(S, S)], r[S])
            q[S] = qS
            if np.any(qS < -1e-10):
                continue
        grad = K @ q - r
        I = [i for i in range(3) if i not in S]
        if I and np.any(grad[I] < -1e-10):
            continue
        if S and np.max(np.abs(grad[S])) > 1e-8:
            continue
        candidates.append((0.5 * q @ K @ q - r @ q, q))
    assert candidates
    return min(candidates, key=lambda z: z[0])[1]


def profits(reg: str, s, x, v: float, gamma: float) -> np.ndarray:
    p, q, _, _ = price_quantity(reg, s, x, v)
    d = np.array([circ_delta(x[i], H[i]) for i in range(3)])
    return p * q - 0.5 * gamma * d**2


def welfare(reg: str, s, x, v: float, gamma: float) -> np.ndarray:
    p, q, K, _ = price_quantity(reg, s, x, v)
    cs = 0.5 * float(q @ K @ q)
    return cs / 3.0 + profits(reg, s, x, v, gamma)


def operating_profit(i: int, reg: str, s, x, p, v: float) -> float:
    return float(p[i] * demand_kkt(reg, s, x, p, v)[i])


def global_price_gap(i: int, reg: str, s, x, pstar, v: float) -> float:
    pstar = np.asarray(pstar, dtype=float)
    current = operating_profit(i, reg, s, x, pstar, v)

    def payoff(z):
        pp = pstar.copy()
        pp[i] = z
        return operating_profit(i, reg, s, x, pp, v)

    grid = np.linspace(0.0, A + 2.0, 201)
    vals = np.array([payoff(z) for z in grid])
    best = float(vals.max())
    for k in np.argsort(vals)[-5:]:
        lo = max(0.0, grid[k] - 0.04)
        hi = min(A + 2.0, grid[k] + 0.04)
        r = minimize_scalar(lambda z: -payoff(z), bounds=(lo, hi), method="bounded")
        best = max(best, -float(r.fun))
    return best - current


# ---------------------------------------------------------------------------
# P1 construction evidence: uniform regularity on v in [0.06,0.16].
# ---------------------------------------------------------------------------
C_MIN = C0 - V_THRESHOLD_AUDIT[1]
C_MAX = C0 + LAM / (TBAR - SBAR)
assert C_MIN > 0
assert B > 2 * C_MAX
assert B * C_MIN > C_MAX**2
assert B - 2 * C_MAX + C_MIN > 0

for reg, s, x, vv in [
    ("IS", [0.0], H, 0.06),
    ("IS", [SBAR], H, 0.16),
    ("SU", [SBAR, SBAR], [0.135, 0.532, 5 / 6], V_CAN),
    ("SU", [0.10, 0.20], [0.20, 0.20, 0.80], 0.16),
    ("SW", [SBAR, SBAR, SBAR], H, V_CAN),
]:
    p, q, K, D = price_quantity(reg, s, x, vv)
    assert eigvalsh(K).min() > B - 2 * C_MAX - 1e-10
    off = D - np.diag(np.diag(D))
    assert np.max(off) <= 1e-12
    assert np.min(D @ np.ones(3)) > 0
    for i in range(3):
        assert global_price_gap(i, reg, s, np.asarray(x, float), p, vv) < 3e-7


# ---------------------------------------------------------------------------
# Exact symmetric-IS policy calculus.
# ---------------------------------------------------------------------------
aa, bb, cc = sp.symbols("a b c", positive=True)
W_IS_C = aa**2 * (3 * bb**2 + 2 * bb * cc - cc**2) / (8 * bb**2 * (bb + 2 * cc))
dWdc = sp.factor(sp.diff(W_IS_C, cc))
target = -aa**2 * (2 * bb**2 + bb * cc + cc**2) / (4 * bb**2 * (bb + 2 * cc) ** 2)
assert sp.simplify(dWdc - target) == 0

# At anchors phi_bar=1/4 and chi=s/sbar.
# c'(s_bar)<=0 is sufficient for W_IS to rise throughout [0,s_bar].
V_IS_FULL_THRESHOLD = SBAR * LAM * 0.25 / (TBAR - SBAR) ** 2
assert abs(V_IS_FULL_THRESHOLD - 1 / 18) < 1e-14


def su_derivative(d: float, s12: float, s3: float, v: float, gamma: float) -> float:
    x = np.array([H[0] - d, H[1] + d, H[2]])
    h = 1e-6
    xp = x.copy(); xp[0] += h
    xm = x.copy(); xm[0] -= h
    return float((profits("SU", [s12, s3], xp, v, gamma)[0]
                  - profits("SU", [s12, s3], xm, v, gamma)[0]) / (2 * h))


def su_location(s12: float, s3: float, v: float, gamma: float) -> np.ndarray:
    grid = np.linspace(-0.12, 0.18, 181)
    vals = np.array([su_derivative(d, s12, s3, v, gamma) for d in grid])
    roots = []
    for k in range(len(grid) - 1):
        if vals[k] == 0 or vals[k] * vals[k + 1] < 0:
            roots.append(brentq(lambda d: su_derivative(d, s12, s3, v, gamma), grid[k], grid[k + 1]))
    assert roots
    stable = []
    for d in roots:
        x = np.array([H[0] - d, H[1] + d, H[2]])
        e = 1e-4
        f0 = profits("SU", [s12, s3], x, v, gamma)[0]
        xp = x.copy(); xp[0] += e
        xm = x.copy(); xm[0] -= e
        sec = (profits("SU", [s12, s3], xp, v, gamma)[0] - 2 * f0
               + profits("SU", [s12, s3], xm, v, gamma)[0]) / e**2
        if sec < 0:
            stable.append((abs(d), d))
    assert stable
    d = min(stable)[1]
    return np.array([H[0] - d, H[1] + d, H[2]])


def global_location_gap(i: int, reg: str, s, x, v: float, gamma: float) -> float:
    x = np.asarray(x, dtype=float).copy()
    current = float(profits(reg, s, x, v, gamma)[i])

    def payoff(z):
        xx = x.copy(); xx[i] = z % 1.0
        return float(profits(reg, s, xx, v, gamma)[i])

    grid = np.linspace(0.0, 1.0, 241, endpoint=False)
    vals = np.array([payoff(z) for z in grid])
    best = float(vals.max())
    step = 1.0 / len(grid)
    for k in np.argsort(vals)[-6:]:
        lo = max(0.0, grid[k] - 2 * step)
        hi = min(1.0, grid[k] + 2 * step)
        r = minimize_scalar(lambda z: -payoff(z), bounds=(lo, hi), method="bounded")
        best = max(best, -float(r.fun))
    return best - current


# ---------------------------------------------------------------------------
# Policy best-response construction checks.
# In the threshold region v in [0.06,0.16], IS and both SU blocs choose s_bar.
# ---------------------------------------------------------------------------
def audit_su_policy_best_responses(v: float, gamma: float, full: bool) -> None:
    grid = np.linspace(0.0, SBAR, 31)
    member = []
    outsider = []
    for z in grid:
        xm = su_location(z, SBAR, v, gamma) if full else H
        xo = su_location(SBAR, z, v, gamma) if full else H
        member.append(float(welfare("SU", [z, SBAR], xm, v, gamma)[0]))
        outsider.append(float(welfare("SU", [SBAR, z], xo, v, gamma)[2]))
    assert int(np.argmax(member)) == len(grid) - 1
    assert int(np.argmax(outsider)) == len(grid) - 1
    assert np.min(np.diff(member)) > 0
    assert np.min(np.diff(outsider)) > 0


for vv in (0.06, V_CAN, 0.12, 0.16):
    # exact IS condition gives the same upper-bound optimum throughout this range
    assert vv > V_IS_FULL_THRESHOLD
    audit_su_policy_best_responses(vv, GAMMA_CAN, full=False)
    audit_su_policy_best_responses(vv, GAMMA_CAN, full=True)


# High-stakes whole-circle location audits.
for vv, gg in [(0.07, 0.025), (V_CAN, GAMMA_CAN), (0.09, 0.035), (0.12, GAMMA_CAN), (0.14, GAMMA_CAN)]:
    for s3 in (0.0, SBAR):
        x = su_location(SBAR, s3, vv, gg)
        for i in range(3):
            assert global_location_gap(i, "SU", [SBAR, s3], x, vv, gg) < 3e-6


# ---------------------------------------------------------------------------
# B-FIX exact member blocking threshold at full-depth policy equilibrium.
# ---------------------------------------------------------------------------
v = sp.symbols("v", real=True)
b = sp.Rational(10)
a = sp.Rational(2)
cm = sp.Rational(7, 15) - v
co = sp.Rational(2, 5)
Ksu = sp.Matrix([[b, cm, co], [cm, b, co], [co, co, b]])
Dsu = Ksu.inv()
one = sp.ones(3, 1)
psu = (Dsu + sp.diag(*[Dsu[i, i] for i in range(3)])).inv() * (Dsu * (a * one))
qsu = Dsu * (a * one - psu)
cssu = sp.Rational(1, 2) * (qsu.T * Ksu * qsu)[0]
Wsu_fix = sp.simplify(cssu / 3 + psu[0] * qsu[0])
Wis_fix = sp.simplify(a**2 * (3 * b**2 + 2 * b * cm - cm**2) / (8 * b**2 * (b + 2 * cm)))
DFIX = sp.factor(Wsu_fix - Wis_fix)
num, den = sp.fraction(DFIX)
assert sp.rem(sp.Poly(num, v), sp.Poly(15 * v - 1, v)) == 0
assert abs(float(DFIX.subs(v, 0.06))) > 1e-6 and float(DFIX.subs(v, 0.06)) > 0
assert float(DFIX.subs(v, 0.08)) < 0
V_FIX = 1 / 15


# ---------------------------------------------------------------------------
# Threshold objects for exogenous-depth and FULL models.
# B-EXO-HIST uses the pre-existing #65 positive-depth history:
# IS: s=s_bar; SU: (s12,s3)=(s_bar,0); SW: zero depth.
# FULL uses endogenous policy; in the threshold region all relevant blocs choose s_bar.
# ---------------------------------------------------------------------------
def delta_exo(vv: float, gamma: float) -> float:
    x = su_location(SBAR, 0.0, vv, gamma)
    return float(welfare("SU", [SBAR, 0.0], x, vv, gamma)[0]
                 - welfare("IS", [SBAR], H, vv, gamma)[0])


def delta_full(vv: float, gamma: float) -> float:
    x = su_location(SBAR, SBAR, vv, gamma)
    return float(welfare("SU", [SBAR, SBAR], x, vv, gamma)[0]
                 - welfare("IS", [SBAR], H, vv, gamma)[0])


def unique_root_on_grid(fun, lo: float, hi: float) -> float:
    grid = np.linspace(lo, hi, 51)
    vals = np.array([fun(z) for z in grid])
    assert np.all(np.diff(vals) < 0)
    idx = np.where(vals[:-1] * vals[1:] < 0)[0]
    assert len(idx) == 1
    return brentq(fun, grid[idx[0]], grid[idx[0] + 1])


thresholds = {}
for gg in GAMMA_BOX:
    v_exo = unique_root_on_grid(lambda z: delta_exo(z, gg), 0.06, 0.16)
    v_full = unique_root_on_grid(lambda z: delta_full(z, gg), 0.06, 0.16)
    assert V_FIX < v_exo < v_full
    thresholds[gg] = (v_exo, v_full)

V_EXO = thresholds[GAMMA_CAN][0]
V_FULL = thresholds[GAMMA_CAN][1]
assert abs(V_EXO - 0.11154504) < 2e-6
assert abs(V_FULL - 0.13368738) < 2e-6


# ---------------------------------------------------------------------------
# Explicit strict-blocking / residual-membership stability operator.
# A deviating coalition forms its own exclusive bloc; nondeviators preserve
# their existing coalition links where feasible. This gives the transitions below.
# ---------------------------------------------------------------------------
DEVIATIONS = {
    "IS": [((0, 1), "SU12"), ((0, 2), "SU13"), ((1, 2), "SU23"),
           ((0,), "SU23"), ((1,), "SU13"), ((2,), "SU12")],
    "SU12": [((0,), "SW"), ((1,), "SW"), ((0, 2), "SU13"), ((1, 2), "SU23"), ((0, 1, 2), "IS")],
    "SU13": [((0,), "SW"), ((2,), "SW"), ((0, 1), "SU12"), ((1, 2), "SU23"), ((0, 1, 2), "IS")],
    "SU23": [((1,), "SW"), ((2,), "SW"), ((0, 1), "SU12"), ((0, 2), "SU13"), ((0, 1, 2), "IS")],
    "SW": [((0, 1), "SU12"), ((0, 2), "SU13"), ((1, 2), "SU23"), ((0, 1, 2), "IS")],
}


def payoff_dict(wis: float, wm: float, wo: float, wsw: float):
    return {
        "IS": np.array([wis, wis, wis]),
        "SU12": np.array([wm, wm, wo]),
        "SU13": np.array([wm, wo, wm]),
        "SU23": np.array([wo, wm, wm]),
        "SW": np.array([wsw, wsw, wsw]),
    }


def stable_set(payoffs, tol: float = 1e-12):
    stable = []
    for reg, w in payoffs.items():
        blocked = False
        for coalition, alt in DEVIATIONS[reg]:
            if all(payoffs[alt][i] > w[i] + tol for i in coalition):
                blocked = True
                break
        if not blocked:
            stable.append(reg)
    return stable


def benchmark_payoffs(vv: float, gamma: float, kind: str):
    wis = float(welfare("IS", [SBAR], H, vv, gamma)[0])
    if kind == "B-FIX":
        wsu = welfare("SU", [SBAR, SBAR], H, vv, gamma)
        wsw = float(welfare("SW", [SBAR, SBAR, SBAR], H, vv, gamma)[0])
    elif kind == "B-EXO-HIST":
        x = su_location(SBAR, 0.0, vv, gamma)
        wsu = welfare("SU", [SBAR, 0.0], x, vv, gamma)
        wsw = float(welfare("SW", [0.0, 0.0, 0.0], H, vv, gamma)[0])
    elif kind == "FULL":
        x = su_location(SBAR, SBAR, vv, gamma)
        wsu = welfare("SU", [SBAR, SBAR], x, vv, gamma)
        wsw = float(welfare("SW", [SBAR, SBAR, SBAR], H, vv, gamma)[0])
    else:
        raise ValueError(kind)
    return payoff_dict(wis, float(wsu[0]), float(wsu[2]), wsw)


# Historical local box: B-FIX has only IS stable; FULL has exactly the three SUs stable.
for vv in V_BOX:
    for gg in GAMMA_BOX:
        assert stable_set(benchmark_payoffs(vv, gg, "B-FIX")) == ["IS"]
        assert stable_set(benchmark_payoffs(vv, gg, "FULL")) == ["SU12", "SU13", "SU23"]

# Full-interaction witness derived from the threshold ordering, not used to tune primitives.
V_INTERACTION = 0.12
assert V_EXO < V_INTERACTION < V_FULL
assert stable_set(benchmark_payoffs(V_INTERACTION, GAMMA_CAN, "B-FIX")) == ["IS"]
assert stable_set(benchmark_payoffs(V_INTERACTION, GAMMA_CAN, "B-EXO-HIST")) == ["IS"]
assert stable_set(benchmark_payoffs(V_INTERACTION, GAMMA_CAN, "FULL")) == ["SU12", "SU13", "SU23"]


if __name__ == "__main__":
    print("C1 global regularity: PASS on v in", V_THRESHOLD_AUDIT)
    print("IS full-depth threshold =", V_IS_FULL_THRESHOLD)
    print("B-FIX blocking threshold =", V_FIX)
    for gg, (ve, vf) in thresholds.items():
        print("gamma", gg, "B-EXO-HIST threshold", ve, "FULL threshold", vf)
    x_can = su_location(SBAR, SBAR, V_CAN, GAMMA_CAN)
    print("canonical FULL SU location =", x_can)
    print("canonical B-FIX stable set =", stable_set(benchmark_payoffs(V_CAN, GAMMA_CAN, "B-FIX")))
    print("canonical FULL stable set =", stable_set(benchmark_payoffs(V_CAN, GAMMA_CAN, "FULL")))
    print("v=0.12 B-FIX stable set =", stable_set(benchmark_payoffs(V_INTERACTION, GAMMA_CAN, "B-FIX")))
    print("v=0.12 B-EXO-HIST stable set =", stable_set(benchmark_payoffs(V_INTERACTION, GAMMA_CAN, "B-EXO-HIST")))
    print("v=0.12 FULL stable set =", stable_set(benchmark_payoffs(V_INTERACTION, GAMMA_CAN, "FULL")))
    print("STAGE 4 C1 MINIMAL MODEL CONSTRUCTION PASS")
