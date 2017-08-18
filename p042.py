import csv
import numpy

with open('p042_words.csv') as f:
	reader = csv.reader(f)
	words = sorted(list(reader)[0])

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letters = [c for c in letters]

scores = []
for word in words:
	score = 0
	for c in word:
		score += letters.index(c) + 1
	scores.append(score)


triangluars = [1]
i = 1
while max(triangluars) < max(scores):
	i += 1
	triangluars.append(i*(i+1)/2)

total = 0
for score in scores:
	if score in triangluars:
		total += 1

print total