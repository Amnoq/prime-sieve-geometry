# Multi-torus framework — foundation (from scratch, 2026-09-30)

The user's original idea, rebuilt from a clean foundation (it was never
written down; the April 2026 archive does not contain it): **link a 2-torus
and a 3-torus by a self-adjoint operator**, in service of the Node 11
operator hunt. The dead-end guardrails (archive_dead_ends.md) apply
throughout — especially D8 (do not simulate the non-simulatable).

## 1. Objects

- **T^2**: the flat 2-torus (R/Z)^2. Also the topological type of the
  genus-1 Jacobian — our 10d function-field object. The "leaf."
- **T^3**: the flat 3-torus (R/Z)^3. The "ambient."
- **T** (the operator): self-adjoint, required to satisfy the Node 11
  checklist — (R1) spectrum = zeta zeros, (R2) trace formula = explicit
  formula, (R3) self-adjointness <=> RH, (R4) positivity counting-born,
  (R5) exact formula, (R6) functional-equation symmetry geometric.

## 2. Candidate linkages

- **L1 — product**: T^3 = T^2 x S^1. Operator: Laplacian
  (tensor sum). Status: DEAD as spectral candidate (12b, Weyl's law).
- **L2 — mapping torus**: M_f = T^2 x [0,1] / (x,0)~(f(x),1),
  f in SL(2,Z) (flat / Nil / Sol according as f is elliptic /
  parabolic / hyperbolic, e.g. Arnold's cat map). The flow suspends f;
  f plays Frobenius. Laplacian: fixed dimension -> DEAD by Weyl as a
  zeta-spectral candidate. Dynamical (Ruelle/Artin-Mazur) zeta of the
  cat map is rational (#Fix(f^n) = |det(I - A^n)|), not zeta-like.
  Status: DEAD as spectral candidate; alive only as analogy.
- **L3 — unit tangent bundle**: UT(T^2) = T^3 in the flat case, with
  the geodesic flow. Spectrally L1. Status: DEAD.
- **L4 — Deninger-type dynamical system** (conjectural): a compact
  3-dimensional foliated dynamical system (X, F, phi^t) with 2D leaves,
  flow transverse to the foliation; closed orbits <-> primes with
  length = log p; Ruelle zeta = Riemann zeta; explicit formula =
  Lefschetz trace formula for the flow. The operator (flow generator,
  skew-adjoint; i times it self-adjoint) is exactly the "link" binding
  leaf (T^2-type) to ambient (3-space). Status: CONJECTURAL,
  non-probable per D8 — formulate precisely, do NOT simulate shadows.
- **L5 — twisted torus (Heisenberg nilmanifold)**: non-trivial T^2
  bundle over S^1 (nilmanifold Gamma\H_3). Laplacian spectrum via the
  Weil representation — theta-function content, genuinely arithmetic.
  Status: DONE 2026-09-30 (12d) — NEGATIVE on all three panels:
  exact spectrum (2pih)^2 + 2pi|h|(2k+1) (mult |h|) + torus part;
  65,401 eigenvalues enumerated; counting is Weyl d=3 (slope 3/2)
  vs zeros' T log T; bulk spacings rigid/degenerate (mass at 0, no
  level repulsion) vs zeros' GUE-like repulsion. Moral: arithmetic
  flavor (theta/Weil) in a geometric Laplacian != zero spectrum.
  heisenberg_probe.py / heisenberg_probe.png.

## 3. The Weyl verdict (12b)

For a closed d-dimensional Riemannian manifold, Weyl's law:
N(Lambda) = #{lambda_j <= Lambda} ~ C_d Vol(M) Lambda^{d/2}.
The zeta zeros need N(T) ~ (T/2pi)(log(T/2pi) - 1).
No integer d works: d=2 gives linear (too slow by a log), d>=3 gives
Lambda^{d/2} with d/2 > 1 (too fast). Hence no fixed-dimension
manifold Laplacian has the zeros as its spectrum *in counting*.
[exact theorem]
Honest loophole (not closed): the zeros could be a *subset* of a
higher-dimensional spectrum (subset counting can sit below Weyl).
But then the operator is not "the" spectral realization until the
selection is explained. The flat-T^3 negative is stronger anyway:
its spectrum is explicitly 2pi*sqrt(m^2+n^2+k^2) — visibly not the
zeros, not just in counting.

## 4. Standing

- "Multi-torus via Laplacian" (L1-L3): DEAD, by theorem (Weyl), not by
  difficulty. This is the 9c-shaped kill for this framework.
- "Multi-torus via dynamics" (L4): the SURVIVING form of the user's
  original idea — and it is Deninger's program. Conjectural; D8 applies.
- The link the user sought exists in L4: the operator (flow generator)
  binds the 2D leaf to the 3D ambient. In L1-L3 no operator can do the
  job.
- Next: 12d (Heisenberg probe). After that, the framework's computable
  content is exhausted; what remains is L4 as formulated conjecture.
