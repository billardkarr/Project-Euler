def digitsum(N):
	digits = []
	while N > 0:
		digits.append(N % 10)
		N = N/10
	return sum(digits)

N = 100
sums = []
for a in range(1,N):
	for b in range(1,N):
		sums.append(digitsum(a**b))

print max(sums)