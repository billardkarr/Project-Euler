def palindrome(N,B):
	digits = []
	while N > 0:
		digits.append(N % B)
		N = N/B

	return digits == list(reversed(digits))

N = 1000000

S = 0
for i in range(N):
	if palindrome(i,10) & palindrome(i,2):
		S += i

print S

