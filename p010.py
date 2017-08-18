N = 2*10**6

def get_primes(n):
	numbers = set(range(n-1, 1, -1))
	primes = []
	while len(numbers) > 0:
		p = numbers.pop()
		primes.append(p)
		numbers.difference_update(set(range(p**2,n,p)))
	return primes

primes = get_primes(N)
print sum(primes)
