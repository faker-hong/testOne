from collections import OrderedDict

import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision
import torchvision.transforms as transforms
import torch.optim as optim


# define transform

transform = transforms.Compose(
    [transforms.ToTensor(),
     transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])]
)

# 获取数据
data_train = torchvision.datasets.CIFAR10(root="./data", train=True, transform=transform, download=True)
data_test = torchvision.datasets.CIFAR10(root="./data", train=False, transform=transform, download=True)

train_loader = torch.utils.data.DataLoader(data_train, batch_size=64, shuffle=True)
test_loader = torch.utils.data.DataLoader(data_test, batch_size=64, shuffle=True)


# define model
class LeNet(nn.Module):
    # 一般在__init__中定义网络需要的操作算子，比如卷积、全连接算子等等
    def __init__(self):
        super(LeNet, self).__init__()

        self.fc1 = nn.Linear(1024, 512)
        self.fc2 = nn.Linear(512, 128)
        self.fc3 = nn.Linear(128, 64)
        # 最终有10类，所以最后一个全连接层输出数量是10
        self.fc4 = nn.Linear(64, 10)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))
        x = self.fc4(x)
        return x


model = LeNet()
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.003)

# hyper-parameter and train network
epochs = 3
print_every = 40
step = 0
print("Start Training...")
for e in range(epochs):
    running_loss = 0
    for images, labels in iter(train_loader):
        # print(images.size())
        step += 1
        images.resize_(images.size()[0], 1024)

        optimizer.zero_grad()

        output = model.forward(images)
        loss = criterion(output, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item()

        if step % print_every == 0:
            print("Epoch: {}/{}".format(e + 1, epochs),
                  "Loss:{:.4f}".format(running_loss / print_every))

            running_loss = 0

print("Done Training!")