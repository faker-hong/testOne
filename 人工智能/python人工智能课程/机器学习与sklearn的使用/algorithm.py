from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris, fetch_20newsgroups
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.ensemble import RandomForestClassifier


# KNN算法
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


# KNN算法模型选择与调优
def KNN_iris_GSCV():
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
    estimator = KNeighborsClassifier()
    # K值的选择，CV为把数据分为几组，进行交叉验证
    param_dic = {"n_neighbors": [1, 3, 5, 7, 9]}
    estimator = GridSearchCV(estimator, param_grid=param_dic, cv=10)
    estimator.fit(x_train, y_train)

    # 模型评估，计算准确率
    score = estimator.score(x_test, y_test)
    print(score)

    # GridSearchCV结果的属性
    a = estimator.best_params_      # 最佳参数
    b = estimator.best_score_       # 最佳结果
    c = estimator.best_estimator_   # 最佳预估器
    d =estimator.cv_results_       # 交叉验证结果
    print("最佳参数：", a)
    print("最佳结果：", b)
    print("最佳预估器：", c)
    print("交叉验证结果：", d)


# 朴素贝叶斯算法 新闻分类
# 下载的时候速度很慢，这里把data网上下载然后修改datasets里twenty_newsgroups的_download_20newsgroups方法
def nb_news():
    # 获取数据
    news = fetch_20newsgroups(subset='all')
    # 划分数据集
    x_train, x_test, y_train, y_test = train_test_split(news.data, news.target)
    # 特征工程:文本特征抽取   Tfid
    transfer = TfidfVectorizer()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)

    # 朴素贝叶斯算法预估器流程
    estimator = MultinomialNB()
    estimator.fit(x_train, y_train)
    # 模型评估
    score = estimator.score(x_test, y_test)
    print(score)


# 决策树来分类鸢尾花
def dicition_iris():
    # 获得数据
    iris = load_iris()
    # 划分数据
    x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target)
    # 决策树预估器
    estimator = DecisionTreeClassifier(criterion='entropy')
    estimator.fit(x_train, y_train)
    # 模型评估
    score = estimator.score(x_test, y_test)
    print(score)
    export_graphviz(estimator, out_file='tree.doc', feature_names=iris.feature_names)


# 随机森林
def random_forest():
    iris = load_iris()
    x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target)
    estimator = RandomForestClassifier()
    # 加入网格搜索和交叉验证
    param_dic = {"n_estimators": [120, 200, 300, 500],
                 "max_depth": [1, 2, 3, 4]}
    estimator = GridSearchCV(estimator, param_grid=param_dic, cv=3)
    estimator.fit(x_train, y_train)
    score = estimator.score(x_test, y_test)
    print(score)
    print(estimator.best_params_)


if __name__ == '__main__':
    # KNN_iris()
    # KNN_iris_GSCV()
    # nb_news()
    # dicition_iris()
    random_forest()