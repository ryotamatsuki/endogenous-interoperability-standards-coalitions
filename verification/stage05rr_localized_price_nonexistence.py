"""Stage 5RR: exact pure-price-equilibrium kill test for localized competition.

At the hostile off-path IS history
    x = (2/5, 1/2, 5/6), s_I = 1/4,
localized competition means that consumers on each arc compare only the two
products bounding that arc. Under IS the network term is common across all
products, so it cancels from pairwise choice and the price game is exactly
piecewise quadratic.

This script establishes two facts exactly with SymPy rationals:

1. The old interior candidate p=(1/4,43/200,57/200) is still not a Nash
   equilibrium even under localized competition: firm 1 (index 0) can raise
   its price to 71/200, abandon the short 0--1 arc, and increase profit from
   1/12 to 5041/60000.
2. The localized pure price game has no Nash equilibrium at this feasible
   location history. The proof is a finite exhaustive candidate enumeration.

Why the candidate enumeration is exhaustive:
- each firm's demand is the sum of two clipped affine arc shares;
- hence profit is continuous and piecewise quadratic in its own nonnegative
  price, holding rival prices fixed;
- a global best response must therefore be either p_i=0, an interior FOC in
  one active-set cell, or an arc-share kink p_i-p_j=+/-tau*ell_ij;
- there are 3^3 global arc active states (left capture / interior / right
  capture) and six candidate optimality equations per firm (FOC, zero, and
  four incident-arc kinks);
- all nonsingular systems are solved exactly, and every solution is checked
  against the exact global best-response correspondence.

The result is a valid Stage 5RR NO-GO for the single localized-consideration
repair. It does not assert that mixed price equilibria do not exist.
"""
from __future__ import annotations

import itertools
import sympy as sp

R = sp.Rational
TAU = R(3, 4)

# Clockwise arcs at x=(2/5,1/2,5/6).
ARCS = [
    (0, 1, R(1, 10)),
    (1, 2, R(1, 3)),
    (2, 0, R(17, 30)),
]
NEIGHBORS = {
    0: [(1, R(1, 10)), (2, R(17, 30))],
    1: [(0, R(1, 10)), (2, R(1, 3))],
    2: [(1, R(1, 3)), (0, R(17, 30))],
}


def clip(x, lo, hi):
    if x < lo:
        return lo
    if x > hi:
        return hi
    return x


def demand_i(pi, p, i):
    """Exact localized demand of firm i in the hostile IS subgame."""
    q = R(0)
    for j, ell in NEIGHBORS[i]:
        raw = ell / 2 + (p[j] - pi) / (2 * TAU)
        q += clip(raw, R(0), ell)
    return sp.simplify(q)


def profit_i(pi, p, i):
    return sp.simplify(pi * demand_i(pi, p, i))


# ---------------------------------------------------------------------------
# Exact second counterexample against the old interior candidate.
# ---------------------------------------------------------------------------
P_OLD = [R(1, 4), R(43, 200), R(57, 200)]
Q0_OLD = R(1, 3)
PI0_OLD = sp.simplify(P_OLD[0] * Q0_OLD)
P0_DEV = R(71, 200)
Q0_DEV = demand_i(P0_DEV, P_OLD, 0)
PI0_DEV = profit_i(P0_DEV, P_OLD, 0)

assert Q0_DEV == R(71, 300)
assert PI0_OLD == R(1, 12)
assert PI0_DEV == R(5041, 60000)
assert PI0_DEV > PI0_OLD


# ---------------------------------------------------------------------------
# Active-state affine demand representation.
# State for clockwise arc (i,j):
#   -1: i gets zero; j captures whole arc
#    0: interior split
#   +1: i captures whole arc
# ---------------------------------------------------------------------------
def affine_state(state):
    c = sp.zeros(3, 1)
    D = sp.zeros(3, 3)
    for st, (i, j, ell) in zip(state, ARCS):
        if st == -1:
            c[j] += ell
        elif st == 1:
            c[i] += ell
        else:
            c[i] += ell / 2
            c[j] += ell / 2
            D[i, i] += -1 / (2 * TAU)
            D[i, j] += 1 / (2 * TAU)
            D[j, i] += 1 / (2 * TAU)
            D[j, j] += -1 / (2 * TAU)
    return c, D


def equation_options(i, state):
    """All necessary optimality equations for a pure best response."""
    c, D = affine_state(state)
    out = []

    # Interior quadratic optimum in the maintained active cell:
    # q_i + p_i*dq_i/dp_i = 0.
    row = [D[i, j] for j in range(3)]
    row[i] = 2 * D[i, i]
    out.append(("FOC", row, -c[i]))

    # Nonnegative price boundary.
    row = [R(0)] * 3
    row[i] = R(1)
    out.append(("ZERO", row, R(0)))

    # Four incident-arc kinks.  For an arc of length ell between i and j,
    # firm i's share switches at p_i-p_j = +/- TAU*ell.
    for j, ell in NEIGHBORS[i]:
        row = [R(0)] * 3
        row[i] = R(1)
        row[j] = R(-1)
        out.append((f"KINK_ZERO_SHARE_{j}", row, TAU * ell))
        out.append((f"KINK_FULL_SHARE_{j}", row, -TAU * ell))
    return out


def exact_best_response(p, i):
    """Exact global best-response value and correspondence for firm i."""
    breakpoints = {R(0)}
    for j, ell in NEIGHBORS[i]:
        for z in (p[j] - TAU * ell, p[j] + TAU * ell):
            if z >= 0:
                breakpoints.add(sp.simplify(z))
    bps = sorted(breakpoints, key=lambda z: float(z))

    candidates = set(bps)

    # On each bounded interval demand is affine: q_i=c+d*p_i.
    for a, b in zip(bps[:-1], bps[1:]):
        if a == b:
            continue
        mid = (a + b) / 2
        c = R(0)
        d = R(0)
        for j, ell in NEIGHBORS[i]:
            raw_mid = ell / 2 + (p[j] - mid) / (2 * TAU)
            if raw_mid <= 0:
                pass
            elif raw_mid >= ell:
                c += ell
            else:
                c += ell / 2 + p[j] / (2 * TAU)
                d += -1 / (2 * TAU)
        if d < 0:
            vertex = sp.simplify(-c / (2 * d))
            if a <= vertex <= b:
                candidates.add(vertex)

    values = [(profit_i(z, p, i), z) for z in candidates]
    best_value = max(v for v, _ in values)
    best_prices = {z for v, z in values if v == best_value}
    return best_value, best_prices


def enumerate_pure_equilibria():
    """Enumerate every finite necessary candidate and verify global BRs."""
    equilibria = []
    nonsingular_systems = 0

    for state in itertools.product((-1, 0, 1), repeat=3):
        options = [equation_options(i, state) for i in range(3)]
        for combo in itertools.product(*options):
            A = sp.Matrix([x[1] for x in combo])
            b = sp.Matrix([x[2] for x in combo])
            if A.det() == 0:
                continue
            p = list(A.LUsolve(b))
            nonsingular_systems += 1
            if any(z < 0 for z in p):
                continue

            is_equilibrium = True
            for i in range(3):
                _, br_prices = exact_best_response(p, i)
                if p[i] not in br_prices:
                    is_equilibrium = False
                    break
            if is_equilibrium:
                equilibria.append(
                    {
                        "state": state,
                        "modes": tuple(x[0] for x in combo),
                        "prices": tuple(p),
                    }
                )

    return nonsingular_systems, equilibria


N_SYSTEMS, EQUILIBRIA = enumerate_pure_equilibria()
assert N_SYSTEMS == 2440
assert EQUILIBRIA == []


if __name__ == "__main__":
    print("old firm-1 profit:", PI0_OLD, float(PI0_OLD))
    print("localized raising-price deviation demand:", Q0_DEV, float(Q0_DEV))
    print("localized raising-price deviation profit:", PI0_DEV, float(PI0_DEV))
    print("nonsingular necessary candidate systems checked:", N_SYSTEMS)
    print("pure price equilibria found:", len(EQUILIBRIA))
    print("STAGE 5RR NO-GO: localized-consideration repair still lacks a pure price continuation at the hostile feasible history")
