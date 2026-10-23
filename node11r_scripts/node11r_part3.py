"""
Node 11r probe, part 3: high-precision E_mean(hbar) in HO basis, then
separate the non-analytic piece: E_mean = poly(hbar) + A*exp(-S/hbar).
Discriminating: is the non-analytic scale S = 2*S0 (double traversal)
or S0 (single)? The 1-instanton cancels in the mean, so E_mean should
show ONLY even-traversal non-analyticity.
"""
import numpy as np
from numpy.linalg import eigh

S0 = 4.0*np.sqrt(2.0)/3.0
OM = 2.0  # HO basis frequency

def emeans(hbar, N=160):
    n = np.arange(N)
    a = np.diag(np.sqrt(n[1:]), 1)
    ad = a.T
    X = np.sqrt(hbar/(2*OM))*(a+ad)
    P = 1j*np.sqrt(hbar*OM/2)*(ad-a)
    T = (P @ P)/2.0
    T = T.real
    X2 = X @ X
    V = (X2 - np.eye(N)) @ (X2 - np.eye(N))
    H = T + V
    E, _ = eigh(H)
    return E[0], E[1]

# convergence check
print("=== HO-basis convergence (hbar=0.2) ===")
for N in [100, 140, 180, 220]:
    e0, e1 = emeans(0.2, N)
    print(f"  N={N}: E0={e0:.12f} Emean={(e0+e1)/2:.12f} dE={e1-e0:.6e}")

hbars = [0.30, 0.27, 0.24, 0.21, 0.18, 0.16, 0.14, 0.12]
print("\n=== E_mean vs hbar (N=200) ===")
rows = []
for hb in hbars:
    e0, e1 = emeans(hb, 200)
    em = 0.5*(e0+e1)
    rows.append((hb, em))
    print(f"  hbar={hb:.2f}: Emean={em:.10f} dE={e1-e0:.4e}")
rows = np.array(rows)

# Fit E_mean = poly(hbar, deg K) + A*exp(-S/hbar), try S=2S0 and S=S0
print("\n=== non-analytic scale fit ===")
for S, name in [(2*S0, "2*S0 (double)"), (S0, "S0 (single)")]:
    for K in [3,4,5]:
        hb = rows[:,0]; y = rows[:,1]
        cols = [hb**k for k in range(K+1)] + [np.exp(-S/hb)]
        M = np.vstack(cols).T
        coef, residuals, *_ = np.linalg.lstsq(M, y, rcond=None)
        pred = M@coef
        rms = np.sqrt(np.mean((y-pred)**2))
        A = coef[-1]
        print(f"  S={name}, K={K}: A={A:+.4e}  rms resid={rms:.3e}")

# also: ratio test — residual after polynomial-only fit, does it scale as exp(-2S0/hb)?
print("\n=== polynomial-only residuals vs exp scales ===")
for K in [4,5]:
    hb = rows[:,0]; y = rows[:,1]
    cols = [hb**k for k in range(K+1)]
    M = np.vstack(cols).T
    coef, *_ = np.linalg.lstsq(M, y, rcond=None)
    res = y - M@coef
    # fit log|res| = -S_eff/hb + c
    lr = np.log(np.abs(res))
    M2 = np.column_stack([-1.0/hb, np.ones_like(hb)])
    c2, *_ = np.linalg.lstsq(M2, lr, rcond=None)
    print(f"  K={K}: residual scale S_eff={c2[0]:.4f} (2S0={2*S0:.4f}, S0={S0:.4f})")
    for i in range(len(hb)):
        print(f"     hb={hb[i]:.2f}: resid={res[i]:+.3e}  exp(-2S0/hb)={np.exp(-2*S0/hb[i]):.3e}")
