# Program to multiply two matrices using nested loops, using numpy
import numpy as np
import time 
import random

start = time.clock()
N = 250

## Optimized with NumPy

# NxN matrix
X = []
for i in range(N):
    X.append([np.random.randint(0,100) for r in range(N)])

Y = []
for i in range(N):
    Y.append([np.random.randint(0,100) for r in range(N+1)])

Z = np.dot(X,Y)

print 'NumPy version took: {0} seconds'.format(time.clock()-start) 


## Old script

# NxN matrix
X = []
for i in range(N):
    X.append([random.randint(0,100) for r in range(N)])

# Nx(N+1) matrix
Y = []
for i in range(N):
    Y.append([random.randint(0,100) for r in range(N+1)])

# result is Nx(N+1)
result = []
for i in range(N):
    result.append([0] * (N+1))

# iterate through rows of X
for i in range(len(X)):
    # iterate through columns of Y
    for j in range(len(Y[0])):
        # iterate through rows of Y
        for k in range(len(Y)):
            result[i][j] += X[i][k] * Y[k][j]

print 'Regular version took: {0} seconds'.format(time.clock()-start) 


### Checking if outputs are the same

# NxN matrix
X = []
for i in range(N):
    X.append([np.random.randint(0,100) for r in range(N)])

Y = []
for i in range(N):
    Y.append([np.random.randint(0,100) for r in range(N+1)])

Z = np.dot(X,Y)

result = []
for i in range(N):
    result.append([0] * (N+1))

# iterate through rows of X
for i in range(len(X)):
    # iterate through columns of Y
    for j in range(len(Y[0])):
        # iterate through rows of Y
        for k in range(len(Y)):
            result[i][j] += X[i][k] * Y[k][j]


print 'Checking if the two variations get the same result...'
print Z==result
