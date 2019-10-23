import matplotlib as plt
from sklearn import datasets
# 调用线性回归函数
from sklearn.linear_model import LinearRegression

#导入数据
loaded_data = datasets.load_boston()
# 全部作为训练集
data_x = loaded_data.data
data_y = loaded_data.target


# 设置线性回归魔鬼
model = LinearRegression()
# 训练数据
model.fit(data_x, data_y)

# 利用模型，对比数据，进行预测，与原标签比较
print(model.predict(data_x[:4]))
print(data_y[:4])