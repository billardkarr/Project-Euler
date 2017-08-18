def isprime(n): # computes list of prime factors (with repeats)
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            return False
            n //= d
        d += 1
    return True

spiralcount = 5
primecount = 3

n = 1
ratio = primecount*1.0/spiralcount
while ratio >= 0.1:
    n += 1
    new = range((2*n+1)**2 - 6*n,(2*n+1)**2+1,2*n)
    for p in new:
        if isprime(p):
            primecount += 1
    spiralcount += 4
    ratio = primecount*1.0/spiralcount

print 2*n + 1