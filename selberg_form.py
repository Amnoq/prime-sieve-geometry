#!/usr/bin/env python3
"""10c: Selberg's lambda^2 sieve as an optimized quadratic form on the complex.

Face-native Selberg form on the finite complex Delta_z (primes <= z):
    Q(lam) = sum_{S,T} lam_S lam_T / prod(S union T),   lam_empty = 1.
Squarefree d <-> face S with prod S = d; lcm(d_S, d_T) = prod(S union T).

Parts:
  A. PD check + exact optimizer lam* for z = 5,7,11,13,17,19.
  B. lam* pattern: is lam*_S / mu(S) radial in prod S?
  C. Qmin vs Mertens product delta(z)^{-1} = prod(1-1/p)^{-1}.
  D. Explicit sum-of-squares (eigen-decomposition) at z=7.
  E. Classical level-truncated G(z) = sum_{d<=z} mu^2(d)/phi(d) for context.
"""
import math
import numpy as np

def primes_upto(z):
    bs = bytearray(b"\x01") * (z + 1)
    bs[0:2] = b"\x00\x00"
    for i in range(2, int(z ** 0.5) + 1):
        if bs[i]:
            bs[i * i:z + 1:i] = b"\x00" * (((z - i * i) // i) + 1)
    return [i for i in range(2, z + 1) if bs[i]]

def face_system(primes):
    n = len(primes); N = 2 ** n
    prod = np.ones(N); mu = np.ones(N, dtype=int)
    for m in range(1, N):
        b = (m & -m).bit_length() - 1
        prev = m ^ (1 << b)
        prod[m] = prod[prev] * primes[b]
        mu[m] = -mu[prev]
    M = np.empty((N, N))
    for a in range(N):
        pa = prod[a]
        for b_ in range(N):
            # prod(a|b) = prod[a]*prod[b]/prod[a&b]
            M[a, b_] = prod[a & b_] / (pa * prod[b_])
    return prod, mu, M

def optimize(M):
    N = M.shape[0]
    e = np.zeros(N); e[0] = 1.0
    Minv_e = np.linalg.solve(M, e)
    den = float(e @ Minv_e)
    return Minv_e / den, 1.0 / den

print("Part A/B/C: optimizer, pattern, Mertens recovery")
print(f"{'z':>3} {'n_pr':>4} {'faces':>6} {'min eig':>10} {'Qmin':>10} "
      f"{'delta^-1':>10} {'Qmin*delta':>10}")
for z in [5, 7, 11, 13, 17, 19]:
    pr = primes_upto(z)
    prod, mu, M = face_system(pr)
    try:
        np.linalg.cholesky(M)
        pd = True
    except np.linalg.LinAlgError:
        pd = False
    mineig = float(np.linalg.eigvalsh(M)[0])
    lam, Qmin = optimize(M)
    delta_inv = 1.0
    for p in pr:
        delta_inv /= (1 - 1 / p)
    print(f"{z:>3} {len(pr):>4} {2**len(pr):>6} {mineig:>10.3e} {Qmin:>10.6f} "
          f"{delta_inv:>10.6f} {Qmin/delta_inv:>10.6f}   PD={pd and mineig>0}")

# Part B detail at z=7: lam*_S / mu(S) vs prod S
print("\nPart B: lam* pattern at z=7 (S, mu, lam*, lam*/mu, prod)")
pr = primes_upto(7)
prod, mu, M = face_system(pr)
lam, Qmin = optimize(M)
N = len(lam)
order = sorted(range(N), key=lambda m: (prod[m], m))
for m in order:
    S = tuple(pr[i] for i in range(len(pr)) if (m >> i) & 1)
    r = lam[m] / mu[m]
    print(f"  S={str(S):>16} mu={mu[m]:+d} lam*={lam[m]:+.6f} lam*/mu={r:+.6f} prod={int(prod[m])}")

# radiality check: group lam*/mu by prod value
print("\n  radiality: lam*/mu grouped by prod S")
from collections import defaultdict
g = defaultdict(list)
for m in range(N):
    g[int(prod[m])].append(lam[m] / mu[m])
for d in sorted(g):
    vs = g[d]
    print(f"    prod={d:>4}: n={len(vs):>2} mean={np.mean(vs):+.6f} spread={max(vs)-min(vs):.2e}")

# Part D: sum of squares at z=7
print("\nPart D: eigen-decomposition at z=7 (Q = sum_k (q_k . lam)^2 / sigma_k)")
w, V = np.linalg.eigh(M)
print(f"  eigenvalues: min={w[0]:.3e} max={w[-1]:.3e} all>0: {bool((w>0).all())}")
print(f"  verify: ||M - V diag V'|| = {np.linalg.norm(M - (V*w)@V.T):.2e}")
# top eigenvector face pattern (largest eigenvalue direction)
vmax = V[:, -1]
print("  top eigenvector (largest eig) face pattern [S: coeff]:")
for m in order:
    S = tuple(pr[i] for i in range(len(pr)) if (m >> i) & 1)
    print(f"    {str(S):>12}: {vmax[m]:+.4f}")
# reconstruct Q(lam*) from the square form as a check: M = V diag(w) V',
# so lam' M lam = sum_k w_k (V_k . lam)^2
Qcheck = float(sum(w[k] * (V[:, k] @ lam) ** 2 for k in range(N)))
print(f"  Q(lam*) via squares = {Qcheck:.6f}  (direct {float(lam@M@lam):.6f})")

# Part E: classical level-truncated G(z) for context
print("\nPart E: classical G(z)=sum_{d<=z} mu^2(d)/phi(d); 1/G(z) vs our Qmin")
for z in [5, 7, 11, 13, 17, 19]:
    pr = primes_upto(z)
    # all squarefree d<=z from these primes
    N = 2 ** len(pr)
    G = 0.0
    for m in range(N):
        d = 1; phi = 1; ok = True
        for i, p in enumerate(pr):
            if (m >> i) & 1:
                d *= p
                if d > z:
                    ok = False; break
                phi *= (p - 1)
        if ok and d <= z:
            G += 1.0 / phi
    prod, mu, M = face_system(pr)
    _, Qmin = optimize(M)
    print(f"  z={z:>2}: 1/G(z)={1/G:.6f}  Qmin(face-native)={Qmin:.6f}  "
          f"delta^-1={1/np.prod([1-1/p for p in pr]):.6f}")
