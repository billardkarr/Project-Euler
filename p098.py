import csv
from itertools import combinations
from itertools import permutations
from math import sqrt, ceil, floor

with open('p098_words.txt') as f:
	reader = csv.reader(f)
	words = sorted(list(reader)[0])

def encrypt(word,key):
	code = []
	for letter in word:
		code.append(key[letter])
	return code

def decrypt(code,key):
	word = []
	for x in code:
		word.append(key[x])
	return word

def number(code):
	mystr = ''
	for x in code:
		mystr += x
	return int(mystr)

candidates = set([])
for (A,B) in combinations(words,2):
	if sorted(list(A)) == sorted(list(B)):
		d = len(list(A))
		a = int(ceil(sqrt(10**(d-1))))
		b = int(floor(sqrt(10**d - 1)))
		valid = []
		squares = []
		for n in range(a,b+1):
			code = list(str(n**2))
			squares.append(code)
			dkey = {}
			ekey = {}
			for i in range(d):
				dkey[code[i]] = A[i]
				ekey[A[i]] = code[i]
			if encrypt(A,ekey) == code:
				if decrypt(code,dkey) == list(A):
					valid.append((code,ekey))
		for (code,key) in valid:
			if encrypt(B,key) in squares:
				a = number(encrypt(A,key))
				b = number(encrypt(B,key))
				candidates.add(max(a,b))
				print A,B
				print a,b
				print

print "Max: %d" % max(candidates)

