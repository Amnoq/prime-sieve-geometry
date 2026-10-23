#!/usr/bin/env python3
"""10b: Li's criterion through the D1 face-sum.

Li (1997, cited): RH <=> lambda_n >= 0 for all n>=1,
  lambda_n = sum_rho [1 - (1-1/rho)^n].

Part A: lambda_n via Keiper's exact Taylor formula (no zeros):
  lambda_n = n * [z^n] log xi(1/(1-z)),  w = z/(1-z), L(w) = log xi(1+w).
Part B: lambda_n from zeros (truncated) -- agreement + positivity.
Part C: S_1 = sum 1/rho -> 1+gamma/2-(1/2)log(4pi): archimedean, no prime sum.
Part D: the obstruction -- A_k(eps)=sum Lambda(n)(log n)^k n^{-1-eps}
  diverges as k!/eps^{k+1}; lambda_n's prime content = finite parts.
"""
import math
import numpy as np
import mpmath

mpmath.mp.dps = 80
N = 40

# ---------- Part A: Keiper-Taylor ----------
# c(w) = w*zeta(1+w) = 1 + sum_{j>=1} (-1)^{j-1} gamma_{j-1}/(j-1)! w^j
c = [mpmath.mpf(1)] + [(-1) ** (j - 1) * mpmath.stieltjes(j - 1) / math.factorial(j - 1)
                       for j in range(1, N + 1)]
# d = log c, formal
d = [mpmath.mpf(0)] * (N + 1)
for k in range(1, N + 1):
    d[k] = c[k] - sum(mpmath.mpf(j) / k * d[j] * c[k - j] for j in range(1, k))

l = [mpmath.mpf(0)] * (N + 1)   # L(w) = sum l_k w^k
l[0] = -mpmath.log(2)
logpi = mpmath.log(mpmath.pi)
for k in range(1, N + 1):
    lk = (-1) ** (k + 1) / k            # log(1+w)
    lk += d[k]                          # log(w*zeta(1+w))
    if k == 1:
        lk += -logpi / 2                # -((1+w)/2) log pi
    lk += mpmath.polygamma(k - 1, mpmath.mpf('0.5')) / (math.factorial(k) * 2 ** k)  # logGamma
    l[k] = lk

# compose with w(z) = z/(1-z): m_n = sum_{k=1..n} l_k C(n-1,k-1); lambda_n = n*m_n
lam_taylor = {}
for n in range(1, N + 1):
    m = sum(l[k] * math.comb(n - 1, k - 1) for k in range(1, n + 1))
    lam_taylor[n] = float(n * m)

print("Part A: lambda_n via Keiper-Taylor (exact, no zeros)")
for n in [1, 2, 3, 5, 10, 20, 30, 40]:
    print(f"  n={n:3d}  lambda_n = {lam_taylor[n]:.10f}   lambda_n/(n log n) = "
          f"{lam_taylor[n]/(n*math.log(n)) if n > 1 else float('nan'):.6f}")
print(f"  min over n<=40: {min(lam_taylor.values()):.6f}  (>=0: {all(v >= 0 for v in lam_taylor.values())})")

# ---------- Part B: zero side ----------
print("Part B: zeros...", flush=True)
NZ = 150
zeros = [complex(mpmath.zetazero(k)) for k in range(1, NZ + 1)]
rhos = np.array(zeros)
print(f"  {NZ} zeros to gamma={max(z.imag for z in zeros):.1f}", flush=True)
print("Part B: lambda_n from zeros vs Taylor")
for n in [1, 2, 3, 5, 10, 20, 30]:
    s = np.sum(1 - (1 - 1 / rhos) ** n)
    lam_z = float(2 * s.real)   # rho <-> rhobar pairing
    print(f"  n={n:3d}  zero-side = {lam_z:12.6f}   taylor = {lam_taylor[n]:12.6f}   "
          f"diff = {abs(lam_z - lam_taylor[n]):.2e}")

# ---------- Part C: S_1 ----------
S1_partial = float(2 * np.sum(1 / rhos).real)   # rho <-> rhobar pairing
S1_exact = 1 + float(mpmath.euler) / 2 - 0.5 * math.log(4 * math.pi)
print(f"Part C: sum_|gamma|<={max(z.imag for z in zeros):.0f} 1/rho = {S1_partial:.7f}  "
      f"exact 1+gamma/2-(1/2)log(4pi) = {S1_exact:.7f}")

# ---------- Part D: divergence of the naive prime sums ----------
print("Part D: A_k(X,eps) = sum_{n<=X} Lambda(n)(log n)^k n^{-1-eps}; expect ~ k!/eps^{k+1}")
X = 10000000
bs = bytearray(b"\x01") * (X + 1)
bs[0:2] = b"\x00\x00"
for i in range(2, int(X ** 0.5) + 1):
    if bs[i]:
        bs[i * i:X + 1:i] = b"\x00" * (((X - i * i) // i) + 1)
PP = []
for p in range(2, X + 1):
    if bs[p]:
        q, lp = p, math.log(p)
        while q <= X:
            PP.append((q, lp))
            if q > X // p:
                break
            q *= p
print(f"  {len(PP)} prime powers to {X}", flush=True)
for k, eps in [(0, 0.10), (0, 0.05), (1, 0.15), (1, 0.10), (2, 0.25), (2, 0.20)]:
    A = 0.0
    for q, lp in PP:
        # q = p^m, Lambda(q) = lp = log p, log q = m*log p
        lq = math.log(q)
        A += lp * lq ** k * math.exp((-1 - eps) * lq)
    pred = math.factorial(k) / eps ** (k + 1)
    print(f"  k={k} eps={eps:.2f}  A={A:12.2f}  k!/eps^(k+1)={pred:12.2f}  ratio={A/pred:.3f}")
