#!/usr/bin/env python3
"""D9/9c numerics, part 1: kill the D8 deformation seed.

Twin deformation: |R_2|=1, |R_p|=2 (p odd).
  zeta_R(s) = prod_p (1 - |R_p| p^{-s})^{-1}      (Euler product)
  F(s) = -zeta_R'/zeta_R(s) = sum_p |R_p| (log p)/(p^s - |R_p|)
Coefficients |R_p|^k log p >= 0, so 3-4-1 transports. Question: does it
constrain anything NEW? Check: pole order at s=1, 3-4-1 positivity, and
whether zeta_R has any zeros for the mechanism to exclude.
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


P = 300000
primes = primes_upto(P)
Rp = np.where(primes == 2, 1.0, 2.0)          # |R_p|
logp = np.log(primes)
lnp = np.log(primes)


def F(s):
    # -zeta_R'/zeta_R(s) = sum_p |R_p| log p / (p^s - |R_p|)
    ps = primes ** s
    return complex(np.sum(Rp * logp / (ps - Rp)))


print("sigma    F(sigma)   2/(sigma-1)   (pole order check: F ~ 2/(s-1)?)")
for sigma in [2.0, 1.5, 1.2, 1.1]:
    print(f"{sigma:.2f}    {F(sigma).real:10.4f}   {2/(sigma-1):10.4f}")

print("\n3-4-1 transports: S = 3F(s)+4ReF(s+it)+ReF(s+2it) >= 0 ?")
ok = True
for sigma in [1.5, 1.2, 1.1]:
    mn = 1e18
    for t in np.linspace(0.1, 50, 200):
        S = 3 * F(sigma) + 4 * F(sigma + 1j * t).real + F(sigma + 2j * t).real
        mn = min(mn, S.real)
    print(f"  sigma={sigma:.2f}  min S = {mn:+.4f}  positive: {mn >= 0}")
    ok = ok and mn >= 0

print("\nZeros of zeta_R for Re(s)>1? Each factor (1-|R_p|p^{-s})^{-1}:")
print("  |R_p| p^{-sigma} <= 2*2^{-sigma} < 1 for sigma>1 -> no factor vanishes")
print("  => zeta_R has NO zeros for Re(s)>1 (Euler product).")
print("  The 3-4-1 machine runs fine (positivity holds) but there is")
print("  NOTHING for it to exclude. Pole order doubled (2 vs 1): the")
print("  inequality is EASIER to satisfy, not stronger.")
print("  => deformations repackage the pole; they create no new zero-detector.")
print("  SEED KILLED.")
