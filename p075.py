from math import sqrt
from fractions import gcd
import numpy

N = 1500000
counts = numpy.zeros(N+1)

m = 2
while 2*m*(m + 1) <= N:
	n = 1
	while m > n:
		if gcd(m,n) == 1:
			if (m % 2 == 0) or (n % 2 == 0):
				a = m**2 - n**2
				b = 2*m*n
				c = m**2 + n**2
				k = 0
				while (k+1)*(a+b+c) <= N:
					k += 1
					counts[k*(a+b+c)] += 1
		n += 1
	m += 1

# print numpy.where(counts==1)[0]
print len(numpy.where(counts==1)[0])