def get_digits(N):
	digits = []
	while N > 0:
		digits.append(N % 10)
		N = N/10
	return digits

def reversed(N):
	digits = get_digits(N)
	ans = 0
	d = len(digits)
	for i in range(len(digits)):
		ans += digits[d - (i+1)]*(10**i)
	return ans

def palindrome(N):
	return N == reversed(N)


N = 10000
count = 0
for i in range(1,N):
	print "testing %d" % i
	for j in range(50):
		i += reversed(i)
		if palindrome(i):
			break
		if j == 49:
			count += 1

print count