import asyncio


l = []
lock = asyncio.Lock()

async def work(name):
    print("77777777777777777")
    # 这里加个锁，第一次调用该协程，运行到这个语句块，上锁
    # 当语句块结束后解锁，开锁前该语句块不可被运行第二次
    # 如果上锁后有其它任务调用了这个协程函数，运行到这步会被阻塞，直至解锁
    # with 是普通上下文管理器关键字，async with 是异步上下文管理器关键字
    # 能够使用 with 关键字的对象须有 __enter__ 和 __exit__ 方法
    # 能够使用 async with 关键字的对象须有 __aenter__ 和 __aexit__ 方法
    # async with 会自动运行 lock 的 __aenter__ 方法，该方法会调用 acquire 方法上锁
    # 在语句块结束时自动运行 __aexit__ 方法，该方法会调用 release 方法解锁
    # 这和 with 一样，都是简化 try ... finally 语句
    async with lock:
        print('{} start'.format(name))
        if 'x' in l:
            return name
        await asyncio.sleep(0)
        print('---------------------')
        l.append('x')
        print('{} end'.format(name))
        return name

async def one():
    name = await work('one')
    print('{} ok'.format(name))

async def two():
    name = await work('two')
    print('{} ok'.format(name))

def main():
    loop = asyncio.get_event_loop()
    tasks = asyncio.wait([one(), two()])
    loop.run_until_complete(tasks)

if __name__ == '__main__':
    main()

"""
    运行流程大概是:
    1.work('one')
    2.asyncio.sleep()切换了协程
    3.执行work('two') 但代码块被锁，只能带到代码块执行完
    4.work('one')执行玩后执行work('two')
"""