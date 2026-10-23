"""Cross-scale comparison: pairing records at N = 9, 18, 36, 81.
For each N: residues r=1..9, blocks b=1..(N^2/9 - 1), partner v = 9b+r.
Full JSON records + hit analysis per eligible residue + cross-scale verdict.
Pre-registered legs: (claim) scale-stable structure? (polar) null/irregular at
all scales vs PNT-for-AP expected counts; (control) embedding consistency +
sieve cross-check.
"""
import json, math

def primes_upto(n):
    sieve = bytearray(b'\x01') * (n + 1)
    sieve[0:2] = b'\x00\x00'
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i:n + 1:i] = b'\x00' * ((n - i * i) // i + 1)
    return [i for i in range(n + 1) if sieve[i]]

def factorize(k, primes):
    tmp, parts = k, []
    for d in primes:
        if d * d > tmp:
            break
        e = 0
        while tmp % d == 0:
            tmp //= d
            e += 1
        if e:
            parts.append([d, e])
    if tmp > 1:
        parts.append([tmp, 1])
    return parts

def is_prime(k, primes):
    if k < 2:
        return False
    for d in primes:
        if d * d > k:
            break
        if k % d == 0:
            return False
    return True

PR = primes_upto(1000)
WS = '/home/hatch/workspace/prime-sieve-geometry'
scales = {}
for N in (9, 18, 36, 81):
    B = N * N // 9 - 1
    recs = []
    for r in range(1, 10):
        for b in range(1, B + 1):
            v = 9 * b + r
            ip = is_prime(v, PR)
            recs.append({'r': r, 'b': b, 'v': v, 'is_prime': ip,
                         'parity': 'even' if v % 2 == 0 else 'odd',
                         'factorization': factorize(v, PR)})
    scales[N] = {'B': B, 'recs': recs}
    json.dump({'N': N, 'blocks': B, 'records': recs},
              open(f'{WS}/across_hole_pairs_{N}x{N}.json', 'w'))
    print(f"{N}x{N}: blocks 1..{B}, records {len(recs)}", flush=True)

# control: independent sieve cross-check to max value
SIEVE = set(primes_upto(81 * 81))
for N in (9, 18, 36, 81):
    bad = [x for x in scales[N]['recs']
           if x['is_prime'] != (x['v'] in SIEVE)]
    print(f"{N}x{N}: sieve cross-check mismatches: {len(bad)}", flush=True)
    assert not bad

# control: embedding consistency (smaller scale hits == larger restricted)
for N1, N2 in ((9, 18), (18, 36), (36, 81)):
    B1 = scales[N1]['B']
    for r in (1, 2, 4, 5, 7, 8):
        h1 = sorted(x['b'] for x in scales[N1]['recs'] if x['r'] == r and x['is_prime'])
        h2 = sorted(x['b'] for x in scales[N2]['recs'] if x['r'] == r and x['is_prime'] and x['b'] <= B1)
        assert h1 == h2, (N1, N2, r)
print("embedding consistency: smaller-scale hits == larger restricted, all residues [exact]", flush=True)

lines = []
lines.append("# Cross-scale comparison: 9×9, 18×18, 36×36, 81×81")
lines.append("")
lines.append("Pairing record v=9b+r, residues r=1..9, blocks b=1..B (B=N²/9−1).")
lines.append("Legs: (claim) scale-stable structure? (polar) null — irregular at all")
lines.append("scales vs PNT-for-AP expected counts; (control) embedding + sieve cross-check.")
lines.append("")
for N in (9, 18, 36, 81):
    B = scales[N]['B']
    recs = scales[N]['recs']
    lines.append(f"## {N}×{N} — blocks 1..{B}")
    for r in (1, 2, 4, 5, 7, 8):
        hits = [x['b'] for x in recs if x['r'] == r and x['is_prime']]
        gaps = [hits[i + 1] - hits[i] for i in range(len(hits) - 1)]
        # PNT-for-AP heuristic: odd values here are = r mod 18 with (r,18)=1,
        # so P(prime) ~= 18/(phi(18)*ln v) = 3/ln v  [exact: phi(18)=6]
        exp = sum(3 / math.log(9 * b + r) for b in range(1, B + 1) if (9 * b + r) % 2 == 1)
        gh = {}
        for g in gaps:
            gh[g] = gh.get(g, 0) + 1
        lines.append(f"- r={r}: hits={len(hits)} (PNT-AP expected ~{exp:.1f}), "
                     f"blocks={hits}")
        lines.append(f"  gaps={gaps}")
        lines.append(f"  gap histogram={dict(sorted(gh.items()))}")
    lines.append("")

lines.append("## Cross-scale verdict")
lines.append("")
lines.append("Embedding: each scale's hit list extends the previous exactly (verified) —")
lines.append("no hits appear, disappear, or move across scales. What changes with scale is")
lines.append("only sample size, not structure.")
lines.append("")
open(f'{WS}/across_hole_cross_scale.md', 'w').write("\n".join(lines) + "\n")
print("wrote across_hole_cross_scale.md")
