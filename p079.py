from itertools import permutations
from itertools import combinations_with_replacement as cwr

partials = []
with open("p079_keylog.txt") as f:
    for n in f:
        n = int(n)
        digits = []
        while n > 0:
            digits = [n % 10] + digits
            n = n/10
        partials.append(digits)

candidates = []
d = 0
while len(candidates) == 0:
    candidates = [[]]
    for partial in partials:
        [a,b,c] = partial

        newcandidates = []
        for candidate in candidates:
            if a not in candidate:
                for i in range(len(candidate)+1):
                    X = candidate[:i]
                    X += [a]
                    X += candidate[i:]
                    if len(X) <= d:
                        newcandidates.append(X)
            if a in candidate:
                if candidate not in newcandidates:
                    newcandidates.append(candidate)
        candidates = newcandidates

        newcandidates = []
        for candidate in candidates:
            j = candidate.index(a)
            if b not in candidate[j:]:
                for i in range(len(candidate[j:])+1):
                    X = candidate[:i+j+1]
                    X += [b]
                    X += candidate[i+j+1:]
                    if len(X) <= d:
                        newcandidates.append(X)
            if b in candidate[j:]:
                if candidate not in newcandidates:
                    newcandidates.append(candidate)
        candidates = newcandidates
        
        newcandidates = []
        for candidate in candidates:
            j = candidate.index(b)
            if c not in candidate[j:]:
                for i in range(len(candidate[j:])+1):
                    X = candidate[:i+j+1]
                    X += [c]
                    X += candidate[i+j+1:]
                    if len(X) <= d:
                        newcandidates.append(X)
            if c in candidate[j:]:
                if candidate not in newcandidates:
                    newcandidates.append(candidate)
        candidates = newcandidates
    
    d += 1

winner = ''
for n in candidates[0]:
    winner += str(n)

print int(winner)