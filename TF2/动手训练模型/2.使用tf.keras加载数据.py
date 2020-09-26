import tensorflow as tf
import matplotlib.pyplot as plt

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

print(x_train.shape, y_train.shape)
print(x_test.shape, y_test.shape)

y_train = y_train.astype('float32')
y_test = y_test.astype('float32')

# validation dataset
x_val = x_train[-1000:]
y_val = y_train[-1000:]
x_train = x_train[:-1000]
y_train = y_train[:-1000]

# 可视化数据
fig = plt.figure()
for i in range(9):
    plt.subplot(3, 3, i+1)
    plt.tight_layout()      # 自动适配子尺寸
    plt.imshow(x_train[i], cmap='Greys')
    plt.title('Label:{}'.format(y_train[i]))
    plt.xticks([])      # 删除x刻度
    plt.yticks([])      # 删除y刻度

plt.show()

