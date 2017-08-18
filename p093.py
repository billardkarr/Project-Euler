from __future__ import division
from itertools import combinations, permutations, product
from itertools import combinations_with_replacement as cwr

operations = ['+','-','*','/','//']

def operate(a,b,operation):
	if a == 'nan':
		return 'nan'
	if b == 'nan':
		return 'nan'
	if operation == '+':
		return a+b
	if operation == '-':
		return a-b
	if operation == '*':
		return a*b
	if operation == '/':
		if b == 0:
			return 'nan'
		else:
			return a/b
	if operation == '//':
		if a == 0:
			return 'nan'
		else:
			return b/a

def concat(quad):
	mystr = ''
	for a in quad:
		mystr += str(a)
	return mystr

maxn = 0
for quad in combinations(range(0,10),4):
	numbers = set([])
	for (a,b,c,d) in permutations(quad):
		for (x,y,z) in product(operations,repeat=3):
			w = operate(a,b,x)
			w = operate(w,c,y)
			w = operate(w,d,z)
			if w != 'nan':
				if w % 1 == 0:
					if w > 0:
						numbers.add(w)
			w1 = operate(a,b,x)
			w2 = operate(c,d,y)
			w = operate(w1,w2,z)
			if w != 'nan':
				if w % 1 == 0:
					if w > 0:
						numbers.add(int(w))
	numbers = sorted(list(numbers))
	n = 0
	while n+1 in numbers:
		n+=1
	if n > maxn:
		maxn = n
		winner = concat(quad)
		print winner
		print numbers[:n]

print winner