#!/usr/bin/env python3
"""
Extended verification of the user's linear circle sieve.

Faithful simulation of the 2026-09-29 construction:
  - unit circles tile [0,1],[1,2],... (the substrate; n=1 degenerate)
  - at each step n >= 2, point n is "shared" iff a previously spammed
    circle has a boundary there, i.e. iff some earlier prime p divides n
  - if unshared: draw the diameter-[0,n] circle, spam it forward
    (boundaries at multiples of n), and record n as a new prime-sized circle

Verdict-equivalence note (exact, not heuristic):
  sieve_complex.linear_circle_sieve computes divs = {p in spammed : n % p == 0}
  and calls n unshared iff divs is empty. This script computes the same
  predicate by trial division over discovered primes, stopping at p*p > n.
  If n is composite its least prime factor is <= sqrt(n), so the early stop
  cannot change any verdict: per-n outcomes are bit-identical to the literal
  simulation. Only the materialized multiple-sets are skipped (memory).

Compared against an independent bytearray Sieve of Eratosthenes and against
known pi(N) values.
"""
import time, json

def linear_circle_sieve_faithful(N):
    """Returns list of unshared points (new circle sizes) up to N."""
    primes = []
    for n in range(2, N + 1):
        shared = False
        for p in primes:
            if p * p > n:
                break
            if n % p == 0:
                shared = True
                break
        if not shared:
            # unshared: draw diameter-[0,n] circle, spam forward
            primes.append(n)
    return primes

def classic_primes(N):
    bs = bytearray(b"\x01") * (N + 1)
    bs[0:2] = b"\x00\x00"
    for i in range(2, int(N ** 0.5) + 1):
        if bs[i]:
            bs[i * i:N + 1:i] = b"\x00" * ((N - i * i) // i + 1)
    return [i for i in range(N + 1) if bs[i]]

# known pi(N) for cross-check
PI_KNOWN = {2000: 303, 10000: 1229, 100000: 9592, 1000000: 78498}

def main():
    results = []
    for N in [2000, 10000, 100000, 1000000]:
        t0 = time.time()
        geo = linear_circle_sieve_faithful(N)
        t_geo = time.time() - t0
        t0 = time.time()
        cls = classic_primes(N)
        t_cls = time.time() - t0
        exact = (geo == cls)
        first_diff = None
        if not exact:
            for a, b in zip(geo, cls):
                if a != b:
                    first_diff = (a, b)
                    break
            if first_diff is None:
                first_diff = ("length", len(geo), len(cls))
        results.append({
            "N": N,
            "geometric_count": len(geo),
            "classic_count": len(cls),
            "pi_known": PI_KNOWN[N],
            "exact_match": exact,
            "first_difference": first_diff,
            "geo_seconds": round(t_geo, 2),
            "classic_seconds": round(t_cls, 3),
        })
        print(f"N={N:>8d}  geo={len(geo):>6d}  classic={len(cls):>6d}  "
              f"pi={PI_KNOWN[N]:>6d}  exact={exact}  geo_time={t_geo:.1f}s",
              flush=True)
    with open("/home/hatch/workspace/prime-sieve-geometry/"
              "linear_sieve_extended_results.json", "w") as f:
        json.dump(results, f, indent=2)
    print("wrote linear_sieve_extended_results.json")

if __name__ == "__main__":
    main()
