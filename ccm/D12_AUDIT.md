# D12 Provenance Audit — CCM Reimplementation (2026-09-30)

## Question
Does any zeta-zero information enter the D_log^{(λ,N)} pipeline?
If yes, the spectral coincidence is circular (cf. D12 dead end: rh_final
engineered weights to delete continuous spectrum — answer inserted by hand).

## Pipeline inputs traced

### 1. W_{0,2} (point-mass term)
- Source: paper eq.(4.2), closed form.
- Mathematical origin: the 2Re(f̂(i/2)·overline{f̂(−i/2)}) term in the
  semilocal Weil formula (quadratsemi). Comes from evaluating the test
  function at specific points (s=±i/2 related to the pole structure).
- Zero content: NONE. Computed analytically from the test function.
  Does not sum over zeros. Does not use zero locations.

### 2. W_R (archimedean term)
- Source: paper (weinfty), derived from (bombtestR).
- Mathematical origin: the ∫|f̂|²θ'/π term. Involves log(4π), Euler's γ,
  and integrals against the archimedean density ρ(x)=e^{x/2}/(e^x−e^{−x}).
  Comes from the gamma factor in the functional equation.
- Zero content: NONE. The digamma/hypergeometric closed forms are
  pure analysis. No zero sums, no zero locations.

### 3. W_p (prime sum) — THE D12 AUDIT BOUNDARY
- Source: paper eq.(bomp): Σ_{1<k≤λ²} Λ(k)k^{−1/2}q(U_n,U_m)(log k).
- Mathematical origin: the −ΣΛ⟨f|T_{p} f⟩ term. Von Mangoldt Λ(k)
  is nonzero exactly on prime powers k=p^r, where Λ(p^r)=log p.
- Zero content: NONE. Input is the set {p^r ≤ λ²} and the values log p.
  This is prime arithmetic, not zero information.
- This is the ONLY arithmetic input to the entire pipeline.

### 4. Basis {V_n}
- Trigonometric polynomials V_n=κ(U_n), U_n=L^{−1/2}e^{2πinx/L}.
- Zero content: NONE. Pure Fourier analysis.

### 5. Eigensolve (even block, inverse iteration)
- Finds smallest eigenvalue/eigenvector of the even-block matrix.
- Zero content: NONE. Pure linear algebra.

### 6. ξ̂(z) construction and root-finding
- ξ̂(z)=2L^{−1/2}sin(zL/2)Σξ_j/(z−2πj/L). Roots via sign-change scan.
- Zero content: NONE. The formula is from the paper (Prop 6.x);
  root-finding is numerical analysis.

### 7. Comparison with true zeros
- True zeta zeros used ONLY to compute errors AFTER the fact.
- They do NOT enter the matrix, the eigensolve, or ξ̂.
- This is validation, not input.

## Verdict: CLEAN
No zeta-zero information enters the pipeline at any stage. The only
arithmetic input is prime powers via von Mangoldt (eq. bomp). The zeros
emerge from the spectrum; they are not inserted.

## Contrast with D12 dead end (rh_final)
- D12: weight function was ENGINEERED to delete unwanted spectrum.
  The "answer" (zero locations) was built into the weight by hand.
- Here: the weight is von Mangoldt Λ(k), the NATURAL arithmetic weight
  from the explicit formula. It is not tuned to produce zeros; it is
  the prime-counting weight. The zeros emerge; they are not imposed.

## Residual concern
The choice of (λ,N)=(√13,10) follows the paper. A skeptic could worry
the parameters were tuned to match zeros. Mitigation: the paper reports
the phenomenon across (λ,N) (x=9,12,13,14; N up to 120), and the
reproduction confirms 999 digits at larger cutoffs. Our convergence
study (todo item 5) will test multiple (λ,N) to confirm robustness.
