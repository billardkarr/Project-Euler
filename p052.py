def digits(N):
    digits = []
    while N > 0:
        digits.append(N % 10)
        N = N/10
    return sorted(digits)

d = 6
count = 0
x = 0
while count < d:
    x += 1
    sequence = []
    for i in range(1,d+1):
        sequence.append(digits(i*x) == digits(x))
    count = sum(sequence)

print x