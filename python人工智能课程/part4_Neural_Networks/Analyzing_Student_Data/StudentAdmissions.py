import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('./student_data.csv')


def plot_points(data):
    X = np.array(data[['gre', 'gpa']])
    y = np.array(data['admit'])
    admitted = X[np.argwhere(y == 1)]
    rejected = X[np.argwhere(y == 0)]
    # print(admitted)
    # print(rejected)
    plt.scatter([p[0][0] for p in rejected], [p[0][1] for p in rejected], s=25, color='red', edgecolor='k')
    plt.scatter([p[0][0] for p in admitted], [p[0][1] for p in admitted], s=25, color='cyan', edgecolor='k')
    plt.xlabel('TEST(GRE)')
    plt.ylabel('GRADE(PGA)')


# TODO: One-hot encoding the rank
# TODO:  Make dummy variables for rank
one_hot_data = pd.get_dummies(data, columns=['rank'])


# TODO: Drop the previous rank column
# one_hot_data = one_hot_data.drop('rank', axis=1)  # 该方法也可以，或者使用下面的重命名列名
one_hot_data.rename(columns={'rank_1': '1', 'rank_2': '2', 'rank_3': '3', 'rank_4': '4'}, inplace=True)


# Making a copy of our data
processed_data = one_hot_data[:]
# TODO: Scale the columns
# 因为gre, gpa的数据差别很大，这里把这两个特征处理成0-1之间的数值。gre在200-800之间，gpa在1-4之间，so divide the large
processed_data['gre'] = np.divide(processed_data['gre'], 800)
processed_data['gpa'] = np.divide(processed_data['gpa'], 4)


# Splitting the data into Training and Testing
train_index = np.random.choice(processed_data.index, size=int(len(processed_data)*0.9), replace=False)  # replace表示抽样是否放回
train_data, test_data = processed_data.iloc[train_index], processed_data.drop(train_index)
# print("Number of training samples is", len(train_data))
# print("Number of testing samples is", len(test_data))
# print(train_data[:10])
# print(test_data[:10])


# Splitting the data into features and targets (labels)
train_features = train_data.drop('admit', axis=1)
train_targets = train_data['admit']
test_features = test_data.drop('admit', axis=1)
test_targets = test_data['admit']


def sigmoid(x):
    return 1/(1+np.exp(-x))


def sigmoid_prime(x):
    return sigmoid(x)*(1-sigmoid(x))


def error_formula(y, output):
    return -(y*np.log(output) + (1-y)*np.log(1-output))


def error_term_formula(y, output):
    return -(y-output)*output*(1-output)