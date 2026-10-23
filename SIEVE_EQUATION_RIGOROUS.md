# The Sieve Equation: Rigorous Kernel

*Built 2026-10-11 at his direction ("make an airtight rigorous equation
using the sieve that shows the exact same thing"). Honest verdict first:
the marking theorem below is airtight and proved. The tones are
computationally verified prior work (Node 11l), not re-derived here.
The bridge equation — the relational explicit formula — is stated as a
labeled target, not derived. What is open is marked open; nothing is
dressed as rigor that isn't.*

---

## 1. The marking theorem (airtight)

**Definitions** (relational sieve terms).

- Let P_{<n} be the set of primes less than n.
- For each prime p, its *territory* is T(p) = { m : p divides m, m > p }
  — the multiples of p, excluding p itself.
- The *relational profile* of n is Rel(n) = { p ∈ P_{<n} : n ∈ T(p) } —
  the earlier primes whose territory contains n. For composite n,
  Rel(n) is *everything that went into making it*, mapped first-class.
- Let 0 denote the undifferentiated ground, to which every position is
  trivially related (the background relation). Define
  Rel*(n) = Rel(n) ∪ {0}.

**Theorem.** For n > 1: Rel*(n) = {0} ⟺ n is prime.
Equivalently: Rel(n) = ∅ ⟺ n is prime.

*Proof.* (⇒) If n is prime, no prime p < n divides n, so no earlier
prime's territory contains n; Rel(n) = ∅, hence Rel*(n) = {0}.
(⇐) If Rel(n) = ∅, suppose n composite: n = ab with 1 < a ≤ b < n.
By the fundamental theorem of arithmetic, a has a prime divisor p;
then p ≤ a < n and p divides n, so p ∈ Rel(n) — contradiction.
Therefore n is prime. ∎

**Notes.**
- The rule never predicates primality. It never asks "is n prime?"
  It asks only: does any earlier prime's territory contain n? The
  marking is a discovery of the relational situation.
- Nothing is eliminated. Every n — prime or composite — is mapped to
  its relational profile. Composites keep their full makeup as
  first-class data; this is the 2026-10-11 correction built into the
  formalism.
- The n > 1 condition is not a technicality: it is his deposition
  (2026-10-11) that the numbers start with two. 1 is the unit, not a
  number in the sequence; 0 is the ground, not in the sequence. The
  theorem's domain *is* the numbers as he defined them.
- The mathematics here is ancient (Eratosthenes). The novelty is the
  *form*: stated purely relationally, with the {0}-reconciliation
  proving that tonight's "the only thing to relate to is zero" is
  *equivalent* to primality — not a restatement of it, but the same
  content in relational form. Status: **exact theorem**.

## 2. The tones (verified prior work, not re-derived)

- Node 11l: the orbit→tone mechanism — tones measured from prime
  orbits on the Kirchhoff rose graph. Computationally verified
  (with the 11o scan-step correction absorbed).
- These are the *derived zetas*: relationally earned from the orbits,
  not posited. Status: **computationally verified**.
- In the mapped equation, Σ_ρ (x^ρ/ρ) translates to these tones
  stripped of inserted form (continuation, summation convention,
  Hadamard product).

## 3. The target: the relational explicit formula (OPEN)

What "the exact same thing" would look like as construction rather
than equation. Stated as target with labels — *not derived*:

    #{ n ≤ x : Rel*(n) = {0} }  ←→  tone-sum over the derived zetas
         (marked count)                (orbit-measured tones)

- Left side: **rigorous** (the marking theorem counts it exactly).
- Right side tones: **verified** (11l).
- The bridge (←→): **OPEN**. Proving the equality between the marked
  count and the tone sum *is* the node-to-node construction — the
  Circle Sieve as relational bridge of constructions. This is the open
  work, precisely located.
- The 0.5: **heuristic**. The balance point seen from the two
  orderings; the conjecture that the derived tones stand there is
  tonight's live derivation, not a theorem.

## 4. What this establishes — and what it doesn't

**Establishes (airtight):** "Primes are the point where zero is the
only thing to relate to" is a theorem, not a metaphor. Rel*(n) = {0}
⟺ n prime, proved from the relational definitions with composites
preserved first-class throughout. Tonight's central insight now has
rigorous form.

**Does not establish:** the prime–zero bridge as equation. The
explicit formula's *content* (distribution controlled by tones) is
not derived here — only its *terms* are sorted into derived vs.
inserted, and the bridge is located exactly. The construction
remains open work, and the document marks it as such rather than
performing it.

*Status: working document, 2026-10-11. §1 exact theorem (proved);
§2 computationally verified (prior work, Node 11l); §3 open target
(labeled, not derived). No insertion: what is open is marked open.*
