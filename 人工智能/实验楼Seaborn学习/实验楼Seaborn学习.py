import matplotlib.pyplot as plt
import seaborn as sns

# 声明使用的是seaborn的样式
sns.set(palette='bright')
'''
sns.set()的一些默认参数
sns.set(context='notebook', style='darkgrid', palette='deep', font='sans-serif', font_scale=1, color_codes=False, rc=None)

context:参数控制默认的画幅大小，分别有[paper, notebook, talk, poster], 其中， poster > talk > notebook > paper

style:参数控制默认样式， 分别有[darkgrid, whitegrid, dark, white, ticks]

palette: 参数为预设的调色板， 分别有[deep, muted, bright, pastel, dark, colorblind]

font: 设置字体

font_scale: 设置字体大小

color_codes: 不使用调色板而采用之前的色彩缩写
'''

# 数据
x = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
y_bar = [3, 4, 6, 8, 9, 10, 9, 11, 7, 8]
y_line = [2, 3, 5, 7, 8, 9, 8, 10, 6, 7]

plt.bar(x, y_bar)
plt.plot(x, y_line, '-o', color='y')
plt.show()