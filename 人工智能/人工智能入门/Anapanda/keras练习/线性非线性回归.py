import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD
import matplotlib.pyplot as plt
import numpy as np

'''
    线性
'''
# x_data = np.random.rand(100)
# 正态分布
# 参数loc(float)：正态分布的均值，对应着这个分布的中心。loc=0说明这一个以Y轴为对称轴的正态分布，
# 参数scale(float)：正态分布的标准差，对应分布的宽度，scale越大，正态分布的曲线越矮胖，scale越小，曲线越高瘦。
# 参数size(int 或者整数元组)：输出的值赋在shape里，默认为None。
# noise = np.random.normal(0,0.01, x_data.shape)
# y_data = 0.1*x_data + 0.2 + noise
#
# plt.scatter(x_data, y_data)
# plt.show()
#
# model = Sequential()
# model.add(Dense(1, input_shape=(1,)))
# model.compile(optimizer=SGD(), loss='MSE')
#
# for step in range(5001):
#     cost = model.train_on_batch(x_data, y_data)
#     if step % 500 == 0:
#         print("strp:", step, " cost:", cost)
#
# W, b = model.layers[0].get_weights()
# print("W:", W, " b:", b)
#
# y_pred = model.predict(x_data)
# plt.scatter(x_data, y_data)
# plt.plot(x_data, y_pred, 'r', lw=3)
# plt.show()


'''
    非线性
'''
x_data = np.linspace(-1, 1, 200)
noise = np.random.normal(0, 0.1, x_data.shape)
y_data = np.square(x_data) + noise
plt.scatter(x_data, y_data)

model = Sequential()
model.add(Dense(5, input_shape=(1,), activation='tanh'))
model.add(Dense(1,))
model.compile(optimizer=SGD(), loss='MSE')

for step in range(5001):
    cost = model.train_on_batch(x_data, y_data)
    if step % 500 == 0:
        print("strp:", step, " cost:", cost)

W, b = model.layers[0].get_weights()
print("W:", W, " b:", b)

y_pred = model.predict(x_data)
plt.scatter(x_data, y_data)
plt.plot(x_data, y_pred, 'r', lw=3)
plt.show()