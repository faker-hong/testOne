import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from keras.utils import np_utils


# 获得训练集与测试集
(train_data, train_label), (test_data, test_label) = tf.keras.datasets.cifar10.load_data()
# 规范化
train_data = train_data.astype('float')/255
test_data = test_data.astype('float')/255

# 对类别进行one-hot编码
num_class = len(np.unique(train_label))
train_label = np_utils.to_categorical(train_label, num_class)
test_label = np_utils.to_categorical(test_label, num_class)

# 划分训练集和验证集，验证集是为了验证训练的效果是否过拟合或欠拟合
(x_train, x_valid) = train_data[5000:], train_data[:5000]
(y_train, y_valid) = train_label[5000:], train_label[:5000]


# 打乱样本，获得数据批次
def get_batched(x_train, y_train, batch_size):
    # 获取刚好够的数据
    size_batches = len(x_train) // batch_size
    train_data = x_train[:size_batches*batch_size]
    train_label = y_train[:size_batches*batch_size]
    idx = np.arange(len(train_data))
    np.random.shuffle(idx)
    idx = np.array(idx)
    for i in range(0, len(train_data), batch_size):
        # 打乱样本
        idx_ = idx[i:i+batch_size]
        batch_data = np.array(train_data)[idx_]
        batch_label = np.array(train_label)[idx_]
        # 这里获取到的维度为[32, 1, 10],将多余的轴去除，不然与model_input中定义的shape对不上
        batch_label = np.squeeze(batch_label)
        yield batch_data, batch_label


# model_input
def model_input(classes):
    image_inputs = tf.placeholder(tf.float32, [None, 32, 32, 3], name='image_inputs')
    image_targets = tf.placeholder(tf.int32, [None, classes], name='image_targets')
    keep_prob = tf.placeholder(tf.float32, name='keep_prob')
    lr = tf.placeholder(tf.float32, name='lr')

    return image_inputs, image_targets,  keep_prob, lr


# 超参数
epochs = 10
learning_rate = 0.00001
drop_out = 0.3
print_steps = 0
n_classes = 10


def conv_net(x, drop_out):
    # 32*32*3 to 32*32*16 to 16*16*16
    conv1 = tf.layers.conv2d(x, 16, 2, strides=1, padding='SAME', activation=tf.nn.relu)
    maxpool_1 = tf.layers.max_pooling2d(conv1, 2, strides=2)

    # 16*16*16 to 16*16*32 to 8*8*32
    conv2 = tf.layers.conv2d(maxpool_1, 32, 2, strides=1, padding='SAME', activation=tf.nn.relu)
    maxpool_2 = tf.layers.max_pooling2d(conv2, 2, strides=2)

    # 8*8*32 to 8*8*32 to 4*4*64
    conv3 = tf.layers.conv2d(maxpool_2, 64, 2, strides=1, padding='SAME', activation=tf.nn.relu)
    maxpool_2 = tf.layers.max_pooling2d(conv3, 2, strides=2)
    drop_1 = tf.nn.dropout(maxpool_2, drop_out)

    flatten = tf.reshape(drop_1, (-1, 4*4*64))
    fc1 = tf.layers.dense(flatten, 500, activation=tf.nn.relu)
    drop_2 = tf.nn.dropout(fc1, drop_out)
    out = tf.layers.dense(drop_2, 10, activation=tf.nn.softmax)

    return out


def train(epochs, learning_rate, print_steps, drop_out, train_data, train_label, batch_size):
    x, y, keep_prob, lr = model_input(n_classes)
    out = conv_net(x, drop_out)

    cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=out, labels=y))
    opt = tf.train.AdamOptimizer(lr).minimize(cost)

    # accuracy
    correct_pred = tf.equal(tf.argmax(out, 1), tf.argmax(y, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        # train_label_one_hot = train_label_one_hot.eval(session=sess)
        for epoch_i in range(epochs):
            for image_inputs, image_labels in get_batched(train_data, train_label, batch_size):
                print_steps += 1
                # 这里的变量命名不能与run后面的相同
                logits_, loss, _ = sess.run([out, cost, opt], feed_dict={x: image_inputs,
                                                                         y: image_labels,
                                                                         lr: learning_rate,
                                                                         keep_prob: drop_out})

                if print_steps % 10 == 0:
                    test_loss = sess.run(cost, feed_dict={x: x_valid,
                                                          y: y_valid,
                                                          keep_prob: 1.})
                    print("---------------------------------------------------------------")
                    print("valid_acc:{:.4f}".format(test_loss))
                    print("---------------------------------------------------------------")
                print("Epoch:{}/{}".format(epoch_i, epochs),
                      "training loss: {:.4f}".format(loss))


if __name__ == '__main__':
    train(epochs, learning_rate, print_steps, drop_out, train_data, train_label, 32)