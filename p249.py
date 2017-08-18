N = 50
tbd = set(range(N-1,1,-1))
primes = set([])

while len(tbd) > 0:
	p = tbd.pop()
	primes.add(p)
	tbd.difference_update(set(range(p**2,N,p)))
smallprimes = sorted(list(primes))

N = sum(primes)
tbd = set(range(N-1,1,-1))
primes = set([])

while len(tbd) > 0:
	p = tbd.pop()
	primes.add(p)
	tbd.difference_update(set(range(p**2,N,p)))
primes = sorted(list(primes))

from itertools import combinations

count = 0
for r in range(len(smallprimes)):
	for S in combinations(smallprimes,r):
		if sum(S) in primes:
			print S
			count += 1

print count