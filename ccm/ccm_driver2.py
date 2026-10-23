"""
Proper high-precision driver for CCM D_log^{(lam,N)}.
- Builds M at high dps.
- Restricts to even subspace (xi_{-j}=xi_j), dim N+1.
- Inverse iteration for smallest eigenpair (Gotcha 4).
- Normalizes delta_N(xi)=1.
- xihat(z) zeros via scan + Newton; compares to known zeta zeros.

Usage: python3 ccm_driver2.py [lam2] [N] [dps]
  lam2 = lam^2 cutoff, e.g. 13 ; N e.g. 30 ; dps e.g. 120
"""
import sys, math
from mpmath import mp

def main():
    lam2 = float(sys.argv[1]) if len(sys.argv) > 1 else 13.0
    N = int(sys.argv[2]) if len(sys.argv) > 2 else 30
    dps = int(sys.argv[3]) if len(sys.argv) > 3 else 120
    mp.dps = dps
    from ccm_reimpl import build_M
    lam = mp.sqrt(lam2)
    print(f"lam^2={lam2} N={N} dps={dps}", flush=True)
    M, L, idx = build_M(lam, N, verbose=True)
    n = len(idx)
    # even subspace: basis e0=V0, e_k=(V_k+V_{-k})/sqrt2
    # Me[a,b] for a,b in 0..N
    Me = mp.matrix(N+1)
    for a in range(N+1):
        for b in range(a, N+1):
            if a == 0 and b == 0:
                v = M[N, N]
            elif a == 0:
                v = (M[N, N+b] + M[N, N-b]) / mp.sqrt(2)
            elif b == 0:
                v = (M[N+a, N] + M[N-a, N]) / mp.sqrt(2)
            else:
                v = (M[N+a, N+b] + M[N+a, N-b] + M[N-a, N+b] + M[N-a, N-b]) / 2
            Me[a, b] = v
            Me[b, a] = v
    print(f"even block built, dim={N+1}", flush=True)
    # inverse iteration for smallest eigenpair
    Minv = mp.inverse(Me)
    x = mp.matrix([mp.mpf(1)]*(N+1))
    x = x / mp.norm(x)
    lam_old = mp.mpf('0')
    for it in range(50):
        y = Minv * x
        nrm = mp.norm(y)
        x = y / nrm
        # Rayleigh quotient
        Mx = Me * x
        rq = (x.T * Mx)[0]
        if it > 3 and abs((rq - lam_old) / rq) < mp.mpf(10)**(-(dps//3)):
            break
        lam_old = rq
    eps = (x.T * (Me * x))[0]
    print(f"inverse iteration: {it+1} iters, eps_N = {eps}", flush=True)
    # residual
    res = mp.norm(Me*x - eps*x)
    print(f"residual |Me x - eps x| = {res}", flush=True)
    # lift to full even vector xi (length 2N+1), xi_{-j}=xi_j
    xi = mp.matrix([mp.mpf(0)]*n)
    xi[N] = x[0]
    for k in range(1, N+1):
        xi[N+k] = x[k] / mp.sqrt(2)
        xi[N-k] = x[k] / mp.sqrt(2)
    # normalize delta_N(xi)=1 : delta_N has unit mode coeffs, so sum(xi_j)=1
    s = mp.fsum(xi[j] for j in range(n))
    xi = xi / s
    print(f"delta_N(xi) check (should be 1): {mp.fsum(xi[j] for j in range(n))}", flush=True)
    # xihat(z) = 2 L^{-1/2} sin(zL/2) sum_j xi_j/(z-2pi j/L)
    Lf = float(L)
    xif = [float(xi[j]) for j in range(n)]
    ajs = [2*math.pi*(j-N)/Lf for j in range(n)]
    def S(z):
        # sum xi_j/(z-a_j), pole-cancelled near a_j via series
        tot = 0.0
        for c, a in zip(xif, ajs):
            d = z - a
            if abs(d) < 1e-8:
                # use derivative term: near pole, summand ~ c/d; but sin(zL/2)
                # has matching zero; use expansion (handled by caller)
                tot += c / d
            else:
                tot += c / d
        return tot
    def xihat(z):
        return 2/math.sqrt(Lf)*math.sin(z*Lf/2)*S(z)
    # scan for sign changes of xihat on (0, 60), avoiding poles a_j
    import numpy as np
    poles = sorted([a for a in ajs if a > 0])
    roots = []
    # scan intervals between consecutive poles
    bounds = [0.1] + poles + [70.0]
    for lo, hi in zip(bounds[:-1], bounds[1:]):
        if hi - lo < 1e-6:
            continue
        # sample densely
        nn = max(20, int((hi-lo)*8)+1)
        zs = np.linspace(lo+1e-9, hi-1e-9, nn)
        vals = [xihat(z) for z in zs]
        for i in range(len(zs)-1):
            if vals[i] == 0:
                roots.append(zs[i])
            elif vals[i]*vals[i+1] < 0:
                a_, b_ = zs[i], zs[i+1]
                for _ in range(80):
                    m_ = 0.5*(a_+b_)
                    if xihat(a_)*xihat(m_) <= 0:
                        b_ = m_
                    else:
                        a_ = m_
                roots.append(0.5*(a_+b_))
    # deduplicate
    roots.sort()
    droots = []
    for r in roots:
        if not droots or abs(r-droots[-1]) > 1e-6:
            droots.append(r)
    print(f"found {len(droots)} roots in (0,70)", flush=True)
    # known zeros (first 10)
    true = [14.134725141734693790, 21.022039638771554993, 25.010857580145688763,
            30.424876125859513210, 32.935061587739189690, 37.586178158825671257,
            40.918719012147495187, 43.327073280914999519, 48.005150881167159727,
            49.773832477672302181]
    for i, (r, t) in enumerate(zip(droots[:10], true)):
        print(f"  root {i+1}: {r:.10f}  true {t:.10f}  err {abs(r-t):.2e}", flush=True)

if __name__ == '__main__':
    main()
