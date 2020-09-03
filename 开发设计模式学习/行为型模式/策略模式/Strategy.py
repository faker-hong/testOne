'''
意图：定义一系列的算法,把它们一个个封装起来, 并且使它们可相互替换。

主要解决：在有多种算法相似的情况下，使用 if...else 所带来的复杂和难以维护。

何时使用：一个系统有许多许多类，而区分它们的只是他们直接的行为。

如何解决：将这些算法封装成一个一个的类，任意地替换。

关键代码：实现同一个接口。

应用实例： 1、诸葛亮的锦囊妙计，每一个锦囊就是一个策略。 2、旅行的出游方式，选择骑自行车、坐汽车，每一种旅行方式都是一个策略。 3、JAVA AWT 中的 LayoutManager。

优点： 1、算法可以自由切换。 2、避免使用多重条件判断。 3、扩展性良好。

缺点： 1、策略类会增多。 2、所有策略类都需要对外暴露。

使用场景：
    1、如果在一个系统里面有许多类，它们之间的区别仅在于它们的行为，那么使用策略模式可以动态地让一个对象在许多行为中选择一种行为。
    2、一个系统需要动态地在几种算法中选择一种。 3、如果一个对象有很多的行为，如果不用恰当的模式，这些行为就只好使用多重的条件选择语句来实现。
'''
from abc import ABCMeta, abstractmethod


class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def doOperation(self, num1, num2):
        pass


class OperationAdd(Strategy):
    def doOperation(self, num1, num2):
        return num1 + num2


class OperationSubtract(Strategy):
    def doOperation(self, num1, num2):
        return num1 - num2


class OperationMultiply(Strategy):
    def doOperation(self, num1, num2):
        return num1 * num2


class Context():
    def __init__(self, strategy):
        self.strategy = strategy

    def executeStrategy(self, num1, num2):
        return self.strategy().doOperation(num1, num2)


if __name__ == '__main__':
    context = Context(OperationAdd)
    res1 = context.executeStrategy(1, 2)
    print(res1)

    context = Context(OperationSubtract)
    res1 = context.executeStrategy(1, 2)
    print(res1)

    context = Context(OperationMultiply)
    res1 = context.executeStrategy(1, 2)
    print(res1)