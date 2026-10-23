#!/usr/bin/env python3
"""
Node 11i -- Sierra-Rodriguez-Laguna deformed xp vs the Berry tones.

The regularization node: the published self-adjoint xp-variant, implemented
FAITHFULLY from the primary source (arXiv:1102.5356, PRL 106, 200201 (2011)),
not from paraphrase.

  Classical : H = x(p + l_p^2/p), x >= l_x                     (eq.3)
  Quantum   : Hh = x^{1/2}(ph + l_p^2/ph^{-1})x^{1/2}          (eq.8)
  BC        : nonlocal, U(1) family parameterized by angle th  (eq.11)
  Spectrum  : roots E_n of                                       (eq.14)
    Xh(E) = e^{-ith/2} K_{1/2+iE/2}(2pi) + e^{+ith/2} K_{1/2-iE/2}(2pi) = 0
  with h = l_x*l_p = 2*pi*hbar, hbar = 1, th = pi/4
  (the paper's Riemann-zero-matching choice; half-integer rule).

  Xh(E) = 2 Re[e^{-ith/2} K_{1/2+iE/2}(2pi)] is real; roots in +/- pairs.
  K-Bessel via mpmath (complex order; scipy kv has no complex-order ufunc).

Tests:
  (a) smooth counting N(E) vs Riemann-von Mangoldt and vs the paper's
      asymptotic (eq.16) -- does the PRL's Fig.3 claim hold computationally?
  (b) Berry tones: Node 13e probe on the positive roots -- prime-power
      frequencies f = r log p / 2pi, z-scores, GUE + shuffled controls.

Status: COMPUTED 2026-10-05. Decision-tree entry: Node 11i.
"""
import numpy as np, json
from mpmath import mp, besselk, pi as mpi
mp.dps = 30

TH = mpi/4
PHASE = mp.exp(mp.mpc(0, -TH/2))
ZARG = 2*mpi

def Xi(E):
    E = mp.mpf(E)
    K = besselk(mp.mpc(mp.mpf('0.5'), mp.mpf('0.5')*E), ZARG)
    return 2*(PHASE*K).real

def find_roots(E_max=2000.0, step=0.25):
    n = int(E_max/step)+1
    Egrid = [i*step for i in range(n+1)]
    vals = [Xi(e) for e in Egrid]
    roots = []
    for i in range(n):
        a, b, fa, fb = Egrid[i], Egrid[i+1], vals[i], vals[i+1]
        if fa == 0:
            roots.append(mp.mpf(a))
        elif fa*fb < 0:
            lo, hi, flo = mp.mpf(a), mp.mpf(b), fa
            for _ in range(40):
                mid = (lo+hi)/2
                fm = Xi(mid)
                if flo*fm <= 0:
                    hi = mid
                else:
                    lo, flo = mid, fm
            roots.append((lo+hi)/2)
    return roots

def main():
    print("scanning Xi(E) for roots ...", flush=True)
    roots = find_roots()
    E = np.array([float(r) for r in roots])
    E = E[E > 0]
    print(f"positive roots below 2000: {len(E)}, "
          f"first={E[0]:.4f}, last={E[-1]:.2f}", flush=True)

    # --- (a) smooth counting vs Riemann and vs paper asymptotic (16) ---
    # Riemann-von Mangoldt smooth:
    def N_riem(t):
        return (t/(2*np.pi))*(np.log(t/(2*np.pi))-1) + 7/8
    # paper (16) with h=2pi, th=pi/4: n = E/2pi*log(E/4pi e) - 5/8
    def N_sierra(t):
        return (t/(2*np.pi))*np.log(t/(4*np.pi*np.e)) - 5/8
    print("  E    N(E)   Riemann  Sierra(16)")
    for T in [100, 500, 1000, 2000]:
        n = int((E <= T).sum())
        print(f"  {T:4d}  {n:4d}   {N_riem(T):7.1f}  {N_sierra(T):7.1f}")

    # --- (b) tone probe ---
    import sys
    sys.path.insert(0, "/home/hatch/workspace/prime-sieve-geometry")
    from fock_primefreq import analyze, zscores
    import math
    def prime_power_freqs(limit=50):
        s = bytearray(b"\x01")*(limit+1); s[:2] = b"\x00\x00"
        for i in range(2, int(limit**0.5)+1):
            if s[i]:
                s[i*i:limit+1:i] = b"\x00"*(((limit-i*i)//i)+1)
        out = []
        for p in range(2, limit+1):
            if s[p]:
                r = 1
                while p**r <= limit:
                    out.append((p, r, r*math.log(p)/(2*math.pi)))
                    r += 1
        return out
    fp = prime_power_freqs(50)
    fvals = [f for (_, _, f) in fp]

    rng = np.random.default_rng(11)
    N = len(E)
    A = (rng.standard_normal((N, N)) + 1j*rng.standard_normal((N, N)))/np.sqrt(2)
    Eg = np.linalg.eigvalsh((A + A.conj().T)/2)
    Es = rng.permutation(E)

    out = {}
    for label, Ev in [("sierra", E), ("gue", Eg), ("shuffled", Es)]:
        freqs, P, span = analyze(Ev, label)
        vals, zs, mu, sd = zscores(freqs, P, fvals)
        detail = {}
        for (p, r, f) in fp:
            i = int(np.argmin(np.abs(freqs-f)))
            detail[f"({p},{r})"] = {"z": float((P[i]-mu)/sd)}
        out[label] = {"mean_z": float(np.mean(zs)), "max_z": float(np.max(zs)),
                      "detail": detail, "freqs": freqs.tolist(),
                      "P": P.tolist()}
        d = detail
        tones = " ".join(f"{k} z={v['z']:.2f}" for k, v in d.items()
                         if k in ("(2,1)","(3,1)","(5,1)","(7,1)",
                                  "(2,2)","(3,2)","(2,3)"))
        print(f"{label}: mean z = {out[label]['mean_z']:.2f}, "
              f"max z = {out[label]['max_z']:.2f}")
        print(f"   letter tones: {tones}")

    json.dump({"roots": E.tolist(),
               "counting": {"E": [100,500,1000,2000],
                            "N": [int((E<=T).sum()) for T in [100,500,1000,2000]],
                            "N_riem": [float(N_riem(T)) for T in [100,500,1000,2000]],
                            "N_sierra16": [float(N_sierra(T)) for T in [100,500,1000,2000]]},
               "stats": {k: {"mean_z": v["mean_z"], "max_z": v["max_z"],
                             "detail": v["detail"]} for k, v in out.items()},
               "freqs": out["sierra"]["freqs"],
               "P_sierra": out["sierra"]["P"], "P_gue": out["gue"]["P"],
               "P_shuffled": out["shuffled"]["P"]},
              open("node11i_sierra.json", "w"))
    print("wrote node11i_sierra.json")

    import matplotlib; matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, axx = plt.subplots(3, 1, figsize=(12, 9), sharex=True)
    flines = [f for (_, _, f) in fp]
    for ax, label, ttl in zip(axx, ["sierra", "gue", "shuffled"],
                              ["Sierra deformed xp, th=pi/4 (positive roots)",
                               "GUE control", "shuffled control"]):
        ax.plot(out[label]["freqs"], out[label]["P"], lw=0.7)
        for f in flines:
            ax.axvline(f, color='r', alpha=0.25, lw=0.8)
        ax.set_title(f"{ttl} (mean z: {out[label]['mean_z']:.2f})")
        ax.set_ylabel("norm. power")
    axx[-1].set_xlabel("frequency f (prime-power lines: r log p / 2pi)")
    fig.tight_layout(); fig.savefig("node11i_sierra.png", dpi=110)
    print("figure -> node11i_sierra.png")

if __name__ == "__main__":
    main()
