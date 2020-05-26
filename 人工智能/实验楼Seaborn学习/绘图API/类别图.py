import seaborn as sns
import matplotlib.pyplot as plt

'''
分类散点图:
stripplot() (kind="strip")
swarmplot() (kind="swarm")

分类分布图:
boxplot() (kind="box")
violinplot() (kind="violin")
boxenplot() (kind="boxen")

分类估计图:
pointplot() (kind="point")
barplot() (kind="bar")
countplot() (kind="count")
'''

iris = sns.load_dataset("iris")


sns.catplot(x="sepal_length", y="species", data=iris)

# kind='swarm' 防止重叠，有效的观察数据
sns.catplot(x="sepal_length", y="species", kind="swarm", data=iris)


# 箱型图
sns.catplot(x="sepal_length", y="species", kind="box", data=iris)


# 小提琴图
sns.catplot(x="sepal_length", y="species", kind="violin", data=iris)


# 增强箱型图
sns.catplot(x="species", y="sepal_length", kind="boxen", data=iris)


# 点线图
sns.catplot(x="sepal_length", y="species", kind="point", data=iris)


# 条形图
sns.catplot(x="sepal_length", y="species", kind="bar", data=iris)


# 计数条形图
sns.catplot(x="species", kind="count", data=iris)