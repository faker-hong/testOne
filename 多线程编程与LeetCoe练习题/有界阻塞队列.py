import threading
from concurrent.futures import ThreadPoolExecutor
import time

'''
    Semaphore信号量，小于堵塞，等于0等待
'''


# 有界阻塞队列
class BoundedBlockingQueue(object):
    def __init__(self, capacity):
        self.queue = []
        self.capacity = capacity
        self.producer = threading.Semaphore(capacity)
        self.consumer = threading.Semaphore(0)

    # 添加元素到队列的前面，如果队列满了使线程阻塞，直到队列不为空
    def enqueue(self, element):
        self.producer.acquire()
        self.queue.append(element)
        self.consumer.release()

    # 删除一个队尾元素并返回这个元素，如果队列为空，阻塞队列直到队列不为空
    def dequeue(self):
        self.consumer.acquire()
        element = self.queue.pop(0)
        print(element)
        self.producer.release()
        return element

    # 返回队列中元素个数
    def size(self):
        print(len(self.queue))
        return len(self.queue)


if __name__ == '__main__':
    Queue = BoundedBlockingQueue(3)
    # 生产者线程与消费者线程
    put = [1, 0, 2, 3]
    producer_pool = ThreadPoolExecutor(3)
    consumer_pool = ThreadPoolExecutor(4)

    for i in put:
        producer_pool.submit(Queue.enqueue, i)

    for i in range(3):
        consumer_pool.submit(Queue.dequeue)

    # size_thread = threading.Thread(target=Queue.size)
    # size_thread.setDaemon(True)
    # size_thread.start()
    time.sleep(5)
    Queue.size()