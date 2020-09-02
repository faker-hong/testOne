'''
    目的：动态的给一个对象添加一些额外的职责。就增加功能来说，装饰器比增加字类更灵活

    优点:
        装饰器与被装饰器可以相互独立，不会相互耦合，装饰模式是继承的一个替代模式，装饰器可以动态扩展一个实现类的功能

    缺点：
        多层装饰器复杂
'''


# 小摊上卖手抓饼和火烧，手抓饼5块一个，火烧6块一个，可以加辣椒酱，生菜，鸡蛋，牛肉片，火腿片
# 辣椒酱免费，生菜多加1元，鸡蛋多加2元，牛肉片多加5元，火腿片多加4元
# 顾客根据自己需要进行组合选择

class Bing:
    name = ''
    price = 0.0

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price

    def getName(self):
        return self.name


class HandHeldCake(Bing):
    def __init__(self):
        self.name = '手抓饼'
        self.price = 5


class HuoShao(Bing):
    def __init__(self):
        self.name = '火烧'
        self.price = 6


class decorator:
    def getName(self):
        pass

    def getPrice(self):
        pass


class spicyDecorator(decorator):
    def __init__(self, decorator):
        self.decorator = decorator

    def getName(self):
        return '+spicy'

    def getPrice(self):
        return 0


class vegatableDecorator(decorator):
    def __init__(self, decorator):
        self.decorator = decorator

    def getName(self):
        return '+生菜'

    def getPrice(self):
        return 1


class eggDecorator(decorator):
    def __init__(self, decorator):
        self.decorator = decorator

    def getName(self):
        return '+鸡蛋'

    def getPrice(self):
        return 2


class beefDecorator(decorator):
    def __init__(self, decorator):
        self.decorator = decorator

    def getName(self):
        return '+牛肉片'

    def getPrice(self):
        return 5


class peikonDecorator(decorator):
    def __init__(self, decorator):
        self.decorator = decorator

    def getName(self):
        return '+火腿片'

    def getPrice(self):
        return 4


if __name__ == '__main__':
    hs = HuoShao()
    szb = HandHeldCake()
    print(hs.getName(), hs.getPrice())
    egg = eggDecorator(hs)
    print(hs.getName(), egg.getName(), hs.getPrice() + egg.getPrice())
    beef = beefDecorator(egg)
    print(hs.getName(), egg.getName(), beef.getName(), hs.getPrice() + egg.getPrice() + beef.getPrice())