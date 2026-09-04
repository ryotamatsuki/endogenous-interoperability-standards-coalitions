"""
Stage 3R C-ESD diagnostic.
Endogenous Standard Differentiation x Strategic Product Repositioning.

This is a mechanism-search diagnostic, not a Stage-4 full solution.
It performs:
1) standard quadratic Hotelling scale-invariance kill;
2) quadratic Hotelling + symmetric network-effect kill;
3) three-firm Salop SU asymmetry diagnostic;
4) anchored-Salop numerical location Nash examples.

Requires: sympy, numpy, scipy.
"""
import sympy as sp
import numpy as np
from scipy.optimize import minimize_scalar

# ---------------------------------------------------------------------
# 1. Quadratic Hotelling, full coverage
# ---------------------------------------------------------------------
x1, x2, t = sp.symbols("x1 x2 t", positive=True)
d = x2 - x1
s = x1 + x2

q1 = (2 + s) / 6
q2 = (4 - s) / 6
p1 = t * d * (2 + s) / 3
p2 = t * d * (4 - s) / 3
pi1 = sp.factor(p1 * q1)
pi2 = sp.factor(p2 * q2)

# Scale invariance: pi_i = t * f_i(x)
assert sp.simplify(sp.diff(pi1 / t, t)) == 0
assert sp.simplify(sp.diff(pi2 / t, t)) == 0

a = sp.symbols("a", nonnegative=True)
hotelling_sym_location_gradient = sp.factor(
    sp.diff(pi1, x1).subs({x1: a, x2: 1-a})
)
assert sp.simplify(hotelling_sym_location_gradient + t*(4*a+1)/6) == 0

# ---------------------------------------------------------------------
# 2. Quadratic Hotelling + market-share network effects / partial compatibility
# Utility network term: v_n(q_i + lambda q_j)
# delta = v_n(1-lambda), H = t(x2-x1)-delta > 0.
# ---------------------------------------------------------------------
delta = sp.symbols("delta", positive=True)
H = t*d - delta
q1N = sp.factor((t*d*(2+s) - 3*delta) / (6*H))
q2N = sp.factor((t*d*(4-s) - 3*delta) / (6*H))
p1N = sp.factor((t*d*(2+s) - 3*delta) / 3)
p2N = sp.factor((t*d*(4-s) - 3*delta) / 3)
pi1N = sp.factor(p1N*q1N)

network_sym_location_gradient = sp.factor(
    sp.diff(pi1N, x1).subs({x1:a, x2:1-a})
)
# Exact cancellation: symmetric location incentive is unchanged.
assert sp.simplify(network_sym_location_gradient + t*(4*a+1)/6) == 0

# ---------------------------------------------------------------------
# 3. Three-firm linear Salop circle with network groups
# q = b - H3 p/(2t) + v H3 G q/(2t)
# where H3 = 3I-J and G maps market shares to compatible-network sizes.
# Normalize by t and set r=v/t.
# ---------------------------------------------------------------------
r = sp.symbols("r", positive=True)
H3 = 3*sp.eye(3) - sp.ones(3)

G_IS = sp.ones(3,3)
G_SW = sp.eye(3)
G_SU = sp.Matrix([[1,1,0],
                  [1,1,0],
                  [0,0,1]])

def salop_K(G):
    # t normalized to 1; r=v/t.
    A = sp.eye(3) - (r/2)*H3*G
    Ainv = sp.simplify(A.inv())
    B = sp.simplify(-Ainv*H3/2)  # q = Ainv b + B p
    slopes = [sp.factor(B[i,i]) for i in range(3)]
    M = sp.diag(*[-1/slopes[i] for i in range(3)])  # p/t = M q
    K = sp.simplify((sp.eye(3)-B*M).inv()*Ainv)      # q = K b
    return sp.Matrix([[sp.factor(sp.cancel(K[i,j])) for j in range(3)]
                      for i in range(3)]), M

K_IS, M_IS = salop_K(G_IS)
K_SW, M_SW = salop_K(G_SW)
K_SU, M_SU = salop_K(G_SU)

# Ordering x3=0 < x1=aa < x2=bb < 1.
aa, bb = sp.symbols("aa bb", real=True)
base = sp.Matrix([bb/2, (1-aa)/2, (1-bb+aa)/2])

def member_profit_gradient_at_equal(K, M, firm=0):
    q = sp.simplify(K*base)
    # actual operating profit = t * M_ii * q_i^2
    dpi_over_t = sp.factor(sp.diff(M[firm,firm]*q[firm]**2, aa))
    return sp.factor(dpi_over_t.subs({aa:sp.Rational(1,3),
                                      bb:sp.Rational(2,3)}))

grad_IS = member_profit_gradient_at_equal(K_IS, M_IS)
grad_SW = member_profit_gradient_at_equal(K_SW, M_SW)
grad_SU = member_profit_gradient_at_equal(K_SU, M_SU)

# IS and SW are symmetric at equidistant positions.
assert sp.simplify(grad_IS) == 0
assert sp.simplify(grad_SW) == 0

grad_SU_target = sp.factor(
    r*(3*r-2)*(12*r-7) /
    (6*(2*r-1)*(6*r-5)**2)
)
assert sp.simplify(grad_SU-grad_SU_target) == 0

# On regular diagnostic domain 0<r<1/2, grad_SU<0:
# r>0; (3r-2)<0; (12r-7)<0; (2r-1)<0; square>0.
grid_r = np.linspace(1e-4, 0.499, 1000)
grad_fn = sp.lambdify(r, grad_SU, "numpy")
assert np.all(grad_fn(grid_r) < 0)

# The SU member's normalized location gradient becomes more negative as r=v/t rises.
dgrad_SU_dr = sp.factor(sp.diff(grad_SU, r))
dgrad_fn = sp.lambdify(r, dgrad_SU_dr, "numpy")
assert np.all(dgrad_fn(grid_r) < 0)

# With an inherited-position adjustment cost gamma/2*(x_i-h_i)^2,
# the member's own-location objective is locally concave whenever gamma
# dominates the convexity of operating profit. Exact local threshold:
t_pos = sp.Symbol("t_pos", positive=True)
gamma_min_SU = sp.factor(
    r**2 * t_pos * (3*r-2)*(12*r-7)**2 /
    (4*(2*r-1)*(6*r-5)**2*(9*r-5)**2)
)

# ---------------------------------------------------------------------
# 4. Anchored-Salop numerical Nash.
# Anchors are inherited brand/technology positions; quadratic deviation cost
# regularizes the otherwise corner/indifferent location game.
# ---------------------------------------------------------------------
Hnp = np.eye(3)*3 - np.ones((3,3))
anchors = np.array([1/6, 1/2, 5/6], dtype=float)

def G_numpy(regime):
    if regime == "IS":
        return np.ones((3,3))
    if regime == "SW":
        return np.eye(3)
    if regime == "SU12":
        return np.array([[1,1,0],[1,1,0],[0,0,1]], dtype=float)
    raise ValueError(regime)

def base_shares(pos):
    pos=np.asarray(pos,float)
    arcs=np.array([pos[1]-pos[0], pos[2]-pos[1], 1-pos[2]+pos[0]])
    return np.array([(arcs[2]+arcs[0])/2,
                     (arcs[0]+arcs[1])/2,
                     (arcs[1]+arcs[2])/2])

def price_equilibrium(pos, tval, vval, regime):
    G=G_numpy(regime)
    A=np.eye(3) - (vval/(2*tval))*Hnp.dot(G)
    Ainv=np.linalg.inv(A)
    B=-Ainv.dot(Hnp)/(2*tval)
    slopes=np.diag(B)
    if np.any(slopes >= 0):
        return None
    M=np.diag(-1/slopes)
    K=np.linalg.inv(np.eye(3)-B.dot(M)).dot(Ainv)
    b=base_shares(pos)
    q=K.dot(b)
    p=M.dot(q)
    if np.any(q <= 0) or np.any(p <= 0):
        return None
    return q,p

def profits(pos,tval,vval,regime,gamma):
    pe=price_equilibrium(pos,tval,vval,regime)
    if pe is None:
        return None
    q,p=pe
    return p*q - 0.5*gamma*(np.asarray(pos)-anchors)**2

def best_response(i,pos,tval,vval,regime,gamma):
    pos=np.asarray(pos,float).copy()
    lo=anchors[i]-0.14
    hi=anchors[i]+0.14
    if i>0:
        lo=max(lo,pos[i-1]+1e-5)
    if i<2:
        hi=min(hi,pos[i+1]-1e-5)
    def objective(x):
        pp=pos.copy()
        pp[i]=x
        pr=profits(pp,tval,vval,regime,gamma)
        return 1e9 if pr is None else -pr[i]
    res=minimize_scalar(objective,bounds=(lo,hi),method="bounded",
                        options={"xatol":1e-11})
    return res.x

def location_nash(tval,vval,regime,gamma,init=None):
    pos=anchors.copy() if init is None else np.asarray(init,float).copy()
    for _ in range(1000):
        old=pos.copy()
        for i in range(3):
            pos[i]=best_response(i,pos,tval,vval,regime,gamma)
        if np.max(np.abs(pos-old))<1e-9:
            break
    return pos, price_equilibrium(pos,tval,vval,regime)

def diagnostic_table(vval=0.05,gamma=0.5):
    rows=[]
    for regime in ("IS","SW","SU12"):
        for tval in (0.5,1.0,2.0):
            pos,pe=location_nash(tval,vval,regime,gamma)
            q,p=pe
            rows.append((regime,tval,*pos,*q))
    return rows

if __name__ == "__main__":
    print("MODEL A: quadratic Hotelling")
    print("pi1 =", pi1)
    print("symmetric d pi1/dx1 =", hotelling_sym_location_gradient)
    print()
    print("MODEL B: quadratic Hotelling + network effect")
    print("symmetric d pi1/dx1 =", network_sym_location_gradient)
    print()
    print("3-firm Salop normalized gradients at equal spacing")
    print("IS:", grad_IS)
    print("SW:", grad_SW)
    print("SU12:", grad_SU)
    print("d(SU12 gradient)/dr:", dgrad_SU_dr)
    print("local gamma threshold:", gamma_min_SU)
    print()
    print("Anchored-Salop numerical location Nash (v=0.05, gamma=0.5)")
    for row in diagnostic_table():
        print(row)
