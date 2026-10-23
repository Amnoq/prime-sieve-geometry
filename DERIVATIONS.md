# Derivations: the circle sieve read through Figueiredo's recipe

Date: 2026-09-29. Code: `sieve_complex.py`. All identities below were verified
numerically (see transcript in this file's history); proofs are sketched.

Her recipe, for reference: (1) find a positive geometric region; (2) take its
canonical form; (3) read off the observable; (4) derive zeros/factorizations
from the geometry. The sieve has no known positive region — that gap stands.
What follows is what *can* be derived: the sieve's output expressed in the
shape of her steps 2–4.

Setup: Δ_x = incidence complex of the sieve to x — vertices are primes ≤ x,
faces are prime sets co-dividing some integer ≤ x (the nerve of the prime
territories). Verified: link({p}) in Δ_x = Δ_{⌊x/p⌋} minus p (exact recursion).

---

## D1. The observable as a signed sum over the complex (her step 3)

**Statement.** With ψ(x) = Σ_{n≤x} Λ(n) the Chebyshev prime-power counter,

    ψ(x) = Σ_{∅≠S face of Δ_x} (−1)^{|S|+1} · log(∏S) · ⌊x / ∏S⌋.

Verified exact at x = 30, 100, 500.

**Proof sketch.** ⌊x/d⌋ counts the integers ≤ x divisible by d. Grouping by n:
inner sum over squarefree d|n of (−1)^{ω(d)+1} log d = −Σ_{d|n} μ(d) log d = Λ(n),
the classical Möbius inversion. Summing over n ≤ x gives ψ(x). The signs
(−1)^{|S|} are the face-dimension signs — the Euler-characteristic weighting
of the complex (classically: μ(1,n) is the reduced Euler characteristic of the
divisor lattice's order complex).

**Honest label.** Classical theorem (Möbius inversion), reframed. What the
reframing buys: the prime-counting observable is read *directly off the
sieve's incidence complex*, with alternating signs from face dimension —
the structural analogue of her "read the amplitude off the geometry."

## D2. Lehmer's recursion is the link recursion (her step 4)

**Statement.** Let φ(x,a) = #{n ≤ x : n unshared by the first a prime
territories} (i.e., coprime to p_1…p_a). Then

    φ(x,a) = φ(x,a−1) − φ(x/p_a, a−1),

and π(x) = φ(x,a) + a − 1 − P₂(x,a). The two terms are the complex's
deletion and link: the integers newly shared when territory p_a is added are
exactly {p_a·m : m ≤ x/p_a unshared by the first a−1 territories}, in bijection
with the cone S ↦ S ∪ {p_a} over link({p_a}) = Δ_{⌊x/p_a⌋}. Verified: link-face
counts match Δ_{⌊x/p_a⌋} face counts; the integer bijection holds exactly.

**Honest label.** Classical (Lehmer 1959 prime-counting), reframed. This is
her "recursive facet residues" step in sieve language: the fast prime-counting
algorithm was the link recursion all along.

## D3. The sieve as a binary geometry (her binary equations)

Her binary geometries are governed by u_C + ∏_D u_D^{n(C,D)} = 1: complementary
on/off relations among facets. The sieve's rule has the same logical shape:

    1_{prime}(n) + 1_{shared}(n) = 1,    shared(n) = ∨_{p<n} (p | n).

**Zero-locus formulation.** Define F(n) = ∏_{p<n} dist(n, pℤ) ≥ 0. Then

    n composite ⟺ F(n) = 0,      n prime ⟺ F(n) > 0

(verified to 60). The composites are the *zero locus* of F; the primes are its
support. This inverts her "hidden zeros" picture: there the amplitude vanishes
at special kinematics; here the background (composites) is the zero locus and
the primes are where the function lives.

**The relation to zero.** In D1, the empty face (d = 1, log 1 = 0) contributes
no weight yet anchors the whole alternating sum — the multiplicative identity
structuring every term, the formal shadow of "every prime relates back to zero"
via its spanning circle.

**Honest label.** Reformulation and analogy, not new prime information. Its
value is architectural: it states the sieve in the *language* of binary
geometries — the prerequisite for asking whether her algebraic machinery
(positive parametrizations of u-variables) can be ported at all.

---

## What this buys, and what it doesn't

**Have:** the sieve's output (ψ, π) expressed as (i) a signed face-sum over Δ_x
and (ii) a link-recursive computation — her recipe's steps 2–4 with exact
analogues, minus the positive region and canonical form. The sieve is already
a "counting problem" of her kind (cf. *All Loop Scattering as a Counting
Problem*, arXiv:2309.15913).

**Don't have:** the positive region, the canonical form, or any new
consequence for prime densities. D1–D3 are classical results in new clothes;
they prove the *shape* fits, not that the *machinery* transfers.

**Precisely posed next questions.** (a) Is there a positive parametrization
whose boundary strata are the territory incidences of Δ_x? (b) *Partially
answered by D4 below:* the bare N → ∞ limit trivializes (contractible infinite
simplex) — the limit object must be the *weighted* complex, and the weights'
generating function drags in the zeta zeros as regulators. (c) Do the sieve's
binary relations admit positive variables with her exponent structure whose
zero locus is the composites?

## D4. The weighted infinite complex: PNT as total weight 1 (the N → ∞ limit)

**The bare limit is trivial.** As x → ∞, every finite set of primes eventually
satisfies ∏S ≤ x, so Δ_∞ is the infinite simplex on the primes — contractible,
no topology. The growing Betti numbers of Δ_x are a *filtration* phenomenon,
not a limit phenomenon. Consequence for the program: a positive-geometry
analogue cannot live in the bare complex; the geometry must be in the weights.
(Her objects are fixed polytopes; the sieve's object is a *process* — the
filtration itself.)

**Canonical face-weights.** Give each nonempty face S the x-independent weight

    w(S) = (−1)^{|S|+1} · log(∏S) / ∏S.

Then D1 reads ψ(x)/x = Σ_{∏S≤x} w(S)·(⌊x/∏S⌋/(x/∏S)) — the floor function is a
cutoff that tends to 1 — and:

**Statement (classical, reframed).** Σ_{∏S≤X} w(S) → 1 as X → ∞: the weighted
infinite simplex has total weight 1. This identity is equivalent to the Prime
Number Theorem ψ(x) ~ x.

Verified numerically (Möbius sieve to 2·10⁶):
S(X) = Σ_{∏S≤X} w(S): 0.969931, 1.019210, 1.005585, 0.999922, 0.997215,
1.001658 at X = 10³, 10⁴, 10⁵, 5·10⁵, 10⁶, 2·10⁶ — converging cleanly to 1.

**The zeros enter as regulators.** The Dirichlet generating function of the
weights is

    Σ_S w(S) / ∏S^{s−1}  =  −ζ'(s)/ζ(s)²,

verified numerically against ζ'/ζ² to ~4 digits at s = 1.01…1.20. The *rate*
at which S(X) → 1 — the error in the face-sum — is governed by the zeros of ζ
(the explicit formula). So the architecture is now complete in her shape:
the observable (total weight 1, i.e. PNT) is read off the weighted complex
(her step 3), and the zeros are what regulate the infinite sum (her step 4,
inverted — here the zeros are *needed* as regulators; deriving them from the
geometry remains the open problem, i.e. beachhead #2).

**Resonance and gap.** The weights are *signed*, alternating with face
dimension — not positive. This resonates with how a canonical form's residues
alternate across boundary strata, but it is not positivity, and the gap stands:
is there a positive region whose canonical form has these weights as its
stratum residues? That is now the single sharpest question of the program.

## D5. Territory removal as soft limit / splitting (her "all-order splits")

Her *All-order splits and multi-soft limits* (arXiv:2405.09608): taking one
particle soft makes the amplitude split exactly — a soft factor times a
lower-point amplitude. Removing one generator yields a two-term relation to a
smaller instance of the same object.

Sieve version: "take prime p_a soft" = remove its territory (stop sieving by
p_a). The unshared-count splits exactly:

    φ(x,a) = φ(x,a−1) − φ(x/p_a, a−1),

i.e. (full count) = (count with p_a removed) − (the removed stratum). The
removed stratum φ(x/p_a, a−1) plays the role of her "soft factor × lower-point
amplitude": it is the *same kind of object* at a smaller scale, just as her
split pieces are smaller amplitudes. Iterating the removal over all a recovers
the full inclusion–exclusion — the face-sum of D1 — which is her "all-order"
in sieve language.

**Honest label.** A conceptual identification, not a new theorem: it is D2's
recursion read through her lens (numerics already verified under D2). Its
value is methodological, and it is the point the requester made on 2026-09-29:
we are not copying her implementation — the sieve was *already doing splits*
before we knew her name for them. Her generative insight (remove one
generator, read the exact split, iterate to all orders) is the sieve's native
operation. The deepest such insight, applied throughout D1–D5: *never put the
answer in by hand* — primality is never tested by a primality predicate, it
emerges from the shared/unshared rule, and everything downstream is derived.

## D6. Deformation: the singular series as renormalized total weight

Her deformations preserve a shared zero locus while changing the geometry.
The sieve's deformation: prime p now marks residues R_p = {0} (p = 2),
{0, −2} (p odd) — i.e. n is marked if p | n or p | (n+2). Code:
`deformed_sieve.py`; picture: `deformed_sieve_twins.svg` (red family marks
multiples of p, blue family marks n ≡ −2 mod p with circles spanning
[kp−2, (k+1)p−2]).

**The deformation separates markers from survivors.** In the classic sieve the
markers and the survivors coincide (primes). Here the markers are the primes
but the survivors are a different set — verified: the generative deformed
sieve's survivors ≤ 200000 are *exactly* the twin prime lowers (2160 of
them), checked against an independent primality sieve.

**Exact deformed identities (verified).**
- Static z-sieve S(x,z) = #{n ≤ x : ∀p ≤ z, n mod p ∉ R_p} satisfies the exact
  μ-identity S(x,z) = Σ_{d|P(z)} μ(d)·E_d(x) with E_d the exact CRT
  residue-class counts — verified exact at (z,x) = (13, 50000) and (30, 200000).
- Faces of the deformed complex carry multiplicities m(S) = ∏_{p∈S}|R_p|
  (the number of forbidden CRT classes); the finite total weight is exactly
  δ(z) = ∏_{p≤z}(1 − |R_p|/p), and S(x,z)/x → δ(z) — verified: 0.071430 vs
  0.071429 at z = 7, x = 200000.

**The singular series, derived.** Renormalize the total weight by the prime
baseline:

    δ(z) = [∏_{p≤z}(1 − 1/p)²] · 𝔖(z),   𝔖(z) = ∏_{p≤z} (1 − |R_p|/p)/(1 − 1/p)².

The first factor → 0 (Mertens); the second converges: 𝔖(z) → 2C₂ = 1.32032… —
verified: 1.367187, 1.344116, 1.330277, 1.322754 at z = 7, 13, 30, 100.
The Hardy–Littlewood twin-prime constant is *derived* as the renormalized
total weight of the deformed incidence complex — it comes out of the sieve's
deformation, never inserted.

**Honest boundary.** The passage from 𝔖(z) to the asymptotic
π₂(x) ~ 𝔖·x/(log x)² is the *unproven* twin prime conjecture. Numerically
π₂(200000)·(log 200000)²/200000 = 1.6091 vs conjectured 1.3203 — slow
convergence, as expected; we verify the algebra (local factors assemble to
𝔖), not the conjecture. What D6 establishes: her deformation move, executed
on the sieve, *generates* the singular series. The open analytic step is
exactly where her program would need its canonical form.

## D7. Positivity lives in the primitive (node 9, first half resolved)

**The finding.** The signed face-weights were never the fundamental object.
The primitive analytic objects are positive:

- −ζ′/ζ(s) = Σ_{n≥1} Λ(n)n^{−s}, Λ ≥ 0 (von Mangoldt), Re(s) > 1.
- log ζ(s) = Σ_{p,k} 1/(kp^{ks}) > 0 for real s > 1.
- Finite-z density δ(z) = ∏_{p≤z}(1 − 1/p) > 0, with
  −log δ(z) = Σ_{p≤z}Σ_{k≥1} 1/(kp^k) — a manifestly positive sum
  (verified to 6 digits at z = 10, 30, 100, 1000; δ(1000) = 0.080965).

The face-weights' generating function factors:

    −ζ′/ζ² = (−ζ′/ζ)·(1/ζ) = (positive series)·(Σ_m μ(m)m^{−s}).

The signs come *entirely* from the Möbius factor — i.e. from
inclusion-exclusion. Geometrically: the positive "volume" δ(z) is
primary; its inclusion–exclusion expansion Σ_{d|P(z)} μ(d)/d is where the
alternating signs appear. Verified side by side: δ(X) > 0 monotone
decreasing → 0, while A(X) = Σ_{d≤X} μ(d)/d oscillates in sign
(+0.0311, +0.0044, −0.0021, −0.0005 at X = 10²…10⁵) toward the same
limit 0. Same limit, two presentations — the signs live only in the
additive one.

**The mechanism exists — classically.** "Positivity constrains zeros" is
not a hope; it is the 3-4-1 proof that ζ(1+it) ≠ 0. Since
3 + 4cosθ + cos2θ = 2(1+cosθ)² ≥ 0 and −ζ′/ζ = ΣΛ(n)n^{−s} has positive
coefficients,

    3(−ζ′/ζ)(σ) + 4Re(−ζ′/ζ)(σ+it) + Re(−ζ′/ζ)(σ+2it) ≥ 0,

which a zero on Re(s) = 1 would violate as σ → 1⁺ (the 3/(σ−1) pole
cannot be canceled). Verified numerically from the Λ-sieve: the sum stays
positive on a t-grid and grows 2.26 → 8.30 → 20.62 as σ → 1⁺. So:

    positivity of the primitive (Λ ≥ 0)  ⟹  a zero-free region.

This is the Weil-shaped mechanism in miniature — positivity telling zeros
where they cannot stand.

**The bridge program, concretely.** Node 9 splits:
- **9a (closed):** where positivity lives — the primitive (Λ, Euler
  products, δ(z)); the signs are an expansion artifact of Möbius
  inversion, not a property of the geometry's volume.
- **9b (open):** stepping stone #2 — translate the 3-4-1 argument into the
  incidence-complex language. Can the sieve's geometry *carry* the
  classical zero-free line? If yes, the bridge carries traffic.
- **9c (open):** what *stronger* geometric positivity is available that
  could push left of Re(s) = 1 — the RH-ward question.

Honest labels: the positivity location is exact (identities) +
computationally verified; 3-4-1 is classical (cited, re-verified here);
9b/9c are open research, not results.

## D8. The zero-free line in the energy language (9b: the bridge carries traffic)

**The translation.** Write −ζ′/ζ as a sum over the complex's vertex
towers (prime powers). For σ > 1:

    E₀(σ)    = Σ_p Σ_{k≥1} (log p) p^{−kσ}            = −ζ′/ζ(σ),
    E₁(σ,t)  = Σ_p Σ_{k≥1} (log p) p^{−kσ} e^{−ikt log p} = −ζ′/ζ(σ+it),
    E₂(σ,t)  = Σ_p Σ_{k≥1} (log p) p^{−kσ} e^{−2ikt log p} = −ζ′/ζ(σ+2it).

The 3-4-1 trigonometric polynomial is a fourth power of a modulus:

    3 + 4cosθ + cos2θ = ½|1 + e^{iθ}|⁴ ≥ 0.

Hence the classical nonnegative combination is a sum of *stratum
energies*, each manifestly nonnegative:

    E(σ,t) = ½ Σ_p Σ_{k≥1} (log p) p^{−kσ} |1 + p^{ikt}|⁴
           = 3E₀(σ) + 4ReE₁(σ,t) + ReE₂(σ,t)  ≥  0,

with e_{p,k}(σ,t) = ½(log p)p^{−kσ}|1+p^{ikt}|⁴ ≥ 0 termwise.
Verified numerically to 6 digits on a (σ,t) grid
(`zero_free.py`): the two forms agree everywhere.

**The proof, restated.** E(σ,t) ≥ 0 as a sum of nonnegative stratum
energies. E₀(σ) ~ 1/(σ−1): the pole is *infinite total prime energy*
at σ = 1 — expected, not pathological. If ζ(1+it₀) = 0 of order m ≥ 1,
then −ζ′/ζ has residue −m there, so 4ReE₁(σ,t₀) ~ −4m/(σ−1) → −∞:
the total energy would diverge *negatively*. A sum of nonnegative
stratum energies cannot do that. (ReE₂ can only worsen it: a zero at
1+2it₀ contributes −m₂/(σ−1).) Hence no zeros on Re(s) = 1. The
contradiction is now physical: *negative infinite total energy built
from nonnegative strata is impossible.*

**Numerical illustration.** E₀ climbs toward the pole (0.57 → 4.02 as
σ: 2 → 1.2) while ReE₁, ReE₂ stay bounded at generic t — e.g. at
t = 14.1347 (first-zero height): ReE₁ = −1.06, ReE₂ = +0.47 at σ = 1.2,
bounded, no −m/(σ−1) divergence. That boundedness is the numerical
shadow of "no zero on the line there." E > 0 on the whole grid.

**Honest verdict on 9b.** The bridge carries traffic: the complete
classical argument — Dirichlet series, trig positivity, pole/zero
singularity structure — is now expressible in the sieve's language, and
the energy reading makes the contradiction *visible* (termwise
nonnegativity versus a required negative divergence) in a way the bare
trig identity hides. What the translation does NOT do: it does not
eliminate the analysis. The singularity structure (residue −m at a
zero) is an analytic fact about Dirichlet series that the complex
*houses* but does not *derive*. So: same traffic, new bridge, one
genuinely new visible feature — no new theorem yet. 9c (stronger
positivity → a new zero-free region) remains the real test.

*Direction noted for 9c (speculative):* the mechanism is
deformation-agnostic — for any residue pattern with |R_p| ≥ 0 the
deformed log-derivative keeps positive coefficients — so the space of
sieve deformations may parametrize the space of admissible positive
trig polynomials used in modern zero-free regions. Undeveloped.

## D9. 9c: the bridge's load limits (principled boundaries + viable core)

**1. The D8 seed, killed — with evidence.** The speculation was that
sieve deformations parametrize new positivity for constraining zeros.
Test on the twin deformation: ζ_R(s) = ∏_p(1−|R_p|p^{−s})^{−1},
F = −ζ_R′/ζ_R = Σ_p|R_p|(log p)/(p^s−|R_p|), coefficients ≥ 0, so the
3-4-1 machine transports (verified: min S = 3F(σ)+4ReF(σ+it)+ReF(σ+2it)
> 0 on a t-grid, `deformation_kill.py`). But:
  (a) ζ_R is an Euler product ⟹ zero-free for Re(s) > 1 — exact, since
      |R_p|p^{−σ} < 1 means no factor vanishes. The zero-exclusion
      machine runs with *nothing to exclude*.
  (b) The pole only gets heavier: F(σ) ~ 2/(σ−1) (verified with tail
      correction: 19.33 vs 20.00 at σ = 1.1), making the inequality
      *easier* to satisfy, not stronger.
Deformations repackage the pole; they create no new zero-detector.
Seed killed — it was ours, and the evidence killed it.

**2. Positivity is blind left of the line.** The Dirichlet-series
positivity Σ_nΛ(n)n^{−σ}P(t log n) ≥ 0 converges only for σ > 1.
Everything left of Re(s) = 1 comes from analytic input: the zero's own
partial-fraction term 1/(s−ρ) and bounds on ζ′/ζ. Structural fact: any
argument using only (Λ ≥ 0 plus the pole at s = 1) can *at most*
recover ζ(1+it) ≠ 0 — the inputs do not even define the objects left
of the line. The crossing is done by analysis. Honest division of
labor: geometry owns the positivity inputs, analysis owns the
continuation and bounds.

**3. The parity barrier.** Pure sieve/combinatorial positivity cannot
resolve the parity of ω(n) (Selberg) — so *some* oscillatory/analytic
input is necessary, not optional. 9c-via-pure-positivity was blocked by
theorem, not by lack of trying.

**4. The literature has saturated the polynomial optimization.**
Mossinghoff–Trudgian–Yang (2022, arXiv:2212.06867): σ ≥ 1−1/(5.558691
log|t|) via a degree-16 optimized nonnegative trig polynomial — "the
trigonometric-polynomial method is near its intrinsic limit."
Bellotti–Trudgian–Yang (2026): 1/(4.896 log|t|). "Better polynomials
from geometry" as an *improvement* avenue is essentially closed, by the
experts' own assessment.

**5. The viable core — what survives.** (a) The sieve *produces* the
positivity inputs geometrically: every charge pattern q on residues
gives P(θ) = |Q(e^{iθ})|² ≥ 0 by autocorrelation,
a_d = 2Σ_jq_jq_{j+d} (d ≥ 1), with a clean exclusion criterion —
a₁ > a₀ kills simple line zeros (from a₀−a₁m ≥ 0 forcing m < 1).
Exhibited: q=(1,1) → 2+2cosθ, a₁/a₀ = 1, too weak (the classical fact);
q=(1,2,1) → 6+8cosθ+2cos2θ = 2×(3-4-1), excludes; q=(1,1,1) →
3+4cosθ+2cos2θ, a₁/a₀ = 4/3, excludes — the *unweighted* 3-block works;
q=(1,0,1) (twin residues {0,2}) → a₁ = 0, blind; q=(1,3,3,1) →
a₁/a₀ = 3/2, stronger. So the family the literature optimizes over has
a residue-pattern interpretation — the sieve *explains* the positivity
inputs even where it cannot *improve* them. (b) Open computable
question (9c′): do the saturated degree-16 optimizers have
small-support autocorrelation structure? Unknown — the literature's
are black-box (simulated annealing/SDP).

**Verdict on 9c.** 9c-as-"prove RH by stronger positivity" is closed:
blocked by (2)+(3)+(4) — principled limits, not difficulty. What
remains is 9c′ (the explanatory autocorrelation program) and the
hybrid division of labor as the bridge's true shape. The "almost" is
now a *measured* almost: we know exactly how far the bridge goes, what
it carries, and what must carry the rest.

Honest labels: the deformation kill is exact (Euler-product
zero-freeness) + computationally verified (pole order, transport);
blindness-left-of-line is structural (exact reasoning about the
inputs); parity barrier and saturation are cited literature;
the autocorrelation family is exact identities; 9c′ is open.

## D10a-step1 — The explicit formula, grounded in our objects (2026-09-30)

**Status: computationally verified.** Script: `explicit_formula.py`.

**Statement (classical, exact theorem — Davenport):** for x > 1 not a prime power,
ψ(x) = x − Σ_ρ x^ρ/ρ − log(2π) − ½log(1−x^{−2}),
sum over nontrivial zeros ρ, symmetric pairing ρ ↔ ρ̄.

**What we did:** ψ(x) computed from the sieve itself (prime-power sum —
*exactly* the D1 face-sum, no independent ψ routine). Zeros from mpmath
(first 400, γ ≤ 679.7). Truncated sum
S_T(x) = x − 2Re Σ_{0<γ≤T} x^ρ/ρ − log(2π) − ½log(1−x^{−2}).

**Result:** max |ψ − S_T| over x ∈ [20.5, 200.5] (half-integers avoid jumps):
T=50 → 4.55; T=100 → 2.46; T=200 → 1.95; T=400 → 1.36. Decreasing in T,
well inside the O(x log²x/T) truncation bound. Pointwise oscillation
match, e.g. x=100.5: ψ−x = −6.4547 vs zero-sum −6.5852.

**Interpretation (exact translation of D1):** the error term
E(x) = ψ(x) − x = −Σ_ρ x^ρ/ρ − log(2π) − …
is *made of zeros*. D4's "beachhead #2" is now concrete: the zeta zeros
are the regulators of the infinite face-sum. The face-sum knows the
primes; the zeros know the face-sum's error. This is the joint both
abutments share.

**Thesis toward Weil (programmatic/heuristic):** Weil's positivity
W(f∗f̃) ≥ 0 ⟺ RH. Via the explicit formula, W of a test function is a
*weighted integral of E(x) = ψ(x) − x* plus archimedean terms. Since ψ
is our face-sum (D1), Weil's positivity becomes **a positivity
constraint on the incidence complex's face-sum error**. That is the
span's shape. Next: implement W(f∗f̃) via the arithmetic (prime-power)
side for concrete f — the translation's first computable instance.

## D10a-step2 — Weil's formula as prime-side positivity (2026-09-30)

**Status: computationally verified.** Script: `weil_positivity.py`
(bug note: first run had prime powers grouped by prime with an early
break, silently dropping p ≥ 3 contributions; caught by the a=0.1
mismatch, fixed by sorting + full summation — the verification below
is from the corrected run).

**Formula (symmetric Guinand–Weil; normalization confirmed by our own
numerics, not trusted from the source):** for even test h with
g(u) = (1/2π)∫h(r)e^{−iru}dr,
Σ_ρ h(γ_ρ) = h(i/2)+h(−i/2) + (1/2π)∫h(r)[Re dig(1/4+ir/2)−logπ]dr
             − 2Σ_{n≥2} Λ(n)n^{−1/2}g(log n).
Test family: h_a(r) = e^{−ar²} = |e^{−ar²/2}|² — a *square*.

**Verification (zero side vs prime side, 60 zeros, 26152 prime powers):**

| a    | Σ_ρ h(γ_ρ)      | W(h) prime-side   | \|diff\| |
|------|-----------------|-------------------|----------|
| 0.02 | 3.708258e-02    | 3.708258e-02      | 2.4e-16  |
| 0.10 | 4.209600e-09    | 4.209600e-09      | 2.2e-17  |
| 0.50 | 8.262e-44       | 5.3e-15 (noise)   | 5.3e-15  |

Machine-precision agreement in all three regimes, including the
delicate a=0.5 cancellation (pole+arch−primesum = 0 to 15 digits).

**Positivity exhibited with no zeros used:** W(h_a) ≥ 0 in all cases,
computed purely from prime powers + digamma integral + pole terms.

**Derived structural finding (ours):** prime-side positivity is *not*
termwise — it is a cancellation. Components for a=0.5:
pole 2.266297 + archimedean (−1.196347) − prime drain 1.069950 ≈ 0.
The archimedean background is *negative* and nearly cancels the pole;
the prime-power sum eats the remainder. This *refines* the step-1
thesis: the span's positivity is subtler than D8's manifest termwise
kind — on the zero side it is termwise (Σ_ρ|H(γ_ρ)|² ≥ 0 under RH), on
the prime side it is a global balance. The bridge *is* the formula
equating them.

**Dictionary (translation, exact):** Weil's square h = |H|² ⟷ our
autocorrelation square P(θ) = |Q(e^{iθ})|² (D9). Same generative move:
squares manufacture positivity. The prime sum −2ΣΛ(n)n^{−1/2}g(log n)
is a *weighted vertex-tower sum* — our native objects carrying Weil's
functional.

**Honesty boundary:** Weil's criterion — W(h) ≥ 0 for all admissible
square-type h ⟺ RH (Weil 1952; Bombieri 2000 exposition) — is *cited*,
not derived. What we derived: the prime-side presentation, its
cancellatory structure, and the square dictionary. Translation ≠ proof;
the positivity must come from the geometry independently (or the
argument is circular).

**Forward pointer (10a-step3):** optimize over H — the Weil analogue
of the degree-16 polynomial optimization (D9): which square test
function maximizes the positivity's constraining power?

## D10a-step3 — the prime-side zero detector; resolution priced by uncertainty (2026-09-30)

**Status: computationally verified.** Script: `weil_detector.py`.

**Construction (exact):** detector bump at height T0, width w,
h(r) = e^{-(r-T0)^2/2w^2} + e^{-(r+T0)^2/2w^2} (sum of squares, >=0,
peak 1, even), with exact Fourier partner
g(u) = w*sqrt(2/pi) * e^{-w^2 u^2/2} * cos(T0*u).
Derived bound (h >= 0 + Weil formula): with B+ = [T0-w, T0+w],
N+(B+) <= e^{1/2} * W(h), W(h) computed prime-side.

**Verification (W prime-side vs zero-side, 80 zeros, 1.27M prime powers to 2e7):**

| T0  | w   | W'     | N+ | bound | leakage |
|-----|-----|--------|----|-------|---------|
| 50  | 2.0 | 3.8861 | 2  | 6.41  | 0.6827  |
| 50  | 1.0 | 2.2472 | 1  | 3.71  | 0.2977  |
| 50  | 0.5 | 1.8062 | 1  | 2.98  | 0.0007  |
| 100 | 2.0 | 3.9959 | 2  | 6.59  | 0.7001  |
| 100 | 1.0 | 1.8518 | 0  | 3.05  | 1.8518  |

Agreement 4e-16 (8e-13 at w=0.5). Primes alone count zeros in a
window: the bridge working as an instrument.

**Resonance mechanism (components, T0=50):**
w=1.0: pole 0 + arch +1.6548 - (prime-sum -0.5925) = 2.2472.
w=0.5: pole 0 + arch +0.8274 - (prime-sum -0.9788) = 1.8062.
When a zero sits in the window, the oscillatory prime sum goes
*negative* and adds to W -- the primes "ring" at the zero's
frequency. Window empty (T0=100, w=1, zeros at 98.83/101.32 just
outside): prime-sum +0.3562, W all leakage. The pole is exactly 0
for detectors (e^{-T0^2/2w^2}); the archimedean term is the positive
background. Honest weak point: the bound is loose when zeros sit at
the window edge -- concentration *relative to actual zero positions*
is what matters.

**Tightest dictionary (exact algebra, derived):**
prime-sum = 2*Cg*Re[ sum_{p,k} (log p) p^{-k(1/2+iT0)} e^{-w^2(k log p)^2/2} ]
i.e. the detector's prime side = 2*Cg*Re[ *windowed* E_1(1/2,T0) ],
our D8 energy E_1 = -zeta'/zeta, Gaussian-windowed in log(p^k),
evaluated at sigma=1/2. The window buys the convergence D8 could not
have at sigma=1/2 (needed sigma>1 unwindowed). Step-2's cancellatory
positivity and D8's termwise positivity are two faces: windowed vs
unwindowed.

**Optimization answer (derived):** the figure of merit is
*concentration* -- leakage 0.68 -> 0.30 -> 0.0007 as w = 2 -> 1 -> 0.5.
The price is the uncertainty principle: envelope e^{-w^2 u^2/2}
reaches 1e-12 at n = e^{7.4/w}: w=2 -> 41, w=1 -> 1700, w=0.5 ->
2.8e6. No finite optimum -- a Pareto frontier. The uncertainty
principle is the bridge's load limit in detector form: sharper
zero-vision costs exponentially more prime data.

**10a complete.** The formula now runs entirely on our objects:
grounded (step 1), positivity structured (step 2), detector built and
priced (step 3). The remaining open span -- an *independent*
Gram/intersection source for the positivity -- belongs to the whole
bridge program (10d its natural home), not to translation.
**Honesty:** the detector bound uses h >= 0 at the zeros, i.e. gamma
real -- certified numerically per-window here (agreement to 1e-15 *is*
the certificate), not proved in general. Weil's criterion cited.

## D10b — Li's criterion through the D1 face-sum (2026-09-30)

**Status: computationally verified (Parts A-D); structural verdict derived.**
Script: `li_criterion.py` (bug note: zero-side sums initially missed the
rho<->rhobar doubling; caught by the n=1 mismatch, fixed).

**Criterion (cited, Li 1997):** RH <=> lambda_n >= 0 for all n >= 1,
lambda_n = sum_rho [1 - (1-1/rho)^n].

**Part A -- Keiper-Taylor (exact, no zeros):** lambda_n = n[z^n]log xi(1/(1-z)),
via L(w) = log xi(1+w) series (Stieltjes numbers to k=40, polygamma at 1/2,
formal log + composition with w = z/(1-z)). n = 1..40: all lambda_n >= 0
(min 0.0230957 at n=1). lambda_1 = 0.0230957090, lambda_2 = 0.0923457352
(match known values). lambda_n/(n log n) = 0.067, 0.063, 0.072, 0.099,
0.146, 0.182, 0.207 (n = 2..40) -- rising toward the known (1/2)n log n
asymptote.

**Part B -- zero side:** 2Re sum_{0<gamma<=319}[1-(1-1/rho)^n] (150 zeros)
vs Taylor: n=1: 0.020642 vs 0.023096; n=10: 2.034 vs 2.279; n=30: 16.35
vs 18.55. Residual = high-zero tail; tail estimated by the zero-density
integral matches every observed gap to 3 s.f. (n=30: est 2.21, obs 2.21).
Fully reconciled -- the bridge carries traffic.

**Part C -- S_1 is archimedean (structural):** sum_{|gamma|<=319} 1/rho
-> 0.0230957 = 1 + gamma/2 - (1/2)log(4pi). Its proof uses only the
functional equation: S_1 = xi'(1)/xi(1) = [1 from s(s-1)] + [gamma from
zeta's Laurent] + [-(1/2)log pi - log 2 from Gamma]. The prime Dirichlet
series sum Lambda(n)n^{-s} *diverges* at s=1 -- it never appears as a
convergent sum. **S_1 admits no convergent prime-sum presentation; its
value is fixed by archimedean constants.**

**Part D -- obstruction generalized:** A_k(X,eps) = sum_{n<=X}
Lambda(n)(log n)^k n^{-1-eps} grows as eps^{-k-1}: k=0: 7.45 -> 10.50
(eps 0.10 -> 0.05); k=1: 30.7 -> 47.7; k=2: 98.0 -> 156.2 -- tracking
k!/eps^{k+1} up to X-truncation. The Lambda-sums that "want" to be
lambda_n's coefficients *diverge*; lambda_n needs their finite parts
(eta_k / Stieltjes constants). Renormalization, not direct summation.

**Structural verdict (derived):** lambda_n = sum_{k=1}^n (-1)^{k+1}C(n,k)S_k
is a *coefficient* positivity on the Dirichlet side. The D1 face-sum
reaches it only through renormalized divergent sums. **Weil is
face-sum-native (convergent windowed prime sums, 10a); Li is
Dirichlet-series-native (finite parts of divergent sums).** Formal coda
(heuristic, labeled): lambda_n is Weil-type positivity for the
non-decaying "test function" 1-((rho-1)/rho)^n -- the sharp cutoff is
exactly why its prime side diverges; Li is the inadmissible sharp limit
of Weil.

**10b closed.** Lesson for the bridge program: the face-sum's native
positivity is Weil-type (smoothed/windowed); do not expect it to carry
coefficient-positivity directly. This sharpens the hunt: 10c (Selberg
lambda^2, a genuine quadratic form) and 10d (function-field template)
are where an independent source can live.

## D10c — Selberg's lambda^2 sieve as an optimized quadratic form (2026-09-30)

**Status: exact theorem (optimizer + minimum); computationally verified
(PD, sum-of-squares, classical comparison).** Script: `selberg_form.py`.

**Face-native form.** Squarefree d <-> face S, prod S = d; lcm = prod of
union. On the finite complex Delta_z (primes <= z):
    Q(lam) = sum_{S,T} lam_S lam_T / prod(S union T),   lam_empty = 1.
M_{S,T} = 1/prod(S union T) is positive definite (Cholesky + all
eigenvalues > 0, verified z <= 19; min eig 1.1e-8 at z=19), so
Q(lam) = sum_k w_k (v_k . lam)^2 -- an explicit sum of squares,
Weil-shaped positivity by construction. (Caught+fixed own bug: square
reconstruction must use M's eigendecomposition, not M^{-1}'s.)

**Exact theorem: the optimizer is Mobius.** (M mu)_S
= sum_T mu(T)/prod(S union T). Since prod(S union T) = prod S * prod(T\S),
split T = T1 union T2 with T1 = T cap S, T2 = T\S (disjoint):
    = (1/prod S) [sum_{T1 subset S} mu(T1)] [sum_{T2 cap S = empty} mu(T2)/prod T2].
The first bracket is (1-1)^{|S|} = delta_{S,empty}; the second at S=empty
is prod_{p<=z}(1-1/p) = delta(z). Hence M mu = delta(z) e_empty,
M^{-1} e_empty = mu/delta(z), and with lam_empty = 1:
    lam*_S = mu(S),   Qmin = delta(z) = prod_{p<=z}(1-1/p).
Verified: Qmin/delta(z) = 1 to 12 digits, max|lam*-mu| < 5e-14, z<=19.
The sieve's optimal quadratic form *is* inclusion-exclusion: the Mobius
weights are the energy minimizers, and the minimum recovers the Mertens
product *exactly* (not just asymptotically).

**Classical comparison.** Level-truncated 1/G(z), G(z)=sum_{d<=z}mu^2(d)/phi(d):
1/G(19)=0.2348 vs face-native Qmin=delta(19)=0.1710. The d<=z truncation
is a *constraint*; the full-face optimum is the better (smaller) bound.
Both -> e^{-gamma}/log z asymptotically, but only the face-native form
is exact at finite z.

**Structural verdict (derived).** Selberg's form is the canonical
*optimized quadratic form on the complex*: finite, convergent,
Weil-type (sum of squares) -- consistent with 10b's lesson that the
face-sum carries Weil-type, not Li-type, positivity. But it is an
*upper-bound machine*: PD by construction (positivity assumed, not
discovered from arithmetic), no analytic continuation, no zeros, and the
parity barrier stands -- the same form bounds primes and almost-primes
alike, so no amount of optimization resolves omega(n) parity. 10c gives
the *template* (optimized face-quadratic form, exact optimizer = mu),
not an independent zero-detecting positivity source. That remains 10d.

## D10d — function-field / intersection-pairing template (2026-09-30)

**Status: computationally verified (curve computations); mechanism is
cited classical theorem (Hasse/Weil); template+ledger derived.**
Script: `function_field.py`.

**Part A -- the explicit formula is finite and exact.** E: y^2=x^3+1/F_5:
#E(F_5)=6, #E(F_25)=36, #E(F_125)=126 -- each equals p^n+1-pi^n-pibar^n
*exactly* (|pi|=sqrt(5) verified to 6 digits). E: y^2=x^3+1/F_7:
#E(F_7)=12, #E(F_49)=48, exact. Zeta numerator roots |t|=1/sqrt(p)
(RH for the curve) verified. Contrast 10a-step3: the number-field
explicit formula is infinite and needs windowing (Pareto frontier
n ~ e^{7.4/w}); the function-field formula needs no window -- the prime
side is a *finite* point count.

**Part B -- RH as discriminant of a counting-born PSD form.**
Frobenius eigenvalues pi,pibar=(a_p +/- sqrt(a_p^2-4p))/2. The degree
quadratic form Q(m,n) = deg(m*phi+n) = p m^2 + a_p m n + n^2 is PSD
*because degree counts kernel points* (deg >= 0). PSD <=> discriminant
a_p^2-4p <= 0 <=> |a_p| <= 2 sqrt(p) <=> |pi|=sqrt(p) (Hasse = RH).
Verified: discriminants -20 (F_5), -12 (F_7); Q >= 0 on grid.
Counting anchors exhibited: deg(1-phi) = #E(F_p) = 6, 12 (counted);
deg(1+phi) = #twist(F_p) = 6, 4 (counted) = p+1+a_p. The positivity
source is *counting* -- the same kind as Lambda >= 0 (D7/D9).

**Part C -- template: anatomy of an independent Weil-positivity source.**
(i) Geometric space with torus: the Jacobian J(C), a complex torus.
(ii) Correspondence/operator: Frobenius, eigenvalues pi_i.
(iii) Counting-born PSD form: deg >= 0 -> discriminant condition.
(iv) Zeros as eigenvalues; RH as the discriminant inequality.
(v) Finite exact explicit formula (no truncation).

**Ledger for the number-field / face-complex analogue.**
HAVE: counting positivity (Lambda >= 0, D7/D9 -- same kind as deg>=0);
finite PD quadratic forms on faces (10c); an explicit formula (10a --
but infinite, windowed). MISSING: a space playing the Jacobian's role
(Delta_infty is contractible, D4 -- topologically trivial, so the
object must live in weights/operators, not the bare space); a
Frobenius-like operator with the zeros as eigenvalues; an intersection
pairing tying zeros to the counting positivity. The torus in the RH
story is the Jacobian -- this answers the toroidal question: plane for
zeta's domain, torus for the geometric explainer.

**Structural verdict (derived).** The template locates the gap
precisely: the missing object is *operator-theoretic* (a "Frobenius for
Delta"), not another positivity inequality. 10a-10c assembled
positivity inputs (Weil-type smoothed, Selberg-type optimized,
primitive counting); 10d shows what would have to *use* them: a space +
operator + counting-PSD form with zeros as eigenvalues. This reframes
the hunt and closes the systematic pass: 10e audits the supporting
analytic tools.

## D10e — supporting tools: mean-value, large sieve, uncertainty (2026-09-30)

**Status: computationally verified (1-3); zero-density role audited.**
Script: `supporting_tools.py`. P(t) = sum_{n<=N0} a_n n^{it},
a_n = Lambda(n)/sqrt(n), N0 = 50000 (5217 prime powers, S2 = 56.99).

**1. Montgomery-Vaughan mean value -- verified on our polynomial.**
(1/2H) int_{T0-H}^{T0+H} |P|^2 / S2 at T0 = 20000:
H=200: 0.9948; H=1000: 0.9789; H=5000: 0.9596; H=20000: 1.0073.
Converges to 1 -- the mean-square amplifier is real on the detector's
prime-side polynomial. This is what converts pointwise window counts
into L^2 bounds.

**2. Large sieve -- verified.** sum_{r<=R}|P(t0+r delta)|^2 <= (N0+delta^-1)S2:
delta=1: ratio 0.0041; delta=0.5: ratio 0.0080. Holds with headroom
(the bound is crude for this polynomial, as expected).

**3. Uncertainty principle -- quantified.** Window width w needs prime
data n = e^{7.433/w} (10a-step3 envelope): w=2 -> 41; w=1 -> 1.7e3;
w=0.5 -> 2.9e6; w=0.25 -> 8.2e12; w=0.1 -> 1.9e32. At T0=100 (mean zero
spacing 2.27): w=1 resolves 0.44 spacings, w=0.5 resolves 0.22 -- but
isolating single zeros cleanly (w=0.25) needs 8e12 primes: infeasible.
This is the fundamental wall of the prime-side detector, and the sharp
contrast with the function-field finite exact formula (10d), which
needs no window at all.

**Zero-density audit (role, not a new estimate).** Our detector bound
N_+([T0-w,T0+w]) <= e^{1/2} W(h) used RH to interpret windows as
critical-line zero counts. Unconditionally, off-line zeros pollute
windows; zero-density estimates N(sigma,T) bound how many can stray --
they are the tool that would make the detector program unconditional.
Classical estimates cited, not re-derived; the plug-in point is precise.

**Structural verdict (derived).** 10e's tools are analytic *amplifiers*,
not independent positivity sources: they strengthen what the bridge
says (mean-square control, unconditional leakage bounds) but add no new
positivity and change nothing in the 10d ledger. The systematic bridge
pass 10a-10e is complete.

## Node 14 — face-weights: obstruction, identity, differentiated residues
(2026-09-30; D4's positive-region half. Status: exact theorem +
exact obstruction + refined construction.)

**Setup.** Face-weights w(S) = (-1)^{|S|+1} log(prod S)/(prod S) on
subsets S of primes <= z (D4). Finite-z total W(z) = sum_{S} w(S).

**Obstruction (exact).** No *ordinary* positive geometry (AHBL sense:
canonical form with logarithmic poles, residues +-1 on boundary
strata, +-1 at 0-dimensional strata) can carry w(S) as its stratum
residues. Proof: residues of logarithmic forms are quantized; a
0-dimensional stratum residue is +-1 or 0. But |w({2})| = (log 2)/2
= 0.3466 not in {0,1}. The *signs* (-1)^{|S|+1} are compatible with
residue alternation; the *magnitudes* log(prod S)/(prod S) are
impossible. So D4's "no positive region found" is explained, not
merely observed: the literal question has a negative answer, by
theorem. (Loophole named: *weighted* positive geometries allow
general residues; the construction below is the natural such
weighting, so the obstruction is really "the ordinary notion is
insufficient; the deformed notion is the home.")

**Identity (exact theorem).** For F_z(u) = prod_{p<=z}(1 - p^{-u})
(entire in u, finite product):
  d/du F_z(u) |_{u=1} = sum_{S subset P_z} w(S)
                     = delta(z) * sum_{p<=z} (log p)/(p-1),
where delta(z) = prod_{p<=z}(1-1/p).
*Proof 1 (subset expansion):* F_z(u) = sum_S (-1)^{|S|} (prod S)^{-u};
d/du = sum_S (-1)^{|S|}(-log prod S)(prod S)^{-u}; at u=1 this is
sum_S (-1)^{|S|+1} log(prod S)/(prod S) = sum_S w(S). Then
sum_S w(S) = sum_j (log p_j/p_j) prod_{i!=j}(1-1/p_i)
= delta(z) sum_j (log p_j)/(p_j-1), by writing
(log prod S)/(prod S) = sum_{j in S} (log p_j/p_j)
prod_{i in S, i!=j}(1/p_i) and summing over S containing j.
*Proof 2 (calculus):* F_z'/F_z = sum_p (p^{-u} log p)/(1-p^{-u)};
at u=1: F_z'(1) = F_z(1) sum_p (log p)/(p-1) = delta(z) sum_p
(log p)/(p-1). Verified numerically to 10 digits at
z = 2..29 (face_weights.py); the identity computes the 2^{pi(z)}
subset sum in O(pi(z)) operations.
*Asymptotic:* W(z) -> e^{-gamma} = 0.56146 as z->infty, since
delta(z) ~ e^{-gamma}/log z and sum_{p<=z}(log p)/(p-1) ~ log z
(Mertens). Numerics: 0.4780 (z=29), 0.5153 (z=10^3),
0.5333 (z=10^5), climbing to 0.5615. (Distinct from D4's
sum_{prod S <= X} w(S) -> 1: different regularization -- all
subsets of P_z here vs product-bounded there.)

**K-theoretic home.** In H^*_{S^1}(pt; R) = R[u], let
E_z = (+)L_p over p<=z with equivariant Chern roots -u*log p
(real coefficients legitimate). Then
ch(lambda_{-1}(E_z)) = prod_p (1 - e^{u*log p *(-1)})
= prod_p (1 - p^{-u}) = F_z(u),
the equivariant K-theoretic Euler class. The face-weights are
F_z'(1): the *u-derivative at u=1* of the equivariant Euler class
-- differentiated residues. Only the primes are input (as Chern
roots); the subset combinatorics, the signs, and the log
magnitudes are all computed.

**Refined positive region.** Positive region: the simplex
Delta^{m-1} (m = pi(z)), the face complex's geometric home, with
its ordinary canonical form Omega (residues +-1). *Stringy*
deformation: I(u) = int_{Delta} (prod_p x_p^{-u log p}) Omega
(Dirichlet integral = [prod_p Gamma(-u log p)...] ratio; exponents
are the prime logs). Differentiating at u=1 produces exactly
sum_S w(S) as generalized residues. This is Figueiredo's
*deformations* move (D6) as the mechanism: her deformations are
what produce non-+-1 generalized residues; here the deformation
parameter is u and the exponents are the prime logs. The bare
simplex is contractible (D4); the arithmetic lives in the
deformation, i.e., in the weights -- exactly D4's conclusion,
now with the obstruction explained and the refined object named.
