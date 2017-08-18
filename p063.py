def digits(N):
    digits = []
    while N > 0:
        digits.append(N % 10)
        N = N/10
    return len(digits)

solutions = []

n = 1
while 10**(n-1) <= 9**n:
    for a in range(1,10):
        if digits(a**n) == n:
            solutions.append(a**n)
    n += 1

print len(solutions)
print len(set(solutions))