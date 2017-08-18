n = 100

from fractions import gcd

sequence = [2]
for i in range(n/3 + 1):
    sequence += [1,2*(i+1),1]

sequence = sequence[:n]

num = 1
den = sequence[-1]
sequence = sequence[:-1]
while True:
    num = sequence[-1]*den + num
    g = gcd(num,den)
    num = num/g
    den = den/g
    if len(sequence) == 1:
        break
    num, den = den, num
    sequence = sequence[:-1] 

digitsum = 0
for a in list(str(num)):
    digitsum += int(a)

print digitsum