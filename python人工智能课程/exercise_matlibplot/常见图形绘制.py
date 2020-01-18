import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# 柱状图
x = [2, 3, 4, 5]
y = [12, 55, 78, 220]
fig, ax = plt.subplots(figsize=(16, 12), ncols=3, nrows=3)

# 设置子图间的间隙
fig.tight_layout(pad=5, h_pad=2, w_pad=2)


# 将3*3的子图展开赋值给axes
axes = ax.flatten()

# 第一张图----柱状图
axes[0].bar(x, y, color='red')
axes[0].set_title('one')


# 第二张图----水平柱状图
axes[1].barh(x, y, color='b')
axes[1].set_title('two')


# 第三张图----直方图
# 对于定量数据的分析，一般采用直方图
# 对于定性数据的分布，一般采用柱状图
data = np.random.randint(0, 100, 100)
bins = np.arange(0, 101, 10)
axes[2].hist(data, bins, color='fuchsia')
plt.xlim(0, 100)


# 第四张图----水平直方图
axes[3].hist(data, bins, color='fuchsia', orientation='horizontal')


# 第五张图----累计分布直方图(排序之后)
axes[4].hist(data, bins, color='fuchsia', cumulative=True, edgecolor='b')
plt.show()


# 第六张图----饼图
# 绘制饼图使用pie方法，主要参数有：
# labels：用于设置扇形图的标签
# colors：用于设置扇形图的颜色
# shadow：用于设定扇形图是否有阴影
# axes[5].pie([10, 20, 30, 80], labels=('a', 'b', 'c', 'd'), colors=('b', 'g', '0', 'c'), shadow=True)
# plt.pie([228, 35, 81, 1], labels=('(2,3]', '(3,4]', '(4,5]', '(5,6]'), colors=('b', 'g', 'r', 'c'), shadow=True)
# plt.show()



# 第七张图----箱型图
df = pd.DataFrame(np.random.rand(10, 5), columns=['A', 'B', 'C', 'D', 'E'])
color = dict(boxes='DarkGreen', whiskers='DarkOrange', medians='DarkBlue', caps='Gray')
# 箱型图着色
# boxes → 箱线
# whiskers → 分位数与error bar横线之间竖线的颜色
# medians → 中位数线颜色
# caps → error bar横线颜色

df.plot.box(ylim=[0, 1.2],
           grid=True,
           color=color,
           ax=ax[7])
plt.show()