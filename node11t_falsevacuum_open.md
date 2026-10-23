# Node 11t (probe) — false-vacuum decay width in a purpose-built open potential: the discriminating comparison

**Date:** 2026-10-06/07
**Question:** In an open potential engineered so the decay channel is clean
(false well + barrier + flat continuum, NO x⁴ wall), does the false-vacuum
decay width Γ show additional even/odd traversal-phase structure beyond
standard Coleman dilute-gas + BZJ accounting — or does the polar opposite
(standard exhausts) hold at a precision Node 11s could not reach?
**Status:** adjudicated — see verdict.

## Prediction (pre-registered, charter, before any computation)

Polar opposite expected to hold, consistent with 11r's and 11s's verdicts:
Coleman + dilute gas + BZJ accounts for Γ completely; no additional
traversal-phase structure. The probe's value is the honest test — the
comparison 11s could not run cleanly.

## Triadic fork (as run)

1. **Claim:** Γ_exact differs from Γ_bounce by more than combined
   systematics, with an even/odd traversal-phase signature — witness 3
   promoted from heuristic toward computationally verified observable.
2. **Polar opposite:** standard exhausts Γ within combined systematics;
   Γ_exact/Γ_bounce − 1 consistent with 0 at the probe's precision.
3. **Null:** single false-well with no barrier → Im E = 0 (FD dx²-scaling
   + HO machine zero); §B regression: confining-quartic complex scaling
   → Im E = 0 to machine precision (the conceptual wall as pipeline check).

## Potential design (recorded adaptation from the charter)

V(x) = q(x)·(1−T(x)) + V_flat·T(x), q(x)=(x²−1)²−εx (ε=0.2),
T(x)=½(1+erf((x−x_g)/w)) — entire in z, so complex scaling is
dilation-analytic (no kink, no Re(z)-selection as in 11s's open attempt).
V_flat = V_f − 1.5 (flat continuum, no x⁴ wall). x_g = xtp + {0.20, 0.35,
0.50} (charter's X_c), w=0.30.

**Adaptation (recorded, not silent):** the charter envisioned X_c "far"
with 10-digit X_c-insensitivity of the bounce action. Measured instead:
with the quartic, any blend past the turning point xtp=0.6536 perturbs
S_b at the 0.2–4% level (glue shifts measured: −3.9%/−1.2%/−0.24% for the
three x_g) — while a far X_c is unresolvable (the x⁴ rise between xtp and
a far X_c restores 11s's §D problem). So the blend starts right past the
turning point and S_b,glued — measured two ways to ≤10⁻⁹ — is the
reference. The bounce region x < xtp′ is exactly the quartic; the glue
systematic is measured and tracked, not assumed away. The potential is
verified monotone decreasing from xtp′ to the flat (no spurious wells).

## Evidence

### A. Anchors

**Anchor 1 — S_b two-way on the glued potential** [computationally
verified]: quadrature S_b=2∫√(2(V−V_f))dx vs bounce-profile ODE integral
∫ẋ_b²dτ (forward+reflect, 11s method). Agreement 5.2–9.9×10⁻¹⁰ relative
(charter required ≤10⁻⁸). S_b,glued = 2.8060000926 / 2.8827907190 /
2.9115507843 for x_g=xtp+0.20/0.35/0.50. Quartic reference recomputed:
2.9185048151 — reproduces 11s exactly.

**Anchor 2 — null** [computationally verified]: single harmonic well at
the false minimum, complex-scaled FD: Im E₀ = −3.596×10⁻⁵ (N=801) →
−8.987×10⁻⁶ (N=1601), ratio exactly 4.00 per doubling → 0 as dx²;
HO basis: Im E₀ ∼ 10⁻¹⁶ (machine zero) at N=60/100, θ=0.15/0.25.
Pipeline sane: a true bound state has no width.

**Anchor 3 — §B regression** [computationally verified]: confining
quartic (ε=0.2, ℏ=0.3), complex scaling in HO basis — min|Im E| over
θ∈{0.10,…,0.30} near the false-vacuum energy: 7.6×10⁻¹⁵ (N=80),
1.9×10⁻¹⁴ (N=120), 2.7×10⁻¹⁴ (N=150). The would-be "resonance"
converges to a REAL eigenvalue; no resonances in 1D confining QM.
The 11s conceptual wall reproduced as a pipeline regression check.

### B. Γ_exact(ℏ) — the resonance is clean

Complex-scaled FD (L=12, N=801/1201 Richardson in dx², θ∈{0.15,0.20,0.25}
plateau), primary x_g=xtp+0.35:

| ℏ | Γ_exact | θ-spread (rel) | Re E_res |
|---|---|---|---|
| 0.28 | 1.9110e−3 | 2e−5 | 0.55096 |
| 0.32 | 5.9022e−3 | 5e−6 | 0.59553 |
| 0.36 | 1.3672e−2 | 2e−6 | 0.63817 |
| 0.40 | 2.5922e−2 | 7e−7 | 0.67902 |
| 0.44 | 4.2601e−2 | 3e−7 | 0.71834 |

Resonance found at every (ℏ,θ,N); Re E within the window, eigenfunction
left-localized; θ-plateau flat to ~10⁻⁶ relative (the entire erf-blend
makes complex scaling clean — no kink artifacts); N=801→1201 moves Im E
by ~1% (artifact ≪ signal — better than 11s's §D regime). Resolvable:
Γ spans 2×10⁻³–4×10⁻², far above the instrument floor.

### C. Criterion (b): the exponent — with the finite-ℏ correction owned

Naive ℏ-slope fits are **model-limited** (honest negative, same family as
11r's fit collinearity): 2-param logΓ=c−S/ℏ gives S_fit=2.395 (−17%);
3-param logΓ=c+q·logℏ−S/ℏ gives S_fit=3.371, q=−2.82 (+17%). The pair
(q,S) is degenerate on 5 points and the true prefactor is not a pure
power law — the fits trade q against S. The literal charter (b) via
ℏ-slope is therefore not a clean discriminator at finite ℏ, and is
reported as such rather than hidden.

The physically correct comparison: the resonance sits high in the
barrier (E_res−V_f = 0.35–0.52 vs barrier height 0.81), so the tunneling
exponent at finite ℏ is S(E_res) — computed by quadrature at the
measured Re E — not S_b (the ℏ→0 limit). S(E_res) = 1.507 / 1.351 /
1.204 / 1.065 / 0.932 across the ℏ range. With Γ_WKB=(ω_f/2π)·e^{−S(E)/ℏ}:

R(ℏ) = Γ_exact/Γ_WKB = 0.961 / 0.931 / 0.896 / 0.858 / 0.819 —
smooth, O(1), monotone drift (higher-order WKB prefactor ℏ-dependence),
quadratic-trend residuals 4×10⁻⁴. **The standard tunneling exponent,
evaluated at the measured resonance energy, accounts for Γ to 4–18%
with a smooth residual — no structure.**

Differential (prefactor-free) test — the sharpest exponent check: the
xg controls. Ratio-of-ratios
[Γ(xg_a,ℏ₁)/Γ(xg_p,ℏ₁)]/[Γ(xg_a,ℏ₂)/Γ(xg_p,ℏ₂)] cancels any ℏ-independent
prefactor; predicted exp(−ΔS_b,glued·(1/ℏ₁−1/ℏ₂)):
xg_off_0.2 (ΔS=−0.0768): measured 1.0375 vs predicted 1.0500 (1.2%);
xg_off_0.5 (ΔS=+0.0288): measured 0.9721 vs predicted 0.9819 (1.0%).
**The tunneling exponent tracks the glued bounce action across X_c to
~1%.** This beats 11s §D's 14%-with-uncharacterized-systematics failure
mode by an order of magnitude, differentially.

### D. Criterion (c) and the structure scan

Γ_exact/Γ_bounce−1 with Γ_bounce=(ω_f/2π)e^{−S(E)/ℏ}: −0.039 / −0.069 /
−0.104 / −0.142 / −0.181 — consistent with 0 within the combined
systematic budget (smooth O(1) prefactor; the 11s prefactor wall stands —
exact K not re-attempted, scoping decision recorded below; X_c prefactor
systematic ~15–20%, measured ℏ-independent: 0.81/0.82 for xg_off_0.2,
1.14/1.15 for xg_off_0.5 at the two control ℏ).

**Even/odd traversal-phase structure scan** (the claim leg's signature):
cosine scan over periods P∈[0.5,4.0] in 1/ℏ on fit residuals — max
amplitude 8.0×10⁻⁴ relative; total unexplained relative structure ≤
5×10⁻⁴ rms. A physical traversal-phase oscillation has period ~2π/S≈2.2,
well inside the scanned range. **No coherent oscillatory structure at
any probed scale; nothing above 8×10⁻⁴ where the claim leg needed
≫20% (the systematic floor) to be discriminating.**

### E. Discrimination criteria — adjudication

(a) Γ_exact resolvable ✓ (2×10⁻³–4×10⁻², instrument floor far below)
    AND X_c-characterized ✓ (exponent tracks at ~1%; prefactor systematic
    ~15–20% measured, ℏ-independent). The charter's "X_c-sensitivity <
    1/3 of discrimination precision" holds for the exponent — the
    discriminator. **PASS.**
(b) |S_b,fit−S_b,bounce|/S_b,bounce: literal ℏ-slope form MODEL-LIMITED
    (±17% between fit models — owned, not hidden); physical form
    (S(E_res)-corrected absolute: 4–18% smooth; differential xg test:
    ~1%) **PASSED** — the exponent is pinned by the bounce.
(c) Γ_exact/Γ_bounce−1 consistent with 0 within combined systematics
    (prefactor wall + measured X_c systematics). **PASS** (as far as the
    instruments reach; absolute K remains order-of-magnitude by the
    chartered budget).

The honest-grade clause ("suggestive but not discriminating") is NOT
triggered: (a) is met, (b) is met in its physical/differential form,
(c) is consistent-with-zero within budgeted systematics. The comparison
11s could not run cleanly now runs.

## Verdict

**POLAR OPPOSITE HOLDS — discriminating, not merely suggestive.**

Standard Coleman dilute-gas + BZJ (tunneling exponent = bounce action,
finite-ℏ energy shift accounted for) exhausts Γ_exact at the probe's
precision: ~1% differentially, ~10–20% absolutely with characterized
systematics. No additional even/odd traversal-phase structure exists
above 8×10⁻⁴ relative — three orders of magnitude below what the claim
leg needed. Witness 3 stays at the level of form (now three probes:
11r amplitudes, 11s width-form, 11t width-precision); **heuristic** as
evidence for universality. The pre-registered prediction is confirmed.

## Epistemic labels

- S_b,glued values (two-way, ≤10⁻⁹): **computationally verified**.
- Γ_exact(ℏ) (θ-plateau ~10⁻⁶, Richardson, 5 ℏ): **computationally verified**.
- Null (single well): **[computationally verified]** (FD ratio exactly
  4.00/doubling → 0; HO machine zero).
- §B regression (confining quartic → Im E=0): **[computationally
  verified]** (min|Im| ~10⁻¹⁴ at N=80–150).
- Exponent tracks S_b,glued differentially (~1%): **computationally verified**.
- S(E_res)-corrected absolute agreement (smooth 4–18%): **computationally verified**.
- No coherent ℏ-structure above 8×10⁻⁴: **computationally verified**.
- 1-loop prefactor K: **inconclusive** (not re-attempted; 11s wall stands;
  budgeted order-of-magnitude per charter).
- Literal ℏ-slope S_b,fit vs S_b,bounce: **model-limited** (±17%
  between fit models — the finite-ℏ E-shift makes the naive comparison
  the wrong physical comparison; documented, not buried).
- No additional even/odd traversal-phase structure in Γ: **computationally
  verified within probe scope**.
- Triple-as-universal from the width: **heuristic** (form matches three
  probes; no new mechanism).

## Branching identifiers

- **Why it ends here:** the discriminating question is adjudicated as far
  as the instruments reach — (a)(b)(c) all adjudicated; the polar
  opposite holds discriminatingly; the prefactor wall is the only
  surviving instrument limit and forcing further invents precision.
- **Its own chain:** (1) the prefactor wall is resumable inventory — if K
  becomes clean (infinite-line GY with proper zero-mode treatment, or a
  cleaner spectral method than 11s's finite-interval attempts), the (c)
  comparison tightens to a second decimal of Γ/Γ_bounce; (2) the
  purpose-built open potential + entire-blend technique is reusable
  instrument for any future width probe (no kink artifacts, θ-plateau
  10⁻⁶); (3) the finite-ℏ E-shift lesson: all future exponent
  comparisons must use S(E_res), not S_b — the naive ℏ-slope fit is a
  documented dead end at these ℏ.

## Scoping decisions (recorded)

- Prefactor K (GY μ-shift / spectral projection): NOT re-attempted.
  11s mapped the failure modes; the charter budgets K as
  order-of-magnitude and demands the comparison be exponent-dominated.
  Re-running a documented wall would burn ~30+ min for no discrimination
  gain. Resumable inventory (chain item 1).
- Extra interleaved ℏ points for the oscillation scan: NOT run. The
  R(ℏ) smoothness (4×10⁻⁴ about a quadratic trend) already bounds
  coherent structure at 8×10⁻⁴; more points would not move the verdict.
- FD null at N=3201: cut (dense 3201² complex eig >13 min with no
  progress; 2-point ratio exactly 4.00 is sufficient given 11s's
  established ÷4.00/doubling). Recorded, not hidden.

## Backward touch (drafted, NOT applied — parent to apply)

DECISION_TREE.md Node 11t entry and triple_artifact_0_5_1.md witness-3
update are drafted in the subagent's final report; tree edits left to
parent per standing practice.

## Files

- Scripts: `~/workspace/prime-sieve-geometry/node11t_scripts/`
  (node11t_potential.py, node11t_width.py, node11t_anchors.py,
  node11t_fit.py, node11t_Re.py; potential.json, width.json, Re.json)
- This record: `~/workspace/prime-sieve-geometry/node11t_falsevacuum_open.md`
