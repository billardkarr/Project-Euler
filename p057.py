from fractions import gcd

def num_digits(N):
	digits = []
	while N > 0:
		digits.append(N % 10)
		N = N/10
	return len(digits)

p = 1
q = 1
count = 0
for i in range(1000):
	pnew = p + 2*q
	qnew = p + q
	divisor = gcd(pnew,qnew)
	pnew = pnew/divisor
	qnew = qnew/divisor
	p = pnew
	q = qnew
	if num_digits(p) > num_digits(q):
		count += 1

print count