"""
Controls for CCM: does the zero recovery actually depend on prime input?
- Control A: Wp = 0 (no prime sum). If zeros persist, primes aren't load-bearing.
- Control B: shuffled prime weights (permute Lambda(k) across k).
- Control C: shuffled log k (permute the positions).
"""
import sys
from mpmath import mp
import math, random

def run_control(mode, lam2=13.0, N=20, dps=100, seed=0):
    mp.dps = dps
    from ccm_reimpl import build_M, prime_weights, W02, WR_entry, Wp_entry
    from ccm_reimpl import alpha_L, beta_L, Ie_L, q_nm, rho
    lam = mp.sqrt(lam2)
    L = 2*mp.log(lam)
    idx = list(range(-N, N+1))
    n = len(idx)
    print(f"Control {mode}: lam^2={lam2} N={N} dps={dps}", flush=True)

    # build abg cache (fast Ie_L)
    a = {nn: alpha_L(nn, L) for nn in idx}
    b = {nn: beta_L(nn, L) for nn in idx}
    ie = {nn: Ie_L(nn, L) for nn in idx}
    abg = (a, b, ie)
    pw = prime_weights(lam)
    ks = sorted(pw.keys())
    print(f"  prime powers: {len(ks)}", flush=True)

    if mode == 'A':
        # zero out Wp
        def wp_mod(n_, m_):
            return mp.mpf('0')
    elif mode == 'B':
        # shuffle Lambda values across k
        random.seed(seed)
        vals = [pw[k] for k in ks]
        random.shuffle(vals)
        pw2 = {k: v for k, v in zip(ks, vals)}
        def wp_mod(n_, m_):
            s = mp.mpf('0')
            for k, lamk in pw2.items():
                lk = mp.log(k)
                if lk > L: continue
                s += lamk * k**mp.mpf('-0.5') * q_nm(lk, n_, m_, L)
            return s
    elif mode == 'C':
        # shuffle the log k positions (keep weights, permute which k)
        random.seed(seed)
        lks = [mp.log(k) for k in ks]
        random.shuffle(lks)
        # assign shuffled log-positions to the prime powers in order
        pairs = list(zip(ks, lks))  # (k_for_weight, shuffled_logpos)
        # weight of k=p^r is log p, placed at shuffled position
        def wp_mod(n_, m_):
            s = mp.mpf('0')
            for k, lk_shuf in pairs:
                if lk_shuf > L: continue
                # k determines k^{-1/2} and Lambda(k); lk_shuf is where q is eval'd
                s += pw[k] * k**mp.mpf('-0.5') * q_nm(lk_shuf, n_, m_, L)
            return s
    else:
        raise ValueError(mode)

    M = mp.matrix(n)
    for ii, n_ in enumerate(idx):
        for jj, m_ in enumerate(idx):
            if jj < ii: continue
            v = W02(n_, m_, L) - WR_entry(n_, m_, L, abg) - wp_mod(n_, m_)
            M[ii, jj] = v; M[jj, ii] = v

    # even block
    Me = mp.matrix(N+1)
    for aa in range(N+1):
        for bb in range(aa, N+1):
            if aa == 0 and bb == 0: v = M[N, N]
            elif aa == 0: v = (M[N, N+bb] + M[N, N-bb])/mp.sqrt(2)
            elif bb == 0: v = (M[N+aa, N] + M[N-aa, N])/mp.sqrt(2)
            else: v = (M[N+aa,N+bb]+M[N+aa,N-bb]+M[N-aa,N+bb]+M[N-aa,N-bb])/2
            Me[aa,bb]=v; Me[bb,aa]=v
    Minv = mp.inverse(Me)
    x = mp.matrix([mp.mpf(1)]*(N+1)); x = x/mp.norm(x)
    for it in range(50):
        y = Minv*x; x = y/mp.norm(y)
    eps = (x.T*(Me*x))[0]
    print(f"  eps_N = {float(eps):.3e}", flush=True)

    # build xihat and find first root
    xi = mp.matrix([mp.mpf(0)]*n)
    xi[N] = x[0]
    for k in range(1, N+1):
        xi[N+k] = x[k]/mp.sqrt(2); xi[N-k] = x[k]/mp.sqrt(2)
    s = mp.fsum(xi[j] for j in range(n)); xi = xi/s
    Lf = float(L); xif = [float(xi[j]) for j in range(n)]
    ajs = [2*math.pi*(j-N)/Lf for j in range(n)]
    def xihat(z):
        tot = 0.0
        for c_, aj_ in zip(xif, ajs):
            d = z - aj_
            tot += c_/d if abs(d) > 1e-12 else 0.0
        return 2/math.sqrt(Lf)*math.sin(z*Lf/2)*tot
    # scan (0, 30) for first sign change away from poles
    import numpy as np
    poles = sorted([a for a in ajs if 0 < a < 30])
    roots = []
    bounds = [0.5] + poles + [30.0]
    for lo, hi in zip(bounds[:-1], bounds[1:]):
        if hi-lo < 1e-6: continue
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
        if roots: break
    if roots:
        print(f"  first root: {roots[0]:.6f} (true 14.134725)", flush=True)
        print(f"  err: {abs(roots[0]-14.1347251417):.2e}", flush=True)
    else:
        print("  NO ROOT FOUND in (0,30)", flush=True)

if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'A'
    seed = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    run_control(mode, seed=seed)
