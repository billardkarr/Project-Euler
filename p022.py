import csv

with open('p022_names.txt') as f:
	reader = csv.reader(f)
	names = sorted(list(reader)[0])

score = 0
for k in range(len(names)):
	score += (k+1)*sum([ord(letter)-64 for letter in names[k]])

print score