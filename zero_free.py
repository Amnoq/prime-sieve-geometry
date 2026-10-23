#!/usr/bin/env python3
"""D8/9b numerics: the 3-4-1 argument in vertex-tower (energy) language.

E(sigma,t) = 1/2 sum_{p,k} (log p) p^{-k sigma} |1 + p^{ikt}|^4
           = 3 E0(sigma) + 4 Re E1(sigma,t) + Re E2(sigma,t) >= 0 termwise,
with E0 = -zeta'/zeta(sigma) ~ 1/(sigma-1) (pole = divergent total prime
energy), E1 = -zeta'/zeta(sigma+it), E2 = -zeta'/zeta(sigma+2it).

A zero of order m at 1+i t0 would force 4 Re E1 ~ -4m/(sigma-1): total
energy -> -infinity, impossible for a sum of nonnegative stratum energies.
"""
import math
import numpy as np


def primes_upto(N):
    bs = bytearray(b"\x01") * (N + 1)
    bs[0:2] = b"\x00\x00"
    for i in range(2, int(N ** 0.5) + 1):
        if bs[i]:
            bs[i * i:N + 1:i] = b"\x00" * (((N - i * i) // i) + 1)
    return np.array([i for i in range(N + 1) if bs[i]], dtype=float)


P = 200000
primes = primes_upto(P)
logp = np.log(primes)
lnp = np.log(primes)


def components(sigma, t):
    a = primes ** (-sigma)
    E0 = float(np.sum(logp * a / (1 - a)))
    z1 = a * np.exp(-1j * t * lnp)
    E1 = complex(np.sum(logp * z1 / (1 - z1)))
    z2 = a * np.exp(-2j * t * lnp)
    E2 = complex(np.sum(logp * z2 / (1 - z2)))
    E = 3 * E0 + 4 * E1.real + E2.real
    # termwise energy form: 1/2 sum_{p,k} (log p) p^{-k s} |1+p^{ikt}|^4
    Et = 0.0
    for p, l in zip(primes, logp):
        pk = p ** (-sigma)
        k = 1
        while pk > 1e-15:
            Et += 0.5 * l * pk * abs(1 + np.exp(1j * k * t * math.log(p))) ** 4
            pk *= p ** (-sigma)
            k += 1
            if k > 200:
                break
    return E0, E1.real, E2.real, E, Et


print("sigma    t        E0(~1/(s-1))  ReE1      ReE2      E=3E0+4ReE1+ReE2   E_termwise")
for sigma in [2.0, 1.5, 1.3, 1.2]:
    for t in [0.0, 5.0, 14.13472514, 30.0]:
        E0, r1, r2, E, Et = components(sigma, t)
        print(f"{sigma:.2f}  {t:11.5f}  {E0:10.4f}  {r1:+9.4f}  {r2:+9.4f}  "
              f"{E:12.4f}      {Et:12.4f}  match={abs(E-Et)<1e-6}")
    print()
