from itertools import combinations_with_replacement as cwr
from math import factorial

wins = 0
total = 0

for P in cwr([1,2,3,4],9):
	P = list(P)
	pcount = factorial(9)
	for i in [1,2,3,4]:
		pcount = pcount/factorial(P.count(i))
	for C in cwr([1,2,3,4,5,6],6):
		C = list(C)
		ccount = factorial(6)
		for i in [1,2,3,4,5,6]:
			ccount = ccount/factorial(C.count(i))
		if sum(P) > sum(C):
			wins += pcount*ccount
		total += pcount*ccount


print round(1.0*wins/total,7)
