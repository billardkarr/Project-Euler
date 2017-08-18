import csv
import numpy
from itertools import product

with open('p059_cipher.txt') as f:
	reader = csv.reader(f)
	code = [int(x) for x in list(reader)[0]]

lowercase = [ord(a) for a in list('abcdefghijklmnopqrstuvwxyz')]
code = numpy.array(code)

candidates = []
found = False
for a in lowercase:
	if found == True:
		break
	decrypt = code.copy()
	decrypt[0::3] = code[0::3] ^ a
	for b in lowercase:
		if found == True:
			break
		decrypt[1::3] = code[1::3] ^ b
		for c in lowercase:
			if found == True:
				break
			decrypt[2::3] = code[2::3] ^ c
			text = ''.join([chr(x) for x in decrypt])
			if ' and ' in text:
				if text not in candidates:
					candidates.append(text)
					print "password: " + chr(a)+chr(b)+chr(c)
					print "text: " + text
					found = True

print "answer: ", sum(decrypt)