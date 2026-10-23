#!/usr/bin/env python3
"""
Node 13d -- off-diagonal two-body pair hopping on the sieve's Fock space.

13c's verdict: the density-density interaction is Fock-diagonal (shifts
energies, no transitions); all mixing came from the integrable one-body
hopping. This probe adds the minimal MIXING term:

  H_pair = sum_{p,q,r,s} w_p w_q w_r w_s a_p^dag a_q^dag a_r a_s

(number-conserving pair hop {r,s} -> {p,q}, arithmetically weighted with
w_p = (log p)/p, the zeta'/zeta prime weights). Full Hamiltonian:

  H(lam) = H_2 + H_diag + lam * H_pair

H_2 = one-body hopping (13b), H_diag = (log p log q)/(pq) n_p n_q (13c).
lam_0 is fixed by ||lam_0 H_pair||_F = ||H_2 + H_diag||_F (mixing carries
the same total weight as the native terms -- parameter-free baseline),
then lam is scanned around it. Control: same build with shuffled
weights (arithmetic vs generic-random). Probe: bulk r-statistic vs
Poisson 0.386 / GUE 0.536, spacing histograms.
"""

import numpy as np, json

def primes_upto(n):
    s = bytearray(b'\x01')*(n+1); s[:2] = b'\x00\x00'
    import math
    for i in range(2, int(math.isqrt(n))+1):
        if s[i]: s[i*i:n+1:i] = b'\x00'*(((n - i*i)//i)+1)
    return [i for i, b in enumerate(s) if b]

def par_below(mask, x):
    return bin(mask & ((1 << x) - 1)).count('1') & 1

def build(z, w):
    ps = primes_upto(z); m = len(ps); N = 1 << m
    w = np.asarray(w, float)
    Hbase = np.zeros((N, N)); Hpair = np.zeros((N, N))
    idx = np.arange(N)
    for i in range(m):                       # H_2 one-body hopping
        Hbase[idx, idx ^ (1 << i)] += w[i]
    bits = ((idx[:, None] >> np.arange(m)) & 1).astype(float)
    wb = bits @ w                            # H_diag density-density
    Hbase[np.diag_indices(N)] += (wb*wb - bits @ (w*w))/2
    for a in range(N):                       # pair hopping, canonical order
        occ = [i for i in range(m) if (a >> i) & 1]   # (prevents the
        emp = [i for i in range(m) if not (a >> i) & 1]  # symmetric-weight
        for ii in range(len(occ)):                   # cancellation:
            for jj in range(ii+1, len(occ)):         # a_r a_s = -a_s a_r)
                r, s = occ[ii], occ[jj]              # r < s, P_{rs} = a_s a_r
                a1 = a ^ (1 << r)
                a2 = a1 ^ (1 << s)
                sgn_rs = par_below(a, r) ^ par_below(a1, s)
                wrs = w[r]*w[s]
                for kk in range(len(emp)):
                    for ll in range(kk+1, len(emp)):
                        p, q = emp[kk], emp[ll]      # p < q, add q then p
                        a3 = a2 | (1 << q)
                        b = a3 | (1 << p)
                        sgn = sgn_rs ^ par_below(a2, q) ^ par_below(a3, p)
                        Hpair[a, b] += wrs*w[p]*w[q]*(-1.0 if sgn else 1.0)
    return Hbase, Hpair

def r_stat(e):
    s = np.diff(np.sort(e)); s = s[s > 1e-12]
    r = np.minimum(s[:-1], s[1:])/np.maximum(s[:-1], s[1:])
    return float(np.mean(r)), s/np.mean(s)

if __name__ == "__main__":
    rng = np.random.default_rng(0)
    out = {}
    for z in [13, 17, 19, 23, 29]:
        ps = primes_upto(z); w = np.log(ps)/ps
        Hb, Hp = build(z, w)
        lam0 = float(np.linalg.norm(Hb)/np.linalg.norm(Hp))
        out[z] = {"dim": Hb.shape[0], "lam0": lam0, "lam_mult": {}}
        for mult in [0.25, 0.5, 1.0, 2.0, 4.0]:
            r, _ = r_stat(np.linalg.eigvalsh(Hb + mult*lam0*Hp))
            out[z]["lam_mult"][mult] = r
            print(f"z={z} mult={mult}: <r>={r:.3f}", flush=True)

    # control: shuffled weights at z=29, mult=1
    ps = primes_upto(29); w = np.log(ps)/ps
    ws = rng.permutation(w)
    Hb, Hp = build(29, ws)
    lam0 = float(np.linalg.norm(Hb)/np.linalg.norm(Hp))
    rc, sc = r_stat(np.linalg.eigvalsh(Hb + lam0*Hp))
    out["control_shuffled"] = {"r": rc}
    print(f"control (shuffled weights) z=29 mult=1: <r>={rc:.3f}")

    # figure
    import matplotlib; matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    x = np.linspace(0, 3, 200)
    poisson = np.exp(-x); wigner = (np.pi*x/2)*np.exp(-np.pi*x*x/4)
    fig, axx = plt.subplots(1, 2, figsize=(12, 4.2))
    for mult in [0.25, 0.5, 1.0, 2.0, 4.0]:
        zs = [z for z in out if isinstance(z, int)]
        axx[0].plot(zs, [out[z]["lam_mult"][mult] for z in zs], 'o-',
                    label=f"lam={mult}x")
    axx[0].axhline(0.386, color='k', ls='--', label="Poisson")
    axx[0].axhline(0.536, color='k', ls=':', label="GUE")
    axx[0].set_xlabel("z"); axx[0].set_title("<r> vs z, pair-hopping strength")
    axx[0].legend(fontsize=8)
    ps = primes_upto(29); w = np.log(ps)/ps
    Hb, Hp = build(29, w)
    lam0 = float(np.linalg.norm(Hb)/np.linalg.norm(Hp))
    _, s29 = r_stat(np.linalg.eigvalsh(Hb + lam0*Hp))
    axx[1].hist(s29, bins=60, range=(0, 3), density=True, alpha=.7,
                label="H z=29 lam=lam0")
    axx[1].plot(x, poisson, 'k--', label="Poisson")
    axx[1].plot(x, wigner, 'k:', label="Wigner (GUE)")
    axx[1].set_title("spacings, z=29"); axx[1].legend(fontsize=8)
    fig.tight_layout(); fig.savefig("fock_pairhop.png", dpi=110)
    json.dump(out, open("fock_pairhop.json", "w"), indent=1)
    print("figure -> fock_pairhop.png")
