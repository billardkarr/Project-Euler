from math import sqrt
from math import floor
from fractions import gcd
import numpy

N = 10**4
solutions = []
for d in range(1,N+1):
	X = [1,0,1]
	cfe = []
	history = []
	while True:
		Y = [1,X[1]/X[0],X[2]/X[0]]
		if Y not in history:
			history.append(Y)
		else:
			if len(cfe) % 2 == 0:
				if cfe[1] != 0:
					solutions.append(d)
			break
		a = 0
		while (X[2] - X[1])**2 < d*X[0]**2:
			a += 1
			X[1] = X[1] - X[2]
		cfe.append(a)
		X = [X[0],-X[1],(d*X[0]**2 - X[1]**2)/X[2]]

print len(solutions)