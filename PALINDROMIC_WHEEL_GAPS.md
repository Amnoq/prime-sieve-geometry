# Palindromic gap structure in primorial wheels (2026-10-13)

Repaired artifact. Source was a damaged LLM explainer (residue lists stripped
in paste, wrap gap omitted). Rebuilt from definitions; every claim below
verified computationally.

## Exact statements [verified for M = 6, 30, 210, 2310]

- Coprime residues R of M, sorted; the LINEAR gap sequence (R[0]→R[-1]) is
  palindromic. [exact]
- The CYCLIC gap sequence (including the wrap gap (R[0]+M)−R[-1]) is
  reversal-symmetric up to rotation. [exact]
- The wrap gap is always 2 (M−1 and 1 are both coprime). [exact]
- Reason: inversion σ(r) = M−r permutes the coprime residues; reflection
  axis at M/2. [classical]
- mod 30: residues [1,7,11,13,17,19,23,29]; gaps [6,4,2,4,2,4,6]; wrap 2.
- φ: 6→2, 30→8, 210→48, 2310→480.

## Era evolution [exact]

Each graduation refines the palindrome (6→30→210→2310). The graduation
witness p_{k+1}² is always a CANDIDATE SLOT (coprime residue) of the current
wheel — that is exactly where the wheel's fidelity breaks:

| wheel M | witness | slot r = witness mod M |
|---------|---------|------------------------|
| 6       | 25 = 5² | 1 |
| 30      | 49 = 7² | 19 |
| 210     | 121 = 11² | 121 |
| 2310    | 169 = 13² | 169 |

The palindrome describes slots; the witness sits in a slot. "Nine doesn't
work" = the first row: at 25 the {2,3}-wheel's fidelity is hit (and at 9,
the {2}-wheel's — 9 = 3² the very first graduation).

## Z/2 parallel with the torus [exact form, null yield]

- σ(r) = M−r on coprime residues and T(i) = i+m mod 2m on the ring are both
  FIXED-POINT-FREE involutions (free Z/2 actions). σ(r)=r ⟺ r=M/2, never
  coprime; T(i)=i has no solution. Same symmetry type — "two is what gives
  us the symmetry."
- Neither preserves primality: σ(29) = 1 (not prime); T-images (5,4)→41
  prime vs (5,8)→77 composite. The involution acts on slots/positions,
  never on primality — this names the wall's shape for both constructions.
- Verdict: real structural parallel, zero predictive yield. Informative
  about the wall, not a way through it.

## Predictive check: does the palindrome predict hits? [computationally verified null]

Reflection-pair prime correlation, M=30, 10,000 periods (X=300,000):

| pair | type | corr |
|------|------|------|
| (1,29) | reflection | +0.058 |
| (7,23) | reflection | −0.024 |
| (11,19) | reflection | −0.024 |
| (13,17) | reflection | −0.026 |
| (1,7),(1,11),(7,13),(11,29) | controls | −0.016…−0.020 |

General reflection pairs are null like controls. The (1,29) anomaly persists
split-half (+0.068 / +0.045) — derived, not mysterious: 29 ≡ 1 (mod 7), so
both primality conditions share the IDENTICAL mod-7 sieve obstruction
(k ≠ 3 mod 7); shared composite-obstruction induces mild positive
correlation. Second-order sieve artifact, not palindromic prediction.

Verdict: the palindrome describes slots, not hits. It predicts nothing
about primality. Null.

## Node 17 implication

σ is local (one input), non-testing, closed (involution) — matches the
"shape of a crossing" desiderata — but provably does not determine
primality. Another mold, not a crossing. No new probe; the boundary
("predicts position, not history" — here: describes slots, not hits)
is reinforced.
