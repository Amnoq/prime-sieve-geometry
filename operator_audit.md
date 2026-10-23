# Operator-candidate audit (Node 11c) — 2026-09-30

Literature survey of Hilbert–Pólya-type operator proposals, each scored on the
8-point checklist. Epistemic labels per standing practice.
Guardrail shorthand: D10 = bridge imported not derived; D12 = engineered
weights deleting spectrum; D2 = error bars; D8 = computational medium limits.

## A. Connes adele-class trace formula (1999)
**Sources:** Connes, arXiv:math/9811068 (Selecta Math. 1999); essay arXiv:1509.05576.

1. **State space:** Adele class space X_ℚ = 𝔸_ℚ/ℚ^× (noncommutative bad quotient);
   Hilbert space L²(X) with the idele-class scaling flow.
2. **Operator:** Infinitesimal generator of the scaling flow (Dirac-type in the
   spectral triple); traces of test-function operators against the flow.
3. **Zeros:** NOT eigenvalues — **absorption spectrum** (missing lines cut from a
   continuum); off-critical zeros would be resonances. Explains the minus sign
   in the explicit formula. [exact theorem, conditional on trace formula]
4. **Trace formula DERIVED?** Yes in the **semilocal** case (finitely many places)
   [exact theorem]. The full adelic statement is *equivalent* to RH — the
   derivation is conditional on the thing sought.
5. **Positivity source:** Weil's explicit-formula distribution W(h) ≥ 0.
6. **Counting-born or RH-equivalent?** RH-EQUIVALENT BY CONSTRUCTION. Weil proved
   RH ⟺ positivity of W. Connes rehouses the equivalence in a noncommutative
   space; the positivity is not independently derived from counting. This is the
   D10-shaped move at the highest level of sophistication.
7. **Sieve/face connection:** YES — the semilocal cutoff (finite place set S) is a
   place-filtration; adding places one at a time parallels our z-filtration Δ_z.
   Geometric side = sum over places p ∈ S with prime terms = face-sum over the
   place set. Limit S → all places ≈ z → ∞.
8. **Guardrails:** D10 (reformulation, not derivation — the hard direction is Weil
   positivity = RH itself); D12 (absorption "deletes" lines from a continuum —
   the continuum regularization must be audited, though Connes is explicit about
   it); D8 (no finite computational model of the adele class space; only
   finite-place truncations are computable — which is exactly candidate B).
**Verdict: LIVE as framework / KILLED as proof.** Deepest existing reformulation;
the missing piece (Weil positivity) is exactly RH. Gold-standard template: any
future operator must reproduce this trace formula.

## B. Connes–Consani–Moscovici zeta spectral triples / prolate / zeta cycles (2021–2025)
**Sources:** arXiv:2106.01715 (zeta cycles, first 31 zeros from spectral side);
arXiv:2006.13771 (Weil positivity, archimedean place only); arXiv:2412.06605
(prolate wave operators); arXiv:2511.22755 (Zeta Spectral Triples, Nov 2025).

1. **State space:** L² of circle length L = 2 log S (zeta cycles); interval
   [λ⁻¹, λ] with the scaling operator's spectral triple; prolate spheroidal wave
   functions (Sonin space) as UV component.
2. **Operator:** D_log^{(λ,N)} — **self-adjoint** rank-one perturbations of the
   scaling spectral triple; perturbation vector from small eigenvectors of the
   Weil quadratic form restricted to test functions of support ≤ S, using only
   Euler factors at p ≤ x = λ². Self-adjointness via Carathéodory–Fejér/Toeplitz
   extension theory.
3. **Zeros:** Claimed as genuine discrete EIGENVALUES of a self-adjoint operator —
   the only candidate attempting the literal Hilbert–Pólya statement with
   self-adjointness proved. Numerical coincidence "with striking accuracy" even
   for small x; convergence as N, λ → ∞ unproved ("a strategy toward a proof").
4. **Trace formula DERIVED?** Half: operator built from primes alone (forward),
   but the eigenvalue↔zero identification is numerical, not derived.
5. **Positivity source:** Self-adjointness of D_log (genuine, by construction)
   forces real spectrum. Reported: approximating values from primes ≤ 13 provably
   on the critical line, matching first 50 zeros to 2.6e-55…1e-3 [secondary
   source — GitHub summary of Connes, J. Open Math. Probl. Apr 2026; treat the
   exact figures as unverified until the primary is read].
6. **Counting-born or RH-equivalent?** MIXED. Input is prime Euler products only
   (counting-born, forward); but "limit = the zeros" is numerical. Self-adjointness
   buys "spectrum is real," not "spectrum is the zeros" — identification remains
   conjectural.
7. **Sieve/face connection:** STRONG — construction filtered by x (primes p ≤ x);
   x → ∞ is a sieve-limit; Weil form restricted to support ≤ S is a finite
   face-sum object. Closest any literature candidate comes to our filtration
   language.
8. **Guardrails:** D10 — survives forward (primes in, spectrum out) but
   zero-identification is numerical; D2 — "striking numerical accuracy" needs
   quantified error bars; D12 — audit the rank-one perturbation direction:
   prime-derived (Weil form eigenvectors — principled) vs zero-fitted is THE
   question for replication; D8 — fully computable: finite matrices from prime
   Euler products.
**Verdict: LIVE — top computational target.** Reimplement D_log^{(λ,N)}
independently from prime Euler products; verify spectral coincidence; audit the
perturbation for zero-fitting; quantify convergence error bars.

## C. Bost–Connes system (1995) + Julia (1990) precursor
**Sources:** Bost–Connes 1995; Planat–Solé–Omar, hal-00549030 (2010/2011).

1. **State space:** Hecke C*-algebra of ℚ-lattices up to scale; GNS space ℓ²(ℕ).
2. **Operator:** H|n⟩ = (log n)|n⟩; partition function Z(β) = Tr e^{−βH} = ζ(β);
   KMS phase transition at β = 1 (unique KMS state for β ≤ 1, Galois-indexed
   extremal states for β > 1).
3. **Zeros:** ABSENT — spectrum is {log n}; no eigenvalues, no resonances. The
   pole of ζ at β = 1 appears as the phase transition. Disqualified as a
   zero-operator at the gate.
4. **Trace formula:** n/a — no spectral side with zeros.
5. **Positivity source:** Gibbs weights n^{−β}/ζ(β) — genuinely counting-born
   (thermal equilibrium over integers).
6. **Counting-born, yes — but it counts integers and produces the POLE, not the
   zeros.** Thermodynamic positivity, unrelated to RH. (Planat et al. restate RH
   as a KMS phase-operator inequality — RH-equivalent by construction, a D10 move
   layered on top.)
7. **Sieve/face connection:** Notable but misdirected — φ_β(q) built on primorials
   N_q with Möbius-weighted sums (a prime-filtration object), filtering toward
   class field theory (β→∞ states ↔ Gal(ℚ^ab/ℚ)), not zeros.
8. **Guardrails:** Fails at the gate (no zeros in the machine); D10 applies to the
   Planat reformulation.
**Verdict: KILLED as zero-operator.** Survives as the canonical "ζ from counting"
machine (gets the pole right) — sharpens the question of what machine gets the
zeros.

## D. Deninger foliated dynamical cohomology program (1990s–present)
**Sources:** Deninger ICM/program papers; Morishita, arXiv:2508.15971 (relation to
Connes–Consani adelic spaces); arXiv:2410.20758 (regularized determinant formula
for 3D Riemannian foliated dynamical systems — Deninger's conjectured formula,
PROVED in the dynamical setting, 2024).

1. **State space:** Conjectural — foliated space (3D in the dynamical picture)
   with a flow φ^t ("arithmetic site"); rational Witt space constructions exist
   as fragments.
2. **Operator:** Θ, infinitesimal generator of the flow on conjectural leafwise
   cohomology H¹; ζ(s) = det_reg(s − Θ|H¹).
3. **Zeros:** Conjectural eigenvalues of Θ; off-line zeros = non-real eigenvalues.
4. **Trace formula:** The explicit formula is the TARGET — it would become a
   Lefschetz trace formula (primes = closed orbits of length log p, matching
   Guinand–Weil prime-power terms). Not derived for Spec ℤ; the space is missing.
   The 2024 theorem proves the template in the dynamical world.
5. **Positivity source:** Would-be Hodge/index positivity on the conjectural
   cohomology (analogue of Weil's intersection pairing). Does not exist yet.
6. **RH-equivalent by aspiration** — explicitly modeled on Weil's function-field
   proof; positivity imported from the template (D10-shaped), not from counting.
7. **Sieve/face connection:** Closed orbits ARE the primes (lengths log p) — the
   dynamical analogue of our face inventory; finite-orbit truncation (length ≤
   log z) is a sieve-like cutoff. But the orbit list is put in, not derived from
   a sieve process.
8. **Guardrails:** D8 — space doesn't exist, no direct computation; bounded
   heuristic possible (concrete 3D flow with orbit lengths ≈ {log p}, numerical
   Ruelle zeta — labeled model-of-template); D10 — imports Weil's architecture.
**Verdict: CONJECTURAL-ONLY as theory** (missing space = the whole problem).
Deserves a BOUNDED heuristic computation only: prototype prime-orbit flow +
numerical Ruelle zeta, never presented as evidence about ζ.

## E. Ruelle transfer operator for the "prime dynamical system"
**Sources:** Mayer transfer operator / Selberg zeta (arXiv:1008.4229) as the
working template.

1.–8. **Does not exist independently.** Transfer operators (Mayer's L_s,
   det(1±L_s) identities) work where a hyperbolic dynamical system exists. For
   the Riemann zeta, "the dynamical system with prime periodic orbits" IS
   Deninger's missing space (candidate D) — no dynamics, no transfer operator.
   Type-error firewall: "prime orbit" (primitive periodic orbit) ≠ rational
   prime; proposals sliding between the senses equivocate.
**Verdict: KILLED as independent candidate — reduces to D.** The Selberg/Mayer
case stands as the control: the one world where the full dream works (trace
formula derived, zeros = Laplacian eigenvalues, positivity geometric) = our
already-closed D10d function-field template.

## F. Sierra xp-regularizations
**Sources:** Sierra–Townsend, arXiv:0805.4079 (Connes absorption = lowest Landau
level limit); Sierra, arXiv:0712.0705 (boundary functions → fluctuation term);
Rindler/Majorana xp-class variants (e.g. arXiv:2503.09644).

1. **State space:** Planar charged particle (E = V₀xy + uniform B); lowest Landau
   level; or 1+1D Rindler/Majorana spinor spaces.
2. **Operator:** Landau Hamiltonian; xp-class Hermitian
   H = √x p̂ √x + a⁻²√x p̂⁻¹√x with domain choices for self-adjointness.
3. **Zeros:** NOT eigenvalues. Models reproduce the SMOOTH counting function N̄(E)
   only (Connes absorption as LLL limit); higher Landau levels "suggested" for
   fluctuations — heuristic. Same ceiling as our 11a (Berry–Keating as formulated).
   The 2025 Rindler/Majorana zero-eigenvalue claims tune the quantization
   condition to ζ — D10-flavored.
4. **Trace formula:** No.
5. **Positivity source:** Ordinary QM spectral positivity (Landau levels) —
   genuine and independent, but counts Landau states → N̄(E), not zeros.
6. **Genuine positivity, irrelevant to RH** (zeros not in spectrum).
7. **Sieve/face connection:** None — input is the smooth N̄(E).
**Verdict: KILLED as zero-operators** (smooth-count ceiling). The Landau-limit
unification of BK and Connes regularizations is elegant physics; background only.

## G. Bender–Brody–Müller PT-symmetric operator (2017)
**Sources:** Bender–Brody–Müller, PRL 2017; Bellissard criticism; Wikipedia
Hilbert–Pólya survey.

1. **State space:** L²(ℝ), PT-symmetric (pseudo-Hermitian).
2. **Operator:** Ĥ = (1−e^{−ip̂})⁻¹(x̂p̂+p̂x̂)(1−e^{−ip̂}).
3. **Zeros:** Claimed eigenvalues via eigenfunctions ψ_z(x) = −ζ(z, x+1) (Hurwitz
   zeta) — **the answer inserted by hand** (D10 textbook case).
4. **Trace formula:** No.  5. **Positivity:** PT-symmetry does not guarantee real
   eigenvalues; self-adjointness unproved, criticized by Bellissard.
6. **The "positivity" is the unproved claim itself.** Fails our self-adjointness
   requirement at face value.
7. **Sieve/face connection:** None.
**Verdict: KILLED** — answer inserted by hand, reality of spectrum unproved, not
self-adjoint.

## H. Wu–Sprung inverse potential (1990s)
**Sources:** Wu–Sprung 1990s; Jaksch, arXiv:2510.16759 (2025).

1. **State space:** L²(ℝ), 1D Schrödinger.  2. **Operator:** −d²/dx² + V(x), V
   reconstructed numerically from the first 500 zeros.
3. **Zeros:** Eigenvalues BY CONSTRUCTION — zeros are the input. Purest D10
   violation on the list.  4.–6. n/a — inverse problem always succeeds, teaches
   nothing. Jaksch (2025) explains the famous fractal D≈1.5 as an artifact of
   the Riemann–von Mangoldt approximation error — the "fractal" was error
   signal.
7. **Sieve/face connection:** None.
**Verdict: KILLED — with the kill now self-explaining** (fractal = approximation
error). Canonical warning: any "operator from zeros" fit must pass the
forward-direction test (primes in, spectrum out).

## Ranked shortlist

**Deserves our own computation (forward, prime-input only):**
1. **B (zeta spectral triples)** — reimplement D_log^{(λ,N)} from prime Euler
   products alone; verify spectral coincidence; audit perturbation for
   zero-fitting vs prime-derivation; quantify convergence (D2). Only candidate
   that is self-adjoint by construction + prime-input-only + numerically
   zero-matching + finite/computable.
2. **D (heuristic prototype)** — bounded: concrete 3D flow with closed-orbit
   lengths ≈ {log p : p ≤ z}, numerical Ruelle zeta, test for zero-like
   structure. Labeled model-of-template from the start.

**Conjectural-only (read, don't compute):**
3. A (Connes 1999 general trace formula) — gold-standard reformulation; missing
   Weil positivity IS RH.
4. D (full program) — missing space is the whole problem.

**Killed (documented):** C (no zeros in machine); E (reduces to D); F
(smooth-count ceiling); G (answer inserted, not self-adjoint); H (inverse
tautology; fractal explained as error artifact).

**Control (template that works):** Selberg zeta via Mayer transfer operator —
already closed as D10d; existence proof the dream is coherent in the hyperbolic
world.
