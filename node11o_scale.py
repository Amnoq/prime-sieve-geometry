#!/usr/bin/env python3
"""
Node 11o -- vertex route length dependence: length or arithmetic?

11l (loops log p, short): vertex sector sang (z=4.02).
11n (loops random in [4.2,6.0], long): vertex sector silent (z=0.15).
Confound: 11n changed BOTH length AND arithmetic structure (prime-log
ratios -> random). This node varies length alone: scale 11l's lengths
by c in {0.5, 1, 2, 4}, preserving all ratios.

H1 (length): vertex tone z decays monotonically with c.
H2 (arithmetic): vertex tone z flat with c (ratios preserved).
Dirichlet sector at each c: positive control (picket fences must sing
at every scale; if not, the probe is broken, not the physics).
Negative controls: scaled non-loop primes 23..47.

Status: COMPUTED 2026-10-05. Decision-tree entry: Node 11o.
"""
import numpy as np, json, math, sys
sys.path.insert(0, "/home/hatch/workspace/prime-sieve-geometry")
from fock_primefreq import zscores

PRIMES_LOOP = [2, 3, 5, 7, 11, 13, 17, 19]
PRIMES_NONLOOP = [23, 29, 31, 37, 41, 43, 47]
L0 = np.array([math.log(p) for p in PRIMES_LOOP])
R = len(L0)
KMAX = 400.0
SCALES = [0.5, 1.0, 2.0, 4.0]

def analyze_f(E, fmax, label, deg=10, nf=8000):
    from scipy.signal import lombscargle
    n = np.arange(1, len(E) + 1)
    Nbar = np.polyval(np.polyfit(E, n, deg), E)
    res = n - Nbar
    lo, hi = int(0.10*len(E)), int(0.90*len(E))
    Eb, rb = E[lo:hi], res[lo:hi] - res[lo:hi].mean()
    freqs = np.linspace(0.02, fmax, nf)
    P = lombscargle(Eb, rb, 2*np.pi*freqs, normalize=True)
    return freqs, P

def G(k, L):
    k = np.atleast_1d(np.asarray(k, dtype=float))
    s = np.sin(k[None, :] * L[:, None] / 2)
    c = np.cos(k[None, :] * L[:, None] / 2)
    out = np.zeros(k.size)
    for j in range(R):
        m = np.ones(R, dtype=bool); m[j] = False
        out += s[j, :] * np.prod(c[m, :], axis=0)
    return out

def vertex_roots(L, kmax=KMAX, step=0.05):
    ks = np.arange(0.01, kmax, step)
    gv = G(ks, L)
    roots = []
    for i in range(len(ks)-1):
        if gv[i] == 0:
            roots.append(ks[i])
        elif gv[i]*gv[i+1] < 0:
            a, b, fa = ks[i], ks[i+1], gv[i]
            for _ in range(60):
                m = 0.5*(a+b)
                fm = float(G(np.array([m]), L)[0])
                if fa*fm <= 0: b = m
                else: a, fa = m, fm
            roots.append(0.5*(a+b))
    return np.array(roots)

def dirichlet_levels(L, kmax=KMAX):
    out = []
    for Lj in L:
        mmax = int(kmax*Lj/(2*math.pi))
        out.extend(2*math.pi*np.arange(1, mmax+1)/Lj)
    return np.array(out)

def main():
    results = {}
    for c in SCALES:
        L = c*L0
        print(f"=== scale c={c} (Ltot={L.sum():.2f}) ===", flush=True)
        kv = vertex_roots(L); kd = dirichlet_levels(L)
        print(f"  vertex {len(kv)}, dirichlet {len(kd)}", flush=True)
        loop_f = [r*lj/(2*math.pi) for lj in L for r in (1, 2, 3)]
        nonloop_f = [math.log(p)*c/(2*math.pi) for p in PRIMES_NONLOOP]
        fmax = max(loop_f)*1.15
        fp_all = loop_f + nonloop_f
        n_loop = len(loop_f)
        row = {"n_vertex": len(kv), "n_dirichlet": len(kd)}
        for label, Ev in [("vertex", np.sort(kv)),
                          ("dirichlet", np.sort(kd))]:
            freqs, P = analyze_f(Ev, fmax, label)
            vals, zs, mu, sd = zscores(freqs, P, fp_all)
            row[label] = {"mean_z_loop": float(np.mean(zs[:n_loop])),
                          "max_z_loop": float(np.max(zs[:n_loop])),
                          "mean_z_nonloop": float(np.mean(zs[n_loop:]))}
            print(f"  {label}: loop z={row[label]['mean_z_loop']:.2f} "
                  f"(max {row[label]['max_z_loop']:.2f}) | nonloop "
                  f"z={row[label]['mean_z_nonloop']:.2f}", flush=True)
        # GUE control at c=1 only
        if c == 1.0:
            rng = np.random.default_rng(21)
            Nn = len(kv)
            A = (rng.standard_normal((Nn, Nn))
                 + 1j*rng.standard_normal((Nn, Nn)))/np.sqrt(2)
            Eg = np.linalg.eigvalsh((A + A.conj().T)/2)
            freqs, P = analyze_f(Eg, fmax, "gue")
            vals, zs, mu, sd = zscores(freqs, P, fp_all)
            row["gue"] = {"mean_z_loop": float(np.mean(zs[:n_loop])),
                          "mean_z_nonloop": float(np.mean(zs[n_loop:]))}
            print(f"  gue: loop z={row['gue']['mean_z_loop']:.2f} | "
                  f"nonloop z={row['gue']['mean_z_nonloop']:.2f}", flush=True)
        results[str(c)] = row
    json.dump({"scales": SCALES, "results": results},
              open("node11o_scale.json", "w"))
    print("wrote node11o_scale.json")

    import matplotlib; matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    cs = np.array(SCALES)
    vz = [results[str(c)]["vertex"]["mean_z_loop"] for c in SCALES]
    dz = [results[str(c)]["dirichlet"]["mean_z_loop"] for c in SCALES]
    fig, ax = plt.subplots(figsize=(9, 6))
    ax.semilogx(cs, vz, 'o-', label="vertex sector (under test)")
    ax.semilogx(cs, dz, 's-', label="dirichlet sector (control)")
    ax.axhline(0, color='k', lw=0.5)
    ax.set_xlabel("length scale c")
    ax.set_ylabel("mean z at loop frequencies")
    ax.set_title("Vertex tone strength vs loop-length scale "
                 "(prime-log ratios preserved)")
    ax.legend(); fig.tight_layout()
    fig.savefig("node11o_scale.png", dpi=110)
    print("figure -> node11o_scale.png")

if __name__ == "__main__":
    main()
