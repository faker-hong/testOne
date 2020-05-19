import asyncio

async def work(id, t):
    print("wordking...")
    await asyncio.sleep(t)
    print('word {} done'.format(id))

def main():
    loop = asyncio.get_event_loop()
    coroutines = [work(i, i) for i in range(1,4)]
    try:
        loop.run_until_complete(asyncio.gather(*coroutines))
    except KeyboardInterrupt:
        loop.stop()
    finally:
        loop.close()

def main2():
    loop = asyncio.get_event_loop()
    coroutines = [work(i,i) for i in range(1,4)]
    try:
        loop.run_until_complete(asyncio.gather(*coroutines))
    except KeyboardInterrupt:
        tasks = asyncio.Task.all_tasks()
        for i in tasks:
            print('取消任务:{}'.format(i))
            print('取消状态：{}'.format(i.cancel()))
    finally:
        loop.close()


"""
    事件循环有
    call.soon 立刻执行
    call.later 延时执行
    call.at  在某时刻执行
"""
if __name__ == '__main__':
    main2()
