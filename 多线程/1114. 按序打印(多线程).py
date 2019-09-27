from threading import Thread
import threading
# Semaphore  信号量, 初始化值为1，表示最多允许一个线程连接
# 调用acquire(),信号值为-1
# 调用release(),信号值会+1
# 小于0将会堵塞，0表示等待


def One():
    print('one', end='')


def Two():
    print('two', end='')


def Three():
    print('three', end='')


class Foo(object):
    def __init__(self):
        self.t1 = threading.Semaphore(1)
        self.t2 = threading.Semaphore(0)
        self.t3 = threading.Semaphore(0)

    def first(self, One):
        """
        :type printFirst: method
        :rtype: void
        """
        self.t1.acquire()
        # printFirst() outputs "first". Do not change or remove this line.
        One()
        self.t2.release()

    def second(self, Two):
        """
        :type printSecond: method
        :rtype: void
        """
        self.t2.acquire()
        # printSecond() outputs "second". Do not change or remove this line.
        Two()
        self.t3.release()

    def third(self, Three):
        """
        :type printThird: method
        :rtype: void
        """
        self.t3.acquire()
        # printThird() outputs "third". Do not change or remove this line.
        Three()


if __name__ == '__main__':
    foo = Foo()
    callablelist = [foo.first, foo.second, foo.third]
    callablelistargs = [One, Two, Three]
    order = [2, 1, 3]
    A = Thread(target=callablelist[order[0]-1], args=(callablelistargs[order[0]-1],))
    B = Thread(target=callablelist[order[1]-1], args=(callablelistargs[order[1]-1],))
    C = Thread(target=callablelist[order[2]-1], args=(callablelistargs[order[2]-1],))
    A.start()
    B.start()
    C.start()