def P(s,n):
	if s == 3:
		return n*(n + 1)/2
	if s == 4:
		return n**2
	if s == 5:
		return n*(3*n - 1)/2
	if s == 6:
		return n*(2*n - 1)
	if s == 7:
		return n*(5*n - 3)/2
	if s == 8:
		return n*(3*n - 2)

banks = []
for s in range(3,9):
	banks.append([])
	n = 1
	while True:
		if (P(s,n) >= 10**3) & (P(s,n) < 10**4):
			banks[-1].append(P(s,n))
		if P(s,n) >= 10**4:
			break
		n += 1

import itertools
def p061():
	for perm in itertools.permutations(banks):
		for p3 in perm[0]:
			for p4 in perm[1]:
				if p3 % 100 == p4/100:
					for p5 in perm[2]:
						if p4 % 100 == p5/100:
							for p6 in perm[3]:
								if p5 % 100 == p6/100:
									for p7 in perm[4]:
									 	if p6 % 100 == p7/100:
									 		for p8 in perm[5]:
									 			if p7 % 100 == p8/100:
									 				if p8 % 100 == p3/100:
									 					print p3+p4+p5+p6+p7+p8
									 					return p3+p4+p5+p6+p7+p8

p061()



