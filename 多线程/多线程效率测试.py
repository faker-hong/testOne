import requests
from bs4 import BeautifulSoup
import time
import numpy as np
from threading import Thread


# CPU密集型任务
def cal(a = None):
    s = 0
    for i in range(50000):
        s += i


# IO密集型任务
def file(a = None):
    with open('try.txt', 'w') as f:
        for i in range(50000):
            f.write('123abc\n')


# 抓取豆瓣top250的10个页面
def gettitle(a):
    url = 'https://movie.douban.com/top250?start={}&filter='.format(a*25)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    lis = soup.find('ol', class_='grid_view').find_all('li')
    for li in lis:
        title = li.find('span', class_='title').text


# 分别将上面三个函数传入， 计算10次， 返回不使用多线程的时间
def no_thread(func):
    t = time.time()
    for i in range(10):
        func(i)
    duration = time.time()-t
    return duration


# 分别将上面三个函数传入， 计算10次， 返回不使用多线程的时间
def use_thread(func):
    t = time.time()
    ths = []
    for i in range(10):
        th = Thread(target=func, args=(i,))
        th.start()
        ths.append(th)
    for th in ths:
        th.join()
    duration = time.time() - t
    return duration


# 每一项做五次实验， 返回每次时间和五次平均时间
def get_duration(func_th, func):
    l = []
    for i in range(5):
        l.append(func_th(func))
    mean_duration = '%.2f' % np.mean(l)
    all_duration = ['%.2f' % i for i in l]
    return mean_duration, all_duration


# CPU密集任务对比
no_thread_cal = get_duration(no_thread, cal)
use_thread_cal = get_duration(use_thread, cal)
print(no_thread_cal)
print(use_thread_cal)

# IO密集任务对比
no_thread_IO = get_duration(no_thread, file)
use_thread_IO = get_duration(use_thread, file)
print(no_thread_IO)
print(use_thread_IO)


# 网络请求任务对比
no_thread_net = get_duration(no_thread, gettitle)
use_thread_net = get_duration(use_thread, gettitle)
print(no_thread_net)
print(use_thread_net )