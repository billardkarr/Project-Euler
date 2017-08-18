import numpy

accuracy = 100
def sqrtdigitsum(d):
	c, p, S = d, 0, 0
	for i in range(accuracy):
		x = 0
		while (x + 1)*(20*p + x + 1) <= c:
			x += 1
		S += x
		c = 100*(c - x*(20*p + x)) 
		p = 10*p + x
	return S

squares = [i**2 for i in range(10)]
S = 0
for i in range(100):
	if i not in squares:
		S += sqrtdigitsum(i)

print S