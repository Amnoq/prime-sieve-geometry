"""
Node 11s — 1-loop prefactor K(eps) = sqrt(S_b/(2*pi*hbar)) * |det'(M_b)/det(M_f)|^{-1/2}
via direct spectral ratio on FD grid. M_b = -d^2/dtau^2 + V''(x_b(tau)),
M_f = -d^2/dtau^2 + wf^2. det' excludes the eigenvalue closest to zero
(the time-translation zero mode); the negative mode is kept (|.|).
Convergence checked in T (interval truncation) and N (grid).
"""
import numpy as np, json
from numpy.linalg import eigh

def Vpp(x): return 12.0*x**2 - 4.0

def log_ratio(eps, T2, N):
    d = np.load(f"/tmp/bounce_eps{eps}.npz")
    tau0, xb0 = d["tau"], d["xb"]
    Tfull = tau0[-1]
    assert T2 <= Tfull
    tau = np.linspace(-T2, T2, N)
    dt = tau[1]-tau[0]
    xb = np.interp(tau, tau0, xb0)
    info = json.load(open("/tmp/node11s_Sb.json"))[str(eps)]
    wf = info["wf"]
    # FD second derivative, Dirichlet BC
    main = np.full(N, 2.0/dt**2)
    off = np.full(N-1, -1.0/dt**2)
    D2 = np.diag(main) + np.diag(off, 1) + np.diag(off, -1)
    Wb = Vpp(xb)
    Mb = D2 + np.diag(Wb)
    Mf = D2 + np.diag(np.full(N, wf**2))
    lb = eigh(Mb)[0]
    lf = eigh(Mf)[0]
    # identify: one negative mode, one ~zero mode
    neg = lb[lb < -1e-8]
    assert len(neg) == 1, f"eps={eps}: {len(neg)} negative modes"
    izero = int(np.argmin(np.abs(lb)))
    assert abs(lb[izero]) < 1e-3, f"eps={eps}: no near-zero mode, min|lb|={abs(lb[izero]):.2e}"
    mask = np.ones(N, bool); mask[izero] = False
    logr = np.log(abs(lb[0])) + np.sum(np.log(lb[mask][1:])) - np.sum(np.log(lf))
    # note: lb[mask][0] is the negative mode (lb sorted); lb[0]==neg mode
    return logr, dict(neg_mode=float(lb[0]), zero_mode=float(lb[izero]),
                      T2=T2, N=N)

if __name__ == "__main__":
    out = {}
    for eps in [0.1, 0.2, 0.3]:
        info = json.load(open("/tmp/node11s_Sb.json"))[str(eps)]
        Tfull = info["T2"]
        print(f"--- eps={eps} (Tfull={Tfull:.2f}) ---")
        res = {}
        for Tfrac in [0.7, 0.85, 1.0]:
            for N in [1200, 2000]:
                lr, det = log_ratio(eps, Tfrac*Tfull, N)
                key = f"Tfrac{Tfrac}_N{N}"
                res[key] = dict(log_ratio=lr, **det)
                print(f"  Tfrac={Tfrac} N={N}: log|det'/det|={lr:+.6f} "
                      f"neg={det['neg_mode']:.4f} zero={det['zero_mode']:.2e}")
        lrs = [res[k]["log_ratio"] for k in res]
        spread = max(lrs)-min(lrs)
        print(f"  spread over (T,N): {spread:.2e}")
        out[str(eps)] = res
    json.dump(out, open("/tmp/node11s_prefactor.json","w"), indent=1)
