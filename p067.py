pyramid = []
with open("p067_triangle.txt") as f:
    for line in f:
        numbers_str = line.split()
        pyramid.append([int(x) for x in numbers_str])

N = len(pyramid)
sums = [pyramid[0][0]]

for i in range(N-1):
	level = pyramid[i+1]
	first = sums[0] + level[0]
	last = sums[-1] + level[-1]
	middle = []
	for j in range(i):
		a = sums[j]+level[j+1]
		b = sums[j+1]+level[j+1]
		middle.append(max(a,b))
	sums = [first] + middle + [last]

print max(sums)