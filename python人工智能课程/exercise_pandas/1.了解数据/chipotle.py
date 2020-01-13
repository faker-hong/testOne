import pandas as pd
import numpy as np

# 数据集地址
# url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
# data = pd.read_csv(url, sep='\t')
# data.to_csv("./chipotle.csv")

data = pd.read_csv("./chipotle.csv")

# 1.查看数据集的大小
data_number = data.shape[0]
# print(data_number)

# 2.数据集的特征数
data_columns = data.shape[1]
# print(data_columns)

# 3.打印所有列名
columns_all = data.columns
# print(columns_all)

# 4.订购最多的商品
ordered_most = data.groupby("item_name").sum()
goods_name = ordered_most.sort_values("quantity", ascending=False)
# print(goods_name.head(1))

# 5.有多少商品是被订购了的
ordered_goods = data.groupby("item_name").sum()
ordered_goods = ordered_goods[ordered_goods["quantity"] > 0]
# print(ordered_goods.shape[0])

# 6.在 choice_description中被订购最多的商品
most_in_cd = data.groupby("choice_description").sum()
most_in_cd = most_in_cd.sort_values("quantity", ascending=False)
# print(most_in_cd.head(1))

# 7.总共订购多少商品
total_goods = data["quantity"].sum()
# print(total_goods)

# 8.把item_price列的类型改为float
'''
Pandas中进行数据类型转换有三种基本方法：
    1.使用astype()函数进行强制类型转换
        数据中有缺失值或者特殊字符会失效
    2.自定义函数进行数据类型转换
    3.使用Pandas提供的函数如to_numeric()、to_datetime()
'''
# 所以这里使用自定义函数的方式解决,第一位是$,最后以为是空格，所有取x[1:-1]
change_func = lambda x: float(x[1:-1])
data['item_price'] = data['item_price'].apply(change_func)
# print(data.info())

# 数据集中的总收入, 商品价格*商品售出数量=总收入
income = (data['quantity'] * data['item_price']).sum()
# print(income)

# 这期间下了多少订单
# value_count()查看有多少个不同值，并计算重复值的个数
orders = data.order_id.value_counts().count()
# print(orders)

# 每笔订单的平均收入
avg_incom = np.around(income / orders, 2)
# print(avg_incom)

# 被售出的商品种类个数
goods_classes = data.item_name.value_counts().count()
print(goods_classes)