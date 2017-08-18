from itertools import combinations_with_replacement as cwr
import numpy

def number(tup):
	return sum( [10**i * tup[i] for i in range(len(tup))] )

goal = 1
monotone = set([])
p, d = 100.0, 0
while p > goal:
	d += 1
	for comb in cwr(range(10),d):
		monotone.add(number(comb))
		monotone.add(number(comb[::-1]))
	monotone.remove(0)
	p = 100.0*len(monotone)/max(monotone)

monotone = sorted(list(monotone))
monotone = numpy.array(monotone)

for k in monotone:
	p = 100.0*len(monotone[monotone <= k])/k
	if p <= goal:
		break

while p < goal:
	k = k - 1
	p = 100.0*len(monotone[monotone <= k])/k
	if p == goal:
		break

print k