import threading
import time


# 线程安全队列异常类
class ThreadSafeQueueException(Exception):
    pass


# 线程安全队列
class ThreadSafeQueue:

    def __init__(self, max_size=0):
        self.max_size = max_size
        self.queue = []
        self.lock = threading.Lock()
        self.condition = threading.Condition()

    # 获取队列中元素的数量
    def size(self):
        self.lock.acquire()
        size = len(self.queue)
        self.lock.release()
        return size

    # 往队列中添加一个元素
    def put(self, item):
        # 如果队列大小不为0，或者队列中的元素大于max_size
        if self.max_size != 0 and self.size() > self.max_size:
            return ThreadSafeQueueException()
        self.lock.acquire()
        self.queue.append(item)
        self.lock.release()
        # 通知其他可能处在等待状态的线程
        self.condition.acquire()
        self.condition.notify()
        self.condition.release()

    # 往队列中批量添加元素
    def batch_put(self, item_list):
        # 判断item_list是否为一个列表
        if not isinstance(item_list, list):
            item_list = list(item_list)

        for item in item_list:
            self.put(item)

    # 从队列中取出元素
    def pop(self, block=False, timeout=0):
        if self.size() == 0:
            # 需要堵塞
            if block:
                self.condition.acquire()
                self.condition.wait(timeout=timeout)
                self.condition.release()
            else:
                return None

        # 如果timeout过后，队列中还是没有元素，直接返回None
        self.lock.acquire()
        item = None
        if len(self.queue) > 0:
            item = self.queue.pop()
        self.lock.release()
        return item

    # 获取元素
    def get(self, index):
        # if self.size() == 0:
        #     return None

        self.lock.acquire()
        item = self.queue[index]
        self.lock.release()
        return item


if __name__ == '__main__':
    queue = ThreadSafeQueue(100)
    def producer():
        while True:
            queue.put(1)
            time.sleep(1)
    def consumer():
        while True:
            item = queue.pop(block=True, timeout=1)
            print(item)
            time.sleep(1)
    thread1 = threading.Thread(target=producer)
    thread2 = threading.Thread(target=consumer)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()