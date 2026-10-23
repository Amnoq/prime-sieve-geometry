# Novel derivations of the circle-sieve program

**Date:** 2026-10-07
**Status:** program documentation. Each entry: the derivation as the
sieve generates it, the classical destination it reaches, exactly
what is novel (the path, never the destination), the epistemic
label, and what would upgrade it.
**Companion:** `DERIVATIONS.md` (D1–D10e, the full sequence);
`../ccc-prototype/corpus_runs/atlas8/DERIVATION_ASSESSMENT.md`
(the Atlas-8 inventory this document expands);
`../ccc-prototype/corpus_runs/atlas8/CRACK_LIST.md` (K8-1…K8-5).

Standing note, from the program's own honesty practice: the
literature proves or stipulates; the sieve *generates*. The
novelty below is in the generative path in every case. Nothing
here is a new theorem about primes.

---

## ND-1. Admissibility derived as sieve output (D6-generalized)

**Epistemic label:** computationally_verified. Predictive test passed.

### The literature's form

Zhang (Theorem 1), Maynard (Prop 4.2 / Theorem 1.2): let
H = {h_1, …, h_k} be an *admissible* tuple — H does not cover all
residue classes modulo any prime p. Admissibility is a *stipulated
input hypothesis*; the theorems conclude infinitely many n with
two (Zhang) or many (Maynard) of the n + h_i simultaneously prime.

### The sieve's derivation

Deform the marking rule per constellation H:

    R_p = { −h mod p : h ∈ H }.

n is marked if n mod p ∈ R_p for some p — i.e., p divides some
n + h_i. The survivors of the deformed sieve are exactly the
n for which all n + h_i are prime: the constellation prime lowers.

**The obstruction, uninserted.** H is inadmissible iff some prime
p covers every residue class mod p through H. Then *every* n is
marked by p — the machine has no survivors. Admissibility is not
hypothesized; it is *computed*:

- Nine constellations (twins, cousins, sexy, two triplet types,
  quad, quint, sext) at x = 10⁶: survivors match independently
  enumerated constellation lowers exactly (twins 8169 = 8169;
  sext 5 = 5); finite-z densities match δ_H to 0.998–1.015;
  𝔖_H(1000) matches the reference singular series to ~0.2%.
- The non-admissible control {0, 2, 4} DIES as the machine
  predicts: exactly one survivor, (3, 5, 7); 𝔖_H(z) = 0 for z ≥ 3.

**Exact algebraic core.** The static z-sieve satisfies the exact
μ-identity S(x,z) = Σ_{d|P(z)} μ(d)·E_d(x) with E_d the exact CRT
residue-class counts (verified exact at (z,x) = (13, 50000) and
(30, 200000)). Faces of the deformed complex carry multiplicities
m(S) = ∏_{p∈S} |R_p| — the number of forbidden CRT classes.

### What is novel

The admissibility *condition* is classical (a covering-set
observation). What is novel is the *derivation*: the condition
emerges as a property of the machine's output rather than being
stipulated as a hypothesis. The literature checks admissibility
by hand before running the theorem; here the sieve runs first
and admissibility is what the survivors exhibit.

### What would upgrade it

A proof (not only computation) that H is admissible ⟺ the
deformed sieve has survivors past the finite-z threshold. The
exact μ-identity core already suggests the shape; the emergence
half is currently computational.

### Sources

- `FRAMEWORK_WHOLE_VIEW_2026-10-05.md` §D6-generalized
- `ktuple_deformation.py` (implementation)
- Atlas-8: `CRACK_LIST.md` K8-2; `verification/verify_k8_2_constellations.py`

---

## ND-2. The twin singular series as renormalized total weight (D6)

**Epistemic label:** computationally_verified (the derivation).
The twin-prime asymptotic itself is explicitly UNCLAIMED.

### The literature's form

Hardy–Littlewood (1923): the twin-prime heuristic constant

    2C₂ = 2 · ∏_{p>2} (1 − 1/(p−1)²) = 1.3203236…,

stated as a constant; the asymptotic π₂(x) ~ 2C₂·x/(log x)² is
conjectural (no k > 1 case of prime k-tuples known).

### The sieve's derivation

Deform R_p = {0} (p = 2), {0, −2} (p odd): n is marked if p | n
or p | (n+2). Markers and survivors separate — the markers are
the primes, the survivors are a different set (verified: the
generative deformed sieve's survivors ≤ 200000 are exactly the
2160 twin-prime lowers, checked against an independent sieve).

Faces carry multiplicities m(S) = ∏_{p∈S} |R_p|; the finite total
weight is exactly δ(z) = ∏_{p≤z} (1 − |R_p|/p), with S(x,z)/x →
δ(z) (verified: 0.071430 vs 0.071429 at z = 7, x = 200000).

Renormalize by the prime baseline:

    δ(z) = [∏_{p≤z}(1 − 1/p)²] · 𝔖(z),
    𝔖(z) = ∏_{p≤z} (1 − |R_p|/p) / (1 − 1/p)².

The first factor → 0 (Mertens); the second converges:

    𝔖(z) → 2C₂ = 1.32032…

verified: 1.367187, 1.344116, 1.330277, 1.322754 at
z = 7, 13, 30, 100 (Atlas-8 re-check: S(1000) = 1.320491).

The constant comes *out of the deformation* — never inserted.

### What is novel

The constant is classical (1923). What is novel is the
generative path: the singular series derived as the renormalized
total weight of a deformed incidence complex, via the exact
deformed μ-identity. Pilot search 2026-09-30: the move appears new.

### Honest boundary

The passage 𝔖(z) → π₂(x) ~ 𝔖·x/(log x)² is the unproven twin
prime conjecture (numerical ratio 1.6091 at 2·10⁵ — slow
convergence, as expected). Verified: the algebra (local factors
assemble to 𝔖). Not claimed: the conjecture. This derivation is
the *mechanism*, not the proof.

### Sources

- `DERIVATIONS.md` §D6; `FRAMEWORK_WHOLE_VIEW_2026-10-05.md` §D6
- `deformed_sieve.py` (implementation)
- Atlas-8: `CRACK_LIST.md` K8-3; `verification/verify_k8_3_singular_series.py`

---

## ND-3. PNT as total weight 1 on the weighted complex (D4)

**Epistemic label:** computationally_verified (the identity).
Framing novel; the underlying mathematics classical.

### The literature's form

The Prime Number Theorem: π(x) ~ x/log x (equivalently
ψ(x) ~ x), proved by Tauberian contour argument
(Hadamard / de la Vallée Poussin; modern expositions e.g.
Zagier/Newman).

### The sieve's derivation

Give each nonempty face S of the incidence complex the
x-independent weight

    w(S) = (−1)^{|S|+1} · log(∏S) / ∏S.

Then D1 reads ψ(x)/x = Σ_{∏S≤x} w(S)·(⌊x/∏S⌋/(x/∏S)), the floor
a cutoff tending to 1, and:

    Σ_{∏S≤X} w(S) → 1   as X → ∞,

i.e. the weighted infinite simplex has total weight 1 — an
identity *equivalent* to PNT. Verified: 0.969931, 1.019210,
1.005585, 0.999922, 0.997215, 1.001658 at
X = 10³, 10⁴, 10⁵, 5·10⁵, 10⁶, 2·10⁶ (Möbius sieve).

The Dirichlet generating function of the weights is

    Σ_S w(S) / ∏S^{s−1} = −ζ′(s)/ζ(s)²,

verified numerically to ~4 digits at s = 1.01…1.20. The *rate*
of convergence S(X) → 1 — the error in the face-sum — is governed
by the zeta zeros (the explicit formula): the zeros enter as
*regulators* of the infinite sum.

### What is novel

Underneath, this is Möbius inversion in face-sum language —
classical mathematics, and the pilot labels it so: "Statement
(classical, reframed)." What is novel is the framing: PNT stated
as a property *of the sieve's native object* (the weighted
complex), with the zeta zeros cast as regulators of its
convergence. That framing is what makes D6 (deformation)
formulable at all — the architecture's value, not a new proof.

### Sources

- `DERIVATIONS.md` §D4 (includes the bare-limit triviality
  argument and the signed-weights resonance/gap discussion)
- Atlas-8: `CRACK_LIST.md` K8-1; `verification/verify_k8_1_pnt_weight.py`
- Node 14 (face-weights: obstruction, identity, differentiated
  residues) for the weight calculus

---

## The pattern

| Derivation | Literature | Sieve | Novelty |
|---|---|---|---|
| ND-1 admissibility | stipulated hypothesis | computed property of output | generative derivation (strongest) |
| ND-2 twin constant | stated heuristic constant | renormalized total weight | generative derivation ("appears new") |
| ND-3 PNT weight-1 | analytic proof | combinatorial identity on the complex | framing (math classical) |

In each case the destination is classical and the path is the
contribution. The program's standing rule holds throughout:
nothing is put in by hand — primality is never tested by a
predicate, admissibility is never stipulated, the constant is
never inserted. What remains, after the machine runs, is the
derivation.
