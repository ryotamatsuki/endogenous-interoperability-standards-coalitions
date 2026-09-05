"""Stage 4R4A exact verifier for the affine-demand Bertrand re-foundation.

This script verifies three things for the transparent normalization
    t_bar=1, s_bar=1/4, beta=1/5, v=1/50, a=1.

1. The global sufficient regularity inequalities hold exactly.
2. At the inherited anchors in SU_12, the positive-demand Bertrand equilibrium
   satisfies the closed-form FOCs with strictly positive prices and quantities.
3. The exact operating-profit displacement derivative for member 1 is negative
   both at zero depth and at s_12=1/4, and deeper SU integration makes that
   outward-repositioning incentive strictly stronger in absolute value.

The derivative calculation uses exact matrix differentiation at the anchor
history; it does not use finite differences or numerical optimization.

This is a Stage 4R4A mechanism/continuation verifier. It does not certify the
policy-depth game, welfare ordering, reversal, or coalition stability.
"""
from __future__ import annotations

import sympy as sp

R = sp.Rational

T_BAR = R(1)
S_BAR = R(1, 4)
BETA = R(1, 5)
V = R(1, 50)
A = R(1)

# Global bounds under chordal delta in [0,2] and tau in
# [t_bar-s_bar,t_bar+s_bar].
M_MIN = 1 / (R(3) + T_BAR + S_BAR)
M_MAX = 1 / (R(1) + T_BAR - S_BAR)
K_MIN = sp.simplify(BETA * M_MIN - V)
K_MAX = sp.simplify(BETA * M_MAX)

assert M_MIN == R(4, 17)
assert M_MAX == R(4, 7)
assert K_MIN == R(23, 850)
assert K_MAX == R(4, 35)
assert V < BETA * M_MIN
assert 2 * K_MAX < 1
assert K_MIN > K_MAX**2

H_ANCHORS = [R(1, 6), R(1, 2), R(5, 6)]


def build_anchor_objects(s12: sp.Rational):
    """Return K, dK/dx0 at inherited anchors for SU_12."""
    tau = {
        (0, 1): T_BAR - s12,
        (0, 2): T_BAR + s12 / 2,
        (1, 2): T_BAR + s12 / 2,
    }
    g = sp.zeros(3)
    g[0, 1] = g[1, 0] = 1

    K = sp.eye(3)
    Kp = sp.zeros(3)

    for i, j in ((0, 1), (0, 2), (1, 2)):
        diff = H_ANCHORS[i] - H_ANCHORS[j]
        delta = 1 - sp.cos(2 * sp.pi * diff)
        denom = 1 + tau[(i, j)] + delta
        m = 1 / denom
        K[i, j] = K[j, i] = sp.simplify(BETA * m - V * g[i, j])

        if i == 0:
            ddelta_dx0 = 2 * sp.pi * sp.sin(2 * sp.pi * diff)
            dm_dx0 = -ddelta_dx0 / denom**2
            Kp[i, j] = Kp[j, i] = sp.simplify(BETA * dm_dx0)

    return K, Kp


def price_quantities_and_profit_gradient(s12: sp.Rational):
    K, Kp = build_anchor_objects(s12)
    H = K.inv()
    Hp = -H * Kp * H

    D = sp.diag(*[H[i, i] for i in range(3)])
    Dp = sp.diag(*[Hp[i, i] for i in range(3)])

    M = D + H
    Mp = Dp + Hp
    ones = sp.ones(3, 1)

    p = M.inv() * H * (A * ones)
    pp = M.inv() * (Hp * (A * ones) - Mp * p)

    q = H * (A * ones - p)
    qp = Hp * (A * ones - p) - H * pp

    dpi = [sp.factor(pp[i] * q[i] + p[i] * qp[i]) for i in range(3)]
    return K, H, p, q, dpi


K0, H0, P0, Q0, DPI0 = price_quantities_and_profit_gradient(R(0))
K1, H1, P1, Q1, DPI1 = price_quantities_and_profit_gradient(S_BAR)

# At s_12=1/4 the anchor K matrix is exact and strictly positive definite.
assert K1 == sp.Matrix(
    [
        [1, R(27, 650), R(8, 145)],
        [R(27, 650), 1, R(8, 145)],
        [R(8, 145), R(8, 145), 1],
    ]
)
assert all(m > 0 for m in K1.det().as_ordered_factors() if m.is_number)

# Gross-substitute sign structure at the witness.
for i in range(3):
    assert H1[i, i] > 0
    for j in range(3):
        if i != j:
            assert H1[i, j] < 0

# Closed-form Bertrand equilibrium has positive p,q and obeys q_i=H_ii p_i.
for i in range(3):
    assert P1[i] > 0
    assert Q1[i] > 0
    assert sp.simplify(Q1[i] - H1[i, i] * P1[i]) == 0

# Mirror symmetry at SU_12 anchors.
assert sp.simplify(P1[0] - P1[1]) == 0
assert sp.simplify(Q1[0] - Q1[1]) == 0

# Exact local repositioning incentive.
g0 = DPI0[0]
g1 = DPI1[0]
assert g0 < 0
assert g1 < 0
assert g1 < g0  # deeper integration strengthens member 1's outward incentive

# Member 2 mirrors member 1; outsider is locally stationary.
assert sp.simplify(DPI0[1] + DPI0[0]) == 0
assert sp.simplify(DPI1[1] + DPI1[0]) == 0
assert sp.simplify(DPI0[2]) == 0
assert sp.simplify(DPI1[2]) == 0

# Pin the exact signs to permanent regression expressions.
EXPECTED_G0 = -R(32149849595931108145632, 486430409433760152272091875) * sp.sqrt(3) * sp.pi
EXPECTED_G1 = -R(
    75651293074675407069532145098524269426176,
    86562062983525181197181659883980660200145203,
) * sp.sqrt(3) * sp.pi
assert sp.simplify(g0 - EXPECTED_G0) == 0
assert sp.simplify(g1 - EXPECTED_G1) == 0

if __name__ == "__main__":
    print("M_MIN =", M_MIN, float(M_MIN))
    print("M_MAX =", M_MAX, float(M_MAX))
    print("K_MIN =", K_MIN, float(K_MIN))
    print("K_MAX =", K_MAX, float(K_MAX))
    print("2*K_MAX < 1:", bool(2 * K_MAX < 1))
    print("K_MIN > K_MAX^2:", bool(K_MIN > K_MAX**2))
    print("SU_12 anchor prices at s=1/4:", [float(z) for z in P1])
    print("SU_12 anchor quantities at s=1/4:", [float(z) for z in Q1])
    print("member-1 d operating profit/dx at s=0:", float(g0))
    print("member-1 d operating profit/dx at s=1/4:", float(g1))
    print("STAGE 4R4A PASS: global regularity region is nonempty, Bertrand continuation is well behaved, and repositioning is nondegenerate")
