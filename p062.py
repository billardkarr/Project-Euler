def iscube(n):
	a = n**(1.0/3)
	a = round(a)
	return a**3 == n

def digits(n):
	if n == 0:
		return [0]
	else:
		digits = []
		while n > 0:
			digits.append(n % 10)
			n = n/10
		return sorted(digits)

def number(diglist):
	S = 0
	P = 1
	for n in diglist:
		S += P*n
		P *= 10
	return S

from itertools import permutations
from math import ceil, floor

target = 5
n = 0
notit = []

cubes = []
for k in range(10**5):
	cubes.append(digits(k**3))

while True:
	digs = digits(n**3)
	maxperm = number(digs)
	minperm = number(reversed(digs))
	b = int(ceil(maxperm**(1.0/3)))+1
	a = int(floor(minperm**(1.0/3)))
	matches = []
	for i in range(len(cubes)):
		if cubes[i] == digs:
			matches.append(k)
		if len(matches) > target:
			break
		if i**3 > maxperm:
			break

	if len(matches) == target:
		break
	n += 1
	if n > len(cubes):
		print "didn't find"
		break

print n**3