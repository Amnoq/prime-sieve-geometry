#!/usr/bin/env python3
"""
D6: deformed sieve -> Hardy-Littlewood singular series.

Deformation: prime p marks residues R_p = {0} (p=2), {0, p-2} (p odd),
i.e. n is marked if p|n or p|(n+2). Markers (primes) and survivors
(twin prime lowers) separate -- in the classic sieve they coincided.

1. Generative deformed sieve: survivors == twin lowers (verified).
2. Static z-sieve: exact mu-identity S(x,z) = sum_{d|P(z)} mu(d) E_d(x).
3. Face multiplicities m(S) = prod |R_p|; total weight delta(z) = prod(1-|R_p|/p);
   singular series as renormalized total weight -> 2*C2.
"""

import math
import numpy as np


def primes_upto(N):
    bs = bytearray(b"\x01") * (N + 1)
    bs[0:2] = b"\x00\x00"
    for i in range(2, int(N ** 0.5) + 1):
        if bs[i]:
            bs[i * i:N + 1:i] = b"\x00" * (((N - i * i) // i) + 1)
    return [i for i in range(N + 1) if bs[i]]


# ------------------------------------------------- 1. generative sieve
def deformed_sieve(x):
    """Generative: new prime p spams residues R_p forward (m > p only)."""
    is_prime = bytearray(b"\x01") * (x + 1)
    is_prime[0:2] = b"\x00\x00"
    survives = bytearray(b"\x01") * (x + 1)
    survives[0:2] = b"\x00\x00"
    for n in range(2, x + 1):
        if is_prime[n]:
            is_prime[n::n] = b"\x00" * (((x - n) // n) + 1)
            R = [0] if n == 2 else [0, n - 2]
            for r in R:
                start = r + n if r > 0 else 2 * n  # strictly forward: m > n
                if start <= x:
                    survives[start::n] = b"\x00" * (((x - start) // n) + 1)
    return [n for n in range(3, x + 1) if survives[n]], is_prime


# ------------------------------------------------- 2. static z-sieve
def static_sieve(x, z, primes):
    """S(x,z) = #{1<=n<=x : forall p<=z, n mod p not in R_p}, via marking."""
    marked = np.zeros(x + 1, dtype=bool)
    for p in primes:
        if p > z:
            break
        R = [0] if p == 2 else [0, p - 2]
        for r in R:
            marked[r::p] = True
    marked[0] = True
    return int((~marked[1:]).sum())


def egcd(a, b):
    if b == 0:
        return a, 1, 0
    g, u, v = egcd(b, a % b)
    return g, v, u - (a // b) * v


def crt(a1, m1, a2, m2):
    g, u, _ = egcd(m1, m2)
    assert g == 1
    return (a1 + m1 * ((a2 - a1) * u % m2)) % (m1 * m2)


def mu_identity(x, z, primes):
    """Exact: S(x,z) = sum_{d|P(z)} mu(d) E_d(x)."""
    ps = [p for p in primes if p <= z]
    R = {p: ([0] if p == 2 else [0, p - 2]) for p in ps}
    total = 0
    # enumerate squarefree d | P(z) via recursion
    def rec(i, d, facs, mu):
        nonlocal total
        if i == len(ps):
            if d > 1 or True:
                # E_d(x): CRT over residue combos
                E = 0
                def combos(j, a, m):
                    nonlocal E
                    if j == len(facs):
                        a1 = a if a >= 1 else m  # smallest n>=1 with n%a... n=d class
                        # count n in [1,x], n = a (mod m)
                        if a1 <= x:
                            E += (x - a1) // m + 1
                        return
                    p = facs[j]
                    for r in R[p]:
                        combos(j + 1, crt(a, m, r, p) if j else r, m * p if j else p)
                combos(0, 0, 1)
                total += mu * E
            return
        rec(i + 1, d, facs, mu)                      # skip ps[i]
        rec(i + 1, d * ps[i], facs + [ps[i]], -mu)   # take ps[i]
    rec(0, 1, [], 1)
    return total


if __name__ == "__main__":
    X = 200000
    primes = primes_upto(X + 2)

    # 1. generative survivors == twin lowers
    surv, is_prime = deformed_sieve(X)
    twins = [n for n in range(3, X + 1)
             if is_prime[n] and n + 2 <= X + 1 and is_prime[n + 2]]
    # note: is_prime was mutated by deformed_sieve's own spam; rebuild clean
    bs = bytearray(b"\x01") * (X + 3)
    bs[0:2] = b"\x00\x00"
    for i in range(2, int((X + 2) ** 0.5) + 1):
        if bs[i]:
            bs[i * i:X + 3:i] = b"\x00" * (((X + 2 - i * i) // i) + 1)
    twins = [n for n in range(3, X + 1) if bs[n] and bs[n + 2]]
    print(f"1. generative survivors == twin lowers <= {X}: {surv == twins} "
          f"({len(surv)} survivors)")

    # 2. mu identity
    for z, xx in [(13, 50000), (30, 200000)]:
        s_static = static_sieve(xx, z, primes)
        s_mu = mu_identity(xx, z, primes)
        print(f"2. z={z}, x={xx}: static={s_static}, mu-sum={s_mu}, "
              f"exact={s_static == s_mu}")

    # 3. density -> delta(z), singular series partial products
    C2_target = 1.320323631693739
    print("3. z      delta(z)   S(x,z)/x (x=2e5)   S_renorm -> 2*C2")
    for z in [7, 13, 30, 100]:
        ps = [p for p in primes if p <= z]
        delta = 1.0
        renorm = 1.0
        for p in ps:
            rp = 1 if p == 2 else 2
            delta *= (1 - rp / p)
            renorm *= (1 - rp / p) / (1 - 1 / p) ** 2
        s = static_sieve(200000, z, primes) / 200000
        print(f"    {z:3d}  {delta:.6f}   {s:.6f}            {renorm:.6f} "
              f"(target {C2_target:.5f})")

    # 4. twin heuristic ratio (conjectural! slow convergence expected)
    lx = math.log(X)
    ratio = len(surv) * lx * lx / X
    print(f"4. twin heuristic: pi_2({X})*(log {X})^2/{X} = {ratio:.4f} "
          f"(conjectured -> {C2_target:.4f}; SLOW convergence, unproven)")
