def get_digits(n):
	digits = []
	while n > 0:
		digits = [n % 10] + digits
		n = n/10
	return digits

def get_number(digits):
	return sum(digits[-i-1]*10**i for i in range(len(digits)))

def candidate(n):
	N = get_digits(n)
	i = 1
	while len(N) < 9:
		i += 1
		N += get_digits(i*n)
	if len(N) == 9:
		if set(N) == set(range(1,10)):
			return [get_number(N)]
		else:
			return []
	else:
		return []


candidates = []
for i in range(1,10**4):
	candidates += candidate(i)

print max(candidates)