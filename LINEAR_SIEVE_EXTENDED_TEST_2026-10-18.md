# Extended test report: the linear circle sieve

Date: 2026-10-18. Code: `linear_sieve_extended_test.py`.
Results: `linear_sieve_extended_results.json`.
Supersedes the N=2000 bound in `EXPERIMENT_REPORT.md` §2.

## What was tested

The user's construction, specified 2026-09-29 and simulated literally in
`sieve_complex.py`:

- unit circles tile [0,1], [1,2], … on a common axis (the substrate;
  n=1 is degenerate — the [0,1] circle spammed forward *is* the unit tiling,
  so the sharing check starts at the second circle);
- at each step n ≥ 2, point n is "shared" iff a previously spammed circle
  has a boundary there; otherwise draw the diameter-[0,n] circle, spam it
  forward (boundaries at multiples of n), and record n as a new
  prime-sized circle.

## Method note (exact, not heuristic)

`sieve_complex.linear_circle_sieve` computes, per n,
`divs = {p in spammed : n % p == 0}` and calls n unshared iff `divs` is
empty. The extended run computes the same predicate by trial division over
the discovered primes, stopping at p*p > n. If n is composite its least
prime factor is ≤ √n, so the early stop cannot change any verdict:
per-n outcomes are bit-identical to the literal simulation. Only the
materialized multiple-sets were skipped (memory). This is a faithful
re-implementation, not a different sieve.

Each cutoff was compared against an independent bytearray Sieve of
Eratosthenes and against known values of π(N).

## Results

| N       | geometric sieve | classic sieve | π(N) known | exact match | geo time |
|---------|-----------------|---------------|------------|-------------|----------|
| 2,000   | 303             | 303           | 303        | yes         | ~0.0 s   |
| 10,000  | 1,229           | 1,229         | 1,229      | yes         | ~0.0 s   |
| 100,000 | 9,592           | 9,592         | 9,592      | yes         | 0.1 s    |
| 1,000,000 | 78,498        | 78,498        | 78,498     | yes         | 1.1 s    |

At every tested cutoff through N = 1,000,000, the unshared points are
*exactly* the primes — element-by-element list equality with the classical
sieve, not just equal counts, and all counts agree with known π(N).

## Standing interpretation (unchanged)

Per `EXPERIMENT_REPORT.md`: point n is shared iff some earlier prime p < n
has a spammed boundary at n, iff p | n, iff n is composite. The geometric
sieve is the Sieve of Eratosthenes drawn as tangent circles. The extension
to 10⁶ confirms the construction's prime-generation behavior three orders
of magnitude further out; it does not change the verdict that the sieve
generates primes by elimination (testing divisibility), it does not predict
them.

## Epistemic label

computationally verified (N ≤ 10⁶, exact list equality vs. independent
classical sieve + known π(N)); the per-n equivalence to the literal
simulation is exact by the least-prime-factor argument above.
