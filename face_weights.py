#!/usr/bin/env python3
"""
Node 14 -- D4's positive-region half.

Exact identity: d/du [prod_{p<=z} (1 - p^{-u})]_{u=1}
              = sum_{S subset P_z} w(S)
              = delta(z) * sum_{p<=z} (log p)/(p-1),
where w(S) = (-1)^{|S|+1} log(prod S)/(prod S), delta(z)=prod(1-1/p).
Two proofs in DERIVATIONS.md (subset expansion; calculus).
K-theoretic home: ch(lambda_{-1}(E_z)) with equivariant Chern roots
-u*log p. As z->infty the total tends to e^{-gamma}.

Also: exact obstruction -- no ORDINARY positive geometry can carry
w(S) as stratum residues (logarithmic residues are +-1; |w({2})| =
(log 2)/2 is not). The refined home is the DIFFERENTIATED (stringy)
simplex: prime logs as exponents, u-derivative at u=1.
"""

import math

def primes_upto(n):
    s = bytearray(b'\x01')*(n+1); s[:2] = b'\x00\x00'
    for i in range(2, int(math.isqrt(n))+1):
        if s[i]: s[i*i:n+1:i] = b'\x00'*(((n - i*i)//i)+1)
    return [i for i, b in enumerate(s) if b]

def total_weight(z):
    # RHS of the identity: delta(z) * sum (log p)/(p-1)  (= sum_S w(S))
    ps = primes_upto(z)
    delta = 1.0; s = 0.0
    for p in ps:
        delta *= (1 - 1/p); s += math.log(p)/(p-1)
    return delta*s

zs = [2,3,5,7,11,13,17,19,23,29,50,100,500,1000,5000,20000,100000]
tot = [total_weight(z) for z in zs]
eg = math.exp(-0.5772156649015329)
for z, t in zip(zs, tot):
    print(f"z={z:6d}: sum_S w(S) = {t:.6f}")
print(f"e^-gamma = {eg:.6f}")

# figure: (a) total -> e^-gamma ; (b) |w(S)| vs |S| at z=29 (why the
# question was asked: alternating, residue-like decay -- yet +-1
# obstruction forbids the literal reading)
import itertools
ps = primes_upto(29)
bydim = {}
for r in range(1, len(ps)+1):
    vals = []
    for S in itertools.combinations(ps, r):
        prod = 1
        for p in S: prod *= p
        vals.append(((-1)**(r+1))*math.log(prod)/prod)
    bydim[r] = vals

import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
fig, axx = plt.subplots(1, 2, figsize=(13, 4.2))
axx[0].semilogx(zs, tot, 'o-', ms=4, label="sum_S w(S) = d/du prod(1-p^-u)|1")
axx[0].axhline(eg, color='k', ls='--', label="e^-gamma")
axx[0].set_xlabel("z"); axx[0].set_title("total face-weight -> e^-gamma")
axx[0].legend(fontsize=8)
for r, vals in bydim.items():
    axx[1].scatter([r]*len(vals), vals, s=6, alpha=0.5)
axx[1].axhline(0, color='k', lw=0.7)
axx[1].set_xlabel("|S| (face dimension+1)"); axx[1].set_ylabel("w(S)")
axx[1].set_title("w(S) at z=29: alternating, decaying -- but |w({2})|=0.347 != 1")
fig.tight_layout(); fig.savefig("face_weights.png", dpi=110)
print("figure -> face_weights.png")
