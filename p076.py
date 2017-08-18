N = 100

def poly(k):
	ans = [0 for i in range(N+1)]
	for i in range(0,N+1,k):
		ans[i] = 1
	return ans

def mult(A,B):
	ans = [0 for i in range(N+1)]
	for k in range(N+1):
		for i in range(k+1):
			ans[k] += A[i]*B[k - i]
	return ans

G = [0 for i in range(N+1)]
G[0] = 1
for i in range(N+10):
	G = mult(G,poly(i+1))

print G[100] - 1