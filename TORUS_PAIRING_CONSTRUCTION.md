# Torus across-hole pairing construction (2026-10-13)

His construction, formalized in his terms. ("Taurus" throughout = torus, dictation.)
Status: construction verified exact; NOT a predictive equation; the wall stands.
See DECISION_TREE.md Node 17, probe 4.

## Definitions

- Residues r = 1..9 (his nine).
- Blocks b = 0, 1, 2, ...; block b = {9b+1, ..., 9b+9}.
- The pairing: from residue r, the partner in block b is **9b + r**.
- N×N grid, N a multiple of nine (his constraint), numbers 1..N² laid in order.

## The function P(i) — the spoiler

**T(i) = (i + m) mod 2m** — the across-hole involution on a 2m-ring.

**P(i) = ( v(T(i)), factorization(v(T(i))), parity(v(T(i))) )** — from one
position, everything across from it: number, history, parity.

Exact properties [all computationally verified]:
1. T(T(i)) = i — involution, its own inverse.
2. P(i) uses only i — locality. No history, no killer-set, no survey.
3. Nothing tested, nothing inserted — values read from the layout (spoiler, not smuggling).
4. Twist every nine: partner parity = (r + b) mod 2 — odd blocks invert parity,
   even blocks preserve. On the minimal 9×2 the across-hole map IS a parity
   inversion, always (offset 9, odd).
5. 9×9: (r,b) ↦ 9b+r is a bijection onto 1..81.

## Closure rule — "the end bites in" [exact, verified]

N must be a multiple of nine (his constraint). The twist bites in — consistent
at the wrap — iff the block count N²/9 is even, i.e. iff N is an **even**
multiple of nine:

| grid | blocks of nine | twist closes | clean antipode |
|------|---------------|--------------|----------------|
| 9×9  | 9 (odd)       | no — parity seam | no (N odd) |
| 18×18| 36 (even)     | yes | yes |
| 36×36| 144 (even)    | yes | yes |
| 81×81| 729 (odd)     | no — parity seam | no (N odd) |

Rule: 18, 36, 54, ... fasten shut. 9, 81, ... leave the twist unclosed.

## Predictive range

Reach of the pairing = 9 × (max block). Same mechanism at every scale:
- 9×9: +72 (out to 81)
- 18×18: +315 (out to 324)
- 36×36: +1,287 (out to 1,296)

Expanding the predictive range = a bigger (even-multiple-of-nine) torus.
The rule never changes.

## Boundary [exact]

P(i) predicts the partner's **number** (9b+r) and **parity** ((r+b) mod 2) by
pure local arithmetic — no walking the intervening numbers, no factoring.
It does NOT predict the partner's factorization or primality:
(5,4) → 41 (prime); (5,8) → 77 = 7×11. Same form, different histories —
the factorization is not in the pairing.

The wall stands: no function of local position alone determines primality
without search (prime gaps unbounded, classical theorem). The construction
exhibits the *shape* of a crossing — local, non-testing, closed — it is the
mold, not the crossing.

## His phrases (verbatim, 2026-10-13)

- "smuggling backwards the information" — spoiler, not smuggling: read out of
  the laid-out structure, never inserted by hand.
- "the Taurus is not actually a thing it is the sum of its relations."
- "Not shape but plane." — the 2D relations are the content; 3D is the vantage.
  (The 3D sightline-through-the-void story breaks geometrically for outer
  points — checked; the plane is what's real.)
- "the twist is going to show us odd and even residues."
- "It has to fit the end bite in in a multiple of nine."
- "The map predicts position, not history."

## Artifacts

- across_hole_pairing_record.md — 9×9 record, 72 pairs, computed.
- across_hole_pairing_record_18x18.md / .json — 18×18 record, 315 pairs (built 2026-10-13).
- toroid_wireframe_pairs.py / .gif — 3D wireframe illustration: pairs glow as they
  line up across the hole, 72 predictions logged live to a growing list.
- toroid_18x18_pairing.png — earlier static pairing render (scaffolding).
