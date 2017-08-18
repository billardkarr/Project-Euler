def cyclelength(d):
	n = 1
	decimal = []
	found = False
	while found == False:
		n = n*10
		if [n/d,n%d] not in decimal:
			decimal.append([n/d,n%d])
			n = n%d
		else:
			found = True
			return len(decimal) - decimal.index([n/d,n%d])

M = 1
winner = 1
for i in range(1,1000):
	if cyclelength(i) > M:
		M = cyclelength(i)
		winner = i

print winner