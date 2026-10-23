#!/usr/bin/env python3
"""
Node 12b -- Weyl's-law probe of the flat multi-torus linkage (L1).

Flat T^3 Laplacian: EXACT spectrum (2pi)^2 (m^2+n^2+k^2), (m,n,k) in Z^3.
Compare the sqrt-spectrum and the counting function against zeta zeros.

Weyl (d=3): N(Lambda) ~ C Lambda^{3/2}. Zeros need ~ (T/2pi) log T.
d=2 is too slow by a log; d>=3 too fast. No fixed-d manifold Laplacian
matches zero counting. The flat-T^3 case is stronger: explicit spectrum,
visibly not the zeros.
"""

import numpy as np
import json, time
import mpmath as mp

t0 = time.time()

# ---- flat T^3 sqrt-spectrum by lattice enumeration
R2max = 2600                      # m^2+n^2+k^2 <= R2max
vals = []
R = int(np.sqrt(R2max)) + 1
for m in range(-R, R+1):
    for n in range(-R, R+1):
        s2 = m*m + n*n
        if s2 > R2max: continue
        kmax = int(np.sqrt(R2max - s2))
        for k in range(-kmax, kmax+1):
            vals.append(s2 + k*k)
vals = np.array(vals, dtype=float)
sq = np.sort(2*np.pi*np.sqrt(vals))
print(f"T^3 lattice points: {len(sq)}, max sqrt-eig = {sq[-1]:.1f}")

# ---- zeta zeros
mp.dps = 25
NZ = 300
print(f"computing {NZ} zeros ...", flush=True)
gammas = np.array([float(mp.im(mp.zetazero(j))) for j in range(1, NZ+1)])
print(f"  gamma_300 = {gammas[-1]:.1f} ({time.time()-t0:.0f}s)")

n_show = 300
s1, g1 = sq[:n_show], gammas[:n_show]
print("first 6 T^3 sqrt-eigs:", np.round(s1[:6], 3))
print("first 6 zeta gammas  :", np.round(g1[:6], 3))

# counting functions for the log-log panel
E = np.logspace(np.log10(7), np.log10(sq[-1]), 60)
N_t3 = np.array([np.sum(sq <= e) for e in E])
Tg = np.logspace(np.log10(15), np.log10(gammas[-1]), 60)
N_z = np.array([np.sum(gammas <= t) for t in Tg])

with open("multi_torus_probe.json", "w") as f:
    json.dump({"n_lattice": int(len(sq)), "n_zeros": NZ,
               "t3_first6": [float(x) for x in s1[:6]],
               "gamma_first6": [float(x) for x in g1[:6]]}, f, indent=1)

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

fig, axx = plt.subplots(1, 2, figsize=(12, 4.5))
n = np.arange(1, n_show+1)
axx[0].plot(n, s1, lw=1.5, label="sqrt(eig), flat T^3 Laplacian")
axx[0].plot(n, g1, lw=1.5, label="zeta zeros gamma_n")
axx[0].set_xlabel("n"); axx[0].set_ylabel("value")
axx[0].set_title("flat T^3 spectrum vs zeta zeros")
axx[0].legend(fontsize=9)

axx[1].loglog(E, N_t3, lw=1.8, label="T^3: N(Lambda) ~ Lambda^{3/2}")
axx[1].loglog(Tg, N_z, lw=1.8, label="zeros: N(T) ~ T log T")
# reference slopes
axx[1].loglog(E, 0.02*E**1.5, "k--", lw=1, label="slope 3/2")
axx[1].loglog(Tg, 0.05*Tg*np.log(Tg), "k:", lw=1, label="slope 1 (x log x)")
axx[1].set_xlabel("E / T"); axx[1].set_ylabel("counting function")
axx[1].set_title("Weyl's law: no fixed d fits T log T")
axx[1].legend(fontsize=8)
fig.tight_layout()
fig.savefig("multi_torus_weyl.png", dpi=110)
print("figure -> multi_torus_weyl.png")
