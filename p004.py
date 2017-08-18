def palindrome(N):
	digits = []
	while N > 0:
		digits.append(N % 10)
		N = N/10

	return digits == list(reversed(digits))

products =[]
for k in range(100,1000):
	for n in range(k,1000):
		products.append(n*k)

K = 0
for N in products:
	if palindrome(N):
		K = max(K,N)

print K


