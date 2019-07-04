import numpy as np
A = np.array([1,1,1])
B = np.array([2,2,2])
         
print(np.vstack((A,B)))    # vertical stack
"""
[[1,1,1]
 [2,2,2]]
"""
C = np.vstack((A,B))      
print(A.shape,C.shape)
# (3,) (2,3)

D = np.hstack((A,B))       # horizontal stack
print(D)
# [1,1,1,2,2,2]

print(A.shape,D.shape)
# (3,) (6,)
print(A[np.newaxis,:])
# [[1 1 1]]
print(A[np.newaxis,:].shape)
# (1,3)
print(A[:,np.newaxis])
"""
[[1]
[1]
[1]]
"""
print(A[:,np.newaxis].shape)
# (3,1)

A = np.array([1,1,1])[:,np.newaxis]
B = np.array([2,2,2])[:,np.newaxis]
         
C = np.vstack((A,B))   # vertical stack
D = np.hstack((A,B))   # horizontal stack
print(C)
print(D)
"""
[[1 2]
[1 2]
[1 2]]
"""

print(A.shape,D.shape)
# (3,1) (3,2)

C = np.concatenate((A,B,B,A),axis=0)

print(C)
"""
array([[1],
       [1],
       [1],
       [2],
       [2],
       [2],
       [2],
       [2],
       [2],
       [1],
       [1],
       [1]])
"""

D = np.concatenate((A,B,B,A),axis=1)

print(D)
"""
array([[1, 2, 2, 1],
       [1, 2, 2, 1],
       [1, 2, 2, 1]])
"""