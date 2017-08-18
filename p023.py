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

def sigma(n):
	sigma = 1
	primfac = primefac(n)
	primes = list(set(primfac))
	for p in primes:
		sigma *= ((p**(primfac.count(p) + 1)) - 1)/(p - 1)
	return sigma - n

abundant = []
sums = []
N = 28123
for i in range(1,N+1):
    if sigma(i) > i:
        abundant.append(i)
        for j in range(len(abundant)):
            if i + abundant[j] > N:
                break
            sums.append(i + abundant[j])

sums = set(sums)
nonsums = set(range(N+1)).difference(sums)
print sum(nonsums)