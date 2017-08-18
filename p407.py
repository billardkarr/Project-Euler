N = 10**5

def get_primes(n):
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]

primes = get_primes(N+1)

remaining = set(range(2,N+1))

M = 0
ones = 0
for p in primes[::-1]:
	for n in remaining.intersection(set(range(p,N+1,p))):
		candidates = set(range(p,n,p)).union(set(range(p+1,n,p)))
		candidates.add(1)
		candidates = sorted(list(candidates))
		for a in candidates[::-1]:
			if ((a**2 - a) % n) == 0:
				# print n, a
				M += a
				if a == 1:
					ones += 1
				remaining.discard(n)
				break

print 1.0*N/ones
print M