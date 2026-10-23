"""
Node 11t — Gamma_exact from complex-scaled FD on the purpose-built open
potential (false well + barrier + erf-blend to FLAT continuum, no x^4 wall).

V_cx(z) is entire (erf) -> dilation-analytic; no kink, no Re(z) selection.
Gamma = -2*Im(E_res)/hb.  Resonance: Re E near Vf+hb*wf/2, small Im E < 0,
eigenfunction localized left of the barrier.  Richardson in dx^2 per
(11s: artifact scales as dx^2, measured /4.00 per doubling on the null).
"""
import numpy as np, json, sys
from scipy.linalg import eig
from node11t_potential import (V_cx, quartic_geometry, EPS)

def scan_width(hb, xg, L=12.0, N=801, thetas=(0.15, 0.20, 0.25),
               im_window=0.02, left_frac=0.6):
    g = quartic_geometry(EPS)
    Ef = g["Vf"] + hb*g["wf"]/2.0
    x = np.linspace(-L, L, N); dx = x[1] - x[0]
    main = np.full(N, hb**2/dx**2); off = np.full(N-1, -hb**2/(2*dx**2))
    K = np.diag(main) + np.diag(off, 1) + np.diag(off, -1)
    out = []
    for th in thetas:
        z = x*np.exp(1j*th)
        H = np.exp(-2j*th)*K + np.diag(V_cx(z, xg))
        w, vr = eig(H)
        best = None
        for i in range(N):
            if abs(w[i].real - Ef) < 0.5 and -im_window < w[i].imag < 0.0:
                psi = vr[:, i]
                left = (np.sum(np.abs(psi[x < g["xb"]])**2) /
                        np.sum(np.abs(psi)**2))
                if left > left_frac and (best is None or
                                         abs(w[i].imag) < abs(w[best].imag)):
                    best = i
        if best is not None:
            out.append(dict(theta=th, E=[float(w[best].real),
                                        float(w[best].imag)]))
    return dict(Ef=float(Ef), xg=float(xg), scan=out, L=L, N=N, dx=float(dx))

def richardson_gamma(hb, ims, dxs):
    # Im = a + b*dx^2 -> a ; Gamma = -2a/hb
    X = np.array(dxs)**2
    A = np.column_stack([np.ones_like(X), X])
    coef, res, *_ = np.linalg.lstsq(A, np.array(ims), rcond=None)
    dof = max(len(ims) - 2, 1)
    resid = float(np.sum((np.array(ims) - A@coef)**2))
    return dict(Im_inf=float(coef[0]), slope=float(coef[1]),
                Gamma=float(-2*coef[0]/hb),
                resid_rms=float(np.sqrt(resid/dof)))

def gamma_at(hb, xg, Ns=(801, 1201), thetas=(0.15, 0.20, 0.25), L=12.0):
    """Richardson-extrapolated Gamma per theta, then theta-plateau."""
    per_theta = {th: ([], []) for th in thetas}
    for N in Ns:
        s = scan_width(hb, xg, L=L, N=N, thetas=thetas)
        for rec in s["scan"]:
            per_theta[rec["theta"]][0].append(rec["E"][1])
            per_theta[rec["theta"]][1].append(s["dx"])
    thetas_out = []
    for th in thetas:
        ims, dxs = per_theta[th]
        if len(ims) < 2:
            continue
        r = richardson_gamma(hb, ims, dxs)
        r["theta"] = th
        thetas_out.append(r)
    if not thetas_out:
        return dict(found=False)
    Gs = np.array([t["Gamma"] for t in thetas_out])
    return dict(found=True, Gamma=float(Gs.mean()),
                dGamma_theta=float(Gs.std()),
                thetas=thetas_out)

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "probe"
    pot = json.load(open("/home/hatch/workspace/prime-sieve-geometry/"
                         "node11t_scripts/potential.json"))
    xg_primary = pot["xg_scan"]["xg_off_0.35"]["xg"]
    if mode == "probe":
        # single-point pipeline validation
        hb = 0.35
        print(f"probe: hb={hb} xg={xg_primary:.4f}")
        for N in [801, 1201]:
            s = scan_width(hb, xg_primary, N=N)
            for rec in s["scan"]:
                print(f"  N={N} th={rec['theta']:.2f} "
                      f"Re={rec['E'][0]:.8f} Im={rec['E'][1]:.4e}")
        g = gamma_at(hb, xg_primary)
        print(f"  => Gamma={g['Gamma']:.4e} +- {g['dGamma_theta']:.1e} "
              f"(theta spread)")
    elif mode == "full":
        # primary scan: 5 hb x 3 theta x 2 N, then xg controls
        results = {}
        hbs = [0.28, 0.32, 0.36, 0.40, 0.44]
        print("=== primary xg ===", flush=True)
        for hb in hbs:
            g = gamma_at(hb, xg_primary)
            results[f"xg_primary_hb{hb}"] = g
            print(f"hb={hb}: Gamma={g.get('Gamma', float('nan')):.4e} "
                  f"+-{g.get('dGamma_theta', float('nan')):.1e}", flush=True)
            json.dump(results, open("/home/hatch/workspace/"
                                    "prime-sieve-geometry/node11t_scripts/"
                                    "width.json", "w"), indent=1)
        for off_key, hbs_c in [("xg_off_0.2", [0.35, 0.45]),
                               ("xg_off_0.5", [0.35, 0.45])]:
            xg = pot["xg_scan"][off_key]["xg"]
            print(f"=== control {off_key} xg={xg:.4f} ===", flush=True)
            for hb in hbs_c:
                g = gamma_at(hb, xg)
                results[f"{off_key}_hb{hb}"] = g
                print(f"hb={hb}: Gamma={g.get('Gamma', float('nan')):.4e} "
                      f"+-{g.get('dGamma_theta', float('nan')):.1e}",
                      flush=True)
                json.dump(results, open("/home/hatch/workspace/"
                                        "prime-sieve-geometry/node11t_scripts/"
                                        "width.json", "w"), indent=1)
        print("full width scan complete")
