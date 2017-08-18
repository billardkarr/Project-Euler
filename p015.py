N = 20

def factorial(n):
	if n == 1:
		return 1
	if n > 1:
		return n*factorial(n-1)

def choose(n,k):
	return factorial(n)/(factorial(k)*factorial(n-k))

print choose(2*N,N)