from __future__ import annotations

import sympy as sp

# Stage 4 verification for Coalition-Scope Implementation Crowd-Out (CSIC)
# Canonical workflow: research-paper-workflow v1.1
# Date: 2026-09-04
#
# Purpose:
# 1. derive Cournot continuation equilibria exactly;
# 2. derive symmetric implementation equilibrium conditions;
# 3. test coalition-scope crowd-out rather than assume it;
# 4. audit demand integrability / welfare;
# 5. diagnose benchmark stability reversals numerically after the analytic work.

v, kappa = sp.symbols("v kappa", positive=True, real=True)
a1, a2, a3, a = sp.symbols("a1 a2 a3 a", nonnegative=True, real=True)
q1, q2, q3 = sp.symbols("q1 q2 q3", real=True)
Q = q1 + q2 + q3

# -----------------------------------------------------------------------------
# 1. Cournot continuation: international standardization (IS)
# -----------------------------------------------------------------------------
p1_I = 1 - Q + v * a1 * (q2 + q3)
p2_I = 1 - Q + v * a2 * (q1 + q3)
p3_I = 1 - Q + v * a3 * (q1 + q2)
rev_I = [p1_I * q1, p2_I * q2, p3_I * q3]
foc_q_I = [sp.diff(rev_I[i], [q1, q2, q3][i]) for i in range(3)]
sol_I = sp.solve(foc_q_I, [q1, q2, q3], dict=True, simplify=True)[0]

D_I = 2 + v * (a1 + a2 + a3) - v**3 * a1 * a2 * a3
q1_I_expected = (
    1 + 2 * v * a1 + v**2 * (a1 * a2 + a1 * a3 - a2 * a3)
) / (2 * D_I)
assert sp.simplify(sol_I[q1] - q1_I_expected) == 0

# -----------------------------------------------------------------------------
# 2. Cournot continuation: standardization union SU_12
# -----------------------------------------------------------------------------
p1_U = 1 - Q + v * a1 * q2
p2_U = 1 - Q + v * a2 * q1
p3_U = 1 - Q
rev_U = [p1_U * q1, p2_U * q2, p3_U * q3]
foc_q_U = [sp.diff(rev_U[i], [q1, q2, q3][i]) for i in range(3)]
sol_U = sp.solve(foc_q_U, [q1, q2, q3], dict=True, simplify=True)[0]

qI = sp.factor(sol_I[q1].subs({a1: a, a2: a, a3: a}))
qM = sp.factor(sol_U[q1].subs({a1: a, a2: a}))
qO = sp.factor(sol_U[q3].subs({a1: a, a2: a}))
assert sp.simplify(qI - 1 / (2 * (2 - v * a))) == 0
assert sp.simplify(qM - qI) == 0
assert sp.simplify(qO - (1 - v * a) / (2 * (2 - v * a))) == 0

# Own inverse-demand slope is -1, hence p_i=q_i at an interior Cournot optimum.
assert sp.simplify(p1_I.subs(sol_I) - sol_I[q1]) == 0
assert sp.simplify(p1_U.subs(sol_U) - sol_U[q1]) == 0

# -----------------------------------------------------------------------------
# 3. Reduced implementation profits
# Three identical national markets -> total operating profit = 3 q_i^2.
# -----------------------------------------------------------------------------
Pi1_I = 3 * sol_I[q1] ** 2 - kappa * a1**2 / 2
Pi1_U = 3 * sol_U[q1] ** 2 - kappa * a1**2 / 2

dPi_I_sym = sp.factor(sp.diff(Pi1_I, a1).subs({a1: a, a2: a, a3: a}))
dPi_U_sym = sp.factor(sp.diff(Pi1_U, a1).subs({a1: a, a2: a}))

MB_I = sp.factor(dPi_I_sym + kappa * a)
MB_U = sp.factor(dPi_U_sym + kappa * a)

MB_I_expected = 3 * v * (3 - v * a) / (2 * (2 - v * a) ** 3 * (1 + v * a))
MB_U_expected = 9 * v / (4 * (2 - v * a) ** 3 * (1 + v * a))
assert sp.simplify(MB_I - MB_I_expected) == 0
assert sp.simplify(MB_U - MB_U_expected) == 0

K_I = sp.factor(MB_I / a)
K_U = sp.factor(MB_U / a)
assert sp.simplify(K_I / K_U - 2 * (3 - a * v) / 3) == 0
assert sp.simplify(
    (MB_I - MB_U)
    - 3 * v * (3 - 2 * a * v) / (4 * (2 - a * v) ** 3 * (1 + a * v))
) == 0

dK_I = sp.factor(sp.diff(K_I, a))
dK_U = sp.factor(sp.diff(K_U, a))

# On 0<v<=1/4 and 0<a<=1:
# dK_I/da < 0 because 2(av)^3 - 7(av)^2 + 3 > 0.
# dK_U/da < 0 because 5(av)^2 - 2 < 0.
# Thus each symmetric interior equation K_R(a)=kappa has at most one root.

# Own SOC at an interior symmetric stationary point.
soc_I = sp.factor(
    sp.diff(Pi1_I, a1, 2).subs({a1: a, a2: a, a3: a, kappa: K_I})
)
soc_U = sp.factor(
    sp.diff(Pi1_U, a1, 2).subs({a1: a, a2: a, kappa: K_U})
)

kbar_I = sp.factor(K_I.subs(a, 1))
kbar_U = sp.factor(K_U.subs(a, 1))

# -----------------------------------------------------------------------------
# 4. Global best-response shape for a fixed rival implementation
# -----------------------------------------------------------------------------
x, b = sp.symbols("x b", positive=True, real=True)
qI_own = sp.factor(sol_I[q1].subs({a1: x, a2: b, a3: b}))
qU_own = sp.factor(sol_U[q1].subs({a1: x, a2: b}))
Kown_I = sp.factor(6 * qI_own * sp.diff(qI_own, x) / x)
Kown_U = sp.factor(6 * qU_own * sp.diff(qU_own, x) / x)
dKown_I = sp.factor(sp.diff(Kown_I, x))
dKown_U = sp.factor(sp.diff(Kown_U, x))

# For 0<v<1, 0<b<=1, 0<x<=1, both dKown/dx are strictly negative.
# Hence the own reduced profit is single-peaked and the best response is global:
# x=1 if kappa <= Kown(1;b), otherwise the unique x in (0,1) solving Kown=kappa.

# -----------------------------------------------------------------------------
# 5. Integrability audit
# -----------------------------------------------------------------------------
cross_12 = sp.factor(sp.diff(p1_I, q2) - sp.diff(p2_I, q1))
assert cross_12 == v * (a1 - a2)
# Therefore a C^2 representative utility U(q;a) satisfying p_i=dU/dq_i cannot exist
# for general unilateral implementation deviations a1 != a2.

# -----------------------------------------------------------------------------
# 6. Equilibrium-consistent welfare diagnostic (not a global microfoundation)
# -----------------------------------------------------------------------------
z = sp.symbols("z", nonnegative=True, real=True)  # z = v*a at a symmetric profile
CS_I = sp.factor((9 - 6 * z) / (8 * (2 - z) ** 2))
CS_U = sp.factor((9 - 8 * z + z**2) / (8 * (2 - z) ** 2))
W_O_U = sp.factor((15 - 20 * z + 7 * z**2) / (8 * (2 - z) ** 2))

# In an interior IS implementation equilibrium let mu=kappa/v^2.
mu_I = sp.factor(3 * (3 - z) / (2 * z * (2 - z) ** 3 * (1 + z)))
G_I = sp.factor((15 - 6 * z) / (8 * (2 - z) ** 2) - mu_I * z**2 / 2)
dG_I = sp.factor(sp.diff(G_I, z))
dB = sp.factor(sp.diff(W_O_U, z))

# On 0<z<=1/4, dG_I>0 and dB<0, while G_I(0)=B(0)=15/32.
# Hence interior endogenous IS welfare of country 3 exceeds 15/32,
# while its SU-outsider welfare is below 15/32.

Delta_full_cost = sp.factor(7 * v / (8 * (2 - v)) - kappa / 2)
Delta_full_nocost = sp.factor(7 * v / (8 * (2 - v)))

# -----------------------------------------------------------------------------
# 7. Numerical region audit after exact derivation
# -----------------------------------------------------------------------------
def KI_float(aa: float, vv: float) -> float:
    return 3 * vv * (3 - aa * vv) / (2 * aa * (2 - aa * vv) ** 3 * (1 + aa * vv))


def KU_float(aa: float, vv: float) -> float:
    return 9 * vv / (4 * aa * (2 - aa * vv) ** 3 * (1 + aa * vv))


def bisect_decreasing(K, kk: float, vv: float, lo: float = 1e-12, hi: float = 1.0) -> float:
    if kk <= K(hi, vv):
        return 1.0
    for _ in range(120):
        mid = (lo + hi) / 2
        if K(mid, vv) > kk:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def eq_a(kk: float, vv: float, kind: str) -> float:
    return bisect_decreasing(KI_float if kind == "I" else KU_float, kk, vv)


def WI_float(aa: float, vv: float, kk: float) -> float:
    zz = vv * aa
    return (15 - 6 * zz) / (8 * (2 - zz) ** 2) - kk * aa * aa / 2


def WUO_float(aa: float, vv: float) -> float:
    zz = vv * aa
    return (15 - 20 * zz + 7 * zz * zz) / (8 * (2 - zz) ** 2)


count = 0
crowdout = 0
endo_unstable = 0
cost_benchmark_reversal = 0
nocost_benchmark_reversal = 0

for j in range(1, 26):
    vv = 0.25 * j / 25
    for m in range(1, 241):
        kk = 10 ** (-4 + 5 * (m - 1) / 239)  # 1e-4 ... 10
        ai = eq_a(kk, vv, "I")
        au = eq_a(kk, vv, "U")
        de = WI_float(ai, vv, kk) - WUO_float(au, vv)
        dfc = 7 * vv / (8 * (2 - vv)) - kk / 2
        dfn = 7 * vv / (8 * (2 - vv))
        count += 1
        crowdout += int(ai + 1e-10 < au)
        endo_unstable += int(de < -1e-10)
        cost_benchmark_reversal += int(de * dfc < -1e-10)
        nocost_benchmark_reversal += int(de * dfn < -1e-10)

# Exact illustrative benchmark parameters v=1/5, kappa=1/4.
vv = 0.2
kk = 0.25
ai = eq_a(kk, vv, "I")
au = eq_a(kk, vv, "U")
de = WI_float(ai, vv, kk) - WUO_float(au, vv)
dfc = 7 * vv / (8 * (2 - vv)) - kk / 2
dfn = 7 * vv / (8 * (2 - vv))

print("qI =", qI)
print("qM =", qM)
print("qO =", qO)
print("K_I(a) =", K_I)
print("K_U(a) =", K_U)
print("K_I/K_U =", sp.factor(K_I / K_U))
print("dK_I/da =", dK_I)
print("dK_U/da =", dK_U)
print("SOC_I_at_stationary =", soc_I)
print("SOC_U_at_stationary =", soc_U)
print("dKown_I/dx =", dKown_I)
print("dKown_U/dx =", dKown_U)
print("integrability_cross_difference =", cross_12)
print("G_I(z) =", G_I)
print("dG_I/dz =", dG_I)
print("W_SU_out(z) =", W_O_U)
print("dW_SU_out/dz =", dB)
print("Delta_full_cost =", Delta_full_cost)
print("Delta_full_nocost =", Delta_full_nocost)
print("grid draws =", count)
print("crowd-out cases a_IS<a_SU =", crowdout)
print("endogenous instability cases =", endo_unstable)
print("cost-bearing full-benchmark sign reversals =", cost_benchmark_reversal)
print("costless full-benchmark sign reversals =", nocost_benchmark_reversal)
print(
    "example v=.2, kappa=.25: a_IS, a_SU, Delta_endo, Delta_full_cost, Delta_full_nocost =",
    ai,
    au,
    de,
    dfc,
    dfn,
)

assert crowdout == 0
assert endo_unstable == 0
assert nocost_benchmark_reversal == 0
assert cost_benchmark_reversal > 0
assert abs(dfc + 1 / 36) < 1e-12
assert de > 0
