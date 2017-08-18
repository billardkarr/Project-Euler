def T(n):
	return n*(n+1)/2

def get_primes(n):
	numbers = set(range(n-1, 1, -1))
	primes = []
	while len(numbers) > 0:
		p = numbers.pop()
		primes.append(p)
		composite = set(range(p*2,n,p))
		numbers.difference_update(composite)
	return primes

print get_primes(50)