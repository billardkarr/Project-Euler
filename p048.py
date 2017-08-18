S = 0
for i in range(1,1001):
	a = 1
	for k in range(i):
		a *= i
		a = a % 10**10
	S += a
	S = S % 10**10
print S
