#!/usr/bin/env python3
"""9c' (corrected): Fejer-Riesz support of the saturated degree-16 optimizer.

F16(phi) = sum a_k cos(k phi) = |sum c_k e^{ik phi}|^2  =>
a_0 = sum c_k^2,  a_j = 2 sum_k c_k c_{k+j} (j>=1).

Enumerate all REAL Fejer-Riesz factors (conjugate-symmetric zero choices)
and find minimal support. Also quantify a_k sparsity.
"""
import numpy as np
import itertools

c_pub = np.array([1.0, -2.09100370089199, 0.414661861733616, 4.94973437766435,
    -2.26052224951171, -8.58599241204357, 6.87053689828658, 22.6412990090005,
    -6.76222005424994, -50.2233943767588, 8.07550113395201, 223.771572768515,
    487.278135806977, 597.268928658734, 473.937203439807, 237.271715181426,
    59.6961898512813])
a_pub = np.array([1.0, 1.74126664022806, 1.128282822804652, 0.5065272432186642,
    0.1253566902628852, 9.35696526707405e-13, 4.546614790384321e-13,
    0.01201214561729989, 0.006875849760911001, 7.77030543093611e-12,
    2.846662294985367e-7, 0.001608306592372963, 0.001017994683287104,
    2.838909054508971e-7, 5.482482041999887e-6, 2.412958794855076e-4,
    1.281001290654868e-4])
n = 16

def coscoeffs(c):
    m = len(c) - 1
    r = np.array([np.dot(c[:m+1-k], c[k:]) for k in range(m+1)])
    a = r.copy(); a[1:] *= 2.0
    return a

a_re = coscoeffs(c_pub)
print("sum c_k^2 =", a_re[0], "(paper ~932023.9)")
print("max |a_re/a_re[0]-a_pub| =", np.max(np.abs(a_re/a_re[0]-a_pub)))

phi = np.linspace(0, np.pi, 200001)
F = sum(a_pub[k]*np.cos(k*phi) for k in range(n+1))
print("min F16 =", F.min())

# zero structure of P(z)=sum c_k z^k
P = np.poly1d(c_pub[::-1])
zeros = P.roots
inside = [z for z in zeros if abs(z) < 1-1e-9]
outside = [z for z in zeros if abs(z) > 1+1e-9]
print(f"zeros: {len(zeros)}, inside {len(inside)}, outside {len(outside)}")

# group inside zeros into conjugate pairs / real singles
pairs, singles = [], []
used = [False]*len(inside)
for i, z in enumerate(inside):
    if used[i]: continue
    if abs(z.imag) < 1e-9:
        singles.append(z.real); used[i] = True
    else:
        for j in range(i+1, len(inside)):
            if not used[j] and abs(inside[j]-np.conj(z)) < 1e-6:
                pairs.append((z, inside[j])); used[i]=used[j]=True; break
        else:
            singles.append(z)  # unpaired (shouldn't happen)
print(f"inside: {len(pairs)} conjugate pairs, {len(singles)} singles")
nchoices = 2**(len(pairs)+len(singles))
print(f"=> {nchoices} real Fejer-Riesz factors")

fixed = list(outside)
best = []
for bits in itertools.product([0,1], repeat=len(pairs)+len(singles)):
    zlist = list(fixed)
    for b, pr in zip(bits[:len(pairs)], pairs):
        zlist += [1/np.conj(w) for w in pr] if b else list(pr)
    for b, z in zip(bits[len(pairs):], singles):
        zlist.append(1/np.conj(z) if b else z)
    cc = np.poly(zlist)[::-1].real  # c0..c16
    cc *= np.sqrt(np.dot(c_pub,c_pub)/np.dot(cc,cc))
    if cc[0] < 0: cc = -cc
    # verify it reproduces a_pub
    assert np.max(np.abs(coscoeffs(cc)/coscoeffs(cc)[0]-a_pub)) < 1e-6, \
        "factor does not reproduce F16"
    for tol in [1e-9, 1e-6, 1e-3]:
        sup = int(np.sum(np.abs(cc) > tol*np.max(np.abs(cc))))
        best.append((tol, sup, cc.copy()))

import collections
for tol in [1e-9, 1e-6, 1e-3]:
    sups = [s for t, s, _ in best if t == tol]
    print(f"tol={tol}: min support {min(sups)}/17, "
          f"max support {max(sups)}/17 over {len(sups)} real factors")
# show the sparsest at 1e-6
cands = [(s, cc) for t, s, cc in best if t == 1e-6]
cands.sort(key=lambda x: x[0])
print("sparsest (1e-6) support:", cands[0][0])
print("its c:", np.round(cands[0][1], 3))
print("\npublished c support at 1e-6:",
      int(np.sum(np.abs(c_pub) > 1e-6*np.max(np.abs(c_pub)))), "/17")
print("a_k nonzero (>1e-9):",
      [k for k in range(n+1) if abs(a_pub[k]) > 1e-9])
