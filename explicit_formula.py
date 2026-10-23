#!/usr/bin/env python3
"""10a step 1: ground the explicit formula in our objects.

psi(x) = x - sum_rho x^rho/rho - log(2pi) - (1/2)log(1-x^{-2}),  x not a prime power.
psi from the sieve (D1: sum_{p^k<=x} log p); zeros from mpmath.
Check: truncated zero sum reproduces psi's oscillations; error shrinks with T.
"""
import math
import numpy as np
import mpmath

mpmath.mp.dps = 30


def primes_upto(N):
    bs = bytearray(b"\x01") * (N + 1)
    bs[0:2] = b"\x00\x00"
    for i in range(2, int(N ** 0.5) + 1):
        if bs[i]:
            bs[i * i:N + 1:i] = b"\x00" * (((N - i * i) // i) + 1)
    return [i for i in range(N + 1) if bs[i]]


XMAX = 400
primes = primes_upto(XMAX)
pp_list = []  # (value, log p) for prime powers
for p in primes:
    q, lp = p, math.log(p)
    while q <= XMAX:
        pp_list.append((q, lp))
        q *= p
pp_list.sort()


def psi(x):
    return math.fsum(lp for q, lp in pp_list if q <= x)


print("computing zeros...", flush=True)
N0 = 400
zeros = [complex(mpmath.zetazero(k)) for k in range(1, N0 + 1)]
gammas = np.array([z.imag for z in zeros])
print(f"{N0} zeros, max gamma = {gammas.max():.1f}", flush=True)

xs = np.arange(20.5, 200.5, 5.0)  # half-integers: never prime powers
lnx = np.log(xs)

print("\nT (height) | max|psi - S_T| over x-grid | bound ~ x log^2 x / T (x=200)")
print("----------------------------------------------------------------------")
for T in [50, 100, 200, 400]:
    m = gammas <= T
    gz = gammas[m]
    # S_T(x) = x - 2 Re sum_{0<gamma<=T} x^rho/rho - log(2pi) - 1/2 log(1-x^-2)
    # x^rho = x^{1/2} e^{i gamma log x}; x^rho/rho with rho=1/2+i gamma
    err = 0.0
    for x, lx in zip(xs, lnx):
        s = 0j
        xh = math.sqrt(x)
        for g in gz:
            rho = 0.5 + 1j * g
            s += (xh * complex(math.cos(g * lx), math.sin(g * lx))) / rho
        S = x - 2 * s.real - math.log(2 * math.pi) - 0.5 * math.log(1 - x ** -2)
        err = max(err, abs(psi(x) - S))
    print(f"  {T:6.0f}   |        {err:9.4f}             |      {200*(math.log(200)**2)/T:9.1f}")

# oscillation match at fixed T=400: show psi(x)-x vs -2Re sum (the zeros ARE the error)
print("\nx      psi(x)-x     -2Re sum x^rho/rho - log(2pi)   (T=400)")
m = gammas <= 400
gz = gammas[m]
for x in [30.5, 50.5, 100.5, 150.5]:
    lx = math.log(x)
    xh = math.sqrt(x)
    s = sum((xh * complex(math.cos(g * lx), math.sin(g * lx))) / (0.5 + 1j * g) for g in gz)
    approx = -2 * s.real - math.log(2 * math.pi)
    print(f"{x:6.1f}  {psi(x)-x:+10.4f}   {approx:+10.4f}")
