import numpy as np
import matplotlib.pyplot as plt


def main():

    """
    x = np.linspace(-np.pi, np.pi, 256, endpoint=True)  #   x轴，从-pi到pi，共256个点，最后的点设置为存在
    c, s = np.cos(x), np.sin(x)
    plt.figure(1)
    plt.plot(x, c, color='blue', linewidth=2.0, linestyle="-", label="COS", alpha=0.5)
    plt.plot(x, s, "r*", label="SIN", color="black")
    plt.title("sin and cos")

    ax = plt.gca()  # 轴的编辑器
    ax.spines["right"].set_color("none")    # 将右边的边框去除
    ax.spines["top"].set_color("none")      # 将头部的边框去除
    ax.spines["left"].set_position(("data", 0))         # 左边框放到0位置
    ax.spines["bottom"].set_position(("data", 0))       # 底部边框移动到0位置
    ax.xaxis.set_ticks_position("bottom")               # x轴上的值放到x轴下面
    ax.yaxis.set_ticks_position("left")                 # y轴上的值放到y轴的左边
    plt.legend(loc="upper left")                        # 图例的位置，在左上方
    plt.grid()                                          # 网格线
    for label in ax.get_xticklabels()+ax.get_yticklabels():
        label.set_fontsize(16)

    plt.axis([-1, 1, -0.5, 1])                          # 设置x,y轴的显示范围
    plt.show()
    """


def main2():
    fig = plt.figure()
    ax = fig.add_subplot(3, 3, 1)  # 位置3*3的第一个位置
    n = 128
    X = np.random.normal(0, 1, n)
    Y = np.random.normal(0, 1, n)
    T = np.arctan2(X, Y)
    # plt.axes([0.025, 0.025, 0.95, 0.95])
    ax.scatter(X, Y, s=75, c=T, alpha=0.2)  # 散射图
    plt.xlim(-1.5, 1.5), plt.xticks([])
    plt.ylim(-1.5, 1.5), plt.yticks([])
    plt.axis()
    plt.title("scatter")
    plt.xlabel("x")
    plt.ylabel("y")
    # plt.show()
    # bar树状图
    fig.add_subplot(332)
    n = 10
    X = np.arange(n)
    Y1 = (1 - X/float(n)) * np.random.uniform(0.5, 1.0, n)
    Y2 = (1 - X/float(n)) * np.random.uniform(0.5, 1.0, n)
    plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
    plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')

    # 饼图
    fig.add_subplot(333)
    n = 20
    Z = np.ones(n)
    Z[-1] *= 2
    plt.pie(Z, explode=Z * .05, colors=['%f' % (i/float(n)) for i in range(n)],
            labels=['%.2f' % (i/float(n)) for i in range(n)])
    plt.gca().set_aspect('equal')
    plt.xticks([]), plt.yticks([])
    plt.savefig('./data/fig.png')
    plt.show()


if __name__ == '__main__':
    main2()