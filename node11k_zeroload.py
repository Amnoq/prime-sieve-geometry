#!/usr/bin/env python3
"""
Node 11k -- prime-load hierarchy vs zero index.

Sequential follow-up to 11j (which mapped load-bearing prime powers for
ZERO 1 only). Question: does the monotone-in-k hierarchy hold for higher
zeros, or does it shift (higher zeros needing finer prime data)?

Method: c=13, N=20, dps=80 (same as 11j). Extract the first 5 xihat roots
(reliable at N=20: err <4e-11 per 11f) for baseline and each ablation.
Load matrix: rows = zeros 1-5, columns = dropped prime powers.

If higher zeros need larger k, the load matrix shifts right with row index
-- the machine resolving zeros hierarchically (small primes: low zeros).
If not, small-k dominance is universal.

Status: COMPUTED 2026-10-05. Decision-tree entry: Node 11k.
"""
import sys
import json
import numpy as np
from mpmath import mp
sys.path.insert(0, "/home/hatch/workspace/prime-sieve-geometry/ccm")
sys.path.insert(0, "/home/hatch/workspace/prime-sieve-geometry")
from ccm_reimpl import (prime_weights, W02, WR_entry, q_nm,
                        alpha_L, beta_L, Ie_L)

LAM2 = 13.0
N = 20
DPS = 80
NROOTS = 5
ZTRUE = [14.134725141734693, 21.02203963877155, 25.01085758014569,
         30.42487612585951, 32.93506158773919]
ZSCAN_MAX = 50.0

def even_project(M, N):
    Me = mp.matrix(N+1)
    for aa in range(N+1):
        for bb in range(aa, N+1):
            if aa == 0 and bb == 0:
                v = M[N, N]
            elif aa == 0:
                v = (M[N, N+bb] + M[N, N-bb])/mp.sqrt(2)
            elif bb == 0:
                v = (M[N+aa, N] + M[N-aa, N])/mp.sqrt(2)
            else:
                v = (M[N+aa, N+bb]+M[N+aa, N-bb]
                     + M[N-aa, N+bb]+M[N-aa, N-bb])/2
            Me[aa, bb] = v
            Me[bb, aa] = v
    return Me

def build_base(lam, N):
    mp.dps = DPS
    L = 2*mp.log(lam)
    idx = list(range(-N, N+1))
    n = len(idx)
    a = {nn: alpha_L(nn, L) for nn in idx}
    b = {nn: beta_L(nn, L) for nn in idx}
    ie = {nn: Ie_L(nn, L) for nn in idx}
    abg = (a, b, ie)
    B = mp.matrix(n)
    for ii, nn in enumerate(idx):
        for jj, mm in enumerate(idx):
            if jj < ii:
                B[ii, jj] = B[jj, ii]
                continue
            B[ii, jj] = W02(nn, mm, L) - WR_entry(nn, mm, L, abg)
    return even_project(B, N), L, idx

def build_Qk(lam, N, k, lamk):
    mp.dps = DPS
    L = 2*mp.log(lam)
    lk = mp.log(k)
    if lk > L:
        return None
    idx = list(range(-N, N+1))
    n = len(idx)
    c = lamk * k**mp.mpf('-0.5')
    Q = mp.matrix(n)
    for ii, nn in enumerate(idx):
        Q[ii, ii] = c * q_nm(lk, nn, nn, L)
        for jj, mm in enumerate(idx):
            if jj <= ii:
                continue
            qv2 = c * q_nm(lk, nn, mm, L)
            Q[ii, jj] = qv2
            Q[jj, ii] = qv2
    return even_project(Q, N)

def solve_roots(Me, L, N, idx, nroots=NROOTS):
    """Inverse iteration + first nroots positive xihat zeros."""
    mp.dps = DPS
    n = N+1
    Minv = mp.inverse(Me)
    x = mp.matrix([mp.mpf(1)]*n)
    x = x/mp.norm(x)
    for _ in range(50):
        y = Minv*x
        x = y/mp.norm(y)
    eps = float((x.T*(Me*x))[0])
    nn = 2*N+1
    xi = mp.matrix([mp.mpf(0)]*nn)
    xi[N] = x[0]
    for kk in range(1, N+1):
        xi[N+kk] = x[kk]/mp.sqrt(2)
        xi[N-kk] = x[kk]/mp.sqrt(2)
    s = mp.fsum(xi[j] for j in range(nn))
    xi = xi/s
    Lf = float(L)
    xif = [float(xi[j]) for j in range(nn)]
    ajs = [2*mp.pi*(j-N)/Lf for j in range(nn)]
    import math
    def xihat(z):
        tot = 0.0
        for c_, aj_ in zip(xif, ajs):
            d = z - float(aj_)
            if abs(d) > 1e-12:
                tot += c_/d
        return 2/math.sqrt(Lf)*math.sin(z*Lf/2)*tot
    poles = sorted([float(a) for a in ajs if 0 < a < ZSCAN_MAX])
    bounds = [0.5] + poles + [ZSCAN_MAX]
    roots = []
    for lo, hi in zip(bounds[:-1], bounds[1:]):
        if hi-lo < 1e-6 or len(roots) >= nroots + 2:
            continue
        zs = np.linspace(lo+1e-9, hi-1e-9, max(40, int((hi-lo)*12)))
        vals = [xihat(z) for z in zs]
        for i in range(len(zs)-1):
            if vals[i]*vals[i+1] < 0:
                a_, b_ = zs[i], zs[i+1]
                for _ in range(50):
                    m_ = 0.5*(a_+b_)
                    if xihat(a_)*xihat(m_) <= 0:
                        b_ = m_
                    else:
                        a_ = m_
                r = 0.5*(a_+b_)
                if not roots or r - roots[-1] > 0.5:
                    roots.append(r)
    roots = sorted(roots)[:nroots]
    return eps, roots

def main():
    mp.dps = DPS
    lam = mp.sqrt(LAM2)
    print("building prime-free base ...", flush=True)
    base, L, idx = build_base(lam, N)
    pw0 = prime_weights(lam)
    ks = sorted(pw0.keys())
    Qks = {}
    for k in ks:
        Q = build_Qk(lam, N, k, pw0[k])
        if Q is not None:
            Qks[k] = Q
    print(f"prime powers: {ks}", flush=True)

    def run(dropped):
        Me = base.copy()
        for k, Q in Qks.items():
            if k not in dropped:
                Me = Me - Q
        return solve_roots(Me, L, N, idx)

    # baseline validation against true zeros
    eps0, roots0 = run(set())
    print(f"baseline eps={eps0:.2e}", flush=True)
    print("baseline roots vs true:",
          flush=True)
    for j, (r, zt) in enumerate(zip(roots0, ZTRUE)):
        print(f"  zero {j+1}: {r:.8f} err={abs(r-zt):.2e}", flush=True)
    base_errs = [abs(r-zt) for r, zt in zip(roots0, ZTRUE)]

    results = {"baseline": {"eps": eps0,
                            "roots": roots0,
                            "errs": base_errs}}
    # load matrix: for each dropped k, errs for zeros 1-5
    print("\nload matrix (err per zero | dropped k):", flush=True)
    header = "zero | " + " ".join(f"k={k:2d}" for k in ks)
    print(header, flush=True)
    load = {}
    for k in ks:
        eps, roots = run({k})
        errs = [abs(r-zt) if r else float('nan')
                for r, zt in zip(roots, ZTRUE)]
        # pad if fewer roots found
        while len(errs) < NROOTS:
            errs.append(float('nan'))
        load[k] = errs
    for j in range(NROOTS):
        row = " ".join(f"{load[k][j]:8.1e}" for k in ks)
        print(f"  {j+1}  | {row}", flush=True)

    # full-prime drops
    print("\nfull-prime drops:", flush=True)
    for p in [2, 3, 5, 7, 11, 13]:
        drop = set()
        kk = p
        while kk <= 13:
            drop.add(kk)
            if kk > 13 // p:
                break
            kk *= p
        drop = {k for k in drop if k in ks}
        eps, roots = run(drop)
        errs = [abs(r-zt) if r else float('nan')
                for r, zt in zip(roots, ZTRUE)]
        while len(errs) < NROOTS:
            errs.append(float('nan'))
        results[f"drop_p={p}"] = {"errs": errs, "dropped": sorted(drop)}
        print(f"  p={p}: " + " ".join(f"{e:.1e}" for e in errs), flush=True)

    results["load_single_k"] = {str(k): v for k, v in load.items()}
    results["baseline_errs"] = base_errs
    json.dump(results, open("node11k_zeroload.json", "w"))
    print("wrote node11k_zeroload.json")

if __name__ == "__main__":
    main()
