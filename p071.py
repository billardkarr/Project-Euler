from fractions import gcd

N = 10**6
winner = [2,7]
for d in range(1,N+1):
	n = 3*d/7
	if winner[0]*d < n*winner[1]:
		if 7*n < 3*d:
			winner = [n,d]

n = winner[0]
d = winner[1]
print n/gcd(n,d)