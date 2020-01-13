import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data_sets = pd.read_csv("./student_data.csv")


def plot_points(data_sets):
    X = np.array(data_sets[["gre", "gpa"]])
    Y = np.array(data_sets["admit"])

    # get the student who admit and reject
    # np.argwhere(Y==1)  返回的是Y中等于1的索引值
    admits = X[np.argwhere(Y == 1)]
    rejects = X[np.argwhere(Y == 0)]

    # plot
    plt.scatter([p[0][0] for p in admits], [p[0][1] for p in admits], s=30, color='green', edgecolors="None")
    plt.scatter([p[0][0] for p in rejects], [p[0][1] for p in rejects], s=30, color='red', edgecolors="None")
    plt.xlabel("GRE")
    plt.ylabel("GPA")
    plt.show()


# 数据中的rank列有4个等级，数值大小对神经网络学习有影响，这里处理成one-hot编码
one_hot = pd.get_dummies(data=data_sets, columns=['rank'])

# 把one-hot后的rank列全部重命名为rank
one_hot.rename(columns={"rank_1": 1, "rank_2": 2, "rank_3": 3, "rank_4": 4}, inplace=True)

# 因为gre, gpa的数据差别很大，这里把这两个特征处理成0-1之间的数值。gre在200-800之间，gpa在1-4之间，so divide the large
one_hot['gre'] = np.divide(one_hot['gre'], 800)
one_hot['gpa'] = np.divide(one_hot['gpa'], 4)

# 划分测试集，训练集
index_train = np.random.choice(one_hot.index, size=int(len(one_hot)*0.9), replace=False)
train, test = one_hot.iloc[index_train], one_hot.drop(index_train)

# 训练集与测试集的特征值与目标值
train_feature = train.drop("admit", axis=1)
train_target = train["admit"]
test_feature = test.drop("admit", axis=1)
test_target = test["admit"]

# print(train_feature)
# print(train_target)
# print(test_feature)
# print(test_target)