import pandas as pd

# 日期字符串转换为日期格式
# ser = pd.Series(['01 Jan 2010',
#                 '02-02-2011',
#                  '20120303',
#                  '2013/04/04',
#                  '2014-05-05',
#                  '2015-06-06T12:20'])
# s1 = pd.to_datetime(ser)
# print(s1)


# 从时间序列提取年/月/日/时/分/秒
# print(s1.dt.year)
# print(s1.dt.month)
# print(s1.dt.day)
# print(s1.dt.hour)


# 从series中找出包含两个以上元音字母的单词
# ser = pd.Series(['Apple', 'Orange', 'Plan', 'Python', 'Money'])
# def count(x):
#     yuan = 'aeiou'
#     c = 0
#     for i in x:
#         if i in yuan:
#             c += 1
#     return c
# counts = ser.map(lambda x:count(x))
# re = ser[counts>=2]
# print(re)


# 如何过滤series中的有效电子邮件
# emails = pd.Series(['buying books at amazom.com',
#                     'rameses@egypt.com',
#                     'matt@t.co',
#                     'narendra@modi.com'])
# import re
# pattern = '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,4}'
# valid = emails.str.findall(pattern, flags=re.IGNORECASE)
# res = [x[0] for x in valid if len(x) > 0]
# print(res)


# series A 以series B为分组依据, 然后计算分组后的平均值
# mean()函数为取均值，linespace(),为在范围内取多少个等分的值
# import numpy as np
# fruit = pd.Series(np.random.choice(['apple', 'banana', 'carrot'], 10))
# weights = pd.Series(np.linspace(1, 10, 10))
#
# re = weights.groupby(fruit).mean()
# print(re)


# 读取csv时, 间隔几行读取数据
# import numpy as np
# fpath = 'test.csv'
# df = pd.DataFrame({'a': range(100), 'b': np.random.choice(['apple', 'banana', 'carrot'], 100)})
# df.to_csv(fpath, index=None)
#
# import csv
# with open(fpath, 'r') as f:
#     reader = csv.reader(f)
#     out = []
#     for i,row in enumerate(reader):
#         if i % 20 == 0:
#             out.append(row)
# df = pd.DataFrame(out[1:], columns=out[0])
# print(df)
# print(df.loc[df.a == np.max(df.a)])  从dataframe中找到a列最大值对应的行


# print(df.iat[1, 1])  根据行列取数据
# print(df.at[index, col]  在dataframe中根据index和列名称读取某个值