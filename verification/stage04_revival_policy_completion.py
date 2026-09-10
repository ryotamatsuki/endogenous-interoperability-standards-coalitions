"""Stage 4 completion audit for policy/location histories not covered by the C1 core verifier.

This file complements `stage04_revival_c1_minimal_model.py`.  It checks the
remaining symmetric IS and unilateral SW policy histories needed by the
Stage-4 policy equilibrium and stability statements.  It is construction
verification only; Stage 4A must independently certify the object.
"""
from __future__ import annotations

import math
import numpy as np
from numpy.linalg import inv, solve
from scipy.optimize import brentq, minimize_scalar

A=2.0; B=10.0; C0=.30; LAM=.50; TBAR=1.0; SBAR=.25
H=np.array([1/6,1/2,5/6],float)
PAIRS=((0,1),(0,2),(1,2))


def Tau(reg,s):
    s=np.atleast_1d(np.asarray(s,float)); T=np.zeros((3,3))
    if reg=="IS":
        vals={(0,1):1-s[0],(0,2):1-s[0],(1,2):1-s[0]}
    elif reg=="SU":
        vals={(0,1):1-s[0],(0,2):1+(s[0]+s[1])/2,(1,2):1+(s[0]+s[1])/2}
    elif reg=="SW":
        vals={(0,1):1+(s[0]+s[1])/2,(0,2):1+(s[0]+s[2])/2,(1,2):1+(s[1]+s[2])/2}
    else: raise ValueError(reg)
    for (i,j),z in vals.items(): T[i,j]=T[j,i]=z
    return T


def M(reg,s):
    MM=np.zeros((3,3)); s=np.atleast_1d(np.asarray(s,float))
    if reg=="IS":
        m=s[0]/SBAR
        for i,j in PAIRS: MM[i,j]=MM[j,i]=m
    elif reg=="SU":
        MM[0,1]=MM[1,0]=s[0]/SBAR
    elif reg!="SW": raise ValueError(reg)
    return MM


def phi(z): return .5*(1+math.cos(2*math.pi*z))
def delta(z,h): return ((z-h+.5)%1)-.5


def Kmat(reg,s,x,v):
    T=Tau(reg,s); MM=M(reg,s); x=np.asarray(x,float)%1; K=np.eye(3)*B
    for i,j in PAIRS:
        K[i,j]=K[j,i]=C0+LAM*phi(x[i]-x[j])/T[i,j]-v*MM[i,j]
    return K


def eq(reg,s,x,v):
    K=Kmat(reg,s,x,v); D=inv(K); rhs=D@(np.ones(3)*A)
    p=solve(D+np.diag(np.diag(D)),rhs); q=D@(np.ones(3)*A-p)
    assert np.min(p)>0 and np.min(q)>0
    return p,q,K


def profits(reg,s,x,v,gamma):
    p,q,_=eq(reg,s,x,v); d=np.array([delta(x[i],H[i]) for i in range(3)])
    return p*q-.5*gamma*d*d


def welfare(reg,s,x,v,gamma):
    p,q,K=eq(reg,s,x,v); cs=.5*float(q@K@q)
    return cs/3+profits(reg,s,x,v,gamma)


def global_location_gap(i,reg,s,x,v,gamma):
    x=np.asarray(x,float).copy(); cur=float(profits(reg,s,x,v,gamma)[i])
    def payoff(z):
        xx=x.copy(); xx[i]=z%1
        return float(profits(reg,s,xx,v,gamma)[i])
    grid=np.linspace(0,1,241,endpoint=False); vals=np.array([payoff(z) for z in grid])
    best=float(vals.max()); step=1/len(grid)
    for k in np.argsort(vals)[-6:]:
        lo=max(0,grid[k]-2*step); hi=min(1,grid[k]+2*step)
        r=minimize_scalar(lambda z:-payoff(z),bounds=(lo,hi),method="bounded")
        best=max(best,-float(r.fun))
    return best-cur


def sw_derivative(d,s1,v,gamma):
    x=np.array([H[0],H[1]+d,H[2]-d]); h=1e-6
    xp=x.copy(); xm=x.copy(); xp[1]+=h; xm[1]-=h
    return float((profits("SW",[s1,SBAR,SBAR],xp,v,gamma)[1]
                  -profits("SW",[s1,SBAR,SBAR],xm,v,gamma)[1])/(2*h))


def sw_location_after_unilateral_depth(s1,v,gamma):
    grid=np.linspace(-.12,.12,181); vals=np.array([sw_derivative(d,s1,v,gamma) for d in grid])
    roots=[]
    for k in range(len(grid)-1):
        if vals[k]==0 or vals[k]*vals[k+1]<0:
            roots.append(brentq(lambda d:sw_derivative(d,s1,v,gamma),grid[k],grid[k+1]))
    assert roots
    stable=[]
    for d in roots:
        x=np.array([H[0],H[1]+d,H[2]-d]); e=1e-4
        f0=profits("SW",[s1,SBAR,SBAR],x,v,gamma)[1]
        xp=x.copy(); xm=x.copy(); xp[1]+=e; xm[1]-=e
        sec=(profits("SW",[s1,SBAR,SBAR],xp,v,gamma)[1]-2*f0
             +profits("SW",[s1,SBAR,SBAR],xm,v,gamma)[1])/e**2
        if sec<0: stable.append((abs(d),d))
    assert stable
    d=min(stable)[1]
    return np.array([H[0],H[1]+d,H[2]-d])


# IS: anchors remain global location best responses throughout the high-stakes policy region.
for v in (0.06,0.08,0.12,0.16):
    for s in (0.0,0.125,SBAR):
        for i in range(3):
            assert global_location_gap(i,"IS",[s],H,v,.03)<3e-6

# SW: when all singleton depths are equal at s_bar, anchors are a global location equilibrium.
for gamma in (.025,.03,.035):
    for i in range(3):
        assert global_location_gap(i,"SW",[SBAR,SBAR,SBAR],H,.08,gamma)<3e-6

# Re-solve the location game after a unilateral SW depth deviation and globally audit representative histories.
for s1 in (0.0,0.125,SBAR):
    x=sw_location_after_unilateral_depth(s1,.08,.03)
    for i in range(3):
        assert global_location_gap(i,"SW",[s1,SBAR,SBAR],x,.08,.03)<3e-6

# Each singleton's global policy best response is the upper boundary once downstream locations are re-solved.
for gamma in (.025,.03,.035):
    grid=np.linspace(0,SBAR,31); vals=[]
    for s1 in grid:
        x=sw_location_after_unilateral_depth(s1,.08,gamma)
        vals.append(float(welfare("SW",[s1,SBAR,SBAR],x,.08,gamma)[0]))
    assert int(np.argmax(vals))==len(grid)-1
    assert vals[-1]>max(vals[:-1])

if __name__=="__main__":
    print("IS whole-circle location audit: PASS")
    print("SW unilateral policy/location audit: PASS")
    print("STAGE 4 POLICY COMPLETION PASS")
