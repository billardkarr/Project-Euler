def factors(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return len(set(primfac))

n = 2
Y = [1]

while Y[-4:] != [4,4,4,4]:
	n += 1
	Y.append(factors(n))

print n - 3