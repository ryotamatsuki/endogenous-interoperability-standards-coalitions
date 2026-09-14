"""Stage 7 welfare/generality diagnostics for the repaired C1 revival model.

This is not a new equilibrium-certification artifact. It takes the Stage-4R / repeat-4A
higher-gamma continuation as the economic object and decomposes national welfare,
compares firm-profit and national-welfare rankings, and records finite high-gamma
threshold sensitivity useful for Stage 7 interpretation.
"""
from __future__ import annotations

import math
import numpy as np
from numpy.linalg import inv, solve
from scipy.optimize import brentq, root

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

def cs(reg,s,x,v):
    p,q,K=eq(reg,s,x,v)
    return .5*float(q@K@q)

def welfare(reg,s,x,v,gamma):
    return cs(reg,s,x,v)/3+profit(reg,s,x,v,gamma)

def locfoc(reg,s,x,v,gamma,eps=1e-6):
    x=np.asarray(x,float); out=np.zeros(3)
    for i in range(3):
        xp=x.copy(); xm=x.copy(); xp[i]+=eps; xm[i]-=eps
        out[i]=(profit(reg,s,xp,v,gamma)[i]-profit(reg,s,xm,v,gamma)[i])/(2*eps)
    return out

def near_su(v,gamma,s12=.25,s3=.25):
    ans=root(lambda x:locfoc("SU",[s12,s3],x,v,gamma),H,method="hybr")
    assert ans.success
    return ans.x%1

# Repaired Stage-7 witness.
V=.11; G=.10
X=near_su(V,G)

pi_is=float(profit("IS",[.25],H,V,G)[0])
cs_is=cs("IS",[.25],H,V)/3
w_is=float(welfare("IS",[.25],H,V,G)[0])

pi_full=float(profit("SU",[.25,.25],X,V,G)[0])
cs_full=cs("SU",[.25,.25],X,V)/3
w_full=float(welfare("SU",[.25,.25],X,V,G)[0])

pi_fix=float(profit("SU",[.25,.25],H,V,G)[0])
cs_fix=cs("SU",[.25,.25],H,V)/3
w_fix=float(welfare("SU",[.25,.25],H,V,G)[0])

assert w_full>w_is>w_fix
assert pi_full>pi_is>pi_fix

D_FULL_IS=(pi_full-pi_is, cs_full-cs_is, w_full-w_is)
D_FIX_IS=(pi_fix-pi_is, cs_fix-cs_is, w_fix-w_is)
D_FULL_FIX=(pi_full-pi_fix, cs_full-cs_fix, w_full-w_fix)

# Firm-profit versus national-welfare indifference thresholds in FULL.
def dprofit(v,gamma=G):
    x=near_su(v,gamma)
    return float(profit("SU",[.25,.25],x,v,gamma)[0]-profit("IS",[.25],H,v,gamma)[0])

def dwelfare(v,gamma=G):
    x=near_su(v,gamma)
    return float(welfare("SU",[.25,.25],x,v,gamma)[0]-welfare("IS",[.25],H,v,gamma)[0])

V_PRIVATE=brentq(lambda z:dprofit(z),.07,.14)
V_NATIONAL=brentq(lambda z:dwelfare(z),.07,.14)
assert V_PRIVATE<V_NATIONAL

# Finite higher-gamma sensitivity; numerical interpretation only, not a general theorem.
ROB=[]
for gg in (.08,.10,.12):
    vp=brentq(lambda z:dprofit(z,gg),.07,.14)
    vw=brentq(lambda z:dwelfare(z,gg),.07,.14)
    ROB.append((gg,vp,vw))
    assert 1/15 < vp < vw

if __name__=="__main__":
    print("x_SU =",X)
    print("FULL-IS: dPi, dCS/3, dW =",D_FULL_IS)
    print("FIX-IS: dPi, dCS/3, dW =",D_FIX_IS)
    print("FULL-FIX: dPi, dCS/3, dW =",D_FULL_FIX)
    print("firm-profit threshold =",V_PRIVATE)
    print("national-welfare threshold =",V_NATIONAL)
    print("higher-gamma threshold sensitivity:")
    for row in ROB: print(row)
    print("STAGE 7 WELFARE / GENERALITY DIAGNOSTIC PASS")
