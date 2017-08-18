N = 1000

import numpy as np 

def f(a,b,n):
	X = np.array(range(n))
	return X**2 + a*X + b

def isprime(n):
	n = np.abs(n)
	if n in [0,1]:
		return False
	primfac = []
	d = 2
	while d**2 <= n:
		while n % d == 0:
			return False
		d += 1
	return True

def ccp(X):
	a = X[0]
	k = 0
	while isprime(a) & (k < len(X)):
		a = X[k]
		k +=1
	return k

def ub(b,a):
	x = np.abs(b) - a
	if x > 1:
		return min(b,x)
	else:
		return b

candidates = []
for b in range(-N,N+1):
	if isprime(b) & (b > 40):
		for a in range(-N+1,N):
			if isprime(a+b+1) & (ub(b,a) > 40):
				candidates.append([a,b])

M = 40
A = 1
B = 41
for [a,b] in candidates:
	X = f(a,b,N)
	n = ccp(X)
	if n > M:
		A = a
		B = b
		M = n
	else:
		candidates.remove([a,b])

print A*B
