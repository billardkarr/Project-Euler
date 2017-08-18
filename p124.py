N = 10**5
import numpy

def get_primes(n):
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]

primes = numpy.array(get_primes(N+1))

rad = numpy.ones(N+1)
for p in primes:
	rad[p:N+1:p] *= p

rad += 1.0*numpy.array(range(N+1))/N
E = sorted(rad)
print int(N*(E[N/10] % 1))