"""Stage 3R diagnostic for C-RP relative-profit interoperability.

Purpose:
- verify the exact symmetric marginal-return formulas used at Stage 3R;
- verify benchmark collapses at alpha=0 and under implementation-only RPE;
- scan the regular weak-network domain for the proposed implementation/stability reversal.

This is a Stage-3 mechanism diagnostic, not a Stage-4 theorem proof.
"""

import math
import numpy as np
import sympy as sp


a, v, alpha, kappa, z = sp.symbols("a v alpha kappa z", positive=True, real=True)

# z = v A(a,a), A(a,a)=2a-a^2.
D_I = 4 - 2*z - alpha*(1-z)
D_U = 8 - 4*z + 2*alpha*(1+z) - alpha**2

MB_I = (
    3*v*(2-alpha)*(1-a)
    *(2 + alpha*(1-z))
    *(4 + alpha*(alpha-2)*(1-z))
    / (D_I**3 * (2 + 2*z + alpha*(1-z)))
)

MB_U = (
    3*v*(2-alpha)*(1-a)
    *(alpha+2)**3
    *(alpha**2 - 2*alpha + 4)
    / (2*D_U**3)
)

ratio = sp.factor(MB_I / MB_U)
assert sp.simplify(ratio.subs(alpha, 0) - 2/(1+z)) == 0

# Artifact benchmark: downstream Cournot maximizes ordinary profit, while only the
# implementation objective is evaluated with relative profit.
MB_I_impl_only = 3*v*(1-a)*(2-alpha*z) / (2*(1+z)*(2-z)**3)
MB_U_impl_only = 3*v*(1-a)*(2-alpha*z) / (4*(2-z)**3)
assert sp.simplify(MB_I_impl_only/MB_U_impl_only - 2/(1+z)) == 0

print("Exact alpha=0 collapse: MB_I/MB_U =", sp.factor(ratio.subs(alpha, 0)))
print("Implementation-only RP ratio =", sp.factor(MB_I_impl_only/MB_U_impl_only))

MBI = sp.lambdify((a, v, alpha), MB_I.subs(z, v*(2*a-a**2)), "numpy")
MBU = sp.lambdify((a, v, alpha), MB_U.subs(z, v*(2*a-a**2)), "numpy")
RATIO = sp.lambdify((alpha, z), ratio, "numpy")


def solve_a(mb_fun, vv, al, kk):
    """Unique diagnostic root of MB(a)=kappa*a by monotone bisection on (0,1)."""
    lo, hi = 1.0e-10, 1.0 - 1.0e-10

    def f(x):
        return float(mb_fun(x, vv, al) - kk*x)

    flo, fhi = f(lo), f(hi)
    if not (math.isfinite(flo) and math.isfinite(fhi)):
        return math.nan
    if flo <= 0:
        return 0.0
    if fhi >= 0:
        return 1.0
    for _ in range(120):
        mid = 0.5*(lo+hi)
        fm = f(mid)
        if fm > 0:
            lo = mid
        else:
            hi = mid
    return 0.5*(lo+hi)


def quantities(vv, al, aa, regime):
    x = vv*(2*aa-aa*aa)
    if regime == "IS":
        d = 4-al-(2-al)*x
        q = 1/d
        return q, q, q, x
    d = 8-4*x+2*al*(1+x)-al*al
    qm = (al+2)/d
    qo = (2-2*x+al*(1+x))/d
    return qm, qm, qo, x


def delta_endo(vv, al, kk, ai, au):
    qi, _, _, xi = quantities(vv, al, ai, "IS")
    pi = 1-3*qi+2*xi*qi
    cs_i = (4.5-3*xi)*qi*qi
    w_i = cs_i + 3*pi*qi - 0.5*kk*ai*ai

    qm, _, qo, xu = quantities(vv, al, au, "SU")
    Q = 2*qm + qo
    po = 1-Q
    cs_u = 0.5*Q*Q - xu*qm*qm
    w_o = cs_u + 3*po*qo
    return w_i-w_o


def delta_full_tech(vv, al):
    qi, _, _, xi = quantities(vv, al, 1.0, "IS")
    pi = 1-3*qi+2*xi*qi
    wi = (4.5-3*xi)*qi*qi + 3*pi*qi

    qm, _, qo, xu = quantities(vv, al, 1.0, "SU")
    Q = 2*qm+qo
    po = 1-Q
    wu = 0.5*Q*Q-xu*qm*qm + 3*po*qo
    return wi-wu


# Interval-style grid for the marginal-return ratio itself.
ratio_min = (float("inf"), None)
ratio_max = (-float("inf"), None)
for al in np.linspace(0.0, 0.999, 201):
    for zz in np.linspace(0.0, 0.25, 201):
        rr = float(RATIO(al, zz))
        if rr < ratio_min[0]:
            ratio_min = (rr, (al, zz))
        if rr > ratio_max[0]:
            ratio_max = (rr, (al, zz))

print("ratio grid min:", ratio_min)
print("ratio grid max:", ratio_max)

# 6,000-point full-game diagnostic.
counts = {
    "raw": 0,
    "valid": 0,
    "a_IS<a_SU": 0,
    "Delta_endo<0": 0,
    "reversal_vs_alpha0": 0,
    "reversal_vs_full_tech": 0,
}
min_delta = float("inf")
min_adiff = float("inf")

for vv in np.linspace(0.005, 0.25, 20):
    for al in np.linspace(0.0, 0.95, 10):
        for kk in np.logspace(-3, 1, 30):
            counts["raw"] += 1
            ai = solve_a(MBI, vv, al, kk)
            au = solve_a(MBU, vv, al, kk)
            if not (math.isfinite(ai) and math.isfinite(au)):
                continue
            counts["valid"] += 1
            dd = delta_endo(vv, al, kk, ai, au)
            dft = delta_full_tech(vv, al)
            ai0 = solve_a(MBI, vv, 0.0, kk)
            au0 = solve_a(MBU, vv, 0.0, kk)
            d0 = delta_endo(vv, 0.0, kk, ai0, au0)

            min_delta = min(min_delta, dd)
            min_adiff = min(min_adiff, ai-au)

            if ai < au - 1e-9:
                counts["a_IS<a_SU"] += 1
            if dd < -1e-9:
                counts["Delta_endo<0"] += 1
            if dd*d0 < -1e-10:
                counts["reversal_vs_alpha0"] += 1
            if dd*dft < -1e-10:
                counts["reversal_vs_full_tech"] += 1

print("counts:", counts)
print("minimum Delta_endo:", min_delta)
print("minimum a_IS-a_SU:", min_adiff)

assert counts["valid"] == 6000
assert counts["a_IS<a_SU"] == 0
assert counts["Delta_endo<0"] == 0
assert counts["reversal_vs_alpha0"] == 0
assert counts["reversal_vs_full_tech"] == 0
