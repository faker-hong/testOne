from collections import *

name_tuple = ('faker', 12, 180)
name, age, height = name_tuple  # 拆包
name, *others = name_tuple
print(name, age, height)
print(name, others)

"""
    tuple比list好的地方：
    1.性能上    immutable的tuple会作为常量在编译时，速度快
    2.线程安全
    3.可哈希作为dic的key
    4.拆包特性
"""
