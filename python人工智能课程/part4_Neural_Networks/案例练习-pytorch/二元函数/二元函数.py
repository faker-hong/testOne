import matplotlib.pyplot as plt
import torch
import torch.nn.functional as F
from torch.autograd import Variable
import torch.nn as nn
import torch.optim as optim


# prepare data sets
tmp = torch.linspace(-1, 1, 100)
x = torch.unsqueeze(tmp, dim=1)
y = x**2 + 0.2*torch.rand(x.size())
plt.scatter(x.data.numpy(), y.data.numpy())
plt.show()


# define model
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(1, 10)
        self.fc2 = nn.Linear(10, 1)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        return x


# 打开交互模式
plt.ion()
plt.show()
model = Net()

# define optimizer and error func
optimizer = optim.SGD(model.parameters(), lr=0.2)
error_func = nn.MSELoss()

for i in range(100):
    # forward pass
    output = model.forward(x)
    loss = error_func(output, y)

    # backward pass
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    # 绘图
    if i % 10 == 0:
        # 清除当前图形中的当前活动轴
        plt.cla()
        plt.scatter(x.data.numpy(), y.data.numpy())
        plt.plot(x.data.numpy(), output.data.numpy(), 'r-', lw=5)
        plt.text(0.5, 0, "Loss:%0.4f" % loss.item(), fontdict={'color': 'red', 'size': 20})
        # 每过0.1秒更新图像
        plt.pause(0.1)

# 关闭交互模式
plt.ioff()
plt.show()