n = 4620
while True:
	solutions = 0
	n += 1
	for x in range(n+1,2*n):
		if n*x % (x-n) == 0:
			solutions += 1
	if solutions > 300:
		break

print n