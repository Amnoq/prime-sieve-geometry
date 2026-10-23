#!/usr/bin/env python3
"""
Node 13e -- does the Fock spectrum's fluctuation know about the primes?

The zeros know about primes via the explicit formula: N_osc(T) oscillates
at frequencies (r log p)/(2 pi). Run it in reverse on our operator: take
the z=29 pair-hopping spectrum, subtract the smooth counting function,
Lomb-Scargle the residual, look for peaks at f_p = log(p)/(2 pi).

Controls: (1) a GUE random matrix of the same dimension -- the method
must show no prime peaks there; (2) our Hamiltonian with shuffled
weights -- tests whether peaks track the actual prime values.
Significance: z-score of power at prime frequencies vs the empirical
background over the frequency grid.
"""

import numpy as np, json

def analyze(E, label, deg=10):
    from scipy.signal import lombscargle
    n = np.arange(1, len(E) + 1)
    Nbar = np.polyval(np.polyfit(E, n, deg), E)
    res = n - Nbar
    lo, hi = int(0.10*len(E)), int(0.90*len(E))
    Eb, rb = E[lo:hi], res[lo:hi] - res[lo:hi].mean()
    freqs = np.linspace(0.02, 1.5, 4000)
    P = lombscargle(Eb, rb, 2*np.pi*freqs, normalize=True)
    return freqs, P, float(Eb[-1]-Eb[0])

def prime_freqs(z):
    import math
    s = bytearray(b'\x01')*(z+1); s[:2] = b'\x00\x00'
    for i in range(2, int(math.isqrt(z))+1):
        if s[i]: s[i*i:z+1:i] = b'\x00'*(((z - i*i)//i)+1)
    return [math.log(p)/(2*math.pi) for p in range(2, z+1) if s[p]]

def zscores(freqs, P, fp):
    bg = P.copy()
    for f in fp:                       # mask neighborhoods of prime freqs
        bg[(freqs > f-0.02) & (freqs < f+0.02)] = np.nan
    mu, sd = np.nanmean(bg), np.nanstd(bg)
    vals = [float(P[np.argmin(np.abs(freqs-f))]) for f in fp]
    return vals, [(v-mu)/sd for v in vals], mu, sd

def main():
    from fock_pairhop import build, primes_upto
    rng = np.random.default_rng(1)
    z = 29
    ps = primes_upto(z); w = np.log(ps)/ps
    Hb, Hp = build(z, w)
    lam0 = float(np.linalg.norm(Hb)/np.linalg.norm(Hp))
    E = np.linalg.eigvalsh(Hb + lam0*Hp)
    print(f"z=29 spectrum: dim={len(E)}, range=[{E[0]:.2f},{E[-1]:.2f}]")

    # GUE control, same dimension
    N = len(E)
    A = (rng.standard_normal((N, N)) + 1j*rng.standard_normal((N, N)))/np.sqrt(2)
    Eg = np.linalg.eigvalsh((A + A.conj().T)/2)

    # shuffled-weight control
    ws = rng.permutation(w)
    Hbs, Hps = build(z, ws)
    lam0s = float(np.linalg.norm(Hbs)/np.linalg.norm(Hps))
    Es = np.linalg.eigvalsh(Hbs + lam0s*Hps)

    fp = prime_freqs(z)
    print("prime freqs:", [f"{f:.3f}" for f in fp])
    out = {}
    cases = {"arith": E, "gue": Eg, "shuffled": Es}
    res = {}
    for label, Ev in cases.items():
        freqs, P, span = analyze(Ev, label)
        vals, zs, mu, sd = zscores(freqs, P, fp)
        res[label] = {"P_at_primes": vals, "z": zs,
                      "mean_z": float(np.mean(zs)), "max_z": float(np.max(zs))}
        print(f"{label}: mean z at prime freqs = {np.mean(zs):.2f}, "
              f"max z = {np.max(zs):.2f} (bg mu={mu:.4f} sd={sd:.4f})")
        out[label] = {"freqs": freqs.tolist(), "P": P.tolist()}
    json.dump({"fp": fp, "stats": res,
               "freqs": freqs.tolist(),
               "P_arith": out["arith"]["P"], "P_gue": out["gue"]["P"],
               "P_shuffled": out["shuffled"]["P"]},
              open("fock_primefreq.json", "w"))

    import matplotlib; matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, axx = plt.subplots(3, 1, figsize=(12, 9), sharex=True)
    for ax, label, ttl in zip(axx, ["arith", "gue", "shuffled"],
                              ["pair-hop H (arith weights), z=29",
                               "GUE control, dim=1024",
                               "pair-hop H, shuffled weights"]):
        ax.plot(out[label]["freqs"], out[label]["P"], lw=0.7)
        for f in fp:
            ax.axvline(f, color='r', alpha=0.35, lw=0.8)
        ax.set_title(f"{ttl}  (mean z at red lines: {res[label]['mean_z']:.2f})")
        ax.set_ylabel("norm. power")
    axx[-1].set_xlabel("frequency f  (prime lines: f = log p / 2pi)")
    fig.tight_layout(); fig.savefig("fock_primefreq.png", dpi=110)
    print("figure -> fock_primefreq.png")

if __name__ == "__main__":
    main()
