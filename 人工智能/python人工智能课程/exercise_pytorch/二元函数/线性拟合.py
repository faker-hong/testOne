import torch
import torchvision
import torch.optim as optim
import matplotlib.pyplot as plt
import torch.nn as nn


# 升维函数，在第二维度升维度为1，这里数据的维度为(100, 1)
x_data = torch.unsqueeze(torch.linspace(-1, 1, 100), dim=1)
y_data = x_data * 0.3 + 0.2 + 0.2 * torch.rand(x_data.size())

plt.scatter(x_data.data.numpy(), y_data.data.numpy())
plt.show()


# 准备好数据后开始建模
class CNN(torch.nn.Module):
    def __init__(self, n_features, n_hidden, n_output):
        super(CNN, self).__init__()
        self.fc1 = torch.nn.Linear(n_features, n_hidden)
        self.fc2 = torch.nn.Linear(n_hidden, n_output)

# 因为求的是线性回归问题，所以结果可以不使用激活函数
    def forward(self, x):
        x = self.fc1(x)
        x = self.fc2(x)
        return x


# 初始化模型
model = CNN(1, 10, 1)

# 建立好模型后，设置超参数开始训练模型(误差函数，训练轮次，优化器)
epoch = 100
optimizer = optim.SGD(model.parameters(), lr=0.01)
err_func = torch.nn.MSELoss()   # 均方误差

plt.ion()
for e in range(epoch):

    # forward
    predict = model.forward(x_data)

    loss = err_func(predict, y_data)

    # backward
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    # 每五轮更新一次
    if e % 5 == 0:
        print("loss:", loss.data.numpy())
        # 清除当前活动轴，其他轴不变
        plt.cla()
        plt.scatter(x_data.data.numpy(), y_data.data.numpy())
        plt.plot(x_data.data.numpy(), predict.data.numpy(), 'r-', lw=5)
        plt.text(0.5, 0, 'loss=%.4f' % loss.data.numpy(), fontdict={'size': 20, 'color': 'red'})
        # 显示的秒数
        plt.pause(0.1)

plt.ioff()
plt.show()