N = 100
myset = set([])
for a in range(2,N+1):
	for b in range(2,N+1):
		myset.add(a**b)

print len(myset)
