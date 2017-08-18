from fractions import gcd

def u(n):
	return (1 + n**11)/(1 + n)

def lagrange(X,Y,Z):
	k = len(Y)
	up, down = 0, 1
	for i in range(k):
		num, den = Y[i], 1
		for j in range(k):
			if j != i:
				num *= (Z - X[j])
				den *= (X[i] - X[j])
				g = gcd(num,den)
				num, den = num/g, den/g
		up, down = up*den + down*num, down*den
		g = gcd(up,down)
		up, down = up/g, down/g
	return up/down

N = 11
U = [u(n) for n in range(1,N)]

S = 0
for k in range(1,N):
	X = range(1,k+1)
	Y = U[:k]
	OP = lagrange(X,Y,k+1)
	if u(k+1) != OP:
		S += OP
print S