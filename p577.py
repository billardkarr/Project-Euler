

def V(n):
	if n >= 0:
		return (n+2)*(n+1)/2
	else:
		return 0

def H(n):
	H = 0
	r = 1
	while r <= n/3:
		# print "radius = ", r
		# print "n - 3r = ", (n-3*r)
		# print "# of hexagons = ", r*V(n - 3*r)
		H += r*V(n - 3*r)
		r += 1

	return H

H(3)

sum = 0
N = 12345
for n in range(3,N+1):
	sum += H(n)

print sum
