import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn import metrics
"""
        sklearn主要用于数据分类，回归。
        数据挖掘建模，机器学习
    
    1.先对数据进行预处理  将数据分成训练集与测试集
    2.建模  使用决策树进行fit和predict
    3.验证  分析正确率或者使用混淆矩阵
"""

def main():
    # 拿到鸢尾花的数据,进行预处理
    iris = load_iris()
    train_data, test_data, train_target, test_target = train_test_split(iris.data, iris.target, test_size=0.2, random_state=1)

    # 建模，进行训练和预测数据
    clf = tree.DecisionTreeClassifier(criterion="entropy")
    clf.fit(train_data, train_target)
    pred =clf.predict(test_data)

    # 验证
    print(metrics.accuracy_score(y_pred=pred, y_true=test_target))


if __name__ == '__main__':
    main()