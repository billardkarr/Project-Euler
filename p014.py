import numpy

N = 10**6
X = numpy.array(range(N/2,N))
candidates = X.copy()

while len(candidates) > 1:
	# print len(candidates)*200.0/N
	X[X % 2 == 0] = X[X % 2 == 0]/2
	candidates = candidates[X > 1]
	X = X[X > 1]
	X[X % 2 == 1] = 3*X[X % 2 == 1] + 1

print "The winner is %d." % (candidates[0])