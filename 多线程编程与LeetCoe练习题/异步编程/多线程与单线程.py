import time
import threading


def every_read():
    time.sleep(0.02)


def single():
    for i in range(100):
        every_read()


def not_single():
    threading_list = []
    for i in range(100):
        t = threading.Thread(target=every_read) # target后为方法名
        t.start()
        threading_list.append(t)
    for i in threading_list:
        i.join()


if __name__ == '__main__':
    start = time.time()
    single()
    end = time.time()
    print("单线程耗时：{:.4f}".format(end-start))

    start = time.time()
    not_single()
    end = time.time()
    print("多线程耗时：{:.4f}".format(end-start))