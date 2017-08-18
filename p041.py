def get_digits(n):
	digits = []
	while n > 0:
		digits = [n % 10] + digits
		n = n/10
	return sorted(digits)

N = 7654321

pandigitals = []
numbers = set(range(N, 1, -1))
primes = set([])
while len(numbers) > 0:
	p = numbers.pop()
	digits = get_digits(p)
	if digits == range(1,len(digits)+1):
		pandigitals.append(p)
	primes.add(p)
	numbers.difference_update(set(range(p,N+1,p)))

print max(pandigitals)