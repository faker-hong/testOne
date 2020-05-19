from random import choice

class RandomWalk():
    """一个生成随机漫步数据的类"""

    def __init__(self, number_point=500):
        self.number_point = number_point

        #所有随机漫步都始于（0，0）
        self.x_value=[0]
        self.y_value=[0]

    def fill_walk(self):
        while len(self.x_value) < self.number_point:
            x_direction = choice([1, -1])
            x_distance = choice([1, 2, 3, 4])
            y_direction = choice([1, -1])
            y_distance = choice([1, 2, 3, 4])

            x_step = x_distance * x_direction
            y_step = y_distance * y_direction

            if x_step == 0 and y_step == 0:
                continue

            x_next = self.x_value[-1] + x_step
            y_next = self.y_value[-1] + y_step

            self.x_value.append(x_next)
            self.y_value.append(y_next)
