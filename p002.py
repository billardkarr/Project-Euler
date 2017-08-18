N = 4*(10**6)
fib = [1, 1]

S = 0
while fib[0] < N:
	if fib[0] % 2 == 0:
		S += fib[0]
	fib = [fib[1],sum(fib)]

print S