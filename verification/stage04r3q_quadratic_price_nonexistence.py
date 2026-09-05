"""Stage 4R3Q: exact kill test for pure-quadratic localized price continuation.

Architecture selected at Stage 3R3:
- three firms on a unit circle;
- localized consideration: consumers on each positive-length arc compare only
  the two products bounding that arc;
- pure-quadratic transport/adaptation disutility;
- price stage after locations;
- at IS the network term is common across products and cancels pairwise.

This file tests the lexicographically first hostile feasible history:
    s_I = 1/4,
    x = (2/5, 1/2, 5/6),
    tau = 3/4 on every pair.

For an arc of length ell between i and j, firm i's raw share is
    ell/2 + (p_j-p_i)/(2*tau*ell),
clipped to [0,ell]. Hence a share kink occurs at
    p_i-p_j = +/- tau*ell**2.

The pure-price game is continuous and piecewise quadratic in each firm's own
nonnegative price. Therefore every global best response is attained at one of:
- p_i = 0;
- an interior FOC in an active-set cell;
- one of four incident arc-share kinks.

The code enumerates all 3^3 global arc active states and six necessary
best-response equations per firm, solves every nonsingular system exactly with
SymPy rationals, and verifies every candidate against the exact global
best-response correspondence. Solver failure/nonconvergence is never used as
negative evidence.

Result: zero pure Nash equilibria at this feasible history. This is sufficient
to reject Q1 and hence the Stage 3R3 pure-quadratic localized architecture for
the paper's pure-strategy SPNE.
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
    q = R(0)
    for j, ell in NEIGHBORS[i]:
        raw = ell / 2 + (p[j] - pi) / (2 * TAU * ell)
        q += clip(raw, R(0), ell)
    return sp.simplify(q)


def profit_i(pi, p, i):
    return sp.simplify(pi * demand_i(pi, p, i))


# Interior stationary candidate, useful only as a diagnostic.
p0, p1, p2 = sp.symbols("p0 p1 p2")
PS = [p0, p1, p2]
FOCS = []
for i in range(3):
    qi = R(0)
    slope = R(0)
    for j, ell in NEIGHBORS[i]:
        qi += ell / 2 + (PS[j] - PS[i]) / (2 * TAU * ell)
        slope += -1 / (2 * TAU * ell)
    FOCS.append(sp.Eq(qi + PS[i] * slope, 0))
SOL = sp.solve(FOCS, PS, dict=True)
assert len(SOL) == 1
P_INTERIOR = [sp.simplify(SOL[0][z]) for z in PS]
assert P_INTERIOR == [R(816, 17975), R(1167, 28760), R(7939, 86280)]


# Active-state affine representation.
# State for clockwise arc (i,j):
#   -1: i gets zero; j gets entire arc
#    0: interior split
#   +1: i gets entire arc

def affine_state(state):
    c = sp.zeros(3, 1)
    D = sp.zeros(3, 3)
    for st, (i, j, ell) in zip(state, ARCS):
        if st == -1:
            c[j] += ell
        elif st == 1:
            c[i] += ell
        else:
            coef = 1 / (2 * TAU * ell)
            c[i] += ell / 2
            c[j] += ell / 2
            D[i, i] -= coef
            D[i, j] += coef
            D[j, i] += coef
            D[j, j] -= coef
    return c, D


def equation_options(i, state):
    c, D = affine_state(state)
    out = []

    # Interior FOC: q_i + p_i dq_i/dp_i = 0.
    row = [D[i, j] for j in range(3)]
    row[i] = 2 * D[i, i]
    out.append(("FOC", row, -c[i]))

    # Nonnegative-price boundary.
    row = [R(0)] * 3
    row[i] = R(1)
    out.append(("ZERO", row, R(0)))

    # Four incident-arc kinks. Under quadratic distance, the switch occurs at
    # p_i-p_j = +/- tau*ell^2.
    for j, ell in NEIGHBORS[i]:
        row = [R(0)] * 3
        row[i] = R(1)
        row[j] = R(-1)
        out.append((f"KINK_ZERO_SHARE_{j}", row, TAU * ell**2))
        out.append((f"KINK_FULL_SHARE_{j}", row, -TAU * ell**2))
    return out


def exact_best_response(p, i):
    breakpoints = {R(0)}
    for j, ell in NEIGHBORS[i]:
        for z in (p[j] - TAU * ell**2, p[j] + TAU * ell**2):
            if z >= 0:
                breakpoints.add(sp.simplify(z))
    bps = sorted(breakpoints, key=lambda z: float(z))
    candidates = set(bps)

    # Between consecutive kinks, demand is affine in own price.
    for a, b in zip(bps[:-1], bps[1:]):
        if a == b:
            continue
        mid = (a + b) / 2
        c = R(0)
        d = R(0)
        for j, ell in NEIGHBORS[i]:
            raw_mid = ell / 2 + (p[j] - mid) / (2 * TAU * ell)
            if raw_mid <= 0:
                pass
            elif raw_mid >= ell:
                c += ell
            else:
                c += ell / 2 + p[j] / (2 * TAU * ell)
                d += -1 / (2 * TAU * ell)
        if d < 0:
            vertex = sp.simplify(-c / (2 * d))
            if a <= vertex <= b:
                candidates.add(vertex)

    values = [(profit_i(z, p, i), z) for z in candidates]
    best_value = max(v for v, _ in values)
    best_prices = {z for v, z in values if v == best_value}
    return best_value, best_prices


# Interior stationary point is not Nash: firms 0 and 1 have profitable global
# deviations. Record one exact regression against any future accidental reuse.
PI0_INTERIOR = profit_i(P_INTERIOR[0], P_INTERIOR, 0)
BR0_VALUE, BR0_PRICES = exact_best_response(P_INTERIOR, 0)
assert BR0_PRICES == {R(95727, 575200)}
assert PI0_INTERIOR == R(208896, 12924025)
assert BR0_VALUE == R(539038737, 16542752000)
assert BR0_VALUE > PI0_INTERIOR


def enumerate_pure_equilibria():
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

            ok = True
            for i in range(3):
                _, br_prices = exact_best_response(p, i)
                if p[i] not in br_prices:
                    ok = False
                    break
            if ok:
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
    print("interior stationary prices:", P_INTERIOR)
    print("firm-0 interior profit:", PI0_INTERIOR, float(PI0_INTERIOR))
    print("firm-0 exact global BR prices:", BR0_PRICES)
    print("firm-0 BR profit:", BR0_VALUE, float(BR0_VALUE))
    print("nonsingular necessary candidate systems checked:", N_SYSTEMS)
    print("pure price equilibria found:", len(EQUILIBRIA))
    print("STAGE 4R3Q NO-GO: pure-quadratic localized continuation fails Q1 at the first hostile feasible history")
