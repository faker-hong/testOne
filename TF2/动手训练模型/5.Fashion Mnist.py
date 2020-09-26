import tensorflow as tf
import matplotlib.pyplot as plt


# 1. 获取数据
# fasion = tf.keras.datasets.fashion_mnist

# (x_train, y_train), (x_test, y_test) = fasion.load_data()
fashion_mnist = tf.keras.datasets.fashion_mnist

(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()


# 可视化数据
def visilazation():
    fig = plt.figure()

    for i in range(9):
        plt.subplot(3, 3, i+1)
        plt.tight_layout()
        plt.imshow(x_train[i])
        plt.colorbar()
        plt.title("label:{}".format(y_train[i]))
        plt.xticks([])
        plt.yticks([])

    plt.show()


# 2. 数据处理
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

x_train = x_train / 255.0
x_test = x_test / 255.0


# 3. 构建模型,编译
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])

# print(model.summary())

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])


# 4. 训练
model.fit(x_train, y_train, epochs=3)


# 5. 评估
model.evaluate(x_test, y_test)


# 6. 模型保存
model.save('fashion_model')