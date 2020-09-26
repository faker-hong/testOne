import tensorflow as tf


mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

# 这里因为只是测试，不做验证集
input = tf.keras.Input(shape=(28, 28))
x = tf.keras.layers.Flatten(input_shape=(28, 28))(input)
x = tf.keras.layers.Dense(128, activation='relu')(x)
x = tf.keras.layers.Dropout(0.2)(x)
output = tf.keras.layers.Dense(10, activation='softmax')(x)

model = tf.keras.Model(inputs=input, outputs=output, name='mnist2_model')

# 模型构建好后，进行编译，指定优化器，损失函数等
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy'])

# 训练
model.fit(x_train, y_train, 3)

# 评估
model.evaluate(x_test, y_test)

# 模型保存,后面可以设置一个save_format参数，来设置保存的类型，比如h5
model.save('mnist_model')

# 模型加载评估数据
mo = tf.keras.models.load_model('mnist_model/mnist_model')

# 评估
mo.evaluate(x_test, y_test)