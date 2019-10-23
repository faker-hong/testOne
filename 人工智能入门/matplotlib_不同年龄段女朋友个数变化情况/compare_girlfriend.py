from matplotlib import pyplot as plt

# 设置中文能正常显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

x = range(11, 31)

# y轴女朋友个数增加一条折线的数据
y_m = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
y_r = [1,0,3,1,2,2,3,3,2,1 ,2,1,1,1,1,1,1,1,1,1]

# 设置图像，清晰度
plt.figure(figsize=(20, 8), dpi=100)

plt.plot(x, y_m, label='小明', color='orange', linestyle=':', linewidth=5, alpha=0.8)
plt.plot(x, y_r, label='小红', color='red', linestyle='-', linewidth=5, alpha=0.8)

# 设置x,y轴的刻度
_xtick_labels = [u'{}岁'.format(i) for i in x]
plt.xticks(x, _xtick_labels)
plt.yticks(range(0, 9))

plt.xlabel(u'年龄')
plt.ylabel(u'女朋友个数')
plt.title(u'小明和小红在11-30岁女朋友个数折线图')

# 网格线深浅
plt.grid(alpha=0.5)

# 将图列的位置放在左上
plt.legend(loc='upper left')

# 保存图片
plt.savefig('./小红和小明女朋友随年龄变化图')
plt.show()