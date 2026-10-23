# Interference Theorem — Rose Graph, Two Sectors

**Date:** 2026-10-06
**Status:** theorem note — statement with epistemic labels per part.
**Question answered:** why the merged 11l spectrum shows r=2 > r=1 —
predicted from sector phases alone, before any z-score is computed.
**Companion:** `tone_hierarchy_investigation.md` (the measurements).

---

## Statement

Let the Kirchhoff rose graph have loop lengths L_j (j = 1..R). Its
spectrum splits into a vertex sector (roots of the secular equation)
and a Dirichlet sector (exact picket fences k = 2πm/L_j). At tone
frequency f_{p,r} = r·log p / 2π, let the two sectors contribute
complex Fourier amplitudes C_v(p,r), C_d(p,r) to the oscillatory
level density. Then the merged amplitude is C_v + C_d, and the
hierarchy between odd and even repetitions is fixed by the sector
phases as follows.

**(a) [Exact.]** The Dirichlet sector contributes with
r-independent phase. Its levels are picket fences; N_osc is a
sawtooth whose r-th harmonic has the same phase at every r
(classical Fourier series of the sawtooth; in the probe convention
the measured value is +π/2). No numerics needed — the phase-locking
across harmonics is deterministic.

**(b) [Derived — exact theorem (Node 16, 2026-10-06).]** The
vertex sector's phase alternates with repetition number: −π/2 at odd
r, +π/2 at even r. Derivation: the vertex roots are exactly the
zeros of F(k)=Σ_j tan(kL_j/2) (Lemma 1 — cos-zeros are not G-zeros
by irrationality of log p_i/log p_m); F's poles at π(2m+1)/L_j are
simple, distinct, and interlace the roots one per interval
(Lemmas 2–3); the pole counting function N_poles=Σ_j⌊(kL_j/π+1)/2⌋
Fourier-expands with a (−1)^n from the half-period offset (poles at
*odd* multiples vs Dirichlet levels at *even* multiples), giving
C_v^pole(p,r)=i(−1)^r/(πr) by unique factorization (Lemma 4). The
half-period offset is the analytic origin — Node 15's "sieve's 0.5
was there first," in spectral form. *Correction to the earlier
expectation:* the route is the secular-equation pole structure, NOT
powers of the vertex scattering factor (the periodic-orbit
amplitude (1/R)^r is decisively not the origin). Open sub-step: the
dither anti-alignment (δ−δ̄ Fourier coefficient anti-aligned with
the pole tone, ~25% magnitude) is computationally verified, not
derived — but it is collinear, so arg(C_v)=arg(C_v^pole) exactly,
which is why the measured alignment is ±1.00. Full derivation:
node16_lemma_derivation.md; validation:
node16_scripts/validate_pole_derivation.py.

**(c) [Exact, given (a) and (b).]** Write C_d = |C_d|e^{iφ_d} with φ_d
r-independent, and C_v = |C_v|e^{iφ_v(r)} with φ_v(r+1) = φ_v(r) + π.
Then |C_v + C_d| is minimized when φ_v = φ_d + π (odd r —
destructive interference) and maximized when φ_v = φ_d (even r —
constructive interference), by elementary complex arithmetic.
Hence: **odd-repetition tones are suppressed and even-repetition
tones enhanced in the merged spectrum, for any loop lengths,**
before a single z-score is computed. The winner (r=2) is determined
by the phases alone.

---

## Corollary (predictive)

For any Kirchhoff rose graph — prime-log loops, random loops, any
lengths — the merged-spectrum tone hierarchy inverts the vertex
hierarchy: repetitions with even r are enhanced, odd r suppressed,
relative to the vertex sector alone. The 11n random-loop control is
consistent (merged r=1 below Dirichlet-alone).

**Status 2026-10-06 (Node 11q): computationally verified at the
amplitude level.** Measured on the 11l spectrum: (2,3) and (3,3)
align −0.98/−0.99 (destructive), (2,4) and (3,4) align +1.00
(constructive); |Cm(2,4)|=0.0525 > |Cm(2,3)|=0.0297 and
|Cm(3,4)|=0.0544 > |Cm(3,3)|=0.0252, additivity to 4e-4. The
r=3/r=4 alignment pattern is a second independent witness for the
phase-alternation law (b). The z-score probe itself cannot resolve
r=3/r=4 (merged z 0.78/1.15 inside control background) — a probe
sensitivity limit, not a refutation; amplitude-level analysis is
required above r=2. The vertex-hierarchy leg at r≥3 is inconclusive
(mixed amplitudes; composite-orbit contributions).

## Honest boundaries

- The theorem predicts the *pattern* (odd suppressed / even
  enhanced), not numerical z-scores.
- Part (b) is now derived (Node 16, exact theorem for the
  pole-sum part); the remaining open sub-step is the dither
  anti-alignment (computationally verified, not derived) — narrow
  and precisely located, and it does not affect the phase
  conclusion.
- The Lomb-Scargle probe is unreliable on pure picket fences
  (detrending reduces them to numerical noise); the theorem is
  stated for exact Fourier amplitudes, not probe z-scores, and the
  probe numbers are corroboration, not the proof.
- Node 11q (2026-10-06) mapped the probe's high-r limit: at r=3/r=4
  the merged z-scores (0.78/1.15) sit inside control background —
  the probe is blind above r=2 and amplitude-level analysis is
  required there. This is a sensitivity limit, not a refutation.
- This resolves the 11p puzzle (why r=2 > r=1 in the merged 11l
  spectrum) but does not change 11p's gate verdict: the letter's
  gate concerns the merged spectrum, where r=1 remains absent.

---

*Filed 2026-10-06. Node 16 derived part (b) — the theorem is whole
for the phase pattern; the dither sub-lemma remains the precise
open sub-step.*
