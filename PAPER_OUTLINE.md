# Paper Outline — for user approval (updated 2026-09-30)

## Working title
**The Circle Sieve and Its Deformations: A Geometric Language for Sieve Theory**

## Abstract (sketch)
We present the *linear circle sieve*, a deterministic geometric sieve in
which primality emerges from a single relational rule — an integer is
prime iff no earlier prime's marked boundary lands on it — without any
primality predicate. From this generation rule we build the sieve's
*incidence complex* and show that classical sieve theory reads off it as
geometry: Möbius inversion becomes a signed face-sum for the Chebyshev
function (D1); Lehmer's prime-counting recursion becomes the complex's
link recursion (D2); the Prime Number Theorem becomes the statement that
the weighted infinite complex has total weight 1, with the zeta zeros as
regulators of the face-sum (D4). Deforming the marking rule separates
markers from survivors and *derives* the Hardy–Littlewood singular series
as a renormalized total weight (D6). We locate three kinds of positivity
in the framework (primitive counting, Weil-type windowed, Selberg-type
optimized), prove an obstruction to ordinary positive geometry, and
report a systematic hunt for an arithmetic operator: most candidates die
by theorem or computation; the Connes–Consani–Moscovici zeta spectral
triple survives as a live bridge plank — independently reimplemented here
from prime Euler products alone, recovering zeta zeros to machine
precision with no zero input and clean controls. The method is influenced
by the positive-geometry program: derive everything downstream of the
generation rule; never put the answer in by hand. Every claim carries its
epistemic label; every failure is documented with full rigor.

## Section map

1. **Introduction.** The sieve, built from first principles without the
   literature; what the paper does (unified language) and does not do
   (no new prime theorems). The Figueiredo influence: generative method,
   not implementation. *Status: framing.*
2. **The linear circle sieve.** Exact specification (unit-circle substrate;
   new diameter at each unshared n; spam forward). Proof sketch of
   equivalence with Eratosthenes. Figure: full-circle rendering.
   *Status: exact; verified computationally at every tested cutoff.*
3. **The incidence complex.** Vertices, faces, the link recursion
   link(p) = Δ_{⌊N/p⌋} ∖ {p} (exact). Computed homology table
   (N = 100/500/1000); cutoff dependence stated plainly. *Status: exact
   definitions; computed numbers.*
4. **The observable as a face-sum (D1).** ψ(x) = Σ_{∅≠S}(−1)^{|S|+1}
   log(∏S)⌊x/∏S⌋. *Status: classical (Möbius), reframed; verified
   numerically.*
5. **Recursion as link deletion (D2).** Lehmer's φ(x,a) recursion IS the
   facet recursion; the newly-shared integers as a cone over the link.
   *Status: classical, reframed; bijection verified.*
6. **Binary form and the zero locus (D3).** 1_prime + 1_shared = 1;
   composites as the zero locus of F(n) = ∏_p dist(n, pℤ). *Status:
   reframing; verified through 60.*
7. **The weighted infinite complex (D4).** Bare limit trivializes
   (contractible simplex) — the geometry must live in the weights.
   w(S) = (−1)^{|S|+1}log(∏S)/∏S; Σw(S) → 1 IS PNT (verified to 2·10⁶);
   generating function −ζ′/ζ² (verified ~4 digits) — the zeros regulate
   the sum. *Status: classical identities, new framing; the framing of
   PNT as "total weight 1" appears new.*
8. **Splits and soft limits (D5).** Territory removal as an exact two-term
   split, iterated to all orders = the D1 face-sum. *Status: conceptual
   identification with arXiv:2405.09608's move; not a new theorem.*
9. **Deformation and the singular series (D6).** R_p = {0,−2} deformation;
   markers vs survivors separate (survivors = twin lowers, verified to
   2·10⁵); exact deformed μ-identity; face multiplicities; the twin
   constant 2C₂ derived as renormalized total weight (1.3228 at z=100).
   Honest boundary: π₂(x) ~ 𝔖x/(log x)² remains conjectural (ratio 1.6091
   at 2·10⁵). Figure: deformed twin sieve. *Status: algebra verified;
   the framing appears new; the conjecture is NOT claimed.*
10. **Positivity, three kinds (D7–D9, D10).** Primitive (Λ ≥ 0, 3-4-1);
    Weil-type windowed (W(h) ≥ 0 from primes alone, the detector h_{T0,w});
    Selberg-type optimized (exact theorem: min = δ(z) at λ* = μ). The
    negative results: 9c (blind left of Re(s)=1, by theorem), 9c′
    (saturated optimizers lack small-support structure). *Status: exact /
    verified / closed-negative as labeled.*
11. **Obstructions (D4, 14a, 12b).** No ordinary positive geometry
    carries w(S) (exact: magnitudes); bare Δ_∞ contractible; Weyl kills
    fixed-manifold Laplacians. Refined home: differentiated residues on
    a deformed simplex (14c). *Status: exact theorems.*
12. **The operator hunt (Nodes 11–13).** Checklist R1–R6; what died
    (Berry–Keating, bare Möbius Laplacian, multi-torus, Heisenberg,
    H_2, H_int — by theorem or computation); what survived (13d
    pair-hopping is GUE-chaotic, with caveats; 13e negative). The CCM
    bridge plank (11f): independent reimplementation, D2 verification,
    D12 audit, controls, N=40 convergence. What it is and isn't.
    *Status: verified as labeled.*
13. **Discussion.** Dictionary vs bridge; the Frobenius-like operator as
    the sharpest open question (Node 11 still open); failure-mode mapping
    as the next probe.
14. **Appendix A: documented failures (D1–D13).** Every dead end with
    full rigor — the map's most valuable feature.
15. **Appendix B: reproducibility.** All scripts, versions, seeds.

## Figures
- `sieve_circles_full.svg` — the linear circle sieve (full circles)
- homology table (computed)
- `deformed_sieve_twins.svg` — deformed sieve, both marking families
- `mobius_band.png`, `mobius_cut.png`, `mobius_spectrum.png`
- `multi_torus_weyl.png`, `heisenberg_probe.png`
- `fock_probe.png` — Poisson vs GUE histograms

## What it claims / doesn't claim
- Claims: a new geometric *language*; the circle sieve as an exact,
  independently-derived object; D6's framing of the singular series;
  three verified positivity kinds; the CCM independent reimplementation
  with controls; exactly-labeled negative results.
- Doesn't claim: any new theorem about primes; a proof of RH; a
  positive geometry (obstruction proved); that 13d hears the primes
  (13e negative).

## Next step on approval
Full LaTeX draft in the style of the primorial-wheel paper, with the
verification scripts packaged alongside.
