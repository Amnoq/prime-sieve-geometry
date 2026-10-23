#!/usr/bin/env python3
"""K-tuple deformation sweep: is the deformation a GENERAL generative machine?

For each prime constellation H (admissible) plus one non-admissible control:
  (a) survivors of the deformed sieve at z=sqrt(x+maxH) == constellation lowers
      exactly (soundness + completeness, independently enumerated)
  (b) finite-z density S(x,z0)/x vs delta_H(z0) = prod_{p<=z0}(1-nu_p/p)
  (c) renormalized weight S_H(z) = prod(1-nu_p/p)/(1-1/p)^k vs reference

The deformation: mark n if exists p<=z, h in H with (n+h) a PROPER multiple of p.
(i.e. simultaneous Eratosthenes on the k linear forms n+h_i)
"""
import math, time, json

def sieve_bs(n):
    bs = bytearray(b'\x01')*(n+1)
    if n >= 0: bs[0]=0
    if n >= 1: bs[1]=0
    for i in range(2,int(n**0.5)+1):
        if bs[i]:
            bs[i*i:n+1:i] = b'\x00'*(((n - i*i)//i)+1)
    return bs

def primes_upto(n):
    bs = sieve_bs(n)
    return [i for i in range(2,n+1) if bs[i]]

def deformed_marked(H, x, z):
    """marked[0..x]=1 iff exists p<=z, h in H with (n+h) a proper multiple of p."""
    marked = bytearray(x+1)
    for p in primes_upto(z):
        for h in H:
            r = (-h) % p
            lo = 2*p - h          # need n+h >= 2p (proper multiple)
            start = r
            if start < lo:
                start += ((lo - start + p - 1)//p)*p
            if start > x:
                continue
            cnt = (x - start)//p + 1
            marked[start::p] = b'\x01'*cnt
    return marked

def nu_p(H, p):
    return len(set(h % p for h in H))

def main():
    X = 10**6
    Z0 = 30
    tuples = {
        'twin {0,2}': [0,2],
        'cousin {0,4}': [0,4],
        'sexy {0,6}': [0,6],
        'tripletA {0,2,6}': [0,2,6],
        'tripletB {0,4,6}': [0,4,6],
        'quad {0,2,6,8}': [0,2,6,8],
        'quint {0,2,6,8,12}': [0,2,6,8,12],
        'sext {0,4,6,10,12,16}': [0,4,6,10,12,16],
        'NONADMISSIBLE {0,2,4}': [0,2,4],
    }
    primes100k = primes_upto(100000)
    results = {}
    t_start = time.time()
    for name, H in tuples.items():
        maxH = max(H)
        k = len(H)
        z = int(math.isqrt(X + maxH)) + 1
        # (a) survivors vs independent constellation enumeration
        marked = deformed_marked(H, X, z)
        survivors = set(n for n in range(2, X+1) if not marked[n])
        pbs = sieve_bs(X + maxH)
        lowers = set(q for q in range(2, X+1)
                     if pbs[q] and all(pbs[q+h] for h in H))
        unsound = sorted(survivors - lowers)
        incomplete = sorted(lowers - survivors)
        # (b) finite-z density
        marked0 = deformed_marked(H, X, Z0)
        cnt0 = sum(1 for n in range(2, X+1) if not marked0[n])
        obs_density = cnt0 / X
        delta = 1.0
        for p in primes_upto(Z0):
            delta *= (1 - nu_p(H, p)/p)
        # (c) renormalized weight at several z + reference product
        renorm = {}
        for zz in (30, 100, 300, 1000, 10000):
            num = 1.0; den = 1.0
            for p in primes100k:
                if p > zz: break
                num *= (1 - nu_p(H, p)/p)
                den *= (1 - 1/p)**k
            renorm[zz] = num/den if den else 0.0
        ref = renorm[10000]
        results[name] = {
            'n_survivors': len(survivors),
            'n_lowers': len(lowers),
            'exact_match': (not unsound and not incomplete),
            'unsound_head': unsound[:8],
            'incomplete_head': incomplete[:8],
            'obs_density_z30': obs_density,
            'delta_z30': delta,
            'density_ratio': (obs_density/delta) if delta else None,
            'renorm': renorm,
            'ref_singular': ref,
        }
        dr = results[name]['density_ratio']
        drs = f"{dr:.6f}" if dr is not None else "n/a (delta=0)"
        print(f"{name}: surv={len(survivors)} lowers={len(lowers)} "
              f"exact={results[name]['exact_match']} dens_ratio={drs} "
              f"S(1000)={renorm[1000]:.6f} ref={ref:.6f}", flush=True)
    print(f"total {time.time()-t_start:.1f}s", flush=True)
    with open('ktuple_results.json','w') as f:
        json.dump(results, f, indent=1)

if __name__ == '__main__':
    main()
