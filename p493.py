from itertools import combinations_with_replacement as cwr
from math import factorial

def choose(n,k):
	return factorial(n)/(factorial(n - k)*factorial(k))

pick = 20
colors = 0
total = 0
X = []
for x1 in range(min(pick - sum(X),10)+1):
	X = [x1]
	for x2 in range(min(pick - sum(X),10)+1):
		X = [x1,x2]
		for x3 in range(min(pick - sum(X),10)+1):
			X = [x1,x2,x3]
			for x4 in range(min(pick - sum(X),10)+1):
				X = [x1,x2,x3,x4]
				for x5 in range(min(pick - sum(X),10)+1):
					X = [x1,x2,x3,x4,x5]
					for x6 in range(max(pick-10-sum(X),0),min(pick - sum(X),10)+1):
						X = [x1,x2,x3,x4,x5,x6]
						X.append(pick - sum(X))
						count = 1
						for i in range(7):
							count *= choose(10,X[i])
						colors += count*(7 - X.count(0))
						total += count	

print round(1.0*colors/total,9)