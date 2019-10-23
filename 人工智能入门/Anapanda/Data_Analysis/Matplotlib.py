from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns
'''
    1.创建figure对象-----画布
    2.创建子图fig1， Asex对象
    3.画图，选择类型，散点，折现，饼图等
    4.设置title， legend， XY轴， grid网格
    5.文本text， 注释annotation， 刻度tick

    面向对象画图
    返回画布和图像列表。这里是一行两列
    figure, axes = plt.subplots(nrows=1, ncols=2, figsize=(20, 8), dpi=80)
    面向对象，方法从原来的多一个plt.xticks到axes[0].set_xticks,但并不全这样
    axes[0].plot()
    axes[1].plot()
'''
# 创建图形对象和子图
# f = plt.figure()
# 设置图形总标题
# f.suptitle('abc')

# 这边有两种方法添加子图，这里的对象是Ases对象
# fig1 = plt.subplot(121)
# fig2 = f.add_subplot(122)

#  参数说明([相对左下角X轴距离，相对左下角Y轴距离，X方向相对figure长度，Y轴方向相对figure长度],背景色)
# fig3 = f.add_axes([0.1, 0.1, 0.2, 0.6], facecolor='grey')
# fig4 = plt.axes([0.4, 0.4, 0.4, 0.4], facecolor='green')
# 设置X，Y轴显示范围
# fig3.set_xlim(2, 4)
# fig3.set_ylim(2, 4)
# 设置X，Y轴刻度
# fig3.set_xticks([1, 2, 3, 4])
# fig3.set_yticks([2, 3, 4, 5])

# 坐标轴的显示与移动，先获取坐标轴对象
# zuobiao_zhou = fig3.axes
# zuobiao_zhou.spines['left'].set_color('none')
# zuobiao_zhou.spines['right'].set_color('red')
# zuobiao_zhou.spines['bottom'].set_color('grey')
# zuobiao_zhou.spines['top'].set_color('green')

# 刻度显示位置调整
# zuobiao_zhou.yaxis.set_ticks_position('right')
# zuobiao_zhou.xaxis.set_ticks_position('top')

# 与图像线条相关的设置
# 直接在画线时通过参数设置
# a = fig3.plot([1, 2, 3, 4, 5], [2, 4, 6, 8, 10], color='red', linewidth=3, linestyle='--')
# fig3.legend(loc=1)

# 标题，网格，图例都是在axes对象上操作的，都是属于axes的方法
# fig3.set_title('ahahah', loc='right', fontsize=10, color='red')
# fig3.grid(axis= 'x', color='r', linestyle='-', linewidth=5)

# text,参数说明(X轴数值位置,Y轴数值位置,文本信息), 如果超出范围，无法显示
# fig3.text(0.2, 0.5, 'hhhhh', color='red')
'''
可选参数：
    Alpha=0.5
    
    color='green',
    
    backgroundcolor=‘yellow’

    fontsize=15,（可以简写为size）

    fontstyle=20（可以简写为style）

    rotation='60',表示文本旋转多少度

    fontweight='bold',（可以简写为weight）取值可以是（normal bold heavy light ultrabold ultralight）

    family=‘serif’ 字体

    linespace=1.5  字体行距

    horizontalalignment=‘center’ x参数表示的位置（也可以简写为ha）取值可以是（center right left）

    verticalalignment=‘center’  y参数表示的位置（简写为va）取值可以是（center top bottom baseline）

    multialignment=‘center’ 多行位置控制 取值可以是（center right left）
'''



# annotate注释的使用
# 绘制一个余弦曲线
# fig, ax = plt.subplots()
# t = np.arange(0.0, 5.0, 0.01)
# s = np.cos(2 * np.pi * t)
# line, = ax.plot(t, s, lw=2)
#
# # 绘制一个黑色，两端缩进的箭头
# ax.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
#             xycoords='data',
#             arrowprops=dict(facecolor='black', shrink=0.05)
#             )
# ax.set_ylim(-2, 2)


# Seaborn
# def sinplot(flip=1):
#     x = np.linspace(0, 14, 100)
#     for i in range(1, 7):
#         plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)
#     plt.show()
# 五种主题风格 darkgrid，whitegrid，dark，white，ticks
# sns.set_style('dark')
# sinplot()
