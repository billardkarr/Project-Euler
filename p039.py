P = 1000
squares = [k*k for k in range(P/2)]

def get_solutions(p):
	solutions = []
	for a in range(1,p):
		for b in range(a,p-a):
			c = p - a - b
			if a**2 + b**2 == c**2:
				X = sorted([a,b,c])
				if X not in solutions:
					solutions.append(X)
	return solutions

M = 0
winner = 0
for p in range(1,P+1):
	solutions = get_solutions(p)
	print "When p = %d, # sol'ns is %d" % (p, len(solutions))
	if len(solutions) > M:
		M = len(solutions)
		winner = p

print winner