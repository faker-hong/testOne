import tensorflow as tf
import numpy as np
import os
import matplotlib.pyplot as plt
import cv2
from sklearn.model_selection import train_test_split

data_dir = './data'

# 所有图片的路径目录 21919张, 只用了kaggle上的训练集
all_img_files = os.listdir(os.path.join(data_dir, 'train/'))

def process_data(files):
    data = []
    targets = []

    for img_file in all_img_files[:2000]:
        new_img_file = os.path.join('./data/train', img_file)
        img = cv2.imread(new_img_file)
        resize_img = cv2.resize(img, (100, 100))        # 图片大小不一，统一resize
        img = cv2.cvtColor(resize_img, cv2.COLOR_BGR2RGB)      # 因为cv2的读取方式是GBR，所以需要改变维度的位置

        data.append(img / float(255))       # 特征统一缩放到0-1之间
        if img_file.startswith('c'):
            targets.append([0])
        else:
            targets.append([1])

    return data, targets


# 划分数据集
data, targets = process_data(all_img_files)
x_train, x_test, y_train, y_test = train_test_split(data, targets, test_size=0.3, random_state=0)

# 取测试集的1000个validation
x_val, x_test = x_test[:100], x_test[100:]
y_val, y_test = y_test[:100], y_test[100:]

# 初始化权重,这里用3层卷积层与3层全连接层
weights = {
    # 输入图片为100*100*3， 卷积窗口为5*5，channels为3， 输出channels为16
    'wc1': tf.Variable(tf.truncated_normal([5, 5, 3, 16], stddev=0.1)),
    'wc2': tf.Variable(tf.truncated_normal([5, 5, 16, 32], stddev=0.1)),
    'wc3': tf.Variable(tf.truncated_normal([5, 5, 32, 64], stddev=0.1)),
    'fc1': tf.Variable(tf.truncated_normal([12*12*64, 1024], stddev=0.1)),
    'fc2': tf.Variable(tf.truncated_normal([1024, 512], stddev=0.1)),
    'out': tf.Variable(tf.truncated_normal([512, 1], stddev=0.1))
}

biases = {
    'bc1': tf.Variable(tf.truncated_normal([16], stddev=0.1)),
    'bc2': tf.Variable(tf.truncated_normal([32], stddev=0.1)),
    'bc3': tf.Variable(tf.truncated_normal([64], stddev=0.1)),
    'fc1': tf.Variable(tf.truncated_normal([1024], stddev=0.1)),
    'fc2': tf.Variable(tf.truncated_normal([512], stddev=0.1)),
    'out': tf.Variable(tf.truncated_normal([1]))
}


def net(img, w, b, dropout):
    # 1 - Conv layer 100*100*3 to 50*50*16
    conv_1 = tf.nn.conv2d(img, w['wc1'], strides=[1, 1, 1, 1], padding='SAME')
    conv_1_add_bias = tf.nn.bias_add(conv_1, b['bc1'])
    conv_1_out = tf.nn.relu(conv_1_add_bias)
    conv_1_maxpool = tf.nn.max_pool(conv_1_out, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

    # 2 - Conv layer 50*50*16 to 25*25*32
    conv_2 = tf.nn.conv2d(conv_1_maxpool, w['wc2'], strides=[1, 1, 1, 1], padding='SAME')
    conv_2_add_bias = tf.nn.bias_add(conv_2, b['bc2'])
    conv_2_out = tf.nn.relu(conv_2_add_bias)
    conv_2_maxpool = tf.nn.max_pool(conv_2_out, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

    # 3 - Conv layer 25*25*32 to 12*12*64
    conv_3 = tf.nn.conv2d(conv_2_maxpool, w['wc3'], strides=[1, 1, 1, 1], padding='SAME')
    conv_3_add_bias = tf.nn.bias_add(conv_3, b['bc3'])
    conv_3_out = tf.nn.relu(conv_3_add_bias)
    conv_3_maxpool = tf.nn.max_pool(conv_3_out, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='VALID')

    # 先转为一维
    flatten = tf.reshape(conv_3_maxpool, [-1, w['fc1'].get_shape().as_list()[0]])

    # 4 - Fully Connected 12*12*64 to 1024
    fc1 = tf.add(tf.matmul(flatten, w['fc1']), b['fc1'])
    fc1 = tf.nn.relu(fc1)

    # 5 - Fully Connected 1024 to 512
    fc2 = tf.add(tf.matmul(fc1, w['fc2']), b['fc2'])
    fc2 = tf.nn.relu(fc2)
    # 增加dropout
    drop = tf.nn.dropout(fc2, dropout)

    # 6 - out
    logits = tf.add(tf.matmul(drop, w['out']), b['out'])
    out = tf.nn.sigmoid(logits, name='predict')

    return out


def get_batches(x, y, batch_size):
    length = len(x)
    batchs = length // batch_size
    length = len(x[: batch_size*batchs])
    batch_i = 0
    result = []
    for i in range(0, length, batch_size):
        batch_i += 1
        batch_x = x[i: i+batch_size]
        batch_y = y[i: i+batch_size]
        result.append([batch_i, batch_x, batch_y])

    return result


# 超参数
learning_rate = 0.00001
epochs = 10
keep_prob = 0.75
steps = 0
batch_size = 128

# model input
x = tf.placeholder(tf.float32, [None, 100, 100, 3], name='x')
y = tf.placeholder(tf.float32, [None, 1], name='y')
dropout = tf.placeholder(tf.float32, name='dropout')

# define loss func , optimizer
out = net(x, weights, biases, dropout)
loss = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=out, labels=y))
optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(loss)

# accuracy
correct_pred = tf.equal(tf.round(out), y)
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

# 保存模型
saver = tf.train.Saver()

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for epoch_i in range(epochs):
        result = get_batches(x_train, y_train, batch_size)
        for batch_i, batch_x, batch_y in result:
            cost, _ = sess.run([loss, optimizer], feed_dict={x: batch_x,
                                                             y: batch_y,
                                                             dropout: keep_prob})

            print("epoch: {} / {} ----- batch: {}".format(epoch_i+1, epochs, batch_i),
                  "cost: {:.4f}".format(cost))

            if batch_i % 5 == 0:
                acc_val = sess.run(accuracy, feed_dict={x: x_val,
                                                        y: y_val,
                                                        dropout: 1.})
                print("-------------------------Accuracy: {:.2f}".format(acc_val))

        # 测试
        acc_test = sess.run(accuracy, feed_dict={x: x_test,
                                                 y: y_test,
                                                 dropout: 1.})
        print("Accuracy Test: {:.2f}".format(acc_test))

    # data-00000-of-00001和.index保存了所有的weights、biases、gradients等变量。
    # meta保存了图结构。
    # checkpoint文件是个文本文件，里面记录了保存的最新的checkpoint文件以及其它checkpoint文件列表
    saver.save(sess, 'models/classification')


    # 使用模型
    # saver = tf.train.import_meta_graph('models/classification.meta')
    # saver.restore(sess, tf.train.latest_checkpoint('models'))
    #
    # graph = tf.get_default_graph()
    # # 得到的就是那两个placeholder
    # x = graph.get_tensor_by_name('x:0')
    # y = graph.get_tensor_by_name('y:0')
    # dropout = graph.get_tensor_by_name('dropout:0')
    # predict = graph.get_tensor_by_name('predict:0')
    #
    # # 把x传进去就是预测值
    # predict_value = sess.run(predict, feed_dict={x: x_val,
    #                                              y: y_val,
    #                                              dropout: 1.})
    # print(predict_value)