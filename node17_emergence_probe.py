#!/usr/bin/env python3
"""
Node 17 emergence-ordering probe (2026-10-13).

Observation-first probe of the orienting hypothesis:
"derive the next distinction from the point where all distinctions coincide."

For S_k = first k primes (k = 3..12), the near-origin fan separates pairs
(d1, d2) in order of increasing (sqrt(d2) - sqrt(d1)) -- the emergence
ordering. When p_{k+1} joins, its new pairs insert at definite ranks.
We record the orderings, the insertion ranks, and look for any regularity.

Epistemic status of outputs: enumerations are [computationally verified];
any regularity claim is [observed pattern] or [null].
"""
import json
import math
from datetime import date

# First 13 primes (need p_{k+1} for k up to 12)
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]

TIE_TOL = 1e-12


def emergence_ordering(S):
    """Return list of ((d1, d2), gap) sorted by gap ascending, gap = sqrt(d2)-sqrt(d1)."""
    pairs = []
    for i in range(len(S)):
        for j in range(i + 1, len(S)):
            d1, d2 = S[i], S[j]
            pairs.append(((d1, d2), math.sqrt(d2) - math.sqrt(d1)))
    pairs.sort(key=lambda t: t[1])
    return pairs


def detect_ties(ordering):
    """Return groups of indices (0-based) whose gaps agree within TIE_TOL."""
    groups = []
    i = 0
    n = len(ordering)
    while i < n:
        j = i
        while j + 1 < n and abs(ordering[j + 1][1] - ordering[i][1]) < TIE_TOL:
            j += 1
        if j > i:
            groups.append(list(range(i, j + 1)))
        i = j + 1
    return groups


def insertion_ranks(ordering, new_pairs):
    """
    For each new pair (gap value), return the 1-based rank at which it would
    insert into the existing ordering (bisect-left position + 1), plus the
    rank range if it ties an existing gap within TIE_TOL.
    """
    gaps = [g for _, g in ordering]
    out = []
    for (d1, d2), g in new_pairs:
        # bisect left
        lo, hi = 0, len(gaps)
        while lo < hi:
            mid = (lo + hi) // 2
            if gaps[mid] < g - TIE_TOL:
                lo = mid + 1
            else:
                hi = mid
        rank_lo = lo + 1  # 1-based
        # extend over ties
        k = lo
        while k < len(gaps) and abs(gaps[k] - g) < TIE_TOL:
            k += 1
        rank_hi = k  # 1-based inclusive upper = k (since k is count of <= )
        out.append({"pair": (d1, d2), "gap": g,
                    "rank_lo": rank_lo, "rank_hi": rank_hi,
                    "n_existing": len(gaps)})
    return out


def main():
    results = {"date": str(date.today()), "k_results": []}
    for k in range(3, 13):
        S_k = PRIMES[:k]
        q = PRIMES[k]  # p_{k+1}
        ordering = emergence_ordering(S_k)
        ties = detect_ties(ordering)
        new_pairs = [((q, d), math.sqrt(q) - math.sqrt(d)) for d in S_k]
        # note: pairs stored as (larger, smaller) for the new prime; normalize below
        new_pairs = [((d, q), g) for (qq, d), g in new_pairs]
        ranks = insertion_ranks(ordering, new_pairs)

        smallest = ordering[0]
        largest = ordering[-1]
        involves_max = (smallest[0][0] == S_k[-1] or smallest[0][1] == S_k[-1])

        # where do the new pairs land, as fractions of the ordering length
        n = len(ordering)
        fracs = [(r["rank_lo"] - 1) / n for r in ranks]  # 0 = very first, ~1 = tail

        results["k_results"].append({
            "k": k,
            "S_k": S_k,
            "next_prime": q,
            "n_pairs": n,
            "ordering": [{"pair": list(p), "gap": g} for p, g in ordering],
            "ties": ties,
            "smallest_gap": {"pair": list(smallest[0]), "gap": smallest[1],
                             "involves_max_Sk": involves_max},
            "largest_gap": {"pair": list(largest[0]), "gap": largest[1]},
            "insertion_ranks": ranks,
            "insertion_fraction_of_ordering": fracs,
        })

    with open("/home/hatch/workspace/prime-sieve-geometry/node17_emergence_probe.json",
              "w") as f:
        json.dump(results, f, indent=1)

    # ---- printed summary for the report ----
    print("k | S_k size | n_pairs | next p | smallest gap (pair) | involves max | "
          "new-pair insertion ranks (of n) | frac positions")
    for r in results["k_results"]:
        sg = r["smallest_gap"]
        ir = [(x["rank_lo"], x["rank_hi"], x["n_existing"]) for x in r["insertion_ranks"]]
        fr = [f"{x:.2f}" for x in r["insertion_fraction_of_ordering"]]
        print(f"{r['k']:2d} | {len(r['S_k']):7d} | {r['n_pairs']:7d} | {r['next_prime']:6d} | "
              f"{sg['gap']:.6f} {sg['pair']} | {str(sg['involves_max_Sk']):5s} | {ir} | {fr}")
    # tie report
    any_ties = [(r["k"], r["ties"]) for r in results["k_results"] if r["ties"]]
    print("\nTies within TIE_TOL=1e-12:", any_ties if any_ties else "none")


if __name__ == "__main__":
    main()
