import numpy as np
A = np.arange(2,14).reshape((3,4)) 

# array([[ 2, 3, 4, 5]
#        [ 6, 7, 8, 9]
#        [10,11,12,13]])
# argmin() 和 argmax() 两个函数分别对应着求矩阵中最小元素和最大元素的索引         
print(np.argmin(A))    # 0
print(np.argmax(A))    # 11

print(np.mean(A))        # 7.5
print(np.average(A))     # 7.5
print(A.mean())          # 7.5
print(np.median(A))       # 7.5 中位数
print(np.cumsum(A)) 

# [2 5 9 14 20 27 35 44 54 65 77 90]
print(np.diff(A))   

print(np.nonzero(A))     #这个函数将所有非零元素的行与列坐标分割开，重构成两个分别关于行和列的矩阵。

# (array([0,0,0,0,1,1,1,1,2,2,2,2]),array([0,1,2,3,0,1,2,3,0,1,2,3]))

B = np.arange(14,2, -1).reshape((3,4)) 

# array([[14, 13, 12, 11],
#       [10,  9,  8,  7],
#       [ 6,  5,  4,  3]])

print(np.sort(B))    

# array([[11,12,13,14]
#        [ 7, 8, 9,10]
#        [ 3, 4, 5, 6]])
print(np.transpose(B))    #矩阵的转置
print(B.T)

print(B)
# array([[14,13,12,11]
#        [10, 9, 8, 7]
#        [ 6, 5, 4, 3]])
#这个函数的格式是clip(Array,Array_min,Array_max)，顾名思义，Array指的是将要被执行用的矩阵，
# 而后面的最小值最大值则用于让函数判断矩阵中元素是否有比最小值小的或者比最大值大的元素，
# 并将这些指定的元素转换为最小值或者最大值。
print(np.clip(B,5,9))    
# array([[ 9, 9, 9, 9]
#        [ 9, 9, 8, 7]
#        [ 6, 5, 5, 5]])