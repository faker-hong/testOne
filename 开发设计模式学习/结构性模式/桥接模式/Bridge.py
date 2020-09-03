'''
意图：将抽象部分与实现部分分离，使它们都可以独立的变化。

主要解决：在有多种可能会变化的情况下，用继承会造成类爆炸问题，扩展起来不灵活。

何时使用：实现系统可能有多个角度分类，每一种角度都可能变化。

如何解决：把这种多角度分类分离出来，让它们独立变化，减少它们之间耦合。

关键代码：抽象类依赖实现类。

优点： 1、抽象和实现的分离。 2、优秀的扩展能力。 3、实现细节对客户透明。

缺点：桥接模式的引入会增加系统的理解与设计难度，由于聚合关联关系建立在抽象层，要求开发者针对抽象进行设计与编程。

注意事项：对于两个独立变化的维度，使用桥接模式再适合不过了。
'''


# 具体实现者1/2
class DrawingAPI1(object):

    def draw_circle(self, x, y, radius):
        print('API1.circle at {}:{} 半径 {}'.format(x, y, radius))


# 具体实现者2/2
class DrawingAPI2(object):

    def draw_circle(self, x, y, radius):
        print('API2.circle at {}:{} 半径 {}'.format(x, y, radius))


# 优雅的抽象
class CircleShape(object):

    def __init__(self, x, y, radius, drawing_api):
        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api

    # 低层次的，即具体的的实现
    def draw(self):
        self._drawing_api.draw_circle(self._x, self._y, self._radius)

    # 高层次的抽象
    def scale(self, pct):
        self._radius *= pct


def main():
    shapes = (
        CircleShape(1, 2, 3, DrawingAPI1()),
        CircleShape(5, 7, 11, DrawingAPI2())
    )

    for shape in shapes:
        '''坐标--缩放变换'''
        shape.scale(2.5)
        shape.draw()


if __name__ == '__main__':
    main()