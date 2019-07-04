import numpy as np
A = np.arange(3,15)

# array([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
         
print(A[3])    # 6
B = np.arange(3,15).reshape((3,4))
"""
array([[ 3,  4,  5,  6]
       [ 7,  8,  9, 10]
       [11, 12, 13, 14]])
"""
         
print(B[2])  #索引第3行         
# [11 12 13 14]

#二维索引
print(B[1][1])      # 8
print(B[1, 1:3])    # [8 9]

for row in B:    #打印行
    print(row)

for column in B.T:  #打印列
    print(column)

A = np.arange(3,15).reshape((3,4))
         
print(B.flatten())   #展开成一行
# array([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

for item in B.flat:   #flat是一个迭代器，是个object
    print(item)