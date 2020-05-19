import keras
from keras.models import Sequential
from keras.layers import Conv2D, Dense, Dropout, Flatten, MaxPooling2D
from keras.callbacks import ModelCheckpoint
from keras.datasets import cifar10
from keras.utils import np_utils
import numpy as np

# 获取数据
(x_train, y_train), (x_test, y_test) = cifar10.load_data()

# 规范化
x_train = x_train.astype('float')/255
x_test = x_test.astype('float')/255

# 对类别进行one-hot编码
num_class = len(np.unique(y_train))
y_train = np_utils.to_categorical(y_train, num_class)
y_test = np_utils.to_categorical(y_test, num_class)

# 划分训练集和验证集，验证集是为了验证训练的效果是否过拟合或欠拟合
(x_train, x_valid) = x_train[5000:], x_train[:5000]
(y_train, y_valid) = y_train[5000:], y_train[:5000]

# 构建model结构
model = Sequential()
model.add(Conv2D(filters=16, kernel_size=2, padding='same', activation='relu', input_shape=(32, 32, 3)))
model.add(MaxPooling2D(pool_size=2))
model.add(Conv2D(filters=32, kernel_size=2, padding='same', activation='relu'))
model.add(MaxPooling2D(pool_size=2))
model.add(Conv2D(filters=64, kernel_size=2, padding='same', activation='relu'))
model.add(MaxPooling2D(pool_size=2))
model.add(Dropout(0.3))
model.add(Flatten())
model.add(Dense(500, activation='relu'))
model.add(Dropout(0.3))
model.add(Dense(10, activation='softmax'))


# 编译模型
model.compile(loss='categorical_crossentropy', optimizer='rmsprop',
              metrics=['accuracy'])

# 训练
checkpoint = ModelCheckpoint(filepath='model.weights.best.hdf5', verbose=1, save_best_only=True)
hist = model.fit(x_train, y_train, batch_size=32, epochs=100, validation_data=(x_valid, y_valid),
                 callbacks=[checkpoint], verbose=2, shuffle=True)

# 保存model
model.load_weights('model.weights.best.hdf5')

# 测试集准确率
score = model.evaluate(x_test, y_train, verbose=0)
print('test accuracy %.2f' % 100*score[1])
