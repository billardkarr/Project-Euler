from fractions import gcd

N = 12000
count = 0
for d in range(1,N+1):
	for n in range(d/3, d/2 + 1):
		if gcd(n,d) == 1:
			if (3*n > d) & (2*n < d):
				count += 1

print count