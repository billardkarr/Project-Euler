def tri(n):
	return n*(n+1)/2

def primefac(n): # computes list of prime factors (with repeats)
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac

def sigma(n): # computes # of divisors of n
	sigma = 1
	fac = primefac(n)
	plist = set(fac)

	for p in plist:
		a = sum([p == i for i in fac])
		sigma *= (a + 1)

	return sigma

n = 1
while sigma(tri(n)) < 500:
	n += 1

print "n = %d" % n
print "T(n) = %d" % tri(n)
print "sigma = %d" % sigma(tri(n))


print primefac(1103)