from collections import Counter

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
# data = pd.read_csv(url, sep='\t')
# data.to_csv("./chipotle.csv")
data = pd.read_csv('./chipotle.csv')

'''
# 柱状图
# 获取item_name列的数据
x = data.item_name

# 使用Counter类计数
letter_count = Counter(x)

# 把letter_count转为DataFrame
df = pd.DataFrame.from_dict(letter_count, orient='index')  # orient 数据的方向
# print(df)

# 取前五名数据
df = df[0].sort_values(ascending=False)[:5]
# print(df)

df.plot(kind='bar')

plt.xlabel('item_name')
plt.ylabel('price')
plt.title('-------')

plt.show()
'''

# 散点图
# 把item_price字段中的$符号和末尾空格去除转化为float类型
data.item_price = [float(x[1:-1]) for x in data.item_price]

# 计算相同订单的订购商品数量
orders = data.groupby('order_id').sum()

# 画图
plt.scatter(orders.item_price, orders.quantity, s=50, c='green')

plt.xlabel('item_price')
plt.ylabel('quantity')
plt.title('Number of items ordered per order price')
plt.show()