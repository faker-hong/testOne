import threading


def printFizz():
    print('Fizz', end=', ')


def printBuzz():
    print('Buzz', end=', ')


def printFizzBuzz():
    print('FizzBuzz', end=', ')


def printNumber(i):
    print(i, end=', ')


class FizzBuzz(object):
    def __init__(self, n):
        self.n = n
        self.d = {}

    # printFizz() outputs "fizz"
    def fizz(self, printFizz):
        """
        :type printFizz: method
        :rtype: void
        """
        self.d['f'] = printFizz
        self.res()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz):
        """
        :type printBuzz: method
        :rtype: void
        """
        self.d['b'] = printBuzz
        self.res()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz):
        """
        :type printFizzBuzz: method
        :rtype: void
        """
        self.d['fb'] = printFizzBuzz
        self.res()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        self.d['n'] = printNumber
        self.res()

    def res(self):
        if len(self.d) == 4:
            for i in range(1, self.n + 1):
                if i % 15 == 0:
                    self.d['fb']()
                elif i % 3 == 0:
                    self.d['f']()
                elif i % 5 == 0:
                    self.d['b']()
                else:
                    self.d['n'](i)


if __name__ == '__main__':
    s = FizzBuzz(16)
    thread_1 = threading.Thread(target=s.number, args=(printNumber,))
    thread_2 = threading.Thread(target=s.fizzbuzz, args=(printFizzBuzz,))
    thread_3 = threading.Thread(target=s.fizz, args=(printFizz,))
    thread_4 = threading.Thread(target=s.buzz, args=(printBuzz,))
    thread_1.start()
    thread_2.start()
    thread_3.start()
    thread_4.start()
