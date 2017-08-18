def spiral(N):
	n = 1
	ans = 1
	while (2*n+1)**2 <= N**2:
		ans += 4*(2*n+1)**2 - 12*n
		n += 1
	return ans

print spiral(1001)