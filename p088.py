from itertools import combinations_with_replacement as cwr


k = 8

for comb in cwr(range(1,k+1),5):
	a = sum(comb)
	b = 1
	for x in comb:
		b *= x
	if a == b:
		print a, comb