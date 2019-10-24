from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def KNN_iris():
    # 获取数据
    iris = load_iris()

    # 划分数据
    x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=True, test_size=0.2)

    # 特征工程：标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    # 因为x_train已经找到了这类数据的规则(方差，均值等),所以测试集只需要transform和训练集一样的标准化
    x_test = transfer.transform(x_test)

    # KNN算法评估
    estimator = KNeighborsClassifier(n_neighbors=3)
    estimator.fit(x_train, y_train)

    # 模型评估，计算准确率
    score = estimator.score(x_test, y_test)
    print(score)


if __name__ == '__main__':
    KNN_iris()