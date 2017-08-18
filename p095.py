import numpy

def get_primes(n):
	numbers = set(range(n, 1, -1))
	primes = []
	while len(numbers) > 0:
		p = numbers.pop()
		primes.append(p)
		numbers.difference_update(set(range(p**2,n+1,p)))
	return sorted(list(primes))

N = 10**6
primes = get_primes(N)

X = numpy.array(range(N+1))

s = {0:0,1:0}

for p in primes:
	a = 1
	while p**a <= N:
		s[p**a] = (p**a - 1)/(p - 1)
		a += 1

for n in xrange(N+1):
	if n not in s:
		k = 0
		p = primes[k]
		while n % p != 0:
			k += 1
			p = primes[k]
		m = 1
		while n % p == 0:
			n = n/p
			m = m*p
		s[n*m] = (s[n]+n)*(s[m]+m)-n*m

starters = set(range(N+1))
found = set([])

longest = []
while len(starters) > 0:
	n = starters.pop()
	chain = [n]
	while s[n] <= N:
		if s[n] in chain:
			i = chain.index(s[n])
			found.update(set(chain))
			cycle = chain[i:]
			if len(cycle) > len(longest):
				longest = cycle
			break
		if s[n] in found:
			found.update(set(chain))
			break
		n = s[n]
		chain.append(n)
		starters.discard(n)
	if s[n] > N:
		found.update(set(chain))

print min(longest)
