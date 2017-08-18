def get_primes(n):
	numbers = set(range(n-1, 1, -1))
	primes = []
	while len(numbers) > 0:
		p = numbers.pop()
		primes.append(p)
		numbers.difference_update(set(range(p*2,n,p)))
	return sorted(primes)

N = 10**6
primes = get_primes(N)
sumlength = 0
winner = 0

p = 0
for i in range(len(primes)):
	j = i+sumlength
	p = sum(primes[i:j])
	while (p <= N) & (j <= len(primes)):
		p += primes[j]
		if p in primes:
			sumlength = j - i + 1
			winner = p
		j += 1

print winner