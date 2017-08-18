def lpf(N):
	reductions = [N]
	k = 2
	while k < N:
		while N % k != 0:
			k = k + 1

		while N % k == 0:
			N = N/k
			if N != 1:
				reductions.append(N)

	print reductions[-1]

lpf(25)
lpf(81)
lpf(13195)
lpf(600851475143)