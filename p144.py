import numpy as np
from numpy import dot

def grad(P):
    return np.array([8*P[0],2*P[1]])

def proj(V,N):
    return ((dot(V,N))/(dot(N,N)))*N

def f(P):
    return 4*P[0]**2 + P[1]**2

P0 = np.array([0.0,10.1])
P = np.array([1.4,-9.6])
V = P - P0
V = V

n = 1
while True:
    N = grad(P)
    V = V - 2*proj(V,N)
    t = -dot(P,grad(V))/f(V)
    P += t*V
    if abs(P[0]) <= 0.01:
        if P[1] > 0:
            print n
            break
    n += 1

