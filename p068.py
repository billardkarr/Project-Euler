
X = range(1,11)

from math import factorial
from itertools import permutations

count = 0
candidates = []

for perm1 in permutations(X,3):
	Y1 = [x for x in X if x not in perm1]
	for perm2 in permutations(Y1,2):
		if sum(perm1) == sum(perm2) + perm1[-1]:
			Y2 = [y for y in Y1 if y not in perm2]
			for perm3 in permutations(Y2,2):
				if sum(perm2) + perm1[-1] == sum(perm3) + perm2[-1]:
					Y3 = [y for y in Y2 if y not in perm3]
					for perm4 in permutations(Y3,2):
						if sum(perm3) + perm2[-1] == sum(perm4) + perm3[-1]:
							Y4 = [y for y in Y3 if y not in perm4]
							if sum(perm4) + perm3[-1] == Y4[0] + perm4[-1] + perm1[1]:
								candidates.append([])
								candidates[-1] += list(perm1)
								candidates[-1] += list(perm2)
								candidates[-1].insert(-1,perm1[-1])
								candidates[-1] += list(perm3)
								candidates[-1].insert(-1,perm2[-1])
								candidates[-1] += list(perm4)
								candidates[-1].insert(-1,perm3[-1])
								candidates[-1] += [Y4[0],perm4[-1],perm1[1]]

finalists = []
for i in range(len(candidates)):
	X = candidates[i]
	if X[0] == min([X[l] for l in range(0,15,3)]):
		mystr = ''
		for x in X:
			mystr += str(x)
		if len(mystr) == 16:
			finalists.append(int(mystr))

print max(finalists)