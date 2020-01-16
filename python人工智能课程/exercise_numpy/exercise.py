from collections import Counter

import numpy as np


# 生成一个都是0的数组，参数填写数组的形状
zero_1 = np.zeros(10)
zero_2 = np.zeros((10, 10))
# print(zero_1)
# print(zero_2)


# 生成一个都是1的数组，参数填写数组的形状
ones_1 = np.ones(10)
ones_2 = np.ones((10, 10))
# print(ones_1)
# print(ones_2)


# 创建连续范围值的数组
range = np.arange(20, 50)
# print(range)


# 反转向量
range = range[::-1]
# print(range)


# 改变数组形状
# 生成一个2*8的数组，然后改为4*4
range = np.ones((2, 8))
range = range.reshape((4, 4))
# print(range)


# 单位矩阵,3*3
e = np.eye(3)


# 随机数
rand_1 = np.random.random((10, 10))
# print(rand_1)
# rand_max = rand_1.max()
# rand_min = rand_1.min()
# print(rand_max, rand_min)


# 创建一个二维数组，其中边界值为1，其余值为0
Z = np.ones((10, 10))
Z[1:-1, 1:-1] = 0
# print(Z)

# 创建一个8x8 的矩阵，并且设置成棋盘样式,1::2表示从一开始，步长为2
Z = np.zeros((8, 8))
Z[1::2, ::2] = 1
Z[::2, 1::2] = 1
# print(Z)


# 对5*5的数组进行归一化 (x - min) / (max - min)
Z = np.random.random((5, 5))
result = (Z - Z.min()) / (Z.max() - Z.min())
# print(result)


# 矩阵相乘，第一个矩阵的列对应第二个矩阵的行，否则报错
x = np.random.random((5, 3))
y = np.random.random((3, 2))
z = np.dot(x, y)
# print(z)


# 对数组中做判断
Z = np.random.randint(1, 10, size=20)
# print(Z)
# print(Z[Z > 5])


# 找两个数组的相同元素    np.intersect1d()
Z1 = np.random.randint(0, 10, 10)
Z2 = np.random.randint(0, 10, 10)
# print(np.intersect1d(Z1, Z2))


# 如何得到昨天，今天，明天的日期
yesterday = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
today = np.datetime64('today', 'D')
tomorrow = np.datetime64('today', 'D') + np.timedelta64(1, 'D')
# print(yesterday)
# print(today)
# print(tomorrow)


# ndarray的加减乘除,out表示把结果复制给该对象
A = np.ones(3)*1
B = np.ones(3)*2
C = np.ones(3)*3
# print(np.add(A, B, out=B))
# print(np.divide(A, 2, out=A))
# print(np.negative(A, out=A))
# print(np.multiply(A, B, out=A))


# 创建一个长度为10的随机向量，其值域范围从0到1，但是不包括0和1
# 范围内均匀增长
Z = np.linspace(0, 1, 11, endpoint=False)[1:]
# print(Z)


# 创建一个长度为10的随机向量，并将其排序
# Z = np.random.random(10)
# Z = np.sort(Z)
# print(Z)

# 判断连个数组是否相等
A = np.random.randint(0, 2, 5)
B = np.random.randint(0, 2, 5)
equal = np.array_equal(A, B)
# print(equal)


# 创建只读数组
# Z = np.ones(10)
# Z.flags.writeable = False
# Z[1] = 10


# 创建一个长度为10的向量，并将向量中最大值替换为1
Z = np.random.random(10)
Z[Z.argmax()] = 1
# Z[Z == Z.max()] = 2
# print(Z)


# 给定标量时，如何找到数组中最接近标量的值argmin(),返回最小值的索引
Z = np.arange(100)
v = np.random.uniform(0, 100)
index = (np.abs(Z-v)).argmin()
# print(Z[index])


# 考虑一个向量[1,2,3,4,5],如何建立一个新的向量，在这个新向量中每个值之间有3个连续的零
X = np.zeros(17)
Z = [1, 2, 3, 4, 5]
X[::4] = Z
# print(X)


# 如何找到一个数组中出现频率最高的值
Z = np.random.randint(1, 5, size=20)
c = Counter(Z)
print(c)