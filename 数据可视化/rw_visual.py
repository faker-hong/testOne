import matplotlib.pyplot as plt
from 数据可视化.random_walk import RandomWalk

while True:
    rw = RandomWalk(5000)
    rw.fill_walk()
    plt.figure(figsize=(10,10))
    number_point = list(range(rw.number_point))
    # plt.plot(rw.x_value,rw.y_value)
    plt.scatter(rw.x_value, rw.y_value,c=number_point, cmap=plt.cm.Blues, edgecolors='none', s=15)
    plt.scatter(0, 0, c='red', edgecolors='none', s=50)
    plt.scatter(rw.x_value[-1], rw.y_value[-1], c='green', edgecolors='none', s=50)
    # plt.axis('off') #去掉坐标轴

    plt.show()

    keep_running = input("是否继续，(y/n)")
    if keep_running == 'n':
        break