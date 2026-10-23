"""
Node 11s — "0" leg: Rayleigh-Schrodinger around the false vacuum.
PT gives a REAL energy to all orders (knows nothing of decay);
the series is asymptotic (factorial growth) -> incomplete/ambiguous.
Light check: reality of coefficients + growth pattern. The Borel
singularity location is recorded as an instrument observation only
(11r's lesson: coupling-expansion Borel is not the hbar-expansion).
"""
import numpy as np, json, math
from scipy.optimize import brentq

def Vp(x, eps): return 4.0*x*(x**2 - 1.0) - eps

def rs_false_vacuum(hb, eps, n_orders=22, n_basis=110):
    xf = brentq(lambda x: Vp(x, eps), -1.6, -0.2)
    wf = np.sqrt(12.0*xf**2 - 4.0)
    Vf = (xf**2-1.0)**2 - eps*xf
    g3 = 4.0*xf          # V'''(xf)/6
    g4 = 1.0             # V''''(xf)/24
    n = np.arange(n_basis)
    c = np.sqrt(hb/(2.0*wf))
    a = np.diag(np.sqrt(n[1:]), 1); ad = a.T
    y = c*(a+ad)
    y2 = y@y; y3 = y2@y; y4 = y2@y2
    V1 = g3*y3 + g4*y4
    E0h = hb*wf/2.0
    En = hb*wf*(n+0.5)
    R0 = np.zeros(n_basis); R0[1:] = 1.0/(E0h-En[1:])
    e0 = np.zeros(n_basis); e0[0] = 1.0
    E = [E0h]; psi = [e0]
    for k in range(1, n_orders+1):
        Ek = float(e0 @ V1 @ psi[k-1])
        rhs = -V1@psi[k-1]
        for j in range(1, k):
            rhs = rhs + E[j]*psi[k-j]
        psik = -(R0*rhs)
        psik = psik - psik[0]*e0
        E.append(Ek); psi.append(psik)
    return np.array(E), dict(xf=xf, wf=wf, Vf=Vf)

if __name__ == "__main__":
    hb, eps = 0.3, 0.2
    E, info = rs_false_vacuum(hb, eps)
    print(f"false vacuum: xf={info['xf']:.6f} Vf={info['Vf']:.6f}")
    print("RS coefficients (all must be REAL -> PT knows nothing of decay):")
    for n in range(min(12, len(E))):
        print(f"  E^({n}) = {E[n]:+.8e}")
    # growth pattern
    terms = np.abs(E[1:])
    print(f"min |term| at order {int(np.argmin(terms))+1}; "
          f"|E_20|/|E_10| = {terms[19]/terms[9]:.2e} (factorial growth?)")
    # optimal truncation energy (real)
    nopt = int(np.argmin(terms[:20]))+1
    Eopt = float(np.sum(E[:nopt+1])) + info["Vf"]
    print(f"optimal truncation: N_opt={nopt}, E_pert^opt={Eopt:.10f} (REAL)")
    json.dump(dict(E_real=E.tolist(), Eopt=Eopt, nopt=nopt),
              open("/tmp/node11s_rs.json","w"))
