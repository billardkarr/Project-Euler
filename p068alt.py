
X = range(1,11)

from math import factorial
from itertools import permutations

count = 0
candidates = []

for perm1 in permutations(X,5):
	remain = [x for x in X if x not in perm1]
	for perm2 in permutations(remain,5):
		outer = list(perm1)
		inner = list(perm2)
		sums = []
		for i in range(-1,4):
			sums.append(outer[i] + inner[i] + inner[i+1])
			if len(set(sums)) > 1:
				break
		if len(set(sums)) == 1:
			if outer[-1] == min(outer):
				mystr = ''
				for i in range(-1,4):
					mystr += str(outer[i])
					mystr += str(inner[i])
					mystr += str(inner[i+1])
				if len(mystr) == 16:
					candidates.append(int(mystr))

print max(candidates)