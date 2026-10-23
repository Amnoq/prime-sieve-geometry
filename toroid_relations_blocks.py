"""Keep expanding: 1..9 against every block of nine, up to 81.

Eight blocks: 10-18, 19-27, ..., 73-81. Within each block the 9 across-hole
pairs are stepped through slowly. Every node: number + factorization (the
composite's history) + parity color. No torus object -- only the relations.
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


EVEN_C, ODD_C = '#2e5f8a', '#b08d2f'
LEFT = list(range(1, 10))
BLOCKS = [list(range(9 * b + 1, 9 * b + 10)) for b in range(1, 9)]  # 10-18 .. 73-81

# frames: (block_index, n) for each block and each n in 1..9
FRAMES = [(bi, n) for bi in range(len(BLOCKS)) for n in LEFT]

fig, ax = plt.subplots(figsize=(11, 13))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.set_xlim(-1.6, 1.6)
ax.set_ylim(-0.7, 10.6)
ax.axis('off')
ax.text(-0.8, 10.0, 'one through nine', color='#9aa4b5', ha='center', fontsize=11)
ax.text(0.8, 10.0, 'the block', color='#9aa4b5', ha='center', fontsize=11)
title = ax.set_title('', color='white', fontsize=14, pad=18)

yl = {v: 9.2 - (v - 1) * 0.95 for v in LEFT}


def draw_block(bi, hi_n=None):
    """Draw left 1..9 and the block's nine numbers; highlight pair (hi_n, block_n)."""
    artists = []
    yr = {v: 9.2 - (v - BLOCKS[bi][0]) * 0.95 for v in BLOCKS[bi]}
    # left nodes
    for v in LEFT:
        x, y = -0.8, yl[v]
        c = EVEN_C if v % 2 == 0 else ODD_C
        dim = hi_n is not None and v != hi_n
        artists.append(ax.add_patch(plt.Circle((x, y), 0.30, color=c,
                                               alpha=0.28 if dim else 0.9, zorder=3)))
        artists.append(ax.text(x, y, f'{v}\n{factorize(v)}', color='white', fontsize=8,
                               ha='center', va='center', weight='bold', zorder=4,
                               alpha=0.35 if dim else 1.0))
    # right nodes
    for v in BLOCKS[bi]:
        x, y = 0.8, yr[v]
        c = EVEN_C if v % 2 == 0 else ODD_C
        dim = hi_n is not None and v != BLOCKS[bi][hi_n - 1]
        artists.append(ax.add_patch(plt.Circle((x, y), 0.30, color=c,
                                               alpha=0.28 if dim else 0.9, zorder=3)))
        artists.append(ax.text(x, y, f'{v}\n{factorize(v)}', color='white', fontsize=8,
                               ha='center', va='center', weight='bold', zorder=4,
                               alpha=0.35 if dim else 1.0))
    # edges
    for v in LEFT:
        w = BLOCKS[bi][v - 1]
        hot = hi_n == v
        (ln,) = ax.plot([-0.8, 0.8], [yl[v], yr[w]],
                        color='#ffcf3f' if hot else '#555a66',
                        lw=3.5 if hot else 1.2,
                        alpha=1.0 if hot else 0.5, zorder=2)
        artists.append(ln)
    if hi_n is not None:
        w = BLOCKS[bi][hi_n - 1]
        for x, y in ((-0.8, yl[hi_n]), (0.8, yr[w])):
            artists.append(ax.add_patch(plt.Circle((x, y), 0.37, color='none',
                                                   ec='#ffcf3f', lw=2.5, zorder=5)))
        artists.append(ax.text(0, 0.0,
                               f'{hi_n} = {factorize(hi_n)} ({pw(hi_n)})   <-->   '
                               f'{w} = {factorize(w)} ({pw(w)})',
                               color='#ffcf3f', fontsize=13, ha='center',
                               weight='bold', zorder=6))
    b0, b1 = BLOCKS[bi][0], BLOCKS[bi][-1]
    b = bi + 1
    par = 'parity FLIPS across the hole' if b % 2 == 1 else 'parity preserved across the hole'
    title.set_text(f'block {b} of 8: 1..9 adjacent with {b0}..{b1} -- {par}')
    return artists


dyn = []


def clear_dyn():
    while dyn:
        dyn.pop().remove()


def update(f):
    clear_dyn()
    bi, n = FRAMES[f % len(FRAMES)]
    dyn.extend(draw_block(bi, hi_n=n))
    return dyn


anim = FuncAnimation(fig, update, frames=len(FRAMES), interval=900)
anim.save('toroid_relations_blocks.gif', writer='pillow', dpi=100)
print('saved toroid_relations_blocks.gif', len(FRAMES), 'frames')
