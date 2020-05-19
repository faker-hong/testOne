import numpy as np

# 不使用copy方法，修改a的同时会修改X
# X = np.array([1, 2, 3, 4, 5])
# a = X[2:].copy()
# a[0] = 255
# print(a)
# print(X)

# unique 就等于distinct一下
X = np.array([[1, 2, 3], [2, 3, 4], [4, 5, 6]])
a = np.unique(X)
print(a)

# reshape 修改数组形状 （行，列）
X = np.array(range(20)).reshape(2, 10)
print(X)

# sort()
X = np.array([[3, 2, 1], [2, 3, 4], [4, 5, 6]])
a = np.sort(X, axis=1)
b = np.sort(X, axis=0)
print(X)
print("行方向上排序：\n", a)
print("列方向上排序：\n", b)


# Arithmetic operations and Broadcasting
# 数组间的运算可以直接用+-*/来代替function add(), subtract(), multiply(), divide()
X = np.array([1, 2, 3])
Y = np.array([3, 4, 5])
print(X+Y, np.add(X, Y))
print(X-Y, np.subtract(X, Y))
print(X*Y, np.multiply(X, Y))
print(X/Y, np.divide(X, Y))
# 但个数会每一个元素都操作一遍
# 如1*3的数组与3*3的数据， 3*3的数组的每一列都会与这1*3的数组操作一遍
print(X+2)
Z = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
print(X + Z)



# exercises

# Create a 5 x 5 ndarray with consecutive integers from 1 to 25 (inclusive).
# Afterwards use Boolean indexing to pick out only the odd numbers in the array
X = np.array(range(1, 26)).reshape(5,5)
Y = X[X % 2 == 1]

# Use Broadcasting to create a 4 x 4 ndarray that has its first
# column full of 1s, its second column full of 2s, its third column full of 3s, etc..
X = np.ones((4, 4)) * np.array(range(1, 5))
