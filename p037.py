N = 10**6

numbers = set(range(N-1, 1, -1))
primes = set([])
while len(numbers) > 0:
	p = numbers.pop()
	primes.add(p)
	numbers.difference_update(set(range(p*2,N,p)))

def trunctions(n):
	left = set([n])
	right = set([n])
	d = -1
	k = n
	while k >= 10:
		k = k/10
		right.add(k)
		d += 1
	d += 1
	while n >= 10:
		n = n % 10**d
		d -= 1
		right.add(n)
	return left.union(right)

truncatable = set([])
for p in primes:
	if trunctions(p).issubset(primes):
		truncatable.add(p)

truncatable.difference_update(set([2,3,5,7]))
print sum(truncatable)