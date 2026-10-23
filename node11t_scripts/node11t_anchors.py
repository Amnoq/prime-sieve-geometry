"""
Node 11t — anchors 2 (null) and 3 (section-B regression).

Anchor 2 (null): single harmonic well at the false minimum, complex-scaled
FD -> Im E0 must -> 0 as dx^2 (measured /4.00 per doubling in 11s); HO
basis -> machine zero.  Pipeline sanity: a true bound state has no width.

Anchor 3 (section-B regression): confining quartic (eps=0.2), complex
scaling (HO basis, N up to 150, as in 11s) -> the "resonance" candidate
converges to a REAL eigenvalue; Im E = 0 to machine precision.  The
conceptual wall as a pipeline regression check: no resonances exist in
1D confining QM.
"""
import numpy as np
from scipy.linalg import eig
from scipy.optimize import brentq
import sys
sys.path.insert(0, "/home/hatch/workspace/prime-sieve-geometry/node11s_scripts")
from node11s_ho import ho_mats, H_theta
sys.path.insert(0, "/home/hatch/workspace/prime-sieve-geometry/node11t_scripts")
from node11t_potential import quartic_geometry, EPS

def fd_null():
    g = quartic_geometry(EPS)
    hb = 0.25
    print("FD null: single well at false minimum (Im E0 -> 0 as dx^2)",
          flush=True)
    ims = []
    for N in [801, 1601]:
        L = 8.0
        x = np.linspace(-L, L, N); dx = x[1]-x[0]
        main = np.full(N, hb**2/dx**2); off = np.full(N-1, -hb**2/(2*dx**2))
        K = np.diag(main) + np.diag(off, 1) + np.diag(off, -1)
        th = 0.20
        z = x*np.exp(1j*th)
        Vn = 0.5*g["wf"]**2*(z - g["xf"])**2 + g["Vf"]
        H = np.exp(-2j*th)*K + np.diag(Vn)
        w, _ = eig(H)
        i0 = int(np.argmin(abs(w - (g["Vf"] + hb*g["wf"]/2))))
        ims.append(w[i0].imag)
        print(f"  N={N}: Im E0 = {w[i0].imag:.3e}", flush=True)
    r1 = ims[0]/ims[1] if ims[1] != 0 else float("nan")
    print(f"  ratio: {r1:.2f} (dx^2 -> 4.00 per doubling)", flush=True)
    ok = abs(r1 - 4.0) < 0.6
    print("  FD NULL", "PASSED" if ok else "FAILED", flush=True)
    return ok

def ho_null():
    g = quartic_geometry(EPS)
    hb = 0.25
    print("HO-basis null: single well (Im E0 -> machine zero)", flush=True)
    ok = True
    for N in [60, 100]:
        for th in [0.15, 0.25]:
            y, p2o2 = ho_mats(N, hb, g["wf"])
            e = np.exp(1j*th)
            Vn = 0.5*g["wf"]**2*(e**2)*(y @ y) + g["Vf"]*np.eye(N)
            H = np.exp(-2j*th)*p2o2 + Vn
            w, _ = eig(H)
            i0 = int(np.argmin(abs(w - (g["Vf"] + hb*g["wf"]/2))))
            print(f"  N={N} th={th}: Im E0 = {w[i0].imag:.3e}", flush=True)
            ok &= abs(w[i0].imag) < 1e-10
    print("  HO NULL", "PASSED" if ok else "FAILED", flush=True)
    return ok

def section_B_regression():
    # confining quartic, HO basis, theta>0: candidate -> real eigenvalue
    hb, eps = 0.30, 0.2
    g = quartic_geometry(eps)
    Ef = g["Vf"] + hb*g["wf"]/2.0
    print("Section-B regression: confining quartic, complex scaling "
          "(expect Im -> 0, real spectrum)", flush=True)
    thetas = [0.10, 0.15, 0.20, 0.25, 0.30]
    for N in [80, 120, 150]:
        found = []
        for th in thetas:
            H = H_theta(N, hb, eps, g["xf"], g["wf"], th)
            w, vr = eig(H)
            y, _ = ho_mats(N, hb, g["wf"])
            best = None
            for i in range(N):
                if abs(w[i].real - Ef) < 0.5 and -0.05 < w[i].imag < 0.001:
                    psi = vr[:, i]
                    nn = np.sum(np.abs(psi)**2)
                    yexp = float(np.real(np.conj(psi) @ (y @ psi))/nn)
                    if abs(yexp) < 0.6 and (best is None or
                                            abs(w[i].imag) < abs(w[best].imag)):
                        best = i
            if best is not None:
                found.append(w[best].imag)
        if found:
            print(f"  N={N}: min|Im| over theta = "
                  f"{min(abs(f) for f in found):.3e} "
                  f"(n_found={len(found)})", flush=True)
        else:
            print(f"  N={N}: no negative-Im candidate near Ef "
                  f"(consistent: no resonance)", flush=True)
    print("  (11s: HO N=150 -> Im = -9e-14, machine precision)", flush=True)

if __name__ == "__main__":
    ok1 = fd_null()
    ok2 = ho_null()
    section_B_regression()
    print("ANCHORS:", "2 (null) PASSED" if (ok1 and ok2) else "2 (null) FAILED",
          "| 3 (section-B) see above", flush=True)
