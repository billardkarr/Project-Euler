def digits(n):
	digits = []
	while n > 0:
		digits += [ n % 10 ]
		n = n/10
	return digits

primes = [2,3,5,7,11,13,17]
starters = range(10**2,10**3)

candidates = []
for s in starters:
	if len(set(digits(s))) == 3:
		candidates.append(s)
candidates = [candidates]

for p in primes:
	candidates.append([])
	for c in candidates[-2]:
		cdigs = digits(c)
		left = set(range(10)).difference(set(cdigs))
		for l in left:
			if (10*(c%100)+l) % p == 0:
				candidates[-1].append(10*c + l)
	candidates.remove(candidates[0])

print sum(candidates[-1])