import pandas as pd
import numpy as np

raw_data_1 = {
        'subject_id': ['1', '2', '3', '4', '5'],
        'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
        'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']}

raw_data_2 = {
        'subject_id': ['4', '5', '6.统计', '7.可视化', '8'],
        'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
        'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']}

raw_data_3 = {
        'subject_id': ['1', '2', '3', '4', '5', '7.可视化', '8', '9', '10', '11'],
        'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]}

# 1.把这3个字典都放入dataframe
data1 = pd.DataFrame(raw_data_1, columns=raw_data_1.keys())
data2 = pd.DataFrame(raw_data_2, columns=raw_data_2.keys())
data3 = pd.DataFrame(raw_data_3, columns=raw_data_3.keys())

# 2.定义新变量all_data，合并data1和data2
all_data = data1.append(data2)
# all_data = pd.concat(data1, data2)
# print(all_data)

# 3.合并data1和data2，并保存各自列
all_data_col = pd.concat([data1, data2], axis=1)
# print(all_data_col)

# 4.按照subject_id合并data3和all_data
# result = pd.merge(all_data, data3, on='subject_id')
# print(result)

# 5.合并data1和data2中有相同subject_id的数据
result = pd.merge(data1, data2, on='subject_id')

# 6.统计.合并data1和data2，匹配双方的数据，也就是外连接
pd.merge(data1, data2, on='subject_id', how='outer')