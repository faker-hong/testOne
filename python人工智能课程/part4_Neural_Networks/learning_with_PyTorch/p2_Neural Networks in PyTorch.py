import numpy as np
import torch
import python人工智能课程.part4_Neural_Networks.learning_with_PyTorch.helper as helper
import matplotlib.pyplot as plt
from torchvision import datasets, transforms
from torch import nn
import torch.nn.functional as F

# Define a transform to normalize the data
# transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)), ])
transform = transforms.Compose([
     transforms.ToTensor(),
     transforms.Lambda(lambda x: x.repeat(3, 1, 1)),
     transforms.Normalize(mean=(0.5, 0.5, 0.5), std=(0.5, 0.5, 0.5))
 ])
# Download and load the training data
train_set = datasets.MNIST('MNIST_data/', download=True, train=True, transform=transform)
# batch_size 每批图片的数量， shuffle 每个epoch之后是否重新洗牌
train_loader = torch.utils.data.DataLoader(train_set, batch_size=64, shuffle=True)

# Download and load the test data
test_set = datasets.MNIST('MNIST_data/', download=True, train=False, transform=transform)
test_loader = torch.utils.data.DataLoader(test_set, batch_size=64, shuffle=True)

# dataiter = iter(train_loader)
# images, labels = dataiter.next()
# squeeze() 去除单维度条目
# plt.imshow(images[1][1].numpy().reshape(28, 28).squeeze(), cmap='Greys_r')
# plt.show()


class Network(nn.Module):
    def __init__(self):
        super().__init__()
        # Defining the layers, 128, 64, 10 units each
        self.fc1 = nn.Linear(784, 128)
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, 10)

    def forward(self, x):
        ''' Forward pass through the network, returns the output logits '''
        x = self.fc1(x)
        x = nn.ReLU(x)
        x = self.fc2(x)
        x = nn.ReLU(x)
        x = self.fc3(x)
        x = nn.Softmax(x)

        return x


if __name__ == '__main__':
    model = Network()
    # Hyperparameters for our network
    input_size = 784
    hidden_sizes = [128, 64]
    output_size = 10
    # Build a feed-forward network
    model = nn.Sequential(nn.Linear(input_size, hidden_sizes[0]),
                          nn.ReLU(),
                          nn.Linear(hidden_sizes[0], hidden_sizes[1]),
                          nn.ReLU(),
                          nn.Linear(hidden_sizes[1], output_size),
                          nn.Softmax(dim=1))
    # Forward pass through the network and display output
    images, labels = next(iter(train_loader))
    images.resize_(images.shape[0], 1, 784)
    ps = model.forward(images[0, :])
    helper.view_classify(images[0].view(1, 28, 28), ps)
    plt.show()