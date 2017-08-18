from math import factorial

numbers = []
areas = []

N = 2*(10**6)

n = 1
while (n**2)*(n+1)**2 < 4*N:
	m = n
	while n*(n+1)*m*(m+1) < 4*N:
		numbers.append(n*(n+1)*m*(m+1)/4)
		areas.append(n*m)
		m += 1
	
	numbers.append(n*(n+1)*m*(m+1)/4)
	areas.append(n*m)
	n += 1
numbers.append(n*(n+1)*m*(m+1)/4)
areas.append(n*m)

objective = [ abs(k - N) for k in numbers ]
print areas[objective.index(min(objective))]

