import numpy as np

def H(n):
	return n*(2*n - 1)

def P(n):
	return n*(3*n - 1)/2

def T(n):
	return n*(n+1)/2


def Pinv(T):
	return 1.0/6 + np.sqrt(0.25 + 6*T)/3

def Hinv(T):
	return 1.0/4 + np.sqrt(1 + 8*T)/4

def test(n):
	a = int(np.floor(Pinv(T(n))))
	b = int(np.ceil(Pinv(T(n))))
	if P(a) == T(n) or P(b) == T(n):
		a = int(np.floor(Hinv(T(n))))
		b = int(np.ceil(Hinv(T(n))))
		if H(a) == T(n) or H(b) == T(n):
			print "found one: Tn = %d" % T(n)  
			return True
		else: 
			return False
	else: 
		return False


n = 286
while test(n) == False:
	n = n+1