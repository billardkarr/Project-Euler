import numpy

def digitsum(n):
	S = 0
	while n > 0:
		S += n % 10
		n = n/10
	return S

N = 10**5

powers = []
bases = range(2,N)
for b in bases:
	k = 2
	while b**k < N:
		bases.remove(b**k)
		k += 1

for b in bases:
	k = 2
	while b**k < N:
		if b == digitsum(b**k):
			powers.append(b**k)
		k += 1

print len(powers)
print sorted(powers)

