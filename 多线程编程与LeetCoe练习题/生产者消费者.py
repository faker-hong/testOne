import threading
import time

con = threading.Condition()

num = 0

# 生产者
class Producer(threading.Thread):

    def __init__(self):
        super(Producer, self).__init__()

    def run(self):
        # 锁定线程
        global num
        con.acquire()
        while True:
            print("开始添加！！！")
            num += 1
            print(f"火锅里面鱼丸个数：{num}")
            time.sleep(1)
            if num >= 5:
                print("火锅里面里面鱼丸数量已经到达5个，无法添加了！")
                # 唤醒等待的线程
                # 唤醒等到这个对象的线程
                con.notify()
                # 等待通知
                # 会释放当前的锁，然后让出CPU，进入等待状态。
                # 调用某个对象的wait()方法能让当前线程堵塞
                con.wait()
        # 释放锁
        con.release()
        print(7777777777)

# 消费者
class Consumers(threading.Thread):
    def __init__(self):
        super(Consumers, self).__init__()

    def run(self):
        con.acquire()
        global num
        while True:
            print("开始吃啦！！！")
            num -= 1
            print(f"火锅里面剩余鱼丸数量：{num}")
            time.sleep(2)
            if num <= 0:
                print("锅底没货了，赶紧加鱼丸吧！")
                con.notify()  # 唤醒其它线程
                # 等待通知
                con.wait()
        con.release()
        print(666666666)

p = Producer()
c = Consumers()
p.start()
c.start()