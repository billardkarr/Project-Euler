from fractions import gcd

N = 2000

M = 100
triples = []
for m in range(2,M+1):
	for n in range(1,m):
		if gcd(m,n) == 1:
			a,b,c = m**2 - n**2, 2*m*n, m**2 + n**2
			[a,b,c] = sorted([a,b,c])
			for k in range(1,2*M/b + 1):
				if (k*a <= M) & (k*b <= k*a + M):
					triples.append(sorted([k*a,k*b,k*c]))


cuboids = set([])
for [a,b,c] in triples:
	y = a
	for z in range(a,M+1):
		x = b-z
		if x <= y:
			if x > 0:
				cuboids.add((x,y,z))

print len(cuboids)