import pandas as pd
import numpy as np

# url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
# iris = pd.read_csv(url)
# iris.to_csv('./iris.csv')
iris = pd.read_csv('./iris.csv')
iris = iris.iloc[:, 1:]

# 1.给数据设置列名
iris.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
# print(iris)

# 2.查看数据中的缺失值数量
isnull_num = iris.isnull().sum()
# print(isnull_num)

# 3.把10-29行数据的petal_length列的值设置为NaN
iris.loc[10:30, 'petal_length'] = np.NaN
# print(iris)

# 4.把缺失值替补为1.0
iris.fillna(1.0, inplace=True)
# print(iris)

# 5.删除鸢尾花的class列
del iris['class']

# 6.把前三行的数据设置为NaN
iris.iloc[:3, :] = np.NaN
# print(iris)

# 7.删除缺失值数据
iris.dropna(inplace=True)
# print(iris)

# 8.重置索引使其从0开始
# iris.index = [i for i in range(iris.shape[0])]
iris.reset_index(drop=True, inplace=True)
# print(iris)