'''
    目的：将一个类的接口转换成客户希望的另外一个接口。适配器m模式使得原本由于接口不兼容而不能一起工作的那些类可以一起工作

    优点：
        1.可以让任何两个没有关联的类一起运行
        2.提高了类的复用
        3.增加了类的透明度
        4.灵活性好
    缺点：
        1.过多的使用适配器，让系统非常凌乱
        2.java最多允许继承一个类，所以最多只能适配一个适配类，而且目标类必须是抽象类

    Synthesizer类和Human类要想和Computer类一样，调用execute来执行方法
'''


class Computer:
    def __init__(self, name):
        self.name = name

    # print(对象)的时候，会自动输出return的数据
    def __str__(self):
        return 'the {} computer'.format(self.name)

    def execute(self):
        return 'executes a program'


class Synthesizer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'the {} synthesizer'.format(self.name)

    def play(self):
        return 'is playing an electronic song'


class Human:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '{} the human'.format(self.name)

    def speak(self):
        return 'says hello'


# 创建通用的Adapter类，将不同接口适配到统一接口中
class Adapter:
    def __init__(self, obj, adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __str__(self):
        return str(self.obj)


if __name__ == '__main__':
    objects = [Computer('Asus')]
    synth = Synthesizer('moog')
    objects.append(Adapter(synth, dict(execute=synth.play)))
    human = Human('Bob')
    objects.append(Adapter(human, dict(execute=human.speak)))

    for i in objects:
        print('{} {}'.format(str(i), i.execute()))
        print('type is {}'.format(type(i)))