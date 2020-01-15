import numpy as np
import pandas as pd

# url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data'
# wine = pd.read_csv(url)
# wine.to_csv("./wine.csv")

wine = pd.read_csv("./wine.csv")
wine = wine.iloc[:, 1:]

# 1.删除1，4，7，9，13，14列
wine = wine.drop(wine.columns[[0, 3, 6, 8, 11, 12, 13]], axis=1)
# print(wine.shape)

# 2.修改列名
wine.columns = ['alcohol', 'malic_acid', 'alcalinity_of_ash', 'magnesium', 'flavanoids', 'proanthocyanins', 'hue']
# print(wine)

# 3.修改前三行的alcohol列值为NaN
wine.loc[:3, 'alcohol'] = np.NaN
# print(wine)

# 4.修改3.4行的magnesium列值为NaN
wine.loc[2:3, 'magnesium'] = np.NaN
# print(wine['magnesium'])

# 5.把alcohol的NaN值填补为10，magnesium的NaN值填补为100
wine['alcohol'].fillna(10, inplace=True)
wine['magnesium'].fillna(100, inplace=True)
# print(wine)

# 6.计算缺失值数量
missing_num = wine.isnull().sum()
# print(missing_num)

# 7.生成10个随机数数组，上限为10
arr = np.random.randint(10, size=10)
# print(arr)

# 8.把生成的随机数作为索引，其他为NaN
wine.alcohol[arr] = np.NaN
# print(wine)

# 9.现在有多少缺失值
missing_num = wine.isnull().sum()
# print(missing_num)

# 10.删除包含缺失值的数据
wine.dropna(inplace=True)
# print(wine)

# 11.只打印alcohol列的非空值
# result = wine.alcohol.notnull()
# print(result)
# result = wine.alcohol[result]
# print(result)

# 12.重置索引，使其从0开始
wine.reset_index(drop=True, inplace=True)
# print(wine)