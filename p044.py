from math import sqrt

def P(n):
	return n*(3*n - 1)/2

def ispent(n):
	x = int(sqrt(24*n+1))
	if x**2 == 24*n+1:
		i = (1 + x)/6
		if n == P(i):
			return True
		else:
			return False
	else:
		return False

i = 0
found = False
while found == False:
	i += 1
	for j in range(i-1,1,-1):
		if ispent(P(i) - P(j)):
			if ispent(P(i) + P(j)):
				print P(i) - P(j)
				found = True