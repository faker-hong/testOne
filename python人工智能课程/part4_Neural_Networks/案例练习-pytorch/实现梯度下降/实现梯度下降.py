from python人工智能课程.pytorch_practice.实现梯度下降.get_data_sets import train_feature, train_target, test_feature, test_target
import torch
import torchvision
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import numpy as np


def sigmoid(x):
    return 1/(1 + np.exp(-x))

# 6, 2, 1的3层神经网络
hidden_size = 2
output_size = 1
n_record, n_feature = train_feature.shape

# 超参数
epochs = 1000
learnrate = 0.03
last_loss = None

# 自定义weight
weight_input_hidden = np.random.normal(scale=1/n_feature**.5, size=(n_feature, hidden_size))
weight_hidden_output = np.random.normal(scale=1/n_feature**.5, size=hidden_size)

for e in range(epochs):
    del_w_i_h = np.zeros(weight_input_hidden.shape)
    del_w_h_o = np.zeros(weight_hidden_output.shape)
    for x, y in zip(train_feature.values, train_target):
        # forward pass
        hidden_in = np.dot(x, weight_input_hidden)
        hidden_out = sigmoid(hidden_in)

        output_in = np.dot(hidden_out, weight_hidden_output)
        output_out = sigmoid(output_in)

        loss = y - output_out

        loss_item = loss * output_out * (1 - output_out)

        # hidden error
        hidden_error = np.dot(loss_item, weight_hidden_output)
        hidden_error_item = hidden_error * hidden_out * (1 - hidden_out)

        del_w_h_o += loss_item * hidden_out
        del_w_i_h += hidden_error_item * x[:, None]

    weight_hidden_output += learnrate * del_w_h_o / n_record
    weight_input_hidden += learnrate * del_w_i_h / n_record

    # 打印均方误差
    if e % 99 == 0:
        # forward pass
        hidden_out = sigmoid(np.dot(x, weight_input_hidden))
        output_out = sigmoid(np.dot(hidden_out, weight_hidden_output))

        loss = np.mean((output_out - y) ** 2)

        if last_loss and loss > last_loss:
            print(loss, "误差在增大")
        else:
            print("Loss:", loss)


# test
hidden_out = sigmoid(np.dot(test_feature, weight_input_hidden))
output_out = sigmoid(np.dot(hidden_out, weight_hidden_output))

predict = output_out > 0.5
accuracy = np.mean(predict == test_target)

print("准确率：{:.1f}%".format(accuracy * 100))