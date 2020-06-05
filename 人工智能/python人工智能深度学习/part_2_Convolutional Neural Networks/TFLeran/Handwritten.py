import numpy as np
import tensorflow as tf
import tflearn
import tflearn.datasets.mnist as mnist

# 获得训练集与测试集
trainX, trainY, testX, testY = mnist.load_data(one_hot=True)


def build_model():
    tf.reset_default_graph()

    # 输入层
    net = tflearn.input_data([None, trainX.shape[1]])

    # 隐藏层
    net = tflearn.fully_connected(net, 128, activation="ReLu")
    net = tflearn.fully_connected(net, 64, activation="ReLu")

    # 输出层
    net = tflearn.fully_connected(net, 10, activation="softmax")
    net.regression(net, optimizer='sgd',
                   learning_rate=0.01,
                   loss='categorical_crossentropy')
    model = tflearn.DNN(net)
    return model


model = build_model()
model.fit(trainX, trainY, validation_set=0.1, show_metric=True, batch_size=100, n_epoch=20)

# 验证
prediction = np.array(model.predict(testX)).argmax(axis=1)
trueY = testY.argmax(axis=1)
accuracy = np.mean(prediction == trueY, axis=0)