from datetime import datetime

import numpy as np
import pandas as pd

# parse_dates获取0、1、2列并将它们解析为索引
# data_url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/Wind_Stats/wind.data'
# data = pd.read_csv(data_url, sep="\s+", parse_dates=[[0, 1, 2]])
# data.to_csv("./wind.csv")

data = pd.read_csv('./wind.csv')

# 1.修改日期
# def fix_data(x):
#     year = int(x[:4]) - 100 if int(x[:4]) > 1989 else int(x[:4])
#     return str(year) + x[4:]


# data['Yr_Mo_Dy'] = data['Yr_Mo_Dy'].apply(fix_data)
# print(data.head())

# 2.把Yr_Mo_Dy列设为index
data['Yr_Mo_Dy'] = pd.to_datetime(data['Yr_Mo_Dy'])
data.index = data['Yr_Mo_Dy']
# print(data)

# 3.计算所有数据中缺失值的数量
# NaN_num = data.isnull().sum().sum()
# print(NaN_num)

# 4.非空值的数量
# not_missing = data.notnull().sum()
# print(not_missing)

# 5.计算所有地点和时间的平均风速
# print(data.fillna(0).values[:, 2:].mean())

# 6.新建loc_stats的DF对象，包括所有时间和地区的风速min，max， mean
# loc_stats = pd.DataFrame()
# loc_stats['min'] = data.min(axis=1)
# loc_stats['max'] = data.max(axis=1)
# loc_stats['mean'] = data.mean(axis=1)
# loc_stats['std'] = data.std(axis=1)
# print(loc_stats)

# 7.可视化.每个地区一月份的平均风速
result = data.loc[data.index.month == 1].mean()
# print(result)

# 8.以年为单位降低取样
# to_period('A') 把时间戳转为年时期
# result = data.groupby(data.index.to_period('A')).mean()
# print(result)

# 9.以月为单位降低取样
# result = data.groupby(data.index.to_period('M')).mean()
# print(result)

# 10.以星期为单位降低取样
# result = data.groupby(data.index.to_period('W')).mean()
# print(result)

# 11.以星期为单位降低采样，求每个地区的最大最小平均风速,取前52周
result = data.resample('W').agg(['min', 'max', 'mean'])
result = result.loc[result.index[1:53]]
# print(result)