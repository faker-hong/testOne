from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.datasets import load_boston
from sklearn.ensemble import AdaBoostRegressor

# Adaboost是一种将一个弱分类器迭代，下一个分类器以上一个分类器为基础，通过准确率，高的占比高，低的占比低，
# 最终合并求和得出最终模型

# 加载数据
data=load_boston()
# 分割数据
train_x, test_x, train_y, test_y = train_test_split(data.data, data.target, test_size=0.25, random_state=33)
# 使用 AdaBoost 回归模型
regressor = AdaBoostRegressor()
regressor.fit(train_x, train_y)
pred_y = regressor.predict(test_x)
mse = mean_squared_error(test_y, pred_y)
print(" 房价预测结果 ", pred_y)
print(" 均方误差 = ", round(mse, 2))
