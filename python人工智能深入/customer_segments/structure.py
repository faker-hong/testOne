import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn import svm
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

# 1.获取数据
data = pd.read_csv("数据csv文件路径")

# 2.将数据划分，特征值与目标值
income_raw = data['income']
features_raw = data.drop('income', axis=1)

# 3.'capital-gain' 和 'capital-loss'数据的最大最小值相差很大，这里进行log转换，但0的对数的问题，统一都+1
skewed = ['capital-gain', 'capital-loss']
features_log_transformed = pd.DataFrame(data=features_raw)
features_log_transformed[skewed] = features_log_transformed.apply(lambda x: np.log(x+1))

# 4.也可以使用标准化进行数据的缩放
scaler = MinMaxScaler()
numerical = ['age', 'education-num', 'capital-gain', 'capital-loss', 'hours-per-week']
features_log_minmax_transform = pd.DataFrame(data=features_log_transformed)
features_log_minmax_transform[numerical] = scaler.fit_transform(features_log_transformed[numerical])

# 5.用pandas.get_dummies()进行one-hot编码
features_final = pd.get_dummies(features_log_minmax_transform)

# 6.将目标值大于等于50k的为0， 小于50k的为1
income = income_raw.apply(lambda x: 1 if x >= 50000 else 0)

# 7.分割训练集和测试集
x_train, x_test, y_train, y_test = train_test_split(features_final, income, test_size=0.2, random_state=0)

# 8.初始化模型，like decisiontree
clf = svm.SVR()

# 9.训练
clf.fit(x_train, y_train)

# 10.验证评估
predict = clf.predict(y_train)
accuracy = mean_squared_error(predict, y_test)
