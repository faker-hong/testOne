import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# 返回的是颜色的集合，这里取第一个颜色
base_color = sb.color_palette()[0]

df = pd.DataFrame(data=[{"cat_var": 'A', "1": 5, "2": 100, "3": 70},
                        {"cat_var": 'A', "1": 11, "2": 100, "3": 70},
                        {"cat_var": 'B', "1": 12, "2": 100, "3": 70},
                        {"cat_var": 'B', "1": 13, "2": 100, "3": 70},
                        {"cat_var": 'B', "1": 20, "2": 100, "3": 70},
                        {"cat_var": 'C', "1": 21, "2": 100, "3": 70},])
# 获取df列名集合
x_names = df.columns.values

# 画一个表示频率的柱状图，x表示计算频率的列
# g = sb.countplot(data=df, x='cat_var', color=base_color)
# 也可以将列cat_var设置为y
# g = sb.countplot(data=df, y='cat_var')
# plt.yticks(rotation=90)
# plt.show()


# Pie Charts
# 获取排序过的列中值的数量
sorted_counts = df['cat_var'].value_counts()
# 甜甜圈图，width小于1，移除圆心的颜色
# plt.pie(sorted_counts, labels=sorted_counts.index, startangle=90, counterclock=False, wedgeprops={'width': 0.5})
# plt.axis('square')
# plt.show()



# Histograms
# bin_edges = np.arange(0, df['1'].max()+5, 5)
# bins为直方图间距集合
# plt.hist(data=df, x='1', bins=bin_edges)
# plt.show()


# 创建画布
plt.figure(figsize=[10, 5])
# 画板为1行2列，现在画第一个
plt.subplot(1, 2, 1)
bins = np.arange(0, df['1'].max()+5, 5)
plt.hist(data=df, x='1', bins=bins)

plt.subplot(1, 2, 2)
bins = np.arange(0, df['1'].max()+2, 2)
plt.hist(data=df, x='1', bins=bins)
plt.show()


# Descriptive Statistics, Outliers and Axis Limits
# 可以根据数据来更改间距和轴限制， e.g
plt.xlim((0, 50))   # 将x轴的数值限制在0-50


# Scatterplots and Correlation
plt.scatter(data=df, x='1', y='2')
# fit_reg为true为显示线性相关的一条直线, x_jitter为抖动，使每个值稍微偏离真实值
sb.regplot(data=df, x='1', y='2', fit_reg=False, x_jitter=0.3, scatter_kws={'alpha': 0.2})

# heat maps
# 数量越多，网格颜色越深
plt.subplot(1, 2, 2)
bins_x = np.arange(0.5, 10.5+1, 1)
bins_y = np.arange(-0.5, 10.5+1, 1)
plt.hist2d(data=df, x='disc_var1', y='disc_var2',
           bins=[bins_x, bins_y])
plt.colorbar()

# Violin Plots，The distribution is plotted as a kernel density estimate
sb.violinplot(data=df, x='1', y='1')

# Box Plots
# 形图更倾向于对数据进行汇总，主要报告每个类别级别上的数值的一组描述性统计
sb.boxplot(data=df, x='1', y='1')


# Faceting 列子
group_means = df.groupby(['many_cat_var']).mean()
group_order = group_means.sort_values(['num_var'], ascending=False).index

# col_wrap表示每行5张图，size为图的大小
g = sb.FacetGrid(data=df, col='many_cat_var', col_wrap=5, size=2,
                 col_order=group_order)
g.map(plt.hist, 'num_var', bins=np.arange(5, 15+1, 1))
g.set_titles('{col_name}')