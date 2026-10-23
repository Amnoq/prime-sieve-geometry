"""
Node 11s — 1-loop prefactor, determinant ratio via spectral product
with EXPLICIT zero-mode projection (no eigenvalue-magnitude guessing).

R = det'(M_b)/det(M_f); log|R| = sum_{k != zero} log|lam^b_k| - sum_j log(lam^f_j).
zero = argmax_k |<U_k | xdot_b>|  (analytic zero mode known).
The O(dt) discretization error sits IN the zero eigenvalue; excluding it
by overlap removes the contamination. Convergence checked in T and N.
K(eps,hb) = sqrt(S_b/(2*pi*hb)) * |R|^{-1/2}.
Gamma_bounce = K * exp(-S_b/hb).
"""
import numpy as np, json
from numpy.linalg import eigh

def logR_spectral(eps, T2, N):
    d = np.load(f"/tmp/bounce_eps{eps}.npz")
    tau0, xb0 = d["tau"], d["xb"]
    info = json.load(open("/tmp/node11s_Sb.json"))[str(eps)]
    Sb, wf = info["Sb"], info["wf"]
    assert T2 <= tau0[-1]
    tau = np.linspace(-T2, T2, N); dt = tau[1]-tau[0]
    xb = np.interp(tau, tau0, xb0)
    main = np.full(N, 2.0/dt**2); off = np.full(N-1, -1.0/dt**2)
    D2 = np.diag(main) + np.diag(off, 1) + np.diag(off, -1)
    Mb = D2 + np.diag(12.0*xb**2 - 4.0)
    Mf = D2 + np.diag(np.full(N, wf**2))
    lb, Ub = eigh(Mb)
    lf = eigh(Mf)[0]
    # analytic zero mode
    v = np.gradient(xb, tau); v /= np.linalg.norm(v)
    ov = np.abs(Ub.T @ v)
    iz = int(np.argmax(ov))
    # negative modes (excluding zero)
    mask = np.ones(N, bool); mask[iz] = False
    nneg = int(np.sum(lb[mask] < 0))
    logR = np.sum(np.log(np.abs(lb[mask]))) - np.sum(np.log(lf))
    return dict(logR=logR, R=np.exp(logR), nneg=nneg,
                zero_ov=float(ov[iz]), zero_lam=float(lb[iz]),
                T2=T2, N=N, Sb=Sb)

if __name__ == "__main__":
    out = {}
    for eps in [0.1, 0.2, 0.3]:
        info = json.load(open("/tmp/node11s_Sb.json"))[str(eps)]
        Tfull = info["T2"]
        print(f"--- eps={eps} ---")
        res = {}
        for Tfrac in [0.7, 0.85, 1.0]:
            for N in [1000, 1600]:
                r = logR_spectral(eps, Tfrac*Tfull, N)
                key = f"T{Tfrac}_N{N}"
                res[key] = {k: (float(v) if isinstance(v, (int,float,np.floating)) else v)
                            for k, v in r.items()}
                print(f"  Tfrac={Tfrac} N={N}: log|R|={r['logR']:+.5f} "
                      f"nneg={r['nneg']} zero_ov={r['zero_ov']:.4f}")
        lrs = [res[k]["logR"] for k in res]
        print(f"  spread: {max(lrs)-min(lrs):.3e}")
        out[str(eps)] = res
    json.dump(out, open("/tmp/node11s_R2.json","w"), indent=1)
