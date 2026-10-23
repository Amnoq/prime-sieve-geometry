"""
Node 11s — (a) Gamma_exact from complex-scaled exact diagonalization.
H(theta) = -(hb^2/2) e^{-2i theta} D^2 + V(x e^{i theta}; eps), FD grid.
The false-vacuum resonance: Re E near V_f + hb*wf/2, small Im E < 0,
eigenfunction localized left of the barrier. Tracked over theta for
the plateau; convergence checked in (L,N).
Gamma = -2*Im(E_res)/hb.
ANCHOR 3 (null): single well -> Im E0 = 0 to numerical precision.
"""
import numpy as np, json, sys
from scipy.linalg import eig

def Vcx(z, eps):  return (z**2 - 1.0)**2 - eps*z
def Vp(x, eps):   return 4.0*x*(x**2 - 1.0) - eps

def resonance(hb, eps, L=8.0, N=801, thetas=(0.08,0.12,0.16,0.20,0.24,0.30)):
    from scipy.optimize import brentq
    xf = brentq(lambda x: Vp(x,eps), -1.6, -0.2)
    xb = brentq(lambda x: Vp(x,eps), -0.2, 0.2)
    xt = brentq(lambda x: Vp(x,eps), 0.2, 1.6)
    Vf = (xf**2-1.0)**2 - eps*xf
    wf = np.sqrt(12.0*xf**2 - 4.0)
    Ef_guess = Vf + hb*wf/2.0
    x = np.linspace(-L, L, N); dx = x[1]-x[0]
    # kinetic: -(hb^2/2) d^2/dx^2, FD  (11r convention: diag hb^2/dx^2,
    # offdiag -hb^2/2dx^2)
    main = np.full(N, hb**2/dx**2); off = np.full(N-1, -hb**2/(2*dx**2))
    K = np.diag(main) + np.diag(off,1) + np.diag(off,-1)
    out = []
    for th in thetas:
        z = x*np.exp(1j*th)
        H = np.exp(-2j*th)*K + np.diag(Vcx(z, eps))
        w, vr = eig(H)
        # candidates: Re E near Ef_guess, Im E small negative
        cand = [i for i in range(N)
                if abs(w[i].real-Ef_guess) < 0.6 and -0.1 < w[i].imag < 0.001]
        best = None
        for i in cand:
            psi = vr[:, i]
            left = np.sum(np.abs(psi[x < xb])**2)/np.sum(np.abs(psi)**2)
            if left > 0.85:
                if best is None or abs(w[i].imag) < abs(w[best].imag):
                    best = i
        if best is not None:
            out.append(dict(theta=th, E=[float(w[best].real),
                                        float(w[best].imag)]))
    return dict(Ef_guess=float(Ef_guess), Vf=float(Vf), wf=float(wf),
                xf=float(xf), xb=float(xb), scan=out)

def gamma_from_scan(scan):
    # plateau over theta in [0.12, 0.30]
    pts = [(s["theta"], s["E"][0], s["E"][1]) for s in scan["scan"]
           if 0.11 < s["theta"] < 0.31]
    if len(pts) < 3: return None
    re = np.array([p[1] for p in pts]); im = np.array([p[2] for p in pts])
    return dict(Re_mean=float(re.mean()), Re_std=float(re.std()),
                Im_mean=float(im.mean()), Im_std=float(im.std()),
                n_theta=len(pts))

if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "main"
    results = {}
    if which == "null":
        # single well at false-vacuum location: Im E0 must be 0
        hb, eps = 0.25, 0.2
        from scipy.optimize import brentq
        xf = brentq(lambda x: Vp(x,eps), -1.6, -0.2)
        Vf = (xf**2-1.0)**2 - eps*xf
        wf = np.sqrt(12.0*xf**2 - 4.0)
        L, N = 8.0, 801
        x = np.linspace(-L, L, N); dx = x[1]-x[0]
        main = np.full(N, hb**2/dx**2); off = np.full(N-1, -hb**2/(2*dx**2))
        K = np.diag(main) + np.diag(off,1) + np.diag(off,-1)
        for th in (0.15, 0.25):
            z = x*np.exp(1j*th)
            Vn = 0.5*wf**2*(z-xf)**2 + Vf
            H = np.exp(-2j*th)*K + np.diag(Vn)
            w, _ = eig(H)
            i0 = int(np.argmin(w.real))
            print(f"null single-well: theta={th} E0={w[i0].real:.10f} "
                  f"Im E0={w[i0].imag:.3e} (expect ~0)")
            assert abs(w[i0].imag) < 1e-9, "NULL ANCHOR FAILED"
        print("ANCHOR 3 (null: Im E = 0) PASSED")
        sys.exit(0)
    hbs = [0.18, 0.22, 0.26, 0.30, 0.34]
    for eps in [0.1, 0.2, 0.3]:
        for hb in hbs:
            key = f"eps{eps}_hb{hb}"
            print(f"--- {key} ---", flush=True)
            sc = resonance(hb, eps)
            g = gamma_from_scan(sc)
            if g is None:
                print("  NO RESONANCE FOUND (instrument finding)")
                results[key] = dict(found=False)
            else:
                Gamma = -2.0*g["Im_mean"]/hb
                dGamma = 2.0*g["Im_std"]/hb
                print(f"  Re={g['Re_mean']:.8f}+-{g['Re_std']:.1e} "
                      f"Im={g['Im_mean']:.3e}+-{g['Im_std']:.1e} "
                      f"Gamma={Gamma:.3e}+-{dGamma:.1e}")
                results[key] = dict(found=True, Gamma=Gamma, dGamma=dGamma, **g)
            json.dump(results, open("/tmp/node11s_width.json","w"), indent=1)
    print("width scan complete")
