import threading


def printNumber(x):
    print(x, end='')


class ZeroEvenOdd(object):
    def __init__(self, n):
        self.n = n
        self.lock_0 = threading.Semaphore(1)
        self.lock_even = threading.Semaphore(0)
        self.lock_odd = threading.Semaphore(0)

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(1, self.n+1):
            self.lock_0.acquire()
            printNumber(0)
            if i % 2 == 0:
                self.lock_even.release()
            else:
                self.lock_odd.release()

    def even(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(2, self.n+1, 2):
            self.lock_even.acquire()
            printNumber(i)
            self.lock_0.release()

    def odd(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(1, self.n+1, 2):
            self.lock_odd.acquire()
            printNumber(i)
            self.lock_0.release()


if __name__ == '__main__':
    foo = ZeroEvenOdd(5)
    A = threading.Thread(target=foo.zero, args=(printNumber, ))
    B = threading.Thread(target=foo.even, args=(printNumber, ))
    C = threading.Thread(target=foo.odd, args=(printNumber, ))
    A.start()
    B.start()
    C.start()