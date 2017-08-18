N = 50

import itertools
import numpy as np
from numpy import dot
from fractions import gcd

points = []
for x1 in range(N+1):
	for y1 in range(N+1):
		if (x1 != 0) or (y1 != 0):
			A1 = np.array([x1,y1])
			points.append(A1)			

count = 0
for (A1,A2) in itertools.combinations(points,2):
	x = dot(A1,A2)
	a = dot(A1,A1)
	b = dot(A2,A2)
	if x in [0,a,b]:
		count += 1

print count



	

