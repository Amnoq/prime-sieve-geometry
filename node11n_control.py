#!/usr/bin/env python3
"""
Node 11n -- geometry control for 11l: is the tone mechanism purely geometric?

11l showed tones at loop primes (log p_j loop lengths). Confound: the loops
were prime-labeled, so "orbits -> tones" vs "primes -> tones (for some
prime-specific reason)" are not distinguished.

This node: Kirchhoff rose, R=8 loops, lengths L_j RANDOM IRRATIONAL
(seeded, rejection-sampled so no loop frequency or low repetition sits
within 0.03 of any prime-power control frequency). No arithmetic enters.

DISCRIMINATING prediction: tones at the 8 loop lengths (+repetitions r=2,3),
SILENCE at all prime frequencies. GUE/shuffled controls flat.

If it passes, 11l is airtight: the mechanism is geometric, and the
prime-labeling is the zeta-specific fact, cleanly separated.
If primes still show tones -> rethink everything.

Status: COMPUTED 2026-10-05. Decision-tree entry: Node 11n.
"""
import numpy as np, json, math, sys
sys.path.insert(0, "/home/hatch/workspace/prime-sieve-geometry")
from fock_primefreq import analyze, zscores

R = 8
KMAX = 400.0
SEED = 7

def prime_power_freqs(limit=50):
    s = bytearray(b"\x01")*(limit+1); s[:2] = b"\x00\x00"
    for i in range(2, int(limit**0.5)+1):
        if s[i]:
            s[i*i:limit+1:i] = b"\x00"*(((limit-i*i)//i)+1)
    out = []
    for p in range(2, limit+1):
        if s[p]:
            rr = 1
            while p**rr <= limit:
                out.append(rr*math.log(p)/(2*math.pi))
                rr += 1
    return out

PRIME_FREQS = prime_power_freqs(50)
# All prime-power freqs are <= log(49)/(2pi) ~= 0.62. Loop lengths in
# [4.2, 6.0] put fundamentals in [0.67, 0.95] -- a virgin band -- and
# r=2,3 repetitions below 3.0. Separation is structural, not sampled.
rng = np.random.default_rng(SEED)
L = rng.uniform(4.2, 6.0, R)
LOOP_FREQS = [r*c/(2*math.pi) for c in L for r in (1, 2, 3)]
assert max(LOOP_FREQS) < 3.0
dmin = min(abs(f-g) for f in LOOP_FREQS for g in PRIME_FREQS)
assert dmin > 0.03, dmin
print(f"loop lengths: {np.round(L,4).tolist()}")
print(f"loop freq band: [{min(LOOP_FREQS):.3f},{max(LOOP_FREQS):.3f}], "
      f"prime band max: {max(PRIME_FREQS):.3f}, min separation: {dmin:.4f}")
Ltot = float(L.sum())

def analyze_wide(E, label, deg=10):
    from scipy.signal import lombscargle
    n = np.arange(1, len(E) + 1)
    Nbar = np.polyval(np.polyfit(E, n, deg), E)
    res = n - Nbar
    lo, hi = int(0.10*len(E)), int(0.90*len(E))
    Eb, rb = E[lo:hi], res[lo:hi] - res[lo:hi].mean()
    freqs = np.linspace(0.02, 3.0, 8000)
    P = lombscargle(Eb, rb, 2*np.pi*freqs, normalize=True)
    return freqs, P, float(Eb[-1]-Eb[0])

def G(k):
    k = np.atleast_1d(np.asarray(k, dtype=float))
    s = np.sin(k[None, :] * L[:, None] / 2)
    c = np.cos(k[None, :] * L[:, None] / 2)
    out = np.zeros(k.size)
    for j in range(R):
        m = np.ones(R, dtype=bool); m[j] = False
        out += s[j, :] * np.prod(c[m, :], axis=0)
    return out

def vertex_roots(kmax=KMAX, step=0.05):
    ks = np.arange(0.01, kmax, step)
    gv = G(ks)
    roots = []
    for i in range(len(ks)-1):
        if gv[i] == 0:
            roots.append(ks[i])
        elif gv[i]*gv[i+1] < 0:
            a, b, fa = ks[i], ks[i+1], gv[i]
            for _ in range(60):
                m = 0.5*(a+b)
                fm = float(G(np.array([m]))[0])
                if fa*fm <= 0: b = m
                else: a, fa = m, fm
            roots.append(0.5*(a+b))
    return np.array(roots)

def dirichlet_levels(kmax=KMAX):
    out = []
    for Lj in L:
        mmax = int(kmax*Lj/(2*math.pi))
        out.extend(2*math.pi*np.arange(1, mmax+1)/Lj)
    return np.array(out)

def main():
    print("vertex sector ...", flush=True)
    kv_ = vertex_roots(); print(f"  {len(kv_)} roots", flush=True)
    kd = dirichlet_levels(); print(f"  {len(kd)} Dirichlet levels", flush=True)
    E = np.sort(np.concatenate([kv_, kd]))
    keep = np.ones(len(E), dtype=bool); keep[1:] = np.diff(E) > 1e-9
    E = E[keep]
    print(f"merged: {len(E)} levels, k in [{E[0]:.3f},{E[-1]:.1f}]", flush=True)
    print(f"Weyl prediction: {(Ltot/math.pi)*KMAX:.0f}", flush=True)
    s = np.diff(E)
    r = np.minimum(s[:-1], s[1:])/np.maximum(s[:-1], s[1:])
    print(f"spacing ratio <r~> = {r.mean():.4f}", flush=True)

    fp_all = LOOP_FREQS + PRIME_FREQS
    n_loop = len(LOOP_FREQS)

    rng2 = np.random.default_rng(21)
    Nn = len(E)
    A = (rng2.standard_normal((Nn, Nn)) + 1j*rng2.standard_normal((Nn, Nn)))/np.sqrt(2)
    Eg = np.linalg.eigvalsh((A + A.conj().T)/2)
    Es = rng2.permutation(E)

    out = {}
    for label, Ev in [("graph", E), ("gue", Eg), ("shuffled", Es)]:
        freqs, P, span = analyze_wide(Ev, label)
        vals, zs, mu, sd = zscores(freqs, P, fp_all)
        z_loop = zs[:n_loop]; z_prime = zs[n_loop:]
        out[label] = {"mean_z_loop": float(np.mean(z_loop)),
                      "max_z_loop": float(np.max(z_loop)),
                      "mean_z_prime": float(np.mean(z_prime)),
                      "max_z_prime": float(np.max(z_prime)),
                      "z_loop": [float(z) for z in z_loop],
                      "z_prime": [float(z) for z in z_prime],
                      "freqs": freqs.tolist(), "P": P.tolist()}
        print(f"{label}: loop freqs mean z={out[label]['mean_z_loop']:.2f} "
              f"(max {out[label]['max_z_loop']:.2f}) | prime freqs mean z="
              f"{out[label]['mean_z_prime']:.2f} "
              f"(max {out[label]['max_z_prime']:.2f})", flush=True)

    json.dump({"loop_lengths": L.tolist(), "seed": SEED,
               "n_levels": len(E), "kmax": KMAX,
               "spacing_ratio": float(r.mean()),
               "stats": {k: {kk: v[kk] for kk in
                               ("mean_z_loop", "max_z_loop",
                                "mean_z_prime", "max_z_prime",
                                "z_loop", "z_prime")}
                         for k, v in out.items()},
               "loop_freqs": LOOP_FREQS, "prime_freqs": PRIME_FREQS,
               "freqs": out["graph"]["freqs"],
               "P_graph": out["graph"]["P"], "P_gue": out["gue"]["P"],
               "P_shuffled": out["shuffled"]["P"]},
              open("node11n_control.json", "w"))
    print("wrote node11n_control.json")

    import matplotlib; matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, axx = plt.subplots(3, 1, figsize=(12, 9), sharex=True)
    for ax, label, ttl in zip(axx, ["graph", "gue", "shuffled"],
                              ["random-length rose graph (R=8, Kirchhoff)",
                               "GUE control", "shuffled control"]):
        ax.plot(out[label]["freqs"], out[label]["P"], lw=0.7)
        for f in LOOP_FREQS:
            ax.axvline(f, color='g', alpha=0.35, lw=0.8)
        for f in PRIME_FREQS:
            ax.axvline(f, color='r', alpha=0.2, lw=0.6)
        ax.set_title(f"{ttl} (loop-freq mean z: "
                     f"{out[label]['mean_z_loop']:.2f}, prime-freq: "
                     f"{out[label]['mean_z_prime']:.2f})")
        ax.set_ylabel("norm. power")
    axx[-1].set_xlabel("frequency f (green=loop freqs, red=prime freqs)")
    fig.tight_layout(); fig.savefig("node11n_control.png", dpi=110)
    print("figure -> node11n_control.png")

if __name__ == "__main__":
    main()
