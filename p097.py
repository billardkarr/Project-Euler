a = 28433
for n in xrange(7830457):
    a *= 2
    if a >= 10**10:
        a = a % 10**10

a += 1
print a