import tensorflow as tf
import numpy as np
from string import punctuation
from collections import Counter

# tf.reset_default_graph()

# 读取数据
with open('reviews.txt', 'r') as f:
    reviews = f.read()

with open('labels.txt', 'r') as f:
    labels = f.read()

# 得到所有的单词
all_text = ''.join([c for c in reviews if c not in punctuation])
reviews = all_text.split('\n')

all_text = ' '.join(reviews)
words = all_text.split()

# 以字典的方式存储word
counts = Counter(words)
vocab = sorted(counts, key=counts.get, reverse=True)
vocab_to_int = {word: ii for ii, word in enumerate(vocab, 1)}

reviews_ints = []
for each in reviews:
    reviews_ints.append([vocab_to_int[word] for word in each.split()])

# 将labels进行one-hot
labels = labels.split('\n')
labels = np.array([1 if each == 'positive' else 0 for each in labels])

# 因为有一条评论的length为0，需要做处理
non_zero_idx = [ii for ii, review in enumerate(reviews_ints) if len(review) != 0]
reviews_ints = [reviews_ints[ii] for ii in non_zero_idx]
labels = np.array([labels[ii] for ii in non_zero_idx])

# 因为评论有长有短，这里只取长度200，不够left pad 0， 够了的话只要前200个词
seq_len = 200
features = np.zeros((len(reviews_ints), seq_len), dtype=int)
for i, row in enumerate(reviews_ints):
    features[i, -len(row):] = np.array(row)[:seq_len]

# 划分数据集
split_frac = 0.8
split_idx = int(len(features)*0.8)
train_x, val_x = features[:split_idx], features[split_idx:]
train_y, val_y = labels[:split_idx], labels[split_idx:]

test_idx = int(len(val_x)*0.5)
val_x, test_x = val_x[:test_idx], val_x[test_idx:]
val_y, test_y = val_y[:test_idx], val_y[test_idx:]

# build model
learning_rate = 0.001
lstm_size = 256
lstm_layer = 1
batch_size = 500

# model inputs
n_word = len(vocab_to_int)+1    # 加1因为之前的索引从1开始
graph = tf.Graph()      # create graph obj
with graph.as_default():
    inputs_ = tf.placeholder(tf.int32, [None, None], name='inputs_')
    labels_ = tf.placeholder(tf.int32, [None, None], name='labels_')
    keep_prob = tf.placeholder(tf.float32, name='keep_prob')


# build embedding layer
embed_size = 300
with graph.as_default():
    embedding = tf.Variable(tf.random_uniform((n_word, embed_size), -1, 1))
    embed = tf.nn.embedding_lookup(embedding, inputs_)


# LSTM layer
with graph.as_default():
    lstm = tf.contrib.rnn.BasicLSTMCell(lstm_size)
    drop = tf.contrib.rnn.DropoutWrapper(lstm, output_keep_prob=keep_prob)
    cell = tf.contrib.rnn.MultiRNNCell([drop]*lstm_layer)
    initial_state = cell.zero_state(batch_size, tf.float32)


# forward pass
with graph.as_default():
    outputs, final_state = tf.nn.dynamic_rnn(cell, embed, initial_state=initial_state)


# output
with graph.as_default():
    predict = tf.contrib.layers.fully_connected(outputs[:, -1], 1, activation_fn=tf.sigmoid)
    cost = tf.losses.mean_squared_error(labels_, predict)
    optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)


# 验证集的准确率
with graph.as_default():
    correct_pred = tf.equal(tf.cast(tf.round(predict), tf.int32), labels_)
    accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))


# get batches
def get_batches(train_x, train_y, batch_size):
    n_batch = len(train_x) // batch_size
    train_x = train_x[:n_batch*batch_size]
    train_y = train_y[:n_batch*batch_size]

    result = []
    for ii in range(0, len(train_x), batch_size):
        batch_x = train_x[ii: ii+batch_size]
        batch_y = train_y[ii: ii+batch_size]
        result.append([batch_x, batch_y])

    return result


# training
epochs = 10

with graph.as_default():
    saver = tf.train.Saver()

with tf.Session(graph=graph) as sess:
    sess.run(tf.global_variables_initializer())
    iteration = 1
    for e in range(epochs):
        state = sess.run(initial_state)

        for ii, (x, y) in enumerate(get_batches(train_x, train_y, batch_size), 1):
            feed = {inputs_: x,
                    labels_: y[:, None],
                    keep_prob: 0.5,
                    initial_state: state}
            loss, state, _ = sess.run([cost, final_state, optimizer], feed_dict=feed)

            if iteration % 5 == 0:
                print("Epoch: {}/{}".format(e, epochs),
                      "Iteration: {}".format(iteration),
                      "Train loss: {:.3f}".format(loss))

            if iteration % 25 == 0:
                val_acc = []
                val_state = sess.run(cell.zero_state(batch_size, tf.float32))
                for x, y in get_batches(val_x, val_y, batch_size):
                    feed = {inputs_: x,
                            labels_: y[:, None],
                            keep_prob: 1,
                            initial_state: val_state}
                    batch_acc, val_state = sess.run([accuracy, final_state], feed_dict=feed)
                    val_acc.append(batch_acc)
                print("Val acc: {:.3f}".format(np.mean(val_acc)))
            iteration += 1
    saver.save(sess, "checkpoints/sentiment.ckpt")


# test
test_acc = []
with tf.Session(graph=graph) as sess:
    saver.restore(sess, tf.train.latest_checkpoint('checkpoints'))
    test_state = sess.run(cell.zero_state(batch_size, tf.float32))
    for ii, (x, y) in enumerate(get_batches(test_x, test_y, batch_size), 1):
        feed = {inputs_: x,
                labels_: y[:, None],
                keep_prob: 1,
                initial_state: test_state}
        batch_acc, test_state = sess.run([accuracy, final_state], feed_dict=feed)
        test_acc.append(batch_acc)
    print("Test accuracy: {:.3f}".format(np.mean(test_acc)))