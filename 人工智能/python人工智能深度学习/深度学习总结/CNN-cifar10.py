import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt


# 获得训练集与测试集
(train_data, train_label), (test_data, test_label) = tf.keras.datasets.cifar10.load_data()
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


# Store layers weight & bias
weights = {
    'wc1': tf.Variable(tf.truncated_normal([5, 5, 3, 32], stddev=0.1)),
    'wc2': tf.Variable(tf.truncated_normal([5, 5, 32, 64], stddev=0.1)),
    'wd1': tf.Variable(tf.truncated_normal([8*8*64, 1024], stddev=0.1)),
    'out': tf.Variable(tf.truncated_normal([1024, 10], stddev=0.1))}

biases = {
    'bc1': tf.Variable(tf.random_normal([32])),
    'bc2': tf.Variable(tf.random_normal([64])),
    'bd1': tf.Variable(tf.random_normal([1024])),
    'out': tf.Variable(tf.random_normal([10]))}


def conv2d(x, W, b, strides=1):
    x = tf.nn.conv2d(x, W, strides=[1, strides, strides, 1], padding='SAME')
    x = tf.nn.bias_add(x, b)
    return tf.nn.relu(x)


def maxpool2d(x, k=2):
    return tf.nn.max_pool(
        x,
        ksize=[1, k, k, 1],
        strides=[1, k, k, 1],
        padding='SAME')


def conv_net(x, weights, biases, dropout):
    # layer 1 - 32*32*3 to 16*16*32
    conv1 = conv2d(x, weights['wc1'], biases['bc1'])
    conv1 = maxpool2d(conv1, k=2)

    # layer 2 - 16*16*32 to 8*8*64
    conv2 = conv2d(conv1, weights['wc2'], biases['bc2'])
    conv2 = maxpool2d(conv2, k=2)

    # layer -3 fully connected layer  8*8*64 to 1024
    fc1 = tf.reshape(conv2, [-1, weights['wd1'].get_shape().as_list()[0]])
    fc1 = tf.add(tf.matmul(fc1, weights['wd1']), biases['bd1'])
    fc1 = tf.nn.relu(fc1)
    fc1 = tf.nn.dropout(fc1, dropout)

    # layer - 4 output layer  1024 to 10
    logits = tf.add(tf.matmul(fc1, weights['out']), biases['out'])
    out = tf.nn.softmax(logits)

    return out


def get_batched(train_data, train_label_one_hot, batch_size):
    # 获取刚好够的数据
    size_batches = len(train_data) // batch_size
    train_data = train_data[:size_batches*batch_size]
    train_label_one_hot = train_label_one_hot[:size_batches*batch_size]
    for i in range(0, len(train_data), batch_size):
        batch_data = train_data[i: i+batch_size]
        batch_label = train_label_one_hot[i: i+batch_size]
        batch_label = np.squeeze(batch_label)
        yield batch_data, batch_label


learning_rate = 0.000001
epochs = 10
batch_size = 128
dropout = 0.75
steps = 0

# tf Graph input
image_inputs, image_targets, lr, keep_prob = model_input(train_data.shape[1], train_data.shape[2], train_data.shape[3], 10)

# Model
logits = conv_net(image_inputs, weights, biases, keep_prob)

# Define loss and optimizer
cost = tf.reduce_mean(\
    tf.nn.softmax_cross_entropy_with_logits(logits=logits, labels=image_targets))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate)\
    .minimize(cost)

# Accuracy
correct_pred = tf.equal(tf.argmax(logits, 1), tf.argmax(image_targets, 1))
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

# Initializing the variables
init = tf.global_variables_initializer()

# Launch the graph
with tf.Session() as sess:
    sess.run(init)
    train_label_one_hot = train_label_one_hot.eval(session=sess)

    for epoch in range(epochs):
        for x, y in get_batched(train_data, train_label_one_hot, 32):
            steps += 1
            sess.run(optimizer, feed_dict={
                image_inputs: x,
                image_targets: y,
                keep_prob: dropout})

            # Calculate batch loss and accuracy
            loss, _ = sess.run([cost, optimizer], feed_dict={
                image_inputs: x,
                image_targets: y,
                keep_prob: 1.})
            valid_acc = sess.run(accuracy, feed_dict={
                image_inputs: x,
                image_targets: y,
                keep_prob: 1.})
            writer = tf.summary.FileWriter('./logs', sess.graph)
            writer.close()

            if steps % 100 == 0:
                acc = sess.run(accuracy, feed_dict={image_inputs: x,
                                                    image_targets: y,
                                                    keep_prob: 1.})
                print("training loss: {:.4f}".format(loss),
                      "accuracy: {:.4f}".format(acc))