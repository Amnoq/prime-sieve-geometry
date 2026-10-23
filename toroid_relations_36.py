"""The sum of its relations: no torus object, only the pairing graph.

18 nodes (outer-ring values 1..18), edges = across-hole pairing n <-> n+9.
Node color = parity (content, not decoration). Labels carry number +
factorization (the composite's history). Animation steps through the 9 pairs
slowly enough to read every number.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


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


def pw(v):
    return 'even' if v % 2 == 0 else 'odd'


pairs = [(a, a + 18) for a in range(1, 10)]

fig, ax = plt.subplots(figsize=(11, 13))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.set_xlim(-1.6, 1.6)
ax.set_ylim(-0.7, 10.4)
ax.axis('off')

pos = {}
for v in range(1, 10):
    pos[v] = (-0.8, 9.2 - (v - 1) * 0.95)
for v in range(19, 28):
    pos[v] = (0.8, 9.2 - (v - 19) * 0.95)

EVEN_C, ODD_C = '#2e5f8a', '#b08d2f'
nodes, texts, edges = {}, {}, {}
for v in list(range(1, 10)) + list(range(19, 28)):
    x, y = pos[v]
    c = EVEN_C if v % 2 == 0 else ODD_C
    nodes[v] = plt.Circle((x, y), 0.30, color=c, alpha=0.85, zorder=3)
    ax.add_patch(nodes[v])
    texts[v] = ax.text(x, y, f'{v}\n{factorize(v)}', color='white', fontsize=8,
                       ha='center', va='center', weight='bold', zorder=4)
for a, b in pairs:
    x1, y1 = pos[a]
    x2, y2 = pos[b]
    (ln,) = ax.plot([x1, x2], [y1, y2], color='#555a66', lw=1.2, alpha=0.7, zorder=2)
    edges[(a, b)] = ln

ax.text(-0.8, 10.0, 'near side', color='#9aa4b5', ha='center', fontsize=11)
ax.text(0.8, 10.0, 'across the hole', color='#9aa4b5', ha='center', fontsize=11)
ax.set_title('36-ring: across the hole is +18 -- 1..9 adjacent with 19..27',
             color='white', fontsize=14, pad=18)

dyn = []


def clear_dyn():
    while dyn:
        dyn.pop().remove()


def update(f):
    clear_dyn()
    a, b = pairs[f % len(pairs)]
    for v in list(range(1, 10)) + list(range(19, 28)):
        nodes[v].set_alpha(0.28)
        texts[v].set_alpha(0.35)
    for ln in edges.values():
        ln.set_alpha(0.15)
        ln.set_color('#555a66')
        ln.set_linewidth(1.2)
    for v in (a, b):
        nodes[v].set_alpha(1.0)
        texts[v].set_alpha(1.0)
    edges[(a, b)].set_alpha(1.0)
    edges[(a, b)].set_color('#ffcf3f')
    edges[(a, b)].set_linewidth(3.5)
    x1, y1 = pos[a]
    x2, y2 = pos[b]
    for x, y in ((x1, y1), (x2, y2)):
        hl = plt.Circle((x, y), 0.37, color='none', ec='#ffcf3f', lw=2.5, zorder=5)
        ax.add_patch(hl)
        dyn.append(hl)
    t = ax.text(0, 0.0,
                f'{a} = {factorize(a)} ({pw(a)})   <-->   {b} = {factorize(b)} ({pw(b)})',
                color='#ffcf3f', fontsize=13, ha='center', weight='bold', zorder=6)
    dyn.append(t)
    return dyn


anim = FuncAnimation(fig, update, frames=len(pairs), interval=1400)
anim.save('toroid_relations_36.gif', writer='pillow', dpi=100)
print('saved toroid_relations_36.gif')
