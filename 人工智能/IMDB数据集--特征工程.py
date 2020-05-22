from keras.datasets import imdb
import numpy as np


# 获取训练集与测试集， 前10000个常频词
(train_data, train_label), (test_data, test_label) = imdb.load_data(num_words=10000)

# 查看数据和标签是如何的

# 这里为单词的索引
print(train_data[0])

# 0为负面，1为正面
print(train_label[0])

# 将训练集的第一条评论解码为英文单词看一看
word_index = imdb.get_word_index()  # 获得单词和索引的字典

reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])     # 因为work_index的key是单词,value是索引

# 解码训练集中第一条评论
decode_comment = ' '.join([reverse_word_index.get(i-3, '?') for i in train_data[0]])

print(decode_comment)


# 将数据集进行one-hot编码
def convert_to_one_hot(data, dimention=10000):
    results = np.zeros(len(data), dimention)
    for i, sequence in enumerate(data):
        results[i, sequence] = 1

    return results


# 将训练集与测试集进行转换
train_data = convert_to_one_hot(train_data)
test_data = convert_to_one_hot(test_data)

# 将标签也进行向量化
train_label = np.asarray(train_label).astype('float32')
test_label = np.asarray(test_label).astype('float32')