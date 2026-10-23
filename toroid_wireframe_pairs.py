"""3D wireframe torus: pairs glow as they line up across the hole,
and each pair is logged to a growing list -- predictions happening live.

Layout: 9 blocks x 9 residues, value(i,j) = 9*i + j + 1  (1..81).
Scene per block b=1..8: pairs (r, 9b+r) for r=1..9 glow red;
a sightline is drawn through the hole between the two blocks;
the pair list grows: "r -> 9b+r".
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

R, r = 3.0, 1.15
NB, NR = 9, 9

def tpos(u, v):
    return np.array([(R + r * np.cos(v)) * np.cos(u),
                     (R + r * np.cos(v)) * np.sin(u),
                     r * np.sin(v)])

P = {}
for i in range(NB):
    for j in range(NR):
        P[(i, j)] = (tpos(2 * np.pi * i / NB, 2 * np.pi * j / NR), 9 * i + j + 1)

cent = {i: np.mean([P[(i, j)][0] for j in range(NR)], axis=0) for i in range(NB)}

fig = plt.figure(figsize=(13, 7))
ax3d = fig.add_subplot(121, projection='3d')
axl = fig.add_subplot(122)
axl.axis('off')

uu = np.linspace(0, 2 * np.pi, 40)
vv = np.linspace(0, 2 * np.pi, 20)
UU, VV = np.meshgrid(uu, vv)
ax3d.plot_wireframe((R + r * np.cos(VV)) * np.cos(UU),
                    (R + r * np.cos(VV)) * np.sin(UU),
                    r * np.sin(VV), color='gray', alpha=0.10, linewidth=0.4)
ax3d.set_axis_off()

texts = {}
for k, (xyz, val) in P.items():
    texts[k] = ax3d.text(*xyz, str(val), fontsize=6, color='#888888',
                         ha='center', va='center', zorder=10)

sight, = ax3d.plot([], [], [], color='#d40000', alpha=0.55, lw=1.2,
                   ls='--', zorder=5)

list_text = axl.text(0.02, 0.98, '', transform=axl.transAxes, va='top',
                     ha='left', family='monospace', fontsize=8.5)
cap_text = axl.text(0.02, 0.02, '', transform=axl.transAxes, va='bottom',
                    ha='left', fontsize=10, color='#aa0000')

log = []
outdir = '/tmp/wireframes'
os.makedirs(outdir, exist_ok=True)
paths = []
FR = 0
for b in range(1, 9):
    for rr in range(1, 10):
        log.append(f"{rr} -> {9 * b + rr}")
    glow_vals = set(range(1, 10)) | set(range(9 * b + 1, 9 * b + 10))
    for sub in range(3):
        for k, (xyz, val) in P.items():
            t = texts[k]
            if val in glow_vals:
                t.set_color('#d40000')
                t.set_fontsize(9)
                t.set_weight('bold')
                t.set_alpha(1.0)
            else:
                t.set_color('#888888')
                t.set_fontsize(6)
                t.set_weight('normal')
                t.set_alpha(0.75)
        c0, cb = cent[0], cent[b]
        sight.set_data([c0[0], cb[0]], [c0[1], cb[1]])
        sight.set_3d_properties([c0[2], cb[2]])
        ax3d.view_init(elev=18, azim=FR * 15)
        shown = log[-14:]
        head = f"PAIRS LOGGED  ({len(log)} predictions)"
        body = "\n".join(shown)
        tail = f"\n... +{len(log) - len(shown)} earlier" if len(log) > len(shown) else ""
        list_text.set_text(head + "\n" + body + tail)
        cap_text.set_text(f"block {b}/8 across the hole:\n1-9  <->  {9 * b + 1}-{9 * b + 9}")
        p = f"{outdir}/f{FR:02d}.png"
        fig.savefig(p, dpi=90, bbox_inches='tight')
        paths.append(p)
        FR += 1

from PIL import Image
imgs = [Image.open(p) for p in paths]
out = '/home/hatch/workspace/prime-sieve-geometry/toroid_wireframe_pairs.gif'
imgs[0].save(out, save_all=True, append_images=imgs[1:], duration=550, loop=0)
print("saved", out, "frames:", len(paths), "pairs logged:", len(log))
