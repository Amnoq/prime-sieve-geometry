# Node 11t (probe charter, CLOSED 2026-10-07) — clean Γ_exact vs Γ_bounce comparison in a purpose-built open potential

**Date drafted:** 2026-10-06
**Status:** RUN and CLOSED — launched on the user's word ("proceed"); verdict: polar opposite holds, discriminating. Record: node11t_falsevacuum_open.md; scripts: node11t_scripts/; tree entry: DECISION_TREE.md Node 11t.
**Chain:** Node 11s closed with the discriminating comparison (c) blocked by a
conceptual wall (§B: charter's (a) impossible for confining potentials —
no resonances in 1D confining QM) and a structural potential-choice
limitation (§D: the quartic's x⁴ wall forces a resolvability/X_c-independence
trade-off, graded 'suggestive but not discriminating'). 11t removes the
§D limitation by design: a false well + barrier + flat continuum, no x⁴ wall,
so the channel can be opened without perturbing the tunneling dynamics.

## Question

In an open potential engineered so the decay channel is clean (no wall
behind it), does the false-vacuum decay width Γ show additional even/odd
traversal-phase structure beyond standard Coleman dilute-gas + BZJ
accounting — or does the polar opposite (standard exhausts) hold at a
precision the 11s potential could not reach?

## Prediction (pre-registered, before any computation)

The polar opposite expected to hold, consistent with 11r's and 11s's
verdicts: Coleman + dilute gas + BZJ accounts for Γ completely; no additional
traversal-phase structure. The probe's value is the honest test — the
comparison 11s could not run cleanly.

## Triadic fork

1. **Claim:** Γ_exact differs from Γ_bounce by more than combined
   systematics (anchor + prefactor + X_c), with an even/odd traversal-phase
   signature — witness 3 promoted from heuristic toward computationally
   verified observable.
2. **Polar opposite:** standard exhausts Γ within combined systematics;
   Γ_exact/Γ_bounce − 1 is consistent with 0 at the probe's precision.
3. **Null:** the pipeline must return Im E → 0 on a control (single
   false-well with no barrier, or the confining-quartic reproduction of
   11s's §B: complex scaling must give Im E = 0 to machine precision).
   Pipeline sanity; the §B reproduction also re-anchors the conceptual
   wall as a regression check.

## Potential design (the load-bearing choice)

V(x): false well near x_f, barrier peak, and for x > X_c a FLAT continuum
(linear drop or constant), with NO x⁴ wall. Design constraints:
- The Euclidean bounce must be exponentially localized in the
  well/barrier region, far from X_c (kink-exponential-irrelevance
  criterion: 10-digit X_c-insensitivity of the bounce action, as in 11s §D).
- Resolvability and X_c-independence must coexist: with no wall, moving
  X_c outward should reduce the width (continuum coupling) without the
  X_c-dependence seen at X_c=1.0 in 11s §D (7%→50%). Target:
  X_c-sensitivity < 1/3 of the claimed discrimination precision.
- The bounce region (x < bounce turning points) must be X_c-independent
  to 10 digits, so Γ_exact's X_c-dependence is a measured systematic,
  not tunneling-dynamics perturbation.

## Anchors (pass before any claim)

1. **S_b two-way** [computationally verified required]: quadrature
   S_b=2∫√(2(V−V_f))dx vs bounce-profile ODE integral ∫ẋ_b²dτ —
   agreement ≤10⁻⁸ relative (relaxed from 11s's 10⁻¹⁰ only if the open
   wall forces coarser ODE tolerances; record which).
2. **Null** [verified]: single-well control → Im E = 0 (FD: dx²-scaling
   → 0 with measured ÷4.00/doubling; HO: machine zero).
3. **§B regression**: confining-quartic complex-scaled spectrum must
   reproduce Im E = 0 to machine precision — the conceptual wall as a
   pipeline check.

## Instrument walls carried forward (from 11s — respect, don't repeat)

- 1-loop prefactor K: finite-interval zero mode swamped by O(dt)
  discretization; T-truncation breaks mode structure. node11s_gy.py and
  node11s_pref2.py (GY μ-shift, spectral projection by ẋ_b overlap) are
  coded with failure modes mapped — reuse as starting points, do not
  re-derive. Budget K as order-of-magnitude uncertainty in Γ_bounce; the
  discriminating comparison must be EXPONENT-dominated, with the
  S_b,fit-vs-S_b,bounce agreement (11s §D criterion: ≤14% discrepancy
  was the failure mode to beat) as the quantitative check.
- Homoclinic instability → forward+reflect integration for the bounce.
- FD kinetic-sign null check (the bug 11s caught by its null).
- Honest negatives same-exchange: the prefactor wall and any
  X_c-residual are labeled, not buried.

## Discrimination criterion (pre-registered)

The comparison is discriminating iff:
(a) Γ_exact is resolvable (not below the instrument floor as in 11s
    §D's X_c=3.0 case) AND X_c-insensitive to the target precision;
(b) |S_b,fit − S_b,bounce|/S_b,bounce ≪ the size of any claimed
    beyond-standard structure (i.e., the exponent is pinned before the
    prefactor can be blamed);
(c) Γ_exact/Γ_bounce − 1 differs from 0 by more than the combined
    systematic budget.
Otherwise the honest grade is 'suggestive but not discriminating'
again — and that grade is itself the finding.

## Regime assumption (pre-registered, carried from 11s's charter)

The bounce half-phase is a CLOSED-system prediction. In open,
decohered systems vacuum tunneling is Zeno-suppressed (Cosmic Lockdown,
Christie et al., arXiv:2512.14204 — peer-reviewed, computationally
verified in their numerics, not a theorem). The numerical potential is
an isolated quantum system; no bearing on BZJ theorems or 11s's verdict.

## Branching identifiers

- **Why it ends here:** the discriminating question is adjudicated as far
  as the instruments reach — the (c) comparison either resolves or earns
  the honest grade. Forcing further invents precision.
- **Its own chain:** the surviving leg is the prefactor wall: if K becomes
  clean on the open potential (GY/spectral-projection succeed where the
  confining interval failed), the (c) comparison tightens to a second
  decimal of Γ/Γ_bounce — resumable inventory again.

## Launch

Subagent brief: this charter + METHODOLOGY.md (§1–§6, triadic forks,
epistemic labels, live computation only, backward touch on the triple
artifact and Node 11s's record). One word from the user launches; nothing
here runs anything.
