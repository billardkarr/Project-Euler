import numpy as np

def isprime(n):
	n = np.abs(n)
	if n in [0,1]:
		return False
	primfac = []
	d = 0
	while odd_primes[d]**2 <= n:
		while n % odd_primes[d] == 0:
			return False
		d += 1
	return True

odd_primes = [3]
odd_comps = []
squares = set([])

found = False
n = 1
k = 1
while found == False:
	n += 2
	if isprime(n):
		odd_primes.append(n)
	else:
		odd_comps.append(n)
		if k*k < n/2:
			squares.add(k*k)
			k += 1
		check = set([(n - p)/2 for p in odd_primes])
		if check.isdisjoint(squares):
			print n
			found = True