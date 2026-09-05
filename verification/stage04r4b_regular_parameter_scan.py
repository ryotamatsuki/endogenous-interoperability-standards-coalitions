"""Stage 4R4B hostile regular-parameter scan.

Diagnostic only, not a theorem. The scan is pre-specified around the affine
regularity region and asks whether the SU member-bloc welfare is decreasing on
s_12 in {0,1/16,1/8,3/16,1/4} when outsider depth is maximal.

It covers beta in {0.05,0.10,0.20,0.30}, v in {0.002,0.01,0.02,0.04}, and
gamma in {0.05,0.20,1.00}, retaining only cells satisfying the Stage 4R4A
global inequalities. The canonical model is one of the retained cells.
"""
from __future__ import annotations

import math
import numpy as np
from scipy.optimize import brentq, minimize_scalar

T=1.0
SB=0.25
A=1.0
H0=np.array([1/6,1/2,5/6],dtype=float)


def regular(beta,v):
    m_min=1/(3+T+SB)
    m_max=1/(1+T-SB)
    k_min=beta*m_min-v
    k_max=beta*m_max
    return v>0 and v<beta*m_min and 2*k_max<1 and k_min>k_max**2


def continuation(beta,v,gamma,sm,so,y):
    x=(H0+np.asarray(y,dtype=float))%1.0
    tau={(0,1):T-sm,(0,2):T+(sm+so)/2,(1,2):T+(sm+so)/2}
    K=np.eye(3)
    for i,j in ((0,1),(0,2),(1,2)):
        delta=1-math.cos(2*math.pi*(x[i]-x[j]))
        gij=1.0 if (i,j)==(0,1) else 0.0
        K[i,j]=K[j,i]=beta/(1+tau[(i,j)]+delta)-v*gij
    H=np.linalg.inv(K); D=np.diag(np.diag(H))
    p=np.linalg.solve(D+H,H@(A*np.ones(3)))
    q=H@(A*np.ones(3)-p)
    prof=p*q-gamma*np.asarray(y,dtype=float)**2/2
    cs=.5*float(q@K@q)
    return prof+cs/3,prof


def grad0(beta,v,gamma,sm,so,d,eps=2e-6):
    yp=np.array([-d,d,0.0]); ym=yp.copy()
    yp[0]+=eps; ym[0]-=eps
    return (continuation(beta,v,gamma,sm,so,yp)[1][0]-continuation(beta,v,gamma,sm,so,ym)[1][0])/(2*eps)


def loc(beta,v,gamma,sm,so):
    grid=np.linspace(0,.08,41)
    vals=[grad0(beta,v,gamma,sm,so,float(d)) for d in grid]
    roots=[]
    for l,r,fl,fr in zip(grid[:-1],grid[1:],vals[:-1],vals[1:]):
        if fl*fr<0:
            roots.append(brentq(lambda d:grad0(beta,v,gamma,sm,so,d),float(l),float(r)))
    if not roots:
        raise AssertionError((beta,v,gamma,sm,so,'no root'))
    for d in roots:
        y=np.array([-d,d,0.0])
        errs=[]
        for i in range(3):
            def obj(z):
                yy=y.copy(); yy[i]=z
                return -continuation(beta,v,gamma,sm,so,yy)[1][i]
            rr=minimize_scalar(obj,bounds=(-.5,.5),method='bounded',options={'xatol':1e-9})
            errs.append(abs(rr.x-y[i]))
        if max(errs)<5e-6:
            return y
    raise AssertionError((beta,v,gamma,sm,so,'BR failure'))


betas=[.05,.10,.20,.30]
vs=[.002,.01,.02,.04]
gammas=[.05,.20,1.00]
sgrid=[0,.0625,.125,.1875,.25]
rows=[]
for beta in betas:
    for v in vs:
        if not regular(beta,v):
            continue
        for gamma in gammas:
            vals=[]
            for sm in sgrid:
                y=loc(beta,v,gamma,sm,SB)
                W,_=continuation(beta,v,gamma,sm,SB,y)
                vals.append(float(W[0]+W[1]))
            decreasing=all(vals[k]>vals[k+1] for k in range(len(vals)-1))
            rows.append((beta,v,gamma,decreasing,vals[0]-vals[-1]))

assert len(rows)==36
assert all(row[3] for row in rows)
assert all(row[4]>0 for row in rows)

if __name__=='__main__':
    print('regular cells audited:',len(rows))
    print('all member-welfare depth grids strictly decreasing:',all(r[3] for r in rows))
    print('minimum endpoint welfare loss:',min(r[4] for r in rows))
    print('maximum endpoint welfare loss:',max(r[4] for r in rows))
    print('STAGE 4R4B DIAGNOSTIC: no positive SU member-depth region found in the pre-specified regular grid')
