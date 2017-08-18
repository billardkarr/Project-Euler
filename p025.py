import numpy as np

def fibbonaci(X):
	return [X[1],sum(X)]

digits = 1000
X = [1,1]
n = 1
while X[0] < 10**(digits - 1):
	X = fibbonaci(X)
	n += 1

print n