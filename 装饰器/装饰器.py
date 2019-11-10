# def function_out(func):
#
#     def function_in():
#         print("验证")
#         func()
#     return function_in
#
# 调用login()函数等价于  login() == function_out(login)
# @function_out
# def login():
#     print("登陆----")
#
#
# login()

###############################################
# 带参数的装饰器
# def function_out(func):
#
#     def function_in(num):
#         print("验证")
#         func(num)
#     return function_in
#
#
# @function_out
# def login(num):
#     print("登陆-----num=", num)
#
#
# login(15)

#####################################################
# 可变参数的装饰器
# def function_out(func):
#     def function_in(*args, **kwargs):
#         print("验证")
#         func(*args, **kwargs)
#     return function_in
#
#
# @function_out
# def login(*args, **kwargs):
#     print("登陆")
#     print("args=", args)
#     print("kwargs", kwargs)
#
#
# login(12, 13, 14, a=1, b=2, c=3)

######################################################
# 装饰有返回值的函数
def function_out(func):
    def function_in(*args, **kwargs):
        print("验证")
        return func(*args, **kwargs)
    return function_in


@function_out
def login(*args, **kwargs):
    print("登陆")
    print("args=", args)
    print("kwargs", kwargs)
    return 1


re = login(12, 13, 14, a=1, b=2, c=3)
print("---------", re)