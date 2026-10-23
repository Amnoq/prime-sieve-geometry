#!/usr/bin/env python3
"""
Node 11a -- Berry-Keating xp operator on a toroidal lattice, vs the Berry tones.

Operator: H = (x p + p x)/2, symmetrized Berry-Keating. Discretized on a
finite 1D lattice x_j = x0 + j*a (x0 = BK small-x cutoff), with p the
Fourier (periodic = toroidal) derivative. This is the 1D toroidal building
block of the letter's T^3 proposal: if the building block carries no prime
tones, sums of it cannot either. The T^3 sum spectrum (E_ijk = e_i+e_j+e_k)
is tested as a secondary panel, computed directly from the 1D eigenvalues.

Probe: Node 13e machinery (fock_primefreq.analyze / zscores): subtract the
smooth counting function, Lomb-Scargle the residual, z-scores of power at
f = r*log(p)/(2*pi) for prime powers p^r <= 50 (covers the measured tones
r=1: p=2,3,5,7; r=2: p=2,3; r=3: p=2).

Controls: (1) GUE matrix, same dimension -- the method must show no prime
peaks; (2) shuffled BK spectrum -- same level density, correlations
destroyed (the letter's loaded control).

Falsification (per the toroidal phonon letter): tones absent, GUE-only
fluctuations -> the operator is rejected as the spectral realization.

Status: COMPUTED 2026-10-05. See letter TOROIDAL_PHONON_LETTER_2026-10-05.md.
"""
import numpy as np, json, math, sys
sys.path.insert(0, "/home/hatch/workspace/prime-sieve-geometry")
from fock_primefreq import analyze, zscores

def prime_power_freqs(limit=50):
    s = bytearray(b"\x01") * (limit + 1); s[:2] = b"\x00\x00"
    for i in range(2, int(limit ** 0.5) + 1):
        if s[i]:
            s[i*i:limit+1:i] = b"\x00" * (((limit - i*i)//i) + 1)
    out = []
    for p in range(2, limit + 1):
        if s[p]:
            r = 1
            while p ** r <= limit:
                out.append((p, r, r * math.log(p) / (2 * math.pi)))
                r += 1
    return out

def build_bk(N=3000, x0=0.5, a=0.05):
    x = x0 + a * np.arange(N)
    k = 2 * np.pi * np.fft.fftfreq(N, a)          # toroidal momentum
    V = np.fft.fft(np.eye(N)) / np.sqrt(N)
    P = (V * k) @ V.conj().T
    X = np.diag(x)
    H = 0.5 * (X @ P + P @ X)
    asym = np.linalg.norm(H - H.conj().T) / np.linalg.norm(H)
    return H, asym

def spacing_ratio(E):
    s = np.diff(np.sort(E)); s = s[s > 1e-12]
    r = np.minimum(s[:-1], s[1:]) / np.maximum(s[:-1], s[1:])
    return float(np.mean(r))  # GUE ~0.536, Poisson ~0.386

def probe_case(E, label, fp):
    freqs, P, span = analyze(E, label)
    fvals = [f for (_, _, f) in fp]
    vals, zs, mu, sd = zscores(freqs, P, fvals)
    # also per-(p,r) detail for the letter's measured tones
    detail = {}
    for (p, r, f) in fp:
        i = int(np.argmin(np.abs(freqs - f)))
        detail[f"({p},{r})"] = {"z": float((P[i] - mu) / sd)}
    return {"mean_z": float(np.mean(zs)), "max_z": float(np.max(zs)),
            "bg_mu": mu, "bg_sd": sd, "detail": detail,
            "freqs": freqs.tolist(), "P": P.tolist()}

def main():
    rng = np.random.default_rng(7)
    N = 3000
    print("building H = (xp+px)/2 ...", flush=True)
    H, asym = build_bk(N)
    print(f"Hermiticity rel-asymmetry: {asym:.2e}")
    E = np.linalg.eigvalsh(H)
    print(f"spectrum: dim={len(E)}, range=[{E[0]:.1f},{E[-1]:.1f}], "
          f"positive={(E > 0).sum()}", flush=True)
    print(f"spacing ratio <r~> = {spacing_ratio(E):.4f} "
          f"(GUE 0.536 / Poisson 0.386)")

    fp = prime_power_freqs(50)
    print(f"prime-power frequencies: {len(fp)} lines "
          f"(p^r<=50), e.g. (2,1):{fp[0][2]:.3f} (2,2):{fp[1][2]:.3f} "
          f"(2,3):{fp[2][2]:.3f}")

    # GUE control, same dimension
    A = (rng.standard_normal((N, N)) + 1j * rng.standard_normal((N, N))) / np.sqrt(2)
    Eg = np.linalg.eigvalsh((A + A.conj().T) / 2)
    # shuffled control: same levels, correlations destroyed
    Es = rng.permutation(E)

    out = {}
    for label, Ev in [("bk", E), ("gue", Eg), ("shuffled", Es)]:
        r = probe_case(Ev, label, fp)
        out[label] = r
        d = r["detail"]
        tones = " ".join(f"{k} z={v['z']:.2f}" for k, v in d.items()
                         if k in ("(2,1)", "(3,1)", "(5,1)", "(7,1)",
                                  "(2,2)", "(3,2)", "(2,3)"))
        print(f"{label}: mean z at prime-power freqs = {r['mean_z']:.2f}, "
              f"max z = {r['max_z']:.2f}")
        print(f"   letter tones: {tones}")

    # --- secondary panel: T^3 sum spectrum from positive 1D levels ---
    Ep = np.sort(E[E > 0])
    M = 150
    e = Ep[-M:]                      # top-M positive levels
    S = np.add.outer(np.add.outer(e, e), e).ravel()
    S.sort()
    print(f"T^3-sum spectrum: {len(S)} levels from top-{M} 1D positives, "
          f"range=[{S[0]:.1f},{S[-1]:.1f}]", flush=True)
    r3 = probe_case(S, "t3sum", fp)
    out["t3sum"] = r3
    print(f"t3sum: mean z = {r3['mean_z']:.2f}, max z = {r3['max_z']:.2f}")

    json.dump({"prime_power_freqs": [(p, r, f) for (p, r, f) in fp],
               "stats": {k: {kk: v for kk, v in v.items()
                             if kk in ("mean_z", "max_z", "bg_mu", "bg_sd",
                                       "detail")} for k, v in out.items()},
               "freqs": out["bk"]["freqs"],
               "P_bk": out["bk"]["P"], "P_gue": out["gue"]["P"],
               "P_shuffled": out["shuffled"]["P"],
               "P_t3sum": out["t3sum"]["P"],
               "hermiticity_asym": asym,
               "spacing_ratio": spacing_ratio(E),
               "N": N},
              open("node11a_bk.json", "w"))
    print("wrote node11a_bk.json")

    import matplotlib; matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, axx = plt.subplots(4, 1, figsize=(12, 11), sharex=True)
    flines = [f for (_, _, f) in fp]
    for ax, label, ttl in zip(axx, ["bk", "gue", "shuffled", "t3sum"],
                              ["BK (xp+px)/2, N=3000 lattice",
                               "GUE control", "shuffled BK control",
                               "T^3 sum spectrum (secondary)"]):
        ax.plot(out[label]["freqs"], out[label]["P"], lw=0.7)
        for f in flines:
            ax.axvline(f, color='r', alpha=0.25, lw=0.8)
        ax.set_title(f"{ttl}  (mean z at red lines: "
                     f"{out[label]['mean_z']:.2f})")
        ax.set_ylabel("norm. power")
    axx[-1].set_xlabel("frequency f  (prime-power lines: f = r log p / 2pi)")
    fig.tight_layout(); fig.savefig("node11a_bk.png", dpi=110)
    print("figure -> node11a_bk.png")

if __name__ == "__main__":
    main()
