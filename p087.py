N = 50*(10**6)

import numpy

def get_primes(n):
	n = int(n)+1
	numbers = set(range(n, 1, -1))
	primes = []
	while len(numbers) > 0:
		p = numbers.pop()
		primes.append(p)
		numbers.difference_update(set(range(p**2,n+1,p)))
	return primes

primes1 = get_primes(N**(1.0/2))
primes2 = get_primes(N**(1.0/3))
primes3 = get_primes(N**(1.0/4))

ppts = set([])

for p in primes1:
	for q in primes2:
		for r in primes3:
			a = p**2 + q**3 + r**4
			if a < N:
				ppts.add(a)

print len(ppts)