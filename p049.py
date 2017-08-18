def digits(n):
	digits = []
	while n > 0:
		digits += [ n % 10 ]
		n = n/10
	return sorted(digits)

def get_primes(n):
	numbers = set(range(n-1, 1, -1))
	primes = []
	while len(numbers) > 0:
		p = numbers.pop()
		primes.append(p)
		numbers.difference_update(set(range(p*2,n,p)))
	return primes

sequences = []
N = 10**4
primes = get_primes(N)
for p in primes:
	if p < N/10:
		primes.remove(p)


for a in primes:
	for k in range(2,(N - a)/2,2):
		if digits(a) == digits(a+k):
			if digits(a) == digits(a+2*k):
				if a+k in primes:
					if a+2*k in primes:
						sequences.append([a,a+k,a+2*k])

print sum(sequences[-1][i]*10**(8-4*i) for i in range(len(sequences[-1])))
