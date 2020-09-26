import tensorflow as tf
import itertools
import os


# # list 列表数据
dataset = tf.data.Dataset.from_tensor_slices([1, 2, 3])
for element in dataset:
    print(element)


# Generator 生成器
def gen():
    for i in itertools.count(1):
        yield (i, [1] * i)

dataset = tf.data.Dataset.from_generator(
    gen,
    (tf.int64, tf.int64),
    (tf.TensorShape([]), tf.TensorShape([None]))
)

print(list(dataset.take(5)))


# 文本文件
parent_dir = "/TF2/动手训练模型/files"
FILE_NAMES = ['cowper.txt', 'derby.txt', 'butler.txt']


def labeler(example, index):
    return example, tf.cast(index, tf.int64)


labeled_data_sets = []

for i, file_name in enumerate(FILE_NAMES):
    lines_dataset = tf.data.TextLineDataset(os.path.join(parent_dir, file_name))
    labeled_dataset = lines_dataset.map(lambda ex: labeler(ex, i))
    labeled_data_sets.append(labeled_dataset)

BUFFER_SIZE = 10

all_labeled_data = labeled_data_sets[0]
for labeled_dataset in labeled_data_sets[1:]:
    all_labeled_data = all_labeled_data.concatenate(labeled_dataset)

all_labeled_data = all_labeled_data.shuffle(
    BUFFER_SIZE, reshuffle_each_iteration=False)

# 出现编码错误
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xd5 in position 90: invalid continuation byte
for ex in all_labeled_data.take(1):
    print(ex)