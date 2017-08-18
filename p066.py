import numpy
from fractions import gcd

def issquare(X):
	sr = numpy.rint(X**0.5)
	return X == sr**2

N = 1000
cfes = []
Dvals = []
for D in range(1,N+1):
	if issquare(D) == False:
		Dvals.append(D)
		coef = [1,0,1]
		cfes.append([])
		history = []
		while True:
			Y = [1,coef[1]/coef[0],coef[2]/coef[0]]
			if Y not in history:
				history.append(Y)
			else:
				break
			a = 0
			while (coef[2] - coef[1])**2 < D*coef[0]**2:
				a += 1
				coef[1] = coef[1] - coef[2]
			cfes[-1].append(a)
			coef = [coef[0],-coef[1],(D*coef[0]**2 - coef[1]**2)/coef[2]]

def convergent(sequence):
	num = 1
	den = sequence[-1]
	sequence = sequence[:-1]
	if len(sequence) == 0:
		return [num,den]
	while True:
	    num = sequence[-1]*den + num
	    g = gcd(num,den)
	    num = num/g
	    den = den/g
	    if len(sequence) == 1:
			break
	    num, den = den, num
	    sequence = sequence[:-1]
	return [num, den]

Xvals = []
for i in range(len(Dvals)):
	cfe = cfes[i]
	D = Dvals[i]

	if len(cfe) % 2 == 1:
		[X,Y] = convergent(cfe[:-1]) 
		Xvals.append(X)

	if len(cfe) % 2 == 0:
		cfe = cfe + cfe[1:]
		[X,Y] = convergent(cfe[:-1])
		Xvals.append(X)

print Dvals[Xvals.index(max(Xvals))]