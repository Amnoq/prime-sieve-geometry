"""
Node 11r probe, part 4: Pade-Borel sum of the (alternating, Borel-summable)
RS series around one well, then delta = E_mean(exact) - E_BS.
The RS Borel sum is unambiguous (singularity on negative axis), so delta
is EXACTLY the even-instanton (2,4,6..) non-perturbative piece.
Discriminating: does |delta| scale as exp(-2*S0/hbar) (double traversal)
or exp(-S0/hbar)?
"""
import numpy as np, math
from numpy.linalg import eigh
from scipy.integrate import quad

S0 = 4.0*np.sqrt(2.0)/3.0
OMEGA = np.sqrt(8.0)

def rs_series(hbar, n_orders, n_basis=200):
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
        psik = -(R0*rhs); psik = psik - psik[0]*e0
        E.append(Ek); psi.append(psik)
    return np.array(E)

def emeans(hbar, N=200):
    OM = 2.0
    n = np.arange(N)
    a = np.diag(np.sqrt(n[1:]), 1); ad = a.T
    X = np.sqrt(hbar/(2*OM))*(a+ad)
    P = 1j*np.sqrt(hbar*OM/2)*(ad-a)
    T = ((P@P)/2.0).real
    X2 = X@X
    H = T + (X2-np.eye(N))@(X2-np.eye(N))
    E,_ = eigh(H)
    return E[0], E[1]

def pade_borel(Ers, m=15, nn=15):
    """Borel sum of sum Ers[n]: B(z)=sum Ers[n]/n! z^n, Pade [m/n], Laplace."""
    N = len(Ers)-1
    b = np.array([Ers[n]/math.factorial(n) for n in range(N+1)])
    # Pade [m/nn]: solve for denominator q (q0=1), numerator p
    # sum_{i=0}^{m+nn} b_i z^i = P_m(z)/Q_nn(z)
    L = m+nn
    # Q coeffs q_1..q_nn from: b_{m+1+k} + sum_{j=1..nn} q_j b_{m+1+k-j} = 0
    A = np.zeros((nn, nn)); rhs = np.zeros(nn)
    for k in range(nn):
        for j in range(1, nn+1):
            idx = m+1+k-j
            A[k, j-1] = b[idx] if idx >= 0 else 0.0
        rhs[k] = -b[m+1+k]
    q_rest, *_ = np.linalg.lstsq(A, rhs, rcond=None)
    q = np.concatenate([[1.0], q_rest])
    # P coeffs: p_k = sum_{j=0..min(k,nn)} q_j b_{k-j}
    p = np.zeros(m+1)
    for k in range(m+1):
        p[k] = sum(q[j]*b[k-j] for j in range(min(k,nn)+1))
    # check poles on positive real axis
    roots = np.roots(q[::-1])
    bad = [r for r in roots if abs(r.imag) < 1e-8 and r.real > 0]
    def Pade(z):
        num = sum(p[k]*z**k for k in range(m+1))
        den = sum(q[j]*z**j for j in range(nn+1))
        return num/den
    return Pade, bad

results = {}
for hb in [0.30, 0.25, 0.20]:
    Ers = rs_series(hb, 30, 200)
    e0, e1 = emeans(hb, 220)
    emean = 0.5*(e0+e1)
    for (m, nn) in [(15,15),(14,14),(14,16)]:
        Pade, bad = pade_borel(Ers, m, nn)
        val, err = quad(lambda t: np.exp(-t)*Pade(t), 0, np.inf, limit=200)
        delta = emean - val
        print(f"hbar={hb} [{m}/{nn}]: E_BS={val:.10f} err~{err:.1e} poles+:{len(bad)} "
              f"Emean={emean:.10f} delta={delta:+.4e}")
    results[hb] = delta

print("\n=== delta scaling ===")
hbs = sorted(results)
for hb in hbs:
    print(f"  hbar={hb}: |delta|={abs(results[hb]):.4e}  exp(-2S0/hb)={np.exp(-2*S0/hb):.4e}  ratio={abs(results[hb])/np.exp(-2*S0/hb):.4f}")
# fit log|delta| = -S_eff/hb + c
Y = np.array([np.log(abs(results[hb])) for hb in hbs])
M = np.column_stack([[-1.0/hb for hb in hbs], np.ones(len(hbs))])
coef, *_ = np.linalg.lstsq(M, Y, rcond=None)
print(f"  S_eff={coef[0]:.4f} (2S0={2*S0:.4f}, S0={S0:.4f})")
