from fractions import gcd

P = 1
for i in range(1,21):
	P = P*i/gcd(P,i)

print P