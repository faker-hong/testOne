from collections import OrderedDict

import torch
import torchvision
from torchvision import datasets, transforms
from torch import nn, optim
import torch.nn.functional as F
import python人工智能课程.part4_Neural_Networks.learning_with_PyTorch.helper as helper
import matplotlib.pyplot as plt


# Define a transform to normalize the data
transform = transforms.Compose([transforms.ToTensor()])
# Download and load the training data
trainset = datasets.FashionMNIST('F_MNIST_data/', download=True, train=True, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=64, shuffle=True)

# Download and load the test data
testset = datasets.FashionMNIST('F_MNIST_data/', download=True, train=False, transform=transform)
testloader = torch.utils.data.DataLoader(testset, batch_size=64, shuffle=True)


if __name__ == '__main__':
    '''
    这里为什么用output的原始输出，而并没有调用激活函数后的结果。
    因为调用softmax后得到的是一个离散的概率分布，通常输出的值要么接近0，要么接近1.
    由于将数字表示为浮点数的不精确性，使用softmax输出的计算可能会失去准确性并变得不稳定
    '''
    # network architecture
    model = nn.Sequential(OrderedDict([
                           ('fc1', nn.Linear(784, 128)),
                           ('Relu1', nn.ReLU()),
                           ('fc2', nn.Linear(128, 64)),
                           ('Relu2', nn.ReLU()),
                           ('digits', nn.Linear(64, 10))]))

    # optimizer and criterion
    optimizer = optim.SGD(model.parameters(), lr=0.003)
    criterion = nn.CrossEntropyLoss()

    # hyper-parameter and train network
    epochs = 3
    print_every = 40
    step = 0

    for e in range(epochs):
        running_loss = 0
        for images, labels in iter(trainloader):
            step += 1
            print(images.size())
            images.resize_(images.size()[0], 784)

            optimizer.zero_grad()

            output = model.forward(images)
            loss = criterion(output, labels)
            loss.backward()
            optimizer.step()

            running_loss += loss.item()

            if step % print_every == 0:
                print("Epoch: {}/{}".format(e+1, epochs),
                      "Loss:{:.4f}".format(running_loss / print_every))

                running_loss = 0

    # test
    images, labels = next(iter(testloader))

    print(images.size())
    img = images[0]
    print(img.size())
    img = img.resize_(1, 784)
    ps = F.softmax(model.forward(img), dim=1)

    helper.view_classify(img.resize_(1, 28, 28), ps, version='Fashion')
    plt.show()

    # save model
    torch.save(model.state_dict(), 'F_MNIST_NETWORK.pth')