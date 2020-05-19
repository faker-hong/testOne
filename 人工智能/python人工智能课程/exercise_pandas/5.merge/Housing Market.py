import pandas as pd
import numpy as np

# 随机数第一位到high，size个
s1 = pd.Series(np.random.randint(1, high=5, size=100, dtype='l'))
s2 = pd.Series(np.random.randint(1, high=4, size=100, dtype='l'))
s3 = pd.Series(np.random.randint(10000, high=30001, size=100, dtype='l'))

# 1.合并这三个Series
df = pd.concat([s1, s2, s3], axis=1)
# print(df)

# 2.把列名改为bedrs, bathrs, price_sqr_meter
df.columns = ['beds', 'bathrs', 'price_sql_meter']
# print(df)

# 3.合并这三个series为一个列，并复制给变量bigcolumn
df = pd.concat([s1, s2, s3], axis=0)
bigcolumn = df.to_frame()
# print(bigcolumn)

# 4.更改index，使它为0-299
# 两种方法都可以
bigcolumn.index = [i for i in range(300)]
bigcolumn.reset_index(drop=True, inplace=True)
print(bigcolumn)