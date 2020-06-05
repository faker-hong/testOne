import pandas as pd
import numpy as np
import tensorflow as tf
import tflearn
from tflearn.data_utils import to_categorical
from collections import Counter

reviews = pd.read_csv('../IMDB/reviews.txt', header=None)
labels = pd.read_csv('../IMDB/labels.txt', header=None)

# 对所有单词计数
total_counts = Counter()
for _, row in reviews.iterrows():
    total_counts.update(row[0].split(' '))
print("Total words in data set: ", len(total_counts))

# 将出现频率最高的10000个词保存在vacab中,倒叙，vocab中保存的仅是单词
vocab = sorted(total_counts, key=total_counts.get, reverse=True)[:10000]
word2idx = {word: i for i, word in enumerate(vocab)}


def text_to_vector(text):
    word_vector = np.zeros(len(vocab), dtype=np.int_)
    for word in text.split(' '):
        idx = word2idx.get(word, None)
        if idx is None:
            continue
        else:
            word_vector[idx] += 1
    return np.array(word_vector)


# 将所有评论转换为vector的形式
word_vectors = np.zeros((len(reviews), len(vocab)), dtype=np.int_)
for ii, (_, text) in enumerate(reviews.iterrows()):
    word_vectors[ii] = text_to_vector(text[0])


Y = (labels == 'positive').astype(np.int_)
records = len(labels)

shuffle = np.arange(records)
np.random.shuffle(shuffle)      # 把序列顺序打乱
test_fraction = 0.9

train_split, test_split = shuffle[:int(records*test_fraction)], shuffle[int(records*test_fraction):]
trainX, trainY = word_vectors[train_split, :], to_categorical(Y.values[train_split, 0], 2)
testX, testY = word_vectors[test_split, :], to_categorical(Y.values[test_split, 0], 2)


# Network building
def build_model():
    # This resets all parameters and variables, leave this here
    tf.reset_default_graph()

    # Inputs
    net = tflearn.input_data([None, 10000])

    # Hidden layer(s)
    net = tflearn.fully_connected(net, 200, activation='ReLU')
    net = tflearn.fully_connected(net, 25, activation='ReLU')

    # Output layer
    net = tflearn.fully_connected(net, 2, activation='softmax')
    net = tflearn.regression(net, optimizer='sgd',
                             learning_rate=0.1,
                             loss='categorical_crossentropy')

    model = tflearn.DNN(net)
    return model


model = build_model()


# Training
model.fit(trainX, trainY, validation_set=0.1, show_metric=True, batch_size=128, n_epoch=100)

predictions = (np.array(model.predict(testX))[:, 0] >= 0.5).astype(np.int_)
test_accuracy = np.mean(predictions == testY[:, 0], axis=0)
print("Test accuracy: ", test_accuracy)