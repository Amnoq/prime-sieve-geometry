#!/usr/bin/env python3
"""
Node 12d -- Heisenberg nilmanifold (twisted torus) Laplacian probe.

M = Gamma \\ H_3, standard left-invariant metric. EXACT spectrum from
representation theory (Schrodinger reps pi_h, h in Z\\{0}, mult |h|):
  torus part : 4 pi^2 (m^2+n^2),            (m,n) in Z^2
  non-abelian: (2 pi h)^2 + 2 pi |h| (2k+1), h != 0, k >= 0, mult |h|
(the oscillator term is the harmonic oscillator -d^2/dt^2 + (2pi h)^2 t^2;
the (2pi h)^2 is the central direction).

Compare sqrt-spectrum vs zeta zeros: sequences, Weyl counting, and
nearest-neighbour spacings of distinct eigenvalues in a bulk window
(heuristic unfolding by local mean spacing).

Expectation: negative. Counting is Weyl d=3 (Lambda^{3/2}); spacing is
rigid/oscillator-like, not GUE. The point of the probe: even genuine
theta-function / Weil-representation arithmetic content in a geometric
Laplacian does not produce zero statistics. Arithmetic flavor != zero
spectrum.
"""

import numpy as np, json, time
import mpmath as mp

t0 = time.time()
LMAX = (2*np.pi*25)**2          # eigenvalue ceiling
eigs = []

# torus part: 4 pi^2 (m^2+n^2) <= LMAX
R = int(np.sqrt(LMAX/(4*np.pi**2))) + 1
for m in range(-R, R+1):
    for n in range(-R, R+1):
        v = 4*np.pi**2*(m*m+n*n)
        if v <= LMAX: eigs.append(v)

# non-abelian part
hmax = int(np.sqrt(LMAX)/(2*np.pi))
for h in range(1, hmax+1):
    base = (2*np.pi*h)**2
    if base > LMAX: break
    kmax = int((LMAX - base)/(4*np.pi*h) - 0.5) + 1
    ks = np.arange(0, max(kmax, 0))
    vs = base + 2*np.pi*h*(2*ks+1)
    vs = vs[vs <= LMAX]
    for _ in (1, -1):                       # h and -h, mult |h| each
        eigs.extend(np.repeat(vs, h).tolist())

eigs = np.sort(np.array(eigs))
sq = np.sqrt(eigs)
print(f"eigenvalues (with mult): {len(sq)}, max sqrt = {sq[-1]:.1f}")

# distinct eigenvalues for spacing analysis
uniq = np.unique(np.round(sq, 9))
print(f"distinct: {len(uniq)}")

# zeta zeros
mp.dps = 25
NZ = 200
print(f"computing {NZ} zeros ...", flush=True)
gammas = np.array([float(mp.im(mp.zetazero(j))) for j in range(1, NZ+1)])
print(f"  gamma_200 = {gammas[-1]:.1f} ({time.time()-t0:.0f}s)")

# --- panels
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
fig, axx = plt.subplots(1, 3, figsize=(15, 4.2))

n = min(4000, len(sq))
axx[0].plot(np.arange(n), sq[:n], lw=1.2, label="Heisenberg sqrt(eig)")
axx[0].plot(np.arange(NZ), gammas, lw=1.2, label="zeta zeros")
axx[0].set_xlabel("n"); axx[0].set_title("twisted-torus spectrum vs zeros")
axx[0].legend(fontsize=9)

E = np.logspace(np.log10(7), np.log10(sq[-1]), 60)
axx[1].loglog(E, [np.sum(sq <= e) for e in E], lw=1.8,
              label="Heisenberg: N ~ Lambda^{3/2}")
Tg = np.logspace(np.log10(15), np.log10(gammas[-1]), 60)
axx[1].loglog(Tg, [np.sum(gammas <= t) for t in Tg], lw=1.8,
              label="zeros: N ~ T log T")
axx[1].loglog(E, 0.02*E**1.5, "k--", lw=1, label="slope 3/2")
axx[1].set_xlabel("E / T"); axx[1].set_title("Weyl counting")
axx[1].legend(fontsize=8)

# spacings in bulk window, normalized by local mean (heuristic)
def norm_spac(x, lo, hi):
    w = x[(x >= lo) & (x <= hi)]
    s = np.diff(w); return s/np.mean(s)
sh = norm_spac(uniq, 60, 140)
sz = norm_spac(gammas, 60, 140)
axx[2].hist(sh, bins=40, range=(0, 3), alpha=0.6, density=True,
            label=f"Heisenberg (n={len(sh)})")
axx[2].hist(sz, bins=40, range=(0, 3), alpha=0.6, density=True,
            label=f"zeros (n={len(sz)})")
axx[2].set_xlabel("spacing / mean spacing"); axx[2].set_title("bulk spacings")
axx[2].legend(fontsize=9)

fig.tight_layout()
fig.savefig("heisenberg_probe.png", dpi=110)
print("figure -> heisenberg_probe.png")

with open("heisenberg_probe.json", "w") as f:
    json.dump({"n_with_mult": int(len(sq)), "n_distinct": int(len(uniq)),
               "n_zeros": NZ,
               "heis_first6_sqrt": [float(x) for x in sq[:6]],
               "gamma_first6": [float(x) for x in gammas[:6]]}, f, indent=1)
