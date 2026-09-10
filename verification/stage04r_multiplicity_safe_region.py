"""Stage 4R repair verifier for C1 after Stage-4A multiplicity failure.

Purpose:
- preserve the Stage-4A crossing equilibrium at low repositioning cost;
- search for a selection-free higher-gamma region without changing the model;
- re-solve the headline welfare/stability objects at a conservative repair point.

This is construction-level evidence only. A fresh Stage 4A must independently
attack alternative equilibria, policy deviations, and threshold claims.
"""
from __future__ import annotations

import math
import numpy as np
from numpy.linalg import inv, solve
from scipy.optimize import brentq, minimize_scalar, root

A=2.0; B=10.0; C0=.30; LAM=.50; SBAR=.25
H=np.array([1/6,1/2,5/6],float)
PAIRS=((0,1),(0,2),(1,2))

def phi(z): return .5*(1+math.cos(2*math.pi*z))
def delta(z,h): return ((z-h+.5)%1)-.5

def Tau(reg,s):
    s=np.atleast_1d(np.asarray(s,float)); T=np.zeros((3,3))
    if reg=="IS": vals={(0,1):1-s[0],(0,2):1-s[0],(1,2):1-s[0]}
    elif reg=="SU": vals={(0,1):1-s[0],(0,2):1+(s[0]+s[1])/2,(1,2):1+(s[0]+s[1])/2}
    elif reg=="SW": vals={(0,1):1+(s[0]+s[1])/2,(0,2):1+(s[0]+s[2])/2,(1,2):1+(s[1]+s[2])/2}
    else: raise ValueError(reg)
    for (i,j),z in vals.items(): T[i,j]=T[j,i]=z
    return T

def Mmat(reg,s):
    s=np.atleast_1d(np.asarray(s,float)); M=np.zeros((3,3))
    if reg=="IS":
        for i,j in PAIRS: M[i,j]=M[j,i]=s[0]/SBAR
    elif reg=="SU": M[0,1]=M[1,0]=s[0]/SBAR
    return M

def Kmat(reg,s,x,v):
    x=np.asarray(x,float)%1; T=Tau(reg,s); M=Mmat(reg,s); K=np.eye(3)*B
    for i,j in PAIRS:
        K[i,j]=K[j,i]=C0+LAM*phi(x[i]-x[j])/T[i,j]-v*M[i,j]
    return K

def eq(reg,s,x,v):
    K=Kmat(reg,s,x,v); D=inv(K)
    p=solve(D+np.diag(np.diag(D)),D@(np.ones(3)*A))
    q=D@(np.ones(3)*A-p)
    assert np.min(p)>0 and np.min(q)>0
    return p,q,K

def profit(reg,s,x,v,gamma):
    p,q,_=eq(reg,s,x,v)
    d=np.array([delta(x[i],H[i]) for i in range(3)])
    return p*q-.5*gamma*d*d

def welfare(reg,s,x,v,gamma):
    p,q,K=eq(reg,s,x,v)
    return .5*float(q@K@q)/3+profit(reg,s,x,v,gamma)

def locfoc(reg,s,x,v,gamma,eps=2e-6):
    x=np.asarray(x,float); out=np.zeros(3)
    for i in range(3):
        xp=x.copy(); xm=x.copy(); xp[i]+=eps; xm[i]-=eps
        out[i]=(profit(reg,s,xp,v,gamma)[i]-profit(reg,s,xm,v,gamma)[i])/(2*eps)
    return out

def global_gap(i,reg,s,x,v,gamma,n=121):
    x=np.asarray(x,float); cur=float(profit(reg,s,x,v,gamma)[i])
    def pay(z):
        xx=x.copy(); xx[i]=z%1
        return float(profit(reg,s,xx,v,gamma)[i])
    grid=np.linspace(0,1,n,endpoint=False); vals=np.array([pay(z) for z in grid])
    step=1/n; best=float(vals.max())
    for k in np.argsort(vals)[-3:]:
        c=grid[k]
        r=minimize_scalar(lambda z:-pay(z),bounds=(c-2*step,c+2*step),method="bounded")
        best=max(best,-float(r.fun))
    return best-cur

def multistart_su(s12,s3,v,gamma,nstarts=10,seed=0):
    rng=np.random.default_rng(seed)
    starts=[H.copy(),np.array([.48,.19,5/6]),np.array([.14,.53,5/6])]
    starts += [rng.random(3) for _ in range(nstarts)]
    roots=[]
    for st in starts:
        ans=root(lambda x:locfoc("SU",[s12,s3],x,v,gamma),st,method="hybr",options={"maxfev":400})
        if not ans.success: continue
        x=ans.x%1
        if any(np.max(np.abs(((x-y+.5)%1)-.5))<3e-4 for y in roots): continue
        if max(global_gap(i,"SU",[s12,s3],x,v,gamma) for i in range(3))<2e-5:
            roots.append(x)
    return roots

def near_su(s12,s3,v,gamma):
    ans=root(lambda x:locfoc("SU",[s12,s3],x,v,gamma),H,method="hybr")
    assert ans.success
    x=ans.x%1
    assert max(global_gap(i,"SU",[s12,s3],x,v,gamma) for i in range(3))<2e-5
    return x

# Permanent Stage-4A regression: multiplicity survives at low gamma.
old=multistart_su(.25,.25,.12,.03,nstarts=18,seed=77)
assert len(old)>=2

# Construction search at gamma=.05, selected as a conservative lower audit point
# after locating the low-gamma multiplicity. No alternative equilibrium is found
# on this declared policy/parameter grid. This is not an analytic uniqueness proof.
hist=[]
for vv in (.07,.11,.13):
    for s12,s3 in ((0,0),(.05,.20),(.125,.125),(.20,.05),(.25,0),(.25,.25)):
        hist.append((vv,s12,s3))
for k,(vv,s12,s3) in enumerate(hist):
    roots=multistart_su(s12,s3,vv,.05,nstarts=10,seed=100+k)
    assert len(roots)==1,(vv,s12,s3,len(roots))

# Conservative headline repair point, deliberately away from the multiplicity frontier.
V=.11; GAMMA=.10
su=multistart_su(.25,.25,V,GAMMA,nstarts=30,seed=2026)
assert len(su)==1
XSU=su[0]
WIS=float(welfare("IS",[.25],H,V,GAMMA)[0])
WSU=welfare("SU",[.25,.25],XSU,V,GAMMA)
assert WSU[0]>WIS

# SU bloc-depth best-response construction scans with downstream re-solution.
grid=np.linspace(0,.25,21)
member=[]; outsider=[]
for z in grid:
    member.append(float(welfare("SU",[z,.25],near_su(z,.25,V,GAMMA),V,GAMMA)[0]))
    outsider.append(float(welfare("SU",[.25,z],near_su(.25,z,V,GAMMA),V,GAMMA)[2]))
assert np.all(np.diff(member)>0)
assert np.all(np.diff(outsider)>0)

# SW unilateral-depth completion at gamma=.10.
def sw_location(s1):
    def xd(d): return np.array([H[0],H[1]+d,H[2]-d])%1
    def f(d):
        x=xd(d); e=1e-6; xp=x.copy(); xm=x.copy(); xp[1]+=e; xm[1]-=e
        return (profit("SW",[s1,.25,.25],xp,V,GAMMA)[1]-profit("SW",[s1,.25,.25],xm,V,GAMMA)[1])/(2*e)
    gg=np.linspace(-.08,.08,81); ff=[f(d) for d in gg]; rr=[]
    for a,b,fa,fb in zip(gg[:-1],gg[1:],ff[:-1],ff[1:]):
        if fa*fb<0: rr.append(brentq(f,a,b))
    return xd(min(rr,key=abs))

sw=[]
for z in grid:
    x=sw_location(z)
    sw.append(float(welfare("SW",[z,.25,.25],x,V,GAMMA)[0]))
assert np.all(np.diff(sw)>0)
WSW=float(welfare("SW",[.25,.25,.25],H,V,GAMMA)[0])
assert WSU[0]>WSW

# Repaired threshold comparison at gamma=.10.
def member_diff(v,s3):
    x=near_su(.25,s3,v,GAMMA)
    return float(welfare("SU",[.25,s3],x,v,GAMMA)[0]-welfare("IS",[.25],H,v,GAMMA)[0])

V_FIX=1/15
V_EXO=brentq(lambda vv:member_diff(vv,0),.07,.14)
V_FULL=brentq(lambda vv:member_diff(vv,.25),.07,.14)
assert V_FIX<V_EXO<V_FULL
assert V_EXO<V<V_FULL

if __name__=="__main__":
    print("Stage-4A low-gamma multiplicity count:",len(old))
    print("gamma=.05 declared no-alternative grid histories:",len(hist))
    print("repair point SU location:",XSU)
    print("W_IS, W_SU_member, W_SU_outsider, W_SW:",WIS,float(WSU[0]),float(WSU[2]),WSW)
    print("v thresholds FIX, EXO-HIST, FULL:",V_FIX,V_EXO,V_FULL)
    print("STAGE 4R CONSTRUCTION REPAIR PASS — REPEAT STAGE 4A REQUIRED")
