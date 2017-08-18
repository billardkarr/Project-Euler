N = 10**5

def f(n):
	b = int(str(n)[::-1])
	f = b + n
	digits = [ int(a) % 2 for a in str(f) ]
	if n % 10 == 0:
		return False
	if set(digits) == set([1]):
		return True
	else:
		return False

reversible = set([])

for n in range(1,10**3):
	if f(n):
		b = int(str(n)[::-1])
		a = b + n
		print a, n
		# print n, f(n)
		reversible.add(n)

print len(reversible)