#!/usr/bin/env python3
"""
Node 13 -- fermionic Fock fork: an arithmetic operator from the sieve's
own materials.

EXACT identification: faces S of Delta_z (subsets of primes <= z) are the
fermionic Fock basis over primes (each prime used at most once = Pauli;
squarefree kernel). Mu = (-1)^F (fermion parity). Face adjacency
(S <-> S+{p}) is fermionic hopping.

H_2 = sum_p (log p / p) (a_p^dag + a_p): one-body hopping with the
prime terms of -zeta'/zeta. KILLED BY INSPECTION: the terms commute
([O_p, O_q] = 0, O_p^2 = 1), so the spectrum is EXACTLY
{sum_p +/- (log p)/p} -- integrable, not chaotic. No zero statistics.
Verified below against dense diagonalization.

H_int = H_2 + sum_{p<q} (log p log q)/(pq) n_p n_q: minimal interacting
native Hamiltonian. One-body = prime terms of zeta'/zeta; two-body =
semiprime terms of (zeta'/zeta)^2. Self-adjoint, no symmetries.
Probe: bulk level statistics (r-statistic, spacing histogram) vs
Poisson <r>=0.386 / GUE <r>=0.536. GUE-like would put the sieve's own
operator in the zeros' universality class; Poisson is another kill.
"""

import numpy as np, json

def primes_upto(n):
    s = bytearray(b'\x01')*(n+1); s[:2] = b'\x00\x00'
    import math
    for i in range(2, int(math.isqrt(n))+1):
        if s[i]: s[i*i:n+1:i] = b'\x00'*(((n - i*i)//i)+1)
    return [i for i, b in enumerate(s) if b]

def build_H(z, interacting=True):
    ps = np.array(primes_upto(z), dtype=float); m = len(ps)
    N = 1 << m
    c = np.log(ps)/ps
    H = np.zeros((N, N))
    idx = np.arange(N)
    for i in range(m):                       # hopping: flip bit i
        H[idx, idx ^ (1 << i)] += c[i]
    if interacting:                          # density-density, diagonal
        bits = ((idx[:, None] >> np.arange(m)) & 1).astype(float)
        wb = bits @ c
        H[np.diag_indices(N)] += (wb*wb - bits @ (c*c))/2
    return H, ps

def r_stat(e):
    s = np.diff(np.sort(e)); s = s[s > 1e-12]
    r = np.minimum(s[:-1], s[1:])/np.maximum(s[:-1], s[1:])
    return float(np.mean(r)), s

# ---- H_2 exact spectrum vs dense diagonalization (sanity)
H2, ps = build_H(13, interacting=False)
e_dense = np.linalg.eigvalsh(H2)
m = len(ps); c = np.log(ps)/ps; N = 1 << m
bits = ((np.arange(N)[:, None] >> np.arange(m)) & 1).astype(float)
e_exact = np.sort(bits @ (2*c) - c.sum())
print(f"H_2 z=13: max|dense-exact| = {np.max(np.abs(e_dense-e_exact)):.2e}")
r2, s2 = r_stat(e_exact)
print(f"H_2 <r> = {r2:.3f} (Poisson 0.386, GUE 0.536)")

# ---- H_int across z
res = {}
for z in [13, 17, 19, 23, 29]:
    H, ps = build_H(z, interacting=True)
    e = np.linalg.eigvalsh(H)
    r, s = r_stat(e)
    res[z] = {"dim": int(len(e)), "r": r}
    print(f"H_int z={z}: dim={len(e)}, <r>={r:.3f}")

# figure: H_2 spacings vs H_int spacings at z=29 vs Poisson/Wigner
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
H, _ = build_H(29, interacting=True)
_, sint = r_stat(np.linalg.eigvalsh(H))
fig, axx = plt.subplots(1, 3, figsize=(15, 4.2))
x = np.linspace(0, 3, 200)
poisson = np.exp(-x); wigner = (np.pi*x/2)*np.exp(-np.pi*x*x/4)
axx[0].hist(s2/np.mean(s2), bins=60, range=(0,3), density=True, alpha=.7,
            label="H_2 (exact)")
axx[0].plot(x, poisson, 'k--', label="Poisson"); axx[0].plot(x, wigner, 'k:')
axx[0].set_title("H_2 spacings: integrable"); axx[0].legend(fontsize=8)
axx[1].hist(sint/np.mean(sint), bins=60, range=(0,3), density=True, alpha=.7,
            label="H_int z=29")
axx[1].plot(x, poisson, 'k--', label="Poisson"); axx[1].plot(x, wigner, 'k:',
            label="Wigner (GUE)")
axx[1].set_title("H_int spacings"); axx[1].legend(fontsize=8)
zs = sorted(res); rs = [res[z]["r"] for z in zs]
axx[2].plot(zs, rs, 'o-', label="<r> H_int")
axx[2].axhline(0.386, color='k', ls='--', label="Poisson 0.386")
axx[2].axhline(0.536, color='k', ls=':', label="GUE 0.536")
axx[2].set_xlabel("z"); axx[2].set_title("r-statistic vs z")
axx[2].legend(fontsize=8)
fig.tight_layout(); fig.savefig("fock_probe.png", dpi=110)
print("figure -> fock_probe.png")
json.dump(res, open("fock_probe.json","w"), indent=1)
