"""
Node 11s — 1-loop prefactor via GY with mu-shift (zero-mode-free).
R = det'(M_b)/det(M_f) = lim_{mu->0} D(mu,T)/mu^2,
D(mu,T) = y_b^{(mu)}(T/2)/y_f(T/2),
y_b^{(mu)} solves (-d^2/dtau^2 + V''(x_b(tau)) + mu^2) y = 0,
y(-T/2)=0, y'(-T/2)=1.  Valid for lam_zero << mu^2 << |lam_neg|, lam_1.
Verified by mu-plateau: D(mu)/mu^2 independent of mu.
"""
import numpy as np, json
from scipy.integrate import solve_ivp

def gy_ratio(eps, mu, T2, n_interp=20001):
    d = np.load(f"/tmp/bounce_eps{eps}.npz")
    tau0, xb0 = d["tau"], d["xb"]
    info = json.load(open("/tmp/node11s_Sb.json"))[str(eps)]
    wf = info["wf"]
    Tfull = tau0[-1]
    assert T2 <= Tfull
    # V''(x_b(tau)) interpolant
    Vpp = 12.0*xb0**2 - 4.0
    def W(tau):
        return np.interp(tau, tau0, Vpp)
    def rhs(t, y):
        return [y[1], (W(t) + mu**2)*y[0]]
    sol = solve_ivp(rhs, [-T2, T2], [0.0, 1.0],
                    rtol=1e-12, atol=1e-14, max_step=0.02,
                    dense_output=True)
    yb = sol.sol(T2)[0]
    # M_f on [-T2,T2]: y_f(-T2)=0, y_f'(-T2)=1 -> y_f(T2)=sinh(2*wf*T2)/wf
    yf = np.sinh(2.0*wf*T2)/wf
    return yb/yf

if __name__ == "__main__":
    out = {}
    for eps in [0.1, 0.2, 0.3]:
        info = json.load(open("/tmp/node11s_Sb.json"))[str(eps)]
        T2 = info["T2"]
        print(f"--- eps={eps} (T2={T2:.2f}) ---")
        res = {}
        for mu in [3e-4, 1e-3, 3e-3]:
            D = gy_ratio(eps, mu, T2)
            R = D/mu**2
            res[str(mu)] = dict(D=D, R=R)
            print(f"  mu={mu:.0e}: D={D:.6e}  R=D/mu^2={R:+.6e}")
        # T-convergence at mu=1e-3
        for Tfrac in [0.8, 1.0]:
            D = gy_ratio(eps, 1e-3, Tfrac*T2)
            print(f"  Tfrac={Tfrac}: R={D/1e-6:+.6e}")
        out[str(eps)] = res
    json.dump(out, open("/tmp/node11s_R.json","w"), indent=1)
