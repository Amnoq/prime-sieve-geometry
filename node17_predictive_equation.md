# Node 17 — Direct predictive equation from positive-region geometry (2026-10-13) — OPEN

**Q:** Can the NEXT generated circle size (next prime) be derived directly
from the relational geometry — no successive candidate testing, no schedule
selection, no interval subdivision, no concealed search?

**Source construction:** the circle sieve (Perplexity derivation, 2026-10-12;
readable re-render with 95 numbered equations in the 2026-10-13
conversation; raw PDF at `~/workspace/user/files/1._7277956198842057117_0_xvsv.pdf`).
Unit circles tile the line; at each integer boundary n, a new circle size is
generated iff no previously generated size's projected sequence meets n
[document eq (5)]. Generated sizes = primes.

## The six reformulations (what was established — with labels)

1. **Boundary test** [exact theorem, document-internal]: generate at n iff
   n/d is non-whole for every existing generated size d [eq (5)]; testing
   sizes ≤ √n suffice [eq (10)]; sizes ≤ ⌊√L⌋ classify through L [eq (11)].
2. **Height product** P_S(x) = ∏_{d∈S} H_d(x)², H_d(x)² = r_d(x)(d−r_d(x)),
   r_d(x) = x − d⌊x/d⌋ [eq (20),(23)]: P_S(n) = 0 ⟺ some d∈S accounts for n;
   P_S(n) > 0 ⟺ n is a survivor [eq (24),(25)]. Exact geometric translation
   of (1), not a new test.
3. **Gap analysis** [exact theorem, document-internal]: after size 2, every
   gap between consecutive combined boundaries has width ≤ 2 [eq (52)]; new
   sizes sit at midpoints of surviving 2-gaps [eq (53)]; each odd d eliminates
   centers at the regular progression j = (d−1)/2 + k·d [eq (57)].
4. **Inclusion–exclusion count** U_S(x) = ⌊x⌋ + Σ_{∅≠T⊆S}(−1)^|T|⌊x/lcm(T)⌋
   [eq (61)] — Legendre's φ-function in the construction's language [exact
   theorem, document-internal]. Counts survivors through x; first increase
   locates the next size [eq (65)] — still a located search.
5. **Euclid openings** [exact theorem, document-internal]: P = ∏S gives
   guaranteed future survivors at P±1 with heights H_d² = d−1 [eq (69)–(75)].
   A bound and an opening, never the earliest survivor.
6. **Residue schedule via modular lifts** [exact theorem,
   document-internal]: surviving residues update algebraically with
   t_0(a) ≡ −a·u (mod p), W·u ≡ 1 [eq (85)–(88)]; next diameter read as
   q = min_a [a + W·⌈(N+1−a)/W⌉] [eq (94)]. Constructive next-event
   mechanism; requires maintaining the (primorial-growing) schedule and
   selecting its earliest future member.

Each relocates the search; none eliminates it.

## Boundary — section G's ten underived items (the problem's edges)

1. No compact, direct, non-testing equation for the next generated diameter.
2. No direct next-circumference prediction independent of the diameter.
3. Circumference, π, square-root limits have not supplied the missing formula.
4. No off-centerline intersection, height extremum, or other geometric
   measurement proved to determine the next size directly.
5. The height product is an exact boundary test, not a direct next-event formula.
6. Gap formulation: locating the first surviving gap still needs search or a
   maintained schedule.
7. Counting equation: inversion still requires locating the first increase.
8. Product openings give bounds, not the earliest survivor.
9. Schedule/lift avoids per-boundary testing but needs large preconstructed state.
10. **No impossibility result exists.** The equation is un-derived, not disproved.

## Triadic fork

### (a) CLAIM leg — the positive-region shape contains the answer: COMPUTED, null observation

Implemented P_S exactly as defined [document eq (20),(23)] and enumerated
every positive region (maximal open interval with P_S > 0) for
S ∈ {(2,3,5), (2,3,5,7), (2,3,5,7,11)}.
Script: `node17_positive_regions.py`; data: `node17_positive_regions.json`
(full per-region tables: endpoints, width, argmax, max, integral, survivor flag).

**Exact structural facts (proved, confirmed in the enumeration)
[exact theorem]:**
- log P_S is strictly concave on each region (each factor log(r_d(d−r_d))
  is concave: r_d affine in x there, r(d−r) concave quadratic) → exactly
  one argmax per region.
- All regions have width 1 or 2 (2∈S puts every even integer in the
  boundary set). Region count = W − φ(W): 22, 162, 1830 for the three S.
- Width-2 regions ARE the survivor regions, exactly: (a,a+2) consecutive
  in the boundary set forces a even, so the interior integer a+1 is odd
  and coprime to all of S. Width-1 regions contain no integer. (Asserted
  in code over all 2014 regions; zero violations.)
- The region containing the first survivor q (prime) is always exactly
  (q−1, q+1) — carries no information beyond q itself.

**Observations (first-survivor shape vs. survivor-region distribution)
[computationally verified]:**
- S=(2,3,5), q=7:   z = (offset +1.01, log-max +1.06, integral +1.08)
- S=(2,3,5,7), q=11: z = (+0.18, +0.01, −0.19)
- S=(2,3,5,7,11), q=13: z = (−0.11, −0.85, −0.88)
- All |z| < 1.1, signs inconsistent across the three S. The first
  survivor's region is unremarkable within the survivor distribution.
- Incremental panel (15 pairs: N = prime ≤ 47, S = primes ≤ N, q = next
  prime): argmax offsets ∈ (−0.157, +0.244), 5 negative / 10 positive —
  mixed signs, small magnitudes, no trend. log-maxval (0 → 55.6) and
  integral (1.33 → 1.36e24) are monotone in |S| — they measure how much
  sieve is built, not where the next prime sits.

**Verdict on leg (a):** null observation, and a genuine result —
[computationally verified] region shape (argmax offset, max, integral)
does not distinguish the first survivor from later survivors, and no
shape→location pattern was found at these scales. The positive regions
encode the residue class of q mod W faithfully but redundantly: shape
is a function of (q mod d)_{d∈S}, and nothing in the three functionals
probed compresses that below the residue data itself.

### (b) POLAR leg — the obstruction is structural: ANALYZED, not refuted

What a compact direct equation would have to be, from established facts only:

- **Unbounded range is mandatory** [exact theorem, classical]: prime gaps
  are unbounded (N!+2,…,N!+N all composite). Any direct q = F(S) must
  emit arbitrarily large outputs; no bounded-local inspection of the
  geometry can suffice. This rules out the "small neighborhood" family
  of candidate equations by theorem, not difficulty.
- **Exact prime formulas already exist — and hide the search**
  [classical literature, cited not re-derived: Willans (1964)-type
  formulas]: closed-form prime enumerators are known, but every one
  sums a primality indicator over candidate ranges — the search is
  relocated into the summation bounds, exactly the document's
  meta-pattern. Existence of *a* formula is not at issue; existence of
  one that does not conceal a search is.
- **The relocation pattern is formulation-independent** [established
  within the derivation document]: six coordinate systems (boundary
  test, height product, gaps, counts, Euclid openings, residue
  schedule) each preserve exactly one search step. The obstruction is
  not an artifact of one formulation.

**Verdict on leg (b):** does NOT refute the claim — consistent with
section G item 10, no impossibility is established. It constrains the
target: the equation must be non-local, unbounded-range, and cannot be
a rearrangement of boundary data. The live candidate the document names
— the positive-region structure of P_S *between* integers, i.e. what
the openings know before any candidate is tested — survives this leg
unscathed: leg (a)'s null concerned integer-region shape functionals,
not the continuous inter-integer geometry.

### (c) NULL leg — control: PASSED

The circle rule implemented literally from document eq (5) (generate at
n iff no existing generated size divides n) through 10^4 produces 1229
sizes; an independently implemented Eratosthenes sieve produces 1229
primes; the lists are **exactly identical**, largest 9973.
[computationally verified] The foundation the legs build on is sound;
leg (a)'s null is not a corrupted-input artifact.

## Status

**OPEN.** Leg (c) passed (foundation verified). Leg (a) returned a clean
null (region-shape functionals carry no first-survivor signature at
probed scales). Leg (b) bounded but did not kill the target. The equation
itself is untouched — per the charter, no invention attempted.

**Why it ends here (this turn):** node opened, triadic fork designed and
executed as far as chartered: control verified, claim leg computed to a
null observation, polar leg analyzed to constraints. The next move —
probing the continuous inter-integer positive-region geometry, or a new
quantity altogether — is a new node, not a continuation.

**Its chain (resumable inventory):**
- The inter-integer structure of P_S (openings between integers, not
  integer-region shape) is the one direction neither leg (a) nor the
  document's six reformulations exhausted.
- Leg (a)'s exact structural facts (log-concavity per region, width ≤ 2,
  width-2 ⟺ survivor, region count = W − φ(W)) are reusable lemmas.
- The null observation is load-bearing for any future attempt: shape
  functionals of survivor regions do not compress residue data.

## User observation (2026-10-13): (rule, origin) determinism

His formulation: every circle's circumference is determined by set rules and reference to a zero point. Precise form: C_d = π·n_d with n_d the qualifying boundary coordinate measured from the single shared origin 0; the architecture's total input is (generation rule, origin) — zero free parameters, fully deterministic.

Consequences recorded:
- Confirms document eq (43) from the other direction: π cancels; circumference is the boundary coordinate in geometric dress. The prediction target is the next qualifying coordinate-from-zero; the geometry contributed the question, not a second quantity.
- Reframes the hunt: no missing input exists, so the equation cannot come from a new independent quantity — any candidate must be derived from (rule, origin). The question becomes whether the rule's unfolding admits a compressed form (a shortcut through the dynamics) rather than simulation. This is the computational-irreducibility question in the architecture's own terms.
- Connects to the standing "self-deriving system" line (2026-09-29): the sieve needs nothing but the rule and zero; Node 17's target is the compressed form of that self-derivation.
[observation, his words formalized; consequences analytic]

## User question (2026-10-13): consistency of the expansion angle

His question: is there consistency in the expansion/trajectory angle at which each generated circle is drawn? Answer: yes — two exact consistencies, both forced by (rule, origin):
1. **Common departure:** every generated circle (diameter [0,d]) satisfies x^2 + y^2 = d·x, hence has vertical tangent x = 0 at the origin. All generated circles are mutually tangent at 0 with the same tangent line. The "trajectory angle" of departure is 90° for every size, without exception.
2. **Common apex ray:** the topmost point of the size-d circle is (d/2, d/2), at angle arctan(1) = 45° from the origin, for every d. Each generated circle is the unit circle scaled by d about the origin — pure homothety, total self-similarity.
Consequence (analytic): shape carries zero distinguishing information between sizes — the consistency is total, so geometry alone cannot select the next size; only the scale (the boundary coordinate from 0) varies. This is of a piece with leg (a)'s null: survivor-region shapes do not compress residue data. The prediction, if it comes, comes from positions, not shapes.
[exact by construction; consequence analytic]

## Orienting hypothesis (2026-10-13, his): the address is 0, not 0.5

His hypothesis: the predictive equation will be found at the origin's neighborhood — where all circles coincide and fan out — not at 0.5. Precise form:
- 0.5 was the wrong address for this problem: it is the balance-point/zeta-line heuristic, belonging to the spectral (zero-distribution) axis. The generation problem's natural address is 0's neighborhood.
- Structural reason the hypothesis has teeth: 0 is the unique accumulation point of the architecture — every neighborhood of 0 contains every generated circle. It is the only point where all size data coexists. If any local reading could yield the next size, it must be there.
- Honest boundary: the near-origin fan is informationally equivalent to S (fan ⟺ S; each curve's d recoverable from its shape). "Look at zero" orients the hunt but adds no power by itself — it is the same data re-encoded.
- Sharpened problem statement: the equation must derive the next distinction from the point where all distinctions coincide — emergence-from-indistinction, in precise form. That move — reading the next difference out of the undifferentiated point — is what nothing has attempted.
[hypothesis his; structural reason exact; boundary analytic]

### Emergence-ordering probe (2026-10-13)

First operationalization of the hypothesis: if the fan's emergence ordering
suggests a move the arithmetic hides, it should show in WHERE a new size's
distinctions insert. Method: S_k = first k primes, k = 3..12; emergence
ordering = all pairs (d1<d2) sorted by √d2−√d1 ascending (the order pairs
become distinguishable as x grows from 0); for q = p_{k+1}, record insertion
ranks of the new pairs (q,d), d ∈ S_k. Script: `node17_emergence_probe.py`
(rerunnable); data: `node17_emergence_probe.json`.

Findings:
- [computationally verified] No √-gap ties within 1e-12 at any k — the
  emergence ordering is strict.
- [computationally verified] The new prime's pairs spread across the FULL
  ordering — insertion fractions run 0.00 to 1.00 at every k, monotonic in
  d. They are not clustered, not confined to the head (last-emerging) or
  the tail.
- [exact] (q,2) always becomes the new tail: √q−√2 strictly exceeds every
  existing gap (q is the new max, 2 the min — no other pair can beat it).
- [computationally verified] The pair (q,p_k) with the predecessor inserts
  at a rank tracking the prime gap q−p_k: twin gaps (2) at larger sizes
  take the head, becoming the new last-emerging distinction (k = 5, 7, 10);
  larger prime gaps insert deeper (k = 4, 6, 9, 12). This is √-concavity
  acting on prime gaps — no independent regularity.
- [computationally verified] The smallest √-gap in S_k (the last-emerging
  distinction) is always the closest twin-prime pair; it involves max(S_k)
  iff the max completes that twin pair (3 of 10 k values: k = 6, 8, 11).
- [null] **Verdict:** the emergence ordering carries no constraint on the
  next size beyond S. Insertion positions are determined BY q, not
  determining OF q — any prime q > p_k produces some spread pattern, and
  no pattern is forbidden. The geometric presentation suggests no move the
  arithmetic presentation hides, consistent with the honest boundary
  (fan ⟺ S).

Scope: this nulls this operationalization, not the hypothesis. The
hypothesis as stated (derive the next distinction from the coincidence
point) remains open; the pairwise emergence ordering is one more
re-encoding, and like the six reformulations it relocates rather than
removes the search.

### Continuous height-field probe (2026-10-13)

Third operationalization: the inter-integer field itself — the points the
integer test never samples. Definitions read fresh from the record:
F_S(x) = log P_S(x) = Σ_d log(r_d(d−r_d)); P_S(x) = 0 only at integer
multiples, so the field is smooth and strictly log-concave on every open
interval (m, m+1); half-integers are the points maximally far from the
integer test stations.

Method: S_k = first k primes, k = 3..10; window = 200 intervals past p_k
[arbitrary choice, labeled]. Three predictors, each defined WITHOUT
reference to p_{k+1} (the check against p_{k+1} happens after):
- P1 half-integer height: a_m = F_{S_k}(m+1/2); select argmax.
- P2 half-integer openness: c_m = −F''_{S_k}(m+1/2) =
  Σ_d [1/r_d² + 1/(d−r_d)²] [analytic; verified in-script against finite
  differences, worst rel err 6e-6]; select argmin ("most open").
- P3 interval openness: I_m = ∫_m^{m+1} F_{S_k}(x) dx (trapezoidal, dense
  grid; no singularities on the open interval since zeros are integers);
  select argmax.
A predictor "selects" q = p_{k+1} iff its argmax/argmin m* ∈ {q−1, q}.
Pre-registered verdict: SIGNAL iff selection at ALL 8 k; else NULL.
Secondary pre-registered measure: how often the selection is adjacent to
ANY survivor (distinguishes "correlates with survivorship in general"
from "selects the next"). Controls: C1 circle rule list-identical to an
independently implemented Eratosthenes sieve through 5000 (669/669);
C2 next size from the rule = Eratosthenes p_{k+1} at all k.
Script: `prime-claim-bench/archive/runs/025_continuous_height_field/run.py`
(rerunnable, ~5 s); output: `output.txt`; bench INDEX entry 025.

Findings:
- [computationally verified] P1 selected q at 1/8 (k=3 only); P2 at 1/8
  (k=3 only); P3 at 0/8. The single hits are chance-consistent (8 trials,
  ~1% per-trial hit rate for a random interval).
- [computationally verified] Secondary: selections adjacent to SOME
  survivor at 8/8 (P1), 8/8 (P2), 7/8 (P3), vs ~38% for a random interval
  at these densities. The between-integer field correlates with
  survivorship in general but does not select the next — the field
  "knows" where survivors are in aggregate, not which comes first.
- [null] **Verdict:** no between-integer predictor selects the next
  generated size. The half-integer field and the interval-openness
  integral carry no first-survivor signature beyond S at probed scales.
- Note: P1/P2 selections coincided at k=3,4 — both favor residues near
  d/2 (max of r(d−r), min of 1/r²+1/(d−r)²), so they are correlated
  predictors, not independent witnesses.
- Equation not attempted (observational scope held).

Scope: nulls this operationalization, not the hypothesis. Three
operationalizations now stand nulled (region shapes, emergence ordering,
inter-integer field); the hypothesis itself — derive the next
distinction from the coincidence point — remains open and un-attempted
as a direct construction.

## Backward touch

- Does not alter any prior node verdict. It is downstream of the
  circle-sieve construction (external derivation, 2026-10-12/13) and of
  the sieve-equation rigor work (`SIEVE_EQUATION_RIGOROUS.md`:
  Rel*(n)={0} ⟺ prime is the same generation rule in relational
  language — consistent, untouched).
- Node 11l/11n (orbit→tone mechanism): unrelated axis (spectral, not
  generative); no touch.
- `DERIVATION_ATTEMPT_2026-10-11.md`: this node is a cleaner, narrower
  restatement of that attempt's open end (predictive equation), now
  with a decision-tree home and a first null observation.

---
*Scripts: `node17_positive_regions.py` (rerunnable; ~30 s).
Data: `node17_positive_regions.json` (594 KB: control result, per-S
region tables, incremental panel). Labels: [exact theorem] /
[computationally verified] / [classical literature, cited] as marked;
nothing here is conjectural or heuristic.*
