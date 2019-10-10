import threading
import time


def display():
    print("放了你们")


# 设置了一个线程数量障碍，当等待的线程到达了这个数量就会唤醒所有的等待线程。
barrier = threading.Barrier(3, display)


class Chick(threading.Thread):
    def run(self):
        while True:
            print(self.getName(), ": 你抓不到我")
            time.sleep(1)
            print(self.getName(), ": 好吧，你抓到我了")
            try:
                barrier.wait()
            except threading.BrokenBarrierError:
                print("BrokenBarrierError")


if __name__ == "__main__":
    c1 = Chick(name="A")
    c2 = Chick(name="B")
    c3 = Chick(name="C")
    c1.start()
    c2.start()
    c3.start()
    time.sleep(2)
    # barrier.reset()
    print("main")