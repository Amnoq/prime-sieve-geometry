#!/usr/bin/env python3
"""Node 11ac -- layered hunt: can sigma act on SPECTRAL data?
Probe A: cycle C_M decorated with the wheel's coprime marking (sigma-symmetric).
Probe B: same cycle decorated with the true prime indicator (sigma-breaking).
Measure ||[H,R]|| in both; identify the wheel marking's spectral content."""
import numpy as np, math

def cycle_adj(M):
    A = np.zeros((M, M))
    for i in range(M):
        A[i, (i+1) % M] = 1.0
        A[i, (i-1) % M] = 1.0
    return A

def reflect(M):
    R = np.zeros((M, M))
    for i in range(M):
        R[i, (-i) % M] = 1.0
    return R

def primes_upto(n):
    s = bytearray(b'\x01')*(n+1); s[:2] = b'\x00\x00'
    for i in range(2, int(n**0.5)+1):
        if s[i]:
            s[i*i:n+1:i] = b'\x00'*(((n-i*i)//i)+1)
    return set(i for i, v in enumerate(s) if v)

# ---------- Probe A: wheel marking, M=210 ----------
M = 210
A, R = cycle_adj(M), reflect(M)
V = np.array([0.0 if math.gcd(r, M) == 1 else 1.0 for r in range(M)])
H = A + np.diag(V)
commA = float(np.linalg.norm(H @ R - R @ H))
print("A) wheel M=210, coprime marking: ||[H,R]|| = %.3e  (sigma EXACT on spectrum)" % commA)

# identify the marking's spectral content: Fourier vs Ramanujan sums
def mu(n):
    cnt, nn, p = 0, n, 2
    while p*p <= nn:
        if nn % p == 0:
            cnt += 1; nn //= p
            if nn % p == 0: return 0
        p += 1 if p == 2 else 2
    if nn > 1: cnt += 1
    return -1 if cnt % 2 else 1
def phi(n):
    r, nn, p = n, n, 2
    while p*p <= nn:
        if nn % p == 0:
            while nn % p == 0: nn //= p
            r -= r // p
        p += 1 if p == 2 else 2
    if nn > 1: r -= r // nn
    return r
def ramanujan(Mq, j):
    from math import gcd
    d = gcd(Mq, j); Mm = Mq // d
    return mu(Mm)*phi(Mq)//phi(Mm)
cop = np.array([1.0 if math.gcd(r, M) == 1 else 0.0 for r in range(M)])
worst = 0.0
for j in range(M):
    got = float(np.real(np.sum(cop*np.exp(2j*math.pi*np.arange(M)*j/M))))
    worst = max(worst, abs(got - ramanujan(M, j)))
print("A) wheel marking Fourier == Ramanujan sums c_M(j): max dev %.3e" % worst)
print("   => the wheel's spectral content is Ramanujan (exact, classical) -- NOT zeta tones")

# control: random sigma-symmetric marking, spectral spacing comparison
rng = np.random.default_rng(0)
def spec_stats(Vv):
    w = np.linalg.eigvalsh(A + np.diag(Vv))
    s = np.diff(np.sort(w)); s = s[s > 1e-9]
    return float(np.mean(s)), float(np.std(s))
Vrand = rng.random(M); Vrand = np.array([Vrand[min(r, (-r) % M)] for r in range(M)])
mw, sw = spec_stats(V); mr, sr = spec_stats(Vrand)
print("A) spacing mean/std: wheel (%.4f, %.4f) vs random-symmetric (%.4f, %.4f)" % (mw, sw, mr, sr))

# ---------- Probe B: true prime marking, N=2000 ----------
N = 2000
P = primes_upto(N)
A2, R2 = cycle_adj(N), reflect(N)
Vp = np.array([0.0 if (i+1) in P else 1.0 for i in range(N)])  # vertex i <-> integer i+1
H2 = A2 + np.diag(Vp)
commB = float(np.linalg.norm(H2 @ R2 - R2 @ H2))
print("B) true-prime marking N=2000: ||[H,R]|| = %.3f  (sigma BROKEN)" % commB)
print("   ratio B/A: %.2e" % (commB/max(commA, 1e-300)))
