"""Supplemental Stage 4R4B check for the FULL SW policy game.

For the frozen affine-demand witness, re-solve the three-firm repositioning game
for each unilateral singleton-depth deviation s_1 while s_2=s_3=s_bar. Verify
that the symmetric SW candidate s_i=s_bar is a policy best response and that
repositioning responses to asymmetric depth do not overturn the comparison
with IS.
"""
from __future__ import annotations

import math
import numpy as np
from scipy.optimize import minimize_scalar, root

T=1.0
SB=0.25
BETA=0.2
V=0.02
A=1.0
GAMMA=0.2
H0=np.array([1/6,1/2,5/6],dtype=float)


def continuation(s,y):
    x=(H0+np.asarray(y,dtype=float))%1.0
    K=np.eye(3)
    for i in range(3):
        for j in range(i+1,3):
            tau=T+(s[i]+s[j])/2
            delta=1-math.cos(2*math.pi*(x[i]-x[j]))
            K[i,j]=K[j,i]=BETA/(1+tau+delta)
    H=np.linalg.inv(K)
    D=np.diag(np.diag(H))
    p=np.linalg.solve(D+H,H@(A*np.ones(3)))
    q=H@(A*np.ones(3)-p)
    profit=p*q-GAMMA*np.asarray(y,dtype=float)**2/2
    cs=.5*float(q@K@q)
    W=profit+cs/3
    return W,profit


def grad_profit(y,s,eps=1e-6):
    out=[]
    for i in range(3):
        yp=np.array(y,float); ym=np.array(y,float)
        yp[i]+=eps; ym[i]-=eps
        out.append((continuation(s,yp)[1][i]-continuation(s,ym)[1][i])/(2*eps))
    return np.array(out)


def location_ne(s,start=None):
    start=np.zeros(3) if start is None else np.asarray(start,dtype=float)
    sol=root(lambda y: grad_profit(y,s),start,method='hybr',options={'xtol':1e-10})
    y=sol.x
    # Do not infer equilibrium from root success alone: perform unrestricted
    # one-dimensional global best-response checks on [-1/2,1/2].
    errors=[]
    for i in range(3):
        def obj(z):
            yy=y.copy(); yy[i]=z
            return -continuation(s,yy)[1][i]
        r=minimize_scalar(obj,bounds=(-.5,.5),method='bounded',options={'xatol':1e-11})
        errors.append(abs(r.x-y[i]))
    if max(errors)>3e-6:
        raise AssertionError((s,y,errors,sol.success))
    return y,continuation(s,y)[0]


grid=np.linspace(0,SB,7)
w0=[]
locs=[]
start=np.zeros(3)
for s0 in grid:
    y,W=location_ne((float(s0),SB,SB),start)
    start=y
    w0.append(float(W[0]))
    locs.append(y)
assert all(w0[i] < w0[i+1] for i in range(len(w0)-1))

# At symmetric maximum depths, rotational symmetry gives the anchor profile;
# the global BR audit above confirms it as the location equilibrium.
y_sw,W_sw=location_ne((SB,SB,SB),np.zeros(3))
assert np.max(np.abs(y_sw))<3e-6

# IS continuation from the Stage 4R4B canonical reconstruction.
# At IS, the policy optimum is s_I=0 and symmetry pins y=0.
def is_welfare():
    g=np.ones((3,3)); np.fill_diagonal(g,0)
    K=np.eye(3)
    for i in range(3):
        for j in range(i+1,3):
            tau=T
            delta=1-math.cos(2*math.pi*(H0[i]-H0[j]))
            K[i,j]=K[j,i]=BETA/(1+tau+delta)-V
    H=np.linalg.inv(K); D=np.diag(np.diag(H))
    p=np.linalg.solve(D+H,H@(A*np.ones(3)))
    q=H@(A*np.ones(3)-p)
    profit=p*q
    cs=.5*float(q@K@q)
    return profit+cs/3

W_is=is_welfare()
assert np.all(W_is > W_sw)

if __name__=='__main__':
    print('SW own-welfare grid with full repositioning:',w0)
    print('SW location responses:',[z.tolist() for z in locs])
    print('SW policy candidate:',(SB,SB,SB))
    print('W_SW FULL:',W_sw.tolist())
    print('W_IS:',W_is.tolist())
    print('FULL SW CHECK PASS: each singleton chooses maximal depth, but all countries still prefer IS')
