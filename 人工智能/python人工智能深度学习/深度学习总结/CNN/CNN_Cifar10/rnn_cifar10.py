import numpy as np
import tensorflow as tf
from tensorflow.contrib.layers import fully_connected

tf.reset_default_graph()

# 获取数据
# (50000, 32, 32, 3) (50000, 1),  (10000, 32, 32, 3) (10000, 1), 得到的数据类型均为ndarray
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
y_train = np.squeeze(y_train)
y_test = np.squeeze(y_test)


def get_batch(x, y, batch_size):
    batches = len(x) // batch_size
    x = x[:batch_size*batches]
    y = y[:batch_size*batches]
    result = []
    batch_i = 0

    for i in range(0, len(x), batch_size):
        batch_i += 1
        x_batch = x[i: i+batch_size]
        y_batch = y[i: i+batch_size]
        result.append([batch_i, x_batch, y_batch])

    return result


# 对label进行one-hot编码，之后进行计算cross_entropy
def one_hot(labels):
    max_index = np.max(labels) + 1
    labels = np.eye(max_index)[labels]
    return labels


y_train = one_hot(y_train)
y_test = one_hot(y_test)


# 划分数据集
x_val, x_test = x_test[:5000], x_test[5000:]
y_val, y_test = y_test[:5000], y_test[5000:]

# model input
x = tf.placeholder(tf.float32, [None, 32, 32, 3])
y = tf.placeholder(tf.int32, [None, 10])

# 参数
n_classes = 10
batch_size = 128

epochs = 10
learning_rate = 0.001


# build model
def net(x):
    # 32*32*3 to 16*16*16
    cov1 = tf.layers.conv2d(x, 16, 5, 1, padding='same', activation=tf.nn.relu)
    cov1 = tf.layers.max_pooling2d(cov1, 2, 2, padding='same')

    # 16*16*16 to 8*8*32
    cov2 = tf.layers.conv2d(cov1, 32, 5, 1, padding='same', activation=tf.nn.relu)
    cov2 = tf.layers.max_pooling2d(cov2, 2, 2, padding='same')

    # flatten
    flatten = tf.reshape(cov2, (-1, 8*8*32))

    # fully connected
    logtis = tf.layers.dense(flatten, 10)

    return logtis


logits = net(x)

crocc_entropy = tf.nn.softmax_cross_entropy_with_logits_v2(labels=y, logits=logits)
cost = tf.reduce_mean(crocc_entropy)

optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)

correct_pred = tf.equal(tf.argmax(logits, 1), tf.argmax(y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for e in range(epochs):
        batches = get_batch(x_train, y_train, batch_size)
        for batch_i, x_batch, y_batch in batches:
            sess.run(optimizer, feed_dict={x: x_batch,
                                           y: y_batch})

            if batch_i % 20 == 0:
                loss = sess.run(cost, feed_dict={x: x_batch,
                                                 y: y_batch})
                acc_test = sess.run(accuracy, feed_dict={x: x_val,
                                                         y: y_val})
                print("epoch: {}/{}".format(e+1, epochs),
                      "train loss: {:.4f}".format(loss),
                      "validation accuracy: {:.2f}".format(acc_test))

    test_acc = sess.run(accuracy, feed_dict={x: x_test,
                                             y: y_test})
    print("test accuracy: {:.2f}".format(test_acc))