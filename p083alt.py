import numpy

matrix = []
with open("p082_matrix.txt") as f:
    for line in f:
        numbers_str = line.split(',')
        matrix.append([int(x) for x in numbers_str])

matrix = numpy.array(matrix)
N = len(matrix)

pathsums = 0*matrix
pathsums[0,0] = matrix[0,0]

found = numpy.where(pathsums > 0)
print found

print pathsums
for i in range(N):
    for j in range(N):
        if pathsums[i,j] == 0:
            pathsums[i,j]