#!/usr/bin/env python3
"""Node 11a diagnostic: is the BK lattice spectrum really a ladder, and why?"""
import numpy as np, sys
sys.path.insert(0, "/home/hatch/workspace/prime-sieve-geometry")

def build_bk(N, x0, a):
    x = x0 + a * np.arange(N)
    k = 2 * np.pi * np.fft.fftfreq(N, a)
    V = np.fft.fft(np.eye(N)) / np.sqrt(N)
    P = (V * k) @ V.conj().T
    X = np.diag(x)
    return 0.5 * (X @ P + P @ X), x

def report(N, x0, a):
    H, x = build_bk(N, x0, a)
    E = np.linalg.eigvalsh(H)
    s = np.diff(E)
    n = np.arange(len(E))
    # linear fit E_n vs n
    A = np.polyfit(n, E, 1)
    pred = np.polyval(A, n)
    resid = E - pred
    print(f"N={N} x0={x0} a={a}: range=[{E[0]:.1f},{E[-1]:.1f}]")
    print(f"  spacing: mean={s.mean():.4f} std={s.std():.4f} "
          f"std/mean={s.std()/s.mean():.4f} (picket~0, GUE~0.52)")
    print(f"  linear fit: E_n = {A[0]:.4f}*n + {A[1]:.2f}, "
          f"max|resid|={np.abs(resid).max():.3f} ({100*np.abs(resid).max()/(E[-1]-E[0]):.2f}% of range)")
    print(f"  2*pi/log(L/x0) = {2*np.pi/np.log(x[-1]/x[0]):.4f}  vs fitted slope {A[0]:.4f}")
    # smooth counting shape: linear (ladder) vs E log E (BK)?
    # fit N(E) = c1*E + c2 vs c1*E*log(E) on positive branch
    Ep = E[E > 0]; nn = np.arange(1, len(Ep) + 1)
    lin = np.polyfit(Ep, nn, 1)
    lin_pred = np.polyval(lin, Ep)
    ll = np.polyfit(Ep * np.log(Ep), nn, 1)
    ll_pred = np.polyval(ll, Ep * np.log(Ep))
    rl = np.sqrt((nn - lin_pred) ** 2).mean()
    re = np.sqrt((nn - ll_pred) ** 2).mean()
    print(f"  counting fit resid: linear {rl:.2f} vs E*log(E) {re:.2f}")
    return A[0]

print("== baseline ==")
report(600, 0.5, 0.05)
print("== x0 doubled ==")
report(600, 1.0, 0.05)
print("== a doubled ==")
report(600, 0.5, 0.10)
