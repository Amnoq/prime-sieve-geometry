# Exact Structural Results on Primorial Wheels

## Labeled closures, the 2310 height-product theorem, and the permanent coarse lattice

*Consolidation of prime-claim-bench runs 026–028 (2026-10-18), commissioned as one coherent package. Every claim below is stated and checked in exact arithmetic — integers and rationals only; no floating point, no approximation, no imported machinery. Labeled throughout as **structural results on the primorial wheels**, not as physics. Proofs are either short derivations given in full or finite exact computations (integer/gcd/Fraction arithmetic), reproducible bit-identically from the archived runs.*

---

### 0. Objects

- **Stages.** $S_k = \{p_1, \dots, p_k\}$ = the first $k$ sieve-generated sizes, $p_1 = 2 < p_2 = 3 < p_3 = 5 < \cdots$ (the circle-sieve generation rule: generate size $n$ iff no existing size divides $n$; verified identical to Eratosthenes through $10^4$). $S_0 = \varnothing$.
- **Wheels.** $W_k = \prod S_k$ ($W_0 = 1$). A *survivor* (mod $W_k$) is a residue coprime to every $d \in S_k$; there are $\varphi(W_k)$ per period.
- **Height product.** For finite $S$: $r_d(x) = x - d\lfloor x/d \rfloor$, $H_d(x)^2 = r_d(x)\,(d - r_d(x))$, $P_S(x) = \prod_{d \in S} H_d(x)^2 \ge 0$. A *survivor region* is a maximal open interval with $P_S > 0$ of width 2, necessarily $(m-1, m+1)$ with $m$ coprime to all of $S$.
- **Balance.** For $m$ a survivor, $B_k(m) = \sum_{d \in S_k} f_d(m \bmod d)$ with $f_d(r) = \frac{1}{r} - \frac{1}{\,d-r\,} = \frac{d - 2r}{r(d-r)}$ (exact rational; $r \ne 0$ since $m$ is a survivor).
- **Charge lattices.** $\Lambda_k = \frac{1}{M_k}\mathbb{Z}$ where $M_k$ is the l.c.m. of all denominators of $B_k$-values over the stage-$k$ survivors. Computed: $M_2 = 2,\; M_3 = 12,\; M_4 = 60,\; M_5 = 2520$.

---

### 1. The 2310 height-product theorem (run 026)

**Theorem 1 (exact-center maxima).** Let $S = (2,3,5,7,11)$, $W = 2310$. On each survivor region $(m-1,m+1)$, $\log P_S$ is strictly concave, hence has exactly one maximizer. Then $m$ itself is the maximizer **iff**
$$\sum_{d \in S}\left[\frac{1}{m \bmod d} - \frac{1}{\,d - (m \bmod d)\,}\right] = 0 \tag{*}$$
as an exact rational identity (the $d = 2$ term vanishes identically since $m$ is odd). Consequently, exactly **2 of the 480** survivor residues mod 2310 — the mirror pair $\{523, 1787\}$, $523 + 1787 = W$ — have their height-product maximum sitting exactly at the survivor integer.

*Proof.* On the open interval $(m-1,m+1)$ no multiple of any $d \in S$ lies strictly inside (if $kd \in (m-1,m+1)$ then $|kd - m| < 1$ with $kd - m \in \mathbb{Z}$ and $kd \ne m$ since $m$ is coprime to $d$ — impossible), so each $r_d$ is linear of slope 1 there and
$$\frac{d}{dx}\log P_S(x) = \sum_{d \in S} \frac{d - 2r_d(x)}{r_d(x)\,(d - r_d(x))}.$$
At the integer center $x = m$ this is exactly the left side of $(*)$. Strict concavity (sum of strictly concave logs) makes the critical point the unique global maximizer. ∎

*The pair, explicitly.* Mod $(3,5,7,11)$: $523 \mapsto (1,3,5,6)$ and
$$\frac11 - \frac12 + \frac13 - \frac12 + \frac15 - \frac12 + \frac16 - \frac15 = \frac12 - \frac16 - \frac{3}{10} - \frac{1}{30} = \frac{15 - 5 - 9 - 1}{30} = 0.$$
$1787 \mapsto (2,2,2,5)$ is the termwise negation. Reflection $r_d \leftrightarrow d - r_d$ negates every term of $(*)$, so solutions necessarily come in mirror pairs $m$, $W - m$ (realized together by CRT; $m'$ is a survivor iff $m$ is).

*Per-period census (exact, finite).* Exact-center maxima per wheel period: $S = (2)$: 1/1 — degenerate, every survivor region (the $d = 2$ term is identically 0); $S = (2,3)$: 0/2; $S = (2,3,5)$: 0/8; $S = (2,3,5,7)$: 0/48; $S = (2,3,5,7,11)$: 2/480, the pair above. Below 20000 the latter are $523, 1787, 2833, 4097, \dots$ (17 hits), alternating the two residue patterns.

*Status: exact theorem + exact finite verification.*

---

### 2. Labeled closures (run 027)

**Definitions.** The *next internal seed* at stage $k$ is $p_{k+1}$ = the least integer $> p_k$ with $p_{k+1} \bmod p_i \ne 0$ for all $i \le k$ ($p_1 = 2$; 1 is the unit, not a number). Its *discrete label* is the residue tuple $L(p_{k+1}) = (p_{k+1} \bmod p_1, \dots, p_{k+1} \bmod p_k)$. The *labeled closure* is the pair $(p_{k+1}, L(p_{k+1}))$.

**Consistency conditions** ("every new seed reaches back and close relative to all previous closures"), all exact finite combinatorics, verified for $k = 0..6$:
- **(C1) Nonvanishing.** Every label component is nonzero — the generation rule itself.
- **(C2) Reach-back.** For each $j \le k$, $p_{k+1} \bmod W_j$ is a stage-$j$ survivor ($\gcd = 1$): the label restricts correctly to every previous closure's wheel.
- **(C3) Firstness.** $p_{k+1}$ is the least integer $> p_k$ satisfying C1 — the seed closes the open question "what comes next."
- **(C4) Mirror pairing.** The full datum is $\{L, -L \bmod W_k\}$; for $k \ge 2$ the involution $r \mapsto W_k - r$ is fixed-point-free on survivors (fixed points need $2r \equiv 0 \bmod W_k$, i.e. $r = 0$ or $r = W_k/2$; $r = 0$ never survives and $W_k/2$ is even, sharing every odd factor with $W_k$). At $k = 1$ the sole survivor is self-mirror (degenerate).

*Status: exact (definitions + finite verification).*

---

### 3. The three fragments (run 027)

Derived label-invariants; graded honestly — each is discrete labeled structure the sieve already carries, not a derivation of the corresponding physics.

**3.1 Binary — SIGNAL, exact.** The mirror-half bit $\beta \in \{0,1\}$ (residue below/above $W_k/2$) is a well-defined two-valued label with canonical flip for every $k \ge 2$. *Boundary:* a $\mathbb{Z}/2$ pairing, not spin-1/2; "spin-like" is analogical.

**3.2 Ternary — SIGNAL, fragment.** $\tau = \operatorname{sgn} B_k \in \{+, -, 0\}$: all three values are attained in the construction ($0$ degenerately at the first closures via the vanishing $d = 2$ term; non-degenerately at the Theorem-1 exact-center maxima). *Boundary:* no combination rule — nothing composes values the way color does.

**3.3 Charge — FRAGMENT-grade SIGNAL.** The balance values over stage-$k$ survivors lie in $\frac{1}{M_k}\mathbb{Z}$ with $M_2 = 2, M_3 = 12, M_4 = 60, M_5 = 2520$ explicitly computed; smallest positive values attained ($1/2, 1/4, 1/30, 1/60$). Companion, exact: the $p_2 = 3$ closure forces a $\{1/3, 2/3\}$-valued fractional component on *every* later seed's label — thirds as the first nontrivial fractional unit, propagated forever by C1–C4. *Boundaries:* $M_k$ is stage-dependent (not a universal $e/3$); the lattice unit $1/M_k$ need not be attained; "charge" names the lattice structure, not electromagnetism.

---

### 4. The permanent coarse lattice (run 028)

**Theorem 2 (summand permanence).** For $k \ge 2$ and every survivor $m$,
$$B_k(m) = t(m) + R_k(m), \qquad t(m) = \begin{cases} +\tfrac12 & m \equiv 1 \bmod 3 \\ -\tfrac12 & m \equiv 2 \bmod 3 \end{cases}$$
with $R_k(m) = \sum_{d \in S_k,\, d > 3} f_d(m \bmod d)$. The mod-3 term never leaves once the second closure happens. *Exact by definition of $B_k$; verified on all survivors at $k = 2,3,4,5$.*

**Theorem 3 (nesting).** $M_k \mid M_{k+1}$ (since $S_k \subset S_{k+1}$), hence with $\Lambda_k = \frac{1}{M_k}\mathbb{Z}$:
$$\Lambda_2 \subset \Lambda_3 \subset \Lambda_4 \subset \cdots, \qquad \bigcap_{k \ge 2} \Lambda_k = \Lambda_2 = \tfrac12\mathbb{Z}.$$
The mod-3-generated coarse lattice $\frac12\mathbb{Z}$ sits *inside* every subsequent charge lattice and is precisely their common part — fixed at the second closure, never moves. *Exact: divisibility chain $2 \mid 12 \mid 60 \mid 2520$ verified; intersection is exact since the chain ascends.*

**Theorem 4 (uniqueness of the constant offset).** Flipping *only* the mod-3 component ($1 \leftrightarrow 2$) while fixing all higher residues shifts $B_k$ by exactly $\mp 1$ — $\varphi(W_k)/2$ exact pairs at every stage $k \ge 2$. Among prime closures, $d = 3$ is the *only* one with this property. *Proof:* for prime $d$, $f_d(r) = \frac1r - \frac1{d-r}$ is strictly decreasing and positive on $1 \le r < d/2$ (derivative $-\frac1{r^2} - \frac1{(d-r)^2} < 0$), so $|\,f_d\,|$ takes exactly $\frac{d-1}{2}$ distinct values; a constant flip-offset needs exactly one, i.e. $\frac{d-1}{2} = 1$, i.e. $d = 3$ ($d = 2$ gives the trivial $0$). The mod-5 flip control is non-constant, as claimed.*

**Corollary (class sums — linear relations among balance sums).** For all $k \ge 2$, exactly:
$$\sum_{m \equiv 1\ (3)} B_k(m) = +\frac{\varphi(W_k)}{4}, \qquad \sum_{m \equiv 2\ (3)} B_k(m) = -\frac{\varphi(W_k)}{4}.$$
*Proof:* the $\varphi(W_k)/2$ pairs each contribute $+1$ to the difference of the class sums and $2R(P)$ to their sum; the total sum vanishes by the mirror $m \leftrightarrow W_k - m$ (which negates $B_k$, fixed-point-free for $k \ge 2$). Verified at $k = 2,3,4,5$ (e.g. $\pm 120$ at $k = 5$).*

**Recursion (linear relation across stages).** $B_{k+1}(m) = B_k(m) + f_{p_{k+1}}(m \bmod p_{k+1})$, exact on all stage-$(k+1)$ survivors, verified $k = 2,3,4$.

**Honest null.** By CRT the survivors biject with all-nonzero residue tuples: the mod-3 component imposes *no* restriction on higher components (every higher pattern lifts to exactly both mod-3 values — verified). No new linear relations among tuple components are forced; the emergent structure governs the balance sums, not the tuples.

*Status of §4: exact theorems + exact finite verifications.*

---

### 5. Labels ledger

| # | Claim | Status |
|---|---|---|
| T1 | 2310 height-product theorem (exact-center maxima: 2/480 per period, mirror pair, characterization $(*)$) | exact theorem + exact finite verification |
| T2 | Per-period census at smaller wheels (0 at $(2,3),(2,3,5),(2,3,5,7)$; degenerate all at $(2)$) | exact finite verification |
| C1–C4 | Labeled-closure consistency conditions | exact (definitions + finite verification $k \le 6$) |
| F1 | Binary mirror-half distinction | exact structural |
| F2 | Ternary $\tau = \operatorname{sgn} B$ | fragment (values attained; no combination rule) |
| F3 | Charge lattice quantization + forced thirds | fragment (lattice + unit exact; $M_k$ stage-dependent) |
| T3 | Coarse-lattice nesting, $\bigcap \Lambda_k = \frac12\mathbb{Z}$ | exact theorem + verified chain |
| T4 | Uniqueness of the constant-offset pairing ($d = 3$ only) | exact theorem (+ control verified) |
| Cor | Class-sum relations $\pm\varphi(W_k)/4$; stage recursion | exact (+ verified $k \le 5$ / $k \le 4$) |
| N1 | No new tuple-component relations | honest null (CRT) |

*Open (not claimed): higher wheels ($2\cdot3\cdot5\cdot7\cdot11\cdot13$ and beyond); refinements of the balance function; combination rules for the ternary values; any dynamical or physical content — none is asserted anywhere above.*

---

### 6. Archive

Self-contained rerunnable scripts + captured outputs, each re-run bit-identical (latest full re-verification 2026-10-18):
- `prime-claim-bench/archive/runs/026_maxima_residue_coincidence/` — the 2310 theorem (numerical discovery leg + exact Fraction leg)
- `prime-claim-bench/archive/runs/027_labeled_closures/` — definitions C1–C4, three fragments
- `prime-claim-bench/archive/runs/028_permanent_thirds/` — P1–P7, nesting, uniqueness, class sums
- Index entries 026–028 in `prime-claim-bench/archive/INDEX.md`; decision-tree probe 7 in `prime-sieve-geometry/DECISION_TREE.md` (Node 17).

*This note is the fixed core. Further probes — higher wheels, balance-function refinements, combination-rule attempts — start from here.*
