"""Stage 4 verification for C-ESD.

Checks the weighted-Salop demand/price system, location FOCs/SOCs,
B-T / B-X / FULL witness, whole-circle location deviations, and a local
parameter box around the witness.
"""
from __future__ import annotations
import numpy as np
import sympy as sp
from numpy.linalg import inv, solve, LinAlgError
from scipy.optimize import minimize_scalar

# ---------- exact homogeneous checks ----------
t, v = sp.symbols("t v", positive=True)
H3 = 3*sp.eye(3)-sp.ones(3)

def homogeneous(G):
    A=sp.eye(3)-v*H3*G/(2*t)
    Ai=sp.simplify(A.inv())
    D=sp.simplify(-Ai*H3/(2*t))
    M=sp.diag(*[-1/D[i,i] for i in range(3)])
    b=sp.Matrix([sp.Rational(1,3)]*3)
    K=sp.simplify((sp.eye(3)-D*M).inv()*Ai)
    q=sp.simplify(K*b); p=sp.simplify(M*q)
    return q,p

qI,pI=homogeneous(sp.ones(3))
qW,pW=homogeneous(sp.eye(3))
assert all(sp.simplify(z-sp.Rational(1,3))==0 for z in qI)
assert all(sp.simplify(z-t/3)==0 for z in pI)
assert all(sp.simplify(z-sp.Rational(1,3))==0 for z in qW)
assert all(sp.simplify(z-(2*t-3*v)/6)==0 for z in pW)
W_IS=sp.factor(v/3-t/36)
W_SW=sp.factor(v/9-t/36)

# ---------- numerical primitives ----------
H=np.array([1/6,1/2,5/6],float)
B0=np.array([.5,0,.5])
BX=np.array([[0,.5,-.5],[-.5,0,.5],[.5,-.5,0]])

def G(reg):
    if reg=="IS": return np.ones((3,3))
    if reg=="SW": return np.eye(3)
    if reg=="SU": return np.array([[1,1,0],[1,1,0],[0,0,1]],float)
    raise ValueError(reg)

def Tau(reg,s,tbar=1.0):
    T=np.zeros((3,3))
    if reg=="IS":
        vals={(0,1):tbar-s[0],(0,2):tbar-s[0],(1,2):tbar-s[0]}
    elif reg=="SU":
        vals={(0,1):tbar-s[0],
              (0,2):tbar+(s[0]+s[1])/2,
              (1,2):tbar+(s[0]+s[1])/2}
    else:
        vals={(0,1):tbar+(s[0]+s[1])/2,
              (0,2):tbar+(s[0]+s[2])/2,
              (1,2):tbar+(s[1]+s[2])/2}
    for (i,j),z in vals.items(): T[i,j]=T[j,i]=z
    return T

def lap(T):
    L=np.zeros((3,3))
    for i in range(3):
        for j in range(i+1,3):
            w=1/T[i,j]
            L[i,i]+=w; L[j,j]+=w; L[i,j]-=w; L[j,i]-=w
    return L

def matrices(reg,s,vv,tbar=1.0):
    T=Tau(reg,s,tbar); L=lap(T)
    try: Ai=inv(np.eye(3)-.5*vv*L@G(reg))
    except LinAlgError: return None
    D=-.5*Ai@L
    if np.any(np.diag(D)>=0): return None
    M=np.diag(-1/np.diag(D))
    try: K=inv(np.eye(3)-D@M)@Ai
    except LinAlgError: return None
    return T,D,M,K

def base_ordered(x):
    x1,x2,x3=x
    return np.array([(1+x2-x3)/2,(x3-x1)/2,(1-x2+x1)/2])

def loc_nash(reg,s,vv,gamma,full=True):
    if not full: return H.copy()
    mm=matrices(reg,s,vv)
    if mm is None: return None
    T,D,M,K=mm; c=K@B0; R=K@BX
    Aeq=np.zeros((3,3)); rhs=np.zeros(3)
    for i in range(3):
        z=2*M[i,i]*R[i,i]
        if 2*M[i,i]*R[i,i]**2-gamma >= 0: return None
        Aeq[i,:]=z*R[i,:]; Aeq[i,i]-=gamma
        rhs[i]=-(z*c[i]+gamma*H[i])
    try: return solve(Aeq,rhs)
    except LinAlgError: return None

def ordered_eq(x,reg,s,vv):
    mm=matrices(reg,s,vv)
    if mm is None: return None
    T,D,M,K=mm; q=K@base_ordered(x); p=M@q
    if np.any(q<=0) or np.any(p<=0): return None
    N=G(reg)@q
    arcs=[(0,1,x[1]-x[0]),(1,2,x[2]-x[1]),(2,0,1-x[2]+x[0])]
    for i,j,ell in arcs:
        y=ell/2+(p[j]-p[i]+vv*(N[i]-N[j]))/(2*T[i,j])
        if not (0<y<ell): return None
    return q,p,T,N,arcs

def welfare(reg,s,vv,gamma,full=True):
    x=loc_nash(reg,s,vv,gamma,full)
    if x is None: return None
    eq=ordered_eq(x,reg,s,vv)
    if eq is None: return None
    q,p,T,N,arcs=eq
    cs=0.0
    for i,j,ell in arcs:
        y=ell/2+(p[j]-p[i]+vv*(N[i]-N[j]))/(2*T[i,j])
        cs+=(-p[i]+vv*N[i])*y-T[i,j]*y*y/2
        z=ell-y
        cs+=(-p[j]+vv*N[j])*z-T[i,j]*z*z/2
    pi=p*q-.5*gamma*(x-H)**2
    # Each country owns 1/3 of the uniform consumer population.
    return cs/3+pi, x, q, p

def su_policy(vv,gamma,sbar,full=True):
    s=np.array([sbar/2,0.0])
    for _ in range(50):
        old=s.copy()
        for pl in (0,1):
            def u(z):
                ss=s.copy(); ss[pl]=z
                out=welfare("SU",ss,vv,gamma,full)
                if out is None: return -1e12
                W=out[0]
                return W[0]+W[1] if pl==0 else W[2]
            r=minimize_scalar(lambda z:-u(z),bounds=(0,sbar),method="bounded")
            cand=[(0,u(0)),(sbar,u(sbar)),(r.x,u(r.x))]
            s[pl]=max(cand,key=lambda z:z[1])[0]
        if np.max(np.abs(s-old))<1e-9: break
    return s,welfare("SU",s,vv,gamma,full)

# ---------- whole-circle deviation audit ----------
def base_general(pos):
    p=np.mod(np.asarray(pos,float),1)
    order=np.argsort(p); b=np.zeros(3); arcs=[]
    for k in range(3):
        i=order[k]; j=order[(k+1)%3]; ell=(p[j]-p[i])%1
        b[i]+=ell/2; b[j]+=ell/2; arcs.append((i,j,ell))
    return b,arcs

def profits_general(pos,reg,s,vv,gamma):
    mm=matrices(reg,s,vv)
    if mm is None: return None
    T,D,M,K=mm; b,arcs=base_general(pos); q=K@b; p=M@q
    if np.any(q<=0) or np.any(p<=0): return None
    N=G(reg)@q
    for i,j,ell in arcs:
        y=ell/2+(p[j]-p[i]+vv*(N[i]-N[j]))/(2*T[i,j])
        if not (0<y<ell): return None
    delta=((np.mod(pos,1)-H+.5)%1)-.5
    return p*q-.5*gamma*delta**2

def global_gap(pos,reg,s,vv,gamma,i,ng=1201):
    cur=profits_general(pos,reg,s,vv,gamma)[i]
    best=-1e99
    for z in np.linspace(0,1,ng,endpoint=False):
        pp=np.array(pos,float); pp[i]=z
        pr=profits_general(pp,reg,s,vv,gamma)
        if pr is not None: best=max(best,pr[i])
    return best-cur

# ---------- Stage-4 witness ----------
V=0.04; GAMMA=0.11; SBAR=0.25
IS_F=welfare("IS",[SBAR],V,GAMMA,True)
IS_T=welfare("IS",[SBAR],V,GAMMA,False)
IS_X=welfare("IS",[0],V,GAMMA,True)
SW_F=welfare("SW",[0,0,0],V,GAMMA,True)
SW_T=welfare("SW",[0,0,0],V,GAMMA,False)
SW_X=SW_F
sF,SU_F=su_policy(V,GAMMA,SBAR,True)
sT,SU_T=su_policy(V,GAMMA,SBAR,False)
SU_X=welfare("SU",[0,0],V,GAMMA,True)

assert np.allclose(sF,[SBAR,0],atol=1e-6)
assert np.allclose(sT,[SBAR,0],atol=1e-6)
assert IS_T[0][0] > SU_T[0][0] and IS_T[0][0] > SU_T[0][2]
assert IS_X[0][0] > SU_X[0][0] and IS_X[0][0] > SU_X[0][2]
assert SU_F[0][0] > IS_F[0][0] > SU_F[0][2]
assert SU_F[0][0] > SW_F[0][0]
for i in range(3):
    assert global_gap(SU_F[1],"SU",sF,V,GAMMA,i) < 1e-5
for reg,s,out in [("IS",[SBAR],IS_F),("SW",[0,0,0],SW_F),
                  ("IS",[0],IS_X),("SU",[0,0],SU_X)]:
    for i in range(3):
        assert global_gap(out[1],reg,s,V,GAMMA,i) < 1e-5

# Local box: 23/27 points pass the strict FULL-only reversal plus global SU BR.
passed=0; total=0
for vv0 in [0.035,0.04,0.045]:
    for gg0 in [0.105,0.11,0.115]:
        for sb0 in [0.225,0.25,0.275]:
            total+=1
            sf,wf=su_policy(vv0,gg0,sb0,True)
            st,wt=su_policy(vv0,gg0,sb0,False)
            wi_f=welfare("IS",[sb0],vv0,gg0,True)
            wi_t=welfare("IS",[sb0],vv0,gg0,False)
            bx_i=welfare("IS",[0],vv0,gg0,True)
            bx_s=welfare("SU",[0,0],vv0,gg0,True)
            objs=[wf,wt,wi_f,wi_t,bx_i,bx_s]
            if any(z is None for z in objs): continue
            cond=(wf[0][0]>wi_f[0][0] and wt[0][0]<wi_t[0][0]
                  and bx_s[0][0]<bx_i[0][0])
            if cond and max(global_gap(wf[1],"SU",sf,vv0,gg0,i,401)
                            for i in range(3)) < 1e-5:
                passed+=1
assert passed >= 20

if __name__=="__main__":
    print("Exact symmetric W_IS =",W_IS)
    print("Exact symmetric W_SW =",W_SW)
    print("B-T IS/SU/SW",IS_T[0],SU_T[0],SW_T[0])
    print("B-X IS/SU/SW",IS_X[0],SU_X[0],SW_X[0])
    print("FULL IS/SU/SW",IS_F[0],SU_F[0],SW_F[0])
    print("FULL SU policy",sF,"locations",SU_F[1])
    print("local box",passed,"/",total)
