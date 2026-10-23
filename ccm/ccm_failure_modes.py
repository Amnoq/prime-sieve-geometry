"""
Failure-mode probes for CCM (honest scope).

We cannot observe "RH false" without an actual counterexample. What we CAN test:
1. PERTURBATION ROBUSTNESS: small noise on prime input -> do zeros degrade
   gracefully (honest reporter) or catastrophically (fine-tuned artifact)?
2. MISSING-PRIME: drop one prime's contribution; the explicit formula predicts
   how zeros shift. Does the operator track the predicted shift?
3. DIRICHLET GENERALIZATION: same machinery on L(s,chi) -- does it report
   THAT function's zeros? (Generality, not RH-false, but tests honesty.)

This script does (1) and (2) at c=13, N=20.
"""
import sys
import numpy as np
from mpmath import mp

def build_and_extract(lam2=13.0, N=20, dps=80, pw_override=None, seed=0):
    mp.dps = dps
    from ccm_reimpl import (prime_weights, W02, WR_entry, Wp_entry,
                            alpha_L, beta_L, Ie_L, q_nm)
    lam = mp.sqrt(lam2); L = 2*mp.log(lam)
    idx = list(range(-N, N+1)); n = len(idx)
    a = {nn: alpha_L(nn, L) for nn in idx}
    b = {nn: beta_L(nn, L) for nn in idx}
    ie = {nn: Ie_L(nn, L) for nn in idx}
    abg = (a, b, ie)
    pw = prime_weights(lam) if pw_override is None else pw_override
    M = mp.matrix(n)
    for ii, n_ in enumerate(idx):
        for jj, m_ in enumerate(idx):
            if jj < ii: continue
            v = W02(n_, m_, L) - WR_entry(n_, m_, L, abg) - Wp_entry(n_, m_, L, pw)
            M[ii, jj] = v; M[jj, ii] = v
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
    # xihat first root
    xi = mp.matrix([mp.mpf(0)]*n)
    xi[N] = x[0]
    for k in range(1, N+1):
        xi[N+k] = x[k]/mp.sqrt(2); xi[N-k] = x[k]/mp.sqrt(2)
    s = mp.fsum(xi[j] for j in range(n)); xi = xi/s
    Lf = float(L); xif = [float(xi[j]) for j in range(n)]
    ajs = [2*mp.pi*(j-N)/Lf for j in range(n)]
    import math
    def xihat(z):
        tot = 0.0
        for c_, aj_ in zip(xif, ajs):
            d = z - float(aj_)
            tot += c_/d if abs(d) > 1e-12 else 0.0
        return 2/math.sqrt(Lf)*math.sin(z*Lf/2)*tot
    poles = sorted([float(a) for a in ajs if 0 < a < 30])
    bounds = [0.5] + poles + [30.0]
    root = None
    for lo, hi in zip(bounds[:-1], bounds[1:]):
        if hi-lo < 1e-6: continue
        zs = np.linspace(lo+1e-9, hi-1e-9, max(30, int((hi-lo)*10)))
        vals = [xihat(z) for z in zs]
        for i in range(len(zs)-1):
            if vals[i]*vals[i+1] < 0:
                a_, b_ = zs[i], zs[i+1]
                for _ in range(50):
                    m_ = 0.5*(a_+b_)
                    if xihat(a_)*xihat(m_) <= 0: b_ = m_
                    else: a_ = m_
                root = 0.5*(a_+b_); break
        if root: break
    return float(eps), root

if __name__ == '__main__':
    mp.dps = 80
    from ccm_reimpl import prime_weights
    lam = mp.sqrt(13.0)
    pw0 = prime_weights(lam)
    ks = sorted(pw0.keys())
    rng = np.random.default_rng(0)

    print("=== Probe 1: multiplicative noise on Lambda ===", flush=True)
    for noise in [1e-6, 1e-4, 1e-2]:
        pw = {k: v*(1+noise*rng.standard_normal()) for k, v in pw0.items()}
        eps, root = build_and_extract(pw_override=pw)
        err = abs(root-14.1347251417) if root else float('nan')
        rs = f"{root:.6f}" if root else "None"
        print(f"  noise={noise:.0e}: eps={eps:.2e}, root={rs}, err={err:.2e}", flush=True)

    print("=== Probe 2: drop one prime (p=2,3,5) ===", flush=True)
    for p_drop in [2, 3, 5]:
        pw = {k: v for k, v in pw0.items()}
        # remove all prime powers of p_drop
        for k in list(pw.keys()):
            kk = k
            while kk % p_drop == 0:
                kk //= p_drop
            if kk == 1:
                del pw[k]
        eps, root = build_and_extract(pw_override=pw)
        err = abs(root-14.1347251417) if root else float('nan')
        rs = f"{root:.6f}" if root else "None"
        print(f"  drop p={p_drop}: eps={eps:.2e}, root={rs}, err vs zeta={err:.2e}", flush=True)
