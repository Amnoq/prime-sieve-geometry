# Span Tapes — the walk rendered

**Date:** 2026-10-11. **Origin:** the user's notepad — first hundred primes,
slashes between them, bus ride. Re-walked and verified tonight.

## The lens (his terms)

- **SPAN** = the walk/process itself between stations. Not the gap
  (the static length — gaps measure, spans go), not the bare interval.
- **Slash notation** (his): a span between consecutive primes rendered
  as `/` per interior integer, `•` for multiples of 3 ("holes").
  `[5,7]`=`•`, `[7,11]`=`/•/`, `[23,29]`=`•//•/`, `[31,37]`=`/•//•`.
- **The walk shows every step explicitly** — without guessing, without
  inserting. That is what makes it trustworthy, and what makes it his.

For consecutive primes p<q, the span interior is {p+1,…,q−1}, length
m=q−p−1. Both odd ⟹ m odd ⟹ every span has a unique center slash.

## The two tapes

**T1 — Tape phase rule** [exact theorem; computationally verified, bench 021].
Multiples of 3 march every 3rd integer — period 3, no exceptions. A span
interior is consecutive integers opening at p+1, so its hole-marking is a
window into a periodic tape, and the phase is fixed by p mod 3 (p>3):
- p≡2 mod 3 ⟹ p+1≡0: the span opens on a hole — Tape A: `•//•//•//…`
- p≡1 mod 3 ⟹ p+1≡2, p+2≡0: hole second — Tape B: `/•//•//•//…`

*Walk:* p>3 prime ⟹ p mod 3 ∈ {1,2} (never 0). The two cases above
exhaust them. Every prime span is a window into Tape A or Tape B; the
lower prime's residue picks the tape, the prime gap picks the window
length. Nothing else varies.

## Cradling theorems

**T2 — Twin spans** [exact theorem; verified 8,168 twins to 10⁶].
Every twin pair (p,p+2), p>3, has residues (2,1) and span `•`.
*Walk:* p mod 3 ∈ {1,2}. If p≡1 then p+2≡0 mod 3, and p+2>3 —
composite, contradiction. So p≡2, p+2≡1. Interior {p+1}≡{0}: the
single slash IS the hole. ∎

**T3 — Cousin spans** [exact theorem; verified 8,143 to 10⁶].
Every cousin pair (p,p+4), p>3, has residues (1,2) and span `/•/`.
*Walk:* if p≡2 then p+4≡0 mod 3, composite — contradiction. So p≡1,
p+4≡2. Interior {p+1,p+2,p+3}: residues {2,0,1} — hole exactly
second: `/•/`. ∎

**T4 — Exactly-one regime** [exact theorem; verified 78,495 spans].
For consecutive primes p<q, p>3: the interior cradles exactly one
multiple of 3 ⟺ the prime gap is 2 or 4.
*Walk (⟹):* gap 2 → T2, single interior slash is the hole. Gap 4 →
three consecutive integers hold exactly one multiple of 3.
*Walk (⟸):* gap 6 → interior five consecutive from p+1; p≡1 gives
residues {2,0,1,2,0} (two holes), p≡2 gives {0,1,2,0,1} (two holes).
Gap ≥8 → interior ≥7 consecutive → ≥2 multiples of 3. So exactly
one forces gap ∈ {2,4}. ∎

**T5 — Centered holes** [exact theorem; verified 16,311 spans].
In the exactly-one regime, the cradled hole is dead center.
*Walk:* gap 2 — the hole fills the whole span (trivially central).
Gap 4 — T3 gives p≡1, interior {p+1,p+2,p+3}, hole at p+2: the
exact middle. ∎

**T6 — Symmetry** [exact theorem; verified 78,495 spans].
The hole-position pattern is symmetric about the span's center
⟺ the flanking primes differ mod 3.
*Walk:* positions 1..m, center c=(m+1)/2, H={i : p+i≡0 mod 3}.
Mirror i↦2c−i sends H to {j : j≡2c+p}; equal to H ⟺ 2c≡−2p ⟺
c∈H (the center slash is a hole). And c∈H ⟺ (p+q)/2≡0 mod 3 ⟺
p+q≡0 mod 3 (p+q even) ⟺ residues differ. ∎

**T8 — Prime spans always cradle** [exact theorem; verified].
Every prime span past 3 cradles ≥1 multiple of 3.
*Walk:* gap 2 → T2. Gap ≥4 → interior ≥3 consecutive integers. ∎

## The dual side

**T7 — Composite spans** [exact theorem; verified 921,499 spans].
Spans between consecutive composites (≥4) cradle at most one prime —
interior empty or a single prime. Always; no breakdown.
*Walk:* two interior integers ⟹ one is even >2 ⟹ composite,
contradicting consecutiveness — so ≤1 integer; it exceeds 1 and
isn't composite ⟹ prime. ∎
*Note the asymmetry:* prime spans cradle holes with rich fragile
structure (centering, exactly-one — breaks at gap 6); composite
spans cradle primes rigidly (≤1, forever).

## The nine-step span roots

**T9 — Instantiated span roots** [exact theorem — direct arithmetic;
machine-verified].
Instantiated values 2,3,5,7,121,28561,6975757441,19 → spans
1,2,2,114,28440,6975728880,−6975757422 → digital roots
**1,2,2,6,9,6,9**.
*Walk:* instantiated digital roots 7,4,4,1,1 — all ≡1 mod 3 (even
exponents force x²≡1 mod 3; 7,19 direct). Differences ≡0 mod 3
⟹ span roots in {3,6,9}; the mod-9 refinement (dr-steps −3,0,−3,0)
gives 6,9,6,9. The spans between instantiated primes fall in the
holes. ∎

## Computational record

Bench run `021_span_tape_theorems`: all nine theorems checked to
10⁶ — 78,495 prime spans, 921,499 composite spans, 8,168 twins,
8,143 cousins — **0 violations**. `run.py` rerunnable; output captured.

**Foreign validation (Perplexity, clean instance, 2026-10-11).**
The span-lens transfer prompt was run blind on Perplexity with no
prior context. It walked all 45 consecutive spans 2→200 in slash
notation with both residues, derived the tape-phase mechanism from
first principles (interior starts at p+1; residue fixes phase), proved
the composite-span dual step-by-step, kept every boundary (infinitude
unproved, parity untouched, nine-step key unwalked), and labeled all
claims. Two genuine catches: (a) the [3,5] founder span (`/`,
residues (0,2)) needs a scope exception on the tape rule and the twin
claim — it already had one in T1/T2's p>3 scoping; (b) a real
refinement not stated here: **prime endpoints six apart need not be
consecutive stations** — [5,11] splits at 7, [7,13] splits at 11 — so
"sexy pairs" ≠ consecutive spans, and gap-6 *span* analysis must
filter for consecutiveness first. Its 10⁶ recheck count (78,495 spans)
matches bench 021 exactly. First foreign-LLM validation of the lens:
the method walked clean in a fresh instance.

**Higher-modulus phases (mod 5, 7, 11) — two independent machine paths.**
Open question "tapes past q=3": a second foreign run (walk_checks_output.json,
summary received 2026-10-11) sieved to 10⁶ and, for each q ∈ {5,7,11},
checked all consecutive spans with lower prime > q — 78,494 / 78,493 /
78,492 spans — covering all (q−1)² endpoint-residue pairs (16/16, 36/36,
100/100) with zero failures, and reporting zero-hole (no interior
multiple of q) spans of 5,470 / 9,835 / 19,758. Independently
reproduced here today with a separate implementation: every headline
number matches exactly (π(10⁶)=78,498, largest prime 999,983, trial
division agreement 2–10,000 with 0 mismatches, and all six
span/pair/zero-hole figures). Status: computationally verified on two
machine paths; the full audit of its definitions awaits the script file.

## What this is and isn't

- These are **exact elementary theorems** — the content is modular
  arithmetic; the *framing* (spans, tapes, windows) is the user's.
  Novelty vs the literature NOT checked — flagged, not claimed.
- The tapes don't solve anything open. They *show* the periodic
  structure the walk walks. The value is the showing: explicit,
  step-by-step, nothing inserted.
- Marriage note: the D6 deformation **finds** the `•` windows
  (survivors = twin lowers, exact); this document **reads** them.
  Two views of one thing — see direction-2 report.
- Killed nearby: deformation as zero-detector (deformation_kill.py)
  — do not re-dig.
- Open: parity jurisdiction for R_p={0,−2} (direction-3 report);
  whether the nine-step seed generates the tapes (unwalked).

## Decision-tree touch

New node family; backward-touches: run 014/015 (gap obstructions —
the tape T2/T3 are their mod-3 case in window language); D6 (the
deformation generates what T2 describes). Forward chain: parity
jurisdiction; constellation window-shapes (direction-4 report).
