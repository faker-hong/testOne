import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/09_Time_Series/Apple_Stock/appl_1980_2014.csv'
apple = pd.read_csv(url)

# 1.将Date设为index
apple.set_index('Date')

# 2.查看日期是否重复
apple.index.is_unique   # 返回true为无重复

# 3.按时间序列降序显示
apple = apple.sort_index(ascending=True)

# 4.业务月末频率
'''
    resample()按某种规则采样，其他数据会sum起来，所以这里用mean()
'''
apple_month = apple.resample('BM').mean()

# 5.数据中时间序列的跨度
# apple = apple.sort_index(ascending=True)
# apple['Date'][0] - apple['Date'][-1]

(apple.idxmax() - apple.idxmin()).days

# 6.数据中总共有多少月份
apple_month = apple.resample('BM').mean()

len(apple_month.shape[0])

# 7.根据Adj Close画图， 画布大小为13.5*9
apple_open = apple['Adj Close'].plot(title='Apple Stock')

# 获取画布对象
fig = apple_open.get_figure()
fig.set_size_inches(13.5, 9)