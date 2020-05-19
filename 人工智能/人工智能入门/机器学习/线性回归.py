from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, SGDRegressor, Ridge, LogisticRegression
from sklearn.metrics import mean_squared_error
from sklearn.externals import joblib
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np


# 波斯顿房价预测，正规方程
def linear_1():
    # 获取数据集
    boston = load_boston()
    # 划分数据集
    x_train, x_test, y_train, y_test = train_test_split(boston.data, boston.target, random_state=22)
    # 特征工程
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)
    # 预估器
    estimator = LinearRegression()
    estimator.fit(x_train, y_train)
    print("正规方程-权重系数：", estimator.coef_)
    print("正规方程-偏置：", estimator.intercept_)
    # 模型评估
    y_predict = estimator.predict(x_test)
    error = mean_squared_error(y_test, y_predict)
    print("正规方程-均方误差：", error)


# 波斯顿房价预测，梯度下降
def linear_2():
    # 获取数据
    boston  = load_boston()
    # 划分数据
    x_train, x_test, y_train, y_test = train_test_split(boston.data, boston.target, random_state=22)
    # 特征工程
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)
    # 预估器   递归10000次, 使用L2正则化的线性回归
    estimator = SGDRegressor(max_iter=10000, penalty='l2')
    estimator.fit(x_train, y_train)
    print("梯度下降-权重系数：", estimator.coef_)
    print("梯度下降-偏置：", estimator.intercept_)
    # 模型评估
    y_predict = estimator.predict(x_test)
    error = mean_squared_error(y_test, y_predict)
    print("梯度下降-均方误差：", error)


# 波斯顿房价预测， 岭回归。模型的保存与加载
def linear_3():
    # 获取数据
    boston  = load_boston()
    # 划分数据
    x_train, x_test, y_train, y_test = train_test_split(boston.data, boston.target, random_state=22)
    # 特征工程
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)

    # # 预估器
    # estimator = Ridge()
    # estimator.fit(x_train, y_train)
    # # 模型保存
    # joblib.dump(estimator, 'bidge.test')

    # 模型加载于使用
    estimator = joblib.load('bidge.test')

    print("岭回归-权重系数：", estimator.coef_)
    print("岭回归-偏置：", estimator.intercept_)
    # 模型评估
    y_predict = estimator.predict(x_test)
    error = mean_squared_error(y_test, y_predict)
    print("岭回归-均方误差：", error)


# 癌症分类预测
def cancer():
    # 获取数据
    path = 'https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data'
    clomun_names = ['Sample code number', 'Clump Thickness', 'Uniformity of Cell Size', 'Uniformity of Cell Shape', 'Marginal Adhesion',
             'Single Epithelial Cell Size', 'Bare Nuclei', 'Bland Chromatin', 'Normal Nucleoli', 'Mitoses', 'Class']
    data = pd.read_csv(path, names=clomun_names)
    # 数据处理: 缺失值处理
    data = data.replace(to_replace="?", value=np.nan)
    data.dropna(inplace=True)
    # print(data.isnull().any())
    # 数据集划分
    x = data.iloc[:, 1:-1]
    y = data["Class"]
    x_train, x_test, y_train, y_test = train_test_split(x, y)
    # 特征工程： 无量纲化-标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)
    # 逻辑回归预估器(假设函数是线性回归， 所以有回归系数和偏置)
    estimator = LogisticRegression()
    estimator.fit(x_train, y_train)
    print("回归系数：", estimator.coef_)
    print("偏置：", estimator.intercept_)
    # 模型评估
    score = estimator.score(x_test, y_test)
    print("准确率", score)


if __name__ == '__main__':
    # linear_1()
    # linear_2()
    linear_3()
    # cancer()