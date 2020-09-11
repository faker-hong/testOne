from 线程实践 import task
from 线程实践 import pool
import time


class SimpleTask(task.Task):
    def __init__(self, callable):
        super(SimpleTask, self).__init__(callable)


def process():
    time.sleep(1)
    print("this is a SimpleTask callable function")
    time.sleep(1)


def test():
    # 1.初始化一个线程池
    test_pool = pool.ThreadPool()
    test_pool.start()

    # 2.生成一系列的任务
    for i in range(10):
        simple_task = SimpleTask(process)
        test_pool.put(simple_task)

    # 3.往线程池提交任务执行


def test_async_task():

    def async_process():
        num = 1
        for i in range(100):
            num += 1
        return num

    # 1.初始化一个线程池
    test_pool = pool.ThreadPool()
    test_pool.start()

    # 2.生成一系列的任务
    for i in range(10):
        async_task = task.AsyncTask(func=async_process)
        test_pool.put(async_task)
        result = async_task.get_result()
        print(result)


# 测试是否可以真正等待
def test_async_task2():

    def async_process():
        num = 1
        for i in range(100):
            num += 1
        time.sleep(1)
        return num

    # 1.初始化一个线程池
    test_pool = pool.ThreadPool()
    test_pool.start()

    # 2.生成一系列的任务
    for i in range(10):
        async_task = task.AsyncTask(func=async_process)
        test_pool.put(async_task)
        print("get result in timestamp: %d" % time.time())
        result = async_task.get_result()
        print("get result in timestamp: %d %d" % (result, time.time()))


# 测试没有等待是否也可以正常获取结果
def test_async_task3():

    def async_process():
        num = 1
        for i in range(100):
            num += 1
        return num

    # 1.初始化一个线程池
    test_pool = pool.ThreadPool()
    test_pool.start()

    # 2.生成一系列的任务
    for i in range(10):
        async_task = task.AsyncTask(func=async_process)
        test_pool.put(async_task)
        print("get result in timestamp: %d" % time.time())
        time.sleep(5)
        result = async_task.get_result()
        print("get result in timestamp: %d %d" % (result, time.time()))


if __name__ == '__main__':
    test()
    # test_async_task()
    # test_async_task2()
    # test_async_task3()