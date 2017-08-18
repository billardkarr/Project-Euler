N = 10**3

hilberts = []
for k in range(N):
	hilberts.append(4*k+1)

squares = [25]
k = 1
while squares[-1] < hilberts[-1]:
	k += 1 
	squares.append((4*k + 1)**2)

print squares

sqfree = []
for h in hilberts:
	residues = []
	for sq in squares:
		residues.append(h % sq)
	if 0 not in residues:
		sqfree.append(h)

print sqfree
print len(sqfree)