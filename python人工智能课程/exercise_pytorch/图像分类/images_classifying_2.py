import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import torchvision.transforms as transforms
import torchvision


# define transfrom 数据处理，归一化
transform = transforms.Compose(
    [transforms.ToTensor(),
     transforms.Normalize((.5, .5, .5), (.5, .5, .5))]  # mean与std
)

# get data_sets
train_sets = torchvision.datasets.CIFAR10('./data', download=True, train=True, transform=transform)
test_sets = torchvision.datasets.CIFAR10('./data', download=True, train=False, transform=transform)

# get data_loader
train_loader = torch.utils.data.DataLoader(train_sets, batch_size=64, shuffle=True)
test_loader = torch.utils.data.DataLoader(test_sets, batch_size=64, shuffle=True)


# define model
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        # Conv2d的第一个参数是输入的channel数量，第二个是输出的channel数量，第三个是kernel size
        # 彩图有三通道(R,G,B),输入channel对应为3,输出channel自选(filter的数量),kernel size为filter的宽高,这里为5*5
        self.conv1 = nn.Conv2d(3, 6, 5)
        # 卷积第二层输入为第一层的输出
        self.conv2 = nn.Conv2d(6, 16, 5)

        # 定义全连接层,由于上一层有16个channel输出，每个feature map大小为5*5，所以全连接层的输入是16*5*5
        self.fc1 = nn.Linear(16*5*5, 120)
        self.fc2 = nn.Linear(120, 60)
        self.fc3 = nn.Linear(60, 10)    # 输出为10个类别，所以输出为10
        # 池化层，第一个参数为窗口大小，第二个为滑动步长
        self.max_pool = nn.MaxPool2d(2, 2)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = self.max_pool(x)
        x = F.relu(self.conv2(x))
        x = self.max_pool(x)

        # 进入全连接层要转为1维的
        x = x.view(-1, 16*5*5)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)

        # dim=1 对每一行进行log_softmax, dim=0, 对每一列进行
        return F.log_softmax(x, dim=1)


# train function
def train(model, train_loader, err_func, optimizer, epochs):
    for e in range(epochs):
        # 在这个模式下，dropout时打开的
        model.train()
        running_loss = 0
        for i, data in enumerate(train_loader):
            images, labels = data

            # forward pass
            output = model.forward(images)
            loss = err_func(output, labels)

            # backward pass
            optimizer.zero_grad()   # 梯度清零
            loss.backward()
            optimizer.step()
            running_loss += loss.item()

            # 每一个样本输出loss与epoch
            if i % 100 == 99:
                # Make sure network is in eval mode for inference
                # 在这个模式下，dropout是关闭的
                model.eval()
                with torch.no_grad():
                    test_loss, accuracy = validation(model, err_func, test_loader)
                print("Epoch:{}/{}".format(e+1, epochs),
                      "Loss:{:.4f}".format(running_loss / 100),
                      "Test Loss:{:.4f}".format(test_loss / len(test_loader)),      # 除以len(test_loader)后获得平均loss
                      "accuracy:{:.3f}".format(accuracy / len(test_loader)))        # 除以len(test_loader)后获得平均正确率

                running_loss = 0
            # 重新打开训练模式
            model.train()


# validation
def validation(model, err_func, test_loader):
    test_loss = 0
    accuracy = 0
    for i, data in enumerate(test_loader):
        images, labels = data

        # forward pass
        output = model.forward(images)
        loss = err_func(output, labels)
        test_loss += loss

        # 因为之前使用log_softmax作为激活函数，计算比softmax快
        # 所以这里要调用一次exp函数，是ps等于softmax函数的结果，指数函数是对数函数的倒数
        ps = torch.exp(output)
        equality = (labels.data == ps.max(dim=1)[1])
        # 调用mean()后获得的就是分类正确的每一个bitch_size的正确率
        accuracy += equality.type(torch.FloatTensor).mean()

    return test_loss, accuracy


if __name__ == '__main__':
    model = Net()

    # define optimizer and err_func
    optimizer = optim.SGD(model.parameters(), lr=0.05)
    err_func = nn.CrossEntropyLoss()

    # train
    train(model, train_loader, err_func, optimizer, 5)
