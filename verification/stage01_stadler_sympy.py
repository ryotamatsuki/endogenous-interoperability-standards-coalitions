"""Stage 1 symbolic audit of Stadler, Tobler Trexler & Unsorg (2022).

Re-derives the two-firm price subgame and first-stage symmetric compatibility FOC
from the published primitives and checks the own-SOC at the reported interior
candidate. SymPy exact algebra is used; numerical values are diagnostic only.

Source: Networks and Spatial Economics 22 (2022), 903–913.
DOI: 10.1007/s11067-022-09572-x
"""

import sympy as sp

alpha, beta, b, gamma, c = sp.symbols(
    "alpha beta b gamma c", positive=True, real=True
)
k1, k2, p1, p2 = sp.symbols("k1 k2 p1 p2", real=True)
k = sp.symbols("k", real=True)

# Published expected demand system.
den = 2 * alpha - beta * (2 - k1 - k2)
D1 = sp.Rational(1, 2) + (
    p2 - p1 + beta * (1 + 2 * b) * (k1 - k2) / 2
) / den
D2 = 1 - D1

pi1 = (p1 - c) * D1 - gamma * k1**2 / 2
pi2 = (p2 - c) * D2 - gamma * k2**2 / 2

# Stage-2 price equilibrium.
price_solution = sp.solve(
    [sp.diff(pi1, p1), sp.diff(pi2, p2)], [p1, p2], dict=True
)[0]

reported_p1 = c + alpha - beta * (3 - 2 * k1 - k2 - b * (k1 - k2)) / 3
reported_p2 = c + alpha - beta * (3 - 2 * k2 - k1 - b * (k2 - k1)) / 3
assert sp.simplify(price_solution[p1] - reported_p1) == 0
assert sp.simplify(price_solution[p2] - reported_p2) == 0

# Reduced first-stage profit and symmetric FOC.
pi1_reduced = sp.factor(pi1.subs(price_solution))
foc_k1_sym = sp.factor(sp.diff(pi1_reduced, k1).subs({k1: k, k2: k}))
reported_foc = beta * (5 + 4 * b) / 12 - gamma * k
assert sp.simplify(foc_k1_sym - reported_foc) == 0

k_star = beta * (5 + 4 * b) / (12 * gamma)

# Own second derivative at a symmetric profile and at the reported interior root.
soc_sym = sp.factor(sp.diff(pi1_reduced, k1, 2).subs({k1: k, k2: k}))
soc_at_k_star = sp.factor(soc_sym.subs(k, k_star))

# With alpha >= 3 beta, the denominator of soc_at_k_star is positive for an
# interior candidate. A sufficient/necessary local-max sign restriction from
# the numerator is therefore:
# 18 gamma (alpha - beta) > beta^2 (2 b^2 - 4 b - 7).
local_max_gap = sp.factor(
    18 * gamma * (alpha - beta) - beta**2 * (2 * b**2 - 4 * b - 7)
)

# Exact counterexample satisfying beta <= alpha/3 and the paper's interiority
# threshold gamma > beta(5+4b)/12, but violating the own-SOC.
example = {
    alpha: sp.Integer(3),
    beta: sp.Integer(1),
    b: sp.Integer(10),
    gamma: sp.Rational(303, 80),  # 3.7875 > 3.75
    c: sp.Integer(0),
}
example_k_star = sp.simplify(k_star.subs(example))
example_soc = sp.simplify(soc_at_k_star.subs(example))
assert 0 < example_k_star < 1
assert example_soc > 0

# Global-best-response diagnostic holding rival at the reported symmetric root.
profit_at_zero = sp.N(pi1_reduced.subs({**example, k2: example_k_star, k1: 0}))
profit_at_root = sp.N(
    pi1_reduced.subs({**example, k2: example_k_star, k1: example_k_star})
)
profit_at_one = sp.N(pi1_reduced.subs({**example, k2: example_k_star, k1: 1}))
assert profit_at_zero > profit_at_root

if __name__ == "__main__":
    print("price_solution =", price_solution)
    print("symmetric compatibility FOC =", foc_k1_sym)
    print("own SOC at symmetric profile =", soc_sym)
    print("own SOC at reported interior root =", soc_at_k_star)
    print("local-max gap (>0 required under alpha>=3beta) =", local_max_gap)
    print("counterexample k* =", example_k_star)
    print("counterexample own SOC =", sp.N(example_soc))
    print("profit k_i=0 =", profit_at_zero)
    print("profit k_i=k* =", profit_at_root)
    print("profit k_i=1 =", profit_at_one)
