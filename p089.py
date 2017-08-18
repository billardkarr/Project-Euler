import numpy

numerals = []
with open("p089_roman.txt") as f:
    for line in f:
        numerals.append(line.split()[0])

options =['M','D','C','L','X','V','I']

def lettervalue(letter):
    if letter == 'I':
        return 1
    if letter == 'V':
        return 5
    if letter == 'X':
        return 10
    if letter == 'L':
        return 50
    if letter == 'C':
        return 100
    if letter == 'D':
        return 500
    if letter == 'M':
        return 1000

def number(numeral):
    letters = list(numeral)
    S = 0
    for i in range(len(letters)-1):
        A = lettervalue(letters[i])
        B = lettervalue(letters[i+1])
        if A >= B:
            S += A
        if A < B:
            S -= A
    S += lettervalue(letters[-1])
    return S

for numeral in numerals:
    print numeral
    if 'VIIII' in numeral:
        numeral = numeral.replace('VIIII','IX',1)
    if 'IIII' in numeral:
        if 'V' not in numeral:
            numeral = numeral.replace('IIII','IV',1)
    if 'LXXXX' in numeral:
        numeral = numeral.replace('LXXXX','XC',1)
    if 'XXXX' in numeral:
        if 'L' not in numeral:
            numeral = numeral.replace('XXXX','XL',1)
    print numeral
    print
