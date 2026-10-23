#!/usr/bin/env python3
"""D7 numerics: positivity in the primitive (multiplicative) presentation
vs sign alternation in the additive (face-sum) presentation; 3-4-1 template."""
import math
import numpy as np


def primes_upto(N):
    bs = bytearray(b"\x01") * (N + 1)
    bs[0:2] = b"\x00\x00"
    for i in range(2, int(N ** 0.5) + 1):
        if bs[i]:
            bs[i * i:N + 1:i] = b"\x00" * (((N - i * i) // i) + 1)
    return [i for i in range(N + 1) if bs[i]]


def mobius_array(N):
    mu = np.ones(N + 1, dtype=np.int8)
    is_c = np.zeros(N + 1, dtype=bool)
    is_c[0:2] = True
    for i in range(2, int(N ** 0.5) + 1):
        if not is_c[i]:
            is_c[i * i:N + 1:i] = True
    for p in np.nonzero(~is_c)[0]:
        p = int(p)
        mu[p:N + 1:p] = -mu[p:N + 1:p]
        if p * p <= N:
            mu[p * p:N + 1:p * p] = 0
    mu[0] = 0
    return mu


primes = primes_upto(200000)

# 1. multiplicative positivity: delta(z) > 0, -log delta = positive prime sum
print("z        delta(z)   e^-g/log z   -log delta  pos-sum")
eg = math.exp(-0.5772156649015329)
for z in [10, 30, 100, 1000]:
    ps = [p for p in primes if p <= z]
    delta = 1.0
    for p in ps:
        delta *= (1 - 1 / p)
    possum = sum(1 / (k * p ** k) for p in ps for k in range(1, 40))
    print(f"{z:4d}  {delta:.6f}   {eg / math.log(z):.6f}    "
          f"{-math.log(delta):.6f}  {possum:.6f}")

# 2. additive presentation oscillates around the same limit 0
N = 200000
mu = mobius_array(N)
dd = np.arange(N + 1, dtype=float)
nz = mu != 0
w = np.zeros(N + 1)
w[nz] = mu[nz] / dd[nz]
A = np.cumsum(w)
print("\nX        A(X)=sum mu(d)/d   delta(X)   (both -> 0)")
for X in [100, 1000, 10000, 100000]:
    dl = 1.0
    for p in primes:
        if p > X:
            break
        dl *= (1 - 1 / p)
    print(f"{X:6d}   {A[X]:+.6f}           {dl:.6f}")

# 3. von Mangoldt + the 3-4-1 positivity: S(sigma,t) >= 0
N2 = 500000
Lam = np.zeros(N2 + 1)
for p in primes_upto(N2):
    q = p
    while q <= N2:
        Lam[q] = math.log(p)
        q *= p
n = np.arange(N2 + 1, dtype=float)
ln_n = np.log(n + 1e-300)
print("\n3-4-1: S(sigma,t) = sum Lam(n) n^-sigma [3+4cos(t log n)+cos(2t log n)]")
for sigma in [1.5, 1.2, 1.05]:
    w2 = Lam * n ** (-sigma)
    w2[0:2] = 0.0
    ts = np.linspace(0.1, 50, 400)
    mn = min(float(np.sum(w2 * (3 + 4 * np.cos(t * ln_n) + np.cos(2 * t * ln_n))))
             for t in ts)
    print(f"  sigma={sigma:.2f}  min over t-grid = {mn:+.4f}  (positive: {mn >= 0})")
