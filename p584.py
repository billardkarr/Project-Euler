import numpy.random as random
import numpy
from decimal import *
getcontext().prec = 9

N = 10
delta = 1
people = 3

sample = []

i = 0
while True:
	birthdays = [random.randint(1,N+1)]
	n = 1
	count = 0
	while count < people:
		birthdays.append(random.randint(1,N+1))
		n += 1
		diff = [[x-y for x in birthdays] for y in birthdays]
		diff = numpy.array(diff)
		counts = sum(diff <= delta) + sum(diff >= N - delta)
		count = (max(counts) - 1)/2
	sample.append(n)
	
	if i % 1000 == 0:
		print Decimal(sum(sample)) / Decimal(len(sample))

	i += 1
	if i > 10**4:
		break

print sample