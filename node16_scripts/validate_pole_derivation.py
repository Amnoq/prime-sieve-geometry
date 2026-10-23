#!/usr/bin/env python3
"""
Node 16 validation: pole-interlacing derivation of the vertex phase alternation.

Analytic claim: vertex roots = zeros of F(k)=sum_j tan(kL_j/2), exactly one
per inter-pole interval (poles all distinct by unique factorization).
N_v(k) = N_poles(k) - 1 + dither(k), dither in {0,1}.
N_poles,osc(k) = sum_j sum_n (-1)^n sin(n k L_j)/(pi n)   [exact Fourier]
=> at tone (p,r): C_v^pole = i*(-1)^r/(pi*r): phase -pi/2 (odd r), +pi/2 (even r).

This script checks, live:
 1. poles distinct; exactly one root per inter-pole interval (exact claims)
 2. phase of C_v^pole at tone freqs = -pi/2 / +pi/2 (exact claim)
 3. phase of C_v^total (roots) vs C_v^pole -> quantifies the dither's effect
 4. magnitude and phase of the dither FT at tone freqs (the obstruction, measured)
"""
import numpy as np, math, sys
sys.path.insert(0, "/home/hatch/workspace/prime-sieve-geometry")
from node11l_graph import G, vertex_roots, PRIMES_LOOP, L, R

KMAX = 400.0
print("recomputing vertex roots ...", flush=True)
kv = vertex_roots(kmax=KMAX, step=0.025)   # finer set (1023 roots, cf. 11q)
kv = np.sort(kv)
print(f"  {len(kv)} roots in (0, {KMAX}]")

# ---- 1. poles of F(k)=sum tan(kL_j/2): k = pi*(2m+1)/L_j ----
poles = []
for Lj in L:
    mmax = int((KMAX*Lj/math.pi - 1)/2) + 1
    poles.extend(math.pi*(2*m+1)/Lj for m in range(mmax+1))
poles = np.array(sorted(poles))
print(f"  {len(poles)} poles in (0, {KMAX}]")
# distinctness
dmin = np.diff(poles).min()
print(f"  min pole gap = {dmin:.3e}  (all distinct: {dmin > 1e-9})")
# exactly one root per inter-pole interval?
ok = True
for i in range(len(poles)-1):
    n = int(np.sum((kv > poles[i]) & (kv < poles[i+1])))
    if n != 1:
        ok = False
        print(f"  VIOLATION: interval {i} has {n} roots")
        break
print(f"  one root per inter-pole interval: {ok}")

# ---- grids and counting functions ----
E = np.arange(0.5, KMAX, 0.05)          # common fine grid
Nv = np.searchsorted(kv, E)            # N_v(E)
# N_poles(E) = sum_j floor((E*L_j/pi + 1)/2)
Npoles = np.zeros_like(E)
for Lj in L:
    Npoles += np.floor((E*Lj/math.pi + 1)/2)
dither = Nv - (Npoles - 1)
print(f"  dither range: [{dither.min()}, {dither.max()}] (expect {{0,1}})",
      f"mean={dither.mean():.4f}")

def lin_detrend(y, x):
    A = np.vstack([x, np.ones_like(x)]).T
    coef, *_ = np.linalg.lstsq(A, y, rcond=None)
    return y - A @ coef

def Cf(y, f):
    # probe convention: C(f) s.t. A*sin(2π f E) -> +i*A  (matches Dirichlet +pi/2)
    return (2.0/len(y)) * np.sum(y * np.exp(-2j*math.pi*f*E))

Nv_o = lin_detrend(Nv, E)
Np_o = lin_detrend(Npoles, E)
dth_o = lin_detrend(dither.astype(float), E)

print("\n tone   |Cvpole| ph(Cvpole) |Cvdither| ph(dither) |Cv tot| ph(Cv tot)  pred|Cv|")
for (p, r) in [(2,1),(3,1),(5,1),(7,1),(2,2),(3,2),(2,3),(3,3),(2,4),(3,4)]:
    f = r*math.log(p)/(2*math.pi)
    cp, cd_, ct = Cf(Np_o, f), Cf(dth_o, f), Cf(Nv_o, f)
    pred = 1/(math.pi*r)
    print(f" ({p},{r})  {abs(cp):.4f}  {np.angle(cp)/math.pi:+.3f}π   "
          f"{abs(cd_):.4f}   {np.angle(cd_)/math.pi:+.3f}π   "
          f"{abs(ct):.4f}  {np.angle(ct)/math.pi:+.3f}π   {pred:.4f}")
print("\nphases in units of pi; +0.5 = +pi/2, -0.5 = -pi/2")
