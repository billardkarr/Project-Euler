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

N = 10000
amicable_sum = 0

for i in range(1,N):
	if sigma(sigma(i)) == i:
		if sigma(i) != i:
			amicable_sum += i

print amicable_sum