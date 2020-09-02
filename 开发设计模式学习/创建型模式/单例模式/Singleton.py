'''
    目的： 确保一个类只有一个实例存在

    优点：
    1、在内存里只有一个实例，减少了内存的开销，尤其是频繁的创建和销毁实例（比如管理学院首页页面缓存）。
    2、避免对资源的多重占用（比如写文件操作）。

    缺点：没有接口，不能继承，与单一职责原则冲突，一个类应该只关心内部逻辑，而不关心外面怎么样来实例化。
'''


class Singleton():
    def __init__(self):
        pass

    # __new__() 是一种负责创建类实例的静态方法，它无需使用 staticmethod 装饰器修饰，且该方法会优先 __init__() 初始化方法被调用。
    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, '_instance'):
            Singleton._instance = object.__new__(cls)
        return Singleton._instance


if __name__ == '__main__':
    s1 = Singleton()
    s2 = Singleton()
    print(s1, s2)