from math import factorial

def s(n):
	m = 0
	while factorial(m) % n != 0:
		m += 1
	return m

def S(n):
	return sum([s(n) for n in range(2,n+1)])

print S(10**3)