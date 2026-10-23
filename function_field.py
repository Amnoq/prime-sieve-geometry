#!/usr/bin/env python3
"""10d: function-field / intersection-pairing template.

Concrete elliptic curve E/F_p: the explicit formula is FINITE and EXACT,
RH is the Hasse bound |a_p| <= 2 sqrt(p), and positivity is COUNTING
positivity (deg >= 0) feeding a PSD quadratic form whose discriminant
condition IS RH. Template for what an independent Weil-positivity source
looks like anatomically.
"""
import cmath, math

# ---------- tiny finite fields F_{p^n} = F_p[t]/(mod) ----------
class FF:
    def __init__(self, p, mod, coeffs):
        self.p, self.mod = p, mod
        n = len(mod) - 1
        c = [x % p for x in coeffs] + [0] * n
        self.c = tuple(c[:n])
    def __add__(self, o):
        return FF(self.p, self.mod, [(a + b) % self.p for a, b in zip(self.c, o.c)])
    def __neg__(self):
        return FF(self.p, self.mod, [(-a) % self.p for a in self.c])
    def __sub__(self, o):
        return self + (-o)
    def __mul__(self, o):
        p, n = self.p, len(self.c)
        t = [0] * (2 * n - 1)
        for i, a in enumerate(self.c):
            for j, b in enumerate(o.c):
                t[i + j] = (t[i + j] + a * b) % p
        m = self.mod  # monic degree n: x^n = -sum_{i<n} mod[i] x^i
        for k in range(2 * n - 2, n - 1, -1):
            if t[k]:
                ck = t[k]
                for i in range(n):
                    t[k - n + i] = (t[k - n + i] - ck * m[i]) % p
        return FF(p, self.mod, t[:n])
    def __pow__(self, e):
        r = FF(self.p, self.mod, [1])
        b, ee = self, e
        while ee:
            if ee & 1: r = r * b
            b = b * b; ee >>= 1
        return r
    def __eq__(self, o):
        return self.c == o.c
    def __hash__(self):
        return hash(self.c)
    def is_square(self):
        if all(x == 0 for x in self.c): return 0
        q = self.p ** len(self.c)
        return 1 if (self ** ((q - 1) // 2)) == FF(self.p, self.mod, [1]) else -1
    def __repr__(self):
        return f"FF{self.c}"

def field_elements(p, mod):
    n = len(mod) - 1
    els = []
    def rec(k, cur):
        if k == n:
            els.append(FF(p, mod, cur)); return
        for v in range(p):
            rec(k + 1, cur + [v])
    rec(0, [])
    return els

def count_points(p, mod, a, b):
    A, B = FF(p, mod, [a]), FF(p, mod, [b])
    s = 0
    for x in field_elements(p, mod):
        f = x * x * x + A * x + B
        s += f.is_square()
    return p ** (len(mod) - 1) + 1 + s

# irreducible mod polys: x^2+2 /F5, x^3+x+1 /F5, x^2+1 /F7
FIELDS = {5: {2: [2, 0, 1], 3: [1, 1, 0, 1]},
          7: {2: [1, 0, 1]}}

print("Part A: finite EXACT explicit formula  #E(F_{p^n}) = p^n+1 - pi^n - pibar^n")
print("Part B: Hasse bound from degree positivity  Q(m,n) = p m^2 + a_p m n + n^2")
for p, degmods in FIELDS.items():
    # find a nonsingular curve y^2 = x^3 + a x + b
    found = None
    for a in range(p):
        for b in range(p):
            if (4 * a ** 3 + 27 * b ** 2) % p != 0:
                found = (a, b); break
        if found: break
    a, b = found
    mod1 = [0, 1]  # F_p itself: degree-1 "mod"
    N1 = count_points(p, mod1, a, b)
    ap = p + 1 - N1
    print(f"\nE: y^2 = x^3 + {a}x + {b} over F_{p}:  #E(F_p)={N1}, a_p={ap}, "
          f"|a_p|={abs(ap)} <= 2sqrt(p)={2*math.sqrt(p):.3f}: {abs(ap) <= 2*math.sqrt(p)}")
    disc = complex(ap ** 2 - 4 * p, 0)
    pi = (ap + cmath.sqrt(disc)) / 2
    print(f"  Frobenius eigenvalues: pi={pi.real:.6f}{pi.imag:+.6f}i, |pi|={abs(pi):.6f} "
          f"(sqrt(p)={math.sqrt(p):.6f})")
    # zeta numerator roots t = 1/pi: |t| = 1/sqrt(p)  <=> RH for the curve
    t1 = 1 / pi
    print(f"  zeta root t=1/pi: |t|={abs(t1):.6f} = 1/sqrt(p)={1/math.sqrt(p):.6f}  (RH for E)")
    for n, mod in degmods.items():
        Nn = count_points(p, mod, a, b)
        pred = round((p ** n + 1 - pi ** n - pi.conjugate() ** n).real)
        print(f"  n={n}: counted #E(F_{p}^{n})={Nn},  p^n+1-pi^n-pibar^n={pred}, match={Nn == pred}")
    # degree form PSD <-> Hasse
    D = ap ** 2 - 4 * p
    print(f"  degree form Q(m,n)={p}m^2{ap:+}mn+n^2: discriminant={D} <= 0: {D <= 0} (Hasse)")
    # anchor the counting origin: deg(1-phi)=#E(F_p), deg(1+phi)=#twist(F_p)
    d = next(v for v in range(2, p) if pow(v, (p - 1) // 2, p) == p - 1)  # nonsquare
    Nt = count_points(p, mod1, (a * d * d) % p, (b * d ** 3) % p)
    print(f"  deg(1-phi) = #E(F_p) = {N1} (counted); deg(1+phi) = #E^d(F_p) = {Nt} "
          f"(counted, twist); p+1+a_p = {p+1+ap}, match={Nt == p+1+ap}")
    # PSD on a grid
    ok = all(p * m * m + ap * m * nn + nn * nn >= 0
             for m in range(-3, 4) for nn in range(-3, 4))
    print(f"  Q(m,n) >= 0 on [-3,3]^2 grid: {ok}")
