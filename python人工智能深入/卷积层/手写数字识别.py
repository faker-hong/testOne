from keras.datasets import mnist
import matplotlib.pyplot as plt
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.callbacks import ModelCheckpoint
import numpy as np


# 获取数据
(X_train, y_train), (X_test, y_test) = mnist.load_data()

print("训练集中有%d个样本" % len(X_train))
print("测试集中有%d个样本" % len(X_test))

# 像素是[0-255]，处理成[0-1]
X_train = X_train.astype('float32')/255
X_test = X_test.astype('float32')/255

# 将标签进行one-hot编码
y_train = np_utils.to_categorical(y_train, 10)
y_test = np_utils.to_categorical(y_test, 10)

# 定义model结构
model = Sequential()
model.add(Flatten(input_shape=X_train.shape[1:]))
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(10, activation='softmax'))

# 编译model
model.compile(loss='categorical_crossentropy', optimizer='rmsprop',
              metrics=['accuracy'])
# 训练
checkpointer = ModelCheckpoint(filepath='mnist.model.best.hdf5',
                               verbose=1, save_best_only=True)
hist = model.fit(X_train, y_train, batch_size=128, epochs=10,
                 validation_split=0.2, callbacks=[checkpointer],
                 verbose=1, shuffle=True)

# 用测试机评估
score = model.evaluate(X_test, y_test, verbose=0)
accuracy = 100*score[1]
print("测试准确率：%.2f%%" % accuracy)

# 保存模型
model.load_weights('mnist.model.best.hdf5')

# 画6个样本
# fig = plt.figure(figsize=(20, 20))
# for i in range(6):
#     ax = fig.add_subplot(1, 6, i+1, xticks=[], yticks=[])
#     ax.imshow(X_train[i], cmap='gray')
#     ax.set_title(str(y_train[i]))
# plt.show()

# 单个图片更详细的显示
# def visualize_input(img, ax):
#     ax.imshow(img, cmap='gray')
#     width, height = img.shape
#     thresh = img.max()/2.5
#     for x in range(width):
#         for y in range(height):
#             ax.annotate(str(round(img[x][y], 2)), xy=(y, x),
#                         horizontalalignment='center',
#                         verticalalignment='center',
#                         color='white' if img[y][x] < thresh else 'black')
#
#
# fig = plt.figure(figsize=(12, 12))
# ax = fig.add_subplot(111)
# visualize_input(X_train[0], ax)
# plt.show()