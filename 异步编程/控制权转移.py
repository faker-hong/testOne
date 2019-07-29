import time
from faker import Faker
from functools import wraps

# 预激协程装饰器
def coroutine(func):
    @wraps(func)
    def wrapper(*args, **kw):
        g = func(*args, **kw)
        next(g)
        return g
    return wrapper

# 子生成器函数，这个生成器是真正做事的生成器
def sub_coro():
    l = []                      # 创建空列表
    while True:                 # 无限循环
        value = yield           # 调用方使用 send 方法发生数据并赋值给 value 变量
        if value == 'CLOSE':    # 如果调用方发生的数据是 CLOSE ，终止循环
            break
        l.append(value)         # 向列表添加数据
    return sorted(l)            # 返回排序后的列表

# 使用预激协程装饰器
@coroutine
# 带有 yield from 语句的父生成器函数
def dele_coro():
    # while True 可以多次循环，每次循环会创建一个新的子生成器 sub_coro()
    # 这里 while 只循环一次，这是由调用方，也就是 main 函数决定的
    # while 循环可以捕获函数本身创建的父生成器终止时触发的 StopIteration 异常
    while True:
        # yield from 会自动预激子生成器 sub_coro()
        # 所以 sub_coro 在定义时不可以使用预激协程装饰器
        # yield from 将捕获子生成器终止时触发的 StopIteration 异常
        # 并将异常的 value 属性值赋值给等号前面的变量 l
        # 也就是 l 变量的值等于 sub_coro 函数的 return 值
        # yield from 还实现了一个重要功能
        # 就是父生成器的 send 方法将发送值给子生成器
        # 并赋值给子生成器中 yield 语句等号前面的变量 value
        l = yield from sub_coro()
        print('排序后的列表：', l)
        print('------------------')

# 调用父生成器的函数，也叫调用方
def main():
    # 生成随机国家代号的方法
    fake = Faker().country_code
    # 嵌套列表，每个子列表中有三个随机国家代号(字符串)
    nest_country_list = [[fake() for i in range(3)] for j in range(3)]
    for country_list in nest_country_list:
        print('国家代号列表：', country_list)
        c = dele_coro()      # 创建父生成器
        for country in country_list:
            c.send(country)  # 父生成器的 send 方法将国家代号发送给子生成器
        # CLOSE 将终止子生成器中的 while 循环
        # 子生成器的 return 值赋值给父生成器 yield from 语句中等号前面的变量 l
        c.send('CLOSE')

if __name__ == '__main__':
    main()