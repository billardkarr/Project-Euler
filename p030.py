import numpy as np

p = 5
n = 1
while n*(9**p) >= 10**(n-1):
	n += 1

X = np.array(range(2,10**(n-1)))
Y = X.copy()
powersum = Y*0
for i in range(n):
	powersum += (Y % 10)**p
	Y = Y/10

Z = X[X == powersum]
print Z
print sum(Z)