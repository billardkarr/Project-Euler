def digits(n):
	digits = []
	while n > 0:
		digits.append(n % 10)
		n = n/10
	return sorted(digits)

def phi(n):
	if n in primes:
		return p - 1
	else:
		phi = n
		i = 0
		while primes[i]**2 <= n:
			if n % primes[i] == 0:
				phi = phi/primes[i]
				phi = phi*(primes[i]-1)
			i += 1
		return phi

import numpy

N = 10**7
tbd = set(range(N-1,1,-1))
primes = set([])

while len(tbd) > 0:
	p = tbd.pop()
	primes.add(p)
	tbd.difference_update(set(range(p**2,N,p)))
print "Found primes"

nvals = numpy.array(range(N))
phi = numpy.array(range(N))
ratios = numpy.ones(N)
for p in primes:
	phi[p:N:p] = phi[p:N:p]/p
	phi[p:N:p] = phi[p:N:p]*(p-1)
	ratios[p:N:p] = ratios[p:N:p]*p
	ratios[p:N:p] = ratios[p:N:p]/(p-1)
print "Computed phi vals"

nvals = nvals[2:N]
phi = phi[2:N]
ratios = ratios[2:N]

minimum = 10
winner = None
count = 0
while len(nvals) > 0:
	count += 1
	if count > N:
		break
	k = nvals[-1]
	r = ratios[-1]
	tot = phi[-1]
	if digits(k) == digits(tot):
		if r < minimum:
			print "found new min"
			winner = k
			minimum = r
		nvals = nvals[ratios < r]
		phi = phi[ratios < r]
		ratios = ratios[ratios < r]
		print "candidates left to check: %d" % len(nvals)
	else:
		nvals = nvals[:-1]
		phi = phi[:-1]
		ratios = ratios[:-1]

print winner