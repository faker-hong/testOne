import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


iris = sns.load_dataset('tips')

# 萼片（sepal）和花瓣（petal）的大小关系（散点图）

# 增加两列，一个为萼片的size， 一个是花瓣的size
iris['sepal_size'] = iris['sepal_length'] * iris['sepal_width']
iris['petal_size'] = iris['petal_length'] * iris['petal_width']

# 画图
# fig, ax = plt.subplots()
# ax.scatter(iris['sepal_size'], iris['petal_size'])

# 添加标题和坐标说明
# ax.set_title('Size of Sepal vs Size of Petal')
# ax.set_xlabel('size of sepal')
# ax.set_ylabel('size of petal')
# plt.show()



# 不同种类（species）鸢尾花萼片和花瓣的大小关系（分类散点子图）

# 获得鸢尾花的3个类别的数据
# species = iris['species'].unique()
# data1 = iris[iris['species'] == species[0]]
# data2 = iris[iris['species'] == species[1]]
# data3 = iris[iris['species'] == species[2]]

# 作图
# fig, ax2_2 = plt.subplots()
#
# ax2_2.scatter(data1['sepal_size'], data1['petal_size'], color='#ff0000', label=species[0])
# ax2_2.scatter(data2['sepal_size'], data2['petal_size'], color='#00ff00', label=species[1])
# ax2_2.scatter(data3['sepal_size'], data3['petal_size'], color='#0000ff', label=species[2])
# ax2_2.legend(loc='best')

# 添加标题和坐标说明
# ax2_2.set_title('Size of Sepal vs Size of Petal')
# ax2_2.set_xlabel('size of sepal')
# ax2_2.set_ylabel('size of petal')
# plt.show()



# 不同种类鸢尾花萼片和花瓣大小的分布情况（柱状图）

# 鸢尾花种类
# species = iris['species'].unique()
# data1 = iris[iris['species'] == species[0]]
# data2 = iris[iris['species'] == species[1]]
# data3 = iris[iris['species'] == species[2]]
#
# total_width, n = 0.8, 2
# width = total_width / n
#
# sepal_large = []
# petal_large = []
# 计算各类别sepal_size大的数量
# sepal_0 = data1[data1['sepal_size'] > data1['petal_size']].shape[0]
# sepal_1 = data2[data2['sepal_size'] > data2['petal_size']].shape[0]
# sepal_2 = data3[data3['sepal_size'] > data3['petal_size']].shape[0]
# sepal_large.append(sepal_0)
# sepal_large.append(sepal_1)
# sepal_large.append(sepal_2)

# 计算各类别petal_size大的数量
# petal_0 = data1.shape[0] - sepal_0
# petal_1 = data2.shape[0] - sepal_1
# petal_2 = data3.shape[0] - sepal_2
# petal_large.append(petal_0)
# petal_large.append(petal_1)
# petal_large.append(petal_2)
#
#
# plt.bar(species, sepal_large, width=width, label='sepal', color='red')
# plt.bar(species+width, petal_large, width=width, label='petal', color='green')
#
# plt.legend(loc='upper left')
# plt.xlabel('classes')
# plt.ylabel('number of large')
# plt.show()