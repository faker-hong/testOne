'''
    工厂模式： 定义一个创建对象的接口， 让其字类决定实例化哪个工厂，使其创建过程延迟到字类进行

    优点：
        1.调用者想创建对象，只要知道其名称就行了
        2.扩展性高，如想增加一个产品，增加一个工厂类就行
        3.屏蔽了产品的具体实现

    缺点：
        没增加一个产品，都需要增加一个具体类和对象实现工厂，增加系统的复杂性和系统具体类的依赖

'''


class Person():

    def __init__(self, name, gender):
        self.name = name
        self.age = gender

    def getName(self):
        return self.name

    def getGender(self):
        return self.gender


class Male(Person):

    def __init__(self, name):
        print("hello, Mr." + name)


class Famale(Person):
    def __init__(self, name):
        print("hello, Miss." + name)


class Factory():
    def getPerson(self, name, gender):
        if gender == 'M':
            return Male(name)
        if gender == 'F':
            return Famale(name)


if __name__ == '__main__':
    f1 = Factory().getPerson('97', 'M')
    f2 = Factory().getPerson('98', 'F')



