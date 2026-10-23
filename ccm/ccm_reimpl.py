"""
Independent reimplementation of Connes-Consani-Moscovici "Zeta Spectral Triples"
(arXiv:2511.22755) D_log^{(lambda,N)} operator from PRIME EULER PRODUCTS ALONE.

Construction (primary source, verified against arXiv TeX source mc2arXiv.tex):
  M_{nm} = QW_{lam,N}(V_n, V_m) = W_{0,2}^#(F) - W_R^#(F) - sum_p W_p^#(F)
  with F(x) = q(U_n,U_m)(log x), indices n,m in {-N,...,N}, L = 2 log lam.

  W_{0,2}^#(F) = int_1^oo F(x)(x^{1/2}+x^{-1/2}) d*x          [Lemma 4.1 closed form]
  W_R^#(F)     = archimedean, via Prop 4.3 table from alpha_L, beta_L, gamma_L
  sum_p W_p^#(F) = sum_{1<k<=lam^2} Lambda(k) k^{-1/2} q(U_n,U_m)(log k)
                 ^^ THE ONLY PLACE PRIMES ENTER ^^

Then: smallest eigenpair (eps_N, xi) of M; spectrum = real zeros of
  xihat(z) = 2 L^{-1/2} sin(zL/2) sum_{j=-N..N} xi_j/(z - 2 pi j/L).

D12 AUDIT STRUCTURE: prime input is isolated in `prime_weights()`; everything
else is prime-free. Controls: shuffled Lambda, zeroed Lambda.
"""
import mpmath as mp

# ----------------------------------------------------------------------------
# closed forms (from TeX source)
# ----------------------------------------------------------------------------
def q_nm(y, n, m, L):
    """Lemma polarize0: q(U_n,U_m)(y), y in [0,L]. Real."""
    if n == m:
        return 2*(L-y)*mp.cos(2*mp.pi*n*y/L)/L
    return (mp.sin(2*mp.pi*m*y/L) - mp.sin(2*mp.pi*n*y/L))/(mp.pi*(n-m))

def W02(n, m, L):
    """Lemma w02 / (hh)."""
    return (32*L*mp.sinh(L/4)**2 * (L**2 - 16*mp.pi**2*m*n)
            / ((L**2 + 16*mp.pi**2*m**2)*(L**2 + 16*mp.pi**2*n**2)))

def rho(x):
    return mp.e**(x/2)/(mp.e**x - mp.e**(-x))

def c_of_L(L):
    return (mp.log(mp.e**(L/2)+1)
            + mp.mpf('0.25')*(-2*mp.log(mp.e**L+1) - mp.pi - mp.log(4))
            + mp.atan(mp.e**(L/2)))

def w_of_L(L):
    return (mp.mpf('0.5')*(mp.euler + mp.log(4*mp.pi))
            - mp.mpf('0.5')*mp.log((mp.e**L+1)/(mp.e**L-1)))

def alpha_L(n, L):
    """(1/pi) int_0^L sin(2 pi n x/L) rho(x) dx ; Prop computearch."""
    if n == 0:
        return mp.mpf('0')
    z = mp.e**(-2*L)
    b = mp.pi*1j*n/L + mp.mpf('0.25')
    hyp = mp.hyper([1, b], [b+1], z)
    t1 = mp.e**(-L/2)*mp.im(2*L/(L+4*mp.pi*1j*n)*hyp)
    t2 = mp.mpf('0.5')*mp.im(mp.digamma(b))
    return (t1+t2)/mp.pi

def beta_L(n, L):
    """(1/L) int_0^L x cos(2 pi n x/L) rho(x) dx ; Prop computearch."""
    z = mp.e**(-2*L)
    a = mp.mpf('0.25') + 1j*mp.pi*n/L
    t1 = -L*mp.e**(-L/2)*mp.im(2*L/(4*mp.pi*n - 1j*L)
                               * mp.hyper([1, a], [a+1], z))
    t2 = -mp.e**(-L/2)/4*mp.re(mp.lerchphi(z, 2, a))
    t3 = mp.mpf('0.25')*mp.re(mp.polygamma(1, a))
    return (t1+t2+t3)/L

def _cosm1_integral(n, L):
    """int_0^L (cos(2 pi n x/L)-1) rho(x) dx ; Prop computearch."""
    z = mp.e**(-2*L)
    b = mp.pi*1j*n/L + mp.mpf('0.25')
    t1 = -mp.e**(-L/2)*mp.re(2*L/(L+4*mp.pi*1j*n)*mp.hyper([1, b], [b+1], z))
    t2 = 2*mp.e**(-L/2)*mp.hyper([mp.mpf('0.25'), 1], [mp.mpf('1.25')], z)
    t3 = -mp.mpf('0.5')*mp.re(mp.digamma(b) - mp.digamma(mp.mpf('0.25')))
    return t1+t2+t3

def gamma_L(n, L, cL=None, wL=None):
    """int_0^L (cos - e^{-x/2}) rho dx + c(L) + w(L); (4.11),(4.14)."""
    if cL is None: cL = c_of_L(L)
    if wL is None: wL = w_of_L(L)
    return _cosm1_integral(n, L) + 2*cL + wL

def Ie_L(n, L, _K_cache={}):
    """int_0^L (cos(2 pi n y/L) - e^{-y/2}) rho(y) dy.
    FAST: = _cosm1_integral(n,L) + K, K=∫_0^L(1-e^{-y/2})rho dy (n-indep).
    Verified vs direct quadrature to 2.7e-51 (2026-09-30)."""
    if L not in _K_cache:
        fK = lambda y: (1-mp.e**(-y/2))*rho(y) if y > 1e-300 else mp.mpf('0.5')
        _K_cache[L] = mp.quad(fK, [0, L], method='tanh-sinh')
    return _cosm1_integral(n, L) + _K_cache[L]

def Ie_L_quad(n, L):
    """Slow direct quadrature (for verification only)."""
    f = lambda y: ((mp.cos(2*mp.pi*n*y/L)-mp.e**(-y/2))*rho(y)
                    if y > 1e-300 else mp.mpf('0.25'))
    return mp.quad(f, [0, L], method='tanh-sinh')

def WR_entry(n, m, L, abg_cache):
    """W_R^# from (weinfty): off-diag via Prop 4.3 (verified);
    diagonal CORRECTED: (weinfty) gives
      W_R(n,n) = (gamma+log(4 pi (e^L-1)/(e^L+1))) + 2 Ie(n) - 2 beta(n).
    (Paper's Prop 4.3 diagonal as printed carries a spurious +2 c(L);
    see derivation in notes. Validated against direct (bombtestR) quad.)"""
    a, b, ie = abg_cache
    if n == m:
        const = mp.euler + mp.log(4*mp.pi*(mp.e**L-1)/(mp.e**L+1))
        return const + 2*ie[n] - 2*b[n]
    return (a[m]-a[n])/(n-m)

# ----------------------------------------------------------------------------
# prime input -- THE ONLY ARITHMETIC INPUT (D12 audit point)
# ----------------------------------------------------------------------------
def prime_weights(lam):
    """Return dict {k: Lambda(k)} for 1<k<=lam^2. von Mangoldt = log p on p^m.
    Cutoff is the exact integer floor(lam^2); avoids fp exclusion of k=lam^2."""
    x = lam**2
    X = int(mp.floor(x + mp.mpf('1e-12')))  # exact integer cutoff
    ks = {}
    # sieve primes up to X
    sieve = bytearray(b'\x01')*(X+1)
    sieve[0:2] = b'\x00\x00'
    import math
    for i in range(2, int(math.isqrt(X))+1):
        if sieve[i]:
            sieve[i*i:X+1:i] = b'\x00'*(((X - i*i)//i)+1)
    primes = [i for i in range(2, X+1) if sieve[i]]
    for p in primes:
        pp = p
        while pp <= X:
            ks[pp] = mp.log(p)
            if pp > X // p: break
            pp *= p
    return ks

def Wp_entry(n, m, L, pw):
    """(bomp): sum_{1<k<=e^L} Lambda(k) k^{-1/2} q(U_n,U_m)(log k)."""
    s = mp.mpf('0')
    for k, lamk in pw.items():
        lk = mp.log(k)
        if lk > L: continue
        s += lamk * k**mp.mpf('-0.5') * q_nm(lk, n, m, L)
    return s

# ----------------------------------------------------------------------------
# matrix assembly
# ----------------------------------------------------------------------------
def build_M(lam, N, pw_override=None, verbose=False):
    L = 2*mp.log(lam)
    idx = list(range(-N, N+1))
    if verbose: print(f"lam={lam} L={L} N={N} dim={len(idx)}", flush=True)
    a = {n: alpha_L(n, L) for n in idx}
    b = {n: beta_L(n, L) for n in idx}
    ie = {n: Ie_L(n, L) for n in idx}
    abg = (a, b, ie)
    pw = prime_weights(lam) if pw_override is None else pw_override
    if verbose: print(f"  prime-power terms: {len(pw)}", flush=True)
    M = mp.matrix(len(idx))
    for ii, n in enumerate(idx):
        for jj, m in enumerate(idx):
            if jj < ii:  # symmetric
                M[ii, jj] = M[jj, ii]
                continue
            M[ii, jj] = W02(n, m, L) - WR_entry(n, m, L, abg) - Wp_entry(n, m, L, pw)
    return M, L, idx

# ----------------------------------------------------------------------------
# verification: closed forms vs direct quadrature
# ----------------------------------------------------------------------------
def verify_closed_forms(L, nvals=(0, 1, 2, 5, 10)):
    mp.dps = 50
    out = {}
    for n in nvals:
        f_sin = lambda x: mp.sin(2*mp.pi*n*x/L)*rho(x) if x > 0 else mp.pi*n/L
        Ia = mp.quad(f_sin, [0, L], method='tanh-sinh')
        f_xc = lambda x: (x*mp.cos(2*mp.pi*n*x/L)*rho(x)) if x > 0 else mp.mpf('0.5')
        Ib = mp.quad(f_xc, [0, L], method='tanh-sinh')
        f_cm1 = lambda x: ((mp.cos(2*mp.pi*n*x/L)-1)*rho(x)) if x > 0 else mp.mpf('0')
        Ic = mp.quad(f_cm1, [0, L], method='tanh-sinh')
        cLq = mp.quad(lambda x: (1-mp.e**(-x/2))/(mp.e**x-mp.e**(-x)) if x > 0 else mp.mpf('0.25'),
                      [0, L], method='tanh-sinh')
        a_cf = alpha_L(n, L); b_cf = beta_L(n, L)
        g_cf = gamma_L(n, L)
        a_q = Ia/mp.pi; b_q = Ib/L; g_q = Ic + 2*cLq + w_of_L(L)
        out[n] = (abs(a_cf-a_q), abs(b_cf-b_q), abs(g_cf-g_q),
                  abs(cLq-c_of_L(L)))
    return out
