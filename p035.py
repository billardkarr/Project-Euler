N = 10**6

numbers = set(range(N-1, 1, -1))
primes = set([])
while len(numbers) > 0:
	p = numbers.pop()
	primes.add(p)
	numbers.difference_update(set(range(p,N,p)))

def rotations(n):
	rotations = [n]
	d = -1
	k = n
	while k > 0:
		k = k/10
		d += 1
	n = (10**d)*(n%10) + n/10
	while n not in rotations:
		rotations.append(n)
		n = (10**d)*(n%10) + n/10
	return set(rotations)

circular = set([])

for p in primes:
	orbit = rotations(p)
	if orbit.issubset(primes):
		circular = circular.union(orbit)

print len(circular)