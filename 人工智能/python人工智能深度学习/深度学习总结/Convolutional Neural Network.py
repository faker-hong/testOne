import numpy as np
import tensorflow as tf


# 获得训练集与测试集
(train_data, train_label), (test_data, test_label) = tf.keras.datasets.cifar10.load_data()
# 将特征的像素都除以255，维持在0-1之间
train_data = train_data / float(255)
# 这里的label需要进行one-hot编码
train_label_one_hot = tf.one_hot(train_label, 10, on_value=1, off_value=0)
test_label_one_hot = tf.one_hot(test_label, 10, on_value=1, off_value=0)


# model_input
def model_input(image_width, image_height, image_channels, classes):
    image_inputs = tf.placeholder(tf.float32, [None, image_width, image_height, image_channels], name='image_inputs')
    image_targets = tf.placeholder(tf.float32, [None, classes], name='image_targets')
    lr = tf.placeholder(tf.float32, name='lr')
    keep_prob = tf.placeholder(tf.float32, name='keep_prob')

    return image_inputs, image_targets, lr, keep_prob


def conv_net(image, classes, keep_prob):
    # image shape 32*32*3
    # 这里不需要定义weights和bias的原因是tf.layers.conv2定义的均匀化的w和b
    conv1 = tf.layers.conv2d(image, 32, 5, strides=1, padding='same', activation=tf.nn.relu)   # 32*32*32
    maxpool_1 = tf.layers.max_pooling2d(conv1, 2, strides=2, padding='same')    # 16*16*32
    maxpool_1 = tf.nn.dropout(maxpool_1, keep_prob)

    conv2 = tf.layers.conv2d(maxpool_1, 64, 5, strides=1, padding='same', activation=tf.nn.relu)   # 16*16*64
    maxpool_2 = tf.layers.max_pooling2d(conv2, 2, strides=2, padding='same')     # 8*8*64
    maxpool_2 = tf.nn.dropout(maxpool_2, keep_prob)

    conv3 = tf.layers.conv2d(maxpool_2, 128, 5, strides=1, padding='same', activation=tf.nn.relu)  # 8*8*128
    maxpool_3 = tf.layers.max_pooling2d(conv3, 2, strides=2, padding='same')  # 4*4*128
    maxpool_3 = tf.nn.dropout(maxpool_3, keep_prob)

    # 先进行展平，然后进入全连接层
    flat = tf.reshape(maxpool_3, (-1, 4*4*128))
    fc1 = tf.layers.dense(flat, 128, activation=tf.nn.relu)
    fc2 = tf.layers.dense(fc1, 64, activation=tf.nn.relu)
    fc2 = tf.nn.dropout(fc2, keep_prob)
    out = tf.layers.dense(fc2, classes, activation=tf.nn.softmax)

    return out


def get_batched(train_data, train_label_one_hot, batch_size):
    # 获取刚好够的数据
    size_batches = len(train_data) // batch_size
    train_data = train_data[:size_batches*batch_size]
    train_label_one_hot = train_label_one_hot[:size_batches*batch_size]
    for i in range(0, len(train_data), batch_size):
        batch_data = train_data[i: i+batch_size]
        batch_label = train_label_one_hot[i: i+batch_size]
        # 这里获取到的维度为[32, 1, 10],将多余的轴去除，不然与model_input中定义的shape对不上
        batch_label = np.squeeze(batch_label)
        yield batch_data, batch_label


# 超参数
epochs = 10
learning_rate = 0.0001
drop_out = 0.75
print_steps = 0


def train(epochs, learning_rate, print_steps, drop_out, train_data, train_label_one_hot, batch_size):
    image_inputs, image_targets, lr, keep_prob = model_input(train_data.shape[1], train_data.shape[2], train_data.shape[3], 10)
    logits = conv_net(image_inputs, 10, drop_out)

    loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=logits, labels=image_targets))
    opt = tf.train.GradientDescentOptimizer(lr).minimize(loss)

    # accuracy
    correct_pred = tf.equal(tf.argmax(logits, 1), tf.argmax(image_targets, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        train_label_one_hot = train_label_one_hot.eval(session=sess)
        for epoch_i in range(epochs):
            for x, y in get_batched(train_data, train_label_one_hot, batch_size):
                print_steps += 1
                # 这里的变量命名不能与run后面的相同
                logits_, train_loss, _ = sess.run([logits, loss, opt], feed_dict={image_inputs: x,
                                                                                  image_targets: y,
                                                                                  lr: learning_rate,
                                                                                  keep_prob: drop_out})

                if print_steps % 100 == 0:
                    acc = sess.run(accuracy, feed_dict={image_inputs: x,
                                                        image_targets: y,
                                                        keep_prob: 1.})
                    print("training loss: {:.4f}".format(train_loss),
                          "accuracy: {:.4f}".format(acc))


if __name__ == '__main__':
    train(epochs, learning_rate, print_steps, drop_out, train_data, train_label_one_hot, 32)