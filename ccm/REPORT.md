# CCM Independent Reimplementation — Final Report (2026-09-30)

## Objective
Independently reimplement the Connes–Consani–Moscovici operator
D_log^{(λ,N)} from arXiv:2511.22755 using ONLY prime Euler products,
verify spectral coincidence with zeta zeros, and audit for zero-fitting.

## Implementation
- Location: `~/workspace/prime-sieve-geometry/ccm/`
- `ccm_reimpl.py`: matrix construction from primary source Sec.4
- `ccm_driver2.py`: high-precision driver (even subspace + inverse iteration)
- `D12_AUDIT.md`: provenance audit

### Matrix construction (all from paper, no zero input)
M = W_{0,2} − W_R − W_p, where:
- **W_{0,2}**: verbatim eq.(4.2). Rank 2 (verified). Point-mass term.
- **W_R**: diagonal via master formula (weinfty), validated vs direct
  quadrature to 2e-16; off-diagonal (J(m)−J(n))/(π(n−m)). Archimedean term.
- **W_p**: verbatim eq.(bomp): Σ_{k=p^r≤λ²} Λ(k)k^{−1/2}q(log k).
  THE ONLY ARITHMETIC INPUT. Fixed endpoint bug (k=λ² excluded by
  float rounding; now exact integer cutoff).

### Key methodological findings
1. **Full matrix has multiple tiny eigenvalues at small N** — NOT a bug.
   Known-good connes-cvs implementation shows identical structure.
2. **Even subspace has SINGLE tiny eigenvalue.** Restrict to even
   (ξ_{−j}=ξ_j), dim N+1. Inverse iteration finds it.
3. **Ground state naturally even.** Odd-block smallest eigenvalue 581×
   larger than even-block at N=10 (1.64e-23 vs 2.83e-26).
4. **High precision load-bearing.** Float64 eigh cannot resolve ε_N;
   need mpmath inverse iteration at dps≥60.

## Results (D2 verification)

| Config | ε_N | Zeros recovered | Best error |
|--------|-----|-----------------|------------|
| c=13, N=10, dps=60 | 2.83e-26 | 3 (err <5e-10) | 7.1e-15 (zero 1) |
| c=13, N=20, dps=100 | 1.57e-39 | 8 (first 5 <4e-11) | exact (zero 1) |
| c=9, N=20, dps=100 | 1.27e-32 | 10 (first 8 <3e-09) | 3.6e-15 (zero 1) |

The first zeta zero (14.13472514173469379...) is recovered from prime
Euler products alone to machine precision. No zeta-zero information
enters the pipeline at any stage.

## D12 audit: CLEAN
- W_{0,2}: analytic point-mass, no zeros.
- W_R: archimedean (gamma factor), no zeros.
- W_p: prime powers + von Mangoldt ONLY. No zeros.
- Eigensolve, ξ̂, root-finding: no zeros.
- True zeros used ONLY for post-hoc error computation.
- Contrast D12 dead end: here the weight is the NATURAL von Mangoldt
  from the explicit formula, not engineered to produce zeros.

## Controls (2026-09-30)
All at c=13, N=20, dps=100. The zeros AND the positivity both vanish
unless the precise prime arithmetic input is present:
- **A (Wp=0)**: eps_N = −0.17 (matrix not positive); first root 2.79, err 11.3.
- **B (shuffled Λ weights)**: eps_N = −0.087; root 5.78, err 8.4.
- **C (shuffled log p positions)**: eps_N = 0.0175 (O(1), not tiny); root 1.16, err 13.0.
The machinery does not generate zeros on its own; the specific prime
structure (values AND positions) is load-bearing.

## Large-N (2026-09-30)
c=13, N=40, dps=120 (201s): eps_even=9.46e-54, eps_odd=3.54e-50,
separation 3744x (vs 581x at N=10 — growing with N as theory predicts).
Zeros 1-5 err <1e-10; zeros 6-10 err <2e-6. Convergence law holding.

## Epistemic status
- Matrix formulas: **exact theorem** (from primary source).
- Closed-form validations: **computationally verified** (2e-16, 2.7e-51).
- Spectral coincidence: **computationally verified** (multiple configs).
- Even-simplicity: **computationally verified** at tested (λ,N).
- General convergence to all zeros: **conjectural** (paper states proof = proof of RH).

## Open
- Larger N (paper: N=120) for more zeros / more digits.
- Full (λ,N) convergence law.
- Failure-mode mapping (what spectra if RH false).
- The 581× even/odd separation at N=10 is modest; check growth with N.
