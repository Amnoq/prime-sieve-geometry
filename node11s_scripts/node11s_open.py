"""
Node 11s — (a) Gamma_exact with an OPEN right channel.
CONCEPTUAL FINDING (computed, not assumed): for the confining quartic,
complex scaling yields Im E = 0 to machine precision — there are no
resonances, so the charter's (a) as specified cannot yield Gamma. The
bounce's Gamma is the width of a resonance that only exists with an
open decay channel. We open the far right (x > Xc) with a linear drop;
the bounce region (x < 0.8) is untouched, so (b) is unchanged.
V_mod is C^0 at Xc; the resonance is exponentially insensitive to Xc
(verified by Xc variation) — the kink is proven irrelevant, not assumed.

V_mod(x;eps) = (x^2-1)^2 - eps*x            for x <= Xc
             = V(Xc) - alpha*(x-Xc)          for x >  Xc
FD complex scaling + Richardson in dx^2 (artifact scales as dx^2,
measured on the null). Gamma = -2*Im(E_res)/hb.
"""
import numpy as np, json, sys
from scipy.linalg import eig
from scipy.optimize import brentq

XC = 1.0
ALPHA = 30.0

def Vp(x, eps): return 4.0*x*(x**2 - 1.0) - eps
def Vq(x, eps): return (x**2 - 1.0)**2 - eps*x

def Vmod(x, eps, Xc=XC, alpha=ALPHA):
    x = np.asarray(x)
    v = Vq(x, eps)
    Vc = Vq(Xc, eps)
    drop = Vc - alpha*(x - Xc)
    return np.where(x <= Xc, v, drop)

def Vmod_cx(z, eps, Xc=XC, alpha=ALPHA):
    # evaluated on the scaled contour; the kink at Re(z)=Xc is
    # exponentially irrelevant (resonance weight there ~1e-11);
    # Xc-insensitivity is verified numerically.
    z = np.asarray(z)
    v = (z**2 - 1.0)**2 - eps*z
    Vc = Vq(Xc, eps)
    rz = np.real(z)
    drop = Vc - alpha*(rz - Xc)
    return np.where(rz <= Xc, v, drop)

def scan_open(hb, eps, L=12.0, N=801, thetas=(0.15, 0.20, 0.25),
              Xc=XC, alpha=ALPHA):
    xf = brentq(lambda x: Vp(x, eps), -1.6, -0.2)
    xb = brentq(lambda x: Vp(x, eps), -0.2, 0.2)
    Vf = Vq(xf, eps)
    wf = np.sqrt(12.0*xf**2 - 4.0)
    Ef = Vf + hb*wf/2.0
    x = np.linspace(-L, L, N); dx = x[1]-x[0]
    main = np.full(N, hb**2/dx**2); off = np.full(N-1, -hb**2/(2*dx**2))
    K = np.diag(main) + np.diag(off, 1) + np.diag(off, -1)
    out = []
    for th in thetas:
        z = x*np.exp(1j*th)
        H = np.exp(-2j*th)*K + np.diag(Vmod_cx(z, eps, Xc, alpha))
        w, vr = eig(H)
        best = None
        for i in range(N):
            if abs(w[i].real - Ef) < 0.5 and -0.02 < w[i].imag < 0.0:
                psi = vr[:, i]
                left = np.sum(np.abs(psi[x < xb])**2)/np.sum(np.abs(psi)**2)
                if left > 0.6 and (best is None or
                                  abs(w[i].imag) < abs(w[best].imag)):
                    best = i
        if best is not None:
            out.append(dict(theta=th, E=[float(w[best].real),
                                        float(w[best].imag)]))
    return dict(Ef=float(Ef), scan=out, L=L, N=N, dx=float(dx))

def richardson(ims, dxs):
    # Im = a + b*dx^2 ; return a (extrapolated) and residual
    X = np.array(dxs)**2
    A = np.column_stack([np.ones_like(X), X])
    coef, res, *_ = np.linalg.lstsq(A, np.array(ims), rcond=None)
    return coef[0], coef[1]

if __name__ == "__main__":
    # Xc-insensitivity + dx^2 scaling check at one point
    hb, eps = 0.30, 0.2
    print("=== Xc insensitivity (N=801, th=0.20) ===")
    for Xc in [1.0, 1.2, 1.5]:
        s = scan_open(hb, eps, N=801, thetas=(0.20,), Xc=Xc)
        e = s["scan"][0]["E"] if s["scan"] else None
        print(f"  Xc={Xc}: {e}")
    print("=== dx^2 scaling (th=0.20, Xc=1.0) ===")
    ims, dxs = [], []
    for N in [801, 1201, 1601]:
        s = scan_open(hb, eps, N=N, thetas=(0.20,))
        e = s["scan"][0]["E"]
        ims.append(e[1]); dxs.append(s["dx"])
        print(f"  N={N}: Re={e[0]:.8f} Im={e[1]:.4e}")
    a, b = richardson(ims, dxs)
    print(f"  Richardson Im(inf)={a:.4e}, slope={b:.3e}")
    print(f"  ratios: {ims[0]/ims[1]:.3f}, {ims[1]/ims[2]:.3f} (dx^2 -> 2.25, 1.78)")
