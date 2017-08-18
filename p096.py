import numpy

grids = []
with open("p096_sudoku.txt") as f:
	i = 0
	for line in f:
		if i % 10 == 0:
			grids.append([])
			i += 1
		else:
			grids[-1].append(list(line.split()[0]))
			i += 1

for grid in grids:
	for i in range(9):
		for j in range(9):
			grid[i][j] = int(grid[i][j])

for i in range(len(grids)):
	grids[i] = numpy.array(grids[i])

for X in grids:
	while True:
		Y = X.copy()
		for i in range(9):
			for j in range(9):
				if X[i,j] == 0:
					out = set(X[i,:])
					out.update(set(X[:,j]))
					for k in range(3):
						out.update(set(X[3*(i/3):3*(i/3 + 1),3*(j/3)+k]))
					out.discard(0)
					candidates = set(range(1,10)).difference(out)
					if len(candidates) == 1:
						X[i,j] = candidates.pop()
		if sum(sum(X != Y)) == 0:
			break

	print X
	print