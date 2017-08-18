N = 10000

potentialprimes = range(2,N)
primes = [2]
for k in range(N/2 + 1):
	while k*2 in potentialprimes: potentialprimes.remove(k*2)

while len(potentialprimes) > 0:
	i = min(potentialprimes)
	residues = []
	for p in primes:
		residues.append(i % p)
	if sum([residue == 0 for residue in residues]) == 0:
		if i > 1:
			primes.append(i)
			for k in range(N/i + 1):
				while k*i in potentialprimes: potentialprimes.remove(k*i)

print primes

# print primes

# def maxpower(d,p):
# 	power = 0
# 	while d % p == 0:
# 		power += 1
# 		d = d/p
# 	return power

# powers = []
# for p in primes:
# 	power = 0
# 	for d in divisors:
# 		power = max(power,maxpower(d,p))
# 	powers.append(power)

# N = 1

# for i in range(len(primes)):
# 	N *= primes[i]**powers[i]

# print N
