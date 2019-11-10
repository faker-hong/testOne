# 先应用最下面的装饰器，然后进入内层函数是一个函数的适合再调用上面的装饰器就成了<b><i>hello-world</i></b>的效果

def block(func):
    def function_in():
        return "<b>"+func()+"</b>"
    return function_in


def italic(func):
    def function_in():
        return "<i>"+func()+"</i>"
    return function_in

@block
@italic
def test():
    return "hello-world"


print(test())