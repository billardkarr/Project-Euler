def solutions(n,tup):
    if n < 0:
        return 0
    elif n == 0 or tup == (1,):
        return 1
    elif (n,tup) in D:
        return D[(n,tup)]
    else:
        f = solutions(n - tup[0],tup) + solutions(n,tup[1:])
    D[(n,tup)] = f
    return f

D = {}
print solutions(100,tuple(range(99,0,-1)))
print tuple(range(99,0,-1))