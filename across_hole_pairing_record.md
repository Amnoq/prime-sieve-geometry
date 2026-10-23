# Across-the-hole pairing record: 1..9 against blocks to 81

Pairs (n, 9b+n) for n=1..9, blocks b=1..8. Parity flips on odd blocks, preserves on even [exact].
P = prime. Factorization shown for composites (the history each carries).

| n | b=1 (10..18) | b=2 (19..27) | b=3 (28..36) | b=4 (37..45) | b=5 (46..54) | b=6 (55..63) | b=7 (64..72) | b=8 (73..81) |
|---|---|---|---|---|---|---|---|---|
| 1 | 10=2x5 | **19P** | 28=2^2x7 | **37P** | 46=2x23 | 55=5x11 | 64=2^6 | **73P** |
| 2 | **11P** | 20=2^2x5 | **29P** | 38=2x19 | **47P** | 56=2^3x7 | 65=5x13 | 74=2x37 |
| 3 | 12=2^2x3 | 21=3x7 | 30=2x3x5 | 39=3x13 | 48=2^4x3 | 57=3x19 | 66=2x3x11 | 75=3x5^2 |
| 4 | **13P** | 22=2x11 | **31P** | 40=2^3x5 | 49=7^2 | 58=2x29 | **67P** | 76=2^2x19 |
| 5 | 14=2x7 | **23P** | 32=2^5 | **41P** | 50=2x5^2 | **59P** | 68=2^2x17 | 77=7x11 |
| 6 | 15=3x5 | 24=2^3x3 | 33=3x11 | 42=2x3x7 | 51=3x17 | 60=2^2x3x5 | 69=3x23 | 78=2x3x13 |
| 7 | 16=2^4 | 25=5^2 | 34=2x17 | **43P** | 52=2^2x13 | **61P** | 70=2x5x7 | **79P** |
| 8 | **17P** | 26=2x13 | 35=5x7 | 44=2^2x11 | **53P** | 62=2x31 | **71P** | 80=2^4x5 |
| 9 | 18=2x3^2 | 27=3^3 | 36=2^2x3^2 | 45=3^2x5 | 54=2x3^3 | 63=3^2x7 | 72=2^3x3^2 | 81=3^4 |

## Exact structural facts in this record
- Parity: block b flips parity iff b odd (9b odd). [exact]
- n multiple of 3 -> all partners multiples of 3 -> never prime. [exact, elementary]
- n coprime to 9 ({1,2,4,5,7,8}): partners form progression n mod 9, Dirichlet gives infinitely many prime hits; positions irregular. [exact theorem + classical]
