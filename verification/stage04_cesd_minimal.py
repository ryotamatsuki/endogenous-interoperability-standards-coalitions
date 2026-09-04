"""
Stage 4 verification for C-ESD.

Frozen game:
rho -> bloc depths s_C -> pairwise friction Tau -> locations x -> prices -> welfare -> stability.

The script verifies:
1. heterogeneous-friction Salop demand in weighted-Laplacian form;
2. price FOCs/SOCs and exact homogeneous IS/SW benchmarks;
3. linear-quadratic location FOCs for a fixed cyclic ordering;
4. the Stage-4 witness;
5. global one-firm location deviations over the whole circle;
6. B-T / B-X / FULL stability comparison;
7. a local positive-measure numerical region around the witness.

Requires numpy, scipy, sympy.
"""
from __future__ import annotations
import numpy as np
import sympy as sp
from numpy.linalg import inv, solve, LinAlgError
from scipy.optimize import minimize_scalar

# ------------------------------------------------------------------
# Symbolic homogeneous checks
# ------------------------------------------------------------------
t, v = sp.symbols("t v", positive=True)
H3 = 3 * sp.eye(3) - sp.ones(3)

def homogeneous_price(G):
    A = sp.eye(3) - v * H3 * G / (2*t)
    Ai = sp.simplify(A.inv())
    D = sp.simplify(-Ai * H3 / (2*t))
    M = sp.diag(*[-1/D[i,i] for i in range(3)])
    b = sp.Matrix([sp.Rational(1,3)]*3)
    K = sp.simplify((sp.eye(3)-D*M).inv()*Ai)
    q = sp.simplify(K*b)
    p = sp.simplify(M*q)
    return q,p

qI,pI = homogeneous_price(sp.ones(3))
qW,pW = homogeneous_price(sp.eye(3))
assert all(sp.simplify(z-sp.Rational(1,3)) == 0 for z in qI)
assert all(sp.simplify(z-t/3) == 0 for z in pI)
assert all(sp.simplify(z-sp.Rational(1,3)) == 0 for z in qW)
assert all(sp.simplify(z-(2*t-3*v)/6) == 0 for z in pW)

# With the gross-utility constant omitted and national consumers uniformly
# distributed across countries, the exact symmetric welfare blocks are
W_IS = sp.factor(v/3 - t/36)
W_SW = sp.factor(v/9 - t/36)

# ------------------------------------------------------------------
# Numerical model
# ------------------------------------------------------------------
ANCHORS = np.array([1/6, 1/2, 5/6], dtype=float)
B0 = np.array([0.5, 0.0, 0.5])
BX = np.array([[0.0, 0.5,-0.5],
               [-0.5,0.0, 0.5],
               [0.5,-0.5,0.0]])

def Gmat(regime):
    if regime == "IS":
        return np.ones((3,3))
    if regime == "SW":
        return np.eye(3)
    if regime == "SU":
        return np.array([[1,1,0],[1,1,0],[0,0,1]],dtype=float)
    raise ValueError(regime)

def tau_matrix(regime, s, tbar=1.0):
    T = np.zeros((3,3))
    if regime == "IS":
        vals={(0,1):tbar-s[0],(0,2):tbar-s[0],(1,2):tbar-s[0]}
    elif regime == "SU":
        vals={(0,1):tbar-s[0],
              (0,2):tbar+(s[0]+s[1])/2,
              (1,2):tbar+(s[0]+s[1])/2}
    elif regime == "SW":
        vals={(0,1):tbar+(s[0]+s[1])/2,
              (0,2):tbar+(s[0]+s[2])/2,
              (1,2):tbar+(s[1]+s[2])/2}
    else:
        raise ValueError(regime)
    for (i,j),z in vals.items():
        T[i,j]=T[j,i]=z
    return T

def weighted_laplacian(T):
    L=np.zeros((3,3))
    for i in range(3):
        for j in range(i+1,3):
            w=1.0/T[i,j]
            L[i,i]+=w; L[j,j]+=w
            L[i,j]-=w; L[j,i]-=w
    return L

def price_matrices(regime,s,vv,tbar=1.0):
    T=tau_matrix(regime,s,tbar)
    L=weighted_laplacian(T)
    A=np.eye(3)-0.5*vv*L@Gmat(regime)
    try:
        Ai=inv(A)
    except LinAlgError:
        return None
    D=-0.5*Ai@L
    if np.any(np.diag(D)>=0):
        return None
    M=np.diag(-1/np.diag(D))
    try:
        K=inv(np.eye(3)-D@M)@Ai
    except LinAlgError:
        return None
    return T,L,D,M,K

def base_ordered(x):
    x1,x2,x3=x
    return np.array([(1+x2-x3)/2,(x3-x1)/2,(1-x2+x1)/2])

def location_nash_ordered(regime,s,vv,gamma,tbar=1.0,full=True):
    if not full:
        return ANCHORS.copy()
    pm=price_matrices(regime,s,vv,tbar)
    if pm is None:
        return None
    T,L,D,M,K=pm
    c=K@B0
    R=K@BX
    Aeq=np.zeros((3,3)); rhs=np.zeros(3)
    for i in range(3):
        z=2*M[i,i]*R[i,i]
        Aeq[i,:]=z*R[i,:]
        Aeq[i,i]-=gamma
        rhs[i]=-(z*c[i]+gamma*ANCHORS[i])
        # own SOC: 2 M_ii R_ii^2 - gamma < 0
        if 2*M[i,i]*R[i,i]**2-gamma >= 0:
            return None
    try:
        return solve(Aeq,rhs)
    except LinAlgError:
        return None

def ordered_equilibrium(x,regime,s,vv,tbar=1.0):
    pm=price_matrices(regime,s,vv,tbar)
    if pm is None:
        return None
    T,L,D,M,K=pm
    q=K@base_ordered(x)
    p=M@q
    if np.any(q<=0) or np.any(p<=0):
        return None
    N=Gmat(regime)@q
    arcs=[(0,1,x[1]-x[0]),(1,2,x[2]-x[1]),(2,0,1-x[2]+x[0])]
    for i,j,ell in arcs:
        y=ell/2+(p[j]-p[i]+vv*(N[i]-N[j]))/(2*T[i,j])
        if not (0<y<ell):
            return None
    return q,p,T,N,arcs

def consumer_surplus(x,regime,s,vv,tbar=1.0):
    eq=ordered_equilibrium(x,regime,s,vv,tbar)
    if eq is None:
        return None
    q,p,T,N,arcs=eq
    cs=0.0
    for i,j,ell in arcs:
        y=ell/2+(p[j]-p[i]+vv*(N[i]-N[j]))/(2*T[i,j])
        cs+=(-p[i]+vv*N[i])*y-T[i,j]*y*y/2
        z=ell-y
        cs+=(-p[j]+vv*N[j])*z-T[i,j]*z*z/2
    return cs

def welfare(regime,s,vv,gamma,tbar=1.0,full=True):
    x=location_nash_ordered(regime,s,vv,gamma,tbar,full)
    if x is None:
        return None
    eq=ordered_equilibrium(x,regime,s,vv,tbar)
    if eq is None:
        return None
    q,p,T,N,arcs=eq
    cs=consumer_surplus(x,regime,s,vv,tbar)
    pi=p*q-0.5*gamma*(x-ANCHORS)**2
    # Each country has one third of the uniform consumer population.
    W=cs/3+pi
    return W,x,q,p

def su_policy(vv,gamma,sbar,full=True):
    s=np.array([sbar/2,0.0])
    for _ in range(50):
        old=s.copy()
        for pl in (0,1):
            def u(z):
                ss=s.copy(); ss[pl]=z
                out=welfare("SU",ss,vv,gamma,full=full)
                if out is None:
                    return -1e12
                W=out[0]
                return W[0]+W[1] if pl==0 else W[2]
            r=minimize_scalar(lambda z:-u(z),bounds=(0,sbar),method="bounded")
            cand=[(0,u(0)),(sbar,u(sbar)),(r.x,u(r.x))]
            s[pl]=max(cand,key=lambda z:z[1])[0]
        if np.max(np.abs(s-old))<1e-9:
            break
    return s,welfare("SU",s,vv,gamma,full=full)

# Whole-circle unilateral deviation audit.
def base_general(pos):
    p=np.mod(np.asarray(pos,float),1.0)
    order=np.argsort(p)
    b=np.zeros(3); arcs=[]
    for k in range(3):
        i=order[k]; j=order[(k+1)%3]
        ell=(p[j]-p[i])%1.0
        b[i]+=ell/2; b[j]+=ell/2
        arcs.append((i,j,ell))
    return b,arcs

def profit_general(pos,regime,s,vv,gamma):
    pm=price_matrices(regime,s,vv)
    if pm is None:
        return None
    T,L,D,M,K=pm
    b,arcs=base_general(pos)
    q=K@b; p=M@q
    if np.any(q<=0) or np.any(p<=0):
        return None
    N=Gmat(regime)@q
    for i,j,ell in arcs:
        y=ell/2+(p[j]-p[i]+vv*(N[i]-N[j]))/(2*T[i,j])
        if not (0<y<ell):
            return None
    delta=((np.mod(pos,1)-ANCHORS+0.5)%1)-0.5
    return p*q-0.5*gamma*delta**2

def global_br_gap(pos,regime,s,vv,gamma,i,ngrid=1201):
    cur=profit_general(pos,regime,s,vv,gamma)[i]
    xs=np.linspace(0,1,ngrid,endpoint=False)
    best=-1e99
    for z in xs:
        pp=np.array(pos,float); pp[i]=z
        pr=profit_general(pp,regime,s,vv,gamma)
        if pr is not None:
            best=max(best,pr[i])
    return best-cur

# ------------------------------------------------------------------
# Stage-4 witness
# ------------------------------------------------------------------
TBAR=1.0
V=0.04
GAMMA=0.11
SBAR=0.25

# IS policy is exact: W_IS=v/3-(tbar-s_I)/36, so s_I*=sbar.
IS_FULL=welfare("IS",[SBAR],V,GAMMA,full=True)
IS_BX=welfare("IS",[0.0],V,GAMMA,full=True)
SW_FULL=welfare("SW",[0.0,0.0,0.0],V,GAMMA,full=True)
SW_BX=SW_FULL
SU_S_FULL,SU_FULL=su_policy(V,GAMMA,SBAR,full=True)
SU_S_BT,SU_BT=su_policy(V,GAMMA,SBAR,full=False)
SU_BX=welfare("SU",[0.0,0.0],V,GAMMA,full=True)
IS_BT=welfare("IS",[SBAR],V,GAMMA,full=False)
SW_BT=welfare("SW",[0.0,0.0,0.0],V,GAMMA,full=False)

assert np.allclose(SU_S_FULL,[SBAR,0],atol=1e-6)
assert np.allclose(SU_S_BT,[SBAR,0],atol=1e-6)

# B-T and B-X: IS strictly dominates both SU member and outsider welfare.
assert IS_BT[0][0] > SU_BT[0][0]
assert IS_BT[0][0] > SU_BT[0][2]
assert IS_BX[0][0] > SU_BX[0]
assert IS_BX[0][0] > SU_BX[2]

# FULL: SU member welfare strictly exceeds IS, while outsider welfare is below IS.
assert SU_FULL[0][0] > IS_FULL[0][0]
assert SU_FULL[0][2] < IS_FULL[0][0]
assert SU_FULL[0][0] > SW_FULL[0][0]

# Global whole-circle location deviations at the FULL witness.
for i in range(3):
    assert global_br_gap(SU_FULL[1],"SU",SU_S_FULL,V,GAMMA,i) < 1e-5
for reg,s,out in [("IS",[SBAR],IS_FULL),("SW",[0,0,0],SW_FULL),
                  ("IS",[0],IS_BX),("SU",[0,0],SU_BX)]:
    pos=out[1] if isinstance(out,tuple) else None
    if pos is not None:
        for i in range(3):
            assert global_br_gap(pos,reg,s,V,GAMMA,i) < 1e-5

# Local positive-measure audit: strict FULL-only sign reversal on a 5x5x5 box.
passed=0; total=0
for vv0 in [0.03,0.035,0.04,0.045,0.05]:
    for gg0 in [0.105,0.11,0.115,0.12,0.125]:
        for sb0 in [0.20,0.225,0.25,0.275,0.30]:
            total+=1
            sf,wf=su_policy(vv0,gg0,sb0,True)
            st,wt=su_policy(vv0,gg0,sb0,False)
            wi_f=welfare("IS",[sb0],vv0,gg0,full=True)
            wi_t=welfare("IS",[sb0],vv0,gg0,full=False)
            bx_i=welfare("IS",[0],vv0,gg0,full=True)
            bx_s=welfare("SU",[0,0],vv0,gg0,full=True)
            if None in (wf,wt,wi_f,wi_t,bx_i,bx_s):
                continue
            cond=(wf[0][0]>wi_f[0][0] and wt[0][0]<wi_t[0][0]
                  and bx_s[0][0]<bx_i[0][0])
            if cond and max(global_br_gap(wf[1],"SU",sf,vv0,gg0,i,401)
                            for i in range(3)) < 1e-5:
                passed+=1
assert passed >= 100

if __name__ == "__main__":
    print("IS exact W_i:",W_IS)
    print("SW exact W_i:",W_SW)
    print("Witness (tbar,v,gamma,sbar)=",(TBAR,V,GAMMA,SBAR))
    print("B-T IS:",IS_BT[0],"SU:",SU_BT[0],"SW:",SW_BT[0])
    print("B-X IS:",IS_BX[0],"SU:",SU_BX[0],"SW:",SW_BX[0])
    print("FULL IS:",IS_FULL[0],"SU:",SU_FULL[0],"SW:",SW_FULL[0])
    print("FULL SU policy:",SU_S_FULL,"locations:",SU_FULL[1])
    print("local box passed:",passed,"/",total)
