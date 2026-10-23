#!/usr/bin/env python3
"""13d strengtheners: (1) sparse Lanczos at z=41,43 for bulk r-stat;
(2) Delta_3 rigidity vs GUE/Poisson; (3) density of states.
"""
import numpy as np
from scipy import sparse
from scipy.sparse.linalg import eigsh
from fock_pairhop import primes_upto, par_below, r_stat

def build_sparse(z, w, which='both'):
    ps = primes_upto(z); m = len(ps); N = 1 << m
    w = np.asarray(w, float)
    rows, cols, data = [], [], []
    idx = np.arange(N)
    if which in ('base', 'both'):
        for i in range(m):
            b = idx ^ (1 << i)
            rows.extend(idx.tolist()); cols.extend(b.tolist())
            data.extend([w[i]]*N)
        bits = ((idx[:, None] >> np.arange(m)) & 1).astype(float)
        wb = bits @ w
        diag = (wb*wb - bits @ (w*w))/2
        rows.extend(idx.tolist()); cols.extend(idx.tolist())
        data.extend(diag.tolist())
    if which in ('pair', 'both'):
        for a in range(N):
            occ = [i for i in range(m) if (a >> i) & 1]
            emp = [i for i in range(m) if not (a >> i) & 1]
            for ii in range(len(occ)):
                for jj in range(ii+1, len(occ)):
                    r, s = occ[ii], occ[jj]
                    a1 = a ^ (1 << r); a2 = a1 ^ (1 << s)
                    sgn_rs = par_below(a, r) ^ par_below(a1, s)
                    wrs = w[r]*w[s]
                    for kk in range(len(emp)):
                        for ll in range(kk+1, len(emp)):
                            p, q = emp[kk], emp[ll]
                            a3 = a2 | (1 << q); b = a3 | (1 << p)
                            sgn = sgn_rs ^ par_below(a2, q) ^ par_below(a3, p)
                            rows.append(a); cols.append(b)
                            data.append(wrs*w[p]*w[q]*(-1.0 if sgn else 1.0))
    H = sparse.coo_matrix((np.array(data), (np.array(rows), np.array(cols))),
                          shape=(N, N)).tocsr()
    # symmetrize (pair-hopping as built is not manifestly symmetric; H must be)
    H = (H + H.T) * 0.5
    return H

def delta3(e_unf, L_vals, nwin=40):
    e = np.sort(e_unf); n = len(e); out = []
    for L in L_vals:
        vals = []
        starts = np.linspace(e[5], e[n-5]-L, nwin)
        for x in starts:
            seg = e[(e >= x) & (e <= x+L)] - x
            if len(seg) < 6: continue
            k = np.arange(1, len(seg)+1)
            A = np.vstack([seg, np.ones_like(seg)]).T
            (a, b), *_ = np.linalg.lstsq(A, k, rcond=None)
            grid = np.linspace(0, L, 400)
            Nev = np.searchsorted(seg, grid)
            vals.append(np.mean((Nev - (a*grid + b))**2))
        out.append(float(np.mean(vals)) if vals else np.nan)
    return out

def unfold(e, deg=12):
    e = np.sort(e); n = len(e)
    x = np.linspace(-1, 1, n)
    return np.polyval(np.polyfit(x, np.arange(n), deg), x)

results = {}
for z in [41, 43]:
    ps = primes_upto(z); m = len(ps); N = 1 << m
    w = np.log(ps)/ps
    print(f"z={z}: m={m}, dim={N}", flush=True)
    print("  building Hb...", flush=True)
    Hb = build_sparse(z, w, 'base')
    print("  building Hp...", flush=True)
    Hp = build_sparse(z, w, 'pair')
    lam0 = float(sparse.linalg.norm(Hb)/sparse.linalg.norm(Hp))
    print(f"  lam0={lam0:.4f}", flush=True)
    H = Hb + lam0*Hp
    # bulk interior eigenvalues via shift-invert around median
    # cheaper: 'SA'/'LA' won't give bulk. Use shift-invert at 0 after shifting.
    # Estimate spectral center via a few Lanczos steps: use eigsh 'BE' is slow.
    # Practical: get 1500 eigenvalues near the middle via shift-invert sigma=0
    # on H - mu*I where mu ~ median. First get extremal to bound.
    print("  extremal eigsh...", flush=True)
    emax = eigsh(H, k=2, which='LA', return_eigenvectors=False)
    emin = eigsh(H, k=2, which='SA', return_eigenvectors=False)
    mu = float((emax[0]+emin[0])/2)
    print(f"  spectrum in [{emin[0]:.2f}, {emax[0]:.2f}], mu={mu:.2f}", flush=True)
    print("  shift-invert for 1200 interior...", flush=True)
    E = eigsh(H - mu*sparse.eye(N), k=1200, sigma=0.0,
              return_eigenvectors=False, tol=1e-6, maxiter=20000)
    E = np.sort(E) + mu
    r, _ = r_stat(E)
    print(f"  z={z}: bulk <r>={r:.3f} (Poisson 0.386, GUE 0.536)", flush=True)
    # Delta_3 on unfolded
    eu = unfold(E)
    Ls = [5, 10, 20, 40]
    d3 = delta3(eu, Ls)
    # GUE theory: (1/pi^2)(log(2pi L) + gamma - 5/4 - ...); Poisson: L/15
    import math
    gue = [(1/math.pi**2)*(math.log(2*math.pi*L)+0.5772-1.25) for L in Ls]
    poi = [L/15 for L in Ls]
    print(f"  Delta_3: L={Ls}", flush=True)
    print(f"    observed: {[f'{v:.3f}' for v in d3]}", flush=True)
    print(f"    GUE:      {[f'{v:.3f}' for v in gue]}", flush=True)
    print(f"    Poisson:  {[f'{v:.3f}' for v in poi]}", flush=True)
    # DOS: save full-ish spectrum shape via extremal + interior
    results[z] = dict(r=r, d3=d3, n=N)
    # DOS figure from the 1200 interior + tails
    import matplotlib; matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.hist(E, bins=60, density=True, alpha=0.7)
    ax.set_xlabel('E'); ax.set_ylabel('density'); ax.set_title(f'DOS z={z} (interior 1200)')
    fig.savefig(f'fock_dos_z{z}.png', dpi=80); plt.close(fig)

print("done")
