# Node 11m — Deninger program: primary-source assessment (2026-10-05)

Study node (theory, no computation). Question: Deninger is the tree's
designated survivor (Node 12c, "Deninger-shaped linkage," formulated
conjecture; Node 12 closed with L4 as the live form). 11l just verified
the prime-orbit→tone mechanism in a computable setting. What does
Deninger's program actually contain — theorem vs conjecture — and how
does it relate to 11l?

Sources (read via primary-source browser task, 2026-10-05):
- C. Deninger, "Dynamical systems for arithmetic schemes,"
  arXiv:1807.06400 (2018); published Indag. Math. (N.S.) 37 (2026),
  no. 1, 25–136.
- C. Deninger, "Primes, knots and periodic orbits," arXiv:2301.11643
  (2023), expository.
- Programmatic origins: [Den98] ICM Berlin 1998; [Den00]; [Den01].

## 1. What EXISTS (theorem)

Deninger CONSTRUCTED the dynamical system — it is not a wish.
For 𝔛₀ integral normal (finite type over Spec ℤ), there is a
continuous-time dynamical system (X₀, φ^t), t ∈ ℝ, built by
suspension from rational Witt vectors: X₀ is a quotient involving
W_rat(𝔛₀)(ℂ) with commuting Frobenius endomorphisms F_p, and ℝ^{>0}
acts by scaling the suspension coordinate.

Theorem 6.1 (arXiv:1807.06400): the points with nontrivial isotropy
are exactly ∐_{x₀} Γ^ℰ_{x₀}, x₀ running over closed points of 𝔛₀
with finite residue fields. Each packet Γ_{x₀} is a compact family
of periodic orbits, ALL of length log N(x₀), fibering over
Ẑ_{(p)}^×/p^Ẑ with circle fibers ℝ^{>0}/N(x₀)^ℤ.

For 𝔛₀ = Spec ℤ: periodic orbits γ_p ↔ prime numbers p, with
l(γ_p) = log p. Confirmed verbatim from the paper's introduction.
[exact theorem]

The foliation: X₀ carries a one-codimensional "foliation" F from the
suspension structure (leaves = images of Ẋ₀(ℂ) × {u}); ℚ^{>0} is the
group of Poincaré return maps. The programmatic 3D form — triples
(X, F, φ) with X a closed 3-manifold, F a 1-codimensional foliation
by Riemann surfaces, φ a flow mapping leaves to leaves — is the
target shape. For Spec ℤ (d=1), the desired 3-dimensional
Riemann-surface-lamination subsystem Y₀ ⊂ X₀ is OPEN (v4 §6 asks
for it explicitly). [exact theorem for X₀; conjectural for the 3D
lamination subsystem]

## 2. The trace formula (theorem in the foliation setting)

The transversal index theorem (proved in the foliation setting,
Kop06/11), eq. (9) of arXiv:2301.11643:

  1 − ∑_ρ e^{tρ} + e^{αt} = ∑_γ l(γ) ∑_{k≥1} ±δ_{kl(γ)},

in D'(ℝ^{>0}), where ρ runs over the spectrum of θ (the flow
generator, see §3). Its left side is the transversal index
∑_i (−1)^i Tr(φ^* | ker Δ^i_{F,(2)}). The number-theoretic
counterpart is Weil's explicit formula as a distribution identity:

  1 − ∑_ρ e^{tρ} + e^t = ∑_p log p ∑_{k≥1} δ_{k log p} + (1−e^{−2t})^{−1},

ρ running over zeta zeros in 0 < Re s < 1.
[exact theorem — the foliation-setting Lefschetz formula]

## 3. The operator Θ (conjectural)

Θ (also θ) = the infinitesimal generator of the ℝ-action, acting
on the space of global leafwise harmonic L²-forms ker Δ^i_{F,(2)}
(the maximal Hausdorff quotient of leafwise L²-cohomology).
Conjectured: "the zeroes and poles of ζ_{𝔛₀}(s) should be the
eigenvalues of the infinitesimal generator of the induced ℝ-action
on foliation cohomology groups of (X₀, F) with compact supports."
If φ^{t*} acts on a leafwise metric with conformal factor e^{αt},
eigenvalues ρ of θ satisfy Re ρ = α/2; the RH analogue wants
α = 1 (so Re ρ = 1/2). On smooth compact manifolds α = 0
necessarily — the arithmetic analogue must be singular enough to
allow α = 1. [conjectural]

Still open: (a) Ruelle zeta of (X₀, φ^t) = Hasse-Weil zeta of 𝔛₀
(the "governing expectation"; needs all Fuller indices of the
packets Γ_{x₀} to be 1 — posed as an open question in v1 §5);
(b) the 3D Riemann-surface-lamination subsystem Y₀ for Spec ℤ;
(c) the cohomology on which Θ would act with the right spectrum.

## 4. Relation to 11l (the mechanism node)

11l and Deninger are the SAME structural hypothesis at two levels:

  11l (computable, finite): quantum graph, prime-labeled closed
    orbits of lengths log p → quantum-graph trace formula →
    spectral TONES at prime frequencies. [computationally verified]

  Deninger (arithmetic-geometric): Spec ℤ → dynamical system with
    prime-labeled closed orbits of lengths log p [theorem] →
    transversal index formula [theorem in foliation setting] →
    (conjecturally) ZETA ZEROS as spectrum of Θ. [conjectural]

11l is the computable proof of concept for Deninger's structural
hypothesis: it demonstrates that the orbit→spectrum-via-trace-formula
machinery WORKS when the prime-orbit geometry is present. Deninger
supplies the theorem that the prime-orbit geometry itself is real
(not a metaphor): closed points of Spec ℤ ARE packets of periodic
orbits of lengths log p in a constructed dynamical system.

Honest boundary (two of them):
(i) 11l tests orbit→TONE (spectral fluctuations), not orbit→ZERO
(eigenvalues). Deninger's claim is the stronger one: primes as
orbits, ZEROS as spectrum of Θ. 11l validates the mechanism
(trace formula from prime orbits), not the full conjecture.
(ii) This node yields NO computable operator. Θ acts on a
foliation cohomology that does not exist yet (the 3D subsystem is
open). There is no matrix to diagonalize, no tone probe to run.
Per D8 (formulate, do not simulate shadows), we do not build a
toy "Deninger-like" operator and pretend it is Deninger's.

## 5. Verdict and path

Node 11m verdict: Deninger is REAL where it matters structurally
(the prime-orbit dynamical system exists by theorem, published
2026) and CONJECTURAL where it matters spectrally (Θ, the
cohomology, Ruelle = zeta, the 3D lamination). 11l confirms the
mechanism in miniature; Deninger is the arithmetic-geometric home
it points to. But the operator hunt cannot proceed THROUGH
Deninger computationally — the path forward stays via finite
computable analogues (11l-style: more topologies, the
geometry-control with non-prime loops, amplitude-structure
matching) and the function-field template (Weil: complete, the
model for what "done" looks like).

Epistemic labels: existence of prime-orbit system [exact theorem];
transversal index formula [exact theorem, foliation setting];
Ruelle = Hasse-Weil [conjectural]; Θ's spectrum = zeros
[conjectural]; 3D lamination subsystem for Spec ℤ [open];
11l-mechanism→Deninger-hypothesis link [heuristic, structurally
grounded].

References: arXiv:1807.06400; arXiv:2301.11643; [Den98] Proc. ICM
1998 Vol. I, 163–186. Related: Morishita arXiv:2508.15971 (2026)
relates Deninger's systems to Connes–Consani adelic spaces, closed
orbits ↔ primes on both sides.
