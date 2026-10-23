"""Extend the across-the-hole pairing record to 18x18 scale (324 numbers,
36 blocks of nine, b=0..35; block 0 = base) and hunt for emergent patterns.

Definitions (exact, per task):
  r in 1..9 (residues), b in 1..35, partner value v = 9*b + r.
  Primality by trial division (exact for v <= 324). Full factorization.

Pre-specified analysis plan (no fishing):
  1. Prime-hit block lists per eligible r in {1,2,4,5,7,8}.
  2. Gap constancy check (would indicate an arithmetic progression).
  3. Residue concentration of hit blocks mod m, m=3..12 (beyond parity).
  4. Named near-miss continuation checks from the 9x9 record.
"""
import json

# ---------- arithmetic ----------
def factorize(k):
    tmp, parts = k, []
    d = 2
    while d * d <= tmp:
        e = 0
        while tmp % d == 0:
            tmp //= d
            e += 1
        if e:
            parts.append(f"{d}^{e}" if e > 1 else str(d))
        d += 1 if d == 2 else 2
    if tmp > 1:
        parts.append(str(tmp))
    return parts

def is_prime(k):
    if k < 2:
        return False
    if k % 2 == 0:
        return k == 2
    d = 3
    while d * d <= k:
        if k % d == 0:
            return False
        d += 2
    return True

# ---------- records ----------
recs = {}
for r in range(1, 10):
    for b in range(1, 36):
        v = 9 * b + r
        p = is_prime(v)
        recs[(r, b)] = {
            "r": r, "b": b, "v": v,
            "factorization": [] if p else factorize(v),
            "parity": "even" if v % 2 == 0 else "odd",
            "is_prime": p,
        }

# ---------- verifications ----------
par_ok = all(recs[(r, b)]["parity"] == ("even" if (r + b) % 2 == 0 else "odd")
             for r in range(1, 10) for b in range(1, 36))
print("parity rule partner-parity == (r+b) mod 2:", par_ok, "[exact]")

mod3_none_prime = all(not recs[(r, b)]["is_prime"]
                      for r in (3, 6, 9) for b in range(1, 36))
mod3_div = all((9 * b + r) % 3 == 0 for r in (3, 6, 9) for b in range(1, 36))
print("r in {3,6,9}: no prime hits:", mod3_none_prime,
      "| all 9b+r divisible by 3:", mod3_div, "[exact, elementary]")

# control: independent sieve to 324, cross-check every primality call
N = 324
sv = [True] * (N + 1)
sv[0] = sv[1] = False
for d in range(2, int(N ** 0.5) + 1):
    if sv[d]:
        for m in range(d * d, N + 1, d):
            sv[m] = False
ctrl_ok = all(recs[(r, b)]["is_prime"] == sv[9 * b + r]
              for r in range(1, 10) for b in range(1, 36))
print("control (trial division vs independent sieve):", ctrl_ok)

# hit-parity constraint: prime hits (v>2, so v odd) need b+r odd
ELIG = (1, 2, 4, 5, 7, 8)
hits = {r: [b for b in range(1, 36) if recs[(r, b)]["is_prime"]] for r in ELIG}
hitpar_ok = all((r + b) % 2 == 1 for r in ELIG for b in hits[r])
print("prime hits all at b+r odd (v odd):", hitpar_ok, "[exact, elementary]")

# ---------- markdown record ----------
L = []
L.append("# Across-the-hole pairing record: 1..9 against blocks to 324 (18x18)")
L.append("")
L.append("Pairs (r, 9b+r) for r=1..9, blocks b=1..35 "
         "(18x18 = 324 numbers = 36 blocks of nine; block 0 is the base).")
L.append("Parity flips on odd blocks, preserves on even [exact].")
L.append("P = prime. Factorization shown for composites (the history each carries).")
L.append("")
L.append("| r | " + " | ".join(f"b={b} ({9*b+1}..{9*b+9})" for b in range(1, 36)) + " |")
L.append("|" + "---|" * 36)
for r in range(1, 10):
    cells = []
    for b in range(1, 36):
        d = recs[(r, b)]
        cells.append(f"**{d['v']}P**" if d["is_prime"] else f"{d['v']}={'x'.join(d['factorization'])}")
    L.append("| " + str(r) + " | " + " | ".join(cells) + " |")
L.append("")
L.append("## Exact structural facts in this record")
L.append("- Parity: block b flips parity iff b odd (9b odd). [exact]")
L.append("- r multiple of 3 -> every partner 9b+r divisible by 3 -> never prime. [exact, elementary]")
L.append("- r coprime to 9 ({1,2,4,5,7,8}): partners form the progression r mod 9; "
         "Dirichlet -> infinitely many prime hits; positions irregular. [exact theorem + classical]")
L.append("- Prime hits (v>2, hence v odd) occur only at blocks with b+r odd. [exact, elementary]")
L.append("")

# ---------- prime-hit analysis ----------
A = []
A.append("## Prime-hit analysis (blocks b=1..35)")
A.append("")
A.append("Pre-specified plan: hit lists, gap constancy, residue concentration mod 3..12, "
         "named near-miss continuations. Null: irregular hits, no pattern "
         "(consistent with classical prime irregularity in arithmetic progressions).")
A.append("")
for r in ELIG:
    h = hits[r]
    gaps = [h[i+1] - h[i] for i in range(len(h) - 1)]
    A.append(f"- r={r}: prime hits at blocks {h} (count {len(h)}); gaps {gaps} "
             f"[computationally verified]")
A.append("")
# gap constancy -> arithmetic progression?
const = {r: (len(set([hits[r][i+1]-hits[r][i] for i in range(len(hits[r])-1)])) == 1)
         for r in ELIG}
A.append(f"- Gap constancy (arithmetic progression of hit blocks): {const} -- "
         "no eligible residue has constant gaps. [computationally verified]")
# residue concentration mod m, m=3..12 (parity mod 2 already forced: b+r odd)
conc = []
for r in ELIG:
    for m in range(3, 13):
        classes = set(b % m for b in hits[r])
        if len(classes) == 1:
            conc.append((r, m, classes))
A.append(f"- Residue concentration: hit blocks confined to a single class mod m "
         f"(m=3..12, beyond forced parity): {conc if conc else 'none'} "
         f"[computationally verified]")
# named near-misses from the 9x9 record
A.append("- Near-miss r=1 (hits at b=2,4,8 looked like powers of two at 9x9 scale): "
         f"b=16 -> 145 = {'x'.join(factorize(145))} (composite) -- pattern broken. [looked-at, not found]")
A.append("- Near-miss r=5 (hits at even blocks 2,4,6 at 9x9 scale): "
         f"b=8 -> 77 = {'x'.join(factorize(77))} (composite) -- pattern broken. [looked-at, not found]")
A.append("")
A.append("## Verdict")
A.append("")
A.append("Null holds at the 35-block scale: prime-hit positions are irregular, with no "
         "periodicity, no arithmetic progression, and no residue concentration beyond the "
         "exact parity constraint. [computationally verified null, 35 blocks]")
A.append("")
A.append("Boundary: this null is scale-bound. Whether structure emerges at larger scales "
         "(36x36 and beyond) is open and untested here. The exact structural facts above "
         "(parity alternation, mod-3 exclusion, hit-parity constraint) are the only "
         "predictive content this record carries.")
L.extend(A)

md_path = "/home/hatch/workspace/prime-sieve-geometry/across_hole_pairing_record_18x18.md"
with open(md_path, "w") as f:
    f.write("\n".join(L) + "\n")
print("wrote", md_path)

# ---------- json ----------
J = {
    "meta": {
        "definition": "partner value v = 9*b + r, r=1..9, b=1..35 (block 0 = base)",
        "scale": "18x18 = 324 numbers = 36 blocks of nine",
        "parity_rule": "partner parity == (r+b) mod 2 [exact]",
        "mod3_exclusion": "r in {3,6,9} -> 9b+r divisible by 3, never prime [exact, elementary]",
        "verifications": {
            "parity_rule": par_ok,
            "mod3_exclusion": mod3_none_prime and mod3_div,
            "sieve_control": ctrl_ok,
            "hit_parity_constraint": hitpar_ok,
        },
    },
    "records": [recs[(r, b)] for r in range(1, 10) for b in range(1, 36)],
    "prime_hits": {str(r): hits[r] for r in ELIG},
}
json_path = "/home/hatch/workspace/prime-sieve-geometry/across_hole_pairing_record_18x18.json"
with open(json_path, "w") as f:
    json.dump(J, f, indent=1)
print("wrote", json_path)

# ---------- stdout analysis summary ----------
print("\n--- prime-hit block lists (computationally verified) ---")
for r in ELIG:
    h = hits[r]
    gaps = [h[i+1] - h[i] for i in range(len(h) - 1)]
    print(f"r={r}: hits={h} count={len(h)} gaps={gaps}")
print("gap-constancy (progression):", const)
print("residue concentration mod 3..12:", conc if conc else "none")
