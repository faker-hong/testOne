import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# 获取数据
data = sns.load_dataset('flights')
# print(data.head(20))

# 分析年度乘客总量变化情况（折线图）

# 方法一

# 1.以year列分组，求和passengers
# 2.year为横坐标，passengers为纵坐标画图
# 3.直接使用pandas内置的matplotlib画图
# data = data.groupby('year').sum()
# data.plot()
# plt.show()

# 方法二

# 1.以year列分组，求和passengers
# 2.year为横坐标，passengers为纵坐标画图
# 3.subplots()方法返回画布和子图

group_year = data.groupby('year').sum()
fig, ax = plt.subplots()
ax.plot(group_year.index, group_year['passengers'])
ax.set_xlabel('year')
ax.set_ylabel('sum passengers')
ax.set_title('Annual change of passenger number')
# plt.show()


# 分析乘客在各月份的分布（柱状图)

# 1.以月份分组
# 2.月份为x, 乘客数为y
# 3.月份一般取前三位，这里稍作处理

group_month = data.groupby('month').sum()
x = group_month.index
x = [i[:3] for i in x]
y = group_month['passengers']
fig1, ax1 = plt.subplots()
ax1.bar(x, y, align='center')
ax1.set_xlabel('month')
ax1.set_ylabel('passengers')
ax1.set_title('Every month change of passengers number')
plt.show()