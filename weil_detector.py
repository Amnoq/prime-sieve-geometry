#!/usr/bin/env python3
"""10a step 3: the prime-side zero detector; resolution vs cost.

h_{T0,w}(r) = exp(-(r-T0)^2/2w^2) + exp(-(r+T0)^2/2w^2)  (sum of squares, >=0, peak 1)
g(u) = w*sqrt(2/pi) * exp(-w^2 u^2/2) * cos(T0*u)        (exact Fourier)
W(h) = pole + arch - 2*sum_{n>=2} Lambda(n) n^{-1/2} g(log n)   [primes only]
     = sum_rho h(gamma_rho)                                        [zeros]
Detector: W(h) ~= weighted count of zeros near T0, from primes alone.
Bound: N+([T0-w,T0+w]) <= e^{1/2} W(h)   (h>=0, min on window = e^{-1/2}).
Cost: envelope e^{-w^2 u^2/2} needs prime powers to n ~ e^{O(1/w)}.
"""
import math
import numpy as np
import mpmath

mpmath.mp.dps = 30

print("zeros...", flush=True)
NZ = 80
zeros = [complex(mpmath.zetazero(k)) for k in range(1, NZ + 1)]
gammas = np.array(sorted(z.imag for z in zeros))
print(f"{NZ} zeros to gamma={gammas.max():.1f}", flush=True)


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
                if q > N // p:
                    break
                q *= p
    out.sort()
    return out


PP = prime_powers(20000000)
print(f"{len(PP)} prime powers to 2e7", flush=True)


def detector(T0, w):
    def h(r):
        return math.exp(-(r - T0) ** 2 / (2 * w * w)) + math.exp(-(r + T0) ** 2 / (2 * w * w))

    Cg = w * math.sqrt(2 / math.pi)

    def g(u):
        return Cg * math.exp(-w * w * u * u / 2) * math.cos(T0 * u)

    Wzero = 2 * float(np.sum([h(g_) for g_ in gammas]))
    pole = 2 * math.exp(-(T0 * T0 - 0.25) / (2 * w * w)) * math.cos(T0 / (2 * w * w))

    def fa(s):
        r = T0 + w * s
        return math.exp(-s * s / 2) * (
            float(mpmath.re(mpmath.digamma(mpmath.mpc(0.25, 0.5 * r)))) - math.log(math.pi)
        )

    arch = (w / math.pi) * float(mpmath.quad(fa, [-10, 10]))
    psum, nmax, last_t = 0.0, 0, 0.0
    for n, lp in PP:
        t = 2 * lp * (n ** -0.5) * g(math.log(n))
        psum += t
        nmax, last_t = n, t
    Wprime = pole + arch - psum
    inB = [g_ for g_ in gammas if abs(g_ - T0) <= w]
    leak = Wzero - 2 * sum(h(g_) for g_ in inB)
    return dict(T0=T0, w=w, Wzero=Wzero, Wprime=Wprime, pole=pole, arch=arch,
                psum=psum, nmax=nmax, last_t=last_t, Nin=len(inB),
                bound=math.exp(0.5) * Wprime, leak=leak,
                zeros_in=[f"{g_:.3f}" for g_ in inB])


print(f"\n{'T0':>6} {'w':>5} {'Wprime':>10} {'Wzero':>10} {'|diff|':>9} "
      f"{'N+':>3} {'bound':>6} {'leak':>7} {'nmax':>9}")
for T0, w in [(50, 2.0), (50, 1.0), (50, 0.5), (100, 2.0), (100, 1.0)]:
    r = detector(T0, w)
    print(f"{r['T0']:6.0f} {r['w']:5.1f} {r['Wprime']:10.4f} {r['Wzero']:10.4f} "
          f"{abs(r['Wprime']-r['Wzero']):9.1e} {r['Nin']:3d} {r['bound']:6.2f} "
          f"{r['leak']:7.4f} {r['nmax']:9d}   zeros@{r['zeros_in']} last_t={r['last_t']:.1e}")
