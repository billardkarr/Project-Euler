def primes(n):
	tbd = set(range(N-1,1,-1))
	primes = set([])

	while len(tbd) > 0:
		p = tbd.pop()
		primes.add(p)
		tbd.difference_update(set(range(p**2,N,p)))
	primes = sorted(list(primes))
	primes.reverse()
	primes = tuple(primes)
	return primes

def solutions(n,tup):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif len(tup) == 1:
    	if n % tup[0] == 0:
    		return 1
    	else:
    		return 0
    elif (n,tup) in D:
        return D[(n,tup)]
    else:
        f = solutions(n - tup[0],tup) + solutions(n,tup[1:])
    D[(n,tup)] = f
    return f

D = {}

N = 10
while solutions(N,primes(N)) < 5000:
	N += 1

print N