#!/usr/bin/env python3
"""
Node 11 — the Frobenius-like operator hunt.

11a: Berry-Keating xp leg. The BK Hamiltonian H=xp predicts, semiclassically,
     the SMOOTH zero-count N(T) ~ (T/2pi)(log(T/2pi)-1) + 7/8 (Riemann-von Mangoldt
     main terms). Verify against actual zeros; exhibit the fluctuation part S(T)
     that BK does NOT give (that is the periodic-orbit / prime side -- cf. the
     user's diagonal-approximation work).

11b: Mobius-band stage leg. M = critical strip / (s ~ 1-sbar) is an infinite
     Mobius band; |xi|^2 descends to it (exact invariance). Zeros collapse
     4 -> 2 on M (pairs {rho, (1-rho)bar}); RH = "all points lie on the central
     line sigma=1/2". Verify the invariance numerically and exhibit the collapse.

Epistemic status: 11a numerics = computationally verified (BK formula itself is a
classical theorem; the xp operator is a conjectural candidate). 11b invariance =
exact theorem, numerically confirmed; the band-as-stage is a heuristic proposal.
"""

import mpmath as mp
import numpy as np
import json, math, time

mp.dps = 25
t0 = time.time()

# ---------------------------------------------------------------- zeros
N_ZERO = 400
print(f"computing {N_ZERO} zeros ...", flush=True)
zeros = [mp.zetazero(k) for k in range(1, N_ZERO + 1)]
gammas = np.array([float(mp.im(z)) for z in zeros], dtype=float)
print(f"  gamma_1={gammas[0]:.6f} gamma_400={gammas[-1]:.3f} ({time.time()-t0:.0f}s)")

# ---------------------------------------------------------------- 11a: BK smooth count
print("\n=== 11a: Berry-Keating xp leg ===")
def N_smooth(T):
    return (T/(2*math.pi))*(math.log(T/(2*math.pi)) - 1) + 7/8

# staircase N(T) at each zero: N(gamma_n) = n
n_vals = np.arange(1, N_ZERO + 1)
smooth_vals = np.array([N_smooth(g) for g in gammas])
S = n_vals - smooth_vals          # fluctuation part (BK does not predict this)
print(f"  N(T) vs BK smooth: max|S(T)| = {np.max(np.abs(S)):.3f}, "
      f"mean|S| = {np.mean(np.abs(S)):.3f}")
print(f"  S(T) at T=gamma_400: {S[-1]:+.3f}  (bounded oscillation, not growing)")
# check the smooth formula tracks the staircase: residual of linear fit of S vs T
A = np.vstack([gammas, np.ones_like(gammas)]).T
slope, icept = np.linalg.lstsq(A, S, rcond=None)[0]
print(f"  drift of S(T) vs T: slope = {slope:.2e} per unit T (BK smooth has no drift)")

res11a = {
    "N_zero": N_ZERO, "Tmax": float(gammas[-1]),
    "max_abs_S": float(np.max(np.abs(S))),
    "mean_abs_S": float(np.mean(np.abs(S))),
    "S_drift_slope": float(slope),
    "S_at_Tmax": float(S[-1]),
}

# ---------------------------------------------------------------- 11b: Mobius stage
print("\n=== 11b: Mobius-band stage ===")
def xi(s):
    return mp.mpf('0.5')*s*(s-1)*mp.power(mp.pi, -s/2)*mp.gamma(s/2)*mp.zeta(s)

mp.dps = 30
test_pts = [0.3+20j, 0.7+100j, 0.15+300j, 0.9+500j, 0.5+14.134725j, 0.42+1000j]
max_rel = 0.0
for s in test_pts:
    s = mp.mpc(s)
    a, b = abs(xi(s)), abs(xi(1-mp.conj(s)))
    rel = abs(a*a - b*b)/max(a*a, b*b)
    max_rel = max(max_rel, float(rel))
print(f"  |xi(1-sbar)|^2 = |xi(s)|^2: max rel. discrepancy = {max_rel:.2e} "
      f"({len(test_pts)} points)")

# quotient map q: fold strip to sigma in [1/2,1] via s -> s if sigma>=1/2 else 1-sbar
def q(s):
    return s if mp.re(s) >= 0.5 else 1 - mp.conj(s)

mp.dps = 25
# orbit collapse 4 -> 2 on M for the first few zeros (all on the line)
print("  zero-orbit collapse on M (rho, rhobar, 1-rho, (1-rho)bar -> q-images):")
shown = 0
for z in zeros[:6]:
    rho = complex(z)
    orb = [rho, rho.conjugate(), 1-rho, 1-rho.conjugate()]
    imgs = sorted({(round(q(mp.mpc(w)).real, 12), round(q(mp.mpc(w)).imag, 12))
                   for w in orb})
    # images should be exactly 2: (1/2, +gamma), (1/2, -gamma)
    assert len(imgs) == 2, imgs
    assert all(abs(s - 0.5) < 1e-9 for s, t in imgs), imgs
    if shown < 3:
        print(f"    gamma={rho.imag:9.4f}: {len(orb)} orbit points -> "
              f"{len(imgs)} points on M, both with sigma' = 1/2")
        shown += 1
print("  all 6 checked: 4 -> 2 collapse confirmed; images lie on central line")

res11b = {"invariance_max_rel_disc": max_rel, "orbit_collapse": "4->2 verified (6 zeros)"}

with open("operator_hunt_results.json", "w") as f:
    json.dump({"11a": res11a, "11b": res11b}, f, indent=1)
print("\nresults -> operator_hunt_results.json")

# ---------------------------------------------------------------- figure: the band
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

R, W = 10.0, 1.6
u = np.linspace(0, 2*np.pi, 120)
v = np.linspace(-1, 1, 25) * 9.0   # |t| <= 9*scale ; scale t by 1/3 below
U, V = np.meshgrid(u, v)
X = (R + V*np.cos(U/2))*np.cos(U)
Y = (R + V*np.cos(U/2))*np.sin(U)
Z = V*np.sin(U/2)

fig = plt.figure(figsize=(11, 5))
ax = fig.add_subplot(121, projection="3d")
ax.plot_surface(X, Y, Z, alpha=0.30, color="steelblue", edgecolor="none")
# central line sigma=1/2 -> u=pi
uc = np.pi
Vc = np.linspace(-9, 9, 200)
Xc = (R + Vc*np.cos(uc/2))*np.cos(uc)
Yc = (R + Vc*np.cos(uc/2))*np.sin(uc)
Zc = Vc*np.sin(uc/2)
ax.plot(Xc, Yc, Zc, color="crimson", lw=2.5, label="sigma = 1/2 (central line)")
# zero pairs: gamma_1..gamma_5 -> v = +/-gamma/3 at u=pi
for g in gammas[:5]/3.0:
    for sgn in (1, -1):
        vv = sgn*g
        ax.scatter([(R + vv*np.cos(uc/2))*np.cos(uc)],
                   [(R + vv*np.cos(uc/2))*np.sin(uc)],
                   [vv*np.sin(uc/2)], color="crimson", s=28, zorder=5)
ax.set_title("M = strip / (s ~ 1-sbar): zero pairs on the central line")
ax.legend(fontsize=8)
ax.view_init(elev=18, azim=-60)
ax.set_axis_off()

ax2 = fig.add_subplot(122)
ax2.set_aspect("equal")
ax2.set_xlim(-0.15, 1.15); ax2.set_ylim(-60, 60)
ax2.add_patch(plt.Rectangle((0, -60), 1, 120, fc="aliceblue", ec="navy"))
ax2.annotate("", xy=(0, 45), xytext=(1, -45),
             arrowprops=dict(arrowstyle="<->", color="navy", lw=1.2))
ax2.annotate("", xy=(0, -45), xytext=(1, 45),
             arrowprops=dict(arrowstyle="<->", color="navy", lw=1.2))
ax2.text(0.5, 52, "(0,t) ~ (1,-t): the flip", ha="center", fontsize=9, color="navy")
ax2.axvline(0.5, color="crimson", lw=2.5)
ax2.text(0.52, -52, "sigma=1/2", color="crimson", fontsize=9)
for g in gammas[:8]:
    ax2.plot(0.5, g, marker="o", color="crimson", ms=4)
    ax2.plot(0.5, -g, marker="o", color="crimson", ms=4)
ax2.set_xlabel("sigma"); ax2.set_ylabel("t")
ax2.set_title("the gluing that makes the band")
fig.tight_layout()
fig.savefig("mobius_band.png", dpi=110)
print("figure -> mobius_band.png")
