N = 10**8

candidates = set([])
n = 1
while n**2 < N:
	a = n
	S = a**2
	a += 1
	while S + a**2 < N:
		S += a**2
		candidates.add(S)
		a += 1
	n += 1

def palindrome(n):
	digits = []
	backwards = []
	while n > 0:
		digits.append(n % 10)
		backwards = [n % 10] + backwards
		n = n/10
	return digits == backwards

S = 0
for x in candidates:
	if palindrome(x):
		S += x

print S