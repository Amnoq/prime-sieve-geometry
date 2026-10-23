# COMPLETE MAP — Prime-Sieve Geometry Research Arc
**Date:** 2026-09-30
**Purpose:** every thread, every node, every open question — the entire
territory in one document. Epistemic labels throughout.

---

## I. FOUNDATIONS (closed)

### D1 — Simplicial sieve (2026-09-29) — CLOSED
**Claim:** the sieve IS the simplicial complex Δ_z (finite prime
subsets = faces = squarefree products); φ(x,a) is face-sum Möbius
inversion; primality = absence of shared-boundary relation.
**Label:** exact theorem (reframing of classical inclusion–exclusion).
**Prior art:** framing appears new (searched 2026-09-30); the underlying
math is classical.

### D2 — Territory/relational reading (2026-09-29) — CLOSED
**Claim:** n prime ⟺ no shared-boundary relation to earlier prime
territory; composites = overlaps. User's relational metaphysics as
machine.
**Label:** exact (definitional reframing).

### D3 — Standing methodology — CLOSED
Numbered decision tree + epistemic labels as standard practice.

### D4 — N→∞ limit (2026-09-29) — CLOSED (two halves)
- **Bare complex:** Δ_∞ is the contractible infinite simplex —
  topologically trivial. Positive geometry must live in the WEIGHTS.
  [exact]
- **Face-weights:** w(S)=(−1)^{|S|+1}log(∏S)/∏S; Σ_{∏S≤X}w(S)→1
  (PNT reframed as "the weighted infinite simplex has total weight 1").
  Verified 0.999922 at 5·10⁵. Dirichlet GF = −ζ′/ζ². [computationally
  verified; the identity is exact]
- **Prior art:** no prior art found for the "total weight 1" framing.

### D5 — Figueiredo steer (2026-09-29) — CLOSED
Take her GENERATIVE insights (process), never copy implementation.
Territory removal = her "soft limit/splitting". Applied throughout.

### D6 — Deformation → twin constant (2026-09-29) — CLOSED (algebra)
**Move:** deform marking rule R_p={0}→{0,−2} (p odd). Deformed
survivors ARE the twin prime lowers (verified ≤200000, 2160 of them).
Renormalized weight 𝔖(z)=∏(1−|R_p|/p)/(1−1/p)² → 2C₂=1.32032.
**Label:** exact (the derivation); the twin conjecture itself remains
UNPROVEN (ratio 1.6091 at 2·10⁵).
**Prior art:** the constant is classical; the generative deformation
move appears new (searched 2026-09-30).

---

## II. POSITIVITY HUNT (closed, with one negative theorem)

### D7/D9 — Positivity located (2026-09-30) — CLOSED
- **9a:** positivity lives in primitive objects (−ζ′/ζ=ΣΛ(n)n^{−s},
  Λ≥0; δ(z)>0; 3-4-1). [exact]
- **9b:** bridge carries traffic — full 3-4-1 as nonnegative stratum
  energies. [computationally verified identity]
- **9c:** CLOSED NEGATIVE *by theorem* — positivity is blind left of
  Re(s)=1; geometry owns positivity, analysis owns continuation.
- **9c′:** CLOSED NEGATIVE — saturated degree-16 optimizers have no
  small-support structure (all 32 Fejér–Riesz factors fully dense).
  Saturation is numerical, not geometric. [computationally verified]

### D10 — Bridge program (2026-09-30) — COMPLETE
- **10a:** explicit formula grounded in our objects; prime-side zero
  detector built. [computationally verified]
- **10b:** Li's criterion CLOSED as face-sum-incompatible; Weil's
  positivity is face-sum-native. [exact/conceptual]
- **10c:** EXACT THEOREM — Selberg's λ² form on Δ_z minimized at
  λ*=μ, minimum δ(z).
- **10d:** function-field template CLOSED (formulated, not simulated).
- **10e:** supporting tools CLOSED (MVT, large sieve, uncertainty wall).
- **Verdict:** face-sum carries three verified positivity kinds; none
  zero-detecting. Missing object is operator-theoretic.

---

## III. OPERATOR HUNT (open — the live frontier)

### Node 11 — operator hunt (2026-09-30) — OPEN
- **11a:** Berry–Keating xp probe — smooth law captured, fluctuations
  not. [conjectural]
- **11b:** s↦1−s̄ symmetry — CORRECTED (not a Möbius band; claim
  withdrawn). ξ-invariance verified to 3.77e-16. [exact]
- **11d:** Möbius-band Laplacian — valid topology, no arithmetic
  mechanism. Topology alone insufficient. [computationally verified]
- **11f:** CCM — THE LIVE CANDIDATE (see below).
- **11z:** 3/4 phase derived exactly — Kirchhoff matrix in the standard
  convention (R=1 circle check), vertex⊕Dirichlet partition, Dirichlet
  tone +1/π, full-rose tone +1/4π, subtraction −3/(4π) anti-phased
  exactly; 2-bond eigenvalues +1/−3/4 make the ladder
  R_m=(9/16)[m/(m+1)]² theorem, not measurement. [exact]
- **11aa:** tone program COMPLETE (2026-10-17) — rung 3 detected
  (ladder three deep), 3/4 exact, dynamical-zeta road blocked
  (entropy mismatch, obstruction named). No open thread remains
  from the tone program.

### Node 11f — CCM (2026-09-30) — computationally verified, conceptually bridged
- Independent reimplementation from arXiv:2511.22755; zeros 1–8
  recovered from primes alone (zero1 exact to float64 at c=13,N=20).
- Controls: zeros AND positivity require exact prime input (A/B/C all
  negative).
- N=120: ε_even=3.48e-59, separation 8771× (monotone 581→3744→8771).
- Failure modes: fragile, not robust — exact-arithmetic reporter.
  Drop p=2/3 destroys; drop p=5 survives. Small primes dominate.
- **Conceptual bridge (2026-09-30):** Λ = μ ∗ log (EXACT) — CCM's fuel
  is one Dirichlet convolution from face-sum-native μ. The machine is
  borrowed; the fuel refines to your weights. [exact theorem]
- **Open:** full Frobenius-like operator question; Node 11 stays OPEN.

### Node 12 — multi-torus (2026-09-30) — CLOSED
Weyl's law kills L1–L3; Heisenberg nilmanifold probe NEGATIVE
(65,401 eigenvalues); surviving form = Deninger's foliated dynamical
system [conjectural, formulated not simulated].

---

## IV. SIDE CHAMBERS (closed)

### Node 13 — fermionic Fock fork (2026-09-30)
- **Exact identification:** Δ_z faces = fermionic Fock basis, μ=(−1)^F.
  [exact] — BUT: independent prior art exists (goldenphysicsproject);
  the identification is NOT unique to this work.
- **H_2 (one-body):** KILLED BY INSPECTION (integrable).
- **H_int (density-density):** NEGATIVE — Poisson-like bulk.
- **13d (pair hopping):** POSITIVE — GUE-like at all z≥17, all λ;
  strengthened to z=41 (dim 8192), ⟨r⟩=0.528. [computationally
  verified] Caveat: shuffled weights also GUE (generic two-body
  chaos) — content is arithmetic weights COMPATIBLE with chaos.
- **13e (prime-frequency probe):** NEGATIVE — operator does not HEAR
  the primes. 13d = universality result, not bridge plank.
- **Our distinct contribution:** the spectral program (no prior art);
  the identification itself is shared.

### Node 14 — positive-region home (2026-09-30) — CLOSED
- **14a OBSTRUCTION (exact):** no ORDINARY positive geometry can carry
  w(S) as stratum residues (|w({2})|=(log2)/2≈0.347 ≠ ±1).
- **14b IDENTITY (exact):** d/du[∏(1−p^{−u})]_{u=1}=Σ_S w(S).
- **14c REFINED HOME:** equivariant Chern roots −u·log p; face-weights
  = differentiated residues; Figueiredo's deformations as mechanism.
  Closes the D4↔D6 loop.

---

## V. FAILURES LEDGER (the favorite part)

Rigorously documented, each with mechanism:
1. **D10 imported resonance↔zero** (not derived) — guardrail from archive.
2. **D11 Prime Zipper Law** — falsified at (1129,1151)→21.
3. **D12 rh_final compactification** — inserts answer by hand.
4. **D13 coset-sum numerology** ≠ Chebyshev mechanism.
5. **9c as RH proof** — closed negative BY THEOREM (positivity blind
   left of Re 1).
6. **9c′ small-support hope** — saturated optimizers fully dense.
7. **11b Möbius-band quotient** — corrected, claim withdrawn.
8. **12a–12c Laplacian multi-torus** — killed by Weyl's law.
9. **12d Heisenberg** — negative on three panels.
10. **13 H_2** — killed by inspection (integrable).
11. **13 H_int** — Poisson, not GUE.
12. **13e prime hearing** — operator is deaf to primes.
13. **CCM robustness** — fragile exact-arithmetic reporter, not a
    stable gap; noise destroys it.
14. **z=43 Lanczos** — timed out (1500s); nice-to-have, not rerun.

---

## VI. OPEN QUESTIONS (what remains)

1. **Node 7 (paper):** outline drafted; awaiting user approval on
   title/scope + prior-art re-search before public novelty claims.
2. **Node 8 (RH bridge):** heuristic, open by nature — the bridge now
   has three verified positivity kinds + one live operator candidate
   (CCM) + one exact fuel dictionary (Λ=μ∗log).
3. **Node 11 (operator):** CCM is the live candidate; the full
   Frobenius-like operator question remains open at the conceptual
   level.
4. **Node 13 fork:** stays open via 13d (universality result); the
   bridge-relevant question (an operator that HEARS primes) is
   unanswered — 13e was negative.
5. **Physical build:** tetrahedral sieve (z=7) + layered territory wall
   — fabrication files not yet created; library time not yet confirmed.

---

## VII. NOVELTY BOUNDARIES (prior-art search 2026-09-30)

| Claim | Status |
|---|---|
| Simplicial-sieve framing (Δ_z) | Appears new (framing); math classical |
| PNT as "weighted simplex, total weight 1" | Appears new (statement) |
| Deformation → 2C₂ (generative move) | Appears new (move); constant classical |
| Fock-over-primes identification | SHARED — independent prior art exists |
| Fock spectral program (13d/13e) | Appears new |
| CCM reimplementation | Independent verification of published work |
| Λ = μ∗log bridge dictionary | Exact theorem; the identity is classical, the *use* as dictionary is ours |

**Rule:** no public novelty claim without re-search. The paper is an
expository/synthesis vehicle, not a breakthrough claim.
