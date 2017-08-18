import numpy

matrix = []
with open("p081_matrix.txt") as f:
    for line in f:
        numbers_str = line.split(',')
        matrix.append([int(x) for x in numbers_str])

matrix = numpy.array(matrix)
N = len(matrix)

def extend(chains,currentmin):
    changes = 0
    for n in range(N):
        for m in range(N):
            chain = chains[n][m]
            if len(chain) > 0:
                (i,j) = chain[-1]
                ends = [(i+1,j),(i,j+1)]
                for end in ends:
                    if end in chain:
                        ends.remove(end)
                for end in ends:
                    if (min(end) >= 0) & (max(end) < N):
                        if len(chains[end[0]][end[1]]) == 0:
                            chains[end[0]][end[1]] = chain+[end]
                            changes += 1
                        else: 
                            if chainsum(chain) + matrix[end] < chainsum(chains[end[0]][end[1]]):
                                chains[end[0]][end[1]] = chain+[end]
                                changes += 1
                        if (end == (N-1,N-1)) & (chain[0] == (0,0)):
                            if chainsum(chain) + matrix[end] < currentmin:
                                currentmin = chainsum(chain) + matrix[end]
                                changes += 1

    return chains, currentmin, changes

def chainsum(chain):
    chain = tuple(chain)
    if chain in sums:
        return sums[chain]
    if chain[:-1] in sums:
        sums[chain] = sums[chain[:-1]] + matrix[chain[-1]]
        return sums[chain[:-1]] + matrix[chain[-1]]
    else:
        S = 0
        for p in chain:
            S += matrix[p]
        sums[chain] = S
        return S

sums = {}

mychains = [[ [] for j in range(N) ] for i in range(N) ]
mychains[0][0] = [(0,0)]

currentmin = sum(matrix[0]) + sum(matrix[1:][-1])

changes = 1
while True:
    newchains, newmin, changes = extend(mychains,currentmin)
    print "Optimizations made: ", changes
    print "Current best: ", currentmin
    if changes == 0:
        break
    print
    mychains = newchains
    currentmin = newmin