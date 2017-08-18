def P(m):
	P = 1
	for i in range(1,m+1):
		for j in range(1,i+1):
			P *= i*2.0/(m+1)
	return int(P)

print sum([P(m) for m in range(2,16)])