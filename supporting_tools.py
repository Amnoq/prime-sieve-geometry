#!/usr/bin/env python3
"""10e: supporting tools -- verify the analytic amplifiers on our objects.

P(t) = sum_{n<=N0} a_n n^{it}, a_n = Lambda(n)/sqrt(n) (prime powers).
  1. Montgomery-Vaughan mean value: (1/2H) int_{T0-H}^{T0+H} |P|^2 -> S2.
  2. Large sieve: sum_{r<=R} |P(t_r)|^2 <= (N0+delta^{-1}) S2, delta-spaced.
  3. Uncertainty cost curve: window w <-> prime data n = e^{7.433/w}.
"""
import math
import numpy as np

N0 = 50000
bs = bytearray(b"\x01") * (N0 + 1)
bs[0:2] = b"\x00\x00"
for i in range(2, int(N0 ** 0.5) + 1):
    if bs[i]:
        bs[i * i:N0 + 1:i] = b"\x00" * (((N0 - i * i) // i) + 1)
ns, aa = [], []
for p in range(2, N0 + 1):
    if bs[p]:
        q, lp = p, math.log(p)
        while q <= N0:
            ns.append(q); aa.append(lp / math.sqrt(q))
            if q > N0 // p: break
            q *= p
L = np.array([math.log(n) for n in ns])
A = np.array(aa)
S2 = float(A @ A)
M = len(ns)
print(f"{M} prime powers <= {N0}, S2 = sum|a_n|^2 = {S2:.6f}")

def P(t):
    return np.sum(A * np.exp(1j * t * L))

T0 = 20000.0
print("\n1. Mean value: I(H)/(2H S2) -> 1")
for H in [200, 1000, 5000, 20000]:
    dt = 0.1
    ts = np.arange(T0 - H, T0 + H, dt)
    # vectorized over t in chunks to keep memory sane
    s = 0.0
    CH = 20000
    for i in range(0, len(ts), CH):
        tc = ts[i:i + CH]
        E = np.exp(1j * np.outer(tc, L))
        Pv = E @ A
        s += float(np.sum(np.abs(Pv) ** 2)) * dt
    print(f"   H={H:>6}: I(H)/(2H S2) = {s / (2 * H * S2):.6f}")

print("\n2. Large sieve: sum_{r<=R}|P(t0+r delta)|^2 <= (N0+delta^-1) S2")
for delta, R in [(1.0, 200), (0.5, 400)]:
    lhs = sum(abs(P(T0 + r * delta)) ** 2 for r in range(1, R + 1))
    bound = (N0 + 1 / delta) * S2
    print(f"   delta={delta}: LHS={lhs:.4f} bound={bound:.4f} ratio={lhs/bound:.6f} (<=1: {lhs<=bound})")

print("\n3. Uncertainty cost curve: n = e^{7.433/w} (10a-step3 envelope)")
print(f"   {'w':>6} {'n (prime data)':>16} {'window':>10} {'vs zero spacing@T0=100':>24}")
for w in [2.0, 1.0, 0.5, 0.25, 0.1]:
    n = math.exp(7.433 / w)
    spacing = 2 * math.pi / math.log(100 / (2 * math.pi))
    print(f"   {w:>6} {n:>16.2e} {'±'+str(w):>10} {w/spacing:>20.2f} x spacing ({spacing:.2f})")
