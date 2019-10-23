from collections import namedtuple

"""
    函数参数， 前者类似user_tuple,后者指明参数名，如user_dict
    def ask(*args, **kwargs)
"""


User = namedtuple('User', ["name", "age", "height", "edu"])
# user = User(name="faker", age=12, height=188)
user_tuple = ('faker', 12, 188)
user_dict = {
    "name": "faker",
    "age": 12,
    "height": 188,
    "edu": "master"
}
# user = User(*user_tuple, "master")

user = User(**user_dict)
print(user)

"""
    namedtuple中的make() 和 asdict() 方法
    user = User._make(user_tuple)   不需要*，函数内会处理，但必须长度相等,传进来可迭代的对象就可以
    user_info_dict = user._asdict()  user中的属性转换为dict
"""