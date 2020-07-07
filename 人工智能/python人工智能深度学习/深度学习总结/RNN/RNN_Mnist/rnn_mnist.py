import tensorflow as tf
import numpy as np
from tensorflow.contrib.layers import fully_connected
from tensorflow.examples.tutorials.mnist import input_data

tf.reset_default_graph()

# 获取数据
mnist = input_data.read_data_sets('./data/MNIST_data/')

# 测试数据
X_test = mnist.test.images.reshape((-1, 28, 28))  # 转换成n个28x28的测试集, 原本是一维的784像素
y_test = mnist.test.labels

# 参数
n_neurons = 256
n_classes = 10
batch_size = 128
epochs = 20
learning_rate = 0.001

x = tf.placeholder(tf.float32, [None, 28, 28])
y = tf.placeholder(tf.int32, [None])

# 构建网络
lstm = tf.contrib.rnn.BasicRNNCell(num_units=n_neurons)
output, state = tf.nn.dynamic_rnn(lstm, x, dtype=tf.float32)

logits = fully_connected(state, n_classes, activation_fn=None)

cross_entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(labels=y, logits=logits)
cost = tf.reduce_mean(cross_entropy)

optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)

correct_pred = tf.nn.in_top_k(logits, y, 1)
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for e in range(epochs):
        for _ in range(batch_size):
            x_batch, y_batch = mnist.train.next_batch(batch_size)
            x_batch = x_batch.reshape((-1, 28, 28))

            sess.run(optimizer, feed_dict={x: x_batch,
                                           y: y_batch})
            print(y_batch.shape)

        acc_train = sess.run(accuracy, feed_dict={x: x_batch,
                                                  y: y_batch})

        acc_test = sess.run(accuracy, feed_dict={x: x_batch,
                                                 y: y_batch})

        print("epoch: {}/{}".format(e+1, epochs),
              "acc_train: {:.2f}".format(acc_train),
              "acc_test: {:.2f}".format(acc_test))