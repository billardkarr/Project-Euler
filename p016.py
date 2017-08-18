N = 2**1000

digits = []
while N > 0:
	digits.append(N % 10)
	N = N/10

print sum(digits)
