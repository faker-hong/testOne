import numpy as np
'''
    查看数组得属性
    1. 数组元素个数：b.size 或 np.size(b)
    2. 数组形状： b.shape 或 np.shape(b)
    3. 数组维度： b.ndim
    4. 数组元素类型： b.dtype
'''
# 1.创建简单数组：直接创建或者将列表,元组转化
# nums = [1, 2, 3]
# nums = np.array(nums)
# nums = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# nums = nums.reshape((2, 4))   reshape方法返回的是一个新的array，不会在原数组上改变



# 2.创建值为0，1或指定数的数组
# nums = np.zeros((2, 2))
# nums = np.ones((3, 3))
# nums = np.full((5, 5), 5)



# 3.创建单位矩阵和对角矩阵
# 单位矩阵， 左上与右下这条对角线的值为1，其余为0
# nums = np.eye(10)
# 如果k为0， 则第一个参数为左上右下对角线数值， 如果k大于0， 则对角线往左上移k个单位，数组的长宽都得相应增加k，k为则相反
# nums = np.diag([10, 20, 30, 40], k=0)     对角矩阵



# 4. 创建随机数组
# nums = np.random.rand(10, 10, 4)  10个10行4列的数值0-1之间数组
# array_uniform = np.random.uniform(0, 100, size=3)  指定0-100范围内，size个随机数
# nums = np.random.randint(50, 60, size=5)  指定50-60范围内的，size个随机整数



# 5. 均匀分布
# X = np.linspace(1, 5, 3)    闭区间1-5之间，3个均差的值



# 6. 正态分布
# 参数（均值， 标准差，维度）
# nums = np.random.normal(loc=1.75, scale=0.1, size=[4, 5])



# 7. Numpy数组的操作
# nums = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [4, 4, 4, 4]])
# print(nums[:2, 1:3])

# 复制，copy是深复制，改变不会互相影响，b = a或 b = a[:],改变数据或相互影响
# a = np.arange(0, 4)
# b = a.copy()
# a[-1] = 9

# 数组排序
# nums = np.array([[1, 3, 2, 4], [5, 6, 7, 8], [4, 4, 4, 4]])
# a = np.sort(nums, axis=1)   # 不在原数组上改变，返回一个新数组, axis=1,在X轴方向上排序，为0在Y轴方向上排序
# nums.sort()         # 对数组对象使用sort()方法，在原数组上改变

# 数组唯一元素
# nums = np.array([[1, 3, 2, 4], [5, 6, 7, 8], [4, 4, 4, 4]])
# 参数说明(数组对象， 在旧数组中index位置， 旧数组元素在新数组中的位置， 与排序中的axis一样)
# print(np.unique(nums))
# print(np.unique(nums, return_index=True))
# print(np.unique(nums, return_index=True, return_inverse=True))
# print(np.unique(nums, return_index=True, return_inverse=True, axis=1))




# 8. reshape与resize
# c = np.array([[[0, 1, 2],
#                 [10, 12, 13]],
#                [[100, 101, 102],
#                 [110, 112, 113]]])
# c_reshape = c.reshape(-1, 2)
# three_dim = c.reshape(3, 2, 2)      # 三维

# resize是在原数组上改变，不会返回新object，元素可变，不足用0补足
# c.resize(3,3)



# 9. Numpy的计算
score = np.array([[80, 88], [82, 81], [84, 75], [86, 83], [75, 81]])
# 大于80为90，小于80则为0
# new_score =np.where(score > 80, 90, 0)


# 求轴的最大最小值
# result = np.amax(score)
# 求每一行的最大值
# result = np.amax(score, axis=1)
# 求每一列的最小值
# result = np.amin(score, axis=0)
# 求每一列的平均值
# result = np.mean(score, axis=0)
# 轴方差
# result = np.std(score, axis=1)


# 数组运算, 加减乘除相同
# score = score[:, :]+5
# 如果是不同的数组，数组间的shape得相同，做除法时除数不能为0
# score = score * 2
# np.intersect1d(参数 1：数组a；参数 2：数组b)：查找两个数组中的相同元素
# np.setdiff1d(参数 1：数组a；参数 2：数组b)：查找在数组a中不在数组b中的元素
# np.union1d(参数 1：数组a；参数 2：数组b)：查找两个数组的并集元素


# 矩阵拼接
# 垂直拼接，列要相同
# v1 = [[0, 1, 2, 3, 4, 5],
#       [6, 7, 8, 9, 10, 11]]
# v2 = [[12, 13, 14, 15, 16, 17],
#       [18, 19, 20, 21, 22, 23],
#       [18, 19, 20, 21, 22, 23]]
# result = np.vstack((v1, v2))
# 水平拼接，行得相同
# result = np.hstack((v1, v2))
# 矩阵删除
# OriginalY = np.array([[1, 2, 3],
#                      [4, 5, 6],
#                      [7, 8, 9]])
# 删除第一行的第一个与第三个元素，转为1维的
# print(np.delete(OriginalY, [0, 2]))
# 删除行上面的第一行与第三行
# print(np.delete(OriginalY, [0, 2], axis=0))
# 删除列上面的第一列与第三列
# print(np.delete(OriginalY, [0, 2], axis=1))

# 矩阵插入
# OriginalY = np.array([[1, 2, 3],
#                      [4, 5, 6],
#                      [7, 8, 9]])
# 添加之后转为1维的
# print(np.insert(OriginalY, 1, [11, 12, 10]))
# 在第一行之后添加一行
# print(np.insert(OriginalY, 1, [[11, 12, 10]], axis=0))
# 在第一列之后添加一列
# print(np.insert(OriginalY, 1, [[11, 12, 10]], axis=1))



# 10.文件加载
np.loadtxt(fname,dtype,comments='#',delimiter=None,skiprows=0,usecols=None)
#
# fname:读取的文件、文件名
#
# dtype：数据类型
#
# comments：注释
#
# delimiter：分隔符，默认是空格
#
# skiprows：跳过前几行读取，默认是0
#
# usecols：读取哪些列，usecols=（1， 2， 5）读取第1,2,5列，默认所有列

# d = StringIO(u"M 21 72\\nF 35 58")
# np.loadtxt(d, dtype={
#                       'names': ('gender', 'age', 'weight'),
#                       'formats': ('S1', 'i4', 'f4')})
# array([(b'M', 21, 72.), (b'F', 35, 58.)],
#     dtype=[('gender', 'S1'), ('age', '<i4'), ('weight', '<f4')])