import threading
import time
import queue


exitflag = 0


class MyThread(threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q

    def run(self):
        print('starting： ' + self.name)
        process(self.name, self.q)
        print('exit： ' + self.name)


def process(threadName, q):
    while not exitflag:
        queueLock.acquire()
        print(threadName + ' 获得锁')
        if not wordQueue.empty():
            data = q.get()
            print('获得队列 ' + data)
            queueLock.release()
            print(threadName + ' 释放锁')
            print('%s process %s' % (threadName, data))
        else:
            queueLock.release()
        time.sleep(2)


queueLock = threading.Lock()
threads = []
threadList = ['thread-1', 'thread-2', 'thread-3']
nameList = ['one', 'two', 'three', 'four', 'five']
wordQueue = queue.Queue(10)
threadID = 1

# 创建新线程,并把线程放入threads集合中
for th in threadList:
    thread = MyThread(threadID, th, wordQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

# 填充队列
queueLock.acquire()
for word in nameList:
    wordQueue.put(word)
    print('写入队列', word)
queueLock.release()

# 等待队列清空
while not wordQueue.empty():
    pass

# 通知线程退出
exitflag = 1

# 等待所有线程完成
for t in threads:
    t.join()
print('退出主线程')
