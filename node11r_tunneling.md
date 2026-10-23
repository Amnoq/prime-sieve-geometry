# Node 11r (probe) — tunneling traversal-sector phase structure

**Date:** 2026-10-06
**Question:** Does the 0/0.5/1 triple's phase structure appear in
quantum tunneling amplitudes — is the double traversal
constructively privileged the way r=2 is in the interference
theorem, or does standard dilute-gas + resurgence exhaust it?
**Status:** adjudicated — see verdict.

## Prediction (stated before computing)

Per the triple artifact's queued thread, the candidate mapping was:
- **0:** perturbation theory (0 traversals) — incomplete/ambiguous.
- **0.5:** the bounce / instanton–anti-instanton pair (2
  traversals, out-and-back) — carrying the imaginary half-phase.
- **1:** the physical answer — real, needing 0+2 combined.
The discriminating test: an even/odd traversal phase pattern in
tunneling amplitudes ANALOGOUS to the interference theorem
(double traversal privileged beyond standard expectations).

## Triadic fork

1. **Claim:** tunneling amplitudes show the even/odd traversal
   phase structure — the triple's third witness, promoting the
   analogy to evidence.
2. **Polar opposite:** standard instanton calculus (dilute gas +
   Bogomolny–Zinn-Justin resurgence) accounts for everything; no
   additional interference pattern exists.
3. **Null:** single harmonic well — no second minimum, no
   traversal structure, no exponential splitting (pipeline sanity).

## Evidence

### A. Anchors (live; pipeline validation)

Exact diagonalization, V=(x²−1)², ℏ∈{0.12,…,0.30}:
- FD grid: convergence checked in L and N (E₀ stable ~10⁻⁵,
  ΔE stable ~10⁻⁷ relative).
- HO-basis (N≤220): E₀ identical to 12 digits across N=100–220
  — high-precision E_mean(ℏ) for scaling fits.
- **Tunnel splitting:** fit log ΔE = −S₀/ℏ + p·logℏ + c₀ over
  8 ℏ values → **S₀,fit = 1.922 vs exact 1.886 (1.9%)**.
  Instanton physics confirmed operating.
  [computationally verified]
- Prefactor power p=0.16 vs 1-loop 0.5 — **inconclusive**:
  2-loop corrections (large coefficient) contaminate at
  accessible ℏ; noted, not forced.
- **Null:** single well V=4(x−1)² → E₀=ℏω/2 exact, ΔE=ℏω,
  no exponential splitting. Pipeline sane.
  [computationally verified]

### B. The 0-sector's expansion (instrument finding)

Rayleigh–Schrödinger around one well (V₁=y⁴+4y³, 30 orders,
basis-convergence verified to 0.00e+00 relative):
- Signs strictly **alternating** to n=30; magnitudes stable
  then factorial — **Borel-summable**, singularity on the
  negative axis (A≈13–18).
- This is the WRONG expansion for the 2S₀ question: the
  2S₀ Borel singularity lives in the ℏ-expansion, not in RS
  around one minimum. Recorded as an instrument finding, not
  a refutation — it maps where the scale does/doesn't live.

### C. Isolating the 2-sector's real fingerprint (three nulls, each moved a level)

1. E_mean − E_pert^opt: swamped by truncation error
   (10⁻³ vs 10⁻⁹ signal). → moved on.
2. E_mean = poly(ℏ) + A·e^{−S/ℏ} fit: polynomial and
   exponential collinear over accessible ℏ; A unstable
   across polynomial degree. → moved on.
3. Padé-Borel of RS series: spurious positive-axis poles in
   [15/15],[14/14]; [14/16] clean but δ doesn't scale as
   e^{−2S₀/ℏ} (S_eff=1.52) — Padé truncation error dominates.
   → stopped: the wall is structural, not technical (see D).

### D. The structural wall (the finding)

The three nulls in C are not independent failures — they are
the Bogomolny–Zinn-Justin point: the 2-sector's real
contribution is **inseparable by theorem** from the 0-sector's
Borel ambiguity (they cancel pairwise). Attempting to isolate
it is attempting what the theory proves ambiguous. The
literature structure (Dunne resurgence notes; Zinn-Justin):
- 1-traversal (instanton): real, ΔE ∼ e^{−S₀} — the splitting.
  [exact theorem]
- 0-sector: non-Borel-summable, c_n ∼ n!/(2S₀)^n, ambiguous
  imaginary part ±i·e^{−2S₀}. [exact theorem]
- 2-traversal (bounce): carries ∓i·e^{−2S₀}; the ambiguities
  cancel; the physical answer is real. [exact theorem, BZJ]
- Even/odd division of labor: odd traversals → off-diagonal
  (splitting); even traversals → diagonal (return amplitude,
  ambiguity cancellation). [exact theorem]

## Verdict

**Third witness CONFIRMED at the level of form; polar opposite
HOLDS for the strong claim.**

- The 0/1/2 traversal structure exists in tunneling with the
  triple's division of labor: 0 ambiguous/incomplete, 1 real
  splitting (exponent verified live), 2 carrying the imaginary
  half-phase that completes 0. The form appears — third
  witness confirmed as form.
- **No additional even/odd interference pattern** was found in
  any real observable beyond dilute-gas + BZJ. Every real
  number checked matches the standard calculus; the
  "constructive privilege" of the double traversal beyond
  standard expectations: NOT FOUND.
- The analogy is therefore real but does not generalize the
  interference theorem and does not promote beyond
  **heuristic** as evidence for the triple as a universal
  principle. The triple's form coincides with known
  resurgence; the interference theorem's specific mechanism
  (two sectors, fixed vs alternating phases) has no tunneling
  analog found here.

## Epistemic labels

- Traversal-sector structure with even/odd division of labor:
  **exact theorem** (standard instanton calculus / resurgence).
- ΔE exponent = −S₀ (1.9%): **computationally verified**.
- Bounce imaginary part ±i·e^{−2S₀} canceling perturbative
  ambiguity: **exact theorem** (Bogomolny–Zinn-Justin).
- No additional pattern in probed real observables:
  **computationally verified** (within probe scope).
- 1-loop prefactor ℏ^{1/2}: **inconclusive** (2-loop
  contamination; not forced).
- Triple-as-universal-principle from tunneling:
  **heuristic** (form matches; no new mechanism).
- Null control: **computationally verified**.

## Branching identifiers

- **Why it ends here:** the discriminating question is
  adjudicated — the form appears (witness at form level) but
  no additional pattern exists in reachable real observables;
  the remaining decisive levels (lateral Borel, false-vacuum
  width) would strengthen the "appearance," not change the
  verdict on "additional pattern." The objective is complete.
- **Its own chain:** (1) false-vacuum decay width as the direct
  physical observable of the bounce's half-phase — queued,
  where the double traversal is the entire decay channel;
  (2) the inseparability finding sharpens future probe design
  — do not attempt to isolate the 2-sector's real
  fingerprint; it is inseparable by theorem; (3) the RS
  summability result maps where the 2S₀ scale does NOT live
  (coupling expansion) — future large-order work must use the
  ℏ-expansion.

## Backward touch (specified; parent's files to edit)

- `triple_artifact_0_5_1.md` — witness 3 status: "confirmed at
  level of form (standard BZJ/resurgence structure); heuristic
  as evidence for universality; no additional pattern found."
- Node 15 — same status update.
- `interference_theorem.md` — no change (probe doesn't bear on
  the graph mechanism).
What changed: witness 3 adjudicated. What didn't: the
interference theorem; the open lemma (b).

## Method self-assessment

- §1 node record: this file (date/question/options/decision/
  evidence/status).
- §2 labels: on every claim above.
- §3 triadic fork: all three legs run — claim (form appears),
  polar opposite (standard exhausts real observables —
  HOLDS), null (single well, clean).
- §4 backward touch: specified above; tree edits left to
  parent (as in 11q).
- §5 branching identifiers: above.
- §6: live computation only (FD + HO diagonalization,
  30-order RS, Padé-Borel — scripts in
  `node11r_scripts/`); nulls treated as instrument findings,
  three levels moved (RS→E_mean fit→Padé-Borel→structural
  wall); controls mandatory (null single well); convergence
  checked (grid, L, basis N, basis-size cross-check on RS);
  honest negatives owned same-exchange (prefactor
  inconclusive; Padé-Borel spurious poles; E_mean fit
  collinearity).
- Deviation: the decisive level for the imaginary part
  itself (lateral Borel sums / false-vacuum width) was
  identified but not executed — recorded as queued, since
  the verdict on the discriminating question does not depend
  on it. A forced attempt would have risked inventing
  precision neither instrument has.
