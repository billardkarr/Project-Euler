from fractions import gcd

N = 1000000

def ratio(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)
            n //= d
        d += 1

    if n > 1:
       primfac.append(n)

    primfac = set(primfac)

    a = 1.0
    for p in primfac:
        a = a*p
        a = a/(p-1)

    return a

currentmax = 0
for k in range(2,N+1):
    if ratio(k) > currentmax:
        currentmax = ratio(k)
        winner = k

print winner 