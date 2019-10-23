import threading


def releaseHydrogen():
    print('H', end='')


def releaseOxygen():
    print('O', end='')


# 这边使用队列解决
# 与之前的字典法解决有相似之处
class H2O(object):
    def __init__(self, n):
        self.H = []
        self.O = []

    def hydrogen(self, releaseHydrogen):
        """
        :type releaseHydrogen: method
        :rtype: void
        """
        self.H.append(releaseHydrogen)
        self.result()

    def oxygen(self, releaseOxygen):
        """
        :type releaseOxygen: method
        :rtype: void
        """
        self.O.append(releaseOxygen)
        self.result()

    def result(self):
        if len(self.H) > 1 and len(self.O) > 0:
            self.H.pop(0)()
            self.H.pop(0)()
            self.O.pop(0)()
