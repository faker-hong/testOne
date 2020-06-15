import tensorflow as tf

# output depth
k_output = 64

# image Properties
image_width = 10
image_height = 10
image_depth = 3

# Convolution Filter
filter_size_width = 5
filter_size_height = 5

# input
input = tf.placeholder(tf.float32, shape=[None, image_height, image_width, image_depth])

# weight and bias
weight = tf.Variable(tf.truncated_normal(
    [filter_size_height, filter_size_width, image_depth, k_output]
))

bias = tf.Variable(tf.zeros(k_output))


# apply Convolution         strides规定是一个思维的张量，前后为1，中间的为水平滑动和垂直滑动的大小
conv_layer = tf.nn.conv2d(input, weight, strides=[1, 2, 2, 1], padding='same')

# add bias
conv_layer = tf.nn.bias_add(conv_layer, bias)

# apply activation
conv_layer = tf.nn.relu(conv_layer)