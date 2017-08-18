from fractions import gcd

def phi(n):
    primfac = []
    a = n
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    primfac = set(primfac)
    
    for p in primfac:
        a = a*(p-1)
        a = a/p
    return a

N = 10**6
count = 0
for d in range(2,N+1):
	count += phi(d)

print count