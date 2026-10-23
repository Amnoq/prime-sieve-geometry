#!/usr/bin/env python3
"""
Node 11j -- systematic prime-load mapping on the CCM machine.

Sequential follow-up to 11f's failure-modes pilot (which dropped only
p=2,3,5). Question: which prime powers in W_p are load-bearing for zero
recovery, and does the measured load hierarchy match the explicit-formula
weights w(k) = Lambda(k)/sqrt(k)?

Method: c=13 (lam=sqrt(13)), N=20, dps=80 -- the 11f pilot scale.
W_p is LINEAR in the prime-power contributions, so precompute the
prime-free base (W02 - WR) and each Q^{(k)} once (even-projected), then
each ablation is a fast matrix sum + inverse iteration.

Metrics per ablation: eps_N (tiny eigenvalue survives?) and first-root
error vs zeta zero 1 (14.1347251417...).

Status: COMPUTED 2026-10-05. Decision-tree entry: Node 11j.
"""
import sys
import json
import numpy as np
from mpmath import mp
sys.path.insert(0, "/home/hatch/workspace/prime-sieve-geometry/ccm")
from ccm_reimpl import (prime_weights, W02, WR_entry, q_nm,
                        alpha_L, beta_L, Ie_L)

LAM2 = 13.0
N = 20
DPS = 80
Z1 = 14.134725141734693

def even_project(M, N):
    n = 2*N+1
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
    """Even-projected contribution of prime power k: Lambda(k)k^-1/2 q(log k)."""
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
        qv = c * q_nm(lk, nn, nn, L)
        Q[ii, ii] = qv
        for jj, mm in enumerate(idx):
            if jj <= ii:
                continue
            qv2 = c * q_nm(lk, nn, mm, L)
            Q[ii, jj] = qv2
            Q[jj, ii] = qv2
    return even_project(Q, N)

def solve_even(Me, L, N, idx):
    """Inverse iteration for smallest eigenpair + xihat first root."""
    mp.dps = DPS
    n = N+1
    Minv = mp.inverse(Me)
    x = mp.matrix([mp.mpf(1)]*n)
    x = x/mp.norm(x)
    for _ in range(50):
        y = Minv*x
        x = y/mp.norm(y)
    eps = (x.T*(Me*x))[0]
    # reconstruct full xi (even extension)
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
    poles = sorted([float(a) for a in ajs if 0 < a < 30])
    bounds = [0.5] + poles + [30.0]
    root = None
    for lo, hi in zip(bounds[:-1], bounds[1:]):
        if hi-lo < 1e-6:
            continue
        zs = np.linspace(lo+1e-9, hi-1e-9, max(30, int((hi-lo)*10)))
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
                root = 0.5*(a_+b_)
                break
        if root:
            break
    return float(eps), root

def main():
    mp.dps = DPS
    lam = mp.sqrt(LAM2)
    print("building prime-free base ...", flush=True)
    base, L, idx = build_base(lam, N)
    pw0 = prime_weights(lam)
    ks = sorted(pw0.keys())
    print(f"prime powers <= 13: {ks}", flush=True)
    Qks = {}
    for k in ks:
        Q = build_Qk(lam, N, k, pw0[k])
        if Q is not None:
            Qks[k] = Q
    print("base + Qk cached.", flush=True)

    def run(dropped):
        Me = base.copy()
        for k, Q in Qks.items():
            if k not in dropped:
                Me = Me - Q
        return solve_even(Me, L, N, idx)

    results = {}
    eps0, root0 = run(set())
    err0 = abs(root0 - Z1) if root0 else float('nan')
    results["baseline"] = {"eps": eps0, "root": root0, "err": err0}
    print(f"baseline: eps={eps0:.2e} root={root0:.6f} err={err0:.2e}",
          flush=True)

    # single prime-power ablations
    for k in ks:
        eps, root = run({k})
        err = abs(root - Z1) if root else float('nan')
        w = float(pw0[k])/np.sqrt(k)  # explicit-formula weight
        results[f"drop_k={k}"] = {"eps": eps, "root": root, "err": err,
                                 "w": w}
        rs = f"{root:.4f}" if root else "None"
        print(f"drop k={k:2d} (w={w:.3f}): eps={eps:.2e} "
              f"root={rs} err={err:.2e}", flush=True)

    # full-prime ablations (all powers of p)
    for p in [2, 3, 5, 7, 11, 13]:
        drop = set()
        kk = p
        while kk <= 13:
            drop.add(kk)
            if kk > 13 // p:
                break
            kk *= p
        drop = {k for k in drop if k in ks}
        eps, root = run(drop)
        err = abs(root - Z1) if root else float('nan')
        results[f"drop_p={p}"] = {"eps": eps, "root": root, "err": err,
                                 "dropped": sorted(drop)}
        rs = f"{root:.4f}" if root else "None"
        print(f"drop p={p:2d} {sorted(drop)}: eps={eps:.2e} "
              f"root={rs} err={err:.2e}", flush=True)

    json.dump({k: {kk: (float(vv) if isinstance(vv, float) else vv)
                   for kk, vv in v.items()} for k, v in results.items()},
              open("node11j_loadmap.json", "w"))
    print("wrote node11j_loadmap.json")

if __name__ == "__main__":
    main()
