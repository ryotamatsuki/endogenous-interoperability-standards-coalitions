"""Efficient CI regression for Stage 4R4A.

The detailed architecture record and slow forensic verifier live in
stage04r4a_affine_bertrand_gate.py.  This CI version checks the same binding
objects with deterministic coarse-to-local global searches so every PR does
not spend excessive Actions minutes.
"""
from __future__ import annotations
import itertools, math
import numpy as np
from numpy.linalg import eigvalsh, inv, solve
from scipy.optimize import minimize_scalar

A=2.0; B=10.0; C0=.30; LAM=.50; V=.08; GAMMA=.03; TBAR=1.0; SBAR=.25
H=np.array([1/6,1/2,5/6],float)
PAIRS=((0,1),(0,2),(1,2))

def G(reg):
    if reg=="IS": return np.ones((3,3))
    if reg=="SW": return np.eye(3)
    if reg=="SU": return np.array([[1,1,0],[1,1,0],[0,0,1]],float)
    raise ValueError(reg)

def Tau(reg,s):
    s=np.atleast_1d(np.asarray(s,float)); T=np.zeros((3,3))
    if reg=="IS": vals={(0,1):1-s[0],(0,2):1-s[0],(1,2):1-s[0]}
    elif reg=="SU": vals={(0,1):1-s[0],(0,2):1+(s[0]+s[1])/2,(1,2):1+(s[0]+s[1])/2}
    else: vals={(0,1):1+(s[0]+s[1])/2,(0,2):1+(s[0]+s[2])/2,(1,2):1+(s[1]+s[2])/2}
    for (i,j),z in vals.items(): T[i,j]=T[j,i]=z
    return T

def phi(z): return .5*(1+math.cos(2*math.pi*z))
def delta(z,h): return ((z-h+.5)%1)-.5

def Kmat(reg,s,x,v=V):
    T=Tau(reg,s); GG=G(reg); x=np.mod(np.asarray(x,float),1); K=np.eye(3)*B
    for i,j in PAIRS:
        K[i,j]=K[j,i]=C0+LAM*phi(x[i]-x[j])/T[i,j]-v*GG[i,j]
    return K

# Uniform Stage-4 domain inequalities.
cmin=C0-V; cmax=C0+LAM/(TBAR-SBAR)
assert cmin>0 and B>2*cmax and B*cmin>cmax*cmax and B-2*cmax+cmin>0

def eq(reg,s,x,v=V):
    K=Kmat(reg,s,x,v); D=inv(K); r=D@(np.ones(3)*A)
    p=solve(D+np.diag(np.diag(D)),r); q=D@(np.ones(3)*A-p)
    return p,q,K,D

def qkkt(reg,s,x,p,v=V):
    K=Kmat(reg,s,x,v); r=np.ones(3)*A-np.asarray(p,float); good=[]
    for mask in range(8):
        S=[i for i in range(3) if mask&(1<<i)]; q=np.zeros(3)
        if S:
            qS=solve(K[np.ix_(S,S)],r[S]); q[S]=qS
            if np.any(qS < -1e-9): continue
        grad=K@q-r; I=[i for i in range(3) if i not in S]
        if I and np.any(grad[I] < -1e-9): continue
        if S and np.max(np.abs(grad[S]))>1e-7: continue
        good.append((.5*q@K@q-r@q,q))
    assert good
    return min(good,key=lambda z:z[0])[1]

def op(i,reg,s,x,p,v=V):
    q=qkkt(reg,s,x,p,v); return p[i]*q[i]

def price_gap(i,reg,s,x,p,v=V):
    cur=op(i,reg,s,x,p,v); grid=np.linspace(0,A+2,101)
    vals=[]
    for z in grid:
        pp=p.copy(); pp[i]=z; vals.append(op(i,reg,s,x,pp,v))
    k=int(np.argmax(vals)); lo=max(0,grid[k]-.08); hi=min(A+2,grid[k]+.08)
    def f(z):
        pp=p.copy(); pp[i]=z; return -op(i,reg,s,x,pp,v)
    r=minimize_scalar(f,bounds=(lo,hi),method="bounded",options={"xatol":1e-10})
    return max(max(vals),-r.fun)-cur

# Matrix signs and direct price-deviation checks at adversarial histories.
for reg,s,x in [
    ("IS",[SBAR],H),("SU",[SBAR,0],H),
    ("IS",[SBAR],[.4,.5,5/6]),("SU",[SBAR,0],[.4,.5,5/6]),
    ("SW",[0,0,0],[.2,.2,.8])]:
    p,q,K,D=eq(reg,s,x)
    assert eigvalsh(K).min()>B-2*cmax-1e-9
    off=D-np.diag(np.diag(D)); assert np.max(off)<=1e-12
    assert np.min(D@np.ones(3))>0 and np.min(p)>0 and np.min(q)>0
    for i in range(3): assert price_gap(i,reg,s,np.asarray(x,float),p)<3e-7

def profits(reg,s,x,v=V,gamma=GAMMA):
    p,q,_,_=eq(reg,s,x,v); d=np.array([delta(x[i],H[i]) for i in range(3)])
    return p*q-.5*gamma*d*d

def br(i,reg,s,x,v=V,gamma=GAMMA):
    x=np.asarray(x,float).copy(); grid=np.linspace(0,1,91,endpoint=False)
    def f(z):
        xx=x.copy(); xx[i]=z%1; return -profits(reg,s,xx,v,gamma)[i]
    vals=np.array([f(z) for z in grid]); step=1/91; best=(grid[np.argmin(vals)],vals.min())
    for k in np.argsort(vals)[:4]:
        c=grid[k]; lo=max(0,c-2*step); hi=min(1,c+2*step)
        r=minimize_scalar(f,bounds=(lo,hi),method="bounded",options={"xatol":1e-10})
        if r.fun<best[1]: best=(r.x%1,r.fun)
    return best[0],-best[1]

def loc(reg,s,v=V,gamma=GAMMA):
    x=H.copy()
    for _ in range(45):
        old=x.copy()
        for i in range(3): x[i]=br(i,reg,s,x,v,gamma)[0]
        if np.max(np.abs(x-old))<2e-8: break
    cur=profits(reg,s,x,v,gamma); gaps=[]
    for i in range(3): gaps.append(br(i,reg,s,x,v,gamma)[1]-cur[i])
    return x,np.asarray(gaps)

def welfare(reg,s,x,v=V,gamma=GAMMA):
    p,q,K,_=eq(reg,s,x,v); cs=.5*q@K@q; return cs/3+profits(reg,s,x,v,gamma)

ix,ig=loc("IS",[SBAR]); sx,sg=loc("SU",[SBAR,0]); wx,wg=loc("SW",[0,0,0])
assert np.max(np.abs(ix-H))<3e-4 and np.max(np.abs(wx-H))<3e-4
assert sx[0]<H[0]-.02 and sx[1]>H[1]+.02 and abs(sx[2]-H[2])<3e-4
assert max(ig.max(),sg.max(),wg.max())<2e-6
fixed=welfare("SU",[SBAR,0],H)[0]-welfare("IS",[SBAR],H)[0]
full=welfare("SU",[SBAR,0],sx)[0]-welfare("IS",[SBAR],ix)[0]
assert fixed<-1e-4 and full>1e-4

robust=0
for vv,gg in itertools.product((.07,.08,.09),(.025,.03,.035)):
    ixx,igg=loc("IS",[SBAR],vv,gg); sxx,sgg=loc("SU",[SBAR,0],vv,gg)
    dt=welfare("SU",[SBAR,0],H,vv,gg)[0]-welfare("IS",[SBAR],H,vv,gg)[0]
    df=welfare("SU",[SBAR,0],sxx,vv,gg)[0]-welfare("IS",[SBAR],ixx,vv,gg)[0]
    if dt<0 and df>0 and sxx[0]<H[0]-.02 and sxx[1]>H[1]+.02 and max(igg.max(),sgg.max())<3e-6: robust+=1
assert robust==9

if __name__=="__main__":
    print("IS x",ix,"SU x",sx,"SW x",wx)
    print("member SU-IS fixed",fixed,"endogenous",full)
    print("local reversal robustness",robust,"/ 9")
    print("STAGE 4R4A CI PASS")
