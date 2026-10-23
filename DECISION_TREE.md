# Prime-Sieve Geometry Decision Tree

The documented path of the circle-sieve / Figueiredo investigation.
Each node: date, the question, options considered, the decision, the
evidence, and status (closed / open / forked). Numbers are stable
references — cite them in future notes (e.g. "reopening node 4").

Companion record: `DERIVATIONS.md` (D1–D6, each with an honest
epistemic label: exact / computationally verified / conjectural /
heuristic). Labels say what kind of thing each claim is; this tree
says where the exploration has been and what is still open. Analyze
both when choosing the next move.

---

## 0. Root — 2026-09-29
**Q:** Can Figueiredo's positive-geometry method be brought to bear on
prime distribution via the user's linear circle sieve?
**Decision:** Pursue. User's framing: the sieve is a deterministic
relational machine ("composites relating to the primes and the primes
relating back to zero"); her binary/geometric work is the same kind of
move — definition through relations, not intrinsic coordinates.
**Status:** closed (the program this tree records).

## 1. Survey her method — 2026-09-29
**Q:** What is actually transferable from her work?
**Decision:** Transfer the *process*, not the implementation. Her
recurring moves: identify a positive region; construct its canonical
form; read off the observable; derive zeros, factorizations, soft
limits afterward — never put the answer in by hand. Papers surveyed:
arXiv:2309.15913, 2312.16282, 2402.06719, 2403.04826, 2405.09608,
2412.19881, 2506.05456, 2603.03425. None touches primes.
**Status:** closed. Standing steer (node 5 reinforced it).

## 2. Finite incidence complex — 2026-09-29
**Q:** Does the sieve's territory structure carry computable geometry?
- **Experiment:** `sieve_complex.py` — vertices = primes ≤ N, faces =
  prime sets with product ≤ N (the divisor complex). Verified the
  corrected sieve equals the classical primes; link recursion exact;
  Betti numbers grow with N (e.g. N=1000: [74,101,26,0]).
- **Finding:** no positive region, no canonical form found; everything
  depends on the cutoff N.
**Status:** closed. Negative result, kept — it killed the naive hope
and forced node 4.

## 3. First derivations D1–D3 — 2026-09-29
**Q:** Do her recipe's steps have analogues on the sieve?
- **D1** (verified): Chebyshev ψ(x) as a signed face-sum — the
  observable read off the complex (Möbius, reframed).
- **D2** (verified): Lehmer's φ-recursion IS the link recursion —
  the fast prime counter was the facet recursion all along.
- **D3** (verified): binary/zero-locus form — composites as the zero
  locus of F(n) = ∏ dist(n, pℤ), primes as its support.
**Decision:** the SHAPE of her recipe fits (steps 2–4 analogues).
**Status:** closed. Honest label: classical theorems in new clothes.

## 4. The N → ∞ limit — 2026-09-29
**Q:** Is there a limit object, or does cutoff-dependence kill the analogy?
- **Bare limit trivializes:** Δ_∞ is the contractible infinite simplex
  — no topology. The geometry must live in the weights, not the bare
  complex.
- **D4** (verified): canonical face-weights w(S) = (−1)^{|S|+1}log(∏S)/∏S;
  Σw(S) → 1 IS the Prime Number Theorem ("the weighted infinite simplex
  has total weight 1"; 1.001658 at 2·10⁶). Weights' Dirichlet generating
  function = −ζ′/ζ² (verified ~4 digits) → the zeta zeros regulate the
  face-sum.
**Status:** closed as a derivation. **Opened:** the positivity question —
weights are SIGNED (alternating), not positive. Sharpest open question:
a positive region with these weights as stratum residues?

## 5. Methodological steer — 2026-09-29
**Q:** Copy her implementation or take her generative insights?
**Decision (user):** do NOT copy the implementation; take her GENERATIVE
insights on the process — whatever most benefits the analysis or derives
an equation.
- **D5** (conceptual): territory removal = her soft-limit/splitting move
  (arXiv:2405.09608); φ(x,a) = φ(x,a−1) − φ(x/p_a,a−1) iterated to all
  orders = the D1 face-sum. The sieve was doing splits before we knew
  her name for them.
- Deepest such insight, applied throughout: *never put the answer in by
  hand* — the sieve never tests primality with a predicate.
**Status:** closed (standing methodology).

## 6. Deformation program — 2026-09-29
**Q:** What does her "deformations" move generate on the sieve?
**Decision (user: "proceed"):** deform the marking rule to R_p = {0}
(p = 2), {0, −2} (p odd).
- Deformation SEPARATES markers (primes) from survivors (twin prime
  lowers) — verified: generative survivors ≤ 200000 are exactly the
  2160 twin lowers.
- Exact deformed μ-identity for the static z-sieve (verified at z=30,
  x=200000); face multiplicities m(S) = ∏|R_p|; δ(z) = ∏(1−|R_p|/p)
  with S(x,z)/x → δ(z) (6 digits at z=7).
- **D6** (verified algebra): the Hardy–Littlewood twin constant DERIVED
  as renormalized total weight — 𝔖(z) → 2C₂ = 1.32032 (1.3228 at z=100).
**Status:** closed on the algebra. **Honest boundary:** π₂(x) ~ 𝔖x/(log x)²
remains the UNPROVEN twin conjecture (ratio 1.6091 at 2·10⁵). We verify
the algebra, not the conjecture.

## 7. The paper — 2026-09-29 — OPEN
**Q:** Does this arc belong in a paper, and which one?
- NOT the primorial-wheel paper (different subject: wheel state-space
  reduction mod 210). This arc wants its own paper.
- Honest vehicle: an expository/synthesis paper — "a geometric language
  for sieve theory" — not a claimed breakthrough. Novelty is in the
  framework/language (D6's framing appears new; the underlying
  computations are classical).
**Next:** draft outline (title, abstract sketch, section map over D1–D6
+ pictures) for user approval, then LaTeX draft with reproducible
verification scripts.
**Status:** open, outline drafted 2026-09-30 (PAPER_OUTLINE.md, updated to
cover D10/Node 11/CCM/Nodes 13-14 + failures appendix). Awaiting user
approval on title/scope + prior-art search before novelty claims.

## 8. The RH bridge question — 2026-09-29 — OPEN
**Q:** (user) RH is unproved for lack of an analytic–geometric bridge;
do we have enough to make that bridge?
**Analysis:** we have a DICTIONARY (analytic ↔ geometric translations),
not a bridge. Weil's template: topology supplies the actors, positivity
tells them where to stand. Our bare complex is contractible (node 4) —
no topology to exploit; the hope lives in the weights, which are signed.
The bridge, if it exists, attaches at POSITIVITY — which is node 9.
**Status:** open. The claim is a research heuristic with precedent, not
an established result.

## 9. Hunt the positive region — 2026-09-29/30 — SPLIT
**Q:** Is there a positive region whose canonical form has the
face-weights w(S) as its stratum residues?
- **9a — CLOSED 2026-09-30 (D7):** where positivity lives is located.
  The primitive objects are positive: −ζ′/ζ = ΣΛ(n)n^{−s} (Λ ≥ 0),
  log ζ(s) > 0, δ(z) = ∏(1−1/p) > 0 with −log δ(z) a manifestly
  positive prime sum (verified 6 digits). The weight generating function
  factors as (positive)·(Σμ(m)m^{−s}) — the signs come entirely from the
  Möbius factor, i.e. from inclusion-exclusion. δ(X) > 0 monotone → 0
  while Σ_{d≤X}μ(d)/d oscillates in sign toward the same 0: the signs
  are an expansion artifact, not a property of the volume.
- **Classical template verified:** the 3-4-1 positivity
  (3+4cosθ+cos2θ ≥ 0 on −ζ′/ζ = ΣΛ(n)n^{−s}) forces ζ(1+it) ≠ 0 —
  positivity of the primitive ⟹ a zero-free region. Re-verified
  numerically from the Λ-sieve (sum stays positive, grows 2.26 → 8.30 →
  20.62 as σ → 1⁺). This is the Weil-shaped mechanism in miniature.
- **9b — CLOSED 2026-09-30 (D8):** the bridge carries traffic — with an
  honest boundary. The full 3-4-1 argument is now expressible in the
  sieve's language: −ζ′/ζ as vertex-tower energies E₀/E₁/E₂, the trig
  polynomial as ½|1+e^{iθ}|⁴, stratum energies e_{p,k} ≥ 0 termwise
  (identity verified 6 digits). The proof restated: a zero on Re(s)=1
  would force negative-infinite total energy from nonnegative strata —
  impossible. The contradiction is *visible* in a way the trig identity
  hides. Boundary: the singularity structure (residue −m) is analytic
  fact the complex houses but doesn't derive — same traffic, new
  bridge, no new theorem yet.
- **9c — CLOSED 2026-09-30 (D9):** answered negatively, by theorem not by
  difficulty. (i) The D8 deformation seed is killed: 3-4-1 transports to
  zeta_R (verified) but zeta_R is an Euler product, hence zero-free for
  Re(s)>1 — the machine runs with nothing to exclude; the pole merely
  gets heavier (order 2, verified). (ii) Positivity is blind left of the
  line: Dirichlet-series positivity converges only for sigma>1; the
  crossing is done by analytic input (partial fractions, zeta'/zeta
  bounds) — geometry owns positivity, analysis owns continuation.
  (iii) Parity barrier: pure sieve positivity cannot resolve omega(n)
  parity (Selberg) — analytic input is *necessary*. (iv) Literature:
  trig-polynomial optimization is saturated (Mossinghoff-Trudgian-Yang
  2022: R=5.558691, "near its intrinsic limit"; Bellotti-Trudgian-Yang
  2026: 1/(4.896 log|t|)).
- **9c' — CLOSED NEGATIVE 2026-09-30:** the saturated degree-16
  optimizers do NOT have small-support autocorrelation structure.
  F16 (Mossinghoff-Trudgian 2015, Table 5 — the degree-16 optimizer
  behind R0<5.57353; MTY 2022's "essentially saturated" method):
  all 32 real Fejer-Riesz factors c=(c_k) are FULLY DENSE — 17/17
  nonzero at 1e-6 relative tolerance (sparsest at 1e-3 still 15/17);
  a_k lags 14/17 nonzero; participation ratio 3.62; coefficients span
  3 orders of magnitude with mass piled at high lags (c11..c16).
  Table-5 internal consistency verified to 5e-15; F16>=0 on fine grid.
  The density holds across EVERY zero-reflection choice, so it is
  structural, not an annealing accident. Interpretation: saturation
  comes from numerical optimization over R^16, not from a hidden
  small charge pattern — the sieve's small-support |Q|^2 language
  captures 3-4-1 (9b) but not the saturated optimum. Consistent with
  9c's "near intrinsic limit": the remaining slack is genuinely
  numerical, not geometric. [computationally verified]
  (zero_free_support.py)
**Status:** 9a/9b/9c/9c' closed. Node 8 (RH bridge) now has its
attachment point and its mechanism-template.

## Node 10 — Completing the bridge: candidate spans (OPEN, 2026-09-30)

**Question:** granted the load limits (D9), what methodology / perspective /
reference could construct the *rest* of the bridge — the hybrid span
between geometric positivity (built, D1–D9) and the analysis that crosses
Re(s) = 1?

**Key orienting fact (literature):** Weil (1952) proved RH *is* a
positivity — W(f∗f̃) ≥ 0 for all test f, where W is the explicit-formula
distribution (Bombieri 2000 exposition; Connes–Consani 2020). And over
function fields, RH was proved *by* a positivity with a known geometric
source (intersection pairing on C×C). So: we know exactly what the
missing span must be made of — a *source* of positivity — and we know
such sources are geometric. Our program has been building a candidate
source (stratum energies). The rest of the bridge = connecting our
geometric positivity to Weil's positivity.

**Options:**
- **10a — Weil's criterion in the energy language.** The explicit
  formula's arithmetic side is a prime-power sum (vertex towers, our
  native objects) minus archimedean terms; the test functions f∗f̃ are
  *squares* — same shape as our |Q|² autocorrelation family. Concrete
  first step: implement W(f∗f̃) numerically via prime powers for simple
  f, verify positivity on examples; then ask which test functions match
  which residue patterns. *This is D8's move, but where the positivity
  IS RH.* Circularity warning (literature): translating Weil ≠ proving
  RH — the positivity must come from the geometry *independently*.
- **10b — Li's criterion via the face-sum.** RH ⟺ λ_n ≥ 0 ∀n
  (Li 1997), λ_n = Σ_ρ[1−(1−1/ρ)^n]; λ_n expand via power sums
  Σ_ρρ^{−k}, which the explicit formula ties to ψ(x) — our D1
  face-sum. Most *computable* of the positivity criteria.
- **10c — Selberg's λ² sieve on the complex.** Selberg positivity is
  already |Σ|²-shaped (same move as our autocorrelations) but with
  *optimized* weights — an eigenvector problem. Our D6 used fixed
  patterns; Selberg optimizes the charge distribution. Concrete:
  formulate the Selberg quadratic form on the complex, solve small
  cases numerically. Ref: Friedlander–Iwaniec, *Opera de Cribro*.
- **10d — Function-field template (perspective).** The only known
  *source* of RH-positivity is geometric (intersection theory). Ask:
  what is the number-field analogue of the intersection pairing on the
  incidence complex? Deepest, most speculative. Ref: Weil; Bombieri;
  Connes–Consani.
- **10e — Tools:** large sieve (positivity of quadratic forms;
  Montgomery's zero-density engine) and the explicit formula's
  z-vs-T cutoff trade-off as "geometric uncertainty." Ref: Montgomery;
  Iwaniec–Kowalski.

**Status:** 10a IN PROGRESS (user: systematic pass through all options, in order).
- 10a-step1 DONE (2026-09-30): explicit formula grounded — truncated zero
  sum reproduces sieve-psi's oscillations, error 4.55→1.36 as T=50→400
  (`explicit_formula.py`, D10a-step1 in DERIVATIONS.md). Zeros regulate
  the face-sum: E(x)=ψ(x)−x is *made of* zeros.
- 10a-step2 DONE (2026-09-30): symmetric Guinand-Weil formula verified
  zero-side vs prime-side to machine precision (2e-16) for Gaussian
  squares h_a = |e^{-ar^2/2}|^2, a = 0.02/0.1/0.5 (`weil_positivity.py`;
  caught+fixed a prime-power ordering bug en route). W(h) >= 0 exhibited
  with NO zeros used — pure prime-side. DERIVED structural finding:
  prime-side positivity is cancellatory, not termwise (pole 2.266297 +
  arch -1.196347 - prime drain 1.069950 ~= 0 at a=0.5); the bridge IS
  the formula equating termwise zero-side positivity with prime-side
  balance. Dictionary: h=|H|^2 <-> P=|Q|^2. Weil's criterion itself
  (positivity <=> RH) cited, not derived.
- 10a-step3 DONE (2026-09-30): built the prime-side zero detector
  h_{T0,w} (sum of squares, exact Fourier pair) -- W(h) from primes
  alone agrees with the zero side to 4e-16 and counts zeros in a
  window (N+(B+) <= e^{1/2}W(h)). DERIVED: resonance mechanism --
  the oscillatory prime sum goes negative exactly when a zero is in
  the window (T0=50: -0.59/-0.98; empty window T0=100: +0.36,
  W all leakage); pole = 0 for detectors, archimedean = positive
  background. TIGHTEST DICTIONARY (exact algebra): detector prime
  side = 2Cg*Re[windowed E_1(1/2,T0)] -- our D8 energy, the window
  buying convergence at sigma=1/2. OPTIMIZATION ANSWER: figure of
  merit = concentration (leakage 0.68->0.30->0.0007); price =
  uncertainty (1e-12 envelope at n=e^{7.4/w}: 41/1700/2.8e6) --
  Pareto frontier, no finite optimum.
- 10a COMPLETE (2026-09-30): translation done. Open span (independent
  Gram/intersection source) belongs to the bridge program; 10d its
  natural home.
- 10b DONE/CLOSED (2026-09-30): Li's criterion does NOT live natively on
  the face-sum. lambda_n >= 0 verified both ways (Keiper-Taylor exact,
  n<=40; zero-side reconciled via density-integral tail to 3 s.f.;
  caught+fixed own pairing bug). DERIVED: S_1 = 1+gamma/2-(1/2)log(4pi)
  is archimedean (no convergent prime-sum presentation possible --
  proof uses only the functional equation); the Lambda-sums that want
  to be lambda_n's coefficients diverge as k!/eps^{k+1} (verified
  7.45->156 across k,eps) -- lambda_n needs their finite parts.
  VERDICT: Weil is face-sum-native, Li is Dirichlet-native; Li is the
  sharp-cutoff (inadmissible) limit of Weil-type positivity. Lesson:
  the face-sum carries smoothed/windowed positivity, not coefficient
  positivity.
- 10c DONE/CLOSED (2026-09-30): EXACT THEOREM -- on Delta_z,
  min_{lam_empty=1} sum_{S,T} lam_S lam_T/prod(S union T) = delta(z),
  uniquely attained at lam* = mu (proved via (1-1)^{|S|}; verified to
  12 digits, z<=19). M is PD (sum-of-squares, Weil-shaped). The optimal
  quadratic form IS inclusion-exclusion; the minimum recovers the
  Mertens product exactly. Classical level-truncated 1/G(z) is the
  constrained (worse) version. VERDICT: canonical template of an
  optimized face-quadratic form, but an upper-bound machine -- PD by
  construction, no continuation, no zeros; parity barrier intact. The
  independent zero-detecting source is still open -> 10d.
- 10d DONE/CLOSED (2026-09-30): function-field template exhibited on
  concrete elliptic curves (F_5, F_7): finite EXACT explicit formula
  #E(F_{p^n})=p^n+1-pi^n-pibar^n verified by direct counting;
  RH=Hasse=discriminant<=0 of the degree form Q(m,n)=pm^2+a_p mn+n^2,
  PSD *because degree counts* (deg(1-/+phi) exhibited as point counts).
  TEMPLATE: (i) Jacobian torus, (ii) Frobenius operator, (iii)
  counting-born PSD form, (iv) zeros as eigenvalues, (v) finite exact
  formula. LEDGER: we HAVE counting positivity (Lambda>=0), finite PD
  face forms (10c), a windowed explicit formula (10a); we MISS the
  Jacobian-role space (Delta_infty contractible), a Frobenius-like
  operator, and the pairing tying zeros to counting positivity. The
  missing object is operator-theoretic, not another inequality.
  Toroidal question answered: plane for zeta's domain, torus (Jacobian)
  for the geometric explainer.
- 10e DONE/CLOSED (2026-09-30): supporting tools verified on our
  objects -- Montgomery-Vaughan mean value (1/2H)int|P|^2/S2 -> 1
  (0.995->1.007); large sieve holds (ratios 0.004, 0.008); uncertainty
  cost curve quantified (w=0.5 -> 2.9e6 primes, w=0.25 -> 8.2e12:
  infeasible -- the prime-side detector's fundamental wall).
  Zero-density audited as the unconditional-izer (plug-in point
  precise; estimates cited). VERDICT: analytic amplifiers, not
  independent positivity sources; 10d ledger unchanged.

## Node 10 -- BRIDGE PROGRAM COMPLETE (2026-09-30)
Systematic pass 10a-10e closed. Standing:
- 10a: Weil positivity is face-sum-native (windowed/smoothed); detector
  built; optimization = Pareto frontier (no finite optimum).
- 10b: Li's criterion is NOT face-sum-native (Dirichlet-native).
- 10c: Selberg lambda^2 = canonical optimized face-quadratic form;
  exact optimizer mu, minimum delta(z). Template, not zero-detector.
- 10d: function-field template + ledger. Missing object is
  operator-theoretic (a "Frobenius for Delta"), not another inequality.
- 10e: amplifiers verified; uncertainty wall quantified.
The face-sum carries three verified positivity kinds (primitive
counting Lambda>=0, Weil-type windowed, Selberg-type optimized); none
detects zeros independently. Sharpest open question: the
Frobenius-like operator (refines D4's).

## Node 11 -- THE FROBENIUS-LIKE OPERATOR HUNT (opened 2026-09-30)
Question (refines 10d ledger): what would a Frobenius-like operator for the
sieve/number-field setting have to satisfy, and does any candidate -- on the
Mobius-band stage M, on the face-complex, or in the literature -- satisfy it?
Checklist from the 10d template: (R1) spectrum = zeros; (R2) trace formula =
explicit formula; (R3) positivity/self-adjointness <=> RH; (R4) positivity is
counting-born (deg>=0 analogue); (R5) finite exact formula; (R6) stage where
the s~1-sbar symmetry is geometric.
- 11a DONE (2026-09-30): Berry-Keating xp leg. Semiclassical prediction
  N(T)~(T/2pi)(log(T/2pi)-1)+7/8 verified against 400 zeros (gamma<=679.7):
  |S(T)|<=1.164, mean 0.502, drift slope 5.5e-6 (no drift). VERDICT: xp gives
  R1's *shape* (reality of spectrum conjectured) and the smooth part of R2;
  the fluctuation S(T) -- the actual zero positions -- is exactly what xp
  does NOT give (it is the periodic-orbit/prime side; cf. the user's
  diagonal-approximation verification). No rigorous operator (domain issues),
  no R4. Score: sharpest spectral candidate, still a candidate.
  [computationally verified numerics; BK formula classical theorem;
   xp-as-operator conjectural]
- 11b DONE (2026-09-30): Mobius-band stage leg. M = strip/(s~1-sbar) with
  (0,t)~(1,-t) gluing. VERIFIED: |xi(1-sbar)|^2=|xi(s)|^2 to 3.8e-16 (6 pts)
  -- |xi|^2 descends to M (exact theorem, numerically confirmed). Zero
  orbits collapse 4->2 on M (pairs {rho,(1-rho)bar}); images lie on the
  central line sigma=1/2 (6 zeros checked). CORRECTION of earlier message:
  the collapse is 4->2, not 4->1 (s~sbar is a separate involution; the
  band uses only s~1-sbar). RH on M: all zero-images lie on the central
  line. VERDICT: M is a genuine *stage* (R6 exact) where the functional
  equation is topological; no operator lives on it yet (R1-R5 open).
  Figure: mobius_band.png. [exact/heuristic as labeled]
- 11c ANALYSIS (2026-09-30): checklist audit across candidates.
  * BK xp: R1 shape-only, R2 smooth-only, R3 conjectural, R4 absent.
  * Mobius band M: R6 exact; R1-R5 absent (stage, not operator).
  * Connes adele-class space (cited, not re-derived): R2 full (trace
    formula = Weil explicit formula); R1 as *missing* spectrum
    (absorption); R3 as Weil-positivity (analytic); R4 not counting-born
    in the deg>=0 sense.
  * Face-complex Delta operators: R4 present (Lambda>=0 counting; 10c PD
    forms); R1-R3 absent -- no natural operator in view (Delta_infty
    contractible, D4); R5 windowed only (10e wall).
  * FF Jacobian (reference): R1-R6 all satisfied -- the template itself.
  VERDICT: the missing piece is consistently R1+R4 *together* -- an
  operator with zeros as spectrum whose positivity is counting-born.
  Positivity without operator (face-complex) and operator-shape without
  counting (xp) and trace formula without geometric positivity (Connes)
  are the three live fragments; none closes R1^R4. The Mobius band is the
  program's own candidate *stage* (new in this conversation); the operator
  on it -- or on the weighted face filtration -- remains the sharpest
  open question. Node 11 stays OPEN pending an operator candidate that
  can be scored.
- 11e OPERATOR AUDIT (2026-09-30): full literature survey, 8 candidates
  x 8-point checklist, D1-D13 filter. Report: operator_audit.md.
  KILLED: Bost-Connes (no zeros in machine — gets the pole, not the
  zeros); Ruelle transfer (reduces to Deninger — no dynamics, no
  operator); Sierra xp-variants (smooth-count ceiling, same as 11a);
  Bender-Brody-Mueller (answer inserted by hand, not self-adjoint);
  Wu-Sprung (inverse tautology; the "fractal" was approximation error).
  CONJECTURAL-ONLY: Connes 1999 adele-class (deepest reformulation;
  missing Weil positivity IS RH — D10 at the highest level); Deninger
  program (missing space is the whole problem; 2024 theorem proves the
  template dynamically only).
  LIVE — Connes-Consani-Moscovici ZETA SPECTRAL TRIPLES (arXiv:2511.22755):
  D_log^{(lam,N)} self-adjoint by construction (Caratheodory-Fejer/
  Toeplitz extension), built ONLY from Euler products over p<=lam^2,
  spectra numerically coincide with low zeros ("striking accuracy" even
  at small x). Independently reproduced (Rust/MPFR, 999 digits, June
  2026). Authors state: proof of convergence = proof of RH (honest).
  Closest any literature candidate comes to our filtration language
  (x->infty is a sieve-limit; Weil form on support<=S is a finite
  face-sum object). TOP COMPUTATIONAL TARGET: reimplement from prime
  Euler products alone; verify spectral coincidence; audit perturbation
  for zero-fitting; quantify convergence error bars (D2); map the
  failure mode (what spectra do if RH is false). [literature survey;
  primary-source abstract verified; reproduction claims secondary]
- 11d DONE (2026-09-30): the cut + bare-stage operator probe. (a) Cutting
  a Mobius band along its center line does NOT give two bands: it gives
  ONE band, 2x length, 4 half-twists (2 full twists), orientable -- the
  one-sidedness is destroyed. Twist count VERIFIED numerically via the
  Gauss linking integral of the two boundary circles (|lk|=1.9999 ->
  k=4; integrator calibrated: k=0->0, k=2->1). Cut at 1/3 from the edge:
  TWO linked bands (thin Mobius + long 2-twist band), the classical
  result. [exact classical topology; twist count computationally
  verified] (b) Spectral probe of the bare stage: truncated (|t|<=50)
  Mobius-band Laplacian has EXACT spectrum lam=(pi*m)^2+(n*pi/2T)^2,
  m+n odd (orientable double cover + deck involution; derived, not
  cited). Its sqrt-spectrum (0.031, 0.094, 0.157, ...) bears no relation
  to zeta zeros (14.13, 21.02, 25.01, ...); the position observable
  |sigma-1/2| has continuous spectrum [0,1/2]. VERDICT (negative,
  exact): bare geometric operators on M do not see zeros. The operator,
  if it exists, must see the arithmetic (prime/weight) data, not just
  the stage geometry. Reflection (heuristic): M minus its central line
  is connected -- the quotient forbids separating sigma<1/2 from
  sigma>1/2; the flip binds them, which is the functional equation as
  inseparability. Next fork queued: probe the WEIGHTED face filtration
  for operator-like structure (the one place in our ledger where
  counting-born positivity actually lives).
  Figures: mobius_cut.png, mobius_spectrum.png.

## Archive dead ends (2026-09-30)
Mined master_archive-1_0_jcc6.docx (April 2026 vortex/k-reduction factoring
program) for dead ends at the user's direction: nine guardrails in
archive_dead_ends.md (D1 endpoint artifacts, D2 error bars exceed
resolution, D3/D4 level-count vs hidden work, D5 parallelism != complexity,
D6 heuristics need bounds, D7 check the uniform null, D8 know what the
medium can test, D9 name the hard core). The archive is closed
archaeology; its live descendants are Circle CEIVE (our geometric
language) and the honesty practice. Cross-reference before launching any
filtration, heuristic-detection, or simulation-heavy step.

## Node 12 — Multi-torus framework, from scratch (2026-09-30)
The user's original idea (never written down; absent from the April 2026
archive): link a 2-torus and a 3-torus by a self-adjoint operator.
Rebuilt from a clean foundation in multi_torus_framework.md. Dead-end
guardrails (archive_dead_ends.md) apply, especially D8.

- 12a (foundation, DONE): objects T^2 (leaf; also the 10d Jacobian type),
  T^3 (ambient), operator spec = Node 11 checklist R1-R6. Five linkages:
  L1 product, L2 mapping torus (flat/Nil/Sol), L3 unit tangent bundle,
  L4 Deninger-type foliated dynamical system (conjectural), L5 Heisenberg
  nilmanifold (twisted torus).
- 12b (Weyl probe, DONE): flat-T^3 Laplacian spectrum is EXACT,
  2pi*sqrt(m^2+n^2+k^2); 554,981 lattice points enumerated, first 300
  vs 300 zeta zeros — no relation (multi_torus_weyl.png). EXACT THEOREM:
  Weyl's law N(Lambda) ~ C_d Vol Lambda^{d/2}; zeros need (T/2pi) log T;
  d=2 too slow by a log, d>=3 too fast. No fixed-dimension manifold
  Laplacian has the zeros as its spectrum in counting. L1-L3 DEAD by
  theorem, not difficulty. Honest loophole recorded in the framework
  doc: zeros-as-subset of a higher-d spectrum is not closed by Weyl.
- 12c (Deninger-shaped linkage, DONE as formulation): the SURVIVING form
  of the user's idea — 3D foliated dynamical system, 2D leaves,
  flow generator (skew-adjoint) as the leaf-to-ambient link, closed
  orbits = primes, Ruelle zeta = zeta, explicit formula = Lefschetz
  trace. Status: conjectural, non-probable per D8 (formulate, do not
  simulate shadows). This is Deninger's program.
- 12d (QUEUED): Heisenberg nilmanifold Laplacian probe — the one
  non-flat computable case (theta-function spectrum via the Weil
  representation). Expect negative; it is the honest remaining check.
Verdict: "multi-torus via Laplacian" is dead (Weyl); "multi-torus via
dynamics" is the live form of the original idea. Framework's computable
content after 12d is exhausted; L4 remains as formulated conjecture.

- 12d (Heisenberg probe, DONE 2026-09-30): EXACT spectrum from
  representation theory — (2pih)^2+2pi|h|(2k+1), mult |h|, plus the
  torus part; 65,401 eigenvalues enumerated (heisenberg_probe.py).
  NEGATIVE on three panels (heisenberg_probe.png): (i) counting is
  Weyl d=3, slope 3/2, vs zeros' T log T; (ii) bulk spacings are
  rigid/degenerate (mass near 0, no level repulsion) vs the zeros'
  GUE-like repulsion; (iii) sequences unrelated. Moral: genuine
  theta-function / Weil-representation arithmetic content in a
  geometric Laplacian still does not give zero statistics —
  arithmetic flavor != zero spectrum. The missing operator is not
  "Laplacian + theta". Framework's computable content now exhausted;
  L4 (Deninger-type dynamics) remains as formulated conjecture.
  Node 12 CLOSED.

## Archive dead ends, second mining (2026-09-30)
Five more April-2026 documents read as archaeology at the user's
direction ("negative results refine the area that could possibly be
positive"). Three new guardrails appended to archive_dead_ends.md:
D10 (toroidal five-step proof — resonance/zero identification
imported, not derived; guardrail: prove the bridge, don't import it
— our 10a is the derived version), D11 (Prime Zipper Law falsified
as stated — first counterexample (1129,1151)->21 at the ~190th
pair; "era interaction" patch is post-hoc; gap quantization dead),
D12 (rh_final's formal compactification — weight engineered to
delete the continuous spectrum the conclusion needs gone; Lemma 3
keeps the test functions but the spectral side is what changed;
maps where Lax-Phillips genuinely gets stuck). D13 (coset-sum
numerology != Chebyshev mechanism). s_watts_v2 and the 60-second
piece filed without new extraction.

## Node 13 — Fermionic Fock fork: operator from the sieve's own materials (2026-09-30)
User approved the weighted face-filtration fork; first construction.
- 13a (EXACT identification): faces S of Delta_z = fermionic Fock basis
  over primes <= z (each prime used at most once = Pauli = squarefree
  kernel); mu = (-1)^F (fermion parity); face adjacency = fermionic
  hopping. Native, not imported.
- 13b (H_2 KILLED BY INSPECTION): H_2 = sum_p (log p / p)(a_p^dag+a_p),
  one-body hopping with the prime terms of -zeta'/zeta. Terms commute
  ([O_p,O_q]=0, O_p^2=1) => spectrum EXACTLY {sum_p +/-(log p)/p},
  verified vs dense diagonalization to 2.4e-15 (z=13); <r>=0.503,
  spiky structured spacings. Integrable by inspection; no numerics
  needed beyond the sanity check.
- 13c (H_int probe, NEGATIVE): H_int = H_2 + sum_{p<q}
  (log p log q)/(pq) n_p n_q — minimal interacting native Hamiltonian
  (one-body = zeta'/zeta prime terms, two-body = (zeta'/zeta)^2
  semiprime terms). Diagonalized z<=29 (dim<=1024, fock_operator.py).
  Bulk spacings track POISSON, not GUE: <r> = 0.459,0.418,0.400,
  0.411,0.419 (Poisson 0.386, GUE 0.536); histogram monotone
  decreasing, max at 0 (fock_probe.png). [computationally verified]
- Understanding (the valuable part): the interaction is Fock-diagonal
  — it shifts energies but causes no transitions; all mixing comes
  from the integrable one-body hopping. Poisson was unsurprising in
  hindsight. Next construction if the fork continues: OFF-DIAGONAL
  two-body (pair hopping a^dag a^dag a a with arithmetic weights).
- D4's positive-region half (canonical form with face-weights as
  stratum residues) remains OPEN. Node 13's minimal construction
  closed as a kill; the fork itself stays open via the off-diagonal
  variant.

## Node 13d — pair-hopping: FIRST POSITIVE operator signal (2026-09-30)
Added the mixing term 13c lacked: H(lam) = H_2 + H_diag
+ lam * sum_{p,q,r,s} w_p w_q w_r w_s a_p^dag a_q^dag a_r a_s
(number-conserving pair hop, w_p=(log p)/p). lam_0 fixed by
||lam_0 H_pair||_F = ||H_2+H_diag||_F; scanned 0.25x-4x; z<=29
(dim<=1024, fock_pairhop.py). Implementation note: summing over ALL
ordered quadruples with symmetric weights gives identically zero
(a_r a_s = -a_s a_r); must use canonical p<q, r<s sectors.
RESULT: bulk statistics GUE-like across all z>=17 and all lam:
<r> -> 0.52-0.55 (GUE 0.536, Poisson 0.386); spacing histogram shows
level repulsion (dip at 0, peak ~0.5) tracking Wigner, far from
Poisson. [computationally verified]
CAVEATS (exact): (1) shuffled-weight control ALSO gives GUE (0.524)
-- this is generic two-body quantum chaos (TBRE class), not created
by the arithmetic; the non-trivial content is that the arithmetic
weights are COMPATIBLE with chaos (they could have been too weak/
structured). (2) Universality class != the zeros: eigenvalues are not
gamma_n; no zero detection. (3) Finite sizes; histogram not pure
Wigner yet. Precise claim: the sieve's native Fock space with
arithmetically-weighted hopping+interaction+pair-hopping is
quantum-chaotic in the GUE class -- the same universality class as
the zeta zeros. First operator in the hunt pointing the right way.
Strengtheners queued: larger z via Lanczos, Delta_3 rigidity,
density of states.
- 13d ROBUSTNESS (2026-09-30, fock_robust.py): dense diagonalization at
  z=31 (dim 2048) and z=37 (dim 4096), lam = 0.5*lam_0 and lam_0:
  <r> = 0.528/0.531 (z=31), 0.535/0.535 (z=37) -- GUE-compatible at 4x
  the original dimension, both couplings. The positive is not a
  small-size artifact. [computationally verified]
- 13d STRENGTHENERS (2026-09-30, fock_strengthen.py): sparse Lanczos at
  z=41 (dim 8192): bulk <r>=0.528 (1200 interior eigenvalues) --
  GUE holds at 8x original dimension. Delta_3 inconclusive (flat at
  ~0.33 across L=5..40; neither GUE-log nor Poisson-linear --
  likely unfolding/window artifact on the 1200-eigenvalue sample,
  not interpreted). z=43 (dim 16384) running. [computationally verified
  for r-stat; Delta_3 not interpreted]

## Node 13e — prime-frequency probe: NEGATIVE (2026-09-30)
Asked whether the pair-hop spectrum's fluctuations oscillate at prime
frequencies f_p = log(p)/2pi (the explicit-formula signature, run in
reverse). z=29 spectrum, degree-10 detrended N_osc, Lomb-Scargle,
vs GUE(1024) and shuffled-weight controls (fock_primefreq.py).
RESULT: no prime-frequency content. Mean z-score at the 10 prime
lines = -0.35 (arith), -0.36 (shuffled); GUE control 0.28 (flat noise,
method unbiased). Both arith and shuffled show one broad structural
hump at f~0.67 (construction-scale, not arithmetic -- identical in
shuffled). [computationally verified]
Honest limits: spectral bandwidth only ~7.3 at z=29, so the lowest
prime frequencies (p=2,3: <1 period across the spectrum) are weakly
resolved; null is strongest at larger p. Degree-10 detrending could
partially absorb broad oscillations, but the GUE control through the
identical pipeline shows the method creates no structure.
VERDICT: the operator is GUE-chaotic (13d) but does not HEAR the
primes -- its fluctuations carry no prime-frequency content. The
"make 10a and 13d talk" attempt returns: they don't, this way. 13d
stands as a universality result (side chamber), not a bridge plank.

## D6-GENERALIZATION — k-tuple deformation sweep (PREDICTIVE TEST, 2026-09-30)
**Q:** (user) "trying to find predictive value" — is the deformation a
general generative machine or a twin fluke?
**Method:** for each constellation H, deform R_p to H's forbidden
residues, mark n when (n+h) is a PROPER multiple of p≤z (simultaneous
Eratosthenes on k linear forms). Three panels per tuple at x=10⁶:
(a) survivors at z=√(x+maxH) vs independently enumerated constellation
lowers (exact set match?); (b) finite-z density S(x,30)/x vs
δ_H(30)=∏(1−ν_p/p); (c) renormalized weight 𝔖_H(z)→S(H) vs reference.
Tuples: twins, cousins, sexy, 2 triplet types, quad, quint, sext +
NON-ADMISSIBLE {0,2,4} control. Code: `ktuple_deformation.py`,
results: `ktuple_results.json`.
**Results:**
- (a) EXACT MATCH on all 9 tuples: twins 8169=8169, sexy 16386,
  triplets 1393/1444, quad 166, quint 34, sext 5=5 — zero unsound,
  zero incomplete. [computationally verified]
- (b) density ratios 0.998–1.015 across all tuples (worst = sext,
  fewest samples). Finite-weight prediction holds uniformly.
  [computationally verified]
- (c) 𝔖_H(1000) matches reference S(H) to ~0.2%: twins/cousins→2C₂,
  sexy→4C₂ (ν₃=1, factor 2 — correctly distinguished!), triplets→
  2.8583, quad→4.1514, quint→10.133, sext→17.301. [computationally
  verified]
- NON-ADMISSIBLE {0,2,4}: deformation DIES as predicted — exactly ONE
  survivor, n=3 i.e. (3,5,7), the unique prime triple of that form;
  𝔖_H(z)=0 for z≥3 (ν₃=3 kills the product). The admissibility
  obstruction emerges from the machine, uninserted. [computationally
  verified]
**Honest calibration:** (a) at z≥√x is essentially definitional
(simultaneous Eratosthenes) — its value is confirming clean
generalization + the non-admissible death, which was the genuinely
falsifiable prediction. (b) is classical sieve theory through the
deformation lens (confirmatory, not new). (c) reproduces known
constants (retrodictive). **Verdict:** the deformation is CONFIRMED as
a general generative machine, not a twin fluke; it produced no new
mathematics (expected — it was built to reproduce classical
structure), but it passed its falsifiable test. The predictive
program's next step is novel deformations (p-dependent R_p), not yet
run.
**Status:** closed as a confirmation sweep; predictive direction noted.

## PRIOR-ART SEARCH — 2026-09-30
**Q:** Which parts of this framework exist in the literature?
Searched 2026-09-30 (web). Findings, with honest calibration:

1. **Simplicial sieve Δ_z (faces = squarefree products, face-sum
   Möbius/inclusion–exclusion):** NO prior art found. The one
   "geometric view of the sieve" in the literature (Iosif,
   arXiv:1112.5796) is about focal lines in integer division —
   unrelated. The classical Möbius-of-a-poset/order-complex connection
   (Rota) is about *chains*, not the full simplex on primes with face
   weights. → The *framing* appears new; the underlying
   inclusion–exclusion is classical (acknowledged throughout).
2. **Weighted infinite simplex, PNT as "total weight 1"**
   (w(S)=(−1)^{|S|+1}log(∏S)/∏S, Σ_{∏S≤X}w(S)→1): NO prior art found.
   → Appears new as a *statement*; it reframes PNT, does not
   reprove it.
3. **Deformation deriving 2C₂:** the constant and its standard
   local-density derivation are classical (Hardy–Littlewood 1923).
   Related heuristic sieves exist (e.g. arXiv:2507.03107 f(t;z)
   analysis). But the specific move — *deforming the sieve's marking
   rule* R_p, proving the deformed survivors ARE the twin lowers, and
   deriving 2C₂ as the *renormalized total weight of the deformed
   sieve* — NOT found. → The generative deformation move appears
   new; the constant is classical.
4. **Fermionic Fock space over primes:** INDEPENDENT PRIOR ART EXISTS.
   The goldenphysicsproject (GitHub, contemporary 2026) independently
   identifies "squarefree prime subsets as the natural basis of the
   finite fermionic prime Fock space" and formalizes CAR structure on
   prime generators in Lean. Priority is genuinely unclear (both
   contemporary, theirs is a repo not a publication). The
   *identification* (faces = Fock basis, μ = fermion parity) is NOT
   unique to this work and must be credited as independently known.
   Our distinct contribution is the *spectral program*: interacting
   Hamiltonians with arithmetic weights + GUE/Poisson probes (13d/13e)
   — no prior art found for that direction.
**Status:** search complete 2026-09-30; novelty language in
PAPER_OUTLINE.md must respect these boundaries. Re-search before any
public claim.

## Node 14 — D4's positive-region half: obstruction + refined home (2026-09-30)
Question: a positive region whose canonical form has the face-weights
w(S) = (-1)^{|S|+1} log(prod S)/(prod S) as stratum residues?
- 14a OBSTRUCTION (exact): NO ordinary positive geometry can. AHBL
  canonical forms have logarithmic poles with residues +-1 (0-dim
  strata: +-1 or 0); |w({2})| = (log 2)/2 = 0.3466 not in {0,1}.
  Signs are fine (residue alternation); magnitudes impossible.
  D4's "no positive region found" explained by theorem, not luck.
- 14b IDENTITY (exact): d/du[prod_{p<=z}(1-p^{-u})]_{u=1}
  = sum_S w(S) = delta(z)*sum_{p<=z}(log p)/(p-1). Two proofs
  (subset expansion; calculus) in DERIVATIONS.md; verified to 10
  digits, z<=29; asymptotic -> e^{-gamma} (0.5333 at z=1e5).
  Computes the 2^{pi(z)} subset sum in O(pi(z)).
- 14c REFINED HOME: E_z = (+)L_p with equivariant Chern roots
  -u*log p (real coeffs, legitimate); ch(lambda_{-1}(E_z)) =
  prod(1-p^{-u}); face-weights = u-derivative at u=1 =
  *differentiated residues*. Positive region = simplex
  Delta^{m-1}; stringy deformation with prime-log exponents;
  differentiation produces the weights. Only the primes are input;
  combinatorics, signs, log-magnitudes computed. This is
  Figueiredo's *deformations* (D6) as the mechanism -- closing the
  D4<->D6 loop: the arithmetic lives in the deformation/weights,
  exactly D4's conclusion, now with the obstruction explained.
  [exact constructions; numerics = hygiene]
- Node 14 CLOSED. D4 fully closed (bare complex trivial + weights
  carry the arithmetic + ordinary positive region impossible +
  deformed home constructed).

## Node 11f — CCM independent reimplementation: FIRST ZERO RECOVERED (2026-09-30)
Question: does D_log^{(lam,N)} built ONLY from prime Euler products
spectrally recover zeta zeros, with zero input nowhere in the pipeline?
- 11f IMPLEMENTATION (2026-09-30): independent Python/mpmath
  reimplementation from primary source arXiv:2511.22755 (ccm/ccm_reimpl.py).
  Matrix M = W_{0,2} - W_R - W_p assembled exactly as paper Sec.4:
  W_{0,2} verbatim eq.(4.2) [rank 2, verified]; W_R diagonal via master
  formula (weinfty) validated against direct quadrature to 2e-16;
  W_R off-diagonal (J(m)-J(n))/(pi(n-m)); prime sum verbatim eq.(bomp)
  over k=p^r<=lam^2 with von Mangoldt weights (D12 audit boundary:
  primes ONLY enter here; all else is zero-independent analysis).
  Fixed endpoint bug: lam=sqrt(13) float rounding excluded k=13;
  now uses exact integer cutoff (9 prime powers at x=13).
- 11f KEY FINDING: full matrix at small N shows multiple tiny
  eigenvalues (NOT a bug — known-good connes-cvs CvS implementation
  shows identical structure at N=8). Resolution: restrict to EVEN
  subspace (dim N+1); even block has SINGLE tiny eigenvalue
  eps_N=2.83e-26 at c=13,N=10,dps=60 (inverse iteration, residual
  1.4e-47). Odd-block smallest is 581x larger (1.64e-23) — ground
  state naturally even, as paper assumes.
- 11f D2 VERIFICATION (computationally verified): xihat(z) zeros from
  even-block ground state (delta_N(xi)=1 normalized, NO zero input):
  At c=13,N=10,dps=60: zero 1 err 7.1e-15, zero 2 err 2.7e-12,
  zero 3 err 4.9e-10. At c=13,N=20,dps=100: eps_N=1.57e-39;
  zeros 1-5 err <4e-11 (zero 1 exact to float64); zeros 6-8 err <1e-6.
  First zeta zero recovered from prime Euler products alone to
  machine precision. Higher zeros (4+) require larger N (spurious
  roots at N=10). Systematic N-convergence confirmed.
- Status: D2 PILOT COMPLETE. The bridge plank EXISTS: primes -> (Weil
  form) -> zeta zeros, with no zero-fitting in the pipeline.
- 11f CONTROLS (2026-09-30, ccm/ccm_controls.py): all at c=13,N=20.
  A (Wp=0): eps_N=-0.17 (not positive), first root 2.79 (err 11.3).
  B (shuffled Lambda): eps_N=-0.087, root 5.78 (err 8.4).
  C (shuffled log p positions): eps_N=0.0175 (not tiny), root 1.16
  (err 13.0). Zeros AND positivity both require the precise prime
  arithmetic input; the machinery does not produce zeros on its own.
  [computationally verified]
  11f LARGE-N (2026-09-30): c=13,N=40,dps=120: eps_even=9.46e-54,
  even/odd separation 3744x (grew from 581x at N=10); zeros 1-5
  err <1e-10, 6-10 err <2e-6. [computationally verified]
  11f N=120 (2026-09-30, ccm_largeN.py, 24 min): eps_even=3.48e-59,
  eps_odd=3.06e-55, separation 8771x (monotone growth: 581x -> 3744x
  -> 8771x across N=10,40,120). Zeros 1-5 err <1e-10; zeros 6-10
  err <2e-6. Paper scale matched. Convergence law + even-sector
  isolation confirmed at the largest N tested. [computationally verified]
  11f FAILURE MODES (2026-09-30, ccm_failure_modes.py): the mechanism
  requires EXACT prime arithmetic -- it is fragile, not robust.
  Multiplicative noise on Lambda: 1e-6 -> root err 2.1; 1e-4 -> err 9.2;
  1e-2 -> err 11.5 (eps goes negative). Drop p=2 or p=3: destroyed
  (err ~10.7). Drop p=5: SURVIVES (root 14.063, err 0.07). The small
  primes carry the weight (explicit-formula hierarchy); the tiny
  eigenvalue is a delicate exact-identity cancellation, not a stable
  gap. Honest scope: true "RH false" mapping needs an actual
  counterexample; what we show is the operator is an exact-arithmetic
  reporter, not a robust statistical effect. [computationally verified]
  Open: N=120 to match paper scale.
- 11f CONCEPTUAL BRIDGE (2026-09-30): the "your bridge or borrowed?"
  question gets a precise answer. CCM's input is Λ (von Mangoldt, on
  prime powers); the face-sum's native weights are μ (on squarefree
  subsets). EXACT THEOREM: Λ = μ ∗ log (Dirichlet convolution),
  Λ(n) = −Σ_{d|n} μ(d) log d — verified numerically to 3.6e-15 for
  n<5000. So CCM's fuel is exactly one convolution away from the
  face-sum's native weights. The *machine* (D_log, even/odd blocks,
  variational principle) is borrowed from CCM; the *fuel* refines to
  face-sum-native μ. The bridge is neither fully yours nor fully
  borrowed — it is a genuine connection: the borrowed machine runs on
  fuel one convolution from your weights. [exact theorem]
- 11f N=120 CLOSED (see above). Node 11 stays OPEN as the operator
  hunt; 11f is the live candidate with a now-explicit face-sum
  dictionary entry (Λ = μ∗log).

## Node 11g — BK xp on toroidal lattice vs Berry tones: CLOSED NEGATIVE (2026-10-05)
(The Oct-5 toroidal phonon letter's "Node 11a"; letter-11a/11b naming is
the letter's own, distinct from the Sep-30 11a semiclassical leg above.)
Proposal: H=(xp+px)/2 discretized on a uniform 1D lattice
(x_j=x0+j·a, N=3000, x0=0.5, a=0.05) with p the Fourier (toroidal)
derivative — the 1D toroidal building block of the letter's T³ claim;
T³ sum spectrum (E_ijk=e_i+e_j+e_k, top-150 positives, 3.375M levels)
as secondary panel. Tested against the Berry tones with the Node 13e
probe: subtract smooth counting, Lomb-Scargle the residual, z-scores of
power at f=r·log p/(2π), 23 prime-power lines p^r≤50 (covers the
measured tones (2,1),(3,1),(5,1),(7,1),(2,2),(3,2),(2,3)). Controls:
GUE same dim (method null), shuffled BK spectrum (correlation null).
Scripts: node11a_bk.py, diag11a.py; outputs node11a_bk.json/png.
- Hermiticity 2.7e-16 ✓. Spectrum dim 3000, range [-9114, 9108],
  1500 positive.
- FINDING 1 (smooth level): WRONG counting. Level density peaks at E=0;
  mean spacing grows 1.75 (center) → 15.5 (spectral edges), symmetric.
  BK predicts density ~(1/2π)log E, i.e. spacing *shrinking* with E.
  The discretization fails before fluctuations: it does not reproduce
  even the smooth BK prediction. (Linear fit beats E·log E fit on the
  positive-branch counting; robust to x0/a doubling.)
- FINDING 2 (fluctuations): chirped ladder — locally rigid
  (<r̃>≈0.99 at N=600/1200/3000), globally varying (std/mean≈1.2).
  Not GUE (0.536), not Poisson (0.386): integrable-like. No
  quantum-chaotic fluctuations at all.
- FINDING 3 (tones): ABSENT. Mean z=0.20 at the 23 prime-power freqs;
  all 7 letter tones z≤0.18, most negative; at/below the shuffled
  control (mean 0.21, max 3.85). T³-sum panel toneless (mean 0.08,
  max 2.95). The letter's falsification criterion is triggered.
- PROBE CAVEAT (instrument limitation, owned): the GUE control hit
  max z=7.73 at one prime frequency — the z-scores assume a white
  background but the residual periodogram is colored, so absolute σ
  thresholds overstate significance. Valid inference is
  candidate-vs-controls, which is cleanly negative here. Caveat
  applies to the 13e probe generally; 13e's control-comparison
  conclusion (negative) stands.
- CAUSE OF DEATH (hypothesized, not proved): a uniform x-lattice
  maximally breaks the dilation symmetry x→e^λx that xp relies on;
  the faithful lattice for xp is log-uniform (x_j=x0·q^j), where
  dilations act as translations. Note the honest boundary: even on a
  log lattice the -i/2 term makes the cutoff boundary conditions the
  physics (self-adjoint extension choice) — a log-lattice test would
  be a NEW node with its own open choices, not a redo of 11g.
- VERDICT: Node 11g CLOSED negative. What it kills: the naive uniform
  toroidal-lattice discretization of BK (letter's Node 11a). What it
  does NOT kill: the continuum BK operator, whose content lives in
  the regularization. Per the letter, 11b (direct zero-matching) does
  not open; a different operator/regularization node opens on the
  user's call. [computationally verified]

## Node 11h — log-lattice xp: CLOSED BY ANALYSIS (2026-10-05)
Sequential follow-up to 11g's cause of death (uniform lattice breaks
dilation symmetry). The faithful repair is the log-uniform lattice
x_j=x0·q^j — uniform in u_j=log x_j, where dilations act as
translations — with H=(xp+px)/2 discretized in u.
- KEY ANALYTIC FACT: (xp+px)/2 = -i(x∂_x+1/2), and the unitary
  (Uψ)(u)=e^{u/2}ψ(e^u) : L²(ℝ⁺,dx)→L²(ℝ,du) satisfies
  U[(xp+px)/2]U⁻¹ = -i∂_u exactly. The bare operator IS free momentum
  in log coordinates — unitarily trivial.
- Hence the faithful discretization (uniform u-lattice, Fourier p_u,
  periodic/toroidal u — the letter's toroidal requirement) has EXACT
  ladder spectrum {2πn/Δu} by construction: the Fourier derivative's
  eigenvalues are exactly the k_n, no diagonalization needed. No
  fluctuations, no tones — analytically, not numerically.
- This sharpens 11g: not merely "wrong lattice" — every
  dilation-faithful discretization of bare xp is (approximately) ring
  momentum, hence (approximately) ladder. 11g's chirped ladder is the
  uniform lattice's broken version of this exact ladder.
- MORAL (in the literature; now earned here): the prime content of
  the BK story was never in the bare operator's spectrum. It lives
  entirely in the regularization — the cutoff boundary conditions /
  self-adjoint-extension choice. The periodic-u regulator gives an
  integrable ladder; a Sierra-style scattering-cutoff regulator is a
  different spectral problem and a different node.
- VERDICT: Node 11h CLOSED by analysis. If the hunt continues on xp,
  the next sequential node is the regularization node (cutoff + BCs
  as the operator) — new design choices, user's call. [exact theorem:
  unitary equivalence and ladder; heuristic: which regulator, if any,
  carries prime content]

## Node 11i — Sierra deformed-xp regularization: SMOOTH PASS, TONES ABSENT (2026-10-05)
The regularization node, implemented FAITHFULLY from the primary
source (Sierra & Rodriguez-Laguna, arXiv:1102.5356, PRL 106, 200201
(2011)) — equations extracted from the PDF via the arXiv HTML
rendering, not from paraphrase.
- Operator: Hh = x^{1/2}(ph + l_p^2/ph^{-1})x^{1/2} on x>=l_x,
  nonlocal BC (eq.11), U(1) self-adjoint-extension family (angle th);
  spectrum = roots E_n of (eq.14)
  Xh(E) = e^{-ith/2}K_{1/2+iE/2}(2pi) + e^{+ith/2}K_{1/2-iE/2}(2pi) = 0,
  with h = l_x*l_p = 2pi, hbar = 1, th = pi/4 (the paper's
  Riemann-matching choice; half-integer rule). K-Bessel via mpmath
  (complex order; scipy kv has no complex-order ufunc). Xh(E) is real
  (2 Re[...]); roots in +/- pairs. 1516 positive roots below E=2000,
  first at 19.1504 (cf. first zero 14.1347 — average match, not
  positional).
- FINDING (a) smooth counting: N(E) matches Riemann-von Mangoldt
  (E/2pi)(log(E/2pi)-1)+7/8 to 0.07% —
  E=100: 28 vs 29.0; 500: 269 vs 269.6; 1000: 648 vs 648.6;
  2000: 1516 vs 1517.0. The PRL's Fig.3 claim is computationally
  CONFIRMED. (Does not match my algebraic reading of the paper's
  eq.(16) as transcribed — the roots are ground truth; the
  transcription discrepancy is noted, not resolved.)
- FINDING (b) tones: ABSENT. Mean z=-0.66 at the 23 prime-power
  freqs, max z=-0.42; all 7 letter tones at z=-0.68 (periodogram
  floor — the residual carries no power at any prime frequency).
  Below the shuffled control (-0.02). Analytic reason: the
  quantization condition contains only the K-Bessel function — no
  prime content can enter — and the computation confirms it.
- VERDICT: the best published xp-regularization has the RIGHT smooth
  counting but NO tones. With 11g (naive discretization dead) and
  11h (bare operator unitarily trivial), the xp FAMILY is exhausted:
  no xp variant carries the tones. This matches Berry and Keating's
  own 2011 conclusion ("this absence of connection with the primes
  is shared by all variants of xp," Sierra slides). The operator
  hunt must leave xp; the live candidate remains 11f (CCM).
  [computationally verified]
- Scripts: node11i_sierra.py; outputs node11i_sierra.json/png.

## Node 11j — CCM prime-load mapping: hierarchy measured (2026-10-05)
Sequential follow-up to 11f's failure-modes pilot (which dropped only
p=2,3,5). Question: which prime powers in W_p are load-bearing for zero
recovery, and does the measured hierarchy match the explicit-formula
weights w(k)=Lambda(k)/sqrt(k)?
- Method: c=13, N=20, dps=80 (11f pilot scale). W_p is LINEAR in prime-
  power contributions: precomputed prime-free base (W02-WR) and each
  Q^{(k)} once (even-projected), then 15 ablations as fast matrix sums
  + inverse iteration. Baseline: eps=1.57e-39, root err 1.8e-15.
  Re-run bit-identical.
- FINDING 1 (hierarchy): load is monotone DECREASING in k, NOT
  proportional to Lambda(k)/sqrt(k) — in fact anti-correlated.
  Single-power drops (root err): k=2: 13.3 DESTROYED; k=3: 11.2
  DESTROYED; k=4: 4.62 DAMAGED; k=5: 0.072 survives; k=7: 4e-11;
  k=8,9,11,13: ~1e-15 unaffected. By w(k) the ranking would be
  7,11,5,13,3,2,9,4,8 — the measured order is nearly the reverse.
  The smallest prime powers carry the load; k>=7 are dispensable
  for the first zero. Prime-power effect: within p=2, it is 2 and 4
  that matter, not 8.
- FINDING 2 (decoupling): zero recovery is MORE robust than the tiny-
  eigenvalue positivity. Dropping k=5,7,11 drives eps NEGATIVE
  (-4e-4, -3e-14, -3e-32) — breaking the variational positivity —
  while the root survives (err 0.072, 4e-11, 1e-15). Refines 11f's
  "zeros AND positivity both require precise prime arithmetic":
  they decouple; the zero position is sturdier than the positivity.
- Interpretation: the fragility is STRUCTURED (hierarchical by k),
  not random. The machine's prime-sensitivity follows the
  small-prime-power dominance of the explicit formula's low-zero
  regime — but via k-ordering, not the naive per-term weight.
  [computationally verified]
- Scripts: node11j_loadmap.py; output node11j_loadmap.json.

## Node 11k — prime-load hierarchy vs zero index: HIERARCHICAL (2026-10-05)
Sequential follow-up to 11j (load map for zero 1 only). Question: does
the monotone-in-k hierarchy hold for higher zeros, or shift with zero
index?
- Method: c=13, N=20, dps=80; first 5 xihat roots per ablation
  (baseline errs <4e-11, validated vs true zeros 1-5); same 15
  ablations as 11j. Script node11k_zeroload.py; output
  node11k_zeroload.json.
- FINDING: the hierarchy SHIFTS — the machine resolves zeros
  hierarchically from prime data. k=2,3 destroy ALL five zeros
  (universal, err 11-19). k=4 damages zero 1 most (4.6) but higher
  zeros less (0.1-0.2). k=5: err grows 0.072 (z1) -> 2.2 (z5).
  k=7: err grows 4e-11 (z1) -> 8.6e-05 (z5) — dispensable for zero 1,
  load-bearing for zero 5. k=8,9,11,13: tiny but monotonically
  growing with zero index. The "load frontier" moves right as zero
  index rises: low zeros need small prime powers; higher zeros
  additionally need larger ones (finer log-k sampling for
  higher-frequency structure).
- Interpretation: mirrors the explicit formula's architecture —
  now measured, not assumed. The machine does not just report zeros;
  it resolves them hierarchically from the prime data.
  [computationally verified]

## Node 11l — prime-orbit quantum graph: MECHANISM CONFIRMED (2026-10-05)
Tests Berry-Keating's epitaph for xp ("a single primitive periodic
orbit for each energy E" vs "a family of primitive orbits labelled by
primes p, with periods log p"): does the prime-orbit mechanism itself
produce tones?
- Construction: Kirchhoff rose graph, R=8 loops of lengths
  L_j=log p_j (p=2..19). Primes enter ONLY as geometry (D12-style
  audit); spectrum computed independently via secular equation.
  Spectrum: vertex sector (1015 roots of smooth G(k)=0) + Dirichlet
  sector (1020 exact levels k=2 pi m/L_j). 2035 levels, k<=400.
- FINDING (full spectrum): tones at loop primes (mean z=2.35),
  NOT at non-loop primes 23..47 (mean z=-0.30, built-in negative
  controls); GUE/shuffled controls flat (<=0.6). Max z=9.14.
- FINDING (sectors separated): vertex sector ALONE shows tones
  (loop 4.02 vs non-loop -0.37, max 10.84) — genuine trace-formula
  orbit interference, no picket fences. Dirichlet sector ALONE shows
  even stronger tones (13.50 vs -0.62, max 24.82) — exact ladders
  with spacing 2 pi/log p give sawtooth harmonics at n log p/2 pi.
  Two distinct routes, same prime imprint.
- Interpretation: the prime-orbit mechanism WORKS. xp failed (11g/h/i)
  because it has no prime orbits; endow a system with prime-labeled
  closed orbits and the spectrum carries prime tones. This is also
  the POSITIVE control for the tone probe — validating that the
  11g/11i negatives are real absences, not probe blindness.
- Honest boundary: primes are input as geometry; this tests the
  orbit->tone mechanism, not the origin of primes. The operator hunt
  still needs the actual operator — but now knows what structure it
  must have (prime-labeled closed orbits).
  [computationally verified]
- Scripts: node11l_graph.py; outputs node11l_graph.json/png.

## Node 11m — Deninger program, primary-source assessment: STRUCTURE REAL, OPERATOR CONJECTURAL (2026-10-05)
Theory node (no computation), opened on the user's "Let's do it" after
11l. Question: what does Deninger's program actually contain — theorem
vs conjecture — and how does it relate to 11l's verified mechanism?
Sources read directly: arXiv:1807.06400 (2018; publ. Indag. Math. 2026,
37(1), 25-136) and expository arXiv:2301.11643 (2023).
- EXISTS [exact theorem]: Deninger CONSTRUCTED the dynamical system
  (X_0, phi^t) via rational Witt vectors and suspension. Thm 6.1:
  closed points of X_0 <-> compact packets Gamma_{x_0} of periodic
  orbits, all of length log N(x_0). For Spec Z: orbits gamma_p <->
  primes p, l(gamma_p) = log p. The "primes as closed orbits" picture
  is a theorem (2026), not a metaphor. One-codimensional foliation F
  from the suspension; the 3D Riemann-surface-lamination subsystem
  Y_0 for Spec Z is OPEN (v4 section 6 asks for it explicitly).
- TRACE FORMULA [exact theorem, foliation setting]: the transversal
  index theorem (Kop06/11): 1 - sum_rho e^{t rho} + e^{alpha t} =
  sum_gamma l(gamma) sum_{k>=1} +- delta_{k l(gamma)}, the exact
  analogue of Weil's explicit formula 1 - sum_rho e^{t rho} + e^t =
  sum_p log p sum_{k>=1} delta_{k log p} + (1-e^{-2t})^{-1}.
- OPERATOR Theta [conjectural]: infinitesimal generator of the
  R-action on leafwise harmonic L^2-forms (foliation cohomology).
  Conjectured eigenvalues = zeta zeros/poles; RH analogue = Re rho =
  1/2 (needs conformal factor alpha=1; smooth compact manifolds force
  alpha=0). Still open: Ruelle zeta = Hasse-Weil zeta (needs all
  Fuller indices = 1); the cohomology itself; the 3D subsystem.
- 11l RELATION [heuristic, structurally grounded]: 11l and Deninger
  are the same structural hypothesis at two levels. 11l: prime orbits
  -> trace formula -> spectral TONES [computationally verified].
  Deninger: prime orbits [theorem] -> transversal index [theorem] ->
  (conjecturally) ZEROS as spectrum of Theta. 11l is the computable
  proof of concept for Deninger's hypothesis: the orbit->spectrum
  machinery works when prime-orbit geometry is present.
- Honest boundaries: (i) 11l tests orbit->tone (fluctuations), not
  orbit->zero (eigenvalues) — Deninger's claim is strictly stronger;
  11l validates the mechanism, not the conjecture. (ii) This node
  yields NO computable operator: Theta acts on a cohomology that does
  not exist yet. Per D8, no toy "Deninger-like" operator is built.
- Verdict: the path forward stays computational via finite analogues
  (11l-style) and the function-field template (Weil, complete). The
  operator hunt now knows the structure it needs (prime-labeled
  closed orbits) AND that the structure is real arithmetic geometry,
  not analogy. Full assessment: node11m_deninger.md.

## Node 11n — geometry control (random loop lengths): MECHANISM IS GEOMETRIC, with interference refinement (2026-10-05)
Control for 11l's confound (loops were prime-labeled). Same Kirchhoff
rose (R=8), same probe, but loop lengths RANDOM IRRATIONAL in
[4.2,6.0] (seed 7) -- fundamentals in the virgin band [0.67,0.95],
all prime-power freqs <=0.62, min separation 0.0506. No arithmetic
enters. Prediction: tones at loop freqs, silence at primes.
- Merged spectrum (5190 levels): loop mean z=0.24 (max 1.02), prime
  mean z=-0.08. NAIVE verdict would be negative -- but sector
  decomposition decides otherwise.
- Dirichlet sector ALONE (2654 levels): loop mean z=26.06, max 61.13;
  prime mean z=-0.42. The mechanism is PURELY GEOMETRIC: exact
  picket-fence ladders put tones at whatever the loop lengths are,
  prime or random. Raw P~0.078 at loop freqs, consistent across all 8.
- Vertex sector ALONE (2536 roots): loop mean z=0.15 (max 1.01) --
  silent, unlike 11l's vertex (4.02). The vertex (trace-formula)
  route is LENGTH-DEPENDENT: sings for short prime-log loops, silent
  for long random loops.
- Merged raw P at loop freqs ~0.002 -- BELOW both Dirichlet (~0.078)
  and vertex (~0.007) alone: DESTRUCTIVE vertex-Dirichlet
  interference at the loop frequencies (vertex-scattered orbit
  amplitude has opposite sign to the Dirichlet-confined contribution
  at the same length). Tone observability in a merged spectrum is
  controlled by this interference, not just by the mechanism.
- Verdict: 11n PASSES its discriminating test -- the tone mechanism
  is geometric, not prime-specific (Dirichlet route, z=26, primes
  silent). Refinement: 11l's vertex tones and merged tones came from
  the short-loop regime; the vertex route's length dependence is now
  a precise open question. Does NOT retroactively falsify 11l (its
  spectrum sang in all sectors); it bounds the regime.
  [computationally verified]
- Scripts: node11n_control.py; outputs node11n_control.json/png
  (json includes sector_decomposition).

## Node 11o -- vertex length dependence: LENGTH, not arithmetic (2026-10-05)
Follow-up to 11n's puzzle (vertex sang for short prime-log loops,
silent for long random loops). Design: scale 11l's lengths by
c in {0.5,1,2,4} -- ratios (arithmetic structure) preserved, absolute
length alone varied. H1: vertex tone z decays with c. H2: flat with c.
- Vertex sector loop mean z: c=0.5 -> 5.54 (max 18.5); c=1 -> 2.57
  (max 9.9); c=2 -> 0.66 (max 3.1); c=4 -> -0.03 (max 0.10, silent).
  MONOTONIC DECAY. H1 confirmed; H2 dead. It is length, pure.
- Dirichlet control (positive): 7.40 -> 13.31 -> 22.73 -> 33.56 --
  sings at every scale (probe honest). GUE at c=1 flat (-0.03).
  Non-loop primes silent at every scale (all <= -0.08).
- 11n explained: its loops ([4.2,6.0]) sit at ~2.5-3.5x 11l scale,
  where the decay curve gives z~0.3 -- consistent with measured 0.15.
- Physical reading: the vertex fundamental tone has fixed absolute
  amplitude (set by the vertex scattering amplitude sigma); the
  background fluctuation variance grows with scale (more levels and
  resolved orbits in the window), so normalized detectability decays.
  The vertex (trace-formula) route is a SHORT-orbit phenomenon.
- Consequence for the hunt: the physical regime we care about --
  loops of length log p (short) -- is exactly where the vertex route
  sings loudest. 11l's regime, not 11n's, is the zeta-relevant one.
  [computationally verified]
- Scripts: node11o_scale.py; outputs node11o_scale.json/png.

## CORRECTION to Nodes 11n and 11o (2026-10-05) -- numerical artifact found and fixed
The user's question ("what sets the vertex route's length dependence?")
prompted a stress test that overturned both verdicts. Root cause: the
vertex root-finder used a FIXED scan step (0.05) while spectral density
grew with scale/length. At dense scales it missed closely-spaced root
pairs (11n: 2536 found vs 2650 true; 11o c=4 similarly corrupted).
Missing ~4.5% of roots -- specifically close pairs -- collapsed tone
z-scores catastrophically (0.15 vs 9.58). The "length dependence" and
the "destructive vertex-Dirichlet interference" were both artifacts of
corrupted spectra, not physics.
- 11n CORRECTED (fine scan 0.01; 5304/5315 Weyl = 99.8% complete):
  vertex alone loop z=9.58 (max 30.38); Dirichlet alone 26.06;
  MERGED loop z=13.82 (max 39.63); primes silent (-0.17) throughout.
  FULL PASS, no interference: random irrational loops sing in every
  sector. The mechanism is purely geometric and robust.
- 11o CORRECTED (exact roots via G(k;cL)=G(ck;L), so k_n(c)=k_n(1)/c
  -- no root-finding at all): vertex loop z = 5.95 (c=0.5), 2.57
  (c=1), 1.87 (c=2), 2.06 (c=4), 2.17 (c=8). FLAT -- the vertex route
  is SCALE-INVARIANT. There is no length dependence.
- Answer to the user's question: nothing sets it -- there is no
  vertex length dependence. The vertex (trace-formula) route is
  scale-invariant and geometry-independent (prime-log and random
  lengths alike). The Dirichlet route was never in doubt.
- Standing lesson (AGENTS.md-worthy): root-finder scan step must
  scale with spectral density; a "clean" total count (97%+) can still
  hide tone-killing defects when the missing roots are close pairs.
  11l unaffected (c=1 roots sparse vs scan step; exact-scaling test
  independently confirms the mechanism). [computationally verified]

## Node 11p — tones gate on the 11l candidate: PARTIAL (r=2 present, r=1 absent) (2026-10-05)
Runs the toroidal phonon letter's Node 11a gate exactly as sequenced,
on the 11l quantum-graph candidate: the candidate's pair-correlation
tones must reproduce the measured Berry tones -- r=1 (p=2,3,5,7),
r=2 (p=2,3), r=3 (p=2).
- Method: 11l spectrum recomputed live (1015 vertex roots + 1020
  Dirichlet levels = 2035 merged levels, bit-identical count to 11l);
  the 11g gate probe (degree-10 detrended Lomb-Scargle, z-scores at
  the 7 letter frequencies f=r*log(p)/(2*pi)); GUE + shuffled
  controls, same seeds. Script: node11p_gate.py (Idea execution);
  output: node11p_gate.json.
- RESULT (live re-run, reproduces 11l's stored detail to 0.1):
  (2,1) z=1.24, (3,1) z=-0.09, (5,1) z=0.62, (7,1) z=0.55,
  (2,2) z=9.23, (3,2) z=8.12, (2,3) z=0.20.
  Controls at the same 7 frequencies: GUE mean 0.61 (max 1.60),
  shuffled mean -0.09 (max 1.41).
- VERDICT: the gate as strictly stated is NOT passed -- the r=1
  fundamentals, the most prominent measured Berry tones, sit at
  control level (absent). But the candidate genuinely carries
  prime-power tones: (2,2) and (3,2) at z~9 and ~8, far above any
  control. (2,3) absent. Mean z over the 7: graph 2.84 vs GUE 0.61.
- Reading: 11l proves the orbit->tone mechanism (tones follow closed-
  orbit lengths), but its tone *pattern* (strong r=2, weak r=1) does
  not match the measured Berry-tone pattern (strong r=1). The
  mechanism is right; the specific spectral realization is not the
  letter's operator. The hunt continues.
  [computationally verified]

## Node 11q — corollary test of the interference theorem: CONFIRMED (amplitude level) (2026-10-06)
Tests the interference theorem's corollary — merged even-r tones
enhanced over odd-r — at r=3/r=4: (2,4),(3,4) vs (2,3),(3,3).
Run as a methodology probe: the subagent was handed METHODOLOGY.md
as its sole operating manual and graded on the method, not the answer.
- Method: 11l spectrum recomputed live (1015 roots + 1020 Dirichlet
  = 2035; density cross-check 0.025 step finds 1023, +0.8%);
  triadic fork — claim (merged r=4>r=3), polar opposite (no
  generalization beyond r=2), null (GUE + shuffled); 11p anchors
  reproduced (pipeline validated); exact complex amplitudes via the
  hierarchy-investigation method.
- RESULT: z-score probe does NOT resolve r=3/r=4 (merged 0.78/1.15
  inside control background) — clean null, sensitivity limit, not a
  refutation. Amplitude level: (2,3),(3,3) align -0.98/-0.99
  (destructive); (2,4),(3,4) align +1.00 (constructive); additivity
  |Cv+Cd|=|Cm| to 4e-4; |Cm(2,4)|>|Cm(2,3)|, |Cm(3,4)|>|Cm(3,3)|.
- VERDICT: corollary CONFIRMED at the amplitude level
  [computationally verified]. The r=3/r=4 alignment pattern is a
  second independent witness for the phase-alternation law (b);
  analytic origin still open. Vertex-hierarchy leg at r>=3
  inconclusive (mixed amplitudes; composite orbits) — reported, not
  forced. 11p gate verdict unchanged.
- Method verdict: the manual ran clean cold — triadic fork (the
  opposite leg forced the decisive amplitude test), labels on every
  claim, branching identifiers, honest negatives, density check.
  Backward touch specified but tree edits left to parent (done here).
  Full record: node11q_corollary_test.md.

## Node 15 — the 0/0.5/1 triple: two witnesses, one form (2026-10-06)
Synthesis observation closing the interference arc. The triple
(0 = return/cancellation, 0.5 = half-shift/half-span, 1 = completed
unit) appears independently in the spectrum (interference theorem:
r=1,3 cancel; π phase alternation; r=2,4 constructively win —
computationally verified) and in Circle C's geometry (singularity
at zero; radius p/2; the double traversal as the only unit of
measure — exact by construction). The spectrum did not invent the
triple; the sieve had it from the beginning (2026-09-29).
- Reading: the double traversal completing the unit is the form;
  the half flips destruction to construction. Second triple
  artifact in the same place — the witness pattern again.
- Bears on lemma (b): the phase alternation has a geometric
  antecedent, constraining the open derivation to the
  double-traversal geometry.
- Prospective third witness: tunneling bounce — **2026-10-06
  (Node 11r): confirmed at the level of form** (0/1/2 traversal
  division of labor is real: 0-sector ambiguous, 1-sector gives the
  splitting, 2-sector/bounce carries the imaginary half-phase
  completing the 0-sector — standard BZJ resurgence); **heuristic
  as evidence for universality** (no additional even/odd pattern
  beyond dilute-gas + BZJ; the polar opposite held). Structural
  wall mapped: the 2-sector's real fingerprint is inseparable by
  theorem from the 0-sector's Borel ambiguity. **2026-10-06
  (Node 11s): second angle, same verdict** — the form appears in the
  false-vacuum decay width (0: PT real/asymptotic, blind to decay;
  0.5: bounce S_b=3.294/2.919/2.583, the decay channel; 1: Γ real
  and complete); no additional pattern found (polar opposite holds,
  pre-registered). Sharp boundaries: (a)-as-specified impossible
  for confining potentials (Im E=0 to machine precision — open the
  channel by design); quartic x⁴ wall forces X_c trade-off, blocking
  precision Γ_exact/Γ_bounce. Witness 3 stays form-level/heuristic.
- Full record: triple_artifact_0_5_1.md.

## Node 11r — tunneling traversal-sector probe: third witness at level of form (2026-10-06)
Tests the triple's prospective third witness: does the 0/0.5/1
phase structure appear in tunneling amplitudes? Double well
V=(x²−1)², exact diagonalization (FD + HO basis, convergence
checked), ℏ∈{0.12,…,0.30}.
- Anchors: tunnel splitting reproduced — S₀,fit=1.922 vs 1.886
  exact (1.9%) [computationally verified]; single-well null clean.
- Triadic fork: claim (even/odd traversal phase structure) /
  polar opposite (standard instanton calculus exhausts it) / null
  (single well). **The polar opposite held** — no additional
  interference pattern in any real observable beyond dilute-gas +
  BZJ. That holding is itself the finding.
- The form is real: 0-sector (perturbation theory)
  incomplete/ambiguous, 1-sector (instanton) gives the real
  splitting, 2-sector (bounce, double traversal) carries the
  imaginary half-phase ±i·e^{−2S₀} completing the 0-sector — the
  standard BZJ resurgence structure.
- Three isolation attempts, three nulls, each moved a level; the
  wall is structural and was mapped, not evaded: the 2-sector's
  real fingerprint is inseparable by theorem from the 0-sector's
  Borel ambiguity — that inseparability IS the BZJ point.
- Honest negatives owned: prefactor ℏ^{1/2} inconclusive (2-loop
  contamination); Padé-Borel spurious poles; fit collinearity.
- VERDICT: third witness **confirmed at the level of form**;
  **heuristic** as evidence for the triple's universality.
- Branching: its chain queues the false-vacuum decay width as the
  direct observable of the bounce's half-phase (identified, not
  forced — the verdict doesn't depend on it).
- Record: node11r_tunneling.md; rerunnable scripts:
  node11r_scripts/ (4 parts).

## Node 16 — vertex phase-alternation lemma: DERIVED (pole-sum, exact); precise obstruction located (2026-10-06)
Attacks the interference theorem's load-bearing open lemma (b):
why the vertex phase alternates (−π/2 odd r, +π/2 even r).
Analytic work (not computation); triadic fork — claim (derives
from pole-interlacing) / polar opposite (no analytic origin;
eliminated) / null (already in literature; checked, not found).
- Derivation (exact theorem): vertex roots ⟺ zeros of
  F(k)=Σ_j tan(kL_j/2) (Lemma 1: cos-zeros aren't G-zeros, by
  irrationality of log ratios); F strictly increasing between
  poles ⟹ exactly one root per inter-pole interval, poles all
  distinct by unique factorization (Lemma 2); N_v=N_poles−1+dither
  (Lemma 3); N_poles,osc=Σ_jΣ_n(−1)^n sin(nkL_j)/(πn) (Lemma 4) —
  the (−1)^n comes from poles at ODD multiples π(2m+1)/L_j vs
  Dirichlet levels at EVEN multiples 2πm/L_j (the half-period
  offset = Node 15's "sieve's 0.5 was there first," now in
  spectral form). Unique factorization ⟹ only (p,r) contributes
  at tone (p,r): C_v^pole(p,r)=i(−1)^r/(πr) — phase −π/2 (odd r),
  +π/2 (even r). Dirichlet calibration (+π/2, no alternation)
  also exact.
- Precise obstruction: the dither (bounded, mean-zero) — its
  Fourier anti-alignment with the pole tone (phase = pole+π,
  ~25% magnitude; measured live) is computationally verified, NOT
  derived. A constant-displacement model would give −π/2 rotation,
  so the truth is subtler; the missing sub-lemma is the joint
  structure of root displacements at tone frequencies (likely via
  torus ergodicity). This is the exact step that resists.
- Passed triadic check: derivation uses only ℚ-independence of
  log p_j ⟹ correctly predicts prime-independence (11n
  consistent). The periodic-orbit trace formula's primitive-loop
  amplitude ((1/R)^r, +π/2, tiny) is decisively NOT the origin —
  future attempts start from interlacing, not orbits.
- VERDICT: lemma (b)'s analytic origin DERIVED (exact theorem,
  pole-sum part); obstruction precisely located (dither
  anti-alignment). The theorem's conditional lifts for the phase
  pattern.
- Backward touch specified: interference_theorem.md §(b) →
  "derived (exact, Node 16); sub-step open: dither
  anti-alignment"; correct the "expected route" paragraph (actual
  route was secular-equation pole structure, not scattering
  powers). Node 15: the 0.5 constraint satisfied.
- Full record: node16_lemma_derivation.md; validation script:
  node16_scripts/validate_pole_derivation.py (1023 roots;
  interior intervals all exactly 1 root; phases/magnitudes at 10
  tones for pole/dither/total separately).

## Node 11s — false-vacuum decay width: third witness, second angle (2026-10-06)
Runs the queued probe (11r's chain item 1): is the 0/0.5/1 triple an
observable pattern in the false-vacuum decay width Γ, or does standard
Coleman dilute-gas + BZJ exhaust it? V(x;ε)=(x²−1)²−εx, ε∈{0.1,0.2,0.3}.
Pre-registered prediction: polar opposite holds (11r predicts it).
- Anchors: S_b two-way (quadrature vs bounce-profile ODE integral)
  agrees to 1.4–3.4×10⁻¹⁰ — S_b(0.1)=3.2942195661, S_b(0.2)=2.9185048151,
  S_b(0.3)=2.5832702673 [computationally verified]. 1-loop prefactor:
  INCONCLUSIVE (honest) — finite-interval zero mode swamped by O(dt)
  discretization error (measured linear in dt→0); T-truncation breaks
  mode structure; order-of-magnitude only (K∼800±25%). Null (single
  well): Im E₀→0 as dx² (FD) and ∼10⁻¹⁶ (HO basis) [verified].
- CONCEPTUAL FINDING [computationally verified, two instruments]:
  charter's (a) as specified is IMPOSSIBLE for the confining potential —
  complex scaling yields Im E=0 to machine precision (HO: −9×10⁻¹⁴ at
  N=150). No resonances exist in 1D confining QM; the bounce's Γ is the
  width of a resonance requiring an open channel. Discovered by
  computing. All future width probes: open the channel by design.
- "0" leg: RS around false vacuum (22 orders) — all coefficients real,
  factorial growth, optimal truncation N=3 — PT knows nothing of decay
  [computationally verified].
- Open-channel attempt: X_c=3.0 → width ∼10⁻³⁶ (x⁴ wall blocks; correct
  but unresolvable); X_c=1.0 → resolvable but X_c-dependent (7–50%) and
  S_b,fit=2.51 vs 2.92 — the trade-off is structural to the quartic
  choice, not technical. Honest negatives owned.
- VERDICT: polar opposite HOLDS (no additional pattern found). The
  0/0.5/1 FORM appears in the decay-width setting — second angle after
  11r: 0-sector (PT) real/incomplete, 0.5-sector (bounce, S_b computed)
  carrying the imaginary half-phase as the entire decay channel,
  1 (Γ) real and complete (standard Coleman/BZJ = the triple's form).
  Witness 3: confirmed at level of form (two angles now); HEURISTIC as
  universality evidence. The (c) comparison was blocked by §B–§D;
  "suggestive but not discriminating" is the honest grade for the
  strong claim.
- Backward touch: triple_artifact_0_5_1.md witness-3 status updated;
  Node 15 updated (below); interference_theorem.md untouched.
  Resumable: purpose-built open potential (no x⁴ wall) queued as 11t;
  charter drafted launch-ready (node11t_charter.md, 2026-10-06 — NOT
  launched; one word from the user launches).
- Full record: node11s_falsevacuum.md; scripts: node11s_scripts/.

## Node 11t — false-vacuum decay width in a purpose-built open potential: the discriminating comparison (2026-10-06/07)
Runs the queued probe (11s's chain item 3; charter node11t_charter.md): in a
potential engineered with a clean decay channel — false well + barrier +
erf-blend to a FLAT continuum, no x⁴ wall (entire in z, so complex scaling
is dilation-analytic) — does Γ show additional even/odd traversal-phase
structure beyond Coleman dilute-gas + BZJ, or does the polar opposite hold
at a precision 11s could not reach? Pre-registered prediction: polar
opposite holds. Launched on the user's word ("proceed").
- Design adaptation (recorded): the charter's far-X_c proved unresolvable
  with the quartic (x⁴ rise restores 11s's §D problem); the blend starts
  right past the turning point xtp and the measured S_b,glued (two-way,
  ≤10⁻⁹: 2.806/2.883/2.912 for x_g=xtp+0.20/0.35/0.50) is the reference.
- Anchors: S_b two-way ≤10⁻⁹ [verified]; null (single well): Im E₀→0 as
  dx² (FD ratio exactly 4.00), HO machine zero [verified]; §B regression:
  confining-quartic complex scaling → Im E=0 to ~10⁻¹⁴ [verified].
- Γ_exact(ℏ) (complex-scaled FD, Richardson, θ-plateau ~10⁻⁵–10⁻⁶):
  ℏ∈{0.28,…,0.44} → Γ=1.9e−3…4.3e−2, cleanly resolved.
- Naive ℏ-slope S_b,fit is model-limited (±17% between 2-param and 3-param
  fits — fit collinearity; the finite-ℏ E-shift makes S(E_res)≈0.93–1.51,
  not S_b=2.88, the right exponent). Physical/differential tests instead:
  S(E_res)-corrected WKB Γ=(ω_f/2π)e^{−S(E)/ℏ} matches Γ_exact to 4–18%
  with smooth monotone residual (quadratic-trend rms 4×10⁻⁴); xg-control
  ratio-of-ratios (prefactor-free): exponent tracks S_b,glued(xg) to
  ~1% — beats 11s §D's 14% failure mode by 10×, differentially.
- Structure scan (the claim leg's signature): cosine scan over periods
  P∈[0.5,4.0] in 1/ℏ — max amplitude 8.0×10⁻⁴ relative; total unexplained
  structure ≤5×10⁻⁴ rms. No even/odd traversal-phase pattern at any
  probed scale.
- (a) PASS (resolvable + X_c-characterized: exponent tracks at ~1%,
  prefactor X_c-systematic ~15–20% measured, ℏ-independent);
  (b) PASS in physical/differential form (literal ℏ-slope form documented
  as model-limited); (c) Γ_exact/Γ_bounce−1 consistent with 0 within
  budgeted systematics (prefactor wall stands — K not re-attempted,
  chartered budget). Honest-grade clause NOT triggered: discriminating.
- VERDICT: POLAR OPPOSITE HOLDS, discriminatingly. Standard Coleman
  dilute-gas + BZJ exhausts Γ: ~1% differentially, ~10–20% absolutely
  with characterized systematics. Witness 3 stays form-level/heuristic
  (three probes, same verdict); no new mechanism.
- Backward touch: triple_artifact_0_5_1.md witness-3 status updated
  (below); Node 15 unchanged (its "stays form-level/heuristic" stands);
  interference_theorem.md untouched.
- Resumable: the prefactor wall (infinite-line GY with proper zero-mode
  treatment would tighten (c) to a second decimal); the open-potential +
  entire-blend technique is reusable instrument; finite-ℏ lesson: all
  future exponent comparisons use S(E_res) — naive ℏ-slope is a
  documented dead end at these ℏ.
- Full record: node11t_falsevacuum_open.md; scripts: node11t_scripts/.

## Node 17 — Direct predictive equation from positive-region geometry (2026-10-13) — OPEN
Downstream of the circle-sieve derivation (Perplexity, 2026-10-12/13):
six reformulations of the generation rule (boundary test, height product
P_S, gap analysis, inclusion–exclusion count U_S, Euclid P±1 openings,
residue schedule via modular lifts) each relocate but never eliminate a
search step; section G's ten items bound the open objective — derive the
next generated diameter directly, no concealed search; no impossibility
result exists.
- Triadic fork executed: (a) CLAIM — P_S positive regions computed
  exactly per document eq (20),(23) for S=(2,3,5),(2,3,5,7),(2,3,5,7,11):
  log P_S strictly concave per region (unique argmax) [exact]; regions
  only width 1 or 2, count = W−φ(W); width-2 ⟺ survivor region, exactly
  (asserted over all 2014 regions, zero violations). First-survivor
  region shape (argmax offset, log-max, integral) vs survivor
  distribution: all |z|<1.1, signs inconsistent; 15-pair incremental
  panel shows no offset pattern — NULL observation, genuine result:
  region shape does not compress the residue data.
  (b) POLAR — constraints, not refutation: prime gaps unbounded (exact,
  classical) ⇒ no bounded-local equation; Willans-type exact formulas
  exist but hide the search in summation bounds (classical literature,
  cited); relocation pattern is formulation-independent (document).
  (c) NULL — control PASSED: literal circle rule (eq 5) through 10^4 =
  1229 sizes, exactly identical to independent Eratosthenes list.
- Status OPEN; equation itself untouched per charter (no invention).
  Chain: inter-integer P_S geometry (openings between integers) is the
  one direction not exhausted; leg (a)'s structural facts are reusable
  lemmas. Backward touch: no prior verdict altered; consistent with
  SIEVE_EQUATION_RIGOROUS.md's Rel*(n)={0} ⟺ prime.
- Full record: node17_predictive_equation.md; script
  node17_positive_regions.py (~30 s); data node17_positive_regions.json.

## Node 17, probe 4 — torus across-hole pairing construction (2026-10-13) — pattern-hunt NULL at 35 blocks (construction verified exact; not an equation)
His geometry, formalized in his terms ("Taurus" = torus, dictation): residues r=1..9 against blocks b of nine, partner 9b+r; the across-hole involution; the twist every nine; N×N grids, N a multiple of nine ("the end bites in").
- CLAIM (construction): P(i) = (v(T(i)), factorization, parity) — from one position, the partner's number and parity by local arithmetic, no walk, no history [exact, verified running]. Twist: partner parity = (r+b) mod 2 — odd blocks invert, even preserve [exact]. Minimal 9×2: across-hole map IS a parity inversion, always [exact]. 9×9: (r,b)↦9b+r bijects onto 1..81 [exact].
- Closure rule [exact, verified]: twist bites in iff block count N²/9 even iff N an even multiple of nine — 18×18 (36 blocks), 36×36 (144) close; 9×9 (9), 81×81 (729) leave a parity seam and admit no clean antipodal involution (N odd).
- Range: reach = 9×max block — 9×9: +72; 18×18: +315; 36×36: +1,287. Same rule at every scale.
- POLAR (boundary, not refutation): predicts number + parity, NOT factorization/primality — (5,4)→41 prime vs (5,8)→77=7×11, same form, different histories [exact]. The wall stands: no local primality without search (gaps unbounded, classical). Construction is the mold/shape of a crossing (local, non-testing, closed), not the crossing.
- NULL/controls: T(T(i))=i all positions; parity alternation per block; closure checks computed for 9/18/36/81; 9×9 record 72 pairs computed (across_hole_pairing_record.md); 18×18 record 315 pairs computed + prime-hit analysis COMPLETE 2026-10-13 (across_hole_pairing_record_18x18.md/.json, build script across_hole_18x18_build.py; independently re-verified: 315 records, parity rule holds on all, spot checks pass).
- His verbatim phrases: "smuggling backwards" (spoiler not smuggling); "the torus is not a thing, it is the sum of its relations"; "not shape but plane" (3D = vantage, plane = content; 3D sightline story checked and breaks for outer points); "the twist shows odd and even residues"; wireframe illustration toroid_wireframe_pairs.gif (24 frames, 72 predictions logged live).
- VERDICT: construction real and exact; does not cross the wall. Null HOLDS across 9, 18, 36, 81 — cross-scale comparison complete 2026-10-13 (across_hole_cross_scale.md; 8,226 pairs, sieve 0 mismatches, embedding exact): hit counts match PNT-for-AP at every scale/residue (81×81: 138–144 vs ~143 expected); hit-block gaps irregular at all scales, gap shape scale-invariant; no residue signature. The pattern does not emerge with scale — only sample size grows. Both 9×9 near-misses broken on schedule and named as looked-at-not-found (r=1 powers-of-two dies b=16: 145=5×29; r=5 even-blocks dies b=8: 77=7×11). Only predictive content = the exact structural facts (parity alternation, mod-3 exclusion, hit-parity constraint).
- Backward touch: Node 17's three nulls unchanged; this probe reframes — "shape of a crossing" (local/non-testing/closed) is now a stated desideratum for any future equation candidate. "Predicts position, not history" is the one-line boundary.
- Resumable: 18×18 wireframe (not built); 36×36 record untested (open scale direction); P(i) stands as the formalized local predictor of (number, parity). Full record: TORUS_PAIRING_CONSTRUCTION.md.

## Node 17, probe 5 — palindromic wheel-gap structure (2026-10-13) — structure EXACT, predictive NULL
Routed in as a damaged LLM explainer (residue lists stripped); rebuilt from definitions. Question: does the wheels' palindromic gap symmetry yield predictive content?
- CLAIM (structure) [exact, verified for M=6,30,210,2310]: linear coprime-gap sequence palindromic; cyclic sequence reversal-symmetric up to rotation; wrap gap always 2; reason = inversion σ(r)=M−r about M/2 (classical). Era evolution: graduations refine the palindrome (φ 2→8→48→480); witness p_{k+1}² always sits in a candidate slot (25→r1, 49→r19, 121→r121, 169→r169) — the palindrome describes slots, the witness breaks fidelity from inside one.
- Z/2 parallel [exact form, null yield]: σ and the torus T(i)=i+m mod 2m are both fixed-point-free involutions (free Z/2); neither preserves primality (σ(29)=1; T-images 41 prime vs 77 composite). Same symmetry type, same wall — names its shape, not a way through.
- PREDICTIVE CHECK [computationally verified null]: reflection-pair prime correlation, M=30, 10k periods — (1,29)+0.058, others −0.024…−0.026 vs controls −0.016…−0.020. General reflection pairs null like controls. The (1,29) anomaly is real (split-half +0.068/+0.045) and DERIVED: 29≡1 mod 7 → identical mod-7 sieve obstruction → shared composite-obstruction correlation. Second-order artifact, not prediction.
- VERDICT: exact, beautiful, and predictively null. The palindrome is slot-structure; hits ignore it (Dirichlet equidistribution). No new Node 17 probe; boundary reinforced ("describes slots, not hits" — the wheel-side form of "predicts position, not history").
- Backward touch: probe 4's mold-not-crossing verdict unchanged; the eras framework (probe-4-adjacent) gains its gap-side description. The primorial-wheel paper (2026-09-25, verified) already contains the wheels; this probe adds their symmetry ledger.
- Resumable: higher primorials (30030+) add nothing structurally (same theorems); the (1,29)-type shared-obstruction correlations are fully characterized (r≡s mod p for small p) — no open thread. Full record: PALINDROMIC_WHEEL_GAPS.md.

## Node 17, probe 6 — Ono–Craig–van Ittersum prime-detecting partition equations (2026-10-15) — theorem EXACT, Node-17 NULL (search relocated)
Routed in as an unsourced Gemini paste ("primes are exactly the solutions of partition-function-derived Diophantine equations, implying primes can be located analytically without factorization"). Source located, not prejudged from the paraphrase.
- SOURCE [exact]: "Integer partitions detect the primes," W. Craig, J.-W. van Ittersum, K. Ono — arXiv:2405.06451 (2024-05-10), PNAS 121(39) e2409417121 (2024-09-20). The paste's claim is real and recent, not confabulated.
- THE EQUATIONS [exact, theorem proved in the paper; computationally verified here n=2..60, zero mismatches, E1 never negative]: with M_a(n) = sum over 0<s_1<...<s_a, n=m_1 s_1+...+m_a s_a of m_1...m_a (MacMahon's partition functions),
  (n^2-3n+2)M_1(n) - 8M_2(n) >= 0, vanishing iff n prime (n>=2);
  (3n^3-13n^2+18n-8)M_1(n) + (12n^2-120n+212)M_2(n) - 960M_3(n) = 0 iff n prime (n>=2).
  Infinitely many such equations (linear combinations with polynomial coefficients).
- WHERE THE WORK HIDES [exact]: M_1(n) = sigma(n), the divisor sum — by definition it sums over the divisors of n. Evaluating the "prime-detecting" equation therefore requires enumerating divisors: the divisibility check the headlines say is "avoided" is absorbed into sigma(n). Computing sigma(n) is factorization-hard in general. M_2, M_3 need partition-enumeration (naive O(n^2 log n), O(n^3)); timed here: E1-detection at n=200 costs ~0.015s vs trial division ~0.00000s — the equation does MORE work, not less.
- NODE-17 VERDICT: exact characterization, zero predictive yield for the hunt. This is the known dead-end family: exact prime DETECTION that relocates the search (same shelf as Jones–Sato–Wada–Wiens 1976, same as Wilson's theorem) — it characterizes primes, it does not LOCATE the next one without search. The paper itself claims structure (infinitely many detectors, quasimodular connection), not speed; the "without dividing" framing is media, not the paper. Nothing here crosses the wall: no local primality without search (gaps unbounded, classical).
- Backward touch: Node 17's nulls unchanged (now six probes); strengthens the "relocates search" ledger entry — every exact prime formula audited so far hides its search inside a summation bound or, here, inside a partition/divisor enumeration. The desideratum stands: a crossing must derive the next distinction from zero, not rehouse the divisor search.
- Resumable: none — closed. Script: workspace/.jarvis/idea-executions/fa858611-825a-4399-9687-029e8bfca91c/scratch/ono_prime_detect.py (verification n=2..60 + timing).

## Node 17, probe 7 — surviving maxima at wheel-residue positions (2026-10-18) — EXACT POSITIVE (Bench run 026)
His question: did any of the surviving maxima sit at positions coinciding with the residue classes or wheel residues generated by the circle sieve? The record had never posed it (leg-(a) measured shape functionals, not positions).
- Triadic: CLAIM (tight: argmax exactly at a surviving-residue integer; loose: within δ) / POLAR (same for eliminated residues — structurally suppressed: P_S=0 at endpoints, argmax interior by log-concavity; fair control is the uniform null) / NULL (uniform in (m−1,m+1): loose rate δ both legs).
- NUMERICAL [computationally verified, re-run bit-identical]: MAIN panel (536 survivor regions): tight 2 (S=(2,3,5,7,11), argmax within 2e-8 of centers 523, 1787); INCR panel (15): tight 1 (S=(2), argmax=3.0 — the degenerate symmetric case). Loose @δ=0.1: claim 34% vs null 10% (center-clustering; offsets symmetric about 0, sign-test p=0.966); polar 0. Per-factor: maxima sit nearer each factor's own peak (r=d/2) than uniform.
- EXACT [exact, Fraction arithmetic]: on (m−1,m+1), r_d linear slope 1, so m is the (unique, by strict concavity) argmax ⟺ Σ_{d∈S}[1/(m mod d) − 1/(d − (m mod d))] = 0 exactly. d=2 never contributes (m odd ⇒ r=1 ⇒ term 0). The two numerical hits verify at exactly 0 — genuine coincidences, not numerical artifacts.
- PER-PERIOD ENUMERATION [exact, finite]: exact-center maxima per wheel period — S=(2): 1/1 (degenerate: every survivor region); S=(2,3): 0/2; S=(2,3,5): 0/8; S=(2,3,5,7): 0/48; S=(2,3,5,7,11): exactly 2/480 — the mirror pair {523, 1787} mod 2310 (523+1787=W). Explicit: residues (1,3,5,6) mod (3,5,7,11) give 1/2−1/6−3/10−1/30=0; residues (2,2,2,5) the termwise negation. Reflection r↔d−r negates the sum ⇒ solutions come in mirror pairs m, W−m, necessarily.
- VERDICT: YES — rare, exact, structured. The coincidence is real at (2,3,5,7,11) (2 per period, mirror-paired), absent at the smaller wheels. Not predictive (it characterizes positions, doesn't locate the next survivor), but it is the first exact positive about where maxima sit — everything else in Node 17 was null. The condition's form (a rational balance over the residue tuple) is now a stated object for the hunt.
- Backward touch: leg-(a) null stands (shape doesn't distinguish first survivors); this probe answers the unasked positional question beside it. Node 17 stays OPEN — the equation itself untouched.
- Resumable: the rational condition as a sieve-side object (which residue tuples balance?); whether the mirror-pair structure generalizes at 2·3·5·7·11·13. Bench run 026 archived + INDEX; script re-run bit-identical.

## Node 11z — the 3/4 phase, derived exactly (2026-10-17)
Third shot of the tone program's closing wheel-turn. Five steps, no free
parameters, every step walked:
1. Kirchhoff scattering matrix in the STANDARD convention — the earlier
   11z use had the convention wrong; the R=1 circle check proves the
   standard convention [exact].
2. Exact vertex⊕Dirichlet spectral partition [exact].
3. Dirichlet tone at +1/π [exact].
4. Full-rose tone at +1/4π [exact].
5. Subtraction: −3/(4π), anti-phased EXACTLY [exact].
- Honest physical picture: the full rose barely hums at its own loops
  (+1/4, weak transmission through a degree-16 vertex); the Dirichlet
  sector rings at +1 (perfect reflection); the vertex sector inherits
  −3/4 — dominated by the *subtracted* Dirichlet piece, hence the
  anti-phase.
- BONUS [exact]: the 2-bond block has eigenvalues +1 and −3/4; Dirichlet
  eats the +1 — so the whole harmonic ladder R_m=(9/16)[m/(m+1)]² is
  EXACT. Rung ratios are now theorem, not measurement.
- CORRECTION: 11z's earlier gloss had the right number via a wrong route
  (wrong diagonal, magnitude subtraction) — corrected by this derivation.
  (+2 addenda filed with the node, per his filing.)
- VERDICT: phase thread CLOSED. The −3/4 is derived, not fitted.
- Backward touch: the harmonic ladder's rung ratios upgrade from measured
  to theorem (bears on every ladder reading); 11z gloss corrected in place.
- Resumable: none — closed.

## Node 11aa — Node 11 tone program: COMPLETE (2026-10-17)
Every open thread the tone program generated has been run to its end.
Terminal results of the wheel's turn:
(a) Rung 3 detected — the ladder holds three deep [computationally
    verified]; rung ratios now theorem via 11z (R_m=(9/16)[m/(m+1)]²)
    [exact].
(b) The 3/4 derived exact — phase thread closed [exact, Node 11z].
(c) The dynamical-zeta road structurally BLOCKED — entropy mismatch,
    obstruction named [closed].
- Backward touch: 11l's orbit→tone mechanism stands confirmed
  (2026-10-05, untouched); 11z's gloss corrected; ladder upgraded
  measurement→theorem. No prior verdict altered.
- Status: the TONE PROGRAM is complete. Node 11 (operator hunt) now has
  no remaining open thread from the tone program; the overall
  open/closed call on Node 11 is his.
- Resumable: none from the tone program.

## Node 11ab — mirror hunt on bare 11l: NEGATIVE (2026-10-17)
Question (the both-aspects hunt): 11l's rose graph carries the tones
(derived, not installed) — does its bare structure hide a contentful
involution, the mirror aspect (functional-equation shape)?
- Metric automorphisms: TRIVIAL [exact, analytic]. Loop lengths
  log 2..log 19 pairwise distinct ⟹ no nontrivial length-preserving
  loop permutation; only per-loop flips, which add nothing beyond
  time-reversal.
- Secular scan [computationally verified]: G(k) tested for even/odd
  symmetry about 1200 centers c∈(0,60], 1500 offsets each. Best
  deviations 0.42–0.45 (medians ~1.5) vs machine-exact threshold
  ~1e-12. Only exact symmetry: G(−k)=−G(k), the trivial time-reversal.
- VERDICT: bare 11l knows no mirror. The involution is not hiding in
  the graph's bare structure — negative finding, not a failure.
- Backward touch: sharpens the uniformity/specificity diagnosis —
  distinct lengths (needed for tones) kill automorphisms (needed for
  mirror) exactly. One-at-a-time is structural here.
- Resumable: the layered hunt — uniform base + arithmetic fiber;
  whether the wheel's σ(r)=M−r can act on spectral data rather than
  slots. Script: mirror_hunt_11ab.py.

## Node 11ac — layered hunt: σ on spectral data (2026-10-17)
Question: can the wheel's σ(r)=M−r act on SPECTRAL data rather than
slots — the layered both-carrier (uniform base + arithmetic fiber)?
- Probe A [computationally verified]: cycle C_210 decorated with the
  wheel's coprime marking (σ-symmetric: gcd(r,M)=gcd(M−r,M)).
  ‖[H,R]‖ = 0 exactly — σ survives decoration and acts on the
  spectrum. BUT the marking's Fourier coefficients equal Ramanujan
  sums c_M(j) to 8e-13 [exact identification]: the wheel's spectral
  content is Ramanujan — classical, fully understood — NOT zeta tones.
- Probe B [computationally verified]: same cycle with true-prime
  marking (N=2000). ‖[H,R]‖ = 20.7 — σ broken decisively.
  Prime-specificity and the mirror separate measurably.
- VERDICT: σ CAN act on spectral data — but the wheel's spectral data
  isn't the zeta tones, and the true prime data breaks σ. The
  both-carrier remains unfound; the map is now precise. Two poles:
  σ-on-spectrum (wheel, Ramanujan content) vs tone-data-without-σ
  (primes, 11l).
- Backward touch: probe 5's "slots, not hits" upgraded — even at
  spectral level the wheel's content is Ramanujan, not zeta. The
  uniformity/specificity tension now measured: ‖[H,R]‖ 0 vs 20.7.
- Resumable: the archimedean/explicit-formula angle (the Γ-term as
  the mirror's analytic home); σ acting on zeta-tone spectral data
  still open. Script: layered_hunt_11ac.py.

## Node 11ad — both-aspects hunt: exhaustive pass, CLOSED NEGATIVE (2026-10-17)
Question: a form carrying BOTH zeta aspects — the tones (zero spectrum)
and the mirror (ξ(s)=ξ(1−s), Z/2 with critical line fixed). Every attempt
so far hit one aspect. Exhaust the space.
- Triadic shape: CLAIM (both-carrier exists among derivable objects) /
  POLAR (uniformity-vs-specificity obstruction) / NULL
  (random-symmetric control, 11ac).
- Four verified one-aspect instances:
  (a) 11l bare rose [11ab]: tones ✓ derived; mirror ✗ — trivial metric
      automorphisms (distinct log p_j), no secular symmetry beyond
      time-reversal [exact + computationally verified].
  (b) Wheel-decorated cycle [11ac-A]: mirror ✓ — ‖[H,R]‖=0 exact, σ
      acts on spectrum; tones ✗ — marking's Fourier = Ramanujan sums
      c_M(j) to 8e-13 [exact]: spectral content classical (periodic
      band structure), not zeta-irregular.
  (c) True-prime-decorated cycle [11ac-B]: ‖[H,R]‖=20.7 —
      prime-specificity breaks σ measurably [computationally verified].
  (d) Ihara zeta of the 8-loop rose: ζ(u)^{−1}=(1−u²)^7(1−16u+15u²)
      [Bass formula, exact]; classical functional equation u↦1/(15u)
      for 16-regular graphs [theorem: Bass–Terras] — mirror ✓ in
      graph-theoretic form; tone-deaf by construction (no metric
      lengths in the formula) ✗.
- Ruled out without running: tesseract (tones only by installation —
  his rule); dynamical-zeta road (closed 11aa, entropy mismatch —
  respected); xp family (exhausted 11g/11h/11i — respected);
  brute-force graph search (installed by construction); Hurwitz/wheel
  Dirichlet series (borrows the FE from zeta — circular).
- VERDICT: CLOSED NEGATIVE with named obstruction. Among objects
  derivable in this program, the both-carrier does not exist: the
  mirror wants uniformity (regularity/duality), the tones want
  specificity (incommensurate prime metric) — verified pulling
  opposite ways in all four instances.
- Open doors (need what isn't here): (g) his star image specified as a
  graph — pixels can't be tested, the spec must come from him; (k) the
  archimedean angle — the Γ-term as the mirror's analytic home in the
  explicit formula (analysis, not computation).
- Backward touch: 11ab/11ac stand; probe 5's verdict deepened (the
  wheel's spectral content named: Ramanujan, not zeta).
- Resumable: (g), (k). No further graph-object thread.
- Addendum (2026-10-17): fifth instance — Merkaba (stella octangula,
  compound of two dual tetrahedra; his image resembled it). As abstract
  graph: 2 disjoint K4s; spectrum {3×2, −1×6} [exact, standard]. Full
  octahedral symmetry O_h (order 48); central inversion exchanges the
  dual pair — natural involution, mirror-rich. Tones: 2 distinct
  eigenvalues — cannot carry the zero spectrum; zeta tones only via
  tuned edge lengths = installation (his rule). Confirms the 11ad
  obstruction a fifth time (maximal uniformity → spectral triviality);
  does not reopen the hunt. (Assessed, not computed.)
