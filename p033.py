import numpy

def primefac(n): # computes list of prime factors (with repeats)
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac

def simplify(n,d):
	nfacs = primefac(n) + [1]
	dfacs = primefac(d) + [1]
	for p in nfacs:
		while (p in nfacs) & (p in dfacs):
			nfacs.remove(p)
			dfacs.remove(p)
	n = numpy.prod(nfacs)
	d = numpy.prod(dfacs)
	return n, d

def get_digits(n):
	digits = []
	while n > 0:
		digits += [n % 10]
		n = n/10
	return digits

def digitreduce(n,d):
	ndigs = get_digits(n)
	ddigs = get_digits(d)
	for d in ndigs:
		if d in ddigs:
			ndigs.remove(d)
			ddigs.remove(d)
	if ndigs == []:
		ndigs.append(1)
	if ddigs == []:
		ddigs.append(1)
	n = sum([ndigs[i]*10**i for i in range(len(ndigs))])
	d = sum([ddigs[i]*10**i for i in range(len(ddigs))])
	return simplify(n, d)

N = 1
D = 1
for d in range(10,100):
	for n in range(10,d):
		ndigs = get_digits(n)
		ddigs = get_digits(d)
		commondigs = set(ndigs).intersection(set(ddigs))
		if commondigs != set([]):
			if commondigs != set([0]):
				if simplify(n,d) == digitreduce(n,d):
					[n,d] = simplify(n,d)
					N *= n
					D *= d

print simplify(N,D)