from math import sqrt

x = 2
nuggets = []
while len(nuggets) < 15:
    y = int(round(sqrt(5*(x**2) - 4)) - x)/2
    n = x*y
    if x**2 - y**2 == n+1:
        nuggets.append(n)
    x+=1

print nuggets[-1]