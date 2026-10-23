# Tones → Sign Changes: Investigation

**Date:** 2026-10-05
**Status:** background investigation — speculative structural question, answered.
**Question:** Can Berry-tone amplitudes at prime-power frequencies
f = r·log(p)/(2π) imply forced sign changes of the Hardy Z-function
Z(t), or feed into a Selberg-type argument for zeros on the critical
line?

**Verdict: no clean connection — dead end for the direct question,
with the mechanism identified.** Three structural barriers, each
stated precisely below. Two nearby live connections are recorded
(§4) showing what *does* work, so the negative is informative rather
than dismissive. A boundary-probing test is sketched (§5).

Honest boundary: the Pearce-Crump preprint was assessed from its
abstract and the exposition of Selberg's method in the search
results, not from a full reading of the paper. The structural
analysis (§2–§3) is the investigator's own.

---

## 1. What the literature establishes

### 1a. Selberg's sign-change architecture — *exact theorem*

Z(t), Hardy's function, is real-valued on the real line; its real
zeros are exactly the ordinates of zeta zeros on the critical line.
A sign change of Z(t) forces a critical zero of odd order. Selberg's
device: multiply by |M(½+it)|², M a Dirichlet-polynomial mollifier.
Since |M|² ≥ 0, the product keeps Z(t)'s sign changes (M's zeros are
of even order, harmless). The gain is analytic: the mollifier
flattens Z(t)'s large fluctuations, sharpening the mean-value
inequalities that turn average size into a sign-change count. A
second moment of the mollified detector, via Jensen's inequality,
yields a *positive proportion* of sign changes: N₀(T) ≫ T log T.
The proportion is governed by the mean value of the mollified
detector — a purely arithmetic quantity in the mollifier
coefficients. (Source: Pearce-Crump, arXiv:2609.15329, §1.1
exposition; standard.)

Pearce-Crump's contribution (Sept 2026): revived Zhuravlev's 1974
quantitative form (Russian, little known in the West), corrected its
errors, optimized the arithmetic mean value (exact closed form for
reciprocal-square-root coefficients; further improved by a
positive-semidefinite family of mollifiers) → 7%, the strongest
result from Selberg's method. *Exact: the paper's claim as stated in
its abstract.*

### 1b. Tones in pair correlation — *exact theorem (formulas)*

Berry–Keating (and Berry's 1980s work): the pair correlation splits
as R(x) = R_GUE(x) + R_c(x), where R_c carries prime-orbit
oscillations — the tones. The zero-density fluctuation is
d_osc(T) = −(1/π)Σ_pΣ_r (log p / p^{r/2})·cos(rT log p) (diagonal
approximation). These are *statistical* statements about the
ensemble/average behavior of zero spacings and densities.
*Exact: the formulas as derived; the diagonal approximation itself
is heuristic.*

### 1c. Statistics → individual zero properties — *exact theorems,
but not via tones*

- **Montgomery (1973):** assuming RH + pair-correlation conjecture,
  at least 2/3 of zeros are simple. The argument uses pair
  correlation at *zero separation* (the diagonal: multiple zeros
  create excess coincident pairs, contradicting level repulsion).
  *Exact theorem.*
- **Gallagher–Mueller (1978):** PCC ⟹ 100% of zeros simple,
  unconditionally on RH. *Exact theorem.*
- **Alpöge–Furman; Lamzouri:** unconditional versions via the
  unconditional pair-correlation formula. *Exact, recent.*
- **arXiv:2503.15449 (preprint, v4 Mar 2026):** claims PCC ⟹
  asymptotically 100% of zeros are simple *and on the critical
  line*, via Gallagher–Mueller's method plus "symmetric diagonal
  zeros." *Preprint; conditional on the unproven PCC.*

Crucial observation: every "statistics → location" result in the
literature uses the **GUE main term** (level repulsion, diagonal
behavior), **never the prime-orbit tone corrections**. The tones are
a refinement that no location-result uses.

### 1d. Negative literature finding

**No published result connects prime-orbit tones to individual zero
locations, let alone to sign changes of Z(t).** The search covered
Montgomery, Berry/Keating, Hejhal, Bogomolny–Keating, and recent
preprints. The tones live in the correction term R_c; the
location-results live in the main term R_GUE. *Finding, not theorem —
absence of evidence, stated as such.*

---

## 2. Structural analysis: three barriers

### Barrier 1 — Two-point vs one-point (type mismatch)

*Status: exact, structural.*

Tones are **two-point** information: pair correlation R₂(x) is the
covariance of zero positions; N_osc(T) describes the fluctuation of
the zero *set*. Selberg's sign changes need **one-point**
information: the actual values Z(t₁) > 0 > Z(t₂) at specific points,
whence a zero by continuity.

There is no mathematical path from a two-point covariance to
pointwise lower bounds. Knowing that zeros cluster with period
2π/(r log p) says nothing about Z(t)'s sign between any two
consecutive zeros — a high-density region is compatible with Z(t)
touching zero (even order, no sign change) throughout. The tone
amplitudes constrain the *distribution*; sign changes require the
*function*. This is not a technical gap; it is a type error.

### Barrier 2 — Circularity of input

*Status: analysis (structural).*

Tones — measured (user's diagonal-approximation work, 11l/11p) or
theoretical (Berry–Keating R_c) — describe the distribution of zeros
*along the line*. Selberg's method *proves* zeros are on the line.
Feeding tone data into a Selberg-type argument would presuppose the
conclusion: the tones are meaningful as on-line phenomena only
insofar as the zeros are already known (or assumed) to be there.

The theoretical tones do not escape this: the diagonal
approximation is derived from the explicit formula without assuming
RH, but it remains a statement about zero *statistics*, and
extracting "forced sign changes" from it would still require the
pointwise control of Barrier 1.

### Barrier 3 — Selberg's mean value is zero-free by design

*Status: exact, given the method's architecture.*

The arithmetic heart Pearce-Crump optimizes — the second moment of
Y_U(s) = ζ(s)M_U(s)M_U(1−s) — is evaluated by Dirichlet-polynomial
mean-value theorems as a **purely arithmetic** expression in the
mollifier coefficients b_n. **No zero input enters.** The zeros
appear only at the final step, via Jensen's inequality turning the
mean value into a sign-change count.

Tone information is *about zeros*. It therefore cannot enter the
mean value — there is no slot for it. Inserting zero data would
destroy the unconditionality that is the method's entire point.
This is structural, not a matter of finding a cleverer estimate:
the architecture is ARITHMETIC (zero-free) → ANALYSIS (Jensen) →
ZEROS. Tones belong to the output side; they cannot be fed back
into the input side.

*Corollary:* the same holds for Levinson's method (also
μ-mollifier-based, also arithmetic mean values). The barrier is
not specific to Selberg's sign-change formulation.

---

## 3. The mollifier angle: three roles of μ, no channel

μ appears in three places, in three irreducibly different roles:

| Context | Role of μ | Status |
|---|---|---|
| Selberg/Levinson/Pearce-Crump mollifier: b_n ∝ μ(n)·(smoothing) | **Tool** — the analyst's choice; M(s) ≈ 1/ζ(s) = Σμ(n)n^{−s} flattens ζ | exact |
| Tones via Λ = μ∗log | **Data** — inherent in the primes; the explicit formula's weights are Λ | exact theorem |
| Node 10c: λ* = μ minimizes the face-complex quadratic form | **Structural optimizer** — inclusion-exclusion weights | exact theorem |

**Deep unity (analysis):** μ is the Dirichlet inversion operator —
the inverse of ζ under Dirichlet convolution. Everywhere the task
is "undo multiplicative accumulation to get clean signal," μ is
forced. This is why it recurs: not coincidence, but μ's universal
role. *Heuristic as a unifying claim; exact in each instance.*

**No channel (analysis, with exact core):** tone amplitudes cannot
improve the mollifier because the mollifier optimization —
max_b Q(b) for Pearce-Crump's arithmetic quadratic form Q — is
determined by the *form*, and the form is zero-free (Barrier 3).
Tone data is zero data. The two μ-optimizations (Pearce-Crump's
maximization; 10c's minimization at λ*=μ) are formally similar —
"extremize an arithmetic quadratic form over μ-weighted
coefficients" — but they optimize different forms over different
variables, and neither admits tone input. The resonance is a shared
symmetry (μ = inversion), not a shared channel.

*Even conditionally*, the path fails: assume the tone amplitudes as
given — Barriers 1 and 2 still block any route to pointwise Z(t)
control. The obstruction is not about unconditionality.

---

## 4. Nearby live connections — what *does* work

Two results show the correct shape of a "prime oscillations →
zeros" bridge, and neither goes through Selberg:

**(a) Montgomery's simplicity program (§1c).** Statistics *can*
constrain individual zero properties — but via the GUE main term at
zero separation (level repulsion vs. coincident pairs), not via
tones. This is the template for what a successful
statistics→location argument looks like. *Exact theorems.*

**(b) The 10a prime-side detector (user's own, 2026-09-30).**
"Built the prime-side zero detector h_{T0,w}… the oscillatory prime
sum goes negative exactly when a zero is in the window." Here prime
oscillations *do* imply zero presence — via the explicit formula as
a detector (resonance mechanism), not via Z(t) sign changes. This
is the project's own positive instance of the question's *spirit*:
prime-side oscillations carrying zero information. But it detects
zeros; it does not prove them onto the line via sign changes.
*Computationally verified.*

The contrast is instructive: (b) works because the explicit formula
is an *identity* linking prime sums to zero sums — no pointwise
control needed. Selberg needs pointwise control, which identities
about sums cannot supply.

---

## 5. Proposed boundary test

If the project wants to probe Barrier 1 empirically rather than
accept the structural argument, the honest test is:

**Test:** Compute Z(t) on [T, 2T] for large T (Odlyzko-quality data
or direct computation). Measure (a) local sign-change density of
Z(t) in sliding windows, and (b) local tone strength at (p,r) via
windowed Lomb–Scargle of N_osc in the same windows. Null model:
sign-change density predicted by mean zero density alone. Question:
does local tone strength predict sign-change density *beyond* the
null?

**Prediction:** no — mechanism: Barrier 1 (two-point information
cannot improve on one-point prediction beyond what the density
already gives). A positive result would be evidence of a channel
the structural analysis misses, and would be worth following up.

**Caveats:** tone amplitude is naturally global; windowing
introduces artifacts; the null must be constructed carefully.
Fiddly but well-posed. *Not run — proposed.*

A cleaner **literature check** (no computation): verify that
arXiv:2503.15449's "PCC → 100% critical" argument uses only the
GUE main term and diagonal behavior, not the tone corrections.
The abstract's stated ingredients ("Gallagher and Mueller's
method and symmetric diagonal zeros") already indicate this.
*Analysis of the abstract; full-paper check not done.*

---

## 6. Verdict and epistemic ledger

| Claim | Status |
|---|---|
| Selberg's sign-change architecture (mollifier → mean value → Jensen → sign changes) | exact theorem |
| Tones exist in pair correlation / N_osc at r·log p/(2π) | exact (formulas); heuristic (diagonal approximation) |
| Montgomery/Gallagher–Mueller/Alpöge–Furman/Lamzouri: pair correlation → simplicity | exact theorems |
| 2503.15449: PCC → 100% on critical line | preprint, conditional on unproven PCC |
| No literature connects tones → individual locations or sign changes | finding (absence of evidence) |
| Barrier 1 (two-point vs one-point type mismatch) | exact, structural |
| Barrier 2 (circularity of tone input) | analysis |
| Barrier 3 (Selberg's mean value is zero-free; tones cannot enter) | exact given the method's architecture |
| μ's three roles; unity via inversion; no usable channel | exact instances; analysis for the unity and no-channel claims |
| 10a detector as the project's positive prime-oscillation→zero instance | computationally verified (per DECISION_TREE 10a-step3) |
| Boundary test prediction (no correlation beyond density) | conjectural (test not run) |

**Bottom line:** the speculative question is well-posed, and the
answer is negative with identified mechanisms — a clean dead end,
which is valuable. The tones and Selberg's method are both
"prime-to-zero" bridges, but they run on different tracks sharing
only the prime input: Selberg goes *arithmetic coefficients →
pointwise forcing* (zero-free mean values, Jensen); tones go
*prime sums → zero statistics* (explicit formula, two-point).
μ's recurrence across both is real — it is the inversion operator,
forced wherever multiplicative accumulation must be undone — but
it marks a shared symmetry, not a shared channel. The project's
own 10a detector remains the correct positive model of how prime
oscillations inform about zeros: via exact identities, not via
pointwise forcing.

*Investigation status: complete, 2026-10-05. No computation run;
literature surveyed via targeted search; structural analysis is the
investigator's own, labeled as such.*
