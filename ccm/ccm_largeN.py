"""
Large-N push for CCM: measure convergence law and even/odd separation.
Runs c=13 at N=40, 60 (and 80/120 if feasible), tracking:
- eps_N (ground state)
- even/odd separation ratio
- zero 1..k errors
"""
import sys, time, math
from mpmath import mp

def run_N(lam2=13.0, N=40, dps=120):
    mp.dps = dps
    from ccm_reimpl import build_M, prime_weights, W02, WR_entry, Wp_entry
    from ccm_reimpl import alpha_L, beta_L, Ie_L, q_nm
    t0 = time.time()
    lam = mp.sqrt(lam2)
    L = 2*mp.log(lam)
    idx = list(range(-N, N+1))
    n = len(idx)
    print(f"N={N}: building matrix ({n}x{n})...", flush=True)

    a = {nn: alpha_L(nn, L) for nn in idx}
    b = {nn: beta_L(nn, L) for nn in idx}
    ie = {nn: Ie_L(nn, L) for nn in idx}
    abg = (a, b, ie)
    pw = prime_weights(lam)

    M = mp.matrix(n)
    for ii, n_ in enumerate(idx):
        for jj, m_ in enumerate(idx):
            if jj < ii: continue
            v = W02(n_, m_, L) - WR_entry(n_, m_, L, abg) - Wp_entry(n_, m_, L, pw)
            M[ii, jj] = v; M[jj, ii] = v
    t1 = time.time()
    print(f"  matrix built in {t1-t0:.0f}s", flush=True)

    # FULL spectrum (not just even) to get even/odd separation
    # Use mp.eig for the full matrix? That's slow. Instead:
    # even block and odd block separately
    # Even block (dim N+1)
    Me = mp.matrix(N+1)
    for aa in range(N+1):
        for bb in range(aa, N+1):
            if aa == 0 and bb == 0: v = M[N, N]
            elif aa == 0: v = (M[N, N+bb] + M[N, N-bb])/mp.sqrt(2)
            elif bb == 0: v = (M[N+aa, N] + M[N-aa, N])/mp.sqrt(2)
            else: v = (M[N+aa,N+bb]+M[N+aa,N-bb]+M[N-aa,N+bb]+M[N-aa,N-bb])/2
            Me[aa,bb]=v; Me[bb,aa]=v
    # Odd block (dim N)
    Mo = mp.matrix(N)
    for aa in range(1, N+1):
        for bb in range(aa, N+1):
            v = (M[N+aa,N+bb]-M[N+aa,N-bb]-M[N-aa,N+bb]+M[N-aa,N-bb])/2
            Mo[aa-1,bb-1]=v; Mo[bb-1,aa-1]=v

    # smallest eigenvalue of each via inverse iteration
    def ground(A):
        Ainv = mp.inverse(A)
        x = mp.matrix([mp.mpf(1)]*A.rows); x = x/mp.norm(x)
        for it in range(60):
            y = Ainv*x; x = y/mp.norm(y)
        return (x.T*(A*x))[0], x

    eps_e, xe = ground(Me)
    eps_o, xo = ground(Mo)
    print(f"  eps_even = {float(eps_e):.3e}", flush=True)
    print(f"  eps_odd  = {float(eps_o):.3e}", flush=True)
    print(f"  separation ratio = {float(eps_o/eps_e):.1f}x", flush=True)
    t2 = time.time()
    print(f"  eigensolve in {t2-t1:.0f}s", flush=True)

    # zero extraction from even ground state
    xi = mp.matrix([mp.mpf(0)]*n)
    xi[N] = xe[0]
    for k in range(1, N+1):
        xi[N+k] = xe[k]/mp.sqrt(2); xi[N-k] = xe[k]/mp.sqrt(2)
    s = mp.fsum(xi[j] for j in range(n)); xi = xi/s
    Lf = float(L); xif = [float(xi[j]) for j in range(n)]
    ajs = [2*math.pi*(j-N)/Lf for j in range(n)]
    def xihat(z):
        tot = 0.0
        for c_, aj_ in zip(xif, ajs):
            d = z - aj_
            tot += c_/d if abs(d) > 1e-12 else 0.0
        return 2/math.sqrt(Lf)*math.sin(z*Lf/2)*tot
    import numpy as np
    poles = sorted([a for a in ajs if 0 < a < 60])
    bounds = [0.5] + poles + [60.0]
    roots = []
    for lo, hi in zip(bounds[:-1], bounds[1:]):
        if hi-lo < 1e-6 or len(roots) >= 10: continue
        zs = np.linspace(lo+1e-9, hi-1e-9, max(30, int((hi-lo)*10)))
        vals = [xihat(z) for z in zs]
        for i in range(len(zs)-1):
            if vals[i]*vals[i+1] < 0:
                a_, b_ = zs[i], zs[i+1]
                for _ in range(60):
                    m_ = 0.5*(a_+b_)
                    if xihat(a_)*xihat(m_) <= 0: b_ = m_
                    else: a_ = m_
                roots.append(0.5*(a_+b_)); break
    true = [14.1347251417, 21.0220396388, 25.0108575801, 30.4248761259,
            32.9350615877, 37.5861781588, 40.9187190121, 43.3270732809,
            48.0051508812, 49.7738324777]
    print(f"  roots found: {len(roots)}", flush=True)
    for i, (r, t) in enumerate(zip(roots, true)):
        print(f"    zero {i+1}: err {abs(r-t):.2e}", flush=True)
    print(f"  total time: {time.time()-t0:.0f}s", flush=True)

if __name__ == '__main__':
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 40
    dps = int(sys.argv[2]) if len(sys.argv) > 2 else 120
    run_N(N=N, dps=dps)
