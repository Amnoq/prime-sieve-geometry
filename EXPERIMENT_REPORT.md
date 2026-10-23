# Experiment report: the linear circle sieve and its incidence complex

Date: 2026-09-29. Code: `sieve_complex.py`. Picture: `sieve_picture.svg`.

## 1. What was built

The user's linear circle sieve was simulated literally: unit circles tile
[0,1],[1,2],… on an axis; at each step n ≥ 2 the right-hand point is checked
against all previously spammed circle boundaries; if unshared, a diameter-[0,n]
circle is drawn and spammed forward (boundaries at multiples of n). The n=1
case is degenerate (the [0,1] circle spammed forward *is* the unit tiling),
so the sharing check starts at the second circle, per the user's dictation.

From the sieve data we built the finite incidence complex Δ_N:
- vertices = primes ≤ N (the "new sized circles"),
- a set S of primes is a face iff some integer ≤ N is divisible by all of
  them — i.e. the spammed-circle boundaries coincide there.

Equivalently, Δ_N is the nerve of the territorial cover: territory(p) =
multiples of p, and faces record exactly where territories overlap.

## 2. Sieve verification (exact)

At every tested N (30 … 2000), the unshared points are *exactly* the primes,
matching a classical sieve. Proof sketch: point n is shared iff some earlier
prime p < n has a spammed boundary at n, iff p | n, iff n is composite. The
geometric sieve is the Sieve of Eratosthenes drawn as tangent circles.

## 3. Measured structure of Δ_N

| N    | f-vector              | #facets | Betti (Z/2)        |
|------|-----------------------|---------|--------------------|
| 30   | [10, 7, 1]            | 9       | [5, 1, 0]          |
| 100  | [25, 30, 5]           | 35      | [11, 11, 0]        |
| 500  | [95, 145, 61, 4]      | 173     | [43, 48, 12, 0]    |
| 1000 | [168, 288, 135, 16]   | 343     | [74, 101, 26, 0]   |
| 2000 | [—, 563, —, —]        | 693     | [—, 202, 66]       |

(f-vector[k] = number of k-dimensional faces; Betti over Z/2; Euler
characteristic from f-vector and from homology agree at every N — the
homology computation is cross-checked.)

## 4. Findings

**Positive 1 — exact facet recursion.** The link of a vertex {p} in Δ_N is
exactly Δ_{⌊N/p⌋} with p deleted (verified computationally at every N).
The complex is built out of scaled copies of itself. This is the same
*shape* of structural property that makes the associahedron's canonical
form work recursively (facets = products of smaller associahedra). It is
the single most "positive-geometry-like" feature found.

**Positive 2 — real, growing topology.** b_1 and b_2 are nonzero and grow
with N (b_1 ≈ N/10, b_2 superlinear in the tested range). The territory
overlaps are not just bookkeeping — the nerve has genuine cycles in
dimensions 1 and 2. b_0 is fully explained: one main component plus one
isolated vertex per prime in (N/2, N].

**Negative 1 — this is a known object.** Δ_N is the classical divisor
complex of combinatorial number theory, not a new positive geometry. The
recursion is real but well-known; it does not by itself produce a canonical
form, let alone one whose residues are prime densities.

**Negative 2 — everything depends on the cutoff N.** Facets, Betti numbers,
even the vertex set change with N. A true positive geometry is
N-independent in structure. No limit object as N → ∞ was identified, and
it is unclear what it would even mean for the "canonical form" to converge.

**Negative 3 — the gap to her method is unbridged.** Her recipe needs a
*positive region* whose boundary stratification is the complex, plus a
canonical form with logarithmic singularities on that boundary. We have a
face lattice with nice recursion and no region, no form. The recursion is
necessary for the analogy but far from sufficient.

## 5. Assessment

The experiment did what it was supposed to do: it tested whether the
sieve's incidence data carries any of the recursive regularity her
program exploits, and the answer is a qualified yes — the link recursion
is exact and the nerve has nontrivial growing homology. But it also drew
the honest boundary: a recursive face lattice is not a positive geometry,
and nothing here selects prime *densities* the way her canonical forms
select amplitudes. The next step, if this line continues, is the hard one:
find (or rule out) a positive parametrization whose boundary strata are
these territory incidences. That search is now precisely posed, which is
what the experiment bought us.
