from math import factorial

def C(n,r):
	return factorial(n)/(factorial(n-r)*factorial(r))

count = 0
for n in range(1,101):
	for r in range(1,n+1):
		if C(n,r) > 10**6:
			count += 1

print count