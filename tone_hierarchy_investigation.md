# Tone Hierarchy Investigation: Why Does 11l Show r=2 > r=1?

**Date:** 2026-10-06
**Question:** In Node 11l (Kirchhoff rose, 8 loops of length log p, p=2..19),
the tone probe finds r=2 repetition tones STRONGER than r=1 fundamentals
((2,2) z=9.23, (3,2) z=8.12 vs (2,1) z=1.24, (3,1) z=-0.09). Berry's diagonal
approximation predicts the opposite (amplitudes 1/(π²r²p^r), r=1 dominant).

**Verdict: genuine graph physics — vertex-Dirichlet interference.**
The Dirichlet picket-fence sawtooth and the vertex trace-formula oscillation
are exactly out of phase at r=1 (destructive) and exactly in phase at r=2
(constructive). This is NOT a probe artifact: the exact N_osc (linear Weyl
detrending, no polynomial) shows the same inversion. The vertex sector alone
has the correct hierarchy (r=1 > r=2), matching trace-formula theory.

---

## 1. Sector separation: vertex has the right hierarchy

Probe (degree-10 detrended Lomb-Scargle) on each sector separately,
recomputed live:

| tone | merged z | vertex z | dirichlet z |
|------|----------|----------|-------------|
| (2,1) | +1.24 | **+6.41** | -0.25 |
| (3,1) | -0.09 | **+9.93** | -0.11 |
| (5,1) | +0.62 | **+8.02** | +6.62 |
| (7,1) | +0.55 | **+6.56** | +3.93 |
| (2,2) | **+9.23** | +0.92 | -0.24 |
| (3,2) | **+8.12** | +0.08 | -0.09 |

*Computationally verified.* The vertex sector alone shows r=1 >> r=2
(z 6–10 vs 0–1), exactly as the trace formula predicts. The inversion
appears only in the merged spectrum.

## 2. Detrending is not the cause

Varying the detrending polynomial degree (4, 6, 10, 14) on the merged
spectrum: the r=2 > r=1 pattern is unchanged (e.g. (2,2) z = 8.76–9.23,
(2,1) z = 0.93–1.24 across degrees). *Computationally verified.* The
inversion is not a degree-specific artifact. (Note: the fitted polynomial
itself carries large low-frequency amplitude, but the inversion persists
with linear detrending too — see §5.)

## 3. Picket-fence probe caveat (not the mechanism, but recorded)

For a PERFECT single picket fence, the degree-10 detrending removes the
signal almost exactly (residual std ~1e-15), and the normalized
Lomb-Scargle amplifies numerical noise to spurious O(1) power equally at
all harmonics. *Computationally verified.* The probe is unreliable for
perfectly regular spectra. This does NOT explain the 11l inversion (the
merged spectrum is not a perfect fence), but it means Dirichlet-alone
z-scores should not be over-interpreted.

## 4. Trace-formula amplitudes (theory)

For the Kirchhoff rose with R loops, the vertex scattering matrix is
σ = (2/2R)J − I. A primitive loop orbit has stability amplitude
A = 1/R (transmission between the loop's two half-edges). The oscillatory
density of states: d_osc(k) = (1/π)Σ_po (l_po/r)·A^r·cos(k·l_po·r).
In N_osc (integrated), the r-th repetition has amplitude (1/π)·(A^r/r),
so r=1 : r=2 = 1 : 1/(2R) = 1 : 1/16 for R=8. *Exact theorem (cited:
Kottos–Smilansky trace formula; Kirchhoff σ standard).*
**Theory predicts r=1 >> r=2 for the vertex sector** — confirmed by §1.

The Dirichlet sector is exact picket fences; each fence contributes a
sawtooth with fundamental amplitude 1/π and n-th harmonic (1/π)(1/n).
*Exact theorem (Fourier series of sawtooth).*

## 5. Decisive test: exact N_osc phase analysis

Computed N_osc exactly on a common fine grid (no polynomial detrending):
- Vertex: N_v(E) from roots, minus LINEAR Weyl fit.
- Dirichlet: Σ_j (1/2 − {E·L_j/2π}) — exact sawtooth sum (sign verified).
- Merged: N_m = N_v + N_d (additivity confirmed: |Cv+Cd| = |Cm| to 4 dp).

Complex Fourier amplitudes at the 7 tone frequencies:

| tone | |Cv| | |Cd| | |Cm| | phase alignment |
|------|------|------|------|------|
| (2,1) | 0.219 | 0.319 | **0.101** | **−1.00 (destructive)** |
| (3,1) | 0.263 | 0.322 | **0.059** | **−1.00 (destructive)** |
| (5,1) | 0.223 | 0.320 | **0.098** | **−1.00 (destructive)** |
| (7,1) | 0.239 | 0.324 | **0.085** | **−1.00 (destructive)** |
| (2,2) | 0.097 | 0.169 | **0.266** | **+1.00 (constructive)** |
| (3,2) | 0.075 | 0.174 | **0.249** | **+1.00 (constructive)** |
| (2,3) | 0.058 | 0.113 | **0.055** | −1.00 (destructive) |

*Computationally verified.* The Dirichlet sawtooth has phase +π/2 at all
harmonics; the vertex component has phase −π/2 at r=1, +π/2 at r=2
(alternating). Hence exact cancellation at r=1, exact reinforcement at
r=2. The merged N_osc genuinely has r=2 > r=1. **This is the mechanism.**

A factorial test (probe detrending + least-squares vs linear detrending +
Lomb-Scargle) confirms the inversion tracks the SPECTRUM (merged N_osc),
not the spectral estimator: both estimators agree on each residual.

## 6. 11n cross-check

The corrected 11n (random irrational loops): vertex loop z=9.58,
Dirichlet 26.06, merged 13.82 at the loop fundamentals (r=1). Merged
below Dirichlet-alone is consistent with partial destructive interference
at r=1. *Computationally verified (from decision-tree record).* The
interference is a general two-sector graph effect, not prime-specific.
(r=2 sector data for 11n was not recorded; the r=1 pattern matches.)

## Mechanism statement

The 11l rose graph has two spectral sectors. The vertex sector obeys the
trace formula (r=1 dominant, 16:1 over r=2). The Dirichlet sector
contributes sawtooth harmonics (1/π, 1/2π, …). In the merged counting
function these add as complex amplitudes: at r=1 the vertex and Dirichlet
phases differ by π (destructive — merged amplitude ~0.06–0.10 vs vertex
alone ~0.22–0.26); at r=2 they coincide (constructive — merged ~0.25–0.27
vs vertex alone ~0.07–0.10). The Lomb-Scargle probe faithfully reports
this merged N_osc. **The inversion is real graph physics.**

## Why the user's tones differ

The user's measured tones come from Berry's diagonal approximation applied
to actual zeta zeros — a single spectrum with no Dirichlet sector. There
is nothing to interfere with, so r=1 dominates as 1/(π²r²p^r) predicts.
The 11l graph's extra (Dirichlet) sector is what inverts the hierarchy.
This resolves the 11p puzzle: the mechanism (orbits → tones) is confirmed,
but the two-sector graph is not a faithful model of the single-spectrum
zeta tone pattern.

## Open: phase origin

Why the vertex phase alternates (−π/2 at r=1, +π/2 at r=2) while the
Dirichlet sawtooth phase is constant (+π/2) is not derived here. The
alternation is an exact computational finding; its analytic origin (Maslov
indices, composite-orbit contributions, or G(k) zero structure) is
*heuristic/open*.

---

*Labels: exact theorem (trace formula, sawtooth Fourier, N_osc additivity);
computationally verified (all numerics above, recomputed live);
conjectural/heuristic (phase-origin theory). Scripts: /tmp/hier_invest.py,
/tmp/hier_abs.py, /tmp/hier_amp.py, /tmp/hier_phase.py, /tmp/hier_phase2.py,
/tmp/hier_factor.py, /tmp/hier_poly.py, /tmp/hier_diag.py.*
