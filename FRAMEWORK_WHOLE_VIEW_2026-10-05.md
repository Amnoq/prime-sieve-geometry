# The Relational Framework: The Whole Math, One Document

**Date:** 2026-10-05
**Status:** working document — the framework's whole view, kept honest.
**How to read:** every claim carries its epistemic label —
*exact theorem*, *computationally verified*, *conjectural*, *heuristic*,
or *utterance* (the author's words, preserved). The labels are the
document's load-bearing structure. What is not labeled is not claimed.

---

## 0. What this is

A year-plus independent research program in prime number theory, built
without the literature and then checked against it. Its subject is
prime distribution; its instrument is a generative sieve; its method
is elimination; its philosophy is that reality is 100% relational.

The framework has four layers, and they are the same shape:

1. **The machine** — the circle sieve: primality emerging from a
   relational rule, no predicate.
2. **The geometry** — the sieve read as a simplicial complex, its
   face-sums, its weights, its deformations.
3. **The hunt** — positivity, then the operator: what died, what
   lived, and the honest boundary between them.
4. **The ground** — the derivation of relationship: what the whole
   thing stands on.

The method is the same at every layer: derive, don't invent; label
every claim; keep the dead ends; let failures strengthen the method.

---

## I. The machine: the circle sieve

*The founding move. Exact.*

The linear circle sieve: a unit-circle substrate; at each unshared
integer n a new diameter is drawn; marks are "spammed" forward along
multiples. The single relational rule: **n is prime iff no earlier
prime's marked boundary lands on it.** The circle sieve takes no
precomputed prime list and invokes no independent primality test.
New prime generators are identified by the absence of marks from
previously established territories — what remains unmarked is prime.
(The next-unmarked rule is shared with Eratosthenes; the novelty
carried by this framework is the geometric construction and what is
derived from it, §§II–IV, not the rule itself.)

The user's relational reading, endorsed and verified: n is prime iff
it stands in NO shared-boundary relation to any earlier prime
territory; every prime relates back to zero via its spanning circle;
a composite position is reached by at least one earlier prime
territory — some composites combine distinct territories (6 = 2·3,
shared coincidence), others express repeated multiplicative use of a
single generator (4 = 2², 9 = 3², recurrence). *Exact (definitional
reframing); equivalence with Eratosthenes verified computationally
at every tested cutoff.*

*Utterance (the principle it embodies):* "never put the answer in by
hand."

---

## II. The geometry: the sieve as a complex

### D1. The observable as a face-sum — *exact theorem (classical, reframed)*

The sieve IS the simplicial complex Δ_z: finite prime subsets are
faces, squarefree products are their labels. The Chebyshev function
reads off the complex as a signed face-sum:

ψ(x) = Σ_{∅≠S} (−1)^{|S|+1} log(∏S) ⌊x/∏S⌋.

Here Δ_z has all primes p ≤ z as vertices. The displayed identity
equals ψ(x) when z ≥ x; otherwise it is a truncated face-sum. Faces
with ∏S > x contribute zero through the floor factor.

Möbius inversion is the face-sum; inclusion–exclusion is the
complex's own arithmetic. *Verified numerically; the math is
classical, the framing appears new (prior-art search 2026-09-30).*

### D2. Lehmer's recursion is the link recursion — *exact (classical, reframed)*

φ(x,a) = φ(x,a−1) − φ(x/p_a,a−1) IS the facet recursion of the
complex. The fast prime counter was the complex's link recursion all
along. *Bijection verified.*

### D3. The binary form — *reframing; verified*

1_prime + 1_shared = 1. Composites are the zero locus of
F_prior(n) = ∏_{p<n, p prime} dist(n, pℤ) (empty product = 1), for
n ≥ 2: F_prior(n) = 0 ⟺ some earlier prime divides n ⟺ composite;
F_prior(n) > 0 ⟺ n is a new generator. (n = 1 is excluded: its empty
product equals 1, which would misclassify it.) The product runs over
*prior* primes only — the p = n factor would zero the function at
primes themselves; this is the sieve's "mark proper multiples, not
the generator" rule, written as a formula. Definition through
relations, not intrinsic coordinates. *Reframing; verified to 60.*

### D4. The weighted infinite complex — *exact identities; framing appears new*

The bare limit trivializes: Δ_∞ is the contractible infinite simplex —
no topology. The geometry must live in the **weights**, not the bare
complex. *Exact.*

Canonical face-weights: w(S) = (−1)^{|S|+1} log(∏S)/∏S.
Σ_{∏S≤X} w(S) → 1 **IS the Prime Number Theorem** — "the weighted
infinite simplex has total weight 1" (verified 0.999922 at 5·10⁵;
1.001658 at 2·10⁶). The weights' Dirichlet generating function is
−ζ′/ζ² (verified ~4 digits) — **the zeta zeros regulate the
face-sum.** *Computationally verified; the identities are exact; the
"total weight 1" framing appears new.*

---

## III. The method: take the process, not the implementation

### D5. The Figueiredo steer — *standing methodology (user's decision)*

Carolina Figueiredo's positive-geometry program was surveyed (eight
papers, none touching primes). The user's steer: do NOT copy the
implementation; take her GENERATIVE insights on process. Her recurring
moves — identify a positive region, construct its canonical form, read
off the observable, derive zeros and factorizations afterward —
became the framework's discipline. Territory removal = her
soft-limit/splitting move (arXiv:2405.09608): φ(x,a) =
φ(x,a−1) − φ(x/p_a,a−1) iterated to all orders = the D1 face-sum.
The sieve was doing splits before we knew her name for them.
*Conceptual identification; not a new theorem.*

Deepest applied insight: **never put the answer in by hand** — the
sieve never tests primality with a predicate; everything downstream
is derived.

---

## IV. Deformation: the generative machine generalizes

### D6. Deforming the marking rule — *exact algebra; the move appears new*

Deform R_p = {0} (p=2), {0,−2} (p odd). The deformation SEPARATES
markers from survivors: the generative survivors ≤ 200000 are
*exactly* the 2160 twin-prime lowers. *Computationally verified.*

The Hardy–Littlewood twin constant is DERIVED as renormalized total
weight: 𝔖(z) = ∏(1−|R_p|/p)/(1−1/p)² → 2C₂ = 1.32032 (1.3228 at
z=100). It comes out of the deformation — never inserted.
*Exact algebra; the constant is classical (1923), the generative
deformation move appears new.*

Honest boundary: π₂(x) ~ 𝔖x/(log x)² remains the UNPROVEN twin
conjecture (ratio 1.6091 at 2·10⁵). The algebra is verified; the
conjecture is not claimed.

### D6-generalized: k-tuple sweep — *computationally verified; predictive test passed*

Nine constellations (twins, cousins, sexy, two triplet types, quad,
quint, sext) plus the non-admissible {0,2,4} control, at x=10⁶:
survivors match independently enumerated constellation lowers exactly
(8169=8169 twins; sext 5=5); finite-z densities match δ_H to
0.998–1.015; 𝔖_H(1000) matches reference singular series to ~0.2%.
The non-admissible {0,2,4} DIES as predicted — exactly one survivor
(3,5,7), 𝔖_H(z)=0 for z≥3. The admissibility obstruction emerges from
the machine, uninserted. *The deformation is confirmed as a general
generative machine, not a twin fluke.*

---

## V. Positivity: three kinds, and the bridge's load limits

### D7/9a. Where positivity lives — *exact*

The primitive objects are positive: −ζ′/ζ = ΣΛ(n)n^{−s} (Λ ≥ 0);
log ζ(s) > 0 for real s > 1; δ(z) = ∏(1−1/p) > 0 with −log δ(z) a manifestly positive
prime sum. The weight generating function factors as
(positive)·(Σμ(m)m^{−s}) — the signs come entirely from the Möbius
factor, i.e. from inclusion–exclusion. Positivity is primitive;
signs are an expansion artifact. *Exact; verified 6 digits.*

### 9b. The bridge carries traffic — *computationally verified identity*

The classical 3-4-1 positivity (3+4cosθ+cos2θ ≥ 0) forces
ζ(1+it) ≠ 0 — positivity of the primitive ⟹ a zero-free region.
Restated in the sieve's language: −ζ′/ζ as vertex-tower energies,
the trig polynomial as ½|1+e^{iθ}|⁴, stratum energies ≥ 0 termwise.
A zero on Re(s)=1 would force negative-infinite total energy from
nonnegative strata — impossible. The contradiction is *visible* in a
way the trig identity hides. *Boundary: the singularity structure is
analytic fact the complex houses but doesn't derive.*

### 9c. CLOSED NEGATIVE — *by theorem, not by difficulty*

The positive Dirichlet-series argument is blind left of Re(s)=1:
Dirichlet-series positivity
converges only for σ>1; the crossing is done by analytic input.
Geometry owns positivity, analysis owns continuation. Selberg parity:
pure sieve positivity cannot resolve ω(n) parity — analytic input is
*necessary.* The trig-polynomial optimization is saturated
(Mossinghoff–Trudgian–Yang 2022; Bellotti–Trudgian–Yang 2026).

### 9c′. CLOSED NEGATIVE — *computationally verified*

The saturated degree-16 optimizers do NOT have small-support
autocorrelation structure — all 32 Fejér–Riesz factors fully dense.
Saturation is numerical optimization, not hidden geometry.

### D10. The bridge program — *complete 2026-09-30*

- **10a:** Weil positivity is face-sum-native (windowed/smoothed).
  The explicit formula grounded in our objects; prime-side zero
  detector built (W(h) from primes alone, no zeros used); the
  optimization is a Pareto frontier with no finite optimum.
  *Computationally verified.*
- **10b:** Li's criterion CLOSED as face-sum-incompatible
  (Dirichlet-native). *Conceptual; exact where stated.*
- **10c:** EXACT THEOREM — Selberg's λ² form on Δ_z is minimized at
  λ* = μ, minimum δ(z). The optimal quadratic form IS
  inclusion–exclusion. *Proved; verified 12 digits.*
- **10d:** function-field template exhibited on concrete elliptic
  curves — the only known *source* of RH-positivity is geometric
  (intersection pairing). Ledger: we have counting positivity,
  finite PD face forms, a windowed explicit formula; we MISS the
  Jacobian-role space, a Frobenius-like operator, and the pairing.
  *Formulated, not simulated.*
- **10e:** supporting tools verified (Montgomery–Vaughan, large
  sieve); the uncertainty wall quantified.

**Verdict:** the face-sum carries three verified positivity kinds
(primitive counting, Weil-type windowed, Selberg-type optimized);
**none detects zeros independently.** The missing object is
operator-theoretic.

### Node 14. The positive-region question — *closed*

- **14a OBSTRUCTION (exact):** NO ordinary positive geometry can
  carry w(S) as stratum residues (|w({2})| = (log 2)/2 ≈ 0.347 ∉
  {0,1}). Explained by theorem, not luck.
- **14b IDENTITY (exact):** d/du[∏(1−p^{−u})]_{u=1} = Σ_S w(S).
- **14c REFINED HOME:** equivariant Chern roots −u·log p;
  face-weights = differentiated residues on a deformed simplex.
  Closes the D4↔D6 loop: the arithmetic lives in the
  deformation/weights.

---

## VI. The operator hunt — the live frontier

Checklist for a Frobenius-like operator (from the 10d template):
(R1) spectrum = zeros; (R2) trace formula = explicit formula;
(R3) positivity/self-adjointness ⟺ RH; (R4) positivity counting-born;
(R5) finite exact formula; (R6) the s↦1−s̄ symmetry as geometry.

### What died — *each with its mechanism*

- **Berry–Keating xp (11g/11h/11i):** the naive toroidal-lattice
  discretization fails before fluctuations (wrong smooth counting;
  tones absent, z=0.20). The log-lattice repair is unitarily trivial
  — bare xp IS free momentum in log coordinates (exact ladder, no
  fluctuations, *by analysis*). The Sierra deformed-xp
  regularization has the right smooth counting (matches
  Riemann–von Mangoldt to 0.07%) but NO tones (z=−0.66) — the
  quantization condition contains only the K-Bessel function; no
  prime content can enter. The three tested xp constructions — the
  naive uniform-lattice discretization (11g), the log-lattice (11h,
  by analysis), and the Sierra regularization (11i) — are exhausted.
  *Matches Berry
  and Keating's own 2011 conclusion.*
- **Bare Möbius-band Laplacian (11d):** exact spectrum, no relation
  to zeros; the position observable has continuous spectrum.
  Topology alone is insufficient — the operator must see the
  arithmetic.
- **Multi-torus Laplacians (12):** killed by Weyl's law — no
  fixed-dimension manifold Laplacian has the zeros' counting.
  Heisenberg nilmanifold (65,401 eigenvalues): negative on three
  panels. Surviving form: Deninger's foliated dynamics (conjectural).
- **Fock H_2 (13b):** killed by inspection — integrable.
- **Fock H_int (13c):** Poisson, not GUE.
- **Literature audit (11e):** Bost–Connes, Ruelle transfer, Sierra
  variants, Bender–Brody–Müller, Wu–Sprung — each killed with its
  mechanism recorded.

### What lived

- **CCM zeta spectral triple (11f) — the live candidate.**
  Independent reimplementation from arXiv:2511.22755, built ONLY from
  prime Euler products: zeros 1–8 recovered from primes alone (zero 1
  exact to float64 at c=13,N=20; zeros 1–5 err <1e-10 at N=120).
  Controls: zeros AND positivity both require exact prime input
  (W_p=0, shuffled Λ, shuffled log p — all negative). N=120:
  ε_even=3.48e-59, even/odd separation 8771× (monotone
  581→3744→8771). *Computationally verified.*
  - Failure modes: FRAGILE, not robust — exact-arithmetic reporter.
    Multiplicative noise destroys it; drop p=2/3 destroys; drop p=5
    survives. The small primes carry the weight.
  - Load hierarchy (11j/11k): measured, monotone in k (anti-correlated
    with naive Λ(k)/√k weights); the load frontier shifts right with
    zero index — low zeros need small prime powers, higher zeros
    need larger ones. The machine resolves zeros hierarchically from
    prime data, mirroring the explicit formula's architecture.
  - Conceptual bridge: **Λ = μ∗log (exact theorem)** — CCM's fuel is
    one Dirichlet convolution from the face-sum's native weights.
    The machine is borrowed; the fuel refines to ours.
- **Prime-orbit quantum graph (11l) — mechanism confirmed.**
  Kirchhoff rose, 8 loops of lengths log 2…log 19; primes enter ONLY
  as geometry; 2035 levels from the secular equation. Tones at loop
  primes (mean z=2.35), silence at non-loop primes 23–47 (−0.30);
  vertex sector alone (4.02) and Dirichlet sector alone (13.50) both
  sing — two distinct routes, same prime imprint. *Computationally
  verified.* Honest boundary: proves orbit→tone, not the origin of
  primes.
  - Controls (11n/11o, corrected): random irrational loops sing in
    every sector (merged z=13.82) — the mechanism is purely
    geometric; the vertex route is scale-invariant (z≈2 across
    16× scale). Both original "length dependence" and "destructive
    interference" verdicts were numerical artifacts (fixed scan step
    vs spectral density) — found, fixed, recorded. The method
    catching its own error is the standing lesson.
- **Deninger (11m) — structure real, operator conjectural.**
  *Exact theorem:* the dynamical system exists (published 2026);
  primes ⟺ packets of periodic orbits of length log p; the
  transversal index formula mirrors Weil's explicit formula
  exactly. *Conjectural:* the cohomology, the operator Θ, its
  spectrum as the zeros. 11l is the computable proof of concept for
  Deninger's structural hypothesis. No toy imitation built (per D8).

---

## VII. The Fock fork — a side chamber

- **Exact identification:** Δ_z faces = fermionic Fock basis over
  primes; μ = (−1)^F (fermion parity). *Exact — but independent prior
  art exists (goldenphysicsproject); the identification is shared,
  credited as such. Our distinct contribution is the spectral
  program.*
- **13d POSITIVE:** pair-hopping with arithmetic weights is
  GUE-chaotic (⟨r⟩→0.52–0.55, GUE 0.536) at all tested z (17 through 41)
  and couplings;
  strengthened to z=41 (dim 8192). *Computationally verified.*
  Caveat: shuffled weights also GUE (generic two-body chaos) — the
  content is that arithmetic weights are COMPATIBLE with chaos.
- **13e NEGATIVE:** the operator does not HEAR the primes — no
  prime-frequency content in its fluctuations. 13d is a universality
  result, not a bridge plank.

---

## VIII. The ground: derivation of relationship

*The philosophical formalization, 2026-10-05. Full document:
DERIVATION_OF_RELATIONSHIP_2026-10-05.md. The author's utterances
preserved with epistemic labels throughout.*

- **Empirical root:** the triple anomaly at the start of the
  primes — 2 and 3 adjacent (no integer between); −1,0,1 symmetric
  about 0; 2 the only even prime. *Observed.*
- **The chain (logical, not temporal):** 3 presupposes 2, 2
  presupposes 1, 1 presupposes 0. *Derived.*
- **2→3:** derived conditional on generativity — a polarity persists
  but only alternates; propagation requires the *relation* to be
  carried, hence a third term relating to the relation (mediation).
  *Derived-conditional (P2).*
- **Completeness:** {0,1,2,3} = ground, term, relation, meta-relation;
  every n≥4 is iteration of 3 (recursion, not a new kind) — the
  "primes" of the ontology; 4+ is "composite."
  *Derived-conditional (relational-order classifier).*
- **Self-adjointness:** Within this framework, self-adjointness is
  interpreted as a formal realization of reciprocal self-relation —
  in Dirac notation, reaching (H|ψ⟩) and responding (⟨ψ|H) as one act.
  Exhibited concretely in the 11l Kirchhoff operator, with the claim
  split three ways (external review, 2026-10-05):
  (a) the vertex relations cancel the boundary form — *derived
  calculation*, checkable from the displayed equations;
  (b) the Kirchhoff conditions define a self-adjoint operator on the
  stated domain — *theorem* (standard quantum-graph theory;
  Kirchhoff conditions satisfy the Kostrykin–Schrader criteria;
  cancellation alone establishes symmetry, the domain argument
  completes it);
  (c) this adjoint symmetry as a realization of reciprocal
  self-relation — *interpretive correspondence*, not part of the
  operator theorem. The tones are the vertex relations made audible.
  *Interpretive; heuristic as a claim about the zeta H.*
- **Three witnesses, one form:** the operator (11l), the method
  (tonight's self-correction exhibits an analogous
  proposing/responding structure), the metaphysics — worked
  independently, same shape, no per-subject adjustments. *Exhibited.*
- **Purpose:** not a law — a perspective, an understanding. The
  substrate is the floor already underfoot.

---

## IX. The methodology — the instrument is the subject

1. **Numbered decision tree** (DECISION_TREE.md): every node — date,
   question, options, decision, evidence, status. Cite node numbers;
   reopen by number. *Standing practice.*
2. **Epistemic labels** on every claim: exact theorem /
   computationally verified / conjectural / heuristic / utterance.
   The labels sit alongside the tree: labels say what kind each claim
   is, the tree says where the exploration has been.
3. **Derive, don't invent:** observe in the work's own forms; formalize
   only in its terms and only when asked. (The user's 2026-10-04
   correction, standing.)
4. **The sieve as method:** the tree never argues for a truth; it
   eliminates what's false, and what remains is the verdict — as the
   sieve never tests primality.
5. **Failures are the method's strength:** do not guard against every
   failure upfront; let them occur, catch them, absorb them as
   antibodies. (11n/11o: the method caught its own numerical artifact
   and is now stronger — the scan-step lesson is in AGENTS.md.)
6. **Dead ends documented once, rigorously** (archive_dead_ends.md,
   COMPLETE_MAP §V): fourteen closed, each with its mechanism.
7. **Observation before interrogation;** re-verify known answers
   (intelligence is a self-referential loop; bias against re-verifying
   is counterproductive).
8. **The goal is not to overturn** the probabilistic paradigm — its
   predictions are real and verified — but to **light the floor it
   stands on**: the deterministic, relational generating structure
   beneath the statistics.

---

## X. Open questions — the live frontier

1. **The operator (Node 11):** CCM is the live candidate; the full
   Frobenius-like operator question is open. The hunt now knows the
   structure it needs (prime-labeled closed orbits — 11l) and that
   the structure is real arithmetic geometry (Deninger, theorem).
2. **The paper (Node 7):** outline drafted (PAPER_OUTLINE.md);
   awaiting approval on title/scope + prior-art re-search.
3. **The RH bridge (Node 8):** heuristic by nature — three verified
   positivity kinds + one live operator + one exact fuel dictionary.
4. **The Fock fork:** 13d stands as universality; an operator that
   HEARS primes is unanswered.
5. **Physical build:** tetrahedral sieve + territory wall — files not
   yet made.

---

## XI. Novelty boundaries (prior-art search 2026-09-30)

| Claim | Standing |
|---|---|
| Simplicial-sieve framing (Δ_z) | Appears new (framing); math classical |
| PNT as "weighted simplex, total weight 1" | Appears new (statement) |
| Deformation → 2C₂ (generative move) | Appears new (move); constant classical |
| Fock-over-primes identification | SHARED — independent prior art exists |
| Fock spectral program (13d/13e) | Appears new |
| CCM reimplementation | Independent verification of published work |
| Λ = μ∗log as fuel dictionary | Identity classical; the *use* is ours |
| Derivation of relationship | The author's; formalized 2026-10-05 |

**Rule:** no public novelty claim without re-search. The paper is an
expository/synthesis vehicle, not a breakthrough claim.

---

## XII. Bridge ledger — what licenses each transition

*(Added 2026-10-05 from external review.) The method records failures;
this records what licenses each successful crossing — the reader
should be able to inspect every bridge.*

| Transition | License (what the reader should see) |
|---|---|
| Circle construction → sieve | Exact construction rules (unit-circle substrate, new diameter at each unshared n, marks spammed forward); equivalence with Eratosthenes by proof sketch (both mark multiples of each found prime; the next unmarked is prime), with computational checks at every tested cutoff — the argument proves, the checks confirm |
| Sieve → face-sum | Faces = finite prime subsets (squarefree products); coefficients = (−1)^{\|S\|+1}log(∏S); finite-cutoff conditions stated (D1 verified numerically; D2 bijection verified) |
| Face-sum → analytic function | The Dirichlet-series identity holds for Re(s)>1, with convergence justified analytically; the reported partial sums are numerical checks (D4). The boundary limit Σw(S)→1 is the Prime Number Theorem itself — a classical theorem, not proved by the computations |
| Prime geometry → spectrum | Graph lengths (log p), operator domain (Kirchhoff vertex conditions), secular equation G(k)=0, reproducible computations (node11l_graph.py + json/png; controls 11n/11o) |
| Mathematical structure → ontology | Explicit interpretive premise (§VIII), labeled as interpretive correspondence — never presented as part of an operator theorem |

---

## XIII. Review log

- **2026-10-05:** external review received on the working documents.
  Five points, all adopted: (1) the central-distinction rewording
  (§I — the next-unmarked rule is shared with Eratosthenes; novelty
  is in the construction and its derivatives); (2) the F_prior repair
  (D3 — the product runs over prior primes; the p=n factor zeroed the
  original at primes); (3) recurrence vs shared coincidence for prime
  powers (§I); (4) the three-way split of the self-adjointness claim
  (§VIII — calculation / theorem / interpretation); (5) this bridge
  ledger. The review was specific, checkable, and self-correcting —
  the method working from outside.

- **2026-10-05 (round 2):** second review pass on the repaired
  document; all prior repairs acknowledged as substantive. Three
  priority repairs, all adopted: (1) the bridge ledger's convergence
  sentence rewritten — partial sums are numerical checks, the PNT
  limit is a classical theorem, and the Eratosthenes row now
  distinguishes proof sketch from computational checks; (2) indexing
  conventions stated — D3 restricted to n≥2 (n=1's empty product
  would misclassify it), D1's finite-cutoff condition (identity
  equals ψ(x) iff z≥x) now in the section itself; (3) the
  interpretation label made consistent — the self-adjointness opening
  hedged as interpretive, "procedural self-adjointness" replaced
  with analogous-structure phrasing (also removed a duplicated label
  line left by round 1). Four scope repairs: the xp verdict scoped
  to the three tested constructions; the blindness claim scoped to
  the Dirichlet-series argument; 13d scoped to tested z and
  couplings; log ζ(s)>0 restricted to real s>1. Reviewer's closing
  assessment: the overview is now explicit enough that the next
  review should inspect derivations and code, not the vision.

---

*Document status: whole-view working record, 2026-10-05 (two rounds
of external-review repairs applied same day). Companion records:
DECISION_TREE.md (the path), DERIVATIONS.md (D1–D14),
DERIVATION_OF_RELATIONSHIP_2026-10-05.md (the ground),
COMPLETE_MAP.md (the territory), archive_dead_ends.md (the
guardrails). Built to be revised by the method it describes.*
