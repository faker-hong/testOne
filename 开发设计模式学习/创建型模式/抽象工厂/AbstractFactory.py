'''
    意图：提供一个创建一系列相关或相互依赖对象的接口，而无需指定它们具体的类。

    优点：当一个产品族中的多个对象被设计成一起工作时，它能保证客户端始终只使用同一个产品族中的对象。

    缺点：产品族扩展非常困难，要增加一个系列的某一产品，既要在抽象的 Creator 里加代码，又要在具体的里面加代
'''

# 1. 为形状和颜色创建接口。
class Shape():
    def draw(self):
        pass


class Color():
    def fill(self):
        pass


# 2. 创建Shape实体类
class Rectangle(Shape):
    def draw(self):
        print("it is Rectangle")


class Square(Shape):
    def draw(self):
        print("it is Square")


class Circle(Shape):
    def draw(self):
        print("it is Circle")


# 3. 创建Color实体类
class Bule(Color):
    def fill(self):
        print("it is Bule")


class Black(Color):
    def fill(self):
        print("it is Black")


class Red(Color):
    def fill(self):
        print("it is Red")


# 4. 创建抽象类
class AbstractFactory():
    def getColor(self, color):
        pass

    def getShape(self, shape):
        pass


# 5. 创建扩展了 AbstractFactory 的工厂类，基于给定的信息生成实体类的对象。
class ShapeFactory(AbstractFactory):
    def getColor(self, color):
        pass

    def getShape(self, shape):
        if shape == 'Circle':
            return Circle()
        elif shape == 'Square':
            return Square()
        elif shape == 'Rectangle':
            return Rectangle()
        else:
            return None


class ColorFactory(AbstractFactory):
    def getColor(self, color):
        if color == 'Bule':
            return Bule()
        elif color == 'Red':
            return Red()
        elif color == 'Black':
            return Black()
        else:
            return None

    def getShape(self, shape):
        pass


# 6. 创建一个工厂创造器/生成器类，通过传递形状或颜色信息来获取工厂。
class FactoryProducer():
    def getFactory(self, color):
        if color == 'Shape':
            return ShapeFactory()
        elif color == 'Color':
            return ColorFactory()

        return None


if __name__ == '__main__':
    shapeFactory = FactoryProducer().getFactory('Shape')

    shape1 = shapeFactory.getShape("Circle")

    shape1.draw()

    colorFactory = FactoryProducer().getFactory('Color')

    color1 = colorFactory.getColor("Red")

    color1.fill()