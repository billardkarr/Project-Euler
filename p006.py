N = 100

summ = 0
squaresum = 0
for k in range(1,N+1):
	summ += k
	squaresum += k**2

ans = summ**2 - squaresum

print ans
