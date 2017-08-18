N = 10**6

from math import factorial

def sumfac(n):
	S = 0
	while n > 0:
		S += factorial(n % 10)
		n = n/10
	return S

count = 0
length = 60
for n in xrange(N):
	sequence = [n]
	for i in xrange(length):
		a = sumfac(sequence[-1])
		if a in sequence:
			break
		sequence.append(a)
	if len(sequence) == length:
		count += 1

print count