N = 10**6

import numpy

def get_primes(n):
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]

primes = get_primes(N+1)

def f(n):
	if n % 2 == 1:
		return 2
	if n % 2 == 0:
		return 2*(n+1)*primes[n]

for n in range(len(primes)):
	if f(n) > 10**10:
		print n+1
		break
