#!/usr/bin/env python3
"""
Linear circle sieve -> finite incidence (divisor) complex experiment.

1. Simulate the user's geometric sieve literally:
   - unit circles tile [0,1],[1,2],... on an axis
   - at step n, point n is "shared" iff a previously spammed circle has a
     boundary there; else draw diameter-[0,n] circle and spam it forward
     (boundaries at multiples of n).
2. Verify the unshared points are exactly the primes.
3. Build the incidence complex Delta_N:
     vertices = primes <= N
     faces    = subsets S of primes with prod(S) <= N
   (a set of primes co-occurs iff some integer <= N is divisible by all of
   them -- exactly the spammed-circle boundary incidences).
4. Compute f-vector, facets, Z/2 homology, and facet recursion.
"""

import itertools, math, sys
from functools import reduce


# ---------------------------------------------------------------- sieve
def linear_circle_sieve(N):
    """Literal simulation. Returns (primes, spammed, divisors)."""
    spammed = {}          # p -> set of boundary points (multiples of p)
    primes = []           # unshared points > 1, in order of discovery
    divisors = {}         # n -> set of primes dividing n (territory incidence)
    for n in range(1, N + 1):
        divs = {p for p in spammed if n % p == 0}
        divisors[n] = divs
        if not divs:
            # unshared: new sized circle [0,n], spammed forward.
            # n=1 is degenerate: [0,1] spammed forward IS the unit tiling
            # (the substrate), so it is not recorded as a spammed marker --
            # the sharing check effectively starts at the second circle.
            if n > 1:
                spammed[n] = set(range(n, N + 1, n))
            if n > 1:
                primes.append(n)
    return primes, spammed, divisors


def classic_primes(N):
    bs = bytearray(b"\x01") * (N + 1)
    bs[0:2] = b"\x00\x00"
    for i in range(2, int(N ** 0.5) + 1):
        if bs[i]:
            bs[i * i:N + 1:i] = b"\x00" * ((N - i * i) // i + 1)
    return [i for i in range(N + 1) if bs[i]]


# ---------------------------------------------------------------- complex
def faces_upto(N, primes):
    """All subsets S of `primes` with prod(S) <= N (empty set included)."""
    out = [()]
    # iterative deepening over primes with product pruning
    stack = [(0, 1, ())]
    while stack:
        i, prod, face = stack.pop()
        for j in range(i, len(primes)):
            p = primes[j]
            if prod * p > N:
                break
            nf = face + (j,)
            out.append(nf)
            stack.append((j + 1, prod * p, nf))
    return out


def f_vector(faces):
    from collections import Counter
    c = Counter(len(f) - 1 for f in faces)
    d = max(c) if c else -1
    return [c.get(k, 0) for k in range(d + 1)]


def facets_of(faces):
    fset = set(faces)
    # a face is a facet iff no strict superface exists; check via vertex add
    # cheap approach: sort by size desc, mark subfaces
    bysize = sorted(faces, key=len, reverse=True)
    sub = set()
    facets = []
    for f in bysize:
        if f in sub:
            continue
        facets.append(f)
        # mark all proper subfaces
        for r in range(len(f)):
            for sf in itertools.combinations(f, r):
                sub.add(sf)
    return facets


# ------------------------------------------------------- GF(2) homology
def betti_numbers(faces):
    """Reduced-style ordinary Betti numbers over Z/2. faces include ()."""
    # group faces by dimension
    bydim = {}
    for f in faces:
        bydim.setdefault(len(f) - 1, []).append(f)
    maxd = max(bydim)
    idx = {f: i for d in bydim for i, f in enumerate(bydim[d])}
    # boundary matrix d_k: rows = (k-1)-faces, cols = k-faces, as bitsets
    def rank(mat_rows, ncols):
        # mat_rows: list of ints (bitmask over columns); rank over GF(2)
        rows = [r for r in mat_rows if r]
        piv = {}
        for r in rows:
            while r:
                b = r.bit_length() - 1
                if b in piv:
                    r ^= piv[b]
                else:
                    piv[b] = r
                    break
        return len(piv)
    ranks = {}
    for k in range(1, maxd + 1):
        rows = []
        lower = bydim.get(k - 1, [])
        lidx = {f: i for i, f in enumerate(lower)}
        for f in bydim[k]:
            mask = 0
            for t in range(len(f)):
                g = f[:t] + f[t + 1:]
                mask |= 1 << lidx[g]
            rows.append(mask)
        # rank of boundary map as column space: transpose view
        # compute rank of matrix with `rows` as row vectors
        ranks[k] = rank(rows, len(bydim[k]))
    betti = []
    for k in range(0, maxd + 1):
        nk = len(bydim.get(k, []))
        r_k = ranks.get(k, 0)        # rank of d_k
        r_k1 = ranks.get(k + 1, 0)   # rank of d_{k+1}
        betti.append((nk - r_k) - r_k1)
    return betti


# ---------------------------------------------------------------- driver
def analyze(N):
    primes, spammed, divisors = linear_circle_sieve(N)
    ok = (primes == [p for p in classic_primes(N)])
    faces = faces_upto(N, primes)
    fv = f_vector(faces)
    facets = facets_of(faces)
    betti = betti_numbers(faces)
    # facet size distribution
    from collections import Counter
    fsize = Counter(len(f) for f in facets)
    # recursion check: link of vertex {p} vs Delta_{N//p} minus p
    rec_ok = True
    vindex = {p: i for i, p in enumerate(primes)}
    for p in primes:
        if p * p > N:
            continue
        # link faces: S with p not in S, prod(S)*p <= N
        link = {f for f in faces if vindex[p] not in f
                and prod_of(f, primes) * p <= N}
        # Delta_{N//p} faces not containing p
        small = [q for q in primes if q <= N // p]
        small_faces = {f for f in faces_upto(N // p, small)
                       if vindex[p] not in {
                           # map local index back: small[j] global index
                           vindex[small[j]] for j in f}}
        # reindex small faces to global indices for comparison
        small_g = set()
        for f in faces_upto(N // p, small):
            g = tuple(vindex[small[j]] for j in f)
            if vindex[p] not in g:
                small_g.add(g)
        if link != small_g:
            rec_ok = False
            break
    return dict(N=N, nprimes=len(primes), sieve_ok=ok, fvec=fv,
                nfacets=len(facets), facet_sizes=dict(sorted(fsize.items())),
                betti=betti, recursion_ok=rec_ok)


def prod_of(f, primes):
    r = 1
    for j in f:
        r *= primes[j]
    return r


if __name__ == "__main__":
    for N in [30, 60, 100, 200, 500, 1000]:
        a = analyze(N)
        print(f"N={a['N']:5d}  primes={a['nprimes']:3d}  sieve==classic: {a['sieve_ok']}")
        print(f"   f-vector : {a['fvec']}")
        print(f"   facets   : {a['nfacets']}  sizes {a['facet_sizes']}")
        print(f"   betti    : {a['betti']}")
        print(f"   link recursion holds: {a['recursion_ok']}")
