# partition function implementation

P = [1,1]

def genpent(i):
	if i % 2 == 0:
		return (-i/2)*(-3*i/2 - 1)/2
	if i % 2 == 1:
		return ((i+1)/2)*(3*(i+1)/2 - 1 )/2

k = 1
while P[k] % 10**6 != 0:
	k += 1
	indices = []
	i = 1
	S = 0
	while k - genpent(i) >= 0:
		S += ((-1)**((i-1)/2)) * P[k - genpent(i)]
		i += 1
	P.append(S)

print k