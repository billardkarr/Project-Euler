N = 1000000

def get_digits(n):
	digits = []
	while n > 0:
		digits = [n % 10] + digits
		n = n/10
	return digits

digits = []
i = 1
while len(digits) < N:
	digits += get_digits(i)
	i += 1

prod = 1
for index in [10**i for i in range(7)]:
	prod *= digits[index-1]

print prod