'''
代理模式

　  定义:为其他对象提供一种代理以控制对特定对象的访问

     角色:抽象实体,实体,代理

     适用场景:远程代理(为远程的对象提供代理),虚代理(根据需要创建很大的对象,即懒加载),保护代理(控制对原始对象的访问,用于具有不同访问权限的对象)

     优点:远程代理(可以隐藏对象位于远程地址空间的事实),虚代理(可对大对象的加载进行优化),保护代理(允许在访问一个对象时有一些附加的处理逻辑,例如权限控制)
'''
from abc import ABCMeta, abstractmethod


# 抽象实体
class Subject(metaclass=ABCMeta):
    @abstractmethod
    def get_content(self):
        pass


# 实体
class RealSubject(Subject):
    def __init__(self, filename):
        print("读取{}的内容".format(filename))
        f = open(filename)
        self.content = f.read()
        f.close()

    def get_content(self):
        return self.content


# 远程代理
class ProxyA(Subject):
    def __init__(self, filename):
        self.sub = RealSubject(filename)

    def get_content(self):
        return self.sub.get_content()


# 虚代理
class ProxyB(Subject):
    def __init__(self,filename):
        self.filename = filename
        self.subj = None

    def get_content(self):
        if not self.subj:
            self.subj = RealSubject(self.filename)
        return self.subj.get_content()


# 保护代理
class ProxyC(Subject):
    def __init__(self,filename):
        self.subj = RealSubject(filename)

    def get_content(self):
        return '???'