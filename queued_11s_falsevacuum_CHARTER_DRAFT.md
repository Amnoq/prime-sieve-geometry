# DRAFT charter — queued probe: false-vacuum decay width (prospective Node 11s)

**Status:** AUTHORIZED 2026-10-06 (user's "Word") — running as Node 11s.
**Date drafted:** 2026-10-06

## Why this probe exists (chain)

Node 11r tested the 0/0.5/1 triple's prospective third witness in the
symmetric double well V=(x²−1)². The form appeared — 0-sector
(perturbation theory) incomplete/ambiguous, 1-sector (instanton) gives
the real splitting, 2-sector (bounce, the double traversal) carries
the imaginary half-phase ±i·e^{−2S₀} completing the 0-sector — but no
additional even/odd interference pattern exists in any real
observable: the polar opposite held (standard dilute-gas + BZJ
resurgence exhausts it). Third witness stands at "confirmed at the
level of form; heuristic as evidence for universality."

11r's own chain queued this probe as item 1: the false-vacuum decay
width as the direct physical observable of the bounce's half-phase.
The reason it is the decisive next level: in the symmetric well the
bounce's imaginary contribution is a subtlety that cancels (energy
stays real); in false-vacuum decay it IS the observable —
Γ = −2 Im E₀. The double traversal is the entire decay channel.

## Question

Does the 0/0.5/1 triple appear as an observable pattern in the
false-vacuum decay width, or does standard Coleman dilute-gas + BZJ
resurgence exhaust it?

## The mapping (his terms)

- **0:** perturbation theory around the false vacuum — knows nothing
  of decay; incomplete/ambiguous.
- **0.5:** the bounce — out-and-back, the double traversal — carries
  the imaginary half-phase.
- **1:** the physical decay width Γ — real, complete, needing 0+2.

## Prediction (stated before computing)

The polar opposite is expected to hold again — 11r's verdict predicts
it: Coleman + dilute gas + BZJ accounts for everything; no additional
traversal-phase structure in Γ. The probe's value is the honest test,
not the hoped outcome.
- Negative → confirms 11r's wall from a second angle; witness 3 stays
  form-level/heuristic; the ledger records the attempt.
- Positive → witness 3 promoted to computationally verified
  observable; the triple gains its third witness in full.

## Triadic fork

1. **Claim:** Γ shows additional even/odd traversal phase structure
   beyond the standard bounce-gas accounting — the triple's third
   witness promoted.
2. **Polar opposite:** standard Coleman dilute-gas bounce (+ BZJ
   resummation of the multi-bounce series) exhausts Γ; no additional
   pattern exists.
3. **Null:** a potential with no false vacuum (single well, or the
   symmetric well with Γ=0) — the complex-scaling pipeline must
   return Im E = 0. Pipeline sanity.

## Discriminating test

Compute Γ three ways and compare:

- (a) **Γ_exact** from complex-scaled exact diagonalization
  (x → xe^{iθ}, Im E₀ = −Γ/2), convergence-checked in basis/grid,
  across several asymmetry parameters ε.
- (b) **Γ_bounce** from the Coleman bounce action S_b plus the
  1-loop fluctuation determinant.
- (c) **The multi-bounce series:** fit
  Γ_exact/Γ_bounce = 1 + c₁e^{−S_b} + c₂e^{−2S_b} + …
  and compare the c_k against dilute-gas predictions. Any deviation
  beyond honest error bars = additional pattern = claim leg.
  Agreement = polar opposite.

## Design constraint from 11r (load-bearing)

Do NOT attempt to isolate the 2-sector's real fingerprint — it is
inseparable by theorem from the 0-sector's Borel ambiguity. 11r
mapped this wall; this probe must not re-attempt it. The observable
is the width itself — the bounce's native channel — not a decomposed
component.

## Regime assumption (pre-registered 2026-10-06, user's word)

The bounce half-phase in Γ is a **closed-system prediction**.
Christie, Joo, Kaplanek, Vennin & Wands ("Cosmic Lockdown,"
JCAP-accepted, arXiv:2512.14204, v2 2026-03-11) show that in an open
system — scalar field in an asymmetric double well during inflation,
coupled to a spectator-field continuum, Markovian + non-Markovian
master equations and stochastic unravelings solved numerically —
decoherence Zeno-suppresses inter-well tunneling: once the state
localizes in a well, the localizing term grows as e^{6N}, sustained
tunneling would require coherences the Lindblad channel immediately
destroys, and remaining relaxation proceeds only via exponentially
rare barrier hops (mean first-passage time exponential in
(μ³vol)³). Interference is what decoherence kills first, and the
half-phase is an interference signature. Their environment
(inflationary spectator continuum) is far from this probe's isolated
QM double well, so the regimes are cleanly separated — but on the
record: in any appreciably monitored environment the tunneling (and
with it the signature) is Zeno-erased.
Epistemic label: peer-reviewed, computationally verified in their
own numerics; not a theorem; no bearing on the BZJ theorems or on
11r's verdict (isolated-system result, different regime).

## Anchors (run first; stop if they fail)

- Reproduce S_b to stated accuracy (analytic thin-wall or numeric
  reference).
- Reproduce the 1-loop prefactor within its known 2-loop
  contamination envelope.
- Null control: Im E = 0 clean.
If anchors fail, that is an instrument finding, not a verdict.

## Honest negatives to own same-exchange

- 2-loop prefactor contamination (the 11r lesson): expect prefactor
  fits to be inconclusive — do not force.
- Multi-bounce terms are exponentially suppressed: state the
  resolution floor for the c_k and do not claim what the floor hides.
- Complex-scaling θ-dependence must plateau; if it doesn't, that is
  an instrument finding.

## Verdict mapping

- Polar opposite holds → witness 3 stays "confirmed at level of
  form, heuristic as universality evidence"; Node 15 + triple note
  updated with the second-angle confirmation.
- Claim (additional pattern, surviving controls and honest error
  bars) → witness 3 promoted to computationally verified; triple
  note, Node 15 updated via backward touch.
- "Suggestive but not discriminating" is an acceptable honest
  outcome per the standing directive — record it as such, do not
  force.

## Backward touch (specified for whoever runs it)

- `triple_artifact_0_5_1.md` — witness 3 status line.
- Node 15 in `DECISION_TREE.md` — same status.
- `DECISION_TREE.md` — new Node 11s record (this charter becomes
  its §1 on authorization).
- `interference_theorem.md` — untouched (probe doesn't bear on the
  graph mechanism).

## Cost

One subagent run under METHODOLOGY.md, same shape as 11r. No user
input needed mid-run. On the user's word, this charter is the brief.
