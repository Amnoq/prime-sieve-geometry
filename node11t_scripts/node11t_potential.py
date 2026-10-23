"""
Node 11t — purpose-built open potential + bounce anchor.

V(x) = q(x)*(1-T(x)) + V_flat*T(x),  q(x) = (x^2-1)^2 - eps*x
T(x) = 1/2*(1+erf((x-xg)/w))  -- entire in z, so complex scaling is clean
(no kink, no Re(z) selection as in 11s).

Design: false well (quartic left) + barrier + smooth monotone descent to a
FLAT continuum V_flat = Vf - DROP for x >> xg.  No x^4 wall on the right.
xg sits just past the quartic turning point xtp (the descent starts where
the quartic would rise), so the Euclidean bounce region [xf, xtp'] is
essentially the quartic bounce; the glue systematic is MEASURED (Sb_glued
vs Sb_quartic) and Sb_glued is the reference for the width fit.

Charter X_c == xg here.
"""
import numpy as np, json
from scipy.optimize import brentq
from scipy.integrate import quad, solve_ivp
from scipy.special import erf

EPS = 0.2
DROP = 1.5     # V_flat = Vf - DROP
W = 0.30       # blend width
XG_OFFSET = 0.35  # xg = xtp + XG_OFFSET  (primary)

def q(x, eps=EPS):   return (x**2 - 1.0)**2 - eps*x
def qp(x, eps=EPS):  return 4.0*x*(x**2 - 1.0) - eps
def qpp(x, eps=EPS): return 12.0*x**2 - 4.0

def quartic_geometry(eps=EPS):
    xf = brentq(lambda x: qp(x, eps), -1.6, -0.2)
    xb = brentq(lambda x: qp(x, eps), -0.2,  0.2)
    xt = brentq(lambda x: qp(x, eps),  0.2,  1.6)
    Vf = q(xf, eps)
    xs = np.linspace(xb, 4.0, 20001)
    i = np.where(q(xs, eps) - Vf < 0)[0][0]
    xtp = brentq(lambda x: q(x, eps) - Vf, xs[i-1], xs[i])
    return dict(xf=xf, xb=xb, xt=xt, xtp=xtp, Vf=Vf,
                wf=float(np.sqrt(qpp(xf, eps))))

def make_V(xg, w=W, drop=DROP, eps=EPS, Vf=None):
    if Vf is None: Vf = quartic_geometry(eps)["Vf"]
    Vflat = Vf - drop
    def V(x):
        x = np.asarray(x, dtype=float)
        T = 0.5*(1.0 + erf((x - xg)/w))
        return q(x, eps)*(1.0 - T) + Vflat*T
    return V, Vflat

def V_cx(z, xg, w=W, drop=DROP, eps=EPS, Vf=None):
    """Entire analytic continuation of the glued potential."""
    if Vf is None: Vf = quartic_geometry(eps)["Vf"]
    Vflat = Vf - drop
    z = np.asarray(z, dtype=complex)
    T = 0.5*(1.0 + erf((z - xg)/w))
    return ((z**2 - 1.0)**2 - eps*z)*(1.0 - T) + Vflat*T

def Vp_glued(x, xg, w=W, drop=DROP, eps=EPS, Vf=None, h=1e-7):
    return (make_V(xg, w, drop, eps, Vf)[0](x + h) -
            make_V(xg, w, drop, eps, Vf)[0](x - h))/(2*h)

def Sb_way1_glued(xg, eps=EPS):
    """S_b = 2 int_{xf}^{xtp'} sqrt(2(V-Vf)) dx on the GLUED potential."""
    g = quartic_geometry(eps); Vf = g["Vf"]
    V, Vflat = make_V(xg, Vf=Vf)
    assert Vflat < Vf
    # turning point: V(x)=Vf to the right of xb
    f = lambda x: V(x) - Vf
    # scan from xb outward for the last crossing
    xs = np.linspace(g["xb"], xg + 3*W, 40001)
    fv = f(xs)
    # forbidden region: f>0; turning point = right edge of f>0 region
    pos = np.where(fv > 0)[0]
    assert len(pos) > 0
    i1 = pos[-1]
    xtp_p = brentq(f, xs[i1], xs[i1+1])
    val, err = quad(lambda x: np.sqrt(max(2.0*(V(x) - Vf), 0.0)),
                    g["xf"], xtp_p, limit=600)
    return 2.0*val, dict(xtp_prime=float(xtp_p), err=err, Vflat=float(Vflat))

def bounce_profile_glued(xg, eps=EPS, delta=1e-8, n_out=20001):
    """Forward+reflect bounce on the glued potential (11s method)."""
    g = quartic_geometry(eps); Vf = g["Vf"]
    V, _ = make_V(xg, Vf=Vf)
    def rhs(t, y):
        return [y[1], Vp_glued(y[0], xg, Vf=Vf)]
    x0 = g["xf"] + delta
    v0 = float(np.sqrt(max(2.0*(V(x0) - Vf), 0.0)))
    def hit_turn(t, y): return y[1]
    hit_turn.terminal = True; hit_turn.direction = -1
    sol = solve_ivp(rhs, [0, 120.0], [x0, v0], events=hit_turn,
                    rtol=1e-12, atol=1e-14, max_step=0.02, dense_output=True)
    assert len(sol.t_events[0]) > 0, "turning point not reached"
    Th = sol.t_events[0][0]
    tau_h = np.linspace(0.0, Th, n_out//2 + 1)
    x_h = sol.sol(tau_h)[0]; v_h = sol.sol(tau_h)[1]
    tau = np.concatenate([-tau_h[::-1][1:], tau_h])
    xbf = np.concatenate([x_h[::-1][1:], x_h])
    vbf = np.concatenate([-v_h[::-1][1:], v_h])
    return dict(tau=tau, xb=xbf, T2=Th, Sb_way2=float(np.trapz(vbf**2, tau)),
                xturn=float(x_h[-1]))

if __name__ == "__main__":
    g = quartic_geometry()
    print("quartic geometry (eps=0.2):")
    print(f"  xf={g['xf']:.8f} xb={g['xb']:.8f} xt={g['xt']:.8f} "
          f"xtp={g['xtp']:.8f} Vf={g['Vf']:.8f} wf={g['wf']:.6f}")
    # quartic reference Sb (11s value: 2.9185048151)
    s_q, _ = quad(lambda x: np.sqrt(max(2.0*(q(x)-g["Vf"]), 0.0)),
                  g["xf"], g["xtp"], limit=600)
    print(f"  Sb_quartic(quad) = {2*s_q:.10f}  (11s: 2.9185048151)")
    out = {}
    for off in [0.20, 0.35, 0.50]:
        xg = g["xtp"] + off
        s1, info = Sb_way1_glued(xg)
        prof = bounce_profile_glued(xg)
        s2 = prof["Sb_way2"]
        rel = abs(s1 - s2)/s1
        glue_sys = (s1 - 2*s_q)/(2*s_q)
        print(f"xg=xtp+{off:.2f}={xg:.4f}: Sb_quad={s1:.10f} "
              f"Sb_prof={s2:.10f} rel={rel:.2e} "
              f"xtp'={info['xtp_prime']:.6f} vs xtp={g['xtp']:.6f} "
              f"glue_shift={glue_sys:+.3e}")
        assert rel < 1e-8, "ANCHOR 1 FAILED"
        out[f"xg_off_{off}"] = dict(xg=xg, Sb=s1, rel_diff=rel,
                                    xtp_prime=info["xtp_prime"],
                                    glue_shift=glue_sys, T2=prof["T2"])
    json.dump(dict(geometry={k: float(v) for k, v in g.items()},
                   Sb_quartic=2*s_q, xg_scan=out),
              open("/home/hatch/workspace/prime-sieve-geometry/"
                   "node11t_scripts/potential.json", "w"), indent=1)
    print("ANCHOR 1 (S_b two-way on glued potential) PASSED")
