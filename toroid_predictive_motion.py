"""The predictive perspective in motion.

A marker bead travels the outer equator of an 18x18 beaded torus. At every
frame, its across-the-hole partner is COMPUTED live from the involution
(u,v) -> (u+pi,v) -- never stored, never looked up. The pairing line and the
caption show the prediction happening: number, factorization (the composite's
history), and parity, for both ends.

Even ring count (18) is load-bearing: on an odd grid the partner lands
half a cell off; on 18 it lands exactly on a bead. [exact]
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

R, r, n = 3.0, 1.3, 18
BEAD_R = 0.16


def factorize(k):
    if k < 2:
        return '1'
    tmp, parts = k, []
    d = 2
    while d * d <= tmp:
        e = 0
        while tmp % d == 0:
            tmp //= d
            e += 1
        if e:
            parts.append(f'{d}^{e}' if e > 1 else str(d))
        d += 1 if d == 2 else 2
    if tmp > 1:
        parts.append(str(tmp))
    if len(parts) == 1 and '^' not in parts[0] and parts[0] == str(k):
        return f'{k} (prime)'
    return ' x '.join(parts)


def bead_pos(i, j):
    u0 = (i + 0.5) * 2 * np.pi / n
    v0 = (j + 0.5) * 2 * np.pi / n
    return np.array([(R + r * np.cos(v0)) * np.cos(u0),
                     (R + r * np.cos(v0)) * np.sin(u0),
                     r * np.sin(v0)])


def parity_word(k):
    return 'even' if k % 2 == 0 else 'odd'


# values: 18x18 multiplication table; outer ring j=0 carries 1..18
values = np.fromfunction(lambda i, j: (i + 1) * (j + 1), (n, n), dtype=int)

fig = plt.figure(figsize=(10, 10))
fig.patch.set_facecolor('black')
ax = fig.add_subplot(111, projection='3d')
ax.set_facecolor('black')
for axis in (ax.xaxis, ax.yaxis, ax.zaxis):
    axis.pane.fill = False
    axis.pane.set_edgecolor('black')
ax.set_box_aspect((2 * (R + r), 2 * (R + r), 2 * r))

# wireframe torus (static)
uu = np.linspace(0, 2 * np.pi, 72)
vv = np.linspace(0, 2 * np.pi, 36)
U, V = np.meshgrid(uu, vv)
X = (R + r * np.cos(V)) * np.cos(U)
Y = (R + r * np.cos(V)) * np.sin(U)
Z = r * np.sin(V)
ax.plot_wireframe(X, Y, Z, color='#9aa4b5', alpha=0.18, linewidth=0.4)

# beads (static): color encodes parity ONLY -- no decorative gradient
su = np.linspace(0, 2 * np.pi, 8)
sv = np.linspace(0, np.pi, 6)
SU, SV = np.meshgrid(su, sv)
EVEN_C, ODD_C = '#2e5f8a', '#b08d2f'
for i in range(n):
    for j in range(n):
        p = bead_pos(i, j)
        c = EVEN_C if values[i, j] % 2 == 0 else ODD_C
        SX = p[0] + BEAD_R * np.cos(SU) * np.sin(SV)
        SY = p[1] + BEAD_R * np.sin(SU) * np.sin(SV)
        SZ = p[2] + BEAD_R * np.cos(SV)
        ax.plot_surface(SX, SY, SZ, color=c, shade=True, edgecolor='none', alpha=0.9)

ax.set_axis_off()

dyn_artists = []


def clear_dyn():
    for a in dyn_artists:
        a.remove()
    dyn_artists.clear()


def highlight(p, color, scale=1.6):
    SX = p[0] + BEAD_R * scale * np.cos(SU) * np.sin(SV)
    SY = p[1] + BEAD_R * scale * np.sin(SU) * np.sin(SV)
    SZ = p[2] + BEAD_R * scale * np.cos(SV)
    dyn_artists.append(ax.plot_surface(SX, SY, SZ, color=color, shade=True,
                                        edgecolor='white', linewidth=0.6, alpha=0.98))


NFRAMES = 36

def update(f):
    clear_dyn()
    ax.view_init(elev=20, azim=-58 + f * 5)          # the torus is not static
    m = (f // 2) % n                                 # marker travels the outer ring
    pm = bead_pos(m, 0)
    # THE PREDICTION: partner derived live from the involution, nothing stored
    p_idx = (m + n // 2) % n
    pp = bead_pos(p_idx, 0)
    highlight(pm, '#ffcf3f')
    highlight(pp, '#37e0ff')
    line, = ax.plot([pm[0], pp[0]], [pm[1], pp[1]], [pm[2], pp[2]],
                    color='#ffcf3f', lw=2.0, alpha=0.9)
    dyn_artists.append(line)
    mv, pv = int(values[m, 0]), int(values[p_idx, 0])
    ax.set_title(f'{mv} = {factorize(mv)} ({parity_word(mv)})'
                 f'   <--->   {pv} = {factorize(pv)} ({parity_word(pv)})',
                 fontsize=12, color='white')
    return dyn_artists


anim = FuncAnimation(fig, update, frames=NFRAMES, interval=220)
anim.save('toroid_predictive_motion.gif', writer='pillow', dpi=100)
print('saved toroid_predictive_motion.gif')
