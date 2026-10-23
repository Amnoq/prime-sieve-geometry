# Parity jurisdiction for the deformed sieve R_p={0,−2}

**Date:** 2026-10-11. **Question** (open since 2026-10-09): what does parity
mean for the deformation? Does Selberg's parity barrier apply?
**Verdict:** resolved by separation — walked below.

## 1. What the parity barrier says [known theorem — classical]

Sieve methods work from **sifting data**: counts of integers satisfying
congruence conditions mod d (d composed of small primes). Selberg's
parity phenomenon: this data **cannot distinguish integers with an odd
number of prime factors from those with an even number**. Consequence:
**no lower bound** for primes — or twin primes, or any set defined by
Ω-conditions — **can be proved from sifting data alone**. The barrier
is about the *information* (sifting data), not about any particular
weighting scheme. It is the reason sieve theory alone cannot prove the
twin prime conjecture, and why Zhang/Maynard had to import
non-sieve input (equidistribution, bilinear forms).

## 2. The deformed sieve's logical form [walked here; computationally verified]

Static deformed sieve: S(x,z) = #{n≤x : ∀p≤z, n mod p ∉ R_p},
R_p={0} (p=2), {0,p−2} (p odd). Exact inclusion–exclusion:

  S(x,z) = Σ_{d|P(z)} μ(d)·E_d(x),   μ(d) = (−1)^ω(d)

E_d(x) = #{n≤x : ∀p|d, n mod p ∈ R_p}. Verified live (x=20000, z=13):
direct marking S=989, μ-sum S=989, exact match. The ω-parity
alternation is visible in the raw sums: ω-even terms +61823,
ω-odd terms −60834, net 989. **The μ(d)=(−1)^ω(d) structure is
identical to the classical sieve; only R_p differs.**

## 3. The two "twos" — disambiguation [exact, walked]

|R_p|=2 (two marked residues per prime) is the sieve's **dimension**
(κ=2) — it sets local densities and the singular series. The
"parity" in *parity barrier* is **ω(d) parity in μ(d)** and **Ω(n)
parity in targets** — a different "two" entirely. Conflating them
is an error; the walk separates them. The deformation changes the
first two; the barrier lives in the second.

## 4. Jurisdiction verdict [derived]

**(a) Lower bounds / infinitude from sifting data: the barrier
APPLIES, unchanged.** The twin target needs Ω(n)=Ω(n+2)=1 —
maximally parity-sensitive. The deformed sifting data {E_d} has the
identical μ-logic as the classical case (§2). The deformation
changes dimension and densities, not parity-blindness. Any attempt
to prove infinitely many twin lowers *from sifting data alone*
hits the same wall as the classical twin sieve.

**(b) Exact generative computation: the question is misplaced.**
D6's verified achievement — survivors ARE the twin lowers, exact,
to 10⁶ — is finite exact computation, not a lower-bound proof.
Parity governs proofs of infinitude, not exact sifting. D6 never
attempted infinitude via sifting; the barrier was never in its way.

**(c) Singular-series derivation: parity-irrelevant.** 2C₂ as the
renormalized total weight is heuristic algebra about the main
term — a *prediction* for the constant, not a lower bound. The
barrier doesn't govern it.

**Resolution:** the "untested jurisdiction" dissolves by separation.
The barrier has full jurisdiction over what D6 *didn't* attempt
(infinitude via sifting) and no jurisdiction over what D6 *did*
(exact survivors, derived constants). There is no escape via the
deformation — and none was needed, because the deformation never
entered the barrier's territory.

## 5. Where the walk stops [honest boundary]

- A fully rigorous Selberg-style parity-flip construction adapted
  to R_p={0,−2} is **not constructed here** — not needed: the
  verdict follows from structural identity with the classical case
  (§2), and the barrier itself is a known classical theorem.
- What infinitude would require: **non-sieve input**
  (Elliott–Halberstam-type equidistribution, bilinear forms — the
  Zhang/Maynard route). The deformation doesn't supply these;
  nothing in the walk suggests it could.
- This does **not** diminish D6: the exact-survivor machine and the
  derived 2C₂ stand, in territory parity never governed.

## 6. Backward touch

- D6's "capture perfectly" recollection (2026-10-09): confirmed
  decomposed — **structure captured** (exact survivors, derived
  constant — done, verified); **infinitude open** — and parity now
  explains *why* it's hard: not a defect of the deformation but
  the universal obstruction. The open question is closed as a
  question; it remains open as a problem, same as classical.
- deformation_kill.py (zero-detector): untouched, still dead.
- Novelty: no literature check needed for this verdict — it leans
  on the classical barrier, not on a novelty claim.

**Epistemic summary:** barrier = known theorem; μ-identity =
computationally verified (live); two-twos separation = exact;
jurisdiction verdict = derived from walked hypotheses.
