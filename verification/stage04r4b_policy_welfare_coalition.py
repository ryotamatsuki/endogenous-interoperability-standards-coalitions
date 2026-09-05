"""Stage 4R4B reconstruction / kill verifier.

This verifier uses only the Stage 4R4A affine-demand architecture and the
transparent pre-registered normalization

    t_bar=1, s_bar=1/4, beta=1/5, v=1/50, a=1, gamma=1/5.

It verifies:
1. exact B-T monotonicity: with outsider depth fixed at s_bar, the SU_12
   member-bloc welfare is strictly decreasing in s_12 on [0,s_bar];
2. the FULL symmetric SU continuation has a globally checked location NE on a
   policy grid and member-bloc welfare is strictly decreasing in s_12 while
   outsider welfare is increasing in its own depth;
3. the resulting canonical SU policy equilibrium is (s_12,s_3)=(0,s_bar);
4. IS chooses s_I=0 and symmetric SW chooses s_i=s_bar on the canonical grid;
5. B-T, B-X, and FULL all have the same strict coalition ranking: every country
   strictly prefers IS to the corresponding SU and SW continuation. Hence the
   full model does not generate a coalition-stability result unavailable in the
   benchmarks.

The numerical parts are a hostile finite/global audit at the frozen witness,
not a theorem for the entire parameter space. The exact B-T monotonicity result
is symbolic and uses Bernstein coefficients on the full policy interval.
"""
from __future__ import annotations

import math
import numpy as np
import sympy as sp
from scipy.optimize import brentq, minimize_scalar

T = 1.0
SB = 0.25
BETA = 0.2
V = 0.02
A = 1.0
GAMMA = 0.2
H_ANCHORS = np.array([1 / 6, 1 / 2, 5 / 6], dtype=float)


def network(regime: str) -> np.ndarray:
    g = np.zeros((3, 3))
    if regime == "IS":
        g[:] = 1.0
        np.fill_diagonal(g, 0.0)
    elif regime == "SU12":
        g[0, 1] = g[1, 0] = 1.0
    return g


def tau_matrix(regime: str, s) -> np.ndarray:
    tau = np.zeros((3, 3))
    if regime == "IS":
        for i in range(3):
            for j in range(i + 1, 3):
                tau[i, j] = tau[j, i] = T - float(s)
    elif regime == "SU12":
        sm, so = map(float, s)
        tau[0, 1] = tau[1, 0] = T - sm
        tau[0, 2] = tau[2, 0] = T + (sm + so) / 2
        tau[1, 2] = tau[2, 1] = T + (sm + so) / 2
    elif regime == "SW":
        ss = list(map(float, s))
        for i in range(3):
            for j in range(i + 1, 3):
                tau[i, j] = tau[j, i] = T + (ss[i] + ss[j]) / 2
    else:
        raise ValueError(regime)
    return tau


def continuation(regime: str, s, y: np.ndarray):
    x = (H_ANCHORS + np.asarray(y, dtype=float)) % 1.0
    tau = tau_matrix(regime, s)
    g = network(regime)
    K = np.eye(3)
    for i in range(3):
        for j in range(i + 1, 3):
            delta = 1.0 - math.cos(2.0 * math.pi * (x[i] - x[j]))
            bij = BETA / (1.0 + tau[i, j] + delta)
            K[i, j] = K[j, i] = bij - V * g[i, j]
    H = np.linalg.inv(K)
    D = np.diag(np.diag(H))
    p = np.linalg.solve(D + H, H @ (A * np.ones(3)))
    q = H @ (A * np.ones(3) - p)
    op_profit = p * q
    profit = op_profit - GAMMA * np.asarray(y, dtype=float) ** 2 / 2.0
    # With the quadratic representative consumer, net consumer surplus is
    # 1/2 q'Kq. With no home bias in the inherited symmetric three-country
    # model, national consumer surplus is one third of global CS.
    cs = 0.5 * float(q @ K @ q)
    W = profit + cs / 3.0
    return W, profit, cs, p, q


def own_profit_derivative(i: int, regime: str, s, y: np.ndarray, eps=2e-6):
    yp = np.array(y, dtype=float)
    ym = np.array(y, dtype=float)
    yp[i] += eps
    ym[i] -= eps
    return (
        continuation(regime, s, yp)[1][i]
        - continuation(regime, s, ym)[1][i]
    ) / (2.0 * eps)


def su_symmetric_location(sm: float, so: float) -> np.ndarray:
    """Solve and globally best-response-check the symmetric SU location NE."""

    def foc(d):
        return own_profit_derivative(0, "SU12", (sm, so), np.array([-d, d, 0.0]))

    grid = np.linspace(0.0, 0.08, 65)
    vals = [foc(float(d)) for d in grid]
    roots = []
    for left, right, fl, fr in zip(grid[:-1], grid[1:], vals[:-1], vals[1:]):
        if fl == 0:
            roots.append(float(left))
        elif fl * fr < 0:
            roots.append(brentq(foc, float(left), float(right), xtol=1e-13))
    if not roots:
        raise AssertionError("no symmetric SU location FOC root")

    # Keep only roots that survive unrestricted unilateral best-response checks.
    for d in roots:
        y = np.array([-d, d, 0.0])
        errors = []
        for i in range(3):
            def obj(z):
                yy = y.copy()
                yy[i] = z
                return -continuation("SU12", (sm, so), yy)[1][i]

            res = minimize_scalar(
                obj, bounds=(-0.5, 0.5), method="bounded", options={"xatol": 1e-11}
            )
            errors.append(abs(res.x - y[i]))
        if max(errors) < 3e-6:
            return y
    raise AssertionError("symmetric SU candidate failed global BR audit")


# ---------------------------------------------------------------------------
# Exact B-T theorem at the frozen normalization.
# ---------------------------------------------------------------------------
s = sp.symbols("s", real=True)
R = sp.Rational
beta = R(1, 5)
v = R(1, 50)
so = R(1, 4)
delta = R(3, 2)  # all anchor pairs are separated by one third of the circle

tau12 = 1 - s
tau13 = 1 + (s + so) / 2
k12 = beta / (1 + tau12 + delta) - v
k13 = beta / (1 + tau13 + delta)
K = sp.Matrix([[1, k12, k13], [k12, 1, k13], [k13, k13, 1]])
H = sp.simplify(K.inv())
D = sp.diag(*[H[i, i] for i in range(3)])
p = sp.simplify((D + H).inv() * H * sp.ones(3, 1))
q = sp.simplify(H * (sp.ones(3, 1) - p))
profit = [sp.simplify(p[i] * q[i]) for i in range(3)]
CS = sp.simplify((q.T * K * q)[0] / 2)
W_members = sp.simplify(profit[0] + profit[1] + R(2, 3) * CS)
dW = sp.factor(sp.diff(W_members, s))
num, den = sp.fraction(dW)

# Convert numerator on s in [0,1/4] to Bernstein form on t in [0,1].
t = sp.symbols("t")
poly = sp.Poly(sp.expand(num.subs(s, t / 4)), t)
n = poly.degree()
power = [poly.nth(j) for j in range(n + 1)]
bernstein = [
    sp.factor(
        sum(power[j] * sp.binomial(k, j) / sp.binomial(n, j) for j in range(k + 1))
    )
    for k in range(n + 1)
]
assert n == 16
assert all(b < 0 for b in bernstein)
assert den.subs(s, 0) > 0 and den.subs(s, R(1, 4)) > 0
assert dW.subs(s, 0) < 0 and dW.subs(s, R(1, 4)) < 0

# ---------------------------------------------------------------------------
# FULL SU policy reconstruction at the frozen witness.
# ---------------------------------------------------------------------------
policy_grid = np.linspace(0.0, SB, 9)
member_welfare = []
for sm in policy_grid:
    y = su_symmetric_location(float(sm), SB)
    W = continuation("SU12", (float(sm), SB), y)[0]
    member_welfare.append(float(W[0] + W[1]))
assert all(member_welfare[i] > member_welfare[i + 1] for i in range(len(member_welfare) - 1))

outsider_welfare = []
for so_val in policy_grid:
    y = su_symmetric_location(0.0, float(so_val))
    outsider_welfare.append(float(continuation("SU12", (0.0, float(so_val)), y)[0][2]))
assert all(outsider_welfare[i] < outsider_welfare[i + 1] for i in range(len(outsider_welfare) - 1))

SU_POLICY = (0.0, SB)
y_su_full = su_symmetric_location(*SU_POLICY)
W_su_full = continuation("SU12", SU_POLICY, y_su_full)[0]

# B-X: zero continuous depth but endogenous repositioning.
y_su_bx = su_symmetric_location(0.0, 0.0)
W_su_bx = continuation("SU12", (0.0, 0.0), y_su_bx)[0]

# B-T: endogenous policy at fixed inherited positions.
W_su_bt = continuation("SU12", SU_POLICY, np.zeros(3))[0]

# IS: symmetry pins y=0. Its bloc welfare is strictly lower at s_bar than at 0.
W_is_0 = continuation("IS", 0.0, np.zeros(3))[0]
W_is_hi = continuation("IS", SB, np.zeros(3))[0]
assert W_is_0.sum() > W_is_hi.sum()
IS_POLICY = 0.0
W_is_full = W_is_0

# SW: at the symmetric candidate, y=0. Own national welfare rises over the
# policy grid when the other two singleton depths are fixed at s_bar.
sw_own = []
for si in policy_grid:
    sw_own.append(float(continuation("SW", (float(si), SB, SB), np.zeros(3))[0][0]))
assert all(sw_own[i] < sw_own[i + 1] for i in range(len(sw_own) - 1))
SW_POLICY = (SB, SB, SB)
W_sw_full = continuation("SW", SW_POLICY, np.zeros(3))[0]
W_sw_bx = continuation("SW", (0.0, 0.0, 0.0), np.zeros(3))[0]

# Coalition-stability comparison. IS strictly Pareto-dominates the SU and SW
# continuations in B-X, B-T and FULL, so the same grand-coalition stability
# conclusion is already present without the full interaction.
assert np.all(W_is_full > W_su_bx)
assert np.all(W_is_full > W_su_bt)
assert np.all(W_is_full > W_su_full)
assert np.all(W_is_full > W_sw_bx)
assert np.all(W_is_full > W_sw_full)

# Repositioning is nonzero in SU but does not change the coalition ranking.
assert abs(y_su_full[0]) > 1e-4
assert abs(y_su_full[1]) > 1e-4
assert abs(y_su_full[2]) < 1e-6

if __name__ == "__main__":
    print("Exact B-T Bernstein coefficients all negative:", len(bernstein))
    print("d member-bloc welfare/ds at 0:", float(dW.subs(s, 0)))
    print("d member-bloc welfare/ds at s_bar:", float(dW.subs(s, R(1, 4))))
    print("FULL SU policy grid member welfare:", member_welfare)
    print("FULL SU outsider welfare grid:", outsider_welfare)
    print("SU policy equilibrium:", SU_POLICY)
    print("SU FULL y:", y_su_full)
    print("W IS:", W_is_full.tolist())
    print("W SU B-T:", W_su_bt.tolist())
    print("W SU B-X:", W_su_bx.tolist())
    print("W SU FULL:", W_su_full.tolist())
    print("W SW B-X:", W_sw_bx.tolist())
    print("W SW FULL:", W_sw_full.tolist())
    print("STAGE 4R4B NO-GO: endogenous repositioning changes levels but not the policy/coalition result; IS stability is already present in nested benchmarks")
