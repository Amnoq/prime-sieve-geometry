#!/usr/bin/env python3
"""Node 17 — Direct predictive equation from positive-region geometry.

Leg (c) NULL/control: the circle sieve's generation rule (document eq 5:
generate size n iff n/d is not a whole number for every existing generated
size d) reproduced against an independent prime list through 10^4.

Leg (a) CLAIM: positive-region geometry of P_S(x) = prod_{d in S} H_d(x)^2,
H_d(x)^2 = r_d(x)*(d - r_d(x)), r_d(x) = x - d*floor(x/d)  [document eq 20,23].
For S in {(2,3,5),(2,3,5,7),(2,3,5,7,11)}: enumerate positive regions
(maximal open intervals where P_S > 0), record endpoints/width/argmax/max/
integral/survivor flag; then record the FIRST survivor beyond each processed
endpoint and its region's shape. Observation only — no conclusions drawn.

Leg (b) POLAR is analytic (see node file); no computation here.
"""

import json
import math
import numpy as np
from scipy.integrate import quad

# ---------------------------------------------------------------- leg (c)
def circle_sieve(N):
    """Document eq (5), literal: new size at n iff no existing size divides n."""
    sizes = []
    for n in range(2, N + 1):
        if all(n % d != 0 for d in sizes):
            sizes.append(n)
    return sizes

def eratosthenes(N):
    """Independent prime list (classical sieve, separate code path)."""
    sieve = bytearray(b"\x01") * (N + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, int(N ** 0.5) + 1):
        if sieve[p]:
            sieve[p * p : N + 1 : p] = b"\x00" * ((N - p * p) // p + 1)
    return [i for i in range(2, N + 1) if sieve[i]]

# ---------------------------------------------------------------- leg (a)
def r_d(x, d):
    return x - d * np.floor(x / d)

def H2(x, d):
    r = r_d(x, d)
    return r * (d - r)

def P_S(x, S):
    x = np.asarray(x, dtype=float)
    p = np.ones_like(x)
    for d in S:
        p = p * H2(x, d)
    return p

def log_P_S(x, S):
    # sum of logs; -inf-safe via clipping (only called strictly inside regions)
    x = np.asarray(x, dtype=float)
    s = np.zeros_like(x)
    for d in S:
        s = s + np.log(np.maximum(H2(x, d), 1e-300))
    return s

def region_argmax(a, b, S):
    """log P_S is concave on (a,b) [sum of concave logs of concave parabolas
    with r_d linear in x there] -> ternary search on the log."""
    lo, hi = a + 1e-12, b - 1e-12
    for _ in range(200):
        m1 = lo + (hi - lo) / 3.0
        m2 = hi - (hi - lo) / 3.0
        if log_P_S(m1, S) < log_P_S(m2, S):
            lo = m1
        else:
            hi = m2
    return 0.5 * (lo + hi)

def analyze_S(S):
    S = tuple(sorted(S))
    W = math.prod(S)
    bounds = set()
    for d in S:
        k = 0
        while k * d < W:
            bounds.add(k * d)
            k += 1
    bounds.add(W)
    B = sorted(bounds)
    regions = []
    for a, b in zip(B[:-1], B[1:]):
        width = b - a
        if width <= 0:
            continue
        amax = region_argmax(a, b, S)
        maxval = float(P_S(amax, S))
        integral, _ = quad(lambda x: float(P_S(x, S)), a, b, limit=200)
        survivor = False
        center = None
        if width == 2:
            center = a + 1  # odd integer strictly inside
            survivor = all(center % d != 0 for d in S)
        regions.append(
            dict(a=a, b=b, width=width, argmax=amax,
                 argmax_offset=amax - (a + b) / 2.0,
                 maxval=maxval, log_maxval=math.log(maxval) if maxval > 0 else None,
                 integral=integral, survivor=survivor, center=center)
        )
    return W, regions

def first_survivor_region(N, S_full):
    """S = primes <= N (construction complete through N); first survivor q;
    region of P_S containing q and its shape. Only the single region (q-1,q+1)
    is computed -- no full enumeration (W explodes)."""
    S = tuple(p for p in S_full if p <= N)
    q = N + 1
    while any(q % d == 0 for d in S):
        q += 1
    a, b = q - 1, q + 1  # exact: q-1 even -> in B_S; q+1 even -> in B_S [2 in S]
    amax = region_argmax(a, b, S)
    maxval = float(P_S(amax, S))
    integral, _ = quad(lambda x: float(P_S(x, S)), a, b, limit=200)
    return dict(N=N, S=S, q=q, a=a, b=b, width=2,
                argmax=amax, argmax_offset=amax - q,
                maxval=maxval, log_maxval=math.log(maxval),
                integral=integral)

def main():
    out = {}

    # ---- leg (c): control ----
    NCTL = 10_000
    circ = circle_sieve(NCTL)
    erat = eratosthenes(NCTL)
    out["leg_c_control"] = dict(
        N=NCTL,
        circle_rule_count=len(circ),
        eratosthenes_count=len(erat),
        exact_match=(circ == erat),
        largest=circ[-1] if circ else None,
    )
    print(f"[leg c] circle rule -> {len(circ)} sizes through {NCTL}; "
          f"eratosthenes -> {len(erat)}; exact match: {circ == erat}")

    # ---- leg (a): region census per S ----
    out["leg_a"] = {}
    for S in [(2, 3, 5), (2, 3, 5, 7), (2, 3, 5, 7, 11)]:
        W, regions = analyze_S(S)
        widths = sorted(set(r["width"] for r in regions))
        w2 = [r for r in regions if r["width"] == 2]
        surv = [r for r in w2 if r["survivor"]]
        # Structural fact (exact): width-2 regions ARE the survivor regions.
        # (a,a+2) consecutive in B_S forces a even, so center a+1 is odd and,
        # being absent from B_S, coprime to all d in S. Width-1 regions hold
        # no integer. Hence no non-survivor width-2 regions exist, ever.
        assert len(w2) == len(surv), "width-2 region without survivor!"
        def stats(rs, key):
            v = np.array([r[key] for r in rs])
            return dict(n=int(len(v)), mean=float(v.mean()), std=float(v.std()),
                        min=float(v.min()), max=float(v.max()))
        N = max(S)
        # first survivor region row: smallest survivor center beyond N
        fs = min((r for r in regions if r["survivor"] and r["center"] > N),
                 key=lambda r: r["center"])
        # z-scores of first-survivor shape vs survivor-region distribution
        z = {}
        for key in ("argmax_offset", "log_maxval", "integral"):
            v = np.array([r[key] for r in surv])
            z[key] = float((fs[key] - v.mean()) / v.std()) if v.std() > 0 else 0.0
        out["leg_a"][str(S)] = dict(
            W=W, n_regions=len(regions), widths=widths,
            max_width=max(widths),
            n_width2=len(w2), n_survivor_regions=len(surv),
            survivor_stats={k: stats(surv, k) for k in
                            ("argmax_offset", "log_maxval", "integral")},
            first_survivor=dict(q=fs["center"], a=fs["a"], b=fs["b"],
                                argmax_offset=fs["argmax_offset"],
                                log_maxval=fs["log_maxval"],
                                integral=fs["integral"], z_vs_survivors=z),
            regions=regions,  # full per-region table
        )
        print(f"[leg a] S={S}: W={W}, regions={len(regions)}, widths={widths}, "
              f"width2={len(w2)} (survivor {len(surv)}), "
              f"first survivor q={fs['center']}, z={ {k: round(v,3) for k,v in z.items()} }")

    # ---- leg (a), second panel: incremental (N, first-survivor) pairs ----
    primes = eratosthenes(200)
    pairs = []
    for i, N in enumerate(primes):
        if N > 47:
            break
        rec = first_survivor_region(N, primes)
        pairs.append(rec)
        print(f"[leg a/inc] N={N:2d} S=primes<={N:2d} ({len(rec['S']):2d} sizes) -> "
              f"q={rec['q']:3d} argmax_offset={rec['argmax_offset']:+.6f} "
              f"log_maxval={rec['log_maxval']:.4f} integral={rec['integral']:.6g}")
    out["leg_a_incremental"] = pairs

    with open("/home/hatch/workspace/prime-sieve-geometry/node17_positive_regions.json",
              "w") as f:
        json.dump(out, f, indent=1)
    print("wrote node17_positive_regions.json")

if __name__ == "__main__":
    main()
