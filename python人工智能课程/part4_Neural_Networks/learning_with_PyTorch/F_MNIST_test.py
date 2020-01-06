from collections import OrderedDict

import torch
import torch.nn.functional as F
from torch import nn
from python人工智能课程.part4_Neural_Networks.learning_with_PyTorch.F_MNIST_exercise import testloader


# load state
state_dic = torch.load('F_MNIST_NETWORK.pth')
model = nn.Sequential(OrderedDict([
                        ('fc1', nn.Linear(784, 128)),
                        ('Relu1', nn.ReLU()),
                        ('fc2', nn.Linear(128, 64)),
                        ('Relu2', nn.ReLU()),
                        ('digits', nn.Linear(64, 10))]))
model.load_state_dict(state_dic)


# validation
def validation(model, testloader, criterion):
    loss = 0
    accuracy = 0
    time = 0
    for images, labels in iter(testloader):
        time += 1
        images.resize_(images.size()[0], 784)

        output = F.log_softmax(model.forward(images))
        loss += criterion(output, labels).item()
        ps = torch.exp(output)
        equality = (labels.data == ps.max(dim=1)[1])
        accuracy += equality.type(torch.FloatTensor).mean()

    return loss, accuracy / time


criterion = nn.CrossEntropyLoss()
loss, accuracy = validation(model, testloader, criterion)
print(loss)
print(accuracy)