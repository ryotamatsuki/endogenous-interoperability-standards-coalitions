"""Stage 3 re-entry diagnostic for C2 bilateral implementation free-riding.

This is a mechanism-search diagnostic, not a Stage-4 proof.

Natural smooth bilateral technology:
    A_ij = a_i + a_j - a_i a_j

Interpretation: either endpoint can supply overlapping converter/interface coverage;
coverage provided by both is not double-counted.  A_ij is symmetric, so the
B0-style inverse-demand system is integrable.

The script derives the symmetric Cournot continuation, implementation marginal
returns, their IS/SU ordering, and scans the weak-network domain for the
headline stability-reversal diagnostic.
"""

import math
import numpy as np
import sympy as sp
from scipy.optimize import brentq

# ---------------------------------------------------------------------------
# Symbolic setup
# ---------------------------------------------------------------------------
v, kappa = sp.symbols("v kappa", positive=True)
a1, a2, a3, a = sp.symbols("a1 a2 a3 a", real=True)
q1, q2, q3 = sp.symbols("q1 q2 q3", real=True)


def A(x, y):
    return x + y - x * y

A12, A13, A23 = A(a1, a2), A(a1, a3), A(a2, a3)

# Cournot FOCs under IS.  Inverse demand is
# p_i = 1-Q + v sum_j A_ij q_j.
eq_I = [
    sp.Eq(1 - 2*q1 - q2 - q3 + v*(A12*q2 + A13*q3), 0),
    sp.Eq(1 - q1 - 2*q2 - q3 + v*(A12*q1 + A23*q3), 0),
    sp.Eq(1 - q1 - q2 - 2*q3 + v*(A13*q1 + A23*q2), 0),
]
sol_I = sp.solve(eq_I, [q1, q2, q3], simplify=True, dict=True)[0]

# SU_12: only firms 1 and 2 are formally linked.
eq_U = [
    sp.Eq(1 - 2*q1 - q2 - q3 + v*A12*q2, 0),
    sp.Eq(1 - q1 - 2*q2 - q3 + v*A12*q1, 0),
    sp.Eq(1 - q1 - q2 - 2*q3, 0),
]
sol_U = sp.solve(eq_U, [q1, q2, q3], simplify=True, dict=True)[0]

q1_I = sp.factor(sol_I[q1])
q1_U = sp.factor(sol_U[q1])

# At an interior Cournot quantity optimum, own slope is -1, hence p_i=q_i.
# There are three identical national markets.
pi_I_operating = 3*q1_I**2
pi_U_operating = 3*q1_U**2

MB_I = sp.factor(sp.diff(pi_I_operating, a1).subs({a1: a, a2: a, a3: a}))
MB_U = sp.factor(sp.diff(pi_U_operating, a1).subs({a1: a, a2: a}))
ratio = sp.factor(sp.simplify(MB_I / MB_U))

x = sp.factor(v * (2*a - a**2))
MB_I_target = 3*v*(1-a) / ((1+x)*(2-x)**3)
MB_U_target = 3*v*(1-a) / (2*(2-x)**3)
ratio_target = 2/(1+x)

assert sp.simplify(MB_I - MB_I_target) == 0
assert sp.simplify(MB_U - MB_U_target) == 0
assert sp.simplify(ratio - ratio_target) == 0

print("MB_I(a) =", MB_I_target)
print("MB_U(a) =", MB_U_target)
print("MB_I/MB_U =", ratio_target)
print("For 0<v<=1/4 and 0<=a<=1, x=v(2a-a^2)<=1/4, so ratio>=8/5>1.")

# Cross-partials are symmetric because A_ij=A_ji.
# This repairs the integrability defect of C1.
p1 = 1 - (q1+q2+q3) + v*(A12*q2 + A13*q3)
p2 = 1 - (q1+q2+q3) + v*(A12*q1 + A23*q3)
assert sp.simplify(sp.diff(p1,q2) - sp.diff(p2,q1)) == 0
print("Cross-partial symmetry: PASS")

# ---------------------------------------------------------------------------
# General public-good benchmark
# ---------------------------------------------------------------------------
# For pi_i=B(G)-c(e_i), G=sum e_i, symmetric e=G/n satisfies
# B'(G)=c'(G/n). Treating n continuously:
# dG/dn = c''(G/n) G/n^2 / [c''(G/n)/n - B''(G)] > 0
# under B''<=0 and c''>0.
print("Standard voluntary public good: total provision G_n rises with group size under B''<=0, c''>0.")

# ---------------------------------------------------------------------------
# Numerical diagnostic on weak-network domain
# ---------------------------------------------------------------------------
def mb_I_num(aa, vv):
    xx = vv*(2*aa-aa*aa)
    return 3*vv*(1-aa)/((1+xx)*(2-xx)**3)


def mb_U_num(aa, vv):
    xx = vv*(2*aa-aa*aa)
    return 3*vv*(1-aa)/(2*(2-xx)**3)


def equilibrium_a(vv, kk, regime):
    mb = mb_I_num if regime == "I" else mb_U_num
    f = lambda z: mb(z, vv) - kk*z
    return brentq(f, 0.0, 1.0)


def A_or(x, y):
    return x + y - x*y


def quantities_I(aa, vv):
    xx = vv*A_or(aa, aa)
    q = 1/(2*(2-xx))
    return q, q, q


def quantities_U(aa, vv):
    xx = vv*A_or(aa, aa)
    qm = 1/(2*(2-xx))
    qo = (1-xx)/(2*(2-xx))
    return qm, qm, qo


def consumer_surplus(qs, links, Aval, vv):
    q = np.asarray(qs, dtype=float)
    U = q.sum() - 0.5*np.dot(q,q)
    for i in range(3):
        for j in range(i+1,3):
            U -= q[i]*q[j]
            if (i,j) in links:
                U += vv*Aval[(i,j)]*q[i]*q[j]
    prices=[]
    for i in range(3):
        p=1-q.sum()
        for j in range(3):
            if i==j:
                continue
            key=(min(i,j),max(i,j))
            if key in links:
                p += vv*Aval[key]*q[j]
        prices.append(p)
    return U - sum(prices[i]*q[i] for i in range(3))


def W3_I(aa, vv, kk):
    qs=quantities_I(aa,vv)
    Aeq=A_or(aa,aa)
    links={(0,1),(0,2),(1,2)}
    vals={(0,1):Aeq,(0,2):Aeq,(1,2):Aeq}
    cs=consumer_surplus(qs,links,vals,vv)
    return cs + 3*qs[2]**2 - kk*aa**2/2


def W3_U_outsider(aa, vv):
    qs=quantities_U(aa,vv)
    Aeq=A_or(aa,aa)
    cs=consumer_surplus(qs,{(0,1)},{(0,1):Aeq},vv)
    return cs + 3*qs[2]**2

raw=0
count_ai_lt_au=0
count_delta_endo_neg=0
count_reversal_tech=0
min_delta=math.inf
for vv in np.linspace(0.005,0.25,50):
    for kk in np.logspace(-3,1,120):
        raw += 1
        ai=equilibrium_a(vv,kk,"I")
        au=equilibrium_a(vv,kk,"U")
        if ai < au - 1e-10:
            count_ai_lt_au += 1
        dendo=W3_I(ai,vv,kk)-W3_U_outsider(au,vv)
        dfull=W3_I(1.0,vv,0.0)-W3_U_outsider(1.0,vv)
        min_delta=min(min_delta,dendo)
        if dendo < -1e-10:
            count_delta_endo_neg += 1
        if dendo*dfull < -1e-10:
            count_reversal_tech += 1

print("Grid points:", raw)
print("a_IS < a_SU:", count_ai_lt_au)
print("Delta_3^endo < 0:", count_delta_endo_neg)
print("sign reversal vs costless full interoperability:", count_reversal_tech)
print("minimum Delta_3^endo on grid:", min_delta)

assert count_ai_lt_au == 0
assert count_delta_endo_neg == 0
assert count_reversal_tech == 0
