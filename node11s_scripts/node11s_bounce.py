"""
Node 11s — bounce action S_b for V(x;eps) = (x^2-1)^2 - eps*x.
ANCHOR 1: two independent S_b computations must agree (quadrature vs
bounce-profile integral). Stated accuracy target: 1e-6 relative.
Saves bounce profile for the prefactor script.
"""
import numpy as np, json
from scipy.optimize import brentq
from scipy.integrate import quad

def V(x, eps):  return (x**2 - 1.0)**2 - eps*x
def Vp(x, eps): return 4.0*x*(x**2 - 1.0) - eps
def Vpp(x, eps): return 12.0*x**2 - 4.0

def stationary(eps):
    xf = brentq(lambda x: Vp(x, eps), -1.6, -0.2)  # false vacuum (left)
    xb = brentq(lambda x: Vp(x, eps), -0.2,  0.2)  # barrier top
    xt = brentq(lambda x: Vp(x, eps),  0.2,  1.6)  # true vacuum (right)
    return xf, xb, xt

def turning(eps, xf, xb):
    Vf = V(xf, eps)
    xs = np.linspace(xb, 4.0, 20001)
    f = V(xs, eps) - Vf
    i = np.where(f < 0)[0][0]
    return brentq(lambda x: V(x, eps) - Vf, xs[i-1], xs[i])

def Sb_way1(eps):
    """S_b = 2 * int_{xf}^{xtp} sqrt(2(V-Vf)) dx  (quadrature)."""
    xf, xb, xt = stationary(eps)
    Vf = V(xf, eps)
    xtp = turning(eps, xf, xb)
    val, err = quad(lambda x: np.sqrt(max(2.0*(V(x, eps)-Vf), 0.0)),
                    xf, xtp, limit=400)
    return 2.0*val, dict(xf=xf, xb=xb, xt=xt, xtp=xtp, Vf=Vf, err=err)

def bounce_profile(eps, delta=1e-8, n_out=20001):
    """Bounce x_b(tau): integrate FORWARD from xf+delta along the
    unstable manifold (v=+sqrt(2(V-Vf))) to the turning point (v=0),
    then reflect: x_b(-tau)=x_b(tau). The return leg is replaced by
    symmetry (it is numerically unstable forward in time).
    Returns dict with uniform tau grid, xb, T2, and way-2 S_b."""
    from scipy.integrate import solve_ivp
    xf, xb, xt = stationary(eps)
    Vf = V(xf, eps)
    xtp = turning(eps, xf, xb)
    x0 = xf + delta
    v0 = float(np.sqrt(max(2.0*(V(x0, eps)-Vf), 0.0)))
    def rhs(t, y):
        return [y[1], Vp(y[0], eps)]
    def hit_turn(t, y): return y[1]  # v = 0 at turning point
    hit_turn.terminal = True; hit_turn.direction = -1
    sol = solve_ivp(rhs, [0, 100.0], [x0, v0], events=hit_turn,
                    rtol=1e-12, atol=1e-14, max_step=0.02,
                    dense_output=True)
    assert len(sol.t_events[0]) > 0, "turning point not reached"
    Th = sol.t_events[0][0]
    tau_h = np.linspace(0.0, Th, n_out//2 + 1)
    x_h = sol.sol(tau_h)[0]; v_h = sol.sol(tau_h)[1]
    # check: turning point matches xtp
    assert abs(x_h[-1]-xtp) < 1e-6, f"turn at {x_h[-1]} vs xtp {xtp}"
    tau = np.concatenate([-tau_h[::-1][1:], tau_h])
    xbf = np.concatenate([x_h[::-1][1:], x_h])
    vbf = np.concatenate([-v_h[::-1][1:], v_h])
    Sb2 = float(np.trapz(vbf**2, tau))
    return dict(tau=tau, xb=xbf, T2=Th, Sb_way2=Sb2,
                xf=xf, xb_bar=xb, xt=xt, xtp=xtp, Vf=Vf)

if __name__ == "__main__":
    out = {}
    for eps in [0.1, 0.2, 0.3]:
        s1, info = Sb_way1(eps)
        prof = bounce_profile(eps)
        s2 = prof["Sb_way2"]
        rel = abs(s1-s2)/s1
        wf = float(np.sqrt(Vpp(info["xf"], eps)))
        print(f"eps={eps}: Sb_quad={s1:.10f}  Sb_prof={s2:.10f}  "
              f"rel.diff={rel:.2e}  T2={prof['T2']:.3f}  wf={wf:.4f}  "
              f"xf={info['xf']:.6f} xtp={info['xtp']:.6f}")
        assert rel < 1e-6, "ANCHOR 1 FAILED"
        out[str(eps)] = dict(Sb=s1, rel_diff=rel, T2=prof["T2"], wf=wf,
                             xf=info["xf"], xb=info["xb"], xt=info["xt"],
                             xtp=info["xtp"], Vf=info["Vf"])
        np.savez(f"/tmp/bounce_eps{eps}.npz", tau=prof["tau"], xb=prof["xb"])
    json.dump(out, open("/tmp/node11s_Sb.json","w"), indent=1)
    print("ANCHOR 1 (S_b two-way) PASSED")
