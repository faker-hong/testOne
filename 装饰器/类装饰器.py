# 类装饰器会自动调用call函数
class test():
    def __init__(self, func):
        print("验证")
        self.func = func

    def run(self):
        print("奔跑")

    def __call__(self, *args, **kwargs):
        print("-----call------")
        self.func()


@test
def login():
    print("开始登陆")


login()