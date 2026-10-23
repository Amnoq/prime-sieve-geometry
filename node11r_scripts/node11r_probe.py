"""
Node 11r probe: tunneling traversal-sector phase structure.
1D symmetric double well V(x) = (x^2-1)^2, hbar variable, m=1.

Sections:
 A. Exact diagonalization (FD) + convergence checks
 B. Anchor: tunnel splitting vs instanton (exponent + prefactor scaling)
 C. Perturbative series (RS in HO basis at one well): sign pattern + Borel singularity location
 D. Sector observables: E_mean - E_pert^opt (multi-instanton real shift)
 E. Null: single harmonic well (no traversal structure)
"""
import numpy as np
from numpy.linalg import eigh
import json, math

S0 = 4.0*np.sqrt(2.0)/3.0          # instanton action for V=(x^2-1)^2
OMEGA = np.sqrt(8.0)                # small-oscillation frequency at minima
print(f"S0 = {S0:.6f}, 2*S0 = {2*S0:.6f}, omega = {OMEGA:.6f}")

# ---------------- A. FD diagonalization ----------------
def spectrum(hbar, L=4.0, N=801):
    x = np.linspace(-L, L, N); dx = x[1]-x[0]
    main = np.full(N, hbar**2/dx**2)
    off  = np.full(N-1, -hbar**2/(2*dx**2))
    H = np.diag(main) + np.diag(off,1) + np.diag(off,-1) + np.diag((x**2-1.0)**2)
    E, U = eigh(H)
    return E, U, x

def convergence(hbar):
    out = {}
    for (L,N) in [(4.0,401),(4.0,801),(5.0,801),(4.0,1201)]:
        E,_,_ = spectrum(hbar,L,N)
        out[(L,N)] = (E[0], E[1]-E[0])
    return out

print("\n=== A. convergence (hbar=0.2) ===")
for k,v in convergence(0.2).items():
    print(f"  L,N={k}: E0={v[0]:.10f}  dE={v[1]:.6e}")

# ---------------- B. splitting vs hbar (exponent anchor) ----------------
hbars = [0.30, 0.25, 0.20, 0.15]
data = {}
print("\n=== B. tunnel splitting ===")
for hb in hbars:
    E,_,_ = spectrum(hb, 4.0, 801)
    dE = E[1]-E[0]
    data[hb] = dict(E0=E[0], E1=E[1], dE=dE)
    print(f"  hbar={hb}: E0={E[0]:.8f} E1={E[1]:.8f} dE={dE:.6e}  dE*e^(S0/hb)={dE*np.exp(S0/hb):.6f}")

# fit log(dE) = -S0_fit/hb + a*log(hb) + b  (linear least squares in [1/hb, log hb, 1])
Y = np.array([np.log(data[hb]['dE']) for hb in hbars])
M = np.column_stack([[-1.0/hb for hb in hbars],[np.log(hb) for hb in hbars],np.ones(len(hbars))])
coef, res, *_ = np.linalg.lstsq(M, Y, rcond=None)
print(f"  fit: S0_fit={coef[0]:.6f} (exact {S0:.6f}), hbar-power={coef[1]:.4f} (1-loop predicts +0.5)")

# ---------------- C. RS perturbation theory around one well ----------------
def rs_series(hbar, n_orders=12, n_basis=90):
    # H0 = -hb^2/2 d^2 + 4(x-1)^2 ; y=x-1 ; V1 = y^4+4y^3
    w = OMEGA
    c = np.sqrt(hbar/(2.0*w))
    n = np.arange(n_basis)
    a = np.diag(np.sqrt(n[1:]), 1)          # raising
    ad = a.T                                 # lowering
    y = c*(a+ad)
    y2 = y@y; y3 = y2@y; y4 = y2@y2
    V1 = y4 + 4.0*y3
    E0h = hbar*w/2.0
    En = hbar*w*(n+0.5)
    R0 = np.zeros(n_basis); R0[1:] = 1.0/(E0h-En[1:])
    e0 = np.zeros(n_basis); e0[0]=1.0
    E = [E0h]; psi=[e0]
    for k in range(1, n_orders+1):
        Ek = float(e0 @ V1 @ psi[k-1])
        rhs = -V1@psi[k-1]
        for j in range(1,k):
            rhs = rhs + E[j]*psi[k-j]
        psik = -(R0[:,None]*rhs.T).T if False else -(R0*rhs)
        # enforce intermediate normalization <0|psi_k>=0
        psik = psik - psik[0]*e0
        E.append(Ek); psi.append(psik)
    return np.array(E)

print("\n=== C. RS perturbative series (hbar=0.2) ===")
hb = 0.2
Ers = rs_series(hb, 14, 100)
for n in range(min(13,len(Ers))):
    print(f"  E^({n}) = {Ers[n]:+.8e}")
# sign pattern + singularity location from large orders
ns = np.arange(4,13)
logs = np.log(np.abs(Ers[4:13]))
# fit log|E_n| = log(n!) - n*log(A) + b*log(n) + c
M2 = np.column_stack([[-float(n) for n in ns],
                      [np.log(float(n)) for n in ns],
                      np.ones(len(ns))])
Y2 = logs - np.array([math.lgamma(n+1) for n in ns])
c2, *_ = np.linalg.lstsq(M2, Y2, rcond=None)
A_fit = np.exp(c2[0])
print(f"  signs n>=1: {[ '+' if e>0 else '-' for e in Ers[1:13]]}")
print(f"  Borel singularity A_fit={A_fit:.4f}  (2*S0={2*S0:.4f}, S0={S0:.4f})")
# optimal truncation vs exact mean
Emean_exact = 0.5*(data[hb]['E0']+data[hb]['E1'])
terms = np.abs(Ers[1:])
nopt = int(np.argmin(terms[:12]))+1
Eopt = float(np.sum(Ers[:nopt+1]))
diff = Emean_exact - Eopt
print(f"  optimal truncation N_opt={nopt}, E_pert^opt={Eopt:.10f}")
print(f"  E_mean(exact)={Emean_exact:.10f}")
print(f"  E_mean - E_pert^opt = {diff:+.6e}   (2-inst scale e^(-2S0/hb)={np.exp(-2*S0/hb):.3e})")

# ---------------- D. multi-instanton shift across hbar ----------------
print("\n=== D. E_mean - E_pert^opt across hbar ===")
for hb in hbars:
    Ers_h = rs_series(hb, 12, 90)
    terms_h = np.abs(Ers_h[1:])
    nopt_h = int(np.argmin(terms_h[:11]))+1
    Eopt_h = float(np.sum(Ers_h[:nopt_h+1]))
    Em = 0.5*(data[hb]['E0']+data[hb]['E1'])
    print(f"  hbar={hb}: shift={Em-Eopt_h:+.6e}  e^(-2S0/hb)={np.exp(-2*S0/hb):.3e}  ratio={(Em-Eopt_h)/np.exp(-2*S0/hb):+.3f}")

# ---------------- E. null: single well ----------------
print("\n=== E. null: single harmonic well V=4(x-1)^2 ===")
def single_well(hbar, L=6.0, N=801):
    x = np.linspace(-L, L, N); dx=x[1]-x[0]
    main=np.full(N,hbar**2/dx**2); off=np.full(N-1,-hbar**2/(2*dx**2))
    H=np.diag(main)+np.diag(off,1)+np.diag(off,-1)+np.diag(4.0*(x-1.0)**2)
    E,_=eigh(H); return E
for hb in [0.2,0.15]:
    E=single_well(hb)
    print(f"  hbar={hb}: E0={E[0]:.8f} (exact {hb*OMEGA/2:.8f}), E1-E0={E[1]-E[0]:.8f} (exact {hb*OMEGA:.8f}) -> no exponential splitting")

json.dump({str(k):v for k,v in data.items()}, open('/tmp/node11r_anchors.json','w'))
print("\nanchors saved to /tmp/node11r_anchors.json")
