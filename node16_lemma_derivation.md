# Node 16 — Derivation of the vertex phase-alternation lemma

**Date:** 2026-10-06
**Question:** Why does the vertex sector's Fourier phase alternate
(−π/2 at odd r, +π/2 at even r)? Derive it or pinpoint exactly
where the derivation resists.

## Prediction (stated before computing)

Per the manual's "winner before it wins" rule and Node 15's
constraint (the derivation must come from the double-traversal
geometry, not probe conventions): the vertex roots interlace the
poles of F(k)=Σ_j tan(kL_j/2); the poles sit at *odd* multiples
π(2m+1)/L_j while Dirichlet levels sit at *even* multiples
2πm/L_j; the half-period offset should Fourier-transform to the
(−1)^n alternation, i.e. the π phase flip. If this route is right,
the pole-sum alone must give phase −π/2 (odd r), +π/2 (even r)
with |C| = 1/(πr).

## Triadic fork

1. **Claim:** the alternation derives analytically from
   pole-interlacing (route above).
2. **Polar opposite:** the alternation has no analytic origin in
   the graph (probe artifact or irreducible numerics) — eliminated:
   the pole sum yields it exactly, and the 11n random-loop control
   is consistent (the derivation uses only incommensurability, so
   it correctly predicts prime-independence).
3. **Null:** the result already exists in the literature — checked:
   not found under an obvious name. Ingredients are standard
   (Kottos–Smilansky trace formula; rose secular equation), but the
   phase consequence at prime-log tone frequencies is original to
   this work.

## Derivation (exact theorem)

Setup: Kirchhoff rose, R loops, L_j = log p_j (distinct primes),
vertex sector = {k>0 : G(k)=0},
G(k) = Σ_j sin(kL_j/2)·Π_{i≠j}cos(kL_i/2).

**Lemma 1.** Zeros of G (k>0) coincide exactly with zeros of
F(k) := Σ_j tan(kL_j/2).
*Proof.* G = (Π_i cos(kL_i/2))·F. If cos(k₀L_m/2)=0 for some m,
then k₀L_m/2 = π/2+πb; for i≠m, cos(k₀L_i/2)=0 would require
L_i/L_m = (2a+1)/(2b+1) rational, but log p_i/log p_m is
irrational for i≠m (else p_i^b=p_m^a). Hence exactly one cosine
vanishes, sin(k₀L_m/2)=±1, and G(k₀)=±Π_{i≠m}cos(k₀L_i/2)≠0.
So Πcos-zeros are not G-zeros, and G-zeros ⟺ F-zeros. ∎

**Lemma 2.** All poles of F are simple and distinct; F is strictly
increasing between consecutive poles, hence has exactly one zero in
each inter-pole interval.
*Proof.* Poles at k=π(2m+1)/L_j. Coincidence
π(2m+1)/L_j=π(2m'+1)/L_i gives (2m+1)/(2m'+1)=log p_j/log p_i,
irrational for i≠j; for i=j forces m=m'. So all poles simple and
distinct. F'(k)=Σ_j(L_j/2)sec²(kL_j/2)>0. At the left end of each
inter-pole interval F→−∞, at the right end F→+∞; continuous and
strictly increasing ⟹ exactly one zero. (On (0,p₁): F(0)=0,
F'>0 just right of 0, so no positive root before p₁.) ∎

**Lemma 3.** N_v(k) := #{vertex roots ≤ k} satisfies
N_v(k) = N_poles(k) − 1 + δ(k), δ(k)∈{0,1},
where N_poles(k)=Σ_j⌊(kL_j/π+1)/2⌋ counts F's poles.
*Proof.* Poles p₁<p₂<…, roots r_n∈(p_n,p_{n+1}) by Lemma 2. For
p_N≤k<p_{N+1}: r_1,…,r_{N−1}≤k always, r_N≤k iff r_N≤k, r_n>k
for n≥N+1. Hence N_v=(N−1)+1_{r_N≤k} with N=N_poles(k). ∎

**Lemma 4 (the alternation).** The oscillatory part of N_poles is
  N_poles,osc(k) = Σ_j Σ_{n≥1} (−1)^n·sin(nkL_j)/(πn),
hence at tone frequency f=r·log p/(2π) the pole-sum contributes
  C_v^pole(p,r) = i·(−1)^r/(πr),
i.e. phase −π/2 for odd r, +π/2 for even r, |C|=1/(πr).
*Proof.* ⌊x⌋=x−{x}; {x}=1/2−Σ_{n≥1}sin(2πnx)/(πn).
N_poles=Σ_j[(kL_j/π+1)/2−{(kL_j/π+1)/2}]
 = k·Ltot/(2π)+Σ_jΣ_n(−1)^n sin(nkL_j)/(πn),
using sin(nkL_j+nπ)=(−1)^n sin(nkL_j). The smooth part is
kLtot/(2π); the rest is the displayed oscillatory sum. At tone
(p,r): n·log p_j=r·log p forces j=p (p_j=p), n=r, by unique prime
factorization (log p_j are ℚ-linearly independent). The probe
convention (A·sin(2πfk)→+iA, calibrated on the Dirichlet sector)
gives C=i(−1)^r/(πr). ∎

**Corollary (Dirichlet calibration).** N_d(k)=Σ_j⌊kL_j/(2π)⌋ gives
N_d,osc=+Σ_jΣ_n sin(nkL_j)/(πn) — no (−1)^n, since Dirichlet levels
sit at *even* multiples 2πm/L_j. Hence phase +π/2 at all r,
|Cd|=1/(πr). The half-period offset between the two sectors'
singular sets (odd vs even multiples) is the analytic origin of
the alternation. This is Node 15's "sieve's 0.5 was there first,"
now in spectral form.

## The precise obstruction

Lemma 4 gives the *pole-sum* phase. The full vertex amplitude is
C_v = C_v^pole + C_v^dither, where the dither δ−δ̄ is bounded and
mean-zero (Lemma 3). What resists: proving analytically that the
dither's Fourier coefficient at tone frequencies is anti-aligned
with (hence does not rotate) the pole-sum tone.

Measured (live validation, `node16_scripts/`):
- C_v^pole has exactly the predicted phase/magnitude (1/(πr)).
- C_v^dither is anti-aligned (phase = pole phase + π, to
  measurement precision) with magnitude ~25% of the pole term.
- Hence arg(C_v)=arg(C_v^pole) exactly (collinear subtraction) —
  this is why the measured alignment is ±1.00.
- The anti-alignment itself is **computationally verified, not
  derived**. A constant-displacement model would give −π/2
  rotation, not π — so the truth is subtler; the joint structure
  of root displacements {d_n=r_n−p_n} at tone frequencies is the
  exact missing sub-lemma. Proving it likely requires
  equidistribution of normalized root positions via torus
  ergodicity (F(k)=0 as a hypersurface condition on
  (kL_1/2,…,kL_R/2)∈𝕋^R).

## Verdict

**Lemma (b)'s analytic origin is DERIVED — exact theorem for the
pole-sum part** (Lemmas 1–4 above); **the dither anti-alignment is
the precise obstruction** (computationally verified, not derived).
The theorem's conditional lifts for the phase pattern; the
remaining open sub-step is narrowly and precisely located. The
derivation uses only incommensurability of the L_j — hence
correctly predicts the effect is prime-independent (11n
consistent), a passed triadic check.

## Epistemic labels

- Lemmas 1–4 (interlacing, pole Fourier, unique-factorization
  selection, alternating phase): **exact theorem**.
- Dirichlet calibration (+π/2, no alternation): **exact theorem**.
- Dither anti-alignment (phase = pole+π, ~25% magnitude):
  **computationally verified** — the obstruction, not derived.
- Literature: phase consequence **not found** (ingredients
  standard: Kottos–Smilansky; rose secular equation).
- Prime-independence prediction: **exact theorem** (uses only
  ℚ-independence of log p_j); 11n consistency noted.

## Branching identifiers

- **Why it ends here:** the analytic origin is derived
  (pole-interlacing → (−1)^n → alternating phase); the exact
  resisting step is pinpointed (dither anti-alignment). The
  objective — derive or precisely locate the obstruction — is
  complete.
- **Its own chain:** (1) the dither sub-lemma is now a
  precisely-posed problem (prove FT[dither] anti-aligned via root-
  position equidistribution); (2) the "0.5 mechanism" (odd/even
  pole offset) is portable to any Kirchhoff rose with
  incommensurable lengths; (3) the periodic-orbit trace formula's
  primitive-loop amplitude ((1/R)^r, phase +π/2, tiny) is
  decisively NOT the origin — the secular-equation route is;
  future attempts must start from interlacing, not orbits.

## Backward touch (specified; parent's files)

- `interference_theorem.md` §(b): status → "derived: pole-
  interlacing gives the alternation (exact theorem, Node 16);
  remaining sub-step: dither anti-alignment (computationally
  verified, not derived)." The "expected analytic route" paragraph
  (vertex scattering factor) should be corrected — the actual
  route was the secular-equation pole structure, not scattering
  powers.
- Node 15: the "0.5" now has its spectral mechanism (odd/even
  pole offset); the constraint it placed ("derive from the
  double-traversal geometry") is satisfied in the sense that the
  half-period offset is the geometric content.
- 11p/11l: unchanged (mechanism and gate verdicts stand).

## Validation

`node16_scripts/validate_pole_derivation.py` (rerunnable):
recomputes 1023 vertex roots; verifies poles distinct (min gap
9.6e−4), one root per inter-pole interval (interior), dither in
{0,1} with mean 0.502; Fourier phases/magnitudes at 10 tone
frequencies for pole sum / dither / total separately. Note: the
script's probe convention is the complex conjugate of the
investigation's — flip all phase signs when comparing (documented
in-script).
