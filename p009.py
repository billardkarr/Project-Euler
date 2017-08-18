N = 1000

for a in range(1,N+1):
	for b in range(a + 1, N - a + 1):
		c = 1000 - a - b
		if c > b:
			if a**2 + b**2 == c**2:
				abc = a * b * c
				print abc

