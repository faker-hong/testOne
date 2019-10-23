from matplotlib import pyplot as plt

# 设置中文能正常显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# x轴年龄
x = range(11, 31)

# y轴女朋友个数
y = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]

# 设置图像大小， 清晰度
plt.figure(figsize=(20, 8), dpi=80)

# 联立
plt.plot(x, y)

# 设置x轴刻度： 中文字符串
_xtick_labels = [u'{}岁'.format(i) for i in x]
plt.xticks(x, _xtick_labels)

plt.yticks(range(0, 9))

# 添加x轴y轴的描述
plt.xlabel(u'年龄')
plt.ylabel(u'女朋友个数')

# 网格线深度
plt.grid(alpha=0.5)

plt.show()