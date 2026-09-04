"""Stage 7 welfare/generality verification for C-ESD.

Imports the frozen Stage-4 model and verifies:
- exact transfer cancellation in global welfare;
- member welfare decomposition into CS and domestic profit;
- global-welfare ranking at the canonical witness;
- constrained social-location benchmark;
- the upper adjustment-cost threshold gamma_W on the regular branch.
"""
from __future__ import annotations
import importlib.util
from pathlib import Path
import numpy as np
from scipy.optimize import differential_evolution, brentq

HERE=Path(__file__).resolve().parent
P=HERE/'stage04_cesd_minimal.py'
spec=importlib.util.spec_from_file_location('s4',P)
s4=importlib.util.module_from_spec(spec); spec.loader.exec_module(s4)

H=s4.H

def decompose(reg,s,vv,gamma,full=True):
    x=s4.loc_nash(reg,s,vv,gamma,full)
    eq=s4.ordered_eq(x,reg,s,vv)
    q,p,T,N,arcs=eq
    cs=0.0; tc=0.0; nv=0.0; payments=0.0
    for i,j,ell in arcs:
        y=ell/2+(p[j]-p[i]+vv*(N[i]-N[j]))/(2*T[i,j])
        z=ell-y
        cs+=(-p[i]+vv*N[i])*y-T[i,j]*y*y/2
        cs+=(-p[j]+vv*N[j])*z-T[i,j]*z*z/2
        tc+=T[i,j]*(y*y+z*z)/2
        nv+=vv*(N[i]*y+N[j]*z)
        payments+=p[i]*y+p[j]*z
    redesign=.5*gamma*(x-H)**2
    op=p*q
    pi=op-redesign
    W=cs/3+pi
    GW=cs+pi.sum()
    return dict(x=x,q=q,p=p,cs=cs,tc=tc,nv=nv,payments=payments,
                redesign=redesign,op=op,pi=pi,W=W,GW=GW)

def su_policy_components(vv,gamma,sbar,full=True):
    s,out=s4.su_policy(vv,gamma,sbar,full)
    return s,decompose('SU',s,vv,gamma,full)

V=.04; GAMMA=.11; SBAR=.25
IS=decompose('IS',[SBAR],V,GAMMA,True)
sSU,SU=su_policy_components(V,GAMMA,SBAR,True)
SW=decompose('SW',[0,0,0],V,GAMMA,True)

# Exact transfer cancellation: operating revenue equals consumer payments.
for Z in (IS,SU,SW):
    assert abs(Z['payments']-Z['op'].sum()) < 1e-10
    assert abs(Z['GW']-(Z['nv']-Z['tc']-Z['redesign'].sum())) < 1e-10

# National-member decomposition.
dCS=(SU['cs']-IS['cs'])/3
dPI=SU['pi'][0]-IS['pi'][0]
dW=SU['W'][0]-IS['W'][0]
assert abs(dW-(dCS+dPI)) < 1e-10
assert dCS < 0 < dPI
assert dW > 0

# Global welfare ranks IS above SU at the witness.
assert IS['GW'] > SU['GW'] > SW['GW']

# Constrained social location benchmark for fixed SU policy profile.
def global_welfare_at_x(x,reg,s,vv,gamma):
    eq=s4.ordered_eq(np.asarray(x,float),reg,s,vv)
    if eq is None: return None
    q,p,T,N,arcs=eq
    cs=0.0
    for i,j,ell in arcs:
        y=ell/2+(p[j]-p[i]+vv*(N[i]-N[j]))/(2*T[i,j])
        z=ell-y
        cs+=(-p[i]+vv*N[i])*y-T[i,j]*y*y/2
        cs+=(-p[j]+vv*N[j])*z-T[i,j]*z*z/2
    redesign=.5*gamma*(np.asarray(x)-H)**2
    return cs+(p*q-redesign).sum()

def social_x(reg,s,vv,gamma):
    def obj(z):
        x=np.asarray(z,float)
        if not (0<x[0]<x[1]<x[2]<1): return 1e3
        w=global_welfare_at_x(x,reg,s,vv,gamma)
        return 1e3 if w is None else -w
    r=differential_evolution(obj,[(.001,.32),(.34,.66),(.68,.999)],
                             seed=1,popsize=8,maxiter=100,tol=1e-9)
    return r.x,-r.fun

XSP,GWSP=social_x('SU',sSU,V,GAMMA)
Dprivate=SU['x'][1]-SU['x'][0]
Dsocial=XSP[1]-XSP[0]
assert Dprivate > Dsocial > (H[1]-H[0])
assert GWSP > SU['GW']

# Upper welfare threshold on the regular branch.
def delta_member(gamma,vv=.04,sbar=.25):
    s,z=su_policy_components(vv,gamma,sbar,True)
    I=decompose('IS',[sbar],vv,gamma,True)
    return z['W'][0]-I['W'][0]

gamma_W=brentq(lambda g:delta_member(g),.13,.14)
assert abs(gamma_W-0.13298301564) < 1e-6

if __name__=='__main__':
    print('SU policy:',sSU)
    print('member dCS/3, dPi, dW:',dCS,dPI,dW)
    print('global welfare IS/SU/SW:',IS['GW'],SU['GW'],SW['GW'])
    print('private/social SU distances:',Dprivate,Dsocial)
    print('gamma_W:',gamma_W)
