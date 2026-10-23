#!/usr/bin/env python3
"""13d robustness: pair-hop GUE at z=31 (dim 2048) and z=37 (dim 4096),
dense diagonalization, lam = lam0 (Frobenius-matched), plus lam=0.5x."""
import numpy as np
from fock_pairhop import build, primes_upto, r_stat, par_below

for z in [31, 37]:
    ps = primes_upto(z); w = np.log(ps)/ps
    print(f"building z={z}, m={len(ps)}, dim={1<<len(ps)}...", flush=True)
    Hb, Hp = build(z, w)
    # symmetry sanity
    assert np.allclose(Hb, Hb.T) and np.allclose(Hp, Hp.T)
    lam0 = float(np.linalg.norm(Hb)/np.linalg.norm(Hp))
    for mult in [0.5, 1.0]:
        E = np.linalg.eigvalsh(Hb + mult*lam0*Hp)
        r, _ = r_stat(E)
        print(f"z={z} mult={mult}: <r>={r:.3f} (Poisson 0.386, GUE 0.536)",
              flush=True)
print("done")
