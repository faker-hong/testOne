import seaborn as sns
import matplotlib.pyplot as plt

'''
分布图主要是用于可视化变量的分布情况，一般分为单变量分布和多变量分布。当然这里的多变量多指二元变量，更多的变量无法绘制出直观的可视化图形。
'''

iris = sns.load_dataset('iris')

# 该方法绘制直方图并拟合核密度估计图
# 参数设置 kde=False 则可以只绘制直方图， hist=False 只绘制核密度估计图
sns.distplot(iris['sepal_length'])

# kdeplot只绘制核密度估计图
sns.kdeplot(iris["sepal_length"])


# joinplot主要用于绘制二元变量分布图
sns.jointplot(x="sepal_length", y="sepal_width", data=iris)


# jointplot并不是一个 Figure-level 接口，但其支持 kind= 参数指定绘制出不同样式的分布图。例如，绘制出核密度估计对比图。
sns.jointplot(x="sepal_length", y="sepal_width", data=iris, kind="kde")


# 六边形计数图
sns.jointplot(x="sepal_length", y="sepal_width", data=iris, kind="hex")


# 回归拟合图
sns.jointplot(x="sepal_length", y="sepal_width", data=iris, kind="reg")


# 一次性将数据集中的特征变量两两对比绘图。默认情况下，对角线上是单变量分布图，而其他则是二元变量分布图。
# 引入第三维度会看上去更加直观
sns.pairplot(iris, hue="species")