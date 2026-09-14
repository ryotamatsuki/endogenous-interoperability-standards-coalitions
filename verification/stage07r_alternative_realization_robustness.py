"""Stage 7R bounded robustness test after Stage 7.5 CONDITIONAL GO.

This verifier changes exactly one functional object:

    chi_alt(s) = 2 (s/s_bar) - (s/s_bar)^2

for s in [0,s_bar].  Players, timing, coalition rule, Tau map, demand,
repositioning technology, welfare accounting, and gamma are unchanged.

Required test:
- re-optimize policy under B-FIX and FULL;
- verify a strict B-FIX/FULL SU-vs-IS blocking-threshold difference;
- attack SU location multiplicity on declared higher-gamma policy histories.

This is a robustness artifact, not a replacement of the baseline C1 model.
"""
from __future__ import annotations

import math
import numpy as np
from numpy.linalg import inv, solve
from scipy.optimize import brentq, minimize_scalar, root

A=2.0; B=10.0; C0=.30; LAM=.50; SBAR=.25; GAMMA=.10
H=np.array([1/6,1/2,5/6],float)
PAIRS=((0,1),(0,2),(1,2))


def phi(z): return .5*(1+math.cos(2*math.pi*z))
def chi_alt(s):
    z=s/SBAR
    return 2*z-z*z

def circ_delta(z,h): return ((z-h+.5)%1)-.5


def tau(reg,s):
    s=np.atleast_1d(np.asarray(s,float)); T=np.zeros((3,3))
    if reg=="IS":
        vals={(0,1):1-s[0],(0,2):1-s[0],(1,2):1-s[0]}
    elif reg=="SU":
        vals={(0,1):1-s[0],
              (0,2):1+(s[0]+s[1])/2,
              (1,2):1+(s[0]+s[1])/2}
    else:
        raise ValueError(reg)
    for (i,j),z in vals.items(): T[i,j]=T[j,i]=z
    return T


def Mmat(reg,s):
    s=np.atleast_1d(np.asarray(s,float)); M=np.zeros((3,3))
    if reg=="IS":
        for i,j in PAIRS: M[i,j]=M[j,i]=chi_alt(s[0])
    elif reg=="SU":
        M[0,1]=M[1,0]=chi_alt(s[0])
    return M


def Kmat(reg,s,x,v):
    T=tau(reg,s); M=Mmat(reg,s); K=np.eye(3)*B
    for i,j in PAIRS:
        K[i,j]=K[j,i]=C0+LAM*phi(x[i]-x[j])/T[i,j]-v*M[i,j]
    return K


def price_quantity(reg,s,x,v):
    K=Kmat(reg,s,x,v); D=inv(K)
    p=solve(D+np.diag(np.diag(D)),D@(np.ones(3)*A))
    q=D@(np.ones(3)*A-p)
    assert np.min(p)>0 and np.min(q)>0
    return p,q,K


def profit(reg,s,x,v):
    p,q,_=price_quantity(reg,s,x,v)
    d=np.array([circ_delta(x[i],H[i]) for i in range(3)])
    return p*q-.5*GAMMA*d*d


def welfare(reg,s,x,v):
    p,q,K=price_quantity(reg,s,x,v)
    return .5*float(q@K@q)/3+profit(reg,s,x,v)


def su_symmetric_location(s12,s3,v):
    def xof(d): return np.array([H[0]-d,H[1]+d,H[2]])
    def foc(d):
        x=xof(d); e=1e-6
        xp=x.copy(); xm=x.copy(); xp[0]+=e; xm[0]-=e
        return (profit("SU",[s12,s3],xp,v)[0]-profit("SU",[s12,s3],xm,v)[0])/(2*e)
    a,b=-.08,.08
    if foc(a)*foc(b)<0:
        return xof(brentq(foc,a,b))
    grid=np.linspace(-.15,.15,61); vals=[foc(d) for d in grid]; roots=[]
    for l,r,fl,fr in zip(grid[:-1],grid[1:],vals[:-1],vals[1:]):
        if fl*fr<0: roots.append(brentq(foc,l,r))
    assert roots
    return xof(min(roots,key=abs))


def continuation(reg,s,v,full):
    if not full or reg=="IS": return H.copy()
    return su_symmetric_location(s[0],s[1],v)


def W(reg,s,v,full):
    return welfare(reg,s,continuation(reg,s,v,full),v)


def global_scalar_max(fun,n=81):
    grid=np.linspace(0,SBAR,n); vals=np.array([fun(z) for z in grid])
    k=int(np.argmax(vals)); step=SBAR/(n-1)
    lo=max(0,grid[k]-step); hi=min(SBAR,grid[k]+step)
    r=minimize_scalar(lambda z:-fun(z),bounds=(lo,hi),method="bounded",
                      options={"xatol":2e-8,"maxiter":80})
    candidates=[(float(grid[k]),float(vals[k])),(float(r.x),float(-r.fun)),
                (0.0,float(fun(0.0))),(SBAR,float(fun(SBAR)))]
    return max(candidates,key=lambda z:z[1])


def policy_equilibrium(v,full):
    s_is=global_scalar_max(lambda s:W("IS",[s],v,full).sum())[0]
    s12,s3=.18,.25
    for _ in range(40):
        n12=global_scalar_max(lambda z:W("SU",[z,s3],v,full)[:2].sum())[0]
        n3=global_scalar_max(lambda z:W("SU",[n12,z],v,full)[2])[0]
        if max(abs(n12-s12),abs(n3-s3))<1e-7:
            s12,s3=n12,n3; break
        s12,s3=n12,n3
    # final global-BR checks
    br12=global_scalar_max(lambda z:W("SU",[z,s3],v,full)[:2].sum())[0]
    br3=global_scalar_max(lambda z:W("SU",[s12,z],v,full)[2])[0]
    assert max(abs(br12-s12),abs(br3-s3))<2e-5
    return s_is,s12,s3


def member_difference(v,full):
    s_is,s12,s3=policy_equilibrium(v,full)
    return float(W("SU",[s12,s3],v,full)[0]-W("IS",[s_is],v,full)[0])


# Re-optimized thresholds under the pre-specified concave realization map.
V_FIX_ALT=brentq(lambda v:member_difference(v,False),.04,.07,xtol=2e-7)
V_FULL_ALT=brentq(lambda v:member_difference(v,True),.09,.12,xtol=2e-7)
assert V_FULL_ALT>V_FIX_ALT

# Transparent same-primitive witness strictly between the two cutoffs.
V_WIT=.08
D_FIX=member_difference(V_WIT,False)
D_FULL=member_difference(V_WIT,True)
assert D_FIX<0<D_FULL
P_FIX=policy_equilibrium(V_WIT,False)
P_FULL=policy_equilibrium(V_WIT,True)


# Independent full-system alternative-equilibrium attack for material FULL-SU
# policy histories in the repaired higher-gamma region.
def location_foc3(s12,s3,v,x,eps=1e-6):
    out=np.zeros(3)
    for i in range(3):
        xp=np.array(x,float); xm=np.array(x,float); xp[i]+=eps; xm[i]-=eps
        out[i]=(profit("SU",[s12,s3],xp,v)[i]-profit("SU",[s12,s3],xm,v)[i])/(2*eps)
    return out


def whole_circle_gap(i,s12,s3,v,x,n=151):
    x=np.asarray(x,float)%1; current=float(profit("SU",[s12,s3],x,v)[i])
    def pay(z):
        xx=x.copy(); xx[i]=z%1
        return float(profit("SU",[s12,s3],xx,v)[i])
    grid=np.linspace(0,1,n,endpoint=False); vals=np.array([pay(z) for z in grid])
    step=1/n; best=float(vals.max())
    for k in np.argsort(vals)[-4:]:
        c=grid[k]
        r=minimize_scalar(lambda z:-pay(z),bounds=(c-1.5*step,c+1.5*step),method="bounded")
        best=max(best,-float(r.fun))
    return best-current


def distinct_nash(s12,s3,v,nstarts=10,seed=0):
    rng=np.random.default_rng(seed)
    starts=[H.copy(),np.array([.48,.19,5/6]),np.array([.14,.53,5/6])]
    starts += [rng.random(3) for _ in range(nstarts)]
    eqs=[]
    for st in starts:
        ans=root(lambda x:location_foc3(s12,s3,v,x),st,method="hybr",options={"maxfev":300})
        if not ans.success: continue
        x=ans.x%1
        if any(np.max(np.abs(((x-y+.5)%1)-.5))<3e-4 for y in eqs): continue
        gaps=[whole_circle_gap(i,s12,s3,v,x) for i in range(3)]
        if max(gaps)<3e-6: eqs.append(x)
    return eqs


HISTORIES=[]
for vv in (.06,.08,.10,.11):
    for s12 in (0,.0625,.125,.1875,.25):
        HISTORIES.append((vv,s12,.25))
for k,(vv,s12,s3) in enumerate(HISTORIES):
    eqs=distinct_nash(s12,s3,vv,nstarts=10,seed=1000+k)
    assert len(eqs)==1,(vv,s12,s3,len(eqs),eqs)


if __name__=="__main__":
    print("chi_alt robustness thresholds FIX, FULL:",V_FIX_ALT,V_FULL_ALT)
    print("witness v=.08 member differences FIX, FULL:",D_FIX,D_FULL)
    print("witness policy IS/SU FIX:",P_FIX)
    print("witness policy IS/SU FULL:",P_FULL)
    print("selection-safety attacked histories:",len(HISTORIES))
    print("STAGE 7R ALTERNATIVE-REALIZATION ROBUSTNESS PASS")
