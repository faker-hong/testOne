import numpy
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
model.add(Dense(500, input_shape=(784, )))   # 输入层，28*28=784
model.add(Activation('tanh'))       # 激活函数
model.add(Dropout(0.5))         # 50%的dropout

model.add(Dense(500))   # 隐藏层节点500个
model.add(Activation('tanh'))
model.add(Dropout(0.5))

model.add(Dense(10))    # 输出类别10个， 所以维度是10
model.add(Activation('softmax'))    # 激活函数为softmax

'''
    编译
'''
sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)     # 优化函数，设定学习率（lr）等参数
model.compile(loss='categorical_crossentropy', optimizer=sgd, class_mode='categorical')

'''
    训练
    .fit的一些参数
    batch_size:对总的样本数进行分组，每组包含的样本数量
    epochs:训练次数
    shuffle:是否把随机数打乱后再进行训练
    validation_split:拿出百分之多少用来做交叉验证
    verbose:屏显模式 0：不输出 1：输出进度 2：输出每次的训练结果
'''
X_train, y_train, X_test, y_test = mnist.load_data()    # 用Keras自带的mnist工具读取数据
# 由于mist的输入数据维度是(num, 28, 28)，这里需要把后面的维度直接拼起来变成784维
X_train = X_train.reshape(X_train.shape[0], X_train.shape[1] * X_train.shape[2])
X_test = X_test.reshape(X_test.shape[0], X_test.shape[1] * X_test.shape[2])
Y_train = (numpy.arange(10) == y_train[:, None]).astype(int)
Y_test = (numpy.arange(10) == y_test[:, None]).astype(int)

model.fit(X_train, Y_train, batch_size=200, epochs=50, shuffle=True, verbose=0, validation_split=0.3)
model.evaluate(X_test, Y_test, batch_size=200, verbose=0)

'''
    输出
'''
print("test set")
scores = model.evaluate(X_test, Y_test, batch_size=200, verbose=0)
print("")
print("The test loss is %f" % scores)
result = model.predict(X_test, batch_size=200, verbose=0)

result_max = numpy.argmax(result, axis = 1)
test_max = numpy.argmax(Y_test, axis = 1)

result_bool = numpy.equal(result_max, test_max)
true_num = numpy.sum(result_bool)
print("")
print("The accuracy of the model is %f" % (true_num/len(result_bool)))