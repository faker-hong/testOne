import threading


def printFoo():
    print('Foo', end='')


def printBar():
    print('Bar', end='')


class FooBar(object):
    def __init__(self, n):
        self.n = n
        self.lock1 = threading.Semaphore(1)
        self.lock2 = threading.Semaphore(0)

    def foo(self, printFoo):
        """
        :type printFoo: method
        :rtype: void
        """
        for i in range(self.n):
            self.lock1.acquire()
            printFoo()
            self.lock2.release()

    def bar(self, printBar):
        """
        :type printBar: method
        :rtype: void
        """
        for i in range(self.n):
            self.lock2.acquire()
            printBar()
            self.lock1.release()


if __name__ == '__main__':
    f = FooBar(5)
    thread_1 = threading.Thread(target=f.foo, args=(printFoo,))
    thread_2 = threading.Thread(target=f.bar, args=(printBar,))
    thread_1.start()
    thread_2.start()