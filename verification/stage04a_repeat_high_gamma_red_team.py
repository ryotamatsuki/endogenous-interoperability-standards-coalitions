"""Repeat Stage 4A independent red-team after Stage 4R multiplicity repair.

This file is intentionally independent of the Stage-4/4R production solvers.
It reconstructs the C1 game from primitives and attacks the repaired higher-
gamma domain with full-system multi-start location searches, whole-circle best
responses, policy-deviation histories, and blocking-threshold recomputation.

The old low-gamma crossing equilibrium remains a mandatory regression.
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
def disp(z,h): return ((z-h+.5)%1)-.5

def tau(reg,s):
    s=np.atleast_1d(np.asarray(s,float)); T=np.zeros((3,3))
    if reg=="IS": vals={(0,1):1-s[0],(0,2):1-s[0],(1,2):1-s[0]}
    elif reg=="SU": vals={(0,1):1-s[0],(0,2):1+(s[0]+s[1])/2,(1,2):1+(s[0]+s[1])/2}
    elif reg=="SW": vals={(0,1):1+(s[0]+s[1])/2,(0,2):1+(s[0]+s[2])/2,(1,2):1+(s[1]+s[2])/2}
    else: raise ValueError(reg)
    for (i,j),z in vals.items(): T[i,j]=T[j,i]=z
    return T

def interoper(reg,s):
    s=np.atleast_1d(np.asarray(s,float)); M=np.zeros((3,3))
    if reg=="IS":
        for i,j in PAIRS: M[i,j]=M[j,i]=s[0]/SBAR
    elif reg=="SU": M[0,1]=M[1,0]=s[0]/SBAR
    return M

def Kmat(reg,s,x,v):
    x=np.asarray(x,float)%1; T=tau(reg,s); M=interoper(reg,s); K=np.eye(3)*B
    for i,j in PAIRS:
        K[i,j]=K[j,i]=C0+LAM*phi(x[i]-x[j])/T[i,j]-v*M[i,j]
    return K

def pq(reg,s,x,v):
    K=Kmat(reg,s,x,v); D=inv(K)
    p=solve(D+np.diag(np.diag(D)),D@(np.ones(3)*A))
    q=D@(np.ones(3)*A-p)
    assert np.min(p)>0 and np.min(q)>0
    return p,q,K

def profit(reg,s,x,v,gamma):
    p,q,_=pq(reg,s,x,v)
    d=np.array([disp(x[i],H[i]) for i in range(3)])
    return p*q-.5*gamma*d*d

def welfare(reg,s,x,v,gamma):
    p,q,K=pq(reg,s,x,v)
    return .5*float(q@K@q)/3+profit(reg,s,x,v,gamma)

def foc(reg,s,x,v,gamma,eps=2e-6):
    x=np.asarray(x,float); out=np.zeros(3)
    for i in range(3):
        xp=x.copy(); xm=x.copy(); xp[i]+=eps; xm[i]-=eps
        out[i]=(profit(reg,s,xp,v,gamma)[i]-profit(reg,s,xm,v,gamma)[i])/(2*eps)
    return out

def br_gap(i,reg,s,x,v,gamma,n=301):
    x=np.asarray(x,float).copy(); cur=float(profit(reg,s,x,v,gamma)[i])
    def pay(z):
        xx=x.copy(); xx[i]=z%1
        return float(profit(reg,s,xx,v,gamma)[i])
    grid=np.linspace(0,1,n,endpoint=False); vals=np.array([pay(z) for z in grid])
    step=1/n; best=float(vals.max())
    for k in np.argsort(vals)[-4:]:
        c=grid[k]
        r=minimize_scalar(lambda z:-pay(z),bounds=(c-2*step,c+2*step),method="bounded")
        best=max(best,-float(r.fun))
    return best-cur

def nash_set(reg,s,v,gamma,nstarts=50,seed=0):
    rng=np.random.default_rng(seed)
    starts=[H.copy(),np.array([.48,.19,5/6]),np.array([.14,.53,5/6])]
    starts += [rng.random(3) for _ in range(nstarts)]
    roots=[]
    for st in starts:
        ans=root(lambda x:foc(reg,s,x,v,gamma),st,method="hybr",options={"maxfev":600})
        if not ans.success: continue
        x=ans.x%1
        if np.max(np.abs(foc(reg,s,x,v,gamma)))>1e-5: continue
        if any(np.max(np.abs(((x-y+.5)%1)-.5))<2e-4 for y in roots): continue
        if max(br_gap(i,reg,s,x,v,gamma) for i in range(3))<2e-6:
            roots.append(x)
    return roots

def near_su(s12,s3,v,gamma,start=H):
    ans=root(lambda x:foc("SU",[s12,s3],x,v,gamma),np.asarray(start,float),method="hybr")
    assert ans.success
    x=ans.x%1
    assert max(br_gap(i,"SU",[s12,s3],x,v,gamma) for i in range(3))<2e-6
    return x

# Permanent low-gamma regression must remain visible.
assert len(nash_set("SU",[.25,.25],.12,.03,nstarts=60,seed=10))>=2

# Higher-gamma full-depth stress box: each point has one attacked pure Nash.
for k,(vv,gg) in enumerate((v,g) for v in (.09,.10,.11,.12,.13) for g in (.08,.10,.12)):
    assert len(nash_set("SU",[.25,.25],vv,gg,nstarts=50,seed=100+k))==1

# Material SU policy-deviation histories around the repaired region.
POLICY=((0,0),(.05,.25),(.125,.25),(.20,.25),(.25,.25),(.25,0),(.25,.05),(.25,.125),(.25,.20))
for k,(vv,gg,s12,s3) in enumerate((v,g,a,b) for v in (.10,.11,.12) for g in (.08,.10,.12) for a,b in POLICY):
    assert len(nash_set("SU",[s12,s3],vv,gg,nstarts=30,seed=1000+k))==1

# All three headline partitions at the repaired witness.
V=.11; GAMMA=.10
assert len(nash_set("IS",[.25],V,GAMMA,nstarts=80,seed=3001))==1
assert len(nash_set("SW",[.25,.25,.25],V,GAMMA,nstarts=80,seed=3002))==1
SU=nash_set("SU",[.25,.25],V,GAMMA,nstarts=80,seed=3003)
assert len(SU)==1
XSU=SU[0]

WIS=float(welfare("IS",[.25],H,V,GAMMA)[0])
WSU=welfare("SU",[.25,.25],XSU,V,GAMMA)
WSW=float(welfare("SW",[.25,.25,.25],H,V,GAMMA)[0])
assert WSU[0]>WIS and WSU[0]>WSW

# Independent SU policy-BR attack along each unilateral depth dimension.
grid=np.linspace(0,.25,51)
member=[]; outsider=[]
prev=H.copy()
for z in grid:
    x=near_su(z,.25,V,GAMMA,prev); prev=x
    member.append(float(welfare("SU",[z,.25],x,V,GAMMA)[0]))
prev=H.copy()
for z in grid:
    x=near_su(.25,z,V,GAMMA,prev); prev=x
    outsider.append(float(welfare("SU",[.25,z],x,V,GAMMA)[2]))
assert np.all(np.diff(member)>0)
assert np.all(np.diff(outsider)>0)

# Blocking thresholds, independently reconstructed on the repaired branch.
def mdiff(v,s3):
    x=near_su(.25,s3,v,GAMMA)
    return float(welfare("SU",[.25,s3],x,v,GAMMA)[0]-welfare("IS",[.25],H,v,GAMMA)[0])
V_FIX=1/15
V_EXO=brentq(lambda z:mdiff(z,0),.07,.14)
V_FULL=brentq(lambda z:mdiff(z,.25),.07,.14)
assert abs(V_EXO-.0993400329)<2e-8
assert abs(V_FULL-.1196400688)<2e-8
assert V_FIX<V_EXO<V<V_FULL

if __name__=="__main__":
    print("repaired SU x =",XSU)
    print("W_IS, W_SU_member, W_SU_outsider, W_SW =",WIS,float(WSU[0]),float(WSU[2]),WSW)
    print("thresholds =",V_FIX,V_EXO,V_FULL)
    print("REPEAT STAGE 4A HIGH-GAMMA RED-TEAM PASS")
