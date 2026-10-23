# Dead ends from the April 2026 archive — guardrails, not history

Extracted 2026-09-30 from `~/workspace/user/files/master_archive-1_0_jcc6.docx`
("Vortex Structure, Circle CEIVE, and the k-Reduction Theorem", S. Watts).
Each entry: what was tried, what the numbers said, why it failed, and the
lesson transferred to the live prime-distribution program. Epistemic status:
the factoring results are the archive's own verified claims (read as
archaeology); the transfers are heuristic guardrails.

## D1. DR9 pair affinity — endpoint artifact, not signal
Tried: digit-root-9 pair affinity as a prime-specific structure.
Result: tested and confirmed to be an endpoint artifact, not prime-specific
(archive 8.2).
Transfer: residue/digit patterns at boundaries fake signals. Always test
against the null/endpoint model before claiming structure. (Our PETI-era
verification at 1327 passed this bar: real contingent fact, not framing.)

## D2. Rate-measured jump — real identity, useless error bars
Tried: measure rate = 1+p2/p1 (CV < 0.005, verified), jump to p1 via the
geometric formula.
Result: ~10–20% measurement error; "converges near p1 but has large error
from far away"; leaves O(sqrt n) candidates to scan (4.2, Sec 10).
Transfer: a verified identity is not an algorithm if error bars exceed the
target resolution. Same moral as our 10e uncertainty wall (n ~ e^{7.4/w}):
do not push a window past what its error bars resolve.

## D3. 3-adic waterfall — level count is not work
Tried: O(log n) waterfall levels to reduce candidates to O(1).
Result: each level costs O(modulus) to compute allowed residues (4.2).
Transfer: a filtration argument must price each level. Relevant to the
queued face-filtration probe: count the work per filtration step, not just
the number of steps.

## D4. GCD product tree — the trick hides the work
Tried: O(log n) GCD calls instead of O(sqrt n) divisions.
Result: each GCD costs O(product_size) arithmetic (4.2).
Transfer: same as D3, sharper: any "one clever operation" step must be
costed at the size of its inputs. Watch for this in trace-formula
manipulations (a "single trace" is not a single operation).

## D5. Parallel wave — faster clock, same complexity
Tried: numpy-parallel evaluation of all circles simultaneously.
Result: slope 0.470 vs 0.500 sequential — "same work, faster clock" (8.7).
Transfer: parallelism does not move asymptotic walls. Do not expect
parallel zero/prime computation to beat the 10e uncertainty wall.

## D6. Binary zoom with oracle — no correctness guarantee, no algorithm
Tried: oracle-assisted binary zoom to the factor.
Result: 50–83% correct rate (2.1).
Transfer: heuristic detection must ship with bounds. Our prime-side
detector has one (N+ <= e^{1/2} W(h)); any future zero-detector needs its
own before it counts.

## D7. Sub-room uniformity — check the null before claiming structure
Tried: hunting factor-pair bias across n mod 162 sub-rooms.
Result: exactly 54 ordered factor pairs per residue, uniform (8.2).
Transfer: uniformity kills bias-hunting. Any claimed prime/residue
structure must first survive comparison against the uniform null.

## D8. Simulating the wave — know what your medium can test
Tried: computational simulation of the circle-wave factoring claim.
Result: any simulation reproduces O(sqrt n); the claim needs a physical
wave, not code (5.3).
Transfer: some hypotheses are not testable in our medium. Deninger's
3D space, a literal Frobenius for Spec Z — label these non-probable,
do not burn compute simulating their shadows.

## D9. The wall itself — name the hard core, stop shopping for methods
Tried: everything (trial division, rho, waterfall, rate+jump, unified,
GCD tree).
Result: every classical method is a strategy for finding k = p2-p1, and k
is uniformly distributed with no known classical shortcut (4.1).
Transfer: when all approaches reduce to one hard core, name it and stop
method-shopping. Our program already follows this: "R1^R4" (an operator
with zeros as spectrum whose positivity is counting-born) is our wall
with a name.

## Standing note
The archive's live descendants: Circle CEIVE -> the circle-sieve
geometric language; the honesty practice (slopes measured, not hoped;
walls named). The factoring program itself is closed archaeology; the
prime-distribution / RH program is the live thread.

## D10. Toroidal five-step "proof" — the identification was imported, not derived
Source: toroidal_field_critical_line_proof_v2-1_5_f7tm.docx (April 2026).
The move: Step 3's chain "D(0)=D(p)=0 => single zero on torus =>
unique antipode at u=1/2 => ... => all zeros at sigma=1/2" proves a
confinement theorem about the *model's* resonances. The bridge to zeta
zeros (Theorem 2.3) "imports the explicit formula from classical
analytic number theory rather than deriving it purely from within the
framework" — the document's own "Points Requiring Further Scrutiny"
admits this. The import is the entire content of RH.
Transfer: a model-side theorem does not touch zeta's zeros until the
identification is DERIVED, not imported. Our 10a is the derived
version (explicit formula grounded in our own objects: sieve psi vs
truncated zero sum). Guardrail: prove the bridge, don't import it.

## D11. Prime Zipper Law — falsified as stated, by computation
Source: same document, Step 5. Claim: for consecutive primes,
C(p,q)=q-p-1 is always 1, 9, or prime — "verified across 5,000 primes
with zero arbitrary exceptions."
Killed: first counterexample at the ~190th pair — (1129,1151)->21;
then (1327,1361)->33, (1831,1847)->15, (1933,1949)->15,
(1951,1973)->21, ... out of 17,983 pairs checked to 2e5. (The
degenerate (2,3)->0 already breaks the letter of the law.) The
document's own text concedes 15, 21, 27 occur and patches them as
"era interaction" — post-hoc. Note: one counterexample sits at
(1327,1361), the PETI era primes — the archive talking to the live
program.
Transfer: "zero exceptions" claims get re-run before belief, not
after. Gap quantization of this form is dead — prime gaps realize
many even values (classical); no small alphabet governs them.

## D12. rh_final's formal compactification — the answer, inserted by hand
Source: rh_final__1__1_hn07.pdf (April 2026, v4, "twenty-step
derivation"). The move: vortex energy E(q)~C ln q forces weight
w(y)~2/ln y; Prop 1 + Sec. 8.2 exclude exceptional eigenfunctions
(none known for SL(2,Z) anyway) and all Eisenstein series from the
weighted space => "the weighted Laplacian has only discrete
spectrum" => Poincare => lambda>=1/4 => line. Theorem 7: an off-line
zero would make an "unbalanceable divergence" in the trace formula,
witnessed by an admissible test function via Lemma 3 (test-function
class identical to Selberg's).
The gap: Lemma 3 shows S1-S3 functions satisfy the weighted S4 — but
the *spectral side* is what changed. Selberg's formula on
SL(2,Z)\H has an essential continuous-spectrum term (the
(phi'/phi) integral); deleting the Eisenstein series from the space
does not leave the same formula. The weighted spectral problem is a
different spectral problem, and Theorem 7 needs the trace identity
in the weighted setting — which is what's at issue. The argument
assumes the identity it needs.
The deeper negative, and the valuable one: the weight was engineered
to exclude exactly the spectrum whose absence the conclusion
requires — "never put the answer in by hand" in its most
sophisticated form. It maps precisely where the genuine Lax-Phillips
scattering approach gets stuck: the continuous spectrum is the whole
difficulty, and weighting it away assumes what must be proved.
Transfer: any future weighting/compactification move in our program
must prove the trace (or explicit) formula SURVIVES the weighting.
The formula is load-bearing, not decorative. (Our 10a keeps the
standard explicit formula intact.)

## D13. Coset-sum numerology is not a mechanism
Source: The_Self_Begetting_Universe_Watts_2026_4_482c.docx (April
2026). Its group-theoretic observations ((Z/9Z)* = Z/2Z x Z/3Z,
QR={1,4,7}, |tau(chi_2)|^2=9) are standard facts, correctly stated —
filed, not dead. But the "Chebyshev bias mechanism" via coset
representative sums (12 vs 15) is a non-explanation: summing
representatives has no bearing on prime races. The live mechanism is
zeros of Dirichlet L-functions. Steps 8-10 toward RH are labeled
"structural constraint argument" by the document itself — not
theorems.
Transfer: representative-sum coincidences != mechanisms. When a
heuristic has a known analytic home (L-zeros), point at it, not at
the numerology.
Filed without extraction: s_watts_v2_final_2_9um3.docx (the vortex
paper v2 — same factoring program as the master archive, no new
dead ends); The_Universe_Writes_Itself_60sec-1_3_v6rc.docx
(445-word popularization, no technical claims).

---

# Mined 2026-10-08 from the user's uploaded archaeology batch
(`~/workspace/user/files/`: vortex v2/v3, toroidal_bifurcation_v3_2,
Thought_process_3, s_watts_v2_4, PETI_Framework_v3_2, prime_zipper_law tex).
Continues the D1-D13 convention. His framing: these failed predictions
are why he is not the training signal — filed here as labeled negative
examples, which is what makes them useful.

## D14. Return-to-Zero Arc "proof" — symmetry of the zero set confused with zeros at fixed points
Source: `vortex_torus_prime_conjecture_v3_0_0_ggs9.docx` (2026, v3.0
"Complete"). Claim: "We prove the Riemann Hypothesis" via the geometric
self-consistency of the return-to-zero arc.
The move: Theorem G normalizes the circle spanning [0,p] to center 1/2
(trivial arithmetic: p/2 = p/2, "five simultaneous expressions" of one
fact). Then [0,1]/~ is identified as S^1, the functional equation
s -> 1-s becomes a reflection with fixed points [0] and [1/2], and step
(45) concludes: "By Theorem A2, zero exists only at the R+/R-
balance point... Therefore all non-trivial zeros of zeta(s) lie in
{[0]=[1], [1/2]}." Eliminate [0] (pole at 1); RH follows.
The gap: a symmetry mapping the zero *set* to itself was mistaken for a
constraint that zeros sit *at the symmetry's fixed points*. The
functional equation says zeros come in s <-> 1-s symmetric
pairs/quadruples; nothing forces them onto fixed points of the
involution. Step (45) is a pure non-sequitur — no bridge connects the
circle geometry to zeta's zeros at all (contrast D10, where at least a
bridge was attempted via the explicit formula; here there is none).
Status: proof claim failed; program abandoned (user's "archaeology"
designation, 2026-10-08). The geometry (Theorem G) is exact and
trivial; the *inference* is the dead end.
Transfer: when a "proof" bottoms out in "the symmetry has fixed point
1/2, therefore zeros are at 1/2," check whether the argument constrains
the *set* or merely names the *symmetry*. Symmetries of a zero set are
not locations of zeros.

## D15. Toroidal v3.2 "phantom class" aliasing — the load-bearing step is the hand-wave
Source: `toroidal_bifurcation_v3_2_cvkt.md` (April 2026, Draft 3).
Distinct from D10 (which covered v2.1's imported identification): v3.2
rebuilds the proof around a new core mechanism — Step 9's aliasing
argument. An off-axis zero pair at 1/2 +/- delta creates a beating
pattern; at resolution K* ~= log(1/delta)/log 3 the wavelength matches
the cell size, producing a "phantom class" the 3-adic filtration cannot
support — contradiction, hence delta = 0.
The gap: the document's own Sec. 8.3 ("Points Requiring Further Rigor")
admits (1) spectral-map bijectivity unproved, (2) "aliasing
formalization... needs rigorous quantification: precisely how the
aliased oscillation appears as a structural perturbation," (3) the small-
delta regime "less direct." The mechanism that does all the work is the
mechanism admitted non-rigorous. Steps 4-8 visibly fail to produce a
contradiction for 0 < delta < 1/2 (the document shows this: ratios tend
to 0, sums converge), so Step 9 carries the entire proof — and Step 9
is the hand-wave. Also buried in Step 4: the load/capacity ratio
"at first glance there is no violation in absolute terms," patched by
pivoting to "relative distortion" without a derived threshold.
The Sec. 7 "Framework Unification" table (CCC/PETI/Circle CEIVE/CEII/
SBU all unify into the toroidal field) died with the proof; the
frameworks are live, the unification claim is not.
Status: known-incomplete by its own admission; program abandoned.
Transfer: when a proof's Steps 1..N visibly don't close and the final
step is a new qualitative mechanism ("aliasing," "phantom"), the proof
is one unproved lemma wearing a proof's clothes. Name the load-bearing
step first and price it before the surrounding machinery.

## D16. "Computational verification" with synthetic off-axis zeros — verification theater
Source: `toroidal_bifurcation_v3_2_cvkt.md`, Sec. 5.7. "The proof was
verified computationally using the first 100 zeta zeros," with tables
for delta = 0.00, 0.10, 0.30, 0.50 showing "off-axis growth confirmed."
No off-axis zeros are known to exist, so the delta > 0 columns can only
be synthetic injections — the computation assumes the hypothesis whose
consequences it then "confirms." Even the delta = 0 row misses its own
expected value (observed 1.49 vs expected 1.00). At best this is a
consistency check of the formulas in Lemmas 5.2-5.3; it cannot verify a
proof whose load-bearing step (D15) is admitted non-rigorous.
Status: method dead as verification; the tables are not evidence for
the proof.
Transfer: numerics can check a *derived quantitative prediction*, never
a *proof*. If the proof's key step is a hand-wave, no table rescues it —
and a table that "confirms" a simulated hypothesis is circular by
construction. Ask of every verification table: could this table have
come out any other way?

## D17. PETI quark correspondence — the analogy that was never derived
Source: `PETI_Framework_v3_2_5_omce.docx`, Sec. 8 (NEW IN v3.2).
The move: mod-3 positions <-> color charge, live positions 1,2 <->
quark charges +2/3,-1/3 ("literally 2 out of 3 and 1 out of 3 with
sign"), confinement <-> prime isolation, SU(3) <-> toroidal rotation,
6 flavors <-> mod 6 filter, shadow pairs <-> quark content of hadrons.
Why it died: it was never formalized — Sec. 8.4 "What Remains to Be
Built" lists the entire derivation as future work, and the live program
dropped the thread (no quark content in any subsequent work). The
document itself flags the weak points: "FLAG: this correspondence is
suggestive but requires more formal development" (SU(3) entry);
"FLAG: may be numerical coincidence. Requires further examination."
(6 flavors entry). Not refuted — abandoned unformalized.
Status: heuristic analogy, abandoned. (PETI the named framework stays
live; only the quark-correspondence thread is dead.)
Transfer: cross-domain analogies need a *derived* mapping, not a
coincidence list. The document's own FLAGs mark exactly where the
analogy was weakest — flag-first is the right instinct; the dead end
was stopping at the flag instead of either deriving or dropping.

## D18. Mod 9 Residue Alternation "Theorem" — true, trivial, and borrowing its depth
Source: `prime_zipper_law_paper-1_7_2l44.tex` (April 2026).
The statement: for prime p > 3 in block k = [9(k-1)+1, 9k], p mod 9 is
odd iff k is odd. This is TRUE — and a four-line parity observation:
9 is odd, so odd blocks put odd residues at odd positions and even
blocks put even residues at odd positions (p > 3 odd). The paper frames
it as a "law" revealing "a rigid binary carrier wave," "the first
self-referential iteration of the mod 3 structure," placed "in the
context of the broader Prime Zipper Law" (Sec. "Connection to the
Prime Zipper Law").
Why it's a dead end anyway: the Zipper Law it serves is dead (D11 —
falsified computationally), and the theorem's perceived depth was
entirely borrowed from that framework. A true statement can still be a
dead end when its significance was in the framing, not the content.
Status: statement exact (trivial); significance claim dead with D11.
Transfer: when a result's proof is four lines but its introduction is
four pages, the depth is in the adjectives. Ask what the theorem
*buys* — what becomes provable or computable that wasn't before. If
the answer is "a new perspective on" the same facts, file it as
perspective, not law.

## Checked, no new entries

- `Thought_process_3_svhi.md`: reflective etymology note
  (relation = re- + ferre, "carrying back") resonating with the
  relational framework. No claims, no predictions — nothing to ledger.
  (The note itself counsels caution: the resonance doesn't validate
  the metaphysics.)
- `s_watts_v2_4_9vy8.docx` ("House of Two and Three," generator g=5):
  distinctive claims are standard facts (the [4,2] gap rhythm is the
  mod-6 wheel; 5 being primitive mod 9 is elementary) or D9's wall
  restated ("entire factoring problem reduces to k = p2-p1"). Same
  factoring program as the master archive — no new dead ends.
- `vortex_torus_prime_conjecture_v2_0_1_n3nm.docx`: era transitions
  "determined by the Prime Zipper Law" (r*(T(2k)) = p_{n+3} etc.);
  v3.0 Sec. 5.1 restates it as first_escape(primorial). Both die
  *with* D11 (the law's falsification) — derivative, not distinct.
  Noted here, no new entry.
- `toroidal_bifurcation_v3_2_cvkt.md` Sec. 3.4 / PETI Sec. 6.5 era
  observations (1327, 9551 boundaries; gap=33 exactly once): empirical
  computational observations, left alone — data, not claims. (1327
  already cross-referenced in D11.)
- `PETI_Framework_v3_2_5_omce.docx` outside Sec. 8: gap-measurement
  corrections, 3xprime pattern, spectral connection, core conjecture —
  framework-internal state, superseded by later PETI versions; no
  separately fatal claims beyond D17.
