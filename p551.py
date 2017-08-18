N = 10**6

a = [1,1]

def sd(n):
	S = n % 10
	while n/10 > 0:
		n = n/10
		S += n % 10
	return S

for i in range(N):
	n1 = a[1]
	n2 = sd(n1) + n1
	a = [n1,n2]
	print n2 - n1