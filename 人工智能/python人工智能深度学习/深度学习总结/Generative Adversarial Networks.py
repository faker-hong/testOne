import tensorflow as tf
import numpy as np
import helper
import os
from glob import glob


data_dir = './data'

'''
data process
'''


# model_input
def model_input(image_width, image_height, image_channels, z_dim):
    inputs_image = tf.placeholder(tf.float32, [None, image_width, image_height, image_channels], name='inputs')
    inputs_z = tf.placeholder(tf.float32, [None, z_dim], name='inputs_z')
    learning_rate = tf.placeholder(tf.float32, name='learning_rate')

    return inputs_image, inputs_z, learning_rate


# generator
def generator(input_z, out_dim, is_train=True, alpha=0.2):
    with tf.variable_scope('generator', reuse=not is_train):
        x1 = tf.layers.dense(input_z, 3*3*512)
        x1 = tf.reshape(x1, (-1, 3, 3, 512))
        bn1 = tf.layers.batch_normalization(x1, training=is_train)
        relu1 = tf.maximum(alpha*bn1, bn1)
        # 3*3*512 now

        x2 = tf.layers.conv2d_transpose(relu1, 256, 5, strides=2, padding='same')
        bn2 = tf.layers.batch_normalization(x2, training=is_train)
        relu2 = tf.maximum(alpha*bn2, bn2)
        # 6*6*256

        x3 = tf.layers.conv2d_transpose(relu2, 128, 5, strides=2, padding='same')
        bn3 = tf.layers.batch_normalization(x3, tarining=is_train)
        relu3 = tf.maximum(alpha*bn3, bn3)
        # 12*12*128

        logits = tf.layers.conv2d_transpose(relu3, out_dim, 6 , strides=2, padding='valid')
        # 28*28*out_dim

        out = tf.tanh(logits)

    return out


# discriminator
def discriminator(inputs, reuse=False, is_train=False, alpha=0.2):
    # 第一层不建议使用batch_normalization，会降低准确率
    with tf.variable_scope('discriminator', reuse=reuse):
        # image shape 28*28*3
        x1 = tf.layers.conv2d(inputs, 32, 5, strides=2, padding='same')
        relu1 = tf.layers.batch_normalization(x1, training=True)

        # 14*14*32
        x2 = tf.layers.conv2d(relu1, 64, 5, strides=2, padding='same')
        bm2 = tf.layers.batch_normalization(x2, training=True)
        relu2 = tf.maximum(alpha*bm2, bm2)

        # 7*7*64
        x3 = tf.layers.conv2d(relu2, 128, 5, strides=2, padding='same')
        bm3 = tf.layers.batch_normalization(x3, training=True)
        relu3 = tf.maximum(alpha*bm3, bm3)

        # 4*4*128
        flat = tf.reshape(relu3, (-1, 4*4*128))

        logits = tf.layers.dense(flat, 1)
        out = tf.sigmoid(logits)

    return logits, out


# loss
def get_loss(inputs_image, inputs_z, out_dim):
    g_model = generator(inputs_z, out_dim)
    d_real_logits, d_real_out = discriminator(inputs_image)
    d_fake_logits, d_fake_out = discriminator(g_model, reuse=True)

    d_real_loss = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=d_real_logits, labels=tf.ones_like(d_real_out)))
    d_fake_loss = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=d_fake_logits, labels=tf.zeros_like(d_fake_out)))

    d_loss = d_real_loss + d_fake_loss
    g_loss = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=d_fake_logits, labels=tf.ones_like(d_fake_out)))

    return d_loss, g_loss


# opt
def model_opt(d_loss, g_loss, learning_rate, beta1):
    # 获取训练的所有variables
    t_vars = tf.trainable_variables()
    g_vars = [var for var in t_vars if var.name.startswith('generate')]
    d_vars = [var for var in t_vars if var.name.startswith('discriminator')]

    # 确保之前所需OPs都执行完
    with tf.control_dependencies(tf.get_collection(tf.GraphKeys.UPDATE_OPS)):
        g_opt = tf.train.AdamOptimizer(learning_rate, beta1=beta1).minimize(g_loss, var_list=g_vars)
        d_opt = tf.train.AdamOptimizer(learning_rate, betal=beta1).minimize(d_loss, var_list=d_vars)

    return d_opt, g_opt


# train
def train(epoch_count, batch_size, z_dim, out_dim, learning_rate, beta1, get_batches, data_shape, data_iamge_mode):
    _, image_width, image_height, image_channels = data_shape

    input_image, input_z, lr = model_input(image_width, image_height, image_channels, z_dim)

    d_loss, g_loss = get_loss(input_image, input_z, out_dim)
    d_opt, g_opt = model_opt(d_loss, g_loss, lr, beta1)

    steps = 0

    with tf.Session() as sess:
        # 全局变量初始化
        sess.run(tf.global_variables_initializer())

        for epoch_i in epoch_count:
            for image_batch in get_batches(batch_size):
                steps += 1

                # 传入的z的数量与image数量相同
                batch_z = np.random.uniform(-1, 1, size=(batch_size, z_dim))

                # run optimizer
                _ = sess.run(d_opt, feed_dict={input_image: image_batch, input_z: batch_z, lr: learning_rate})
                _ = sess.run(g_opt, feed_dict={input_image: image_batch, input_z: batch_z, lr: learning_rate})

                if steps % 100 == 0:
                    train_loss_d = d_loss.eval({input_image:image_batch, input_z:batch_z})
                    train_loss_g = d_loss.eval({input_z:batch_z})
                    print("epoch{}/{}...".format(epoch_i, epoch_count),
                          "Discriminator Loss: {:.4f}".format(train_loss_d),
                          "Generator Loss: {:.4f}".format(train_loss_g))


batch_size = 128
z_dim = 3
learning_rate = 0.001
beta1 = 0.5


epochs = 1

celeba_dataset = helper.Dataset('celeba', glob(os.path.join(data_dir, 'img_align_celeba/*.jpg')))
with tf.Graph().as_default():
    train(epochs, batch_size, z_dim, learning_rate, beta1, celeba_dataset.get_batches,
          celeba_dataset.shape, celeba_dataset.image_mode)