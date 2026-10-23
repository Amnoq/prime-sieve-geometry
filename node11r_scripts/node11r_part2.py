"""
Node 11r probe, part 2: high-order RS to reach the asymptotic regime.
Discriminating number: Borel singularity location A (expect 2*S0=3.771 if
the 0-sector ambiguity lives at the double-traversal scale; S0=1.886 if not).
Also: sign pattern at large n (non-alternating => imaginary ambiguity).
"""
import numpy as np, math

S0 = 4.0*np.sqrt(2.0)/3.0
OMEGA = np.sqrt(8.0)

def rs_series(hbar, n_orders, n_basis):
    w = OMEGA
    c = np.sqrt(hbar/(2.0*w))
    n = np.arange(n_basis)
    a = np.diag(np.sqrt(n[1:]), 1)
    y = c*(a + a.T)
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
        psik = -(R0*rhs)
        psik = psik - psik[0]*e0
        E.append(Ek); psi.append(psik)
    return np.array(E)

for hb, nb, no in [(0.2, 200, 30), (0.3, 200, 26)]:
    Ers = rs_series(hb, no, nb)
    # stability: compare first 12 orders to smaller-basis run
    Ers2 = rs_series(hb, 12, 100)
    stab = np.max(np.abs(Ers[:13]-Ers2)/np.maximum(np.abs(Ers2),1e-300))
    print(f"\n=== hbar={hb}: stability vs smaller basis (rel): {stab:.2e} ===")
    print("  n : E^(n)")
    for n in range(0, min(no+1, 31)):
        print(f"  {n:2d}: {Ers[n]:+.6e}")
    signs = ['+' if e>0 else '-' for e in Ers[1:]]
    print("  signs:", ''.join(signs))
    # fit singularity location on n in [nlo, no]
    for nlo in [14, 18]:
        ns = np.arange(nlo, no+1)
        Y = np.log(np.abs(Ers[ns])) - np.array([math.lgamma(n+1) for n in ns])
        M = np.column_stack([[-float(n) for n in ns],
                             [np.log(float(n)) for n in ns],
                             np.ones(len(ns))])
        coef, *_ = np.linalg.lstsq(M, Y, rcond=None)
        A = np.exp(coef[0])
        print(f"  fit n=[{nlo},{no}]: A={A:.4f} (2S0={2*S0:.4f}, S0={S0:.4f}), power beta={coef[1]:.3f}")
