import numpy as np

n = 100

def factorial(n):
	if n <= 0:
		return 1
	else:
		return n*factorial(n-1)

def digitsum(n):
	if n < 10:
		return n
	else:
		return (n % 10) + digitsum(n/10)

print digitsum(factorial(n))