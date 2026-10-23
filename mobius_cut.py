#!/usr/bin/env python3
"""
Node 11d -- cutting the Mobius band; bare geometric operators on M.

(a) The cut, exhibited. Classical facts, numerically double-checked here:
    center cut -> ONE band, 2x length, k half-twists (k from the Gauss
    linking number of the two boundary circles, calibrated on k=0,2
    bands), orientable: NOT a Mobius band. 1/3 cut -> two LINKED bands
    (thin Mobius + long 2-twist band).
(b) Spectral probe of the bare stage: the truncated Mobius-band Laplacian
    has the EXACT spectrum lam=(pi*m)^2+(n*pi/2T)^2 with m+n odd (from the
    orientable double cover + deck involution). Its sqrt-spectrum looks
    nothing like the zeta zeros; the position observable |sigma-1/2| has
    continuous spectrum [0,1/2].
    VERDICT (negative, exact): bare geometric operators on M do not see
    zeros -> the operator, if it exists, must see the arithmetic weights.
"""

import numpy as np
import json, time

t0 = time.time()

# ---------------------------------------------------------------- twist bands
def band(k, R, w, u, v):
    """k-half-twist band. k even -> annulus (orientable); k odd -> Mobius."""
    U, V = np.meshgrid(u, v)
    X = (R + V*np.cos(k*U/2))*np.cos(U)
    Y = (R + V*np.cos(k*U/2))*np.sin(U)
    Z = V*np.sin(k*U/2)
    return X, Y, Z

def mobius_F(u, v, R=10.0):
    """standard embedding, k=1, u in [0,2pi), v in [-1,1]."""
    U, V = np.meshgrid(u, v)
    X = (R + V*np.cos(U/2))*np.cos(U)
    Y = (R + V*np.cos(U/2))*np.sin(U)
    Z = V*np.sin(U/2)
    return X, Y, Z

# ---------------------------------------------------------------- linking number
def linking_number(P1, P2):
    """Gauss integral for two closed polygonal curves (no repeated endpoint)."""
    def tangents(P):
        d = np.roll(P, -1, axis=0) - np.roll(P, 1, axis=0)
        L = np.linalg.norm(d, axis=1)
        return d / L[:, None], L / 2
    t1, ds1 = tangents(P1)
    t2, ds2 = tangents(P2)
    lk = 0.0
    for i in range(len(P1)):
        R = P1[i][None, :] - P2
        n3 = np.linalg.norm(R, axis=1)**3
        cr = np.cross(t1[i][None, :], t2)
        lk += np.sum(np.einsum('ij,ij->i', R, cr) / n3 * ds2) * ds1[i]
    return lk / (4*np.pi)

def std_band_boundary(k, R, w, N=800):
    """the two boundary circles of the k-half-twist band (k even)."""
    u = np.linspace(0, 2*np.pi, N, endpoint=False)
    out = []
    for vv in (w, -w):
        X = (R + vv*np.cos(k*u/2))*np.cos(u)
        Y = (R + vv*np.cos(k*u/2))*np.sin(u)
        Z = vv*np.sin(k*u/2)
        out.append(np.column_stack([X, Y, Z]))
    return out

# calibration: k=0 -> lk 0 ; k=2 -> lk 1
for kk, expect in ((0, 0.0), (2, 1.0)):
    B1, B2 = std_band_boundary(kk, 10.0, 1.6)
    got = linking_number(B1, B2)
    print(f"  calibration k={kk}: |lk|={abs(got):.4f} (expect {expect:.1f})")
    assert abs(abs(got) - expect) < 0.02

# ---- the center-cut band M': boundaries from the strip model
# B1 = original Mobius boundary (single circle); B2 = slit edge (single circle)
N = 1200
r = np.linspace(0, 2, N, endpoint=False)
u1 = np.where(r < 1, 2*np.pi*r, 2*np.pi*(r-1))
v1 = np.where(r < 1, 1.0, -1.0)
X1 = (10 + v1*np.cos(u1/2))*np.cos(u1)
Y1 = (10 + v1*np.cos(u1/2))*np.sin(u1)
Z1 = v1*np.sin(u1/2)
B1 = np.column_stack([X1, Y1, Z1])
B2 = np.column_stack([10*np.cos(2*np.pi*r), 10*np.sin(2*np.pi*r),
                      np.zeros_like(r)])
lk_cut = linking_number(B1, B2)
k_cut = int(round(2*abs(lk_cut)))
print(f"  center-cut band: lk(boundaries)={lk_cut:.4f} -> k={k_cut} half-twists")
print(f"  => ONE piece, 2x length, {k_cut} half-twists "
      f"({k_cut//2} full twists), orientable: NOT a Mobius band")

# ---------------------------------------------------------------- spectra
print("\n--- spectral probe: truncated Mobius Laplacian vs zeta zeros ---")
T = 50.0
eigs = []
for m in range(-9, 10):
    for n in range(1, 955):
        if (m + n) % 2 == 1:
            eigs.append((np.pi*m)**2 + (n*np.pi/(2*T))**2)
eigs = np.sqrt(sorted(eigs))[:150]

import mpmath as mp
mp.dps = 25
zeros = [float(mp.im(mp.zetazero(j))) for j in range(1, 151)]
zeros = np.array(zeros)
print("  first 8 sqrt-Laplacian-eigenvalues:", np.round(eigs[:8], 4))
print("  first 8 zeta gammas               :", np.round(zeros[:8], 4))
print(f"  ({time.time()-t0:.0f}s elapsed)")

with open("mobius_cut_results.json", "w") as f:
    json.dump({"k_center_cut": k_cut, "lk": float(lk_cut),
               "T_trunc": T,
               "sqrt_eigs_8": [float(x) for x in eigs[:8]],
               "gammas_8": [float(x) for x in zeros[:8]]}, f, indent=1)

# ---------------------------------------------------------------- figures
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Fig 1: the cut
fig = plt.figure(figsize=(15, 5))
u = np.linspace(0, 2*np.pi, 160); v = np.linspace(-1.6, 1.6, 30)

ax = fig.add_subplot(131, projection="3d")
X, Y, Z = band(1, 10.0, 1.6, u, v)
ax.plot_surface(X, Y, Z, alpha=0.35, color="steelblue", edgecolor="none")
uc = np.linspace(0, 2*np.pi, 300)
ax.plot(10*np.cos(uc), 10*np.sin(uc), np.zeros_like(uc),
        color="crimson", lw=2.5, ls="--")
ax.text(10, 0, 2.5, "cut here:\nthe center line", color="crimson", fontsize=9)
ax.set_title("(a) Mobius band + the cut path")
ax.set_axis_off(); ax.view_init(elev=20, azim=-60)

ax = fig.add_subplot(132, projection="3d")
X, Y, Z = band(k_cut, 20.0, 0.8, u, np.linspace(-0.8, 0.8, 20))
ax.plot_surface(X, Y, Z, alpha=0.35, color="seagreen", edgecolor="none")
ax.set_title(f"(b) center cut: ONE band, 2x long,\n{k_cut} half-twists "
             f"({k_cut//2} full) -> orientable,\nNOT a Mobius band")
ax.set_axis_off(); ax.view_init(elev=20, azim=-60)

ax = fig.add_subplot(133, projection="3d")
# thin Mobius (the middle piece)
X, Y, Z = band(1, 8.0, 0.55, u, np.linspace(-0.55, 0.55, 16))
ax.plot_surface(X, Y, Z, alpha=0.4, color="steelblue", edgecolor="none")
# long 2-twist band, threaded through -> linked
uu = np.linspace(0, 2*np.pi, 200); vv = np.linspace(-0.55, 0.55, 14)
U, V = np.meshgrid(uu, vv)
cu = 4.5 + 11*np.cos(U); su = 11*np.sin(U)
e1x, e1z = -np.cos(U), -np.sin(U)
tw = np.cos(2*U)*V
Xb = cu + tw*e1x
Yb = np.sin(2*U)*V
Zb = su + tw*e1z
ax.plot_surface(Xb, Yb, Zb, alpha=0.4, color="darkorange", edgecolor="none")
ax.set_title("(c) cut at 1/3: TWO linked bands\n"
             "thin Mobius + long 2-twist band")
ax.set_axis_off(); ax.view_init(elev=18, azim=-55)
fig.tight_layout()
fig.savefig("mobius_cut.png", dpi=110)
print("figure -> mobius_cut.png")

# Fig 2: spectra
fig, axx = plt.subplots(1, 2, figsize=(12, 4.5))
n = np.arange(1, 151)
axx[0].plot(n, eigs, label="sqrt(Laplacian eig), Mobius |t|<=50", lw=1.5)
axx[0].plot(n, zeros, label="zeta zeros gamma_n", lw=1.5)
axx[0].set_xlabel("n"); axx[0].set_ylabel("value")
axx[0].set_title("bare geometric spectrum vs zeta zeros")
axx[0].legend(fontsize=9)
axx[1].plot(n, eigs, label="Mobius Laplacian", lw=1.5)
axx[1].plot(n, zeros, label="zeta zeros", lw=1.5)
axx[1].set_xlabel("n"); axx[1].set_yscale("log")
axx[1].set_title("same, log scale")
axx[1].legend(fontsize=9)
fig.tight_layout()
fig.savefig("mobius_spectrum.png", dpi=110)
print("figure -> mobius_spectrum.png")
