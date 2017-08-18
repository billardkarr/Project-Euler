import numpy
from math import factorial

def get_digits(n):
	digits = []
	while n > 0:
		digits += [n % 10]
		n = n/10
	return digits

def facdigsum(n):
	digits = get_digits(n)
	return sum([factorial(i) for i in digits])

N = 10**6

for k in range(1,N):
	B = get_digits(k)

found = []
for i in range(10,N):
	digits = get_digits(i)
	dfs = 0
	for d in digits:
		dfs += factorial(d)
	if dfs == i:
		found.append(i)

print sum(found)