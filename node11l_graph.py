#!/usr/bin/env python3
"""
Node 11l -- prime-orbit quantum graph: does the orbit mechanism make tones?

Berry-Keating's epitaph for xp: "for H, there is a single primitive
periodic orbit for each energy E; for the zeta function there is a family
of primitive orbits labelled by primes p, with periods log p."
This node tests whether that missing mechanism -- prime-labeled closed
orbits -- actually produces prime tones in a spectrum.

Construction (Kirchhoff rose graph):
  R=8 loops, loop j has length L_j = log p_j, p_j = 2,3,5,7,11,13,17,19.
  Kirchhoff (Neumann) matching at the single central vertex.
  Closed orbits: loop traversals (length log p_j), repetitions
  (r*log p_j), concatenations (log m, m composite, suppressed by 1/R
  per vertex visit).

Spectrum (two sectors):
  (a) vertex sector: roots of G(k) = sum_j sin(kL_j/2)*prod_{i!=j}cos(kL_i/2)
      = 0  [smooth; = (prod cos)*sum tan, poles removed]. k>0.
  (b) loop-Dirichlet sector: k = 2*pi*m/L_j (exact picket fences).

Trace-formula prediction: N_osc(k) carries cos(k*r*log p_j) tones.
DISCRIMINATING test: loop primes are 2..19; probe prime powers p^r<=50
include NON-loop primes 23,29,31,37,41,43,47 (r=1 only). Tones must
appear at 2..19 (+powers) and NOT at 23+.

Honesty safeguards: primes enter only as loop lengths (geometry);
the spectrum is computed independently via the secular equation;
tone AMPLITUDES/pattern are the output under test. This also serves as
the POSITIVE control for the tone probe (validating the 11g/11i
negatives).

Status: COMPUTED 2026-10-05. Decision-tree entry: Node 11l.
"""
import numpy as np, json, math, sys
sys.path.insert(0, "/home/hatch/workspace/prime-sieve-geometry")
from fock_primefreq import analyze, zscores

PRIMES_LOOP = [2, 3, 5, 7, 11, 13, 17, 19]
L = np.array([math.log(p) for p in PRIMES_LOOP])
R = len(L)
Ltot = float(L.sum())
KMAX = 400.0

def G(k):
    """Secular function (smooth): sum_j sin(kL_j/2) prod_{i!=j} cos(kL_i/2)."""
    k = np.atleast_1d(np.asarray(k, dtype=float))
    s = np.sin(k[None, :] * L[:, None] / 2)   # (R, Nk)
    c = np.cos(k[None, :] * L[:, None] / 2)   # (R, Nk)
    out = np.zeros(k.size)
    for j in range(R):
        m = np.ones(R, dtype=bool)
        m[j] = False
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
                if fa*fm <= 0:
                    b = m
                else:
                    a, fa = m, fm
            roots.append(0.5*(a+b))
    return np.array(roots)

def dirichlet_levels(kmax=KMAX):
    out = []
    for Lj in L:
        mmax = int(kmax*Lj/(2*math.pi))
        out.extend(2*math.pi*np.arange(1, mmax+1)/Lj)
    return np.array(out)

def main():
    print("vertex sector (secular roots) ...", flush=True)
    kv_ = vertex_roots()
    print(f"  {len(kv_)} roots", flush=True)
    kd = dirichlet_levels()
    print(f"  {len(kd)} Dirichlet levels", flush=True)
    E = np.sort(np.concatenate([kv_, kd]))
    # dedupe
    keep = np.ones(len(E), dtype=bool)
    keep[1:] = np.diff(E) > 1e-9
    E = E[keep]
    print(f"merged spectrum: {len(E)} levels, k in [{E[0]:.3f},{E[-1]:.1f}]",
          flush=True)
    print(f"Weyl prediction: {(Ltot/math.pi)*KMAX:.0f}", flush=True)
    # spacing ratio
    s = np.diff(E)
    r = np.minimum(s[:-1], s[1:])/np.maximum(s[:-1], s[1:])
    print(f"spacing ratio <r~> = {r.mean():.4f} (GUE 0.536 / Poisson 0.386)",
          flush=True)

    # tone probe
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
                    out.append((p, rr, rr*math.log(p)/(2*math.pi)))
                    rr += 1
        return out
    fp = prime_power_freqs(50)
    fvals = [f for (_, _, f) in fp]
    loop_ps = set(PRIMES_LOOP)

    rng = np.random.default_rng(21)
    Nn = len(E)
    A = (rng.standard_normal((Nn, Nn)) + 1j*rng.standard_normal((Nn, Nn)))/np.sqrt(2)
    Eg = np.linalg.eigvalsh((A + A.conj().T)/2)
    Es = rng.permutation(E)

    out = {}
    for label, Ev in [("graph", E), ("gue", Eg), ("shuffled", Es)]:
        freqs, P, span = analyze(Ev, label)
        vals, zs, mu, sd = zscores(freqs, P, fvals)
        detail = {}
        for (p, rr, f) in fp:
            i = int(np.argmin(np.abs(freqs-f)))
            detail[f"({p},{rr})"] = {"z": float((P[i]-mu)/sd),
                                    "loop": p in loop_ps}
        zs_loop = [v["z"] for v in detail.values() if v["loop"]]
        zs_non = [v["z"] for v in detail.values() if not v["loop"]]
        out[label] = {"mean_z": float(np.mean(zs)), "max_z": float(np.max(zs)),
                      "mean_z_loop": float(np.mean(zs_loop)),
                      "mean_z_nonloop": float(np.mean(zs_non)),
                      "detail": detail, "freqs": freqs.tolist(),
                      "P": P.tolist()}
        print(f"{label}: mean z all={out[label]['mean_z']:.2f} | "
              f"loop primes={out[label]['mean_z_loop']:.2f} | "
              f"non-loop primes={out[label]['mean_z_nonloop']:.2f} | "
              f"max={out[label]['max_z']:.2f}", flush=True)

    json.dump({"loop_primes": PRIMES_LOOP,
               "n_levels": len(E), "kmax": KMAX,
               "spacing_ratio": float(r.mean()),
               "stats": {k: {kk: v[kk] for kk in
                               ("mean_z", "max_z", "mean_z_loop",
                                "mean_z_nonloop", "detail")}
                         for k, v in out.items()},
               "freqs": out["graph"]["freqs"],
               "P_graph": out["graph"]["P"], "P_gue": out["gue"]["P"],
               "P_shuffled": out["shuffled"]["P"]},
              open("node11l_graph.json", "w"))
    print("wrote node11l_graph.json")

    import matplotlib; matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, axx = plt.subplots(3, 1, figsize=(12, 9), sharex=True)
    for ax, label, ttl in zip(axx, ["graph", "gue", "shuffled"],
                              ["prime-orbit rose graph (R=8, Kirchhoff)",
                               "GUE control", "shuffled control"]):
        ax.plot(out[label]["freqs"], out[label]["P"], lw=0.7)
        for (p, rr, f) in fp:
            ax.axvline(f, color='r' if p in loop_ps else 'b',
                       alpha=0.3, lw=0.8)
        ax.set_title(f"{ttl} (loop-prime mean z: "
                     f"{out[label]['mean_z_loop']:.2f}, non-loop: "
                     f"{out[label]['mean_z_nonloop']:.2f})")
        ax.set_ylabel("norm. power")
    axx[-1].set_xlabel("frequency f (red=loop primes, blue=non-loop primes)")
    fig.tight_layout(); fig.savefig("node11l_graph.png", dpi=110)
    print("figure -> node11l_graph.png")

if __name__ == "__main__":
    main()
