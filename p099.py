import numpy as np
X = np.genfromtxt('p099_base_exp.csv',delimiter=',')

bases = np.array(X[:,0])
exponents = np.array(X[:,1])
logs = exponents*np.log(bases)
n = np.argmax(logs)
print n+1