"""
Node 11s — Gamma(ℏ) scaling test for the open-channel resonance.
If log Gamma = -S_b/ℏ + log K with S_b matching the bounce action,
it's the bounce-mediated decay. Xc=1.0, alpha=30.
"""
import numpy as np, json
from node11s_open import scan_open, richardson

if __name__ == "__main__":
    eps = 0.2
    Sb = json.load(open("/tmp/node11s_Sb.json"))[str(eps)]["Sb"]
    print(f"S_b = {Sb:.6f}")
    results = {}
    for hb in [0.25, 0.30, 0.35, 0.40]:
        ims, dxs = [], []
        for N in [801, 1201]:
            s = scan_open(hb, eps, N=N, thetas=(0.20,), L=12.0)
            if not s["scan"]:
                print(f"hb={hb} N={N}: NO RESONANCE")
                ims.append(np.nan); dxs.append(s["dx"])
            else:
                e = s["scan"][0]["E"]
                ims.append(e[1]); dxs.append(s["dx"])
        # 2-point Richardson
        if not np.isnan(ims).any():
            # Im = a + b*dx^2
            x1, x2 = dxs[0]**2, dxs[1]**2
            a = (ims[0]*x2 - ims[1]*x1)/(x2 - x1)
            Gamma = -2*a/hb
            results[str(hb)] = dict(Im=a, Gamma=Gamma)
            print(f"hb={hb}: Im(inf)={a:.4e} Gamma={Gamma:.4e} "
                  f"1/hb={1/hb:.3f} logGamma={np.log(Gamma):.4f}")
    # fit log Gamma = -Sb_fit/hb + logK
    hbs = np.array([float(k) for k in results])
    lGs = np.array([np.log(results[k]["Gamma"]) for k in results])
    A = np.column_stack([-1/hbs, np.ones_like(hbs)])
    coef, *_ = np.linalg.lstsq(A, lGs, rcond=None)
    print(f"fit: S_b,fit={coef[0]:.4f} (bounce {Sb:.4f}), logK={coef[1]:.4f}")
    json.dump(results, open("/tmp/node11s_Gh.json","w"), indent=1)
