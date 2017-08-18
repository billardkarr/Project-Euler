def digits(n):
	n = int(n)
	digits = []
	while n > 0:
		digits.append(n % 10)
		n = n/10
	return sorted(digits)

phi = (1.0 + (5**0.5))/2

fib = [1,1]
k = 3
first = phi**2/5**0.5
while True:
	first *= phi
	while first > 10**9:
		first = first/10
	fib = [fib[-1] % 10**9,sum(fib) % 10**9]
	if digits(first) == range(1,10):
		if digits(fib[-1]) == range(1,10):
			break
	k += 1

print k