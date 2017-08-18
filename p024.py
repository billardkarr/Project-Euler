from math import factorial as fac

m = 10
N = 10**6

perm = range(m)
answer = 0
for i in range(m-1,0,-1):
	k = (N+1) / fac(i)
	N = N % fac(i)
	answer += perm[k]*(10**i)
	perm.remove(perm[k])

print answer