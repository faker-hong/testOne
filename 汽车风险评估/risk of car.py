import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error
from sklearn.externals import joblib


print("step1:读取数据")
#  训练数据
train_data = pd.read_csv("C:\\Users\\97\\Downloads\\mock data\\train.csv")
train_target = train_data.loc[:, 'Score']
train_features = train_data.iloc[:, 2:]

# 测试数据
test_data = pd.read_csv("C:\\Users\\97\\Downloads\\mock data\\test.csv")
test_target = test_data.loc[:, 'Score']
test_features = test_data.iloc[:, 2:]

print("stpe2: 对数值差别大的列进行标准化，类别的列进行one-hot编码")
# 标准化
transfer = StandardScaler()
train_features.loc[:, ['Col_1', 'Col_2', 'Col_6', 'Col_7']] = transfer.fit_transform(train_features.loc[:, ['Col_1', 'Col_2', 'Col_6', 'Col_7']])
test_features.loc[:, ['Col_1', 'Col_2', 'Col_6', 'Col_7']] = transfer.fit_transform(test_features.loc[:, ['Col_1', 'Col_2', 'Col_6', 'Col_7']])

# 对类别进行one-hot编码
transfer_oneHot = DictVectorizer(sparse=False)
train_features.loc[:, ['Col_3', 'Col_4', 'Col_9', 'Col_11']] = transfer_oneHot.fit_transform(train_features.loc[:, ['Col_3', 'Col_4', 'Col_9', 'Col_11']])
test_features.loc[:, ['Col_3', 'Col_4', 'Col_9', 'Col_11']] = transfer_oneHot.fit_transform(test_features.loc[:, ['Col_3', 'Col_4', 'Col_9', 'Col_11']])

print("step3: 开始训练")
model = RandomForestRegressor()
# 参数调优
param_dic = {'max_features': [max_features for max_features in range(6, 19, 2)],
             'n_estimators': [n_estimators for n_estimators in range(10, 101, 10)]}

estimator = GridSearchCV(model, param_grid=param_dic, cv=10)
estimator.fit(train_features, train_target)
estimator.score(test_features, test_target)
# 得出最佳训练参数
best_params = estimator.best_params_

print("step4: 得到最佳训练参数后进行训练")
model = RandomForestRegressor(best_params)
model.fit(train_features, train_target)

print("step5: 使用均方误差查看模型的效果")
test_predict = model.predict(test_features)
error = mean_squared_error(test_predict, test_target)

print("step6: 保存模型")
joblib.dump(model, 'car_risk_assessment.model')

print("step7: 保存到csv")
result = pd.DataFrame({'id': test_data.loc[:, 'Id'],
                       'Score': test_predict})
result.to_csv("correct_submission.csv", index=False)