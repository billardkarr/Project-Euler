import numpy

power = 7
N = 10**power
X = numpy.array(range(1,N))

starters = X.copy()
EN = numpy.array([])
ONE = numpy.array([])
# while len(EN) + len(ONE) < N:
while len(X) > 0:
	print "%g percent finished." % ((N-len(X))*100.0/N)
	EN = numpy.concatenate((EN,starters[X == 89]),axis=0)
	ONE = numpy.concatenate((ONE,starters[X == 1]),axis=0)
	starters = starters[(X != 89) & (X != 1)]
	X = X[(X != 89) & (X != 1)]
	S = 0*X
	for k in range(power+1):
		S += (X % 10)**2
		X = (X - (X % 10))/10
	X = S

print "Finished! The answer is:"
print len(EN)