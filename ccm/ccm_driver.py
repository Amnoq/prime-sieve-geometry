"""Driver: build M, smallest eigenpair, zeros of xihat, compare with zeta zeros."""
import mpmath as mp
import numpy as np
import sys
sys.path.insert(0, '/home/hatch/workspace/prime-sieve-geometry/ccm')
from ccm_reimpl import build_M

def run_case(lam, N, dps=40, zmax=60.0, nzeros=10, pw_override=None, label=""):
    mp.dps = dps
    M, L, idx = build_M(lam, N, pw_override=pw_override, verbose=True)
    Md = np.array(M.tolist(), dtype=float)
    # symmetrize against rounding
    Md = 0.5*(Md + Md.T)
    w, V = np.linalg.eigh(Md)
    eps = w[0]; gap = w[1]-w[0]
    xi = V[:, 0]
    # evenness check: xi_{-j} vs xi_{+j}; idx[k] = -N+k
    nn = len(idx)
    even_err = max(abs(xi[k]-xi[nn-1-k]) for k in range(nn))/max(abs(xi))
    print(f"[{label}] eps_N={eps:.6e} gap={gap:.3e} even_err={even_err:.2e}", flush=True)

    # xihat(z) = 2 L^-1/2 sin(zL/2) sum_j xi_j/(z - 2 pi j/L)
    a = np.array([2*np.pi*j/float(L) for j in idx])
    pre = 2/np.sqrt(float(L))
    def xihat(z):
        return pre*np.sin(z*float(L)/2)*np.sum(xi/(z-a))
    # scan for sign changes
    zs = np.linspace(0.01, zmax, 20001)
    vals = np.array([xihat(z) for z in zs])
    roots = []
    for k in range(len(zs)-1):
        if vals[k] == 0:
            roots.append(zs[k])
        elif vals[k]*vals[k+1] < 0:
            lo, hi = zs[k], zs[k+1]
            for _ in range(80):
                mid = 0.5*(lo+hi)
                if xihat(lo)*xihat(mid) <= 0: hi = mid
                else: lo = mid
            r = 0.5*(lo+hi)
            # Newton polish
            for _ in range(20):
                h = 1e-7
                d = (xihat(r+h)-xihat(r-h))/(2*h)
                if d == 0: break
                r -= xihat(r)/d
            roots.append(r)
    roots = sorted(set(round(r, 9) for r in roots))
    # zeta zeros via mpmath
    mp.dps = 30
    zetas = [float(mp.zetazero(k).imag) for k in range(1, nzeros+1)]
    print(f"[{label}] root -- zeta -- abs err", flush=True)
    errs = []
    for r, zt in zip(roots[:nzeros], zetas):
        e = abs(r-zt); errs.append(e)
        print(f"  {r:.8f}  {zt:.8f}  {e:.3e}", flush=True)
    return {"eps": eps, "gap": gap, "even_err": even_err,
            "roots": roots, "errs": errs, "L": float(L)}

if __name__ == "__main__":
    import math
    lam = math.sqrt(13); N = int(sys.argv[1]) if len(sys.argv) > 1 else 25
    run_case(lam, N, label=f"pilot lam=sqrt(13) N={N}")
