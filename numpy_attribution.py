import numpy as np #为了方便使用numpy 采用np简写

arr = np.array([[1,2,3],[4,5,6]]) #列表转化为矩阵
print(arr)

print('number of dim:',arr.ndim)  # 维度
# number of dim: 2

print('shape :',arr.shape)    # 行数和列数
# shape : (2, 3)

print('size:',arr.size)   # 元素个数
# size: 6
