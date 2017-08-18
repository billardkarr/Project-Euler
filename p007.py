
N = 10001

primes = [2,3]

def isprime(i):
	for p in primes:
		if i % p == 0:
			return False
	return True

i = primes[-1] + 2
while len(primes) < N:
	if isprime(i):
		primes.append(i)
		i = primes[-1] + 2
	else:
		i += 2

print len(primes)
print primes[-1]