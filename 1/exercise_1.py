# Solutions to exercises for day3 of python course.

import numpy as np

a = 0*np.arange(1, 11)
a[4] = 1

b = np.arange(10, 50)
c = b[::-1]
d = np.arange(0, 9).reshape(3,3) 

e = []
for i, data in enumerate([1,2,0,0,4,0]):
	if data !=0:
		e.append(i)

f = np.mean(np.random.random((30)))
g = np.arange(6).reshape(2,3)
g[:,0::2] = 1
g[:,1::2] = 0

h = np.arange(0, 64).reshape(8,8) 
h[:,0::2] = 0
h[:,1::2] = 1

i = np.array([0,1])
i = np.tile(i, (8,4))

# j
Z = np.arange(11)
Z = Z[[0, 1, 2, 3, 8, 9, 10]] # negate all elements which are between indices 3 and 8
print(Z)

# k
Z = np.random.random(10)
print Z
Z = np.sort(Z)
print(Z)

# l
A = np.random.randint(0,2,5)
B = np.random.randint(0,2,5)
equal = np.array_equal(A,B)
print(equal)

# m
Z = np.arange(10, dtype=np.int32)
print(Z.dtype)
Z = np.float32(Z)
print(Z.dtype)

# n
A = np.arange(9).reshape(3,3)
B = A + 1
C = np.dot(A,B)
D = np.diag(C)
print D

if False:
	print a
	print b
	print c
	print d
	print e
	print f
	print g 
	print h
	print i



