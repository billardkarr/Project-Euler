N = 1000

a = 3
S = 0
while a <= N:
	R = []
	for n in range(a):
		r = 2*n*a % (a**2)
		R.append(r)
	print a, max(R)
	S += max(R)
	a += 1

print S