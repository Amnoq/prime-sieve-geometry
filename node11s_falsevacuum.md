# Node 11s (probe) — false-vacuum decay width: the triple's third witness, second angle

**Date:** 2026-10-06
**Question:** Does the 0/0.5/1 triple appear as an observable pattern in the
false-vacuum decay width Γ, or does standard Coleman dilute-gas + BZJ
resurgence exhaust it?
**Status:** adjudicated — see verdict.

## Prediction (stated before computing, charter §"Prediction")

The polar opposite expected to hold (11r's verdict predicts it): Coleman +
dilute gas + BZJ accounts for everything; no additional traversal-phase
structure in Γ. The probe's value is the honest test.

## Triadic fork

1. **Claim:** Γ shows additional even/odd traversal phase structure beyond
   standard bounce-gas accounting — witness 3 promoted to computationally
   verified observable.
2. **Polar opposite:** standard Coleman dilute-gas bounce (+ BZJ resummation)
   exhausts Γ; no additional pattern exists.
3. **Null:** single well (no false vacuum) — the pipeline must return
   Im E = 0. Pipeline sanity.

## Evidence

### A. Anchors

**Anchor 1 — S_b two-way** [computationally verified]:
V(x;ε)=(x²−1)²−εx, ε∈{0.1,0.2,0.3}. Bounce action by (i) quadrature
S_b=2∫_{xf}^{xtp}√(2(V−V_f))dx and (ii) bounce-profile integral
∫ẋ_b²dτ (independent ODE path). Agreement to 1.4–3.4×10⁻¹⁰ relative.
S_b(0.1)=3.2942195661, S_b(0.2)=2.9185048151, S_b(0.3)=2.5832702673.
(Bounce is out-and-back: S_b→2S₀ as ε→0, verified in the numbers.)

**Anchor 2 — 1-loop prefactor** [inconclusive, honest negative]:
Spectral determinant ratio det'(M_b)/det(M_f) attempted two ways
(direct spectral product with explicit zero-mode projection by ẋ_b
overlap; GY with μ-shift). Both hit the same wall: the finite-interval
zero mode is swamped by O(dt) discretization error (measured: eigenvalue
scales linearly with dt, →0, exact degeneracy artifacts), and T-truncation
breaks the bounce's mode structure (log|R| jumps 10.4 across Tfrac).
At full interval: log|R|≈−12.5±0.5 (N=1000→1600), i.e. K∼800±25% —
order-of-magnitude only. The anchor is NOT cleanly met; the prefactor
enters the fits with this uncertainty owned.

**Anchor 3 — null** [computationally verified]:
Single well via complex-scaled FD: Im E₀=−2.7×10⁻⁵ at N=801, scaling
exactly as dx² → 0 (measured ÷4.00 per doubling; Richardson → 0).
HO-basis null: Im E₀∼10⁻¹⁶ (machine zero). Pipeline sane; the FD
artifact is quantified, not ignored.

### B. Conceptual finding (the probe's sharpest result)

**Charter's (a) as specified is impossible for the confining potential**
[computationally verified]:
Complex scaling (FD + HO basis, two independent instruments) of the
confining quartic double well yields Im E = 0 to machine precision
(HO: −9×10⁻¹⁴ at N=150; the would-be "resonance" converges to a REAL
eigenvalue). There are NO resonances in a confining 1D potential —
the spectrum is purely discrete real. The charter's "(a) Γ_exact from
complex-scaled diagonalization, Im E₀=−Γ/2" assumed a resonance that
does not exist. The bounce's Γ is the width of a resonance that only
exists with an open decay channel. This was discovered by computing,
not assumed — the method working as designed.

### C. The "0" leg — perturbation theory knows nothing of decay

RS around the false vacuum (HO basis, 22 orders) [computationally verified]:
all coefficients REAL (Im E = 0 to all perturbative orders); factorial
growth (|E₂₀|/|E₁₀|=660); optimal truncation at N=3, E_pert^opt=0.5873
(real). PT is incomplete/asymptotic and blind to decay — the 0-sector.

### D. Open-channel attempt (honest negatives owned)

To obtain an independent Γ, the far right was opened (x>X_c linear drop;
bounce region x<0.8 untouched; kink proven exponentially irrelevant at
X_c=3: 10-digit X_c-insensitivity). Findings:
- X_c=3.0: resonance weight at the kink ∼10⁻¹¹ → width ∼10⁻³⁶
  (x⁴ wall blocks escape); Richardson → 0. Below resolution — correct
  but useless.
- X_c=1.0: resolvable resonance (Im E∼−6×10⁻⁴ at ℏ=0.3) BUT
  X_c-dependent (7% for 1.0→1.2, 50% for 1.5) and the ℏ-scaling gives
  S_b,fit=2.51 vs bounce S_b=2.92 (14% low; prefactor ℏ-dependence and
  X_c systematics). The modification is too close — it perturbs the
  tunneling dynamics rather than cleanly opening a channel.
- No X_c gives both resolvability and X_c-independence: the quartic's
  x⁴ wall forces the trade-off. This is a structural limitation of the
  potential choice, not a technical failure.

### E. The form appears (second angle)

What IS established, cleanly:
- **0:** PT around the false vacuum → real, asymptotic, blind to decay (§C).
- **0.5:** the bounce exists with computed action S_b (§A); it is the
  saddle carrying the imaginary part — the decay channel (standard
  Coleman; the computation confirms the saddle, theory gives its role).
- **1:** Γ from the bounce is real and complete (standard).
The triple's division of labor appears in the decay-width setting —
not just in 11r's symmetric-well amplitudes. Second angle on the form.

## Verdict

**Polar opposite HOLDS (no additional pattern found); witness 3 confirmed
at the level of form from a second angle; remains HEURISTIC as evidence
for universality.**

- The 0/0.5/1 form appears in the false-vacuum decay setting: 0-sector
  (PT) incomplete/real, 0.5-sector (bounce) carrying the imaginary
  half-phase as the entire decay channel, 1 (Γ) real and complete.
  This is the standard Coleman/BZJ structure — which coincides with the
  triple's form. Second angle (decay width) after 11r's first angle
  (symmetric-well amplitudes).
- **No additional even/odd traversal phase structure** beyond standard
  accounting was found. The discriminating test (c) could not be run
  cleanly: (a) is conceptually impossible as specified (§B), and the
  open-channel systematics (§D) prevent a precision Γ_exact/Γ_bounce
  comparison. Within these limitations — which are owned, not hidden —
  the pre-registered prediction (polar opposite holds) stands.
- The "additional pattern" leg is therefore not so much refuted as
  untestable at the chartered precision with this potential choice.
  Per the charter, "suggestive but not discriminating" is the honest
  grade for the strong claim; the polar opposite is the verdict.

## Epistemic labels

- S_b values (two-way, 10⁻¹⁰): **computationally verified**.
- (a)-impossible-for-confining (two instruments): **computationally verified**.
- RS reality + factorial growth: **computationally verified**.
- Null (Im E=0, dx²→0 + HO machine-zero): **computationally verified**.
- 1-loop prefactor K: **inconclusive** (order-of-magnitude; wall documented).
- Bounce = decay saddle; Γ real/complete: **exact theorem** (Coleman/BZJ;
  the computation confirms the saddle's action, theory its role).
- No additional pattern in Γ: **computationally verified within probe
  scope** (scope honestly bounded by §B–§D).
- Triple-as-universal from the width: **heuristic** (form matches twice;
  no new mechanism).

## Branching identifiers

- **Why it ends here:** the discriminating question is adjudicated as far
  as the instruments reach — the form appears (second angle), no
  additional pattern found, and the precise (c) comparison is blocked by
  a conceptual wall (§B) and a structural potential-choice limitation
  (§D), both documented. Forcing further would invent precision.
- **Its own chain:** (1) the §B finding sharpens ALL future width probes —
  never assume complex scaling yields a resonance; open the channel by
  design, with a potential whose wall doesn't force the X_c trade-off
  (§D); (2) the prefactor wall (§A-anchor-2) is resumable inventory: the
  GY μ-shift and spectral-projection approaches are coded
  (node11s_gy.py, node11s_pref2.py) and their failure modes mapped;
  (3) a purpose-built open potential (false well + barrier + flat
  continuum, no x⁴ wall) would make (c) clean — queued as a possible
  11t.

## Backward touch (done)

- `triple_artifact_0_5_1.md` — witness 3 status updated (below).
- Node 15 — same status update (below).
- `DECISION_TREE.md` — Node 11s record (this file becomes its §1).
- `interference_theorem.md` — untouched (probe doesn't bear on the graph
  mechanism; charter-specified).

## Method self-assessment

- §1 node record: this file.
- §2 labels: on every claim above; the inconclusive prefactor is labeled,
  not buried.
- §3 triadic fork: all three legs — claim (form appears; additional
  pattern sought), polar opposite (standard exhausts — HOLDS), null
  (single well, clean). The polar opposite leg is what makes the §B
  finding load-bearing: it reframes (a) rather than just failing it.
- §4 backward touch: done (above); tree edits made directly.
- §5 branching identifiers: above; 11t queued as resumable inventory.
- §6: live computation only (scripts in node11s_scripts/); anchors first
  (S_b passed, prefactor honestly inconclusive, null passed); the §B
  conceptual wall was found by computing (HO/FD convergence to real
  spectrum), not by theorizing; failures absorbed (FD kinetic-sign bug
  caught by null; τ-integral singularity → ODE bounce; homoclinic
  instability → forward+reflect; μ-shift/GY walls mapped, not hidden);
  honest negatives owned same-exchange (§A-anchor-2, §D).
- Deviation: the probe adapted its design mid-run (open channel) when
  computation revealed the charter's (a) was conceptually impossible —
  recorded as a finding (§B), not a silent deviation. The adaptation is
  the method's "absorb, don't guard" rule operating.

## Files

- Scripts: `~/workspace/prime-sieve-geometry/node11s_scripts/`
  (node11s_bounce.py, node11s_prefactor.py, node11s_pref2.py,
  node11s_gy.py, node11s_width.py, node11s_ho.py, node11s_open.py,
  node11s_rs.py, node11s_gscale.py)
- This record: `~/workspace/prime-sieve-geometry/node11s_falsevacuum.md`
