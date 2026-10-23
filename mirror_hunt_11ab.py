import numpy as np, math
PRIMES = [2,3,5,7,11,13,17,19]
L = np.array([math.log(p) for p in PRIMES])
R = len(L)

def G(k):
    shape = np.shape(k)
    kf = np.atleast_1d(np.asarray(k, float)).ravel()
    s = np.sin(kf[None,:]*L[:,None]/2)
    c = np.cos(kf[None,:]*L[:,None]/2)
    out = np.zeros(kf.size)
    for j in range(R):
        m = np.ones(R, bool); m[j]=False
        out += s[j]*np.prod(c[m], axis=0)
    return out.reshape(shape)

print("1) loop lengths distinct:", len(set(np.round(L,12)))==R, "(=> metric automorphisms trivial)")

xs = np.linspace(0.01, 400, 20000)
print("2) oddness about 0: max|G(-k)+G(k)| =", float(np.max(np.abs(G(-xs)+G(xs)))))

cs = np.linspace(0.05, 60, 1200)
X  = np.linspace(0.01, 30, 1500)
A = G(cs[:,None]+X[None,:])
B = G(cs[:,None]-X[None,:])
even_dev = np.max(np.abs(A-B), axis=1)
odd_dev  = np.max(np.abs(A+B), axis=1)
ie = int(np.argmin(even_dev)); io = int(np.argmin(odd_dev))
print("3) best EVEN-about-c center: c=%.4f dev=%.3e" % (cs[ie], even_dev[ie]))
print("   best ODD-about-c  center: c=%.4f dev=%.3e" % (cs[io], odd_dev[io]))
mask = cs > 1.0
io2 = int(np.argmin(np.where(mask, odd_dev, np.inf)))
print("   best ODD-about-c with c>1: c=%.4f dev=%.3e" % (cs[io2], odd_dev[io2]))
print("   median even_dev: %.3f | median odd_dev: %.3f" % (float(np.median(even_dev)), float(np.median(odd_dev))))
print("   (|G| <= %d everywhere; machine-exact symmetry would read ~1e-12)" % R)
