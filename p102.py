import numpy

triangles = []
with open("p102_triangles.txt") as f:
    for line in f:
        numbers_str = line.split(',')
        triangles.append([int(x) for x in numbers_str])

winners = 0
for triangle in triangles:
	A = numpy.array(triangle[0:2])
	B = numpy.array(triangle[2:4])
	C = numpy.array(triangle[4::])
	pairs = [[A,B,C],[B,C,A],[C,A,B]]
	count = 0
	for pair in pairs:
		V = pair[1]-pair[0]
		N = numpy.array([V[1],-V[0]])
		x = numpy.dot(N,pair[0])
		y = numpy.dot(N,pair[2])
		if max(x,y) > 0 and min(x,y) < 0:
			count += 1
	if count == 3:
		winners += 1

print winners


