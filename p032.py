sizes = []
for i in range(1,10):
	for j in range(1,i+1):
		if 9 <= 2*(i+j) <= 10:
			sizes.append([i,j])

def get_digits(n):
	digits = []
	while n > 0:
		digits = [n % 10] + digits
		n = n/10
	return digits

def numbers(d):
	answer = []
	if d == 1:
		return digits
	else:
		M = numbers(d-1)
		for i in M:
			used = get_digits(i)
			for k in list(set(digits).difference(used)):
				answer.append(10*i + k)
		return answer

digits = [1,2,3,4,5,6,7,8,9]
ans = []
for size in sizes:
	N1 = numbers(size[0])
	N2 = numbers(size[1])
	for n1 in N1:
		d1 = get_digits(n1)
		for n2 in N2:
			d2 = get_digits(n2)
			d3 = get_digits(n1*n2)
			if sorted(d1 + d2 + d3) == digits:
				ans.append(n1*n2)

print sum(list(set(ans)))