"""
Node 11t — supplementary: Re E_res per hb (single N, single theta; the
width scan stored only Im).  Used for the S(E) WKB correction.
"""
import json
from node11t_width import scan_width

pot = json.load(open("/home/hatch/workspace/prime-sieve-geometry/"
                     "node11t_scripts/potential.json"))
xg_primary = pot["xg_scan"]["xg_off_0.35"]["xg"]
out = {}
for hb in [0.28, 0.32, 0.36, 0.40, 0.44]:
    s = scan_width(hb, xg_primary, N=1201, thetas=(0.20,))
    rec = s["scan"][0]
    out[str(hb)] = dict(Re=rec["E"][0], Im=rec["E"][1])
    print(f"hb={hb}: Re E = {rec['E'][0]:.8f}  Im E = {rec['E'][1]:.4e}",
          flush=True)
json.dump(out, open("/home/hatch/workspace/prime-sieve-geometry/"
                    "node11t_scripts/Re.json", "w"), indent=1)
