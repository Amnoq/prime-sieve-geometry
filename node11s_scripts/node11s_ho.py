"""
Node 11s — (a) Gamma_exact via complex scaling in HO basis (primary instrument).
HO basis centered at xf (false minimum), frequency Om=wf.
H(theta) = e^{-2iθ} p^2/2 + V(xf + y e^{iθ}), y = x - xf.
All operators via ladder matrices — exact polynomial matrix elements,
exponential convergence in N. Cross-checks the FD pipeline.
Gamma = -2*Im(E_res)/hb.
"""
import numpy as np, json, sys
from scipy.linalg import eig
from scipy.optimize import brentq

def Vp(x, eps): return 4.0*x*(x**2 - 1.0) - eps

def ho_mats(N, hb, Om):
    n = np.arange(N, dtype=float)
    a = np.diag(np.sqrt(n[1:]), 1)   # a|n> = sqrt(n)|n-1>  (lowering on kets)
    ad = a.T
    c = np.sqrt(hb/(2.0*Om))
    y = c*(a + ad)
    Hho = np.diag(hb*Om*(n + 0.5))
    p2o2 = Hho - 0.5*Om**2*(y @ y)
    return y, p2o2

def H_theta(N, hb, eps, xf, Om, theta):
    y, p2o2 = ho_mats(N, hb, Om)
    e = np.exp(1j*theta)
    w = y*e
    X = xf*np.eye(N) + w
    X2 = X @ X
    Vmat = (X2 - np.eye(N)) @ (X2 - np.eye(N)) - eps*X
    return np.exp(-2j*theta)*p2o2 + Vmat

def scan(hb, eps, thetas, N=120):
    xf = brentq(lambda x: Vp(x, eps), -1.6, -0.2)
    wf = np.sqrt(12.0*xf**2 - 4.0)
    Vf = (xf**2 - 1.0)**2 - eps*xf
    Ef = Vf + hb*wf/2.0
    out = []
    for th in thetas:
        H = H_theta(N, hb, eps, xf, wf, th)
        w, vr = eig(H)
        # resonance: Re near Ef, small Im<0, <y> near 0 (localized at xf)
        y, _ = ho_mats(N, hb, wf)
        best = None
        for i in range(N):
            if abs(w[i].real - Ef) < 0.5 and -0.05 < w[i].imag < 0.0:
                psi = vr[:, i]
                # <y> via normalized |psi|^2 (diagnostic only)
                nn = np.sum(np.abs(psi)**2)
                yexp = float(np.real(np.conj(psi) @ (y @ psi))/nn)
                if abs(yexp) < 0.6:
                    if best is None or abs(w[i].imag) < abs(w[best].imag):
                        best = i
        if best is not None:
            out.append(dict(theta=th, E=[float(w[best].real),
                                        float(w[best].imag)]))
    return dict(Ef=float(Ef), xf=float(xf), wf=float(wf), scan=out)

if __name__ == "__main__":
    thetas = [0.10, 0.15, 0.20, 0.25, 0.30]
    if len(sys.argv) > 1 and sys.argv[1] == "validate":
        # theta=0 must reproduce FD ground truths (real spectrum)
        for N in [60, 90, 120, 150]:
            s = scan(0.25, 0.2, [0.0], N=N)
            H = H_theta(N, 0.25, 0.2, s["xf"], s["wf"], 0.0)
            w, _ = eig(H)
            w = np.sort(w.real)
            print(f"N={N}: E0={w[0]:.10f} E1={w[1]:.10f} "
                  f"(FD: E0~0.1974+0.25*wt/2 true well; Ef_guess={s['Ef']:.6f})")
        sys.exit(0)
    if len(sys.argv) > 1 and sys.argv[1] == "null":
        # single HO at xf: Im E0 must be 0 (tests basis, not box)
        hb, eps = 0.25, 0.2
        xf = brentq(lambda x: Vp(x, eps), -1.6, -0.2)
        wf = np.sqrt(12.0*xf**2 - 4.0)
        Vf = (xf**2-1.0)**2 - eps*xf
        for N in [60, 100]:
            for th in [0.15, 0.25]:
                y, p2o2 = ho_mats(N, hb, wf)
                e = np.exp(1j*th)
                # V_null = 0.5*wf^2*(y e^{iθ})^2 + Vf  (HO about xf)
                Vn = 0.5*wf**2*(e**2)*(y @ y) + Vf*np.eye(N)
                H = np.exp(-2j*th)*p2o2 + Vn
                w, _ = eig(H)
                i0 = int(np.argmin(abs(w - (Vf+hb*wf/2))))
                print(f"HO-basis null N={N} th={th}: "
                      f"E0={w[i0].real:.10f} Im={w[i0].imag:.3e}")
        sys.exit(0)
    # convergence in N for a resonance point
    hb, eps = 0.30, 0.2
    for N in [80, 100, 120, 150]:
        s = scan(hb, eps, thetas, N=N)
        ims = [p["E"][1] for p in s["scan"]]
        res = [p["E"][0] for p in s["scan"]]
        print(f"N={N}: n_found={len(s['scan'])} "
              f"Re={np.mean(res):.8f}+-{np.std(res):.1e} "
              f"Im={np.mean(ims):.3e}+-{np.std(ims):.1e}")
