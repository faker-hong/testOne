import time
import asyncio
import functools


def one():
    start = time.time()

    @asyncio.coroutine       # 使用协程装饰器创建协程函数
    def do_some_work():       # 携程函数
        print("start coroutines")
        time.sleep(0.1)
        print("this is a coroutines")

    loop = asyncio.get_event_loop()      # 创建事件循环
    coroutines = do_some_work()          # 携程对象
    loop.run_until_complete(coroutines)  # 将协程对象注入事件循环

    end = time.time()
    print("耗时：{:.4f}".format(end-start))

def two():
    start = time.time()

    @asyncio.coroutine
    def do_some_work():
        print("start coroutines")
        time.sleep(0.1)
        print("this is a coroutines")

    loop = asyncio.get_event_loop()
    coroutines = do_some_work()
    task = loop.create_task(coroutines)         # 创建任务
    print('task 是不是 asyncio.Task 的实例？', isinstance(task, asyncio.Task))
    print('Task state:', task._state)
    loop.run_until_complete(task)
    print('Task state:', task._state)

    end = time.time()
    print('运行耗时：{:.4f}'.format(end - start))


######  绑定回调

def three():
    start = time.time()

    async  def corowork():
        print('[corowork] Start coroutine')
        time.sleep(0.1)
        print('[corowork] This is a coroutine')

    def callback(name,task):
        print('[callback] Hello {}'.format(name))
        print('[callback] coroutine state: {}'.format(task._state))

    loop = asyncio.get_event_loop()
    coroutine = corowork()
    task = loop.create_task(coroutine)
    task.add_done_callback(functools.partial(callback, 'shiyanlou'))
    loop.run_until_complete(task)

    end = time.time()
    print('运行耗时：{:.4f}'.format(end - start))


# 多任务
def four():
    start = time.time()

    async def corowork(name, t):
        print('[corowork] Start coroutine', name)
        await asyncio.sleep(t)  # 1
        print('[corowork] Stop coroutine', name)
        return 'Coroutine {} OK'.format(name)

    loop = asyncio.get_event_loop()
    coroutine1 = corowork('one', 3)
    coroutine2 = corowork('two', 1)
    task1 = loop.create_task(coroutine1)
    task2 = loop.create_task(coroutine2)
    gather = asyncio.gather(task1, task2)   # 将任务对象作为参数，asyncio.gather 方法创建任务收集器。注意，asyncio.gather 方法中参数的顺序决定了协程的运行顺序
    loop.run_until_complete(gather)
    print('[task1] ', task1.result())
    print('[task2] ', task2.result())
    end = time.time()
    print('运行耗时：{:.4f}'.format(end - start))

four()