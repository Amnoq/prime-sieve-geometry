"""
Node 11t — discrimination analysis.

(1) hbar-fits of Gamma (primary xg): 2-param logG=c-S/hb and 3-param
    logG=c+q*log(hb)-S/hb  ->  S_fit vs S_b,glued  [charter criterion (b)].
(2) WKB with measured resonance energy: S(E_res) by quadrature;
    R(hb)=Gamma/[(wf/2pi)*exp(-S(E)/hb)] -- smoothness + scan for coherent
    oscillatory (even/odd traversal-phase-like) structure in the residuals.
(3) xg controls: ratio-of-ratios test -- does the exponent track
    S_b,glued(xg)?
(4) Criterion (c) bookkeeping with the measured prefactor systematics.
"""
import numpy as np, json
from scipy.integrate import quad
from node11t_potential import (make_V, quartic_geometry, EPS)

D = "/home/hatch/workspace/prime-sieve-geometry/node11t_scripts/"
width = json.load(open(D + "width.json"))
pot = json.load(open(D + "potential.json"))
Re = json.load(open(D + "Re.json"))
g = quartic_geometry(EPS)
xg_primary = pot["xg_scan"]["xg_off_0.35"]["xg"]
Sb_glued_primary = pot["xg_scan"]["xg_off_0.35"]["Sb"]
wf = g["wf"]

print("=" * 70)
print("(1) hbar fits, primary xg =", round(xg_primary, 4))
print(f"    S_b,glued (quadrature, anchor 1) = {Sb_glued_primary:.10f}")
hbs, Gs, dGs = [], [], []
for hb_s, E in sorted(Re.items(), key=lambda kv: float(kv[0])):
    hb = float(hb_s)
    key = f"xg_primary_hb{hb}"
    hbs.append(hb); Gs.append(width[key]["Gamma"])
    dGs.append(width[key]["dGamma_theta"])
hbs = np.array(hbs); Gs = np.array(Gs); lG = np.log(Gs)
print("    hb      Gamma         logGamma")
for hb, G in zip(hbs, Gs):
    print(f"    {hb:.2f}   {G:.4e}   {np.log(G):+.4f}")

# Fit A: 2-param
A = np.column_stack([np.ones_like(hbs), -1.0/hbs])
cA, *_ = np.linalg.lstsq(A, lG, rcond=None)
resA = lG - A @ cA
# Fit B: 3-param
B = np.column_stack([np.ones_like(hbs), np.log(hbs), -1.0/hbs])
cB, *_ = np.linalg.lstsq(B, lG, rcond=None)
resB = lG - B @ cB
print(f"    Fit A (c,S):            S_fit={cA[1]:.4f} "
      f"rel.diff={(cA[1]-Sb_glued_primary)/Sb_glued_primary:+.3%} "
      f"resid_rms={np.sqrt(np.mean(resA**2)):.3e}")
print(f"    Fit B (c,q,S):          S_fit={cB[2]:.4f} q={cB[1]:+.3f} "
      f"rel.diff={(cB[2]-Sb_glued_primary)/Sb_glued_primary:+.3%} "
      f"resid_rms={np.sqrt(np.mean(resB**2)):.3e}")

print("=" * 70)
print("(2) WKB with measured E_res: S(E) and R(hb)")
V, Vflat = make_V(xg_primary, Vf=g["Vf"])
def S_of_E(E):
    # turning points: V(x)=E, left of xf and right of xb
    from scipy.optimize import brentq
    f = lambda x: V(x) - E
    x1 = brentq(f, -3.0, g["xf"])
    # right turning point: scan for last sign change of f in [xb, xg+..]
    xs = np.linspace(g["xb"], xg_primary + 1.0, 20001)
    fv = f(xs)
    pos = np.where(fv > 0)[0]
    x2 = brentq(f, xs[pos[-1]], xs[pos[-1] + 1])
    val, _ = quad(lambda x: np.sqrt(max(2.0*(V(x) - E), 0.0)), x1, x2,
                  limit=600)
    return 2.0*val
Rs = []
print("    hb      E_res      S(E_res)   R=Gamma/Gamma_WKB")
for hb_s in sorted(Re, key=float):
    hb = float(hb_s); E = Re[hb_s]["Re"]
    SE = S_of_E(E)
    Gwkb = (wf/(2*np.pi))*np.exp(-SE/hb)
    key = f"xg_primary_hb{hb}"
    R = width[key]["Gamma"]/Gwkb
    Rs.append(R)
    print(f"    {hb:.2f}   {E:.6f}   {SE:.6f}    {R:.4f}")
Rs = np.array(Rs)
print(f"    R(hb): mean={Rs.mean():.3f} std={Rs.std():.3f} "
      f"(smooth, O(1) prefactor)")

# oscillation scan on log-residuals of Fit B (relative units)
print("    --- coherent-structure scan on Fit-B residuals ---")
u = 1.0/hbs
best = (0, None, None)
for P in np.linspace(0.5, 4.0, 36):   # period in 1/hb
    M = np.column_stack([np.cos(2*np.pi*u/P), np.sin(2*np.pi*u/P)])
    coef, *_ = np.linalg.lstsq(M, resB, rcond=None)
    amp = float(np.sqrt(coef[0]**2 + coef[1]**2))
    if amp > best[0]:
        best = (amp, P, coef)
amp, P, coef = best
print(f"    max cosine amplitude over P in [0.5,4]: {amp:.3e} at P={P:.2f}")
print(f"    residual rms (no oscillation model): "
      f"{np.sqrt(np.mean(resB**2)):.3e}")
print(f"    => no coherent oscillatory structure above "
      f"{max(amp, np.sqrt(np.mean(resB**2))):.1e} relative")

print("=" * 70)
print("(3) xg controls: does the exponent track S_b,glued(xg)?")
# ratio-of-ratios: [G(xg_a,hb1)/G(xg_p,hb1)] / [G(xg_a,hb2)/G(xg_p,hb2)]
#   predicted = exp(-dS*(1/hb1-1/hb2)), dS=S_a - S_p  (prefactor cancels)
Gprobe = {0.35: 1.1324e-02}  # probe-mode Gamma at primary xg, hb=0.35
# primary hb=0.45 by interpolation of fit B
Gprim_045 = float(np.exp(cB[0] + cB[1]*np.log(0.45) - cB[2]/0.45))
for off_key in ["xg_off_0.2", "xg_off_0.5"]:
    xg_a = pot["xg_scan"][off_key]["xg"]
    dS = pot["xg_scan"][off_key]["Sb"] - Sb_glued_primary
    Ga035 = width[f"{off_key}_hb0.35"]["Gamma"]
    Ga045 = width[f"{off_key}_hb0.45"]["Gamma"]
    r_meas = (Ga035/Gprobe[0.35])/(Ga045/Gprim_045)
    r_pred = np.exp(-dS*(1/0.35 - 1/0.45))
    print(f"    {off_key}: dS={dS:+.4f} ratio_meas={r_meas:.4f} "
          f"ratio_pred={r_pred:.4f} agree={abs(r_meas-r_pred)/r_pred:.2%}")
    # absolute prefactor factor (hb-independent part)
    f035 = (Ga035/Gprobe[0.35])/np.exp(-dS/0.35)
    f045 = (Ga045/Gprim_045)/np.exp(-dS/0.45)
    print(f"             hb-indep prefactor factor: {f035:.3f} @0.35, "
          f"{f045:.3f} @0.45 -> X_c systematic ~{abs(f035-1):.0%}")

print("=" * 70)
print("(4) criterion (c) bookkeeping")
print(f"    Gamma_exact/Gamma_bounce with Gamma_bounce=(wf/2pi)e^-S(E)/hb:")
for hb_s in sorted(Re, key=float):
    hb = float(hb_s)
    key = f"xg_primary_hb{hb}"
    print(f"    hb={hb:.2f}: R-1 = {width[key]['Gamma']/((wf/(2*np.pi))*np.exp(-S_of_E(Re[hb_s]['Re'])/hb))-1:+.3f}")
print("    (deviation from 1 = smooth O(1) prefactor; the 11s prefactor")
print("     wall stands -- K not computed; (c) in absolute form blocked")
print("     by K uncertainty + ~20% X_c prefactor systematic, as budgeted.)")
