def digits(n):
	if n == 0:
		return [0]
	digits = []
	while n > 0:
		digits.append(n % 10)
		n = n/10
	return digits

candidates = []
for x in range(10**5):
	digs = digits(x**2)
	if digs[0:6:2] == [0,9,8]:
		candidates.append(x)

found = False
for x in candidates:
	for y in range(10**4,int(10**4.5)+1):
		z = x + y*(10**5)
		if z**2 >= 10**19:
			break
		if z**2 < 10**18:
			break
		digs = digits(z**2)
		if digs[0::2] == [0,9,8,7,6,5,4,3,2,1]:
			found = True
			winner = z
	if found:
		break

print winner