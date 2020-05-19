import jieba as jieba
import pandas as pd
from scipy.stats import pearsonr
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.preprocessing import minmax_scale, StandardScaler
from sklearn.feature_selection import VarianceThreshold
from sklearn.decomposition import PCA


# 获取iris获取，并将数据分成训练集与测试集
def split_iris():
    iris = load_iris()
    # X为特征值, Y为目标值, test_size测试集大小，float类型, random_state数据是否随机
    x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=True)


# 字典特征提取
def DictVectorizer_test():
    data = [{'city': '杭州', 'temperature': 100},
            {'city': '上海', 'temperature': 200},
            {'city': '南京', 'temperature': 300}]
    # 实例化一个转换器类, sparse默认值为True
    # 如果为True范围的sparse矩阵，稀疏矩阵，它把非零值表示出来，索引为后面非零值的位置。类型多的话，节省空间
    transfer = DictVectorizer(sparse=False)
    # 调用fit_transform()
    data_new = transfer.fit_transform(data)
    feature_names = transfer.get_feature_names()
    print(data_new)
    print(feature_names)


# 特征提取计数
def CountVectorizer_demo():
    data = ["life is short, I like like python", "life is too long, I dislike python"]
    # 中文的话，就会以短语为单位，英文语言特性，每个单词之间有空格
    # 如果把下面用空格隔开也能达到英文效果，但单个字也是会被忽略，词组语句为计数单位
    # data = ["我爱北京天安门", "天安门上太阳升"]
    # 实例化一个分类器
    transfer = CountVectorizer()
    # 调用fit_transform
    data1 = transfer.fit_transform(data)
    # CountVectorizer中没有sparse这个参数，但是sparse实例可以通过toarray的方式，看到二维数组的结果
    # 这个返回的统计单词出现的次数
    print(data1.toarray())
    print(transfer.get_feature_names())


# 中文分词
def cut_CN_words(text):
    # 这里返回的是一个生成器，强转成list
    a = jieba.cut(text)
    list_words = list(a)
    # 然后把他们像英语的方式连接起来，列：我 爱 北京 天安门
    return " ".join(list_words)


# 中文分词后特征提取计数
def CountVectorizer_Chinese_demo():
    data = ["2020年国考网上报名通道将关闭", "已有近百万人通过资格审查", "根据国家公务员局公布的数据"]
    cut_data = []
    for sentence in data:
        cut_data.append(cut_CN_words(sentence))
    transfer = CountVectorizer()
    data_new = transfer.fit_transform(cut_data)
    print(data_new.toarray())
    print(transfer.get_feature_names())


# 特征提取并计算词占比
def TfidfVectorizer_demo():
    data = ["2020年国考网上报名通道将关闭", "已有近百万人通过资格审查", "根据国家公务员局公布的数据"]
    cut_data = []
    for sentence in data:
        cut_data.append(cut_CN_words(sentence))
    # 判读那个词对文章影响大
    transfer = TfidfVectorizer()
    data_new = transfer.fit_transform(cut_data)
    print(data_new.toarray())
    print(transfer.get_feature_names())


# 归一化，把数据映射到自定义范围内，避免某些特征max，min差别过大影响target，适用小数据
def minmax_scale_demo():
    # 数据格式： 每年消耗公里数， 每年消耗冰淇淋重量， 每年出游时间占比，target
    data = pd.read_csv("")
    data = data.iloc[:, :3]
    # 实例转换器类, feature_range默认为[0, 1]
    transfer = minmax_scale(feature_range=[0, 1])
    data_new = transfer.fit_transform(data)
    print(data_new)


# 标准化, 不易受到异常点影响，适用大数据
def StandardScaler_demo():
    # 数据格式： 每年消耗公里数， 每年消耗冰淇淋重量， 每年出游时间占比，target
    data = pd.read_csv("")
    data = data.iloc[:, :3]
    # 实例转换器类, 映射到-1到1
    transfer = StandardScaler()
    data_new = transfer.fit_transform(data)
    print(data_new)


# 低方差过滤，以及求相关系数
def VarianceThreshold_demo():
    data = pd.read_csv("")
    # 实例化转化器类
    transfer = VarianceThreshold(threshold=2)   # 参数，过略掉方差低于2的特征
    data_new = transfer.fit_transform(data)
    print(data_new)
    # 相关系数
    r = pearsonr("列名1", "列名2")


# PCA降维
def PCA_demo():
    data = [[2, 8, 4, 5], [6, 3, 0, 8], [5, 4, 9, 1]]
    # 如果是整数则表示降成几维的(几个特征，这里n_components=3,把四个特征降成3个特征)
    # 如果是小数则表示保留原特征的百分之多少
    # transfer = PCA(n_components=0.95)
    transfer = PCA(n_components=3)
    data_new = transfer.fit_transform(data)
    print(data_new)


if __name__ == '__main__':
    # split_iris()
    # DictVectorizer_test()
    CountVectorizer_demo()
    # cut_CN_words("我爱北京天安门")
    # CountVectorizer_Chinese_demo()
    # TfidfVectorizer_demo()
    # minmax_scale_demo()
    # PCA_demo()