import numpy as np

def digits(n):
	digits = []
	while n > 0:
		digits += [n % 10]
		n = n/10
	return np.array(digits)

def number(digits):
	power = len(digits)
	return sum( [ digits[i]*10**i for i in range(0,power)])

def get_primes(d):
	n = 10**d
	sieve = [True] * (n/2)
	for i in xrange(3,int(n**0.5)+1,2):
		if sieve[i/2]:
			sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
	primes = [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]
	primes = np.array(sorted(primes))
	primes = primes[primes > 10**(d-1)]
	primes = list(primes)
	return primes

d = 6
N = 10**d
m = 3
count = 8

primes = get_primes(d)

candidates = []
for p in primes:
	for i in range(10):
		if sum(digits(p) == i) >= m:
			candidates.append([p,i])

print len(candidates)
print 

found = False
for [p,i] in candidates:
	print p,i
	digs = digits(p)
	family = []
	for j in range(10):
		q = digs.copy()
		q[q == i] = j
		q = number(q)
		if q in primes:
			family.append(q)
	d = len(digits(max(family)))
	for q in family:
		if len(digits(q)) != d:
			family.remove(q)		
	if len(family) == count:
		print family
		break