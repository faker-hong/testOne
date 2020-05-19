import numpy
import keras
from keras import Sequential
from keras.datasets import mnist
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD

''' 
    选择模型:
    1.序贯模式      
    2.函数式模式
 '''
model = Sequential()

'''
    构建网络层:
    1.输入层
    2.隐藏层
    3.输出层
'''
model.add(Dense(512, input_shape=(784, )))   # 输入层，28*28=784
model.add(Activation('relu'))       # 激活函数
model.add(Dropout(0.5))         # 50%的dropout

model.add(Dense(256))   # 隐藏层节点500个
model.add(Activation('relu'))
model.add(Dropout(0.5))

model.add(Dense(10))    # 输出类别10个， 所以维度是10
model.add(Activation('softmax'))    # 激活函数为softmax

'''
    编译
'''
sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)     # 优化函数，设定学习率（lr）等参数
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

'''
    训练
    .fit的一些参数
    batch_size:对总的样本数进行分组，每组包含的样本数量
    epochs:训练次数
    shuffle:是否把随机数打乱后再进行训练
    validation_split:拿出百分之多少用来做交叉验证
    verbose:屏显模式 0：不输出 1：输出进度 2：输出每次的训练结果
'''
(x_train, y_train), (x_test, y_test) = mnist.load_data()    # 用Keras自带的mnist工具读取数据
# 由于mist的输入数据维度是(num, 28, 28)，这里需要把后面的维度直接拼起来变成784维
x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)
x_train = x_train/255
x_test = x_test/255
y_train = keras.utils.to_categorical(y_train, 10)
y_test = keras.utils.to_categorical(y_test, 10)

model.fit(x_train, y_train, batch_size=64, epochs=5, shuffle=True, verbose=0, validation_data=(x_test, y_test))
score = model.evaluate(x_test, y_test)
'''
    输出
'''
print(score)
