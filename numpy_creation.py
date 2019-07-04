import numpy as np #为了方便使用numpy 采用np简写

a = np.empty((3,4)) # 数据为empty，3行4列

b = np.arange(10,20,2) # 10-19 的数据，2步长
c = np.arange(12).reshape((3,4))    # 3行4列，0到11
d = np.linspace(1,10,20)    # 开始端1，结束端10，且分割成20个数据，生成线段
e = np.linspace(1,10,20).reshape((5,4))    # 开始端1，结束端10，且分割成20个数据，生成线段