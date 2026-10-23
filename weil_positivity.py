#!/usr/bin/env python3
"""10a step 2: Weil's explicit formula (symmetric Guinand-Weil form),
verified zero-side vs prime-side, then exhibited as prime-side positivity.

Formula: for even test function h, g(u) = (1/2pi) int h(r) e^{-iru} dr,
  sum_rho h(gamma_rho) = h(i/2)+h(-i/2)
      + (1/2pi) int_{-inf}^{inf} h(r)[Re digamma(1/4+ir/2) - log pi] dr
      - 2 sum_{n>=2} Lambda(n) n^{-1/2} g(log n).
Test family: h_a(r) = e^{-a r^2} = |e^{-a r^2/2}|^2  (a square).
Define W(h) := prime side (pole + archimedean - prime sum), no zeros used.
"""
import math
import numpy as np
import mpmath

mpmath.mp.dps = 30

print("zeros...", flush=True)
NZ = 60
zeros = [complex(mpmath.zetazero(k)) for k in range(1, NZ + 1)]
gammas = np.array([z.imag for z in zeros])
print(f"max gamma used: {gammas.max():.1f}", flush=True)


def prime_powers(N):
    bs = bytearray(b"\x01") * (N + 1)
    bs[0:2] = b"\x00\x00"
    for i in range(2, int(N ** 0.5) + 1):
        if bs[i]:
            bs[i * i:N + 1:i] = b"\x00" * (((N - i * i) // i) + 1)
    out = []
    for p in range(2, N + 1):
        if bs[p]:
            q, lp = p, math.log(p)
            while q <= N:
                out.append((q, lp))
                q *= p
    out.sort()
    return out


PP = prime_powers(300000)
print(f"{len(PP)} prime powers to 300k", flush=True)


def weil(a):
    Ca = (1 / (2 * math.pi)) * math.sqrt(math.pi / a)

    def g(u):
        return Ca * math.exp(-u * u / (4 * a))

    # zero side (needs gamma real; all computed zeros satisfy this)
    lhs = 2 * float(np.sum(np.exp(-a * gammas ** 2)))
    # pole terms
    pole = 2 * math.exp(a / 4)
    # archimedean: (1/2pi) int_{-inf}^{inf} = (1/pi) int_0^{inf} (even)
    def f(r):
        return math.exp(-a * r * r) * (
            float(mpmath.re(mpmath.digamma(mpmath.mpc(0.25, 0.5 * r))))
            - math.log(math.pi)
        )

    arch = float(mpmath.quad(f, [0, mpmath.inf])) / math.pi
    # prime sum: all prime powers (sorted); tail beyond PP certified below
    psum = 0.0
    for n, lp in PP:
        psum += 2 * lp * (n ** -0.5) * g(math.log(n))
    cutoff = PP[-1][0]
    U = math.log(cutoff)
    sig = 0.5 + U / (8 * a)
    # tail: e^{-u^2/4a} <= e^{-U^2/8a} e^{-Uu/8a} for u>=U; sum Lambda n^{-sig} <= .7+1/(sig-1)^2
    tail = 2 * Ca * math.exp(-U * U / (8 * a)) * (0.7 + 1 / (sig - 1) ** 2)
    W = pole + arch - psum
    return dict(a=a, lhs=lhs, pole=pole, arch=arch, psum=psum,
                W=W, tail=tail, cutoff=cutoff)


for a in [0.02, 0.1, 0.5]:
    r = weil(a)
    print(f"\na = {r['a']}:")
    print(f"  zero side : sum_rho h(gamma) = {r['lhs']:.6e}")
    print(f"  prime side: pole={r['pole']:.6f}  arch={r['arch']:.6f}  prime-sum={r['psum']:.6f}")
    print(f"  W(h) = {r['W']:.6e}   |zero-side - prime-side| = {abs(r['lhs']-r['W']):.2e}")
    print(f"  prime tail < {r['tail']:.1e} (cut at n={r['cutoff']});  W(h) >= 0: {r['W'] > -1e-9}")
